# /// script
# requires-python = ">=3.10"
# dependencies = ["rdflib==7.6.0", "pyshacl==0.40.1", "owlready2==0.48"]
# ///
"""运行随 Skill 分发的教学案例；不连接外部平台，不修改输入文件。"""

import hashlib
import io
import shutil
import subprocess
import unittest
from importlib.metadata import version
from pathlib import Path

import owlready2
from owlready2 import OwlReadyInconsistentOntologyError, World, sync_reasoner
from pyshacl import validate
from rdflib import Graph, Literal, Namespace, RDF, URIRef, XSD


EXAMPLES = Path(__file__).resolve().parents[1] / "examples" / "maintenance"
EX = Namespace("https://example.org/maintenance/")
REASON = Namespace("https://example.org/reasoning/")
SH = Namespace("http://www.w3.org/ns/shacl#")
PROV = Namespace("http://www.w3.org/ns/prov#")


def load(name):
    return Graph().parse(EXAMPLES / name, format="turtle")


def timestamp(day):
    return Literal(f"2026-01-{day:02d}T00:00:00Z", datatype=XSD.dateTime)


def focus_nodes(data, shapes, shape):
    # 本案例只使用 targetClass 和 targetSubjectsOf；子类闭包按 SHACL 目标语义展开。
    nodes = set()
    for target in shapes.objects(shape, SH.targetClass):
        nodes.update(row.node for row in data.query(
            "SELECT ?node WHERE { ?node a ?type . "
            "?type <http://www.w3.org/2000/01/rdf-schema#subClassOf>* ?target }",
            initBindings={"target": target},
        ))
    for predicate in shapes.objects(shape, SH.targetSubjectsOf):
        nodes.update(data.subjects(predicate, None))
    return nodes


def require_coverage(data, shapes):
    counts = {shape: len(focus_nodes(data, shapes, shape))
              for shape in (EX.TicketShape, EX.AssignmentShape)}
    if not all(counts.values()):
        raise ValueError(f"目标覆盖不足，不能把空验证当作通过：{counts}")
    return counts


def migrate_v1(legacy):
    """仅转换本例的单负责人快照；没有可信生效时间时拒绝猜测历史。"""
    result = Graph() + legacy
    candidates = set(legacy.subjects(EX.legacyOwner, None)) | set(
        legacy.subjects(EX.legacySince, None))
    recorded_at = list(legacy.objects(EX["legacy-snapshot"], PROV.generatedAtTime))
    if candidates and len(recorded_at) != 1:
        raise ValueError("迁移需要唯一的快照记录时间")
    for ticket in candidates:
        owners = list(legacy.objects(ticket, EX.legacyOwner))
        starts = list(legacy.objects(ticket, EX.legacySince))
        if len(owners) != 1 or len(starts) != 1:
            raise ValueError("旧数据需要唯一负责人和可信的生效时间；否则先补证据")
        assignment = URIRef(f"{ticket}/assignment/v1")
        if (assignment, None, None) in legacy or (None, None, assignment) in legacy:
            raise ValueError("迁移标识已被占用，先核查冲突")
        result.remove((ticket, EX.legacyOwner, None))
        result.remove((ticket, EX.legacySince, None))
        for predicate, value in (
            (RDF.type, EX.Assignment), (EX.ticket, ticket),
            (EX.assignee, owners[0]), (EX.role, Literal("Primary")),
            (EX.validFrom, starts[0]), (PROV.wasDerivedFrom, EX["legacy-snapshot"]),
            (PROV.generatedAtTime, recorded_at[0]),
        ):
            result.add((assignment, predicate, value))
    return result


class MaintenanceExample(unittest.TestCase):
    def setUp(self):
        self.data = load("data.ttl")
        self.shapes = load("shapes.ttl")
        self.query = (EXAMPLES / "assignment-at.rq").read_text(encoding="utf-8")

    def answers(self, data, day):
        # 使用列表保留重复答案，避免集合去重掩盖主负责人区间重叠。
        return sorted((str(row.ticket), str(row.owner) if row.owner else "UNKNOWN")
                      for row in data.query(self.query, initBindings={
                          "asset": EX["asset-A"], "at": timestamp(day)}))

    def assert_violation(self, node, component):
        conforms, report, details = validate(
            self.data, shacl_graph=self.shapes, inference="none")
        self.assertFalse(conforms, details)
        self.assertTrue(any(
            (result, SH.sourceConstraintComponent, component) in report
            for result in report.subjects(SH.focusNode, node)), details)

    def test_valid_data_and_target_coverage(self):
        counts = require_coverage(self.data, self.shapes)
        self.assertEqual(counts, {EX.TicketShape: 2, EX.AssignmentShape: 3})
        conforms, _, details = validate(
            self.data, shacl_graph=self.shapes, inference="none", meta_shacl=True)
        self.assertTrue(conforms, details)

    def test_empty_graph_is_not_delivery_evidence(self):
        self.assertTrue(validate(Graph(), shacl_graph=self.shapes, inference="none")[0])
        with self.assertRaises(ValueError):
            require_coverage(Graph(), self.shapes)

    def test_historical_owner(self):
        self.assertEqual(self.answers(self.data, 10), [
            (str(EX.t1), str(EX.u1)), (str(EX.t2), "UNKNOWN")])

    def test_boundary_and_current_owner_ignore_reviewer(self):
        for day in (15, 20):
            with self.subTest(day=day):
                self.assertEqual(self.answers(self.data, day), [
                    (str(EX.t1), str(EX.u2)), (str(EX.t2), "UNKNOWN")])

    def test_no_record_before_first_assignment(self):
        earlier = Literal("2025-12-31T00:00:00Z", datatype=XSD.dateTime)
        rows = list(self.data.query(self.query, initBindings={
            "asset": EX["asset-A"], "at": earlier}))
        self.assertEqual({row.ticket for row in rows}, {EX.t1, EX.t2})
        self.assertTrue(all(row.owner is None for row in rows))

    def test_source_records_are_distinct_from_person(self):
        records = set(self.data.subjects(EX.denotes, EX.u1))
        self.assertEqual(records, {EX["hr-record-17"], EX["directory-record-92"]})
        self.assertNotIn(EX.u1, records)

    def test_missing_assignee(self):
        self.data.remove((EX.a2, EX.assignee, None))
        self.assert_violation(EX.a2, SH.MinCountConstraintComponent)

    def test_multiple_assignees(self):
        self.data.add((EX.a2, EX.assignee, EX.u1))
        self.assert_violation(EX.a2, SH.MaxCountConstraintComponent)

    def test_missing_employee_type_without_inference(self):
        self.data.remove((EX.u2, RDF.type, EX.Employee))
        self.assert_violation(EX.a2, SH.ClassConstraintComponent)
        # 显式启用 range 推理会补类型；这是不同的数据契约。
        self.assertTrue(validate(self.data, shacl_graph=self.shapes,
                                 ont_graph=load("model.ttl"), inference="rdfs")[0])

    def test_missing_assignment_type_still_targeted(self):
        self.data.remove((EX.a2, RDF.type, EX.Assignment))
        self.assert_violation(EX.a2, SH.ClassConstraintComponent)

    def test_invalid_interval(self):
        self.data.set((EX.a1, EX.validTo, timestamp(1)))
        self.assert_violation(EX.a1, SH.LessThanConstraintComponent)

    def test_overlapping_primary_assignments(self):
        self.data.set((EX.a1, EX.validTo, timestamp(16)))
        self.assert_violation(EX.a1, SH.SPARQLConstraintComponent)

    def test_missing_source(self):
        self.data.remove((EX.a2, PROV.wasDerivedFrom, None))
        self.assert_violation(EX.a2, SH.MinCountConstraintComponent)

    def test_migration_preserves_answer_and_validates(self):
        legacy = load("legacy-v1.ttl")
        migrated = migrate_v1(legacy)
        old_answers = list(legacy.objects(EX.t1, EX.legacyOwner))
        self.assertEqual(old_answers, [EX.u1])
        self.assertEqual(self.answers(migrated, 10), [
            (str(EX.t1), str(old_answers[0])), (str(EX.t2), "UNKNOWN")])
        self.assertTrue(validate(migrated, shacl_graph=self.shapes, inference="none")[0])
        self.assertFalse(list(migrated.triples((None, EX.legacyOwner, None))))
        self.assertEqual(set(migrate_v1(migrated)), set(migrated))

    def test_migration_rejects_missing_history_and_ambiguous_owner(self):
        for predicate, value in ((EX.legacySince, None), (EX.legacyOwner, EX.u2)):
            with self.subTest(predicate=predicate):
                legacy = load("legacy-v1.ttl")
                if value is None:
                    legacy.remove((EX.t1, predicate, None))
                else:
                    legacy.add((EX.t1, predicate, value))
                with self.assertRaises(ValueError):
                    migrate_v1(legacy)

    def test_migration_rejects_missing_snapshot_time(self):
        legacy = load("legacy-v1.ttl")
        legacy.remove((EX["legacy-snapshot"], PROV.generatedAtTime, None))
        with self.assertRaises(ValueError):
            migrate_v1(legacy)

    def test_migration_rejects_occupied_identifier(self):
        legacy = load("legacy-v1.ttl")
        legacy.add((EX.externalRecord, EX.denotes, URIRef(f"{EX.t1}/assignment/v1")))
        with self.assertRaises(ValueError):
            migrate_v1(legacy)


class OwlReasoningExample(unittest.TestCase):
    def reason(self, graph, check):
        # 每次使用独立 World；不一致样本不能污染正常模型的推理结果。
        world = World()
        try:
            world.get_ontology(str(REASON.model)).load(
                fileobj=io.BytesIO(graph.serialize(format="xml", encoding="utf-8")))
            sync_reasoner(world, debug=0)
            check(world)
        finally:
            world.close()

    def test_classification_necessary_conditions_and_unsatisfiable_class(self):
        graph = load("reasoning.ttl")
        self.assertNotIn((REASON.classified, RDF.type, REASON.EmployeeAssignedTicket), graph)

        def check(world):
            entity = lambda name: world[str(REASON[name])]
            self.assertIn(entity("EmployeeAssignedTicket"), entity("classified").INDIRECT_is_a)
            self.assertNotIn(entity("RequiredTicket"), entity("classified").INDIRECT_is_a)
            for name in ("unclassified", "empty"):
                self.assertNotIn(entity("EmployeeAssignedTicket"), entity(name).INDIRECT_is_a)
            self.assertIn(entity("EmployeeAssignedTicket"), entity("required").INDIRECT_is_a)
            self.assertEqual(list(entity("required").assignedTo), [])
            self.assertIn(entity("ImpossibleOwner"), list(world.inconsistent_classes()))

        self.reason(graph, check)

    def test_instance_of_unsatisfiable_class_is_inconsistent(self):
        graph = load("reasoning.ttl")
        graph.add((REASON.bad, RDF.type, REASON.ImpossibleOwner))
        with self.assertRaises(OwlReadyInconsistentOntologyError):
            self.reason(graph, lambda world: None)


if __name__ == "__main__":
    if not shutil.which("java"):
        raise SystemExit("未运行：完整验证需要 Java（本案例使用 Java 17），不能跳过 OWL 后声称全通过。")
    print({package: version(package) for package in ("rdflib", "pyshacl", "owlready2")}, flush=True)
    java = subprocess.run(["java", "-version"], capture_output=True, text=True, check=True)
    print((java.stderr or java.stdout).splitlines()[0], flush=True)
    jar = Path(owlready2.__file__).parent / "hermit" / "HermiT.jar"
    print(f"HermiT jar SHA256: {hashlib.sha256(jar.read_bytes()).hexdigest()}", flush=True)
    unittest.main(verbosity=2)

import tempfile
import unittest
from pathlib import Path

from scripts.bundle_skills import ONTOLOGY, build_bundle, inventory, verify_bundle


class BundleTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "source"
        self.skill = self.root / ONTOLOGY
        self.skill.mkdir(parents=True)
        (self.skill / "SKILL.md").write_text("---\nname: ontology-modeling\ndescription: 教学方法\n---\n[参考](references/model.md)\n", encoding="utf-8")
        (self.skill / "references").mkdir()
        (self.skill / "references/model.md").write_text("# 模型\n", encoding="utf-8")
        (self.skill / "scripts").mkdir()
        (self.skill / "scripts/verify_example.py").write_text("print('example')\n", encoding="utf-8")
        self.output = Path(self.temp.name) / "output"

    def test_standalone_bundle_keeps_references_and_hashes(self):
        manifest = build_bundle(self.root, self.output, "ontology-modeling")
        self.assertEqual(verify_bundle(self.output), manifest)
        self.assertEqual((self.output / "references/model.md").read_bytes(), (self.skill / "references/model.md").read_bytes())
        self.assertEqual(manifest["skills"][0]["path"], ".")

    def test_existing_output_is_preserved(self):
        self.output.mkdir()
        marker = self.output / "keep.txt"
        marker.write_text("keep", encoding="utf-8")
        with self.assertRaises(ValueError):
            build_bundle(self.root, self.output, "ontology-modeling")
        self.assertEqual(marker.read_text(), "keep")

    def test_missing_or_external_reference_is_rejected(self):
        (self.skill / "references/model.md").write_text("[外部](../../../../../README.md)\n", encoding="utf-8")
        with self.assertRaises(ValueError):
            build_bundle(self.root, self.output, "ontology-modeling")
        self.assertFalse(self.output.exists())

    def test_tampering_and_extra_files_are_detected(self):
        build_bundle(self.root, self.output, "ontology-modeling")
        for name in ("references/model.md", "references/bundle-manifest.json"):
            with self.subTest(name=name):
                path = self.output / name
                original = path.read_bytes() if path.exists() else None
                path.write_text("changed", encoding="utf-8")
                with self.assertRaises(ValueError):
                    verify_bundle(self.output)
                if original is None:
                    path.unlink()
                else:
                    path.write_bytes(original)

    def test_output_cannot_be_nested_in_source(self):
        with self.assertRaises(ValueError):
            build_bundle(self.root, self.skill / "nested", "ontology-modeling")

    def test_symlink_is_rejected(self):
        (self.skill / "link").symlink_to(self.skill / "SKILL.md")
        with self.assertRaises(ValueError):
            build_bundle(self.root, self.output, "ontology-modeling")

    def test_inventory_declares_distribution(self):
        self.assertEqual(inventory(self.root)[0]["bundle"], "ontology-modeling")

    def test_repository_bundle_keeps_domain_evidence(self):
        domain = self.root / "domains/ontology-modeling"
        for name in ("README.md", "agent-contracts.md"):
            (domain / name).write_text("# 说明\n", encoding="utf-8")
        (domain / "capability-catalog.md").write_text("`ontology-modeling`\n", encoding="utf-8")
        (self.skill / "agents").mkdir()
        (self.skill / "agents/openai.yaml").write_text(
            'interface:\n  display_name: 本体\n  short_description: 从输入证据建立可验证的模型与决策，明确责任和后续验证行动\n  default_prompt: 使用 $ontology-modeling\n', encoding="utf-8")
        (domain / "source-materials").mkdir()
        (domain / "source-materials/original.md").write_text("# 资料\n", encoding="utf-8")
        build_bundle(self.root, self.output, "repository")
        self.assertTrue((self.output / "domains/ontology-modeling/source-materials/original.md").is_file())
        self.assertEqual(verify_bundle(self.output)["bundle"], "repository")

    def test_dangling_output_symlink_is_rejected(self):
        absent = Path(self.temp.name) / "absent"
        self.output.symlink_to(absent)
        with self.assertRaises(ValueError):
            build_bundle(self.root, self.output, "ontology-modeling")
        self.assertFalse(absent.exists())

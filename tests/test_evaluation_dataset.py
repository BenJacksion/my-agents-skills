"""仅校验评估材料的完整性；不把数据集检查当作模型行为评估。"""

import json
import unittest
from pathlib import Path

from scripts.bundle_skills import inventory


ROOT = Path(__file__).resolve().parents[1]


class EvaluationDatasetTests(unittest.TestCase):
    def test_cases_reference_existing_capabilities_and_context(self):
        cases = json.loads((ROOT / "tests/evals/cases.json").read_text(encoding="utf-8"))
        known = {item["name"] for item in inventory(ROOT)}
        self.assertEqual(len(cases), len({case["id"] for case in cases}))
        self.assertEqual({case["category"] for case in cases}, {"专项", "边界", "交接", "缺失与冲突"})
        for case in cases:
            with self.subTest(case=case["id"]):
                self.assertTrue(case["prompt"].strip())
                self.assertTrue(case["criteria"] and case["forbidden_claims"])
                self.assertTrue(set(case["acceptable_primary"]) <= known)
                self.assertTrue(set(case["required_skills"]) <= known)
                for relative in case["context"]:
                    path = (ROOT / relative).resolve()
                    self.assertTrue(path.is_relative_to(ROOT) and path.is_file())

import json
import unittest
from copy import deepcopy

from scripts.quantitative_examples import DATA, rank_candidates, run_examples, schedule


class QuantitativeExampleTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(DATA.read_text(encoding="utf-8"))

    def test_parallel_network_and_float(self):
        result = schedule(self.data["activities"])
        self.assertEqual(result["duration"], 8)
        self.assertEqual(result["activities"]["B"]["total_float"], 1)
        self.assertEqual(result["activities"]["B"]["free_float"], 1)
        self.assertEqual([name for name, item in result["activities"].items() if item["total_float"] == 0], ["A", "C", "D"])

    def test_resource_order_increases_duration(self):
        result = run_examples(self.data)
        self.assertEqual(result["shared_team_schedule"]["duration"], 11)
        self.assertEqual(result["schedule"]["duration"], 8)

    def test_invalid_networks(self):
        for mode in ("cycle", "unknown", "negative", "nan", "duplicate", "empty"):
            with self.subTest(mode=mode):
                activities = deepcopy(self.data["activities"])
                if mode == "cycle":
                    activities[0]["depends_on"] = ["D"]
                elif mode == "unknown":
                    activities[0]["depends_on"] = ["missing"]
                elif mode in ("negative", "nan"):
                    activities[0]["duration"] = -1 if mode == "negative" else float("nan")
                elif mode == "duplicate":
                    activities.append(activities[0])
                else:
                    activities = []
                with self.assertRaises(ValueError):
                    schedule(activities)

    def test_sensitivity_and_feasible_pareto(self):
        result = run_examples(self.data)
        self.assertEqual(result["simplicity_first"]["ranked"][0], {"id": "manual", "score": 80})
        self.assertEqual(result["automation_first"]["ranked"][0], {"id": "assisted", "score": 77})
        self.assertEqual(result["automation_first"]["pareto"], ["assisted", "manual"])
        self.assertNotIn("automatic", [item["id"] for item in result["automation_first"]["ranked"]])

    def test_invalid_weights_and_scores(self):
        candidates = deepcopy(self.data["candidates"])
        with self.assertRaises(ValueError):
            rank_candidates(candidates, {"simplicity": 0.5}, 10)
        candidates[0]["utility"]["simplicity"] = 101
        with self.assertRaises(ValueError):
            rank_candidates(candidates, {"simplicity": 1}, 10)

    def test_no_feasible_candidates(self):
        self.assertEqual(rank_candidates(self.data["candidates"], {"simplicity": 1}, 0), {"ranked": [], "pareto": []})

"""复算教学用项目网络与候选权衡；仅使用 Python 标准库。"""

import json
import math
from graphlib import CycleError, TopologicalSorter
from pathlib import Path


DATA = Path(__file__).resolve().parents[1] / "docs/cases/maintenance/quantitative.json"


def schedule(activities):
    """计算固定工期、完成后开始关系下的 CPM；资源顺序需显式加入依赖。"""
    tasks = {item["id"]: item for item in activities}
    if not tasks or len(tasks) != len(activities):
        raise ValueError("活动不能为空，且标识必须唯一")
    for item in activities:
        duration = item["duration"]
        if isinstance(duration, bool) or not isinstance(duration, (int, float)) or not math.isfinite(duration) or duration < 0:
            raise ValueError("工期必须是有限非负数")
        if any(predecessor not in tasks for predecessor in item["depends_on"]):
            raise ValueError("活动依赖不存在")
    try:
        order = list(TopologicalSorter({name: item["depends_on"] for name, item in tasks.items()}).static_order())
    except CycleError as exc:
        raise ValueError("活动网络存在循环依赖") from exc
    successors = {name: [] for name in tasks}
    earliest = {}
    for name in order:
        item = tasks[name]
        start = max((earliest[parent][1] for parent in item["depends_on"]), default=0)
        earliest[name] = (start, start + item["duration"])
        for parent in item["depends_on"]:
            successors[parent].append(name)
    finish = max(end for _, end in earliest.values())
    latest = {}
    for name in reversed(order):
        end = min((latest[child][0] for child in successors[name]), default=finish)
        latest[name] = (end - tasks[name]["duration"], end)
    return {
        "duration": finish,
        "activities": {name: {
            "earliest_start": earliest[name][0], "earliest_finish": earliest[name][1],
            "latest_start": latest[name][0], "latest_finish": latest[name][1],
            "total_float": latest[name][0] - earliest[name][0],
            "free_float": min((earliest[child][0] for child in successors[name]), default=finish) - earliest[name][1],
        } for name in order},
    }


def rank_candidates(candidates, weights, max_cost):
    """指标是教学用 0–100 效用分，均越高越好；先按预算过滤再评分。"""
    if not weights or any(not math.isfinite(value) or value < 0 for value in weights.values()) or not math.isclose(sum(weights.values()), 1):
        raise ValueError("权重必须有限、非负且合计为 1")
    if not math.isfinite(max_cost) or max_cost < 0:
        raise ValueError("预算必须是有限非负数")
    if len({item["id"] for item in candidates}) != len(candidates):
        raise ValueError("候选标识必须唯一")
    feasible = []
    for item in candidates:
        if not math.isfinite(item["cost"]) or item["cost"] < 0:
            raise ValueError("成本必须是有限非负数")
        if any(key not in item["utility"] for key in weights):
            raise ValueError("候选缺少指标")
        if any(not math.isfinite(item["utility"][key]) or not 0 <= item["utility"][key] <= 100 for key in weights):
            raise ValueError("效用分必须在 0–100 之间")
        if item["cost"] <= max_cost:
            feasible.append(item)
    ranked = sorted(({
        "id": item["id"],
        "score": round(sum(weights[key] * item["utility"][key] for key in weights), 6),
    } for item in feasible), key=lambda item: (-item["score"], item["id"]))

    def dominates(left, right):
        return (all(left["utility"][key] >= right["utility"][key] for key in weights)
                and any(left["utility"][key] > right["utility"][key] for key in weights))

    frontier = sorted(item["id"] for item in feasible
                      if not any(dominates(other, item) for other in feasible))
    return {"ranked": ranked, "pareto": frontier}


def run_examples(data):
    outputs = {"schedule": schedule(data["activities"])}
    serialized = [{**item, "depends_on": list(item["depends_on"])} for item in data["activities"]]
    for item in serialized:
        if item["id"] == "C":
            item["depends_on"].append("B")
    outputs["shared_team_schedule"] = schedule(serialized)
    for name, weights in data["weight_scenarios"].items():
        outputs[name] = rank_candidates(data["candidates"], weights, data["max_cost"])
    return outputs


if __name__ == "__main__":
    print(json.dumps(run_examples(json.loads(DATA.read_text(encoding="utf-8"))), ensure_ascii=False, indent=2))

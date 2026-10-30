# 可复算的项目网络与权衡

输入见 [quantitative.json](quantitative.json)，来源是自行构造的教学估算和主观效用分，不是实际工期、成本基线或风险概率。方法归属 [project-design](../../../domains/architecture-way/skills/project-design/SKILL.md) 与 [architecture-decision-optimization](../../../domains/system-architecture-product-design/skills/architecture-decision-optimization/SKILL.md)。

在仓库根目录使用 Python 3.12 运行：

```bash
python scripts/quantitative_examples.py
```

[脚本](../../../scripts/quantitative_examples.py)只有标准库依赖；相应[回归测试](../../../tests/test_quantitative_examples.py)核对数值、循环/缺失依赖、非法估算、无可行候选与权重变化。

## 项目网络

假设活动是固定工作日工期，均为完成后开始依赖；独立资源随时可用，无额外等待或日历限制。

| 活动 | 工期 | 前置 | 最早开始/结束 | 最晚开始/结束 | 总浮动/自由浮动 |
| --- | --- | --- | --- | --- | --- |
| A：身份和数据契约 | 2 | 无 | 0/2 | 0/2 | 0/0 |
| B：指派接口 | 3 | A | 2/5 | 3/6 | 1/1 |
| C：映射和历史查询 | 4 | A | 2/6 | 2/6 | 0/0 |
| D：集成验收 | 2 | B、C | 6/8 | 6/8 | 0/0 |

关键路径为 A–C–D，工期 8。若 B/C 共用同一不可并行的团队，显式加入 B→C 资源顺序，本例工期为 11。该顺序是选定方案，脚本没有求解任意资源约束最优排程；资源顺序不应伪装成业务依赖。

循环依赖和不存在的活动应报错。确定性 CPM 不计算估算不确定性、请假、返工或资源技能差异；计划承诺仍需项目负责人确认这些前提。

## 候选权衡与敏感度

教学预算上限 10；先排除成本 15 的 automatic。simplicity 与 automation 为预先给定的 0–100 效用分，均越高越好，不直接混加成本、时间与概率单位。

| 候选 | 成本 | simplicity / automation | 权重 0.8 / 0.2 | 权重 0.3 / 0.7 |
| --- | --- | --- | --- | --- |
| manual | 4 | 90 / 40 | 80 | 55 |
| assisted | 8 | 70 / 80 | 72 | 77 |
| inferior | 7 | 60 / 50 | 58 | 53 |
| automatic | 15 | 40 / 95 | 预算不满足 | 预算不满足 |

预算可行集内，按两项效用比较的帕累托前沿为 manual、assisted；成本在此只作硬约束，不是第三个优化目标。inferior 被 assisted 支配。提高 automation 权重后，首选从 manual 变为 assisted，说明推荐依赖价值偏好，不能把加权第一或帕累托非劣写成唯一最优。

真实选择需补充指标来源、效用尺度、权重责任人与不确定性。示例未实现模糊帕累托、组合搜索或概率风险估计；没有数据时保留定性风险和验证条件。

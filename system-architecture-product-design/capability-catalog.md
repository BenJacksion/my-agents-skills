# 能力目录：从原书章节到 Skills / Agents

本目录把《系统架构：复杂系统的产品设计与开发》的 16 章映射成可路由的能力单元。每个单元包含触发条件、最小输入、操作步骤、交付物、质量门槛和不适用边界，便于直接转成 Skill description、Agent system prompt 或工作流节点。

## 能力地图

| 能力 ID | 原书章节 | 解决的问题 | 推荐 Skill | 推荐 Agent |
| --- | --- | --- | --- | --- |
| ST-01 | 1-3 | 把问题识别为系统并预测涌现 | `system-thinking-emergence` | `system-explorer` |
| FA-01 | 4 | 反向分析已有系统的形式、结构和边界 | `architecture-analysis-mapping` | `architecture-analyst` |
| FA-02 | 5 | 用过程/操作数描述功能与价值通路 | `architecture-analysis-mapping` | `architecture-analyst` |
| FA-03 | 6 | 建立形式-功能映射，解释系统级行为 | `architecture-analysis-mapping` | `architecture-analyst` |
| CC-01 | 7 | 从方案中抽离功能，保持解空间开放 | `architecture-concept-development` | `concept-architect` |
| CC-02 | 8 | 从概念递归扩展到 Level N 架构 | `architecture-concept-development` | `concept-architect` |
| CC-03 | 12 | 结构化/非结构化创新与概念收敛 | `architecture-concept-development` | `concept-architect` |
| CM-01 | 3,13 | 选择分解平面、模块边界和层级 | `complexity-decomposition` | `complexity-manager` |
| CM-02 | 13 | 区分必备、实际、表面复杂度 | `complexity-decomposition` | `complexity-manager` |
| SD-01 | 9-11 | 消解歧义、识别利益相关者、设定目标 | `architecture-strategy-governance` | `architecture-governor` |
| SD-02 | 10 | 处理策略、市场、法规、供应链、平台和运营 | `architecture-strategy-governance` | `architecture-governor` |
| DO-01 | 14 | 把架构表示为决策、选项、约束和指标 | `architecture-decision-optimization` | `decision-analyst` |
| DO-02 | 15 | 分析权衡空间、帕累托前沿和敏感度 | `architecture-decision-optimization` | `decision-analyst` |
| DO-03 | 16 | 用六类模式和启发式搜索求解组合问题 | `architecture-decision-optimization` | `decision-analyst` |

## 统一数据契约

所有能力单元都接受以下最小上下文；缺失字段可为空，但必须标记为未知：

```yaml
system:
  name: ""
  boundary: ""
  lifecycle: []
stakeholders: []
value_propositions: []
requirements: []
constraints: []
existing_elements: []
decisions: []
evidence: []
uncertainties: []
```

所有能力单元都输出以下通用字段：

```yaml
facts: []
assumptions: []
models: []
decisions: []
risks: []
validation_actions: []
open_questions: []
traceability: []
```

## 路由规则

- 用户说“理解系统、涌现、整体、系统思维、故障传播”时路由到 `system-thinking-emergence`。
- 用户说“梳理现有架构、模块、接口、上下文、功能流、形式/功能”时路由到 `architecture-analysis-mapping`。
- 用户说“从需求做概念、生成多个方案、产品概念、架构演化”时路由到 `architecture-concept-development`。
- 用户说“模块化、分层、复杂度、耦合、组织边界、分解”时路由到 `complexity-decomposition`。
- 用户说“架构治理、利益相关者、战略、平台、供应链、法规、产品论证”时路由到 `architecture-strategy-governance`。
- 用户说“权衡、方案组合、帕累托、敏感度、优化、架构决策”时路由到 `architecture-decision-optimization`。
- 同时命中多个路由时，按“系统思维 -> 分析映射 -> 概念创建 -> 复杂度 -> 决策优化”顺序串联；不要跳过价值和边界。

## 质量门槛

一个能力单元只有在以下条件满足时才算完成：

1. 结论能追溯到事实、假设、模型或用户决策；
2. 明确哪些是原书原则、哪些是项目判断；
3. 给出可执行的下一步，而非只输出术语；
4. 对不可验证或高歧义部分保留不确定性；
5. 未引入超出任务范围的扩展性、平台或工具。

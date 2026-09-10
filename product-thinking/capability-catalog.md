# 能力目录：产品思维 Skills / Agents

本目录把产品思维研究中的一手来源和综合结论映射为可路由能力单元。研究依据见 [research.md](research.md)。

## 能力地图

| 能力 ID | 解决的问题 | 推荐 Skill | 推荐 Agent |
| --- | --- | --- | --- |
| PT-00 | 编排产品发现、结果、假设测试、优先级和持续迭代 | `product-thinking` | `product-thinking-lead` |
| PT-01 | 从真实用户行为、目标和情境中发现问题与机会 | `product-discovery` | `product-thinking-lead` |
| PT-02 | 将方向转为可观察结果、成功标准、基线和指标 | `product-outcomes-metrics` | `product-thinking-lead` |
| PT-03 | 拆解方案假设并设计短周期、可证伪实验 | `product-assumption-testing` | `product-thinking-lead` |
| PT-04 | 将愿景、策略、结果和资源约束转为优先级与路线图取舍 | `product-strategy-prioritization` | `product-thinking-lead` |

## 来源映射

| 方法主题 | 主要来源 |
| --- | --- |
| 问题发现、机会空间、持续访谈 | Product Talk、SVPG、GitLab |
| 结果导向、成功标准和指标 | Product Talk、GOV.UK、GitLab |
| 假设拆解、实验和验证 | Product Talk、GitLab、GOV.UK |
| 策略、团队授权、优先级和路线图 | SVPG、Intercom、GitLab |

## 统一数据契约

所有能力单元都接受以下最小上下文；缺失字段可为空，但必须标记为未知：

```yaml
product:
  name: ""
  stage: ""
  vision: ""
  strategy: ""
target_users: []
user_contexts: []
business_context: []
current_outcomes: []
constraints: []
evidence: []
assumptions: []
decisions: []
```

所有能力单元都输出以下通用字段：

```yaml
facts: []
assumptions: []
evidence: []
opportunities: []
outcomes: []
metrics: []
experiments: []
priority_decisions: []
risks: []
validation_actions: []
open_questions: []
traceability: []
```

## 路由规则

- 用户说“产品思维、产品定义、从想法到方案、产品决策、产品负责人”时，路由到 `product-thinking`。
- 用户说“用户研究、客户访谈、问题发现、机会空间、用户需求、痛点”时，路由到 `product-discovery`。
- 用户说“结果、成功标准、指标、北极星、基线、上线后怎么判断有效”时，路由到 `product-outcomes-metrics`。
- 用户说“假设、实验、MVP、原型验证、可用性测试、验证方案”时，路由到 `product-assumption-testing`。
- 用户说“产品策略、优先级、路线图、RICE、取舍、资源分配”时，路由到 `product-strategy-prioritization`。
- 同时命中多个路由时，按“发现问题 -> 定义结果 -> 拆解假设 -> 设计实验 -> 决定优先级”串联。

## 质量门槛

1. 结论能追溯到用户证据、行为数据、业务约束或明确假设；
2. 区分用户问题、机会、方案、产出和结果；
3. 不把单条反馈、内部偏好或评分模型当成最终优先级；
4. 每个高风险假设都有可执行验证行动；
5. 输出包含下一步取舍或学习动作，而不是只给概念名词。

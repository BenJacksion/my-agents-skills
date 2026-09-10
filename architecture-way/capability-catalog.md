# 能力目录：《架构之道：软件构建的设计方法》Skills / Agents

本目录把 *Righting Software* 的公开资料和研究结论映射为最小能力集合。证据与来源见 [research.md](research.md)。

## 能力地图

| 能力 ID | 解决的问题 | 推荐 Skill | 推荐 Agent |
| --- | --- | --- | --- |
| AW-00 | 编排系统设计、可组合性、验证和项目设计 | `architecture-way` | `architecture-way-lead` |
| AW-01 | 识别易变性并据此建立系统结构、层和服务边界 | `volatility-decomposition` | `architecture-way-lead` |
| AW-02 | 设计可组合的系统、服务和契约，降低变化传播与重复实现 | `composable-architecture` | `architecture-way-lead` |
| AW-03 | 验证系统设计、契约、关键路径和项目设计是否闭合 | `architecture-validation` | `architecture-way-lead` |
| AW-04 | 从系统设计推导网络计划、时间/成本/风险和执行选项 | `project-design` | `architecture-way-lead` |

## 来源映射

| 主题 | 主要章节或公开资料 | 能力 |
| --- | --- | --- |
| The Method、系统设计与项目设计的连接 | 第 1、5-7、14 章；官方书籍介绍 | `architecture-way` |
| 避免功能分解、按易变性分解、结构和服务 | 第 2-3 章；软件系统分解样章 | `volatility-decomposition` |
| 可组合设计、变化处理、服务契约 | 第 4 章、附录 B-C | `composable-architecture` |
| 系统设计验证、设计标准、项目设计评审 | 第 5、11、14 章；官方设计标准文章 | `architecture-validation` |
| 网络、浮动时间、时间/成本、风险、跟踪 | 第 7-14 章、附录 A；风险计算样章与官方视频 | `project-design` |
| 系统设计与详细设计边界、代表性垂直切片、核心团队和执行反馈 | 第 5-14 章；官方方法与培训材料 | `architecture-validation`、`project-design`、`architecture-way` |

## 路由规则

- 用户说“架构之道、Righting Software、The Method、系统设计和项目设计”时，路由到 `architecture-way`。
- 用户说“按易变性分解、组件边界、服务边界、功能分解、结构、分层”时，路由到 `volatility-decomposition`。
- 用户说“可组合设计、变化局部化、服务契约、契约分解、复用、组合行为”时，路由到 `composable-architecture`。
- 用户说“架构验证、设计评审、契约评审、端到端验证、架构是否闭合”时，路由到 `architecture-validation`。
- 用户说“项目设计、关键路径、网络计划、浮动时间、时间成本风险、压缩计划、项目选项、挣值、项目跟踪”时，路由到 `project-design`。
- 同时命中多个路由时，按“分解 -> 可组合性 -> 验证 -> 项目设计”组织；若系统结构已确定，可跳过前面的节点。

## 研究主题覆盖说明

研究中的系统设计/详细设计边界、代表性垂直切片、核心团队和执行反馈已由现有能力承载：

- 系统设计与详细设计边界：`architecture-way` 和 `architecture-validation`，作为交付粒度、验证边界和回退条件；
- 垂直切片：`architecture-validation`，作为最小端到端验证活动，并进入项目网络；
- 核心团队：`project-design`，作为活动责任、技能约束、资源可用性和并行条件；
- 执行反馈：`project-design` 和 `architecture-way`，作为剩余工作、预测、风险和架构复审输入。

这些主题不新增独立 Skill，避免把同一条系统设计与项目设计方法拆成重复节点。

## 统一数据契约

所有能力单元接受以下最小上下文；缺失字段保留为空并标记为未知：

```yaml
architecture_way:
  task: ""
  system: ""
  goals: []
  stakeholders: []
  requirements: []
  constraints: []
  volatility_signals: []
  existing_structure: []
  services: []
  contracts: []
  activities: []
  dependencies: []
  estimates: []
  project_options: []
  evidence: []
  assumptions: []
  decisions: []
  risks: []
  validations: []
  feedback: []
  open_questions: []
```

所有能力单元输出以下通用字段，按任务需要填充：

```yaml
facts: []
assumptions: []
evidence: []
decisions: []
architecture: []
contracts: []
project_network: []
options: []
risks: []
validation_actions: []
feedback_actions: []
open_questions: []
traceability: []
```

## 质量门槛

1. 结论能追溯到书籍公开资料、用户材料、项目数据或明确假设。
2. 清楚区分系统设计判断、项目设计计算和最终管理决策。
3. 组件边界说明变化来源、变化传播、契约成本和验证边界。
4. 项目选项同时说明时间、成本、风险和成功条件，不只给单一工期。
5. 模型输入、估算置信度、未知项和复审触发条件透明。
6. 不把“微服务”“敏捷”“云”或某种技术栈当成书中默认答案。

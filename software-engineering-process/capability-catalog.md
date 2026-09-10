# 软件工程流程能力目录

本目录把仓库现有的 24 个 Skills 和 13 个 Agents 映射到软件工程生命周期。它是路由表，不复制各能力域的详细方法。

## 阶段与 Skills

| 阶段 | 推荐 Skills | 主要产物 |
| --- | --- | --- |
| S0 任务受理 | `software-engineering-process` | 问题分类、当前阶段、范围、决策人和成功标准 |
| S1 产品发现与决策 | `product-thinking`、`product-discovery`、`product-outcomes-metrics`、`product-assumption-testing`、`product-strategy-prioritization` | 用户问题、机会、结果、假设、实验和优先级 |
| S2 系统理解与治理 | `system-thinking-emergence`、`architecture-analysis-mapping`、`architecture-strategy-governance` | 系统边界、实体关系、利益相关者、价值、约束和现状映射 |
| S3 系统概念与架构决策 | `complex-system-architecture`、`architecture-concept-development`、`complexity-decomposition`、`architecture-decision-optimization` | 无关方案功能、多个概念、复杂度账本、决策和权衡空间 |
| S4 企业应用架构 | `enterprise-application-architecture`、`domain-application-modeling`、`application-five-views`、`evolutionary-architecture-modernization` | 用例、领域、数据、开发、运行、物理五视图、目标/过渡架构 |
| S4 分布式与平台专项 | `distributed-application-architecture`、`cloud-native-delivery`、`data-platform-architecture` | 分布式机制、云交付、数据平台和治理方案 |
| S5 软件结构与项目设计 | `architecture-way`、`volatility-decomposition`、`composable-architecture`、`project-design` | 易变性边界、服务契约、项目网络、关键路径、时间/成本/风险选项 |
| S5/S7 架构验证 | `architecture-validation` | 关键行为、契约、质量属性、架构和项目设计的验证证据 |
| S7/S8 结果与反馈 | `product-outcomes-metrics`、`product-assumption-testing`、`evolutionary-architecture-modernization`、`project-design` | 发布结果、实验反馈、剩余风险、架构复审和下一轮计划 |

所有现有 Skill 的覆盖情况：

- 产品思维：5 个，覆盖 S1、S7、S8；
- 系统架构：7 个，覆盖 S2、S3；
- 《架构之道：软件构建的设计方法》：5 个，覆盖 S5、S7、S8；
- 企业应用架构：7 个，覆盖 S4、S7、S8；
- 流程编排：1 个，负责 S0 和跨阶段路由。

## 阶段与 Agents

| Agent | 所属能力域 | 生命周期责任 |
| --- | --- | --- |
| `software-engineering-orchestrator` | 项目级流程 | 识别阶段、编排主 Agent、维护跨阶段状态和回退 |
| `product-thinking-lead` | 产品思维 | S1 产品发现、结果、实验和优先级 |
| `system-architecture-orchestrator` | 系统架构 | S2-S3 系统理解、概念、分解和决策 |
| `system-explorer` | 系统架构 | S2 实体、关系、边界、涌现和失效 |
| `architecture-governor` | 系统架构 | S2 利益相关者、约束、目标和治理 |
| `architecture-analyst` | 系统架构 | S2 既有系统形式、功能、接口和映射 |
| `complex-system-architect` | 系统架构 | S3 系统级架构综合和质量门 |
| `concept-architect` | 系统架构 | S3 候选概念和多层架构 |
| `complexity-manager` | 系统架构 | S3 复杂度、分解平面和模块边界 |
| `decision-analyst` | 系统架构 | S3 决策、权衡、敏感度和优化 |
| `enterprise-application-architect` | 企业应用架构 | S4 企业应用架构总编排 |
| `application-design-architect` | 企业应用架构 | S4 用例、领域、数据和五视图 |
| `distributed-data-architect` | 企业应用架构 | S4 分布式、云交付和数据平台 |
| `architecture-way-lead` | 《架构之道：软件构建的设计方法》 | S5 软件结构、组合、验证和项目设计 |

## 路由规则

1. 用户描述用户、客户、机会、指标、MVP 或路线图：进入 S1。
2. 用户描述系统边界、实体关系、利益相关者、涌现或现有系统：进入 S2。
3. 用户要求生成多个方案、分解系统、分析复杂度或比较架构：进入 S3。
4. 用户要求用例、DDD、五视图、分层、遗留系统、微服务、云或数据平台：进入 S4。
5. 用户要求服务边界、易变性、契约、关键路径、排期、成本或风险：进入 S5。
6. 用户要求架构评审、端到端验证、发布判断或结果复盘：进入 S7/S8。
7. 如果问题跨越多个阶段，由 `software-engineering-orchestrator` 选择一个主阶段，其他阶段只提供必要输入，不并行生成完整方案。

## 非覆盖范围

本仓库目前没有独立的编码实现、测试工程、发布工程和生产运维 Skills/Agents。S6 的代码、测试、集成和生产变更由实际工程团队执行；本流程层只提供：

- 可实现的架构约束；
- 可追溯的项目活动；
- 验证场景和通过条件；
- 发布风险和复审触发器。

这是一项覆盖说明，不是待办占位；后续只有在存在稳定方法来源和真实使用需求时，才新增对应能力。

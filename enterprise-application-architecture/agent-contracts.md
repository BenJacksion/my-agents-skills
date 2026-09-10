# Agent 契约与编排细则

本文件定义本能力域的共享状态、Agent 分工、交接条件和回退规则。Agent 必须同时输出结构化结果和中文解释；下游不得把上游假设直接升级为事实。

## 共享状态

```yaml
EnterpriseApplicationState:
  task:
    question: string
    scope: string
    decision_deadline: string|null
  facts: []
  assumptions: []
  ambiguities: []
  stakeholders: []
  goals: []
  use_cases: []
  domain_model: []
  data_model: []
  logical_architecture: []
  development_architecture: []
  runtime_architecture: []
  physical_architecture: []
  quality_attribute_scenarios: []
  interface_contracts: []
  database_decisions: []
  platform_evaluation: []
  physical_topology: []
  data_lineage: []
  distributed_options: []
  cloud_options: []
  data_platform_options: []
  existing_architecture: []
  target_architecture: []
  transition_architecture: []
  decisions: []
  evidence: []
  risks: []
  validations: []
  evolution_actions: []
  open_questions: []
  traceability: []
```

每个条目尽量包含 `id`、`description`、`source`、`confidence` 和 `status`。`source` 可以是用户材料、代码/文档、运行数据、研究文件、实验或专家判断。

## Agent 分工

- `enterprise-application-architect`：判断任务范围，编排领域、5 视图、演进、分布式、云和数据平台能力，维护总体架构闭合。
- `application-design-architect`：负责用例、领域模型、数据责任、5 视图和遗留演进，输出应用内部结构及跨视图问题。
- `distributed-data-architect`：负责分布式、微服务、云交付和数据平台，输出机制选择、运行约束、部署和数据闭环。

不让两个 Agent 各自生成完整架构。总架构师维护唯一决策记录，专项 Agent 只在自己的边界内提供候选、证据和风险。

领域建模 Agent 还必须区分新增功能和结构重构：新增功能优先保证行为正确，重构应以小步方式进行，并由测试、编译或可运行验证保护。

## 推荐编排

新应用：

```text
enterprise-application-architect
  -> application-design-architect
  -> distributed-data-architect（需要时）
  -> enterprise-application-architect（跨视图复审）
```

遗留系统：

```text
enterprise-application-architect
  -> application-design-architect（当前 5 视图与断裂）
  -> distributed-data-architect（运行/部署/数据风险）
  -> application-design-architect（目标与过渡结构）
  -> enterprise-application-architect（演进决策）
```

## 交接条件

### 领域建模 -> 5 视图

- 用例、关键领域概念和边界已经标记；
- 数据责任、关键状态和主要交互可追溯；
- 对外接口的语义、稳定性边界和 DTO/领域对象关系已记录；
- 领域模型到聚合、存储模型、读写模型和数据流转的映射已记录；
- 候选架构仍区分事实、假设和决策。

### 5 视图 -> 分布式/云/数据平台

- 关键逻辑职责和数据所有权已明确；
- 质量属性场景至少列出触发条件、响应和度量；
- 已知的运行、部署、数据规模和组织约束已记录；
- 物理拓扑、故障域、容量与容灾约束已记录；
- 关键数据链路、消费者、指标/标签和数据 API 已有责任归属；
- 没有因为“微服务”“云”或“中台”这些名词直接锁定方案。

### 属性/场景 -> 运行决策

- 非功能属性已转成具体场景，包含触发条件、环境、响应、度量和失败阈值；
- 每个运行机制都说明保护对象、失效模式、恢复方式和运维责任；
- 限流、熔断、降级、幂等和最终一致性没有被当作互相替代的同义词。

### 专项架构 -> 总架构

- 每个技术机制说明解决的约束、引入的复杂度和验证方式；
- 关键跨视图冲突已显式列出；
- 接口契约、数据库/存储决策、技术中台判断、物理拓扑和数据血缘没有脱离总体架构单独存在；
- 结论包含推荐、替代方案、放弃理由和复审条件。

### 企业应用架构 -> 软件结构与项目设计

- 领域、模块和服务责任已区分，不能把逻辑边界直接当成部署单元；
- 对外接口契约、内部依赖方向和数据所有权已可交给 `architecture-way`；
- 数据库/存储决策已说明访问模式、一致性边界、迁移影响和回滚方式；
- 技术中台、采购、自研或外包判断已说明复用收益、退出成本和维护责任；
- 物理拓扑、容量、容灾、数据 API 和关键验证活动已经可以转换为项目活动和依赖。

## 失败与回退

- 业务目标或系统边界不清：回退 `system-architecture-product-design/`。
- 用例和领域责任不清：回退 `domain-application-modeling`，不直接拆微服务。
- 视图之间冲突：回退 `application-five-views`，建立冲突登记和追溯关系。
- 质量目标只有形容词：回退 `evolutionary-architecture-modernization`，改写为质量属性场景。
- 分布式机制无法说明收益：回退 `distributed-application-architecture`，先比较集中式、分布式和渐进式候选。
- 平台范围大于数据消费者和治理责任：回退 `data-platform-architecture`，缩小为可交付数据产品或数据链路。
- 把大数据平台直接称为数据中台：回退 `data-platform-architecture`，先补数据标准、质量、主数据、指标和服务责任。
- 项目网络、关键路径、时间/成本/风险成为主问题：交给 `architecture-way` 的 `project-design`。

## 最小完成标准

1. 用例、领域、数据和关键架构决策可以互相追溯。
2. 5 个视图的主要职责、约束和冲突可解释。
3. 关键质量属性有运行/物理承载方式和验证行动。
4. 分布式、云和数据平台只在证据支持时采用。
5. 演进方案包含当前、目标、过渡结构和复审条件。
6. 未知项有责任人、证据来源或下一步验证行动。

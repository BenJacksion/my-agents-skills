# 能力目录：《架构真意》Skills / Agents

本目录把《架构真意》的公开目录和内容线索映射为最小可路由能力。研究依据见 [research.md](research.md)。

## 能力地图

| 能力 ID | 解决的问题 | 推荐 Skill | 推荐 Agent |
| --- | --- | --- | --- |
| EAA-00 | 编排企业应用从领域到部署、分布式和数据平台的架构闭合 | `enterprise-application-architecture` | `enterprise-application-architect` |
| EAA-01 | 用 5 视图并行深化逻辑、数据、开发、运行和物理架构，并检查跨视图一致性 | `application-five-views` | `application-design-architect` |
| EAA-02 | 从用例、领域模型、聚合和数据责任形成可演化的应用内部结构 | `domain-application-modeling` | `application-design-architect` |
| EAA-03 | 用属性、场景、决策处理非功能需求、目标架构、过渡架构和遗留系统重构 | `evolutionary-architecture-modernization` | `application-design-architect` |
| EAA-04 | 按规模和场景判断缓存、事务、消息、限流、熔断、降级、幂等、分布式数据库和微服务 | `distributed-application-architecture` | `distributed-data-architect` |
| EAA-05 | 把部署、容器、DevOps、Kubernetes、可观测性和自动化运维纳入架构设计 | `cloud-native-delivery` | `distributed-data-architect` |
| EAA-06 | 区分大数据平台与数据中台，设计从采集、治理、加工到数据服务和分析的闭环 | `data-platform-architecture` | `distributed-data-architect` |

## 章节主题到执行能力

以下矩阵以 [research.md](research.md) 的公开研究和
[chapter-notes.md](chapter-notes.md) 的用户补充笔记为准，检查每个章节主题是否已经进入
Skill、Agent 和可交接产物。笔记中的书中结论仍属于用户提供的阅读材料，不自动视为外部一手证据。

| 章节主题 | Skill | Agent | 必须形成的产物 |
| --- | --- | --- | --- |
| 第 1 章：架构师职责、业务/技术翻译、抽象、分治、成本与演进、五视图 | `enterprise-application-architecture`、`application-five-views` | `enterprise-application-architect` | 事实/假设/未知、决策人、成功标准、五视图基线和追溯关系 |
| 第 2 章：Actor、Use Case、System Boundary、原型、事件流、领域模型与技术可行性 | `domain-application-modeling` | `application-design-architect` | 用例表、主成功场景/扩展场景、领域概念、状态、不变量和可行性约束 |
| 第 3 章：领域优先、聚合、实体/值对象/领域服务、仓库/工厂、防腐层、关系/继承/NoSQL、读写模型 | `domain-application-modeling`、`distributed-application-architecture` | `application-design-architect`、`distributed-data-architect` | 领域到存储追溯、数据所有权、存储访问模式、聚合一致性边界和读写模型 |
| 第 4 章：接口语义、DTO 与领域对象、分层/整洁架构、模块、技术选型、平台/采购/自研/外包 | `domain-application-modeling`、`application-five-views` | `application-design-architect`、`enterprise-application-architect` | 接口契约、依赖方向、模块责任、技术选型记录和技术中台评估 |
| 第 5 章：属性→场景→决策、意图架构、架构跑道、使能故事、遗留改造 | `evolutionary-architecture-modernization` | `application-design-architect` | 质量属性场景、当前/目标/过渡架构、使能故事、回滚点和复审触发器 |
| 第 6 章：集中式/分布式、网络拓扑、DMZ、负载均衡、可用区、容量与容灾 | `application-five-views`、`distributed-application-architecture`、`cloud-native-delivery` | `distributed-data-architect` | 物理拓扑、故障域、容量模型、恢复目标、切换路径和部署责任 |
| 第 7 章：按规模演进、缓存、内存数据库、事务、队列、分布式数据库 | `distributed-application-architecture` | `distributed-data-architect` | 负载/故障/一致性模型、机制收益与代价、失效模式、指标和验证场景 |
| 第 8 章：微服务前提、统一语言、子域、限界上下文、治理、测试和调优 | `domain-application-modeling`、`distributed-application-architecture` | `application-design-architect`、`distributed-data-architect` | 服务责任、数据所有权、边界理由、治理能力、测试策略和迁移顺序 |
| 第 9 章：DevOps、容器、Kubernetes、有状态组件、自动化运维 | `cloud-native-delivery` | `distributed-data-architect` | 交付流水线、状态/配置/权限、拓扑、扩缩容、备份恢复、回滚和成本责任 |
| 第 10-11 章：数据驱动业务、采集、治理、标准、质量、主数据、指标、标签、索引、数仓与数据服务 | `data-platform-architecture` | `distributed-data-architect` | 业务域→指标域→数据模型→数据 API、血缘、责任、质量指标和数据产品 |

## 能力覆盖说明

当前 7 个企业应用 Skill 已覆盖研究中的五视图、领域/数据、开发、运行/演进、物理、分布式/微服务、云交付和数据平台主题。
其中“架构师能力模型”“接口设计细则”“数据库映射策略”“技术中台评估”“物理拓扑细节”和“数据链路追溯”
不是新建微技能，而是作为输入、输出和质量门嵌入现有 Skill/Agent。

## 路由规则

- 用户说“架构真意、企业级应用架构、5 视图、五视图”时，路由到 `enterprise-application-architecture` 或 `application-five-views`。
- 用户说“用例、领域模型、DDD、分层架构、整洁架构、数据责任”时，路由到 `domain-application-modeling`。
- 用户说“非功能需求、质量属性、架构演进、目标架构、遗留重构、架构跑道、使能改造”时，路由到 `evolutionary-architecture-modernization`。
- 用户说“高并发、缓存、事务、消息队列、分布式数据库、微服务、事件风暴”时，路由到 `distributed-application-architecture`。
- 用户说“云部署、DevOps、Docker、Kubernetes、自动化运维”时，路由到 `cloud-native-delivery`。
- 用户说“数据中台、数据采集、数据治理、ETL、数据仓库、标签、索引、多维分析、HBase”时，路由到 `data-platform-architecture`。
- 同时命中多个路由时，按“领域与 5 视图 -> 质量属性与演进 -> 分布式/云 -> 数据平台 -> 场景验证”组织；已有系统优先补当前架构和断裂，不从技术名词倒推目标。
- 用户明确要求逐章阅读或需要书籍细节时，先读取 [chapter-notes.md](chapter-notes.md)，再按当前任务选择 Skill；不要把逐章笔记全部复制进每次输出。

## 统一数据契约

所有能力单元接受以下最小上下文，缺失字段必须标记为未知：

```yaml
enterprise_application:
  task: ""
  business_context: []
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
  existing_architecture: []
  target_architecture: []
  transition_architecture: []
  constraints: []
  evidence: []
  assumptions: []
  decisions: []
  risks: []
  validations: []
  open_questions: []
```

输出按任务需要填充：

```yaml
facts: []
assumptions: []
evidence: []
architecture_views: []
interface_contracts: []
database_decisions: []
platform_evaluation: []
physical_topology: []
data_lineage: []
decisions: []
tradeoffs: []
risks: []
validation_actions: []
evolution_actions: []
open_questions: []
traceability: []
```

## 质量门槛

1. 业务目标和用例能追溯到逻辑职责、数据责任和关键架构决策。
2. 5 个视图之间没有未解释的冲突，或冲突已登记为风险和验证行动。
3. 非功能需求写成有触发条件、响应和测量方式的场景。
4. 分布式、云和平台化选择有负载、故障、团队、成本或交付证据支持。
5. 遗留改造区分当前、目标、过渡结构和可停止的阶段。
6. 数据平台明确数据消费者、所有者、质量、时效、治理和服务方式。
7. 结论区分原始事实、用户输入、工程推断、估算和待决问题。

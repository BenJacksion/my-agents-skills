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

## 来源映射

| 公开主题 | 能力 |
| --- | --- |
| 5 视图法、逻辑/数据/开发/运行/物理架构 | `application-five-views` |
| 用例、UI 原型、领域模型、分层和整洁架构 | `domain-application-modeling` |
| 非功能需求、架构演进、遗留系统重构 | `evolutionary-architecture-modernization` |
| 访问量、缓存、内存数据库、事务、消息队列、分布式数据库 | `distributed-application-architecture` |
| 微服务、DDD、事件风暴、服务化和测试 | `distributed-application-architecture` |
| 云计算、DevOps、Docker、Kubernetes、自动化运维 | `cloud-native-delivery` |
| 数据中台、Hadoop、Spark、采集、治理、ETL、数仓、标签、索引、多维分析、HBase | `data-platform-architecture` |

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

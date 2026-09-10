# 软件工程流程 Agent 契约

本文件定义项目级总编排 Agent 如何协调四个能力域。它不替代各能力域的 `agent-contracts.md`，下游结果必须遵守原能力域契约。

## 共享状态

```yaml
SoftwareEngineeringState:
  task:
    question: string
    scope: string
    lifecycle_stage: string
    decision_deadline: string|null
  facts: []
  assumptions: []
  evidence: []
  stakeholders: []
  goals: []
  requirements: []
  opportunities: []
  outcomes: []
  experiments: []
  system_context: []
  concepts: []
  architecture_decisions: []
  application_views: []
  services: []
  contracts: []
  project_network: []
  implementation_changes: []
  validation_evidence: []
  release_decision: []
  operational_feedback: []
  risks: []
  open_questions: []
  traceability: []
```

每个条目尽量包含 `id`、`description`、`source`、`confidence`、`status` 和 `owner`。`source` 必须区分用户输入、代码/运行数据、研究资料、计算结果、实验结果和专家判断。

## 主流程

```text
S0 受理与分阶段
  -> S1 产品发现与决策
  -> S2 系统理解与治理
  -> S3 概念、复杂度与系统架构
  -> S4 企业应用架构
  -> S5 软件结构与项目设计
  -> S6 实现与集成
  -> S7 验证与发布
  -> S8 运行反馈与演进
  -> S1/S2/S4/S5（按反馈回退）
```

默认按顺序推进，但以下情况允许跳过：

- 既有系统且产品目标明确：可以从 S2 开始；
- 架构已稳定、只需排期：可以从 S5 开始；
- 只验证已知架构：可以从 S7 开始；
- 只做运行复盘：从 S8 开始，但必须补齐对上游假设的影响。

## 每阶段协议

### S0：任务受理与分阶段

主 Agent：

- `software-engineering-orchestrator`

必须输出：

- 用户真正要解决的问题；
- 当前已知生命周期阶段；
- 成功标准、范围、决策人和截止时间；
- 缺失信息中会改变路由的部分；
- 推荐主 Agent 和下一阶段。

### S1：产品发现与决策

主 Agent：

- `product-thinking-lead`

调用顺序：

```text
product-discovery
  -> product-outcomes-metrics
  -> product-assumption-testing
  -> product-strategy-prioritization
```

通过条件：

- 问题来自用户行为、情境或可追溯证据；
- 结果可观察且团队可影响；
- 高风险假设有验证方式；
- 取舍包含做与不做的机会成本。

### S2：系统理解与治理

主 Agent：

- `system-architecture-orchestrator`

专项 Agent：

- `system-explorer`
- `architecture-governor`
- `architecture-analyst`

通过条件：

- 系统边界、环境、实体、关系和伴生系统明确；
- 利益相关者、价值交换、需求和约束可追溯；
- 既有系统有形式、功能、接口和映射基线；
- 涌现行为和故障传播不被局部组件假设替代。

### S3：概念、复杂度与系统架构

主 Agent：

- `system-architecture-orchestrator`
- `complex-system-architect`

专项 Agent：

- `concept-architect`
- `complexity-manager`
- `decision-analyst`

通过条件：

- 保留多个真正不同的候选概念；
- 功能与具体方案已经分离；
- 分解平面、复杂度和接口代价已比较；
- 高敏感、高耦合决策有依据、权衡和验证条件；
- 形成系统架构基线，而非只有技术清单。

### S4：企业应用架构

主 Agent：

- `enterprise-application-architect`

专项 Agent：

- `application-design-architect`
- `distributed-data-architect`

通过条件：

- 用例、领域、数据责任和应用边界明确；
- 逻辑、数据、开发、运行、物理五视图相互可解释；
- 非功能需求转成场景、决策和度量；
- 分布式、云、微服务和数据平台有约束证据；
- 当前、目标和过渡架构可追踪。

### S5：软件结构与项目设计

主 Agent：

- `architecture-way-lead`

必须完成：

- 按易变性形成软件边界；
- 检查服务组合、契约、共享状态和变化传播；
- 从架构和验证活动建立项目网络；
- 比较时间、成本、风险和资源不同的执行选项。

通过条件：

- 组件/服务边界能追溯到变化、职责或验证；
- 关键契约和组合场景已列出；
- 活动、依赖、关键路径和资源假设可复核；
- 至少有一个推荐方案和一个有明确取舍的替代方案。

### S6：实现与集成

责任主体：

- 实际开发、测试和集成团队。

流程层输出：

- 架构约束；
- 代码/模块/接口交付物；
- 集成依赖；
- 验证入口；
- 变更记录和未解决风险。

流程层不把架构文档当作代码完成，也不把本项目现有 Agent 伪装成实施团队。

### S7：验证与发布

主 Agent：

- `architecture-way-lead`
- `product-thinking-lead`

调用能力：

- `architecture-validation`
- `product-assumption-testing`
- `product-outcomes-metrics`

通过条件：

- 关键用例、质量属性、服务契约、数据链路和故障场景有证据；
- 未通过项有责任人、风险和发布处理；
- 发布决策说明时间、成本、风险、质量和用户结果；
- 结果基线已建立。

### S8：运行反馈与演进

主 Agent：

- `software-engineering-orchestrator`

协作 Agent：

- `product-thinking-lead`
- `system-architecture-orchestrator`
- `enterprise-application-architect`
- `architecture-way-lead`

必须判断：

- 实际用户/业务结果是否支持原目标；
- 运行数据是否推翻质量属性或容量假设；
- 项目预测是否需要修正；
- 哪个最小范围需要回退；
- 下一轮进入 S1、S2、S4 还是 S5。

## 禁止事项

- 不让多个总控 Agent 并行生成互相竞争的完整方案；
- 不把上游假设直接升级为下游事实；
- 不从技术名词直接跳到微服务、云、数据中台或分布式数据库；
- 不用架构图、评分、排期或文档数量替代运行证据；
- 不将 S6 的编码、测试和生产操作归入本项目已有能力的完成范围。

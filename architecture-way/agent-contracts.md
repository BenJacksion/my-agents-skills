# Agent 契约与编排细则

本文件定义 `architecture-way-lead` 的共享状态、执行边界和交接规则。Agent 必须同时输出结构化结果和 Markdown 解释，下游不得把上游假设直接升级为事实。

## 共享状态对象

```yaml
ArchitectureWayState:
  task:
    question: string
    scope: string
    decision_deadline: string|null
  facts: []
  assumptions: []
  ambiguities: []
  stakeholders: []
  goals: []
  requirements: []
  constraints: []
  volatility_signals: []
  structure: []
  services: []
  contracts: []
  composition_scenarios: []
  activities: []
  dependencies: []
  estimates: []
  project_network: []
  project_options: []
  decisions: []
  evidence: []
  risks: []
  validations: []
  feedback: []
  open_questions: []
  traceability: []
```

每个对象尽量包含 `id`、`description`、`source`、`confidence` 和 `status`。`source` 可以是用户材料、代码/文档、项目数据、研究文件、计算模型、实验或专家判断。

## Agent 输入输出

### `architecture-way-lead`

- 输入：系统目标、需求、约束、现有架构、变化来源、服务或组件候选、项目活动、依赖、人员、工期/成本估算、风险、决策期限和已有项目数据。
- 必须完成：识别当前模式；在需要时进行易变性分解、可组合性检查、架构验证和项目设计；比较多个可行执行选项；输出决策、风险和反馈动作。
- 输出字段：`facts`、`assumptions`、`evidence`、`structure`、`services`、`contracts`、`project_network`、`project_options`、`decisions`、`risks`、`validations`、`feedback`、`open_questions`、`traceability`。
- 不负责：替用户虚构业务目标或权重；替实现团队完成详细编码；把模型计算当成自动裁决；把本书方法包装成适用于所有组织的唯一流程。

## 推荐编排图

```text
系统目标、约束和变化来源
              |
              v
      volatility-decomposition
              |
              v
      composable-architecture
              |
              v
      architecture-validation
              |
              v
         project-design
              |
              v
     执行、跟踪、反馈和复审
```

默认链路可以按证据和任务范围裁剪。已有稳定架构可从验证或项目设计开始；仅做服务边界诊断时不必生成项目计划。

## 交接条件

### 分解 -> 可组合性

- 变化来源和易变性判断已经记录；
- 每个边界有变化局部化、依赖和接口理由；
- 还未把分解方案误写成已批准的详细实现。

### 可组合性 -> 验证

- 关键服务、组合场景和契约已经列出；
- 已知的变化传播、共享状态、重复实现和跨边界副作用可追踪；
- 至少有需要验证的关键行为或质量属性。

### 验证 -> 项目设计

- 架构基线、关键契约和验证结果已经形成；
- 未通过项有风险、责任人、修复或复审条件；
- 项目活动可以从架构交付物和验证活动中识别，而不是凭空估工。

### 项目设计 -> 执行与反馈

- 网络、关键路径、浮动时间、资源假设、成本和风险已披露；
- 至少保留一个正常方案和一个有明确取舍的替代方案，除非约束证明只有一个可行解；
- 规定进度、成本、风险或质量信号变化时的纠偏和复审动作。

## 失败与回退

- **目标或边界不清**：回退到现有的 `system-architecture-product-design` 能力，先补系统上下文和目标，不直接切服务。
- **分解主要按功能或组织切分**：回退 `volatility-decomposition`，补充变化来源和跨边界组合场景。
- **组件局部看似简单但组合困难**：回退 `composable-architecture`，检查契约语义、共享状态、异常、顺序和变化传播。
- **架构图完整但关键行为没有证据**：回退 `architecture-validation`，设计最小可执行验证。
- **项目只有一个工期数字**：回退 `project-design`，补网络、资源、时间/成本曲线和风险选项。
- **计划与实际反馈偏离**：进入 `project-design` 的跟踪与预测模式，修正剩余工作、关键路径和选项，不掩盖原估算误差。

## Agent 验收问题

1. 是否把系统设计和项目设计放在同一个决策链中？
2. 是否说明边界来自哪些变化，以及变化如何传播？
3. 是否能说明服务为何可组合，而不只是列出组件名？
4. 是否验证了关键交互、契约和系统级行为？
5. 是否提供时间、成本、风险不同的可行方案？
6. 是否标出事实、假设、估算、计算结果、判断和未决问题？


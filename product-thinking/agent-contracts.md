# Agent 契约与编排细则

本文件定义产品思维 Agent 的共享状态、输入输出、交接条件和回退规则。Agent 应同时输出结构化事实和 Markdown 解释，不得把假设升级为事实。

## 共享状态对象

```yaml
ProductThinkingState:
  task:
    question: string
    decision_deadline: string|null
    scope: string
  facts: []
  assumptions: []
  evidence: []
  product_context:
    product: string
    stage: string
    vision: string
    strategy: string
  users: []
  user_contexts: []
  opportunities: []
  outcomes: []
  metrics: []
  solutions: []
  experiments: []
  priority_decisions: []
  constraints: []
  risks: []
  validation_actions: []
  open_questions: []
  traceability: []
```

字段为空时写 `[]` 或 `null`，不要删除字段。每个对象尽量包含 `id`、`description`、`source`、`confidence` 和 `status`；`source` 可以是用户输入、访谈、行为数据、研究文件、实验、模型或专家判断。

## Agent 输入输出

### `product-thinking-lead`

- 输入：产品诉求、用户或客户材料、行为数据、业务方向、约束、候选方案、团队容量和决策期限。
- 必须完成：问题/机会定义、结果与指标、高风险假设、实验计划、优先级取舍和持续迭代建议。
- 输出字段：`facts`、`assumptions`、`evidence`、`users`、`user_contexts`、`opportunities`、`outcomes`、`metrics`、`experiments`、`priority_decisions`、`risks`、`validation_actions`、`open_questions`、`traceability`。
- 不负责：详细交互设计、工程实现、营销执行、销售承诺，或替业务负责人决定缺少依据的权重。
- 交接条件：当前产品结果明确；关键机会和假设有证据或验证计划；实验和优先级有停止/复审条件。

## 推荐编排图

```text
用户诉求
   |
   v
product-discovery
   |
   v
product-outcomes-metrics
   |
   v
product-assumption-testing
   |
   v
product-strategy-prioritization
   |
   v
产品决策包 / 下一轮学习
```

这是默认顺序，不是强制线性流程：指标问题可直接从 `product-outcomes-metrics` 开始；已有方案可直接从 `product-assumption-testing` 开始；路线图问题可直接从 `product-strategy-prioritization` 开始。

## 失败与回退

- **没有真实用户问题**：回退 `product-discovery`，不要直接写功能清单。
- **结果不可观察**：回退 `product-outcomes-metrics`，先定义成功标准和基线。
- **方案风险不清**：回退 `product-assumption-testing`，拆解高风险假设。
- **优先级只有分数**：回退 `product-strategy-prioritization`，补充策略、依赖、机会成本和例外理由。
- **证据不足以收敛**：保留多个选项，输出验证行动和需要用户决策的问题。

## Agent 验收问题

1. 是否区分了用户问题、机会、方案、产出和结果？
2. 是否把事实、假设、证据、判断和决策分开？
3. 是否说明了为什么现在做、为什么不做其他选项？
4. 是否有可证伪实验和发布后测量计划？
5. 是否避免用单条反馈、内部偏好或评分公式替代产品判断？

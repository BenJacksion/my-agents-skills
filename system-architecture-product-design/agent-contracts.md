# Agent 契约与编排细则

本文件把角色 Agent 之间的协作从“角色描述”细化为可执行契约。每个 Agent 都应输出结构化事实，同时保留 Markdown 解释；下游 Agent 不得把上游的假设直接升级为事实。

## 共享状态对象

```yaml
ArchitectureState:
  task:
    question: string
    decision_deadline: string|null
    scope: string
  facts: []
  assumptions: []
  ambiguities: []
  stakeholders: []
  value_propositions: []
  goals: []
  system_context:
    system: []
    entities: []
    relationships: []
    boundaries: []
    environments: []
    companion_systems: []
  functions: []
  concepts: []
  forms: []
  mappings: []
  decompositions: []
  interfaces: []
  decisions: []
  trade_space: []
  risks: []
  validations: []
  open_questions: []
  traceability: []
```

字段为空时写 `[]` 或 `null`，不要删除字段。每个对象至少包含 `id`、`description`、`source`、`confidence` 和 `status`；`source` 可以是用户输入、文件、模型、试验或专家判断。

## Agent 输入输出

### `system-explorer`

- 输入：问题、初步系统名或既有上下文。
- 必须完成：实体、关系、边界、环境、伴生系统、层级和涌现假设。
- 输出字段：`system_context`、`facts`、`assumptions`、`risks`。
- 不负责：概念选择、指标权重、具体技术选型。
- 交接条件：至少存在一张实体—关系表和一份边界声明。

### `architecture-governor`

- 输入：`system_context`、用户目标、业务/组织材料。
- 必须完成：利益相关者、价值交换、需求特征、目标、上下游影响和架构基线。
- 输出字段：`stakeholders`、`value_propositions`、`goals`、`ambiguities`、`decisions`。
- 不负责：替技术团队完成详细形式设计。
- 交接条件：每个关键目标有优先级依据或明确标记为未决。

### `concept-architect`

- 输入：目标、约束、无关方案功能。
- 必须完成：多个概念、概念片段、整体/操作/服务概念、Level 1/2 架构草案。
- 输出字段：`functions`、`concepts`、`forms`、`mappings`、`decompositions`。
- 不负责：在权重未确认时宣布唯一最优方案。
- 交接条件：至少两个真正不同概念及淘汰/保留理由。

### `complexity-manager`

- 输入：实体、功能、概念、形式、映射和组织/供应商约束。
- 必须完成：复杂度分类、分解平面比较、2 下 1 上检查、接口/耦合/故障传播诊断。
- 输出字段：`decompositions`、`interfaces`、`risks`、`validations`。
- 不负责：独立创造总体概念。
- 交接条件：每个分解建议有组内/组间关系证据和新增复杂度说明。

### `decision-analyst`

- 输入：候选概念、决策、选项、约束、衡量指标和证据。
- 必须完成：决策模式、权衡空间、帕累托/分群、敏感度、决策顺序和搜索方案。
- 输出字段：`decisions`、`trade_space`、`risks`、`validations`。
- 不负责：定义没有业务依据的权重或把模型输出当最终裁决。
- 交接条件：明确指标来源、模型局限、健壮候选和复审条件。

### `architecture-analyst`

- 输入：既有系统或选定候选的形式、功能、映射和接口材料。
- 必须完成：形式/功能反向核验、接口契约、伴生系统、使用情境、涌现和追溯缺口。
- 输出字段：`forms`、`functions`、`mappings`、`interfaces`、`traceability`、`risks`。
- 不负责：在缺少目标时重新定义业务优先级。
- 交接条件：关键价值、功能、形式、接口和验证证据可互相追溯。

## 推荐编排图

```text
用户问题
   |
   v
system-explorer -----> architecture-governor
                              |
                              v
                      concept-architect
                         /          \
                        v            v
             complexity-manager   decision-analyst
                        \            /
                         v          v
                     architecture-analyst
                              |
                              v
                     架构交付与未决事项
```

这是默认顺序，不是强制线性流程：已有系统盘点可直接从 `architecture-analyst` 开始；只做复杂度诊断可从 `complexity-manager` 开始；只有在价值、边界和目标已稳定时，才允许直接进入 `decision-analyst`。

## 失败与回退

- **边界不清**：回退 `system-explorer`，不继续比较方案。
- **目标冲突**：回退 `architecture-governor`，要求记录利益相关者和优先级来源。
- **只有一个概念**：回退 `concept-architect`，除非硬约束已证明其他概念不可行。
- **模块过细**：回退 `complexity-manager`，检查接口成本、共享状态和验证边界。
- **模型结论翻转**：回退 `decision-analyst`，做敏感度分析并输出多个健壮候选。
- **追溯断裂**：回退 `architecture-analyst`，禁止交付“看起来完整”的架构图。

## Agent 验收问题

1. 该 Agent 是否明确输入、输出、不负责事项和交接条件？
2. 它是否把事实、假设、判断和决策分开？
3. 它是否会在缺少关键上下文时回退，而不是猜测？
4. 它是否输出可验证行动，而不是只给概念名词？
5. 它是否避免把局部指标、算法分数或组织边界直接当系统最优？

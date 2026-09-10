# 架构 Skills 联合使用指南

本指南说明如何联合使用以下两个平级能力域：

- [`system-architecture-product-design/`](system-architecture-product-design/)：复杂系统的系统思维、架构分析、概念开发、复杂度治理和架构决策。
- [`architecture-way/`](architecture-way/)：软件系统设计与项目设计，包括易变性分解、可组合架构、架构验证、项目网络和时间/成本/风险。

仓库另有独立的第三个平级能力域 [`enterprise-application-architecture/`](enterprise-application-architecture/)，专门处理企业应用内部的 5 视图、领域/数据/开发/运行/物理架构，以及分布式、云和数据平台。它不属于本指南的两域联合流程，使用方式见该目录的 [README.md](enterprise-application-architecture/README.md)。

## 一、先分清两个能力域

两套 Skills 不是同一层面的重复实现：

| 能力域 | 主要问题 | 典型产物 |
| --- | --- | --- |
| `system-architecture-product-design` | 系统是什么？服务谁？边界在哪里？有哪些功能、概念、形式和架构决策？ | 系统上下文、利益相关者、目标、功能、候选概念、形式-功能映射、复杂度和权衡 |
| `architecture-way` | 软件结构如何承载变化？组件如何组合和验证？项目如何建造和控制风险？ | 易变性登记、服务边界、服务契约、验证矩阵、项目网络、关键路径、时间/成本/风险选项 |

可以用一句话理解：

```text
系统架构能力负责定义和解释系统；
架构之道能力负责把软件系统设计成可变化、可组合、可验证且可交付的结构。
```

### 不要重复处理的问题

- 不用 `architecture-way` 重新定义已经明确的系统边界、利益相关者和复杂系统价值。
- 不用 `system-architecture-product-design` 重新创建项目网络、关键路径和时间/成本/风险模型。
- 不把“按易变性分解”理解为替代所有系统分解；它是软件结构选择的重要依据。
- 不把“项目设计”理解为架构完成后的机械排期；项目网络应反过来暴露架构边界和验证活动的问题。

## 二、联合使用的总流程

新系统或重大改造默认采用以下链路：

```text
系统思维
  -> 战略与利益相关者
  -> 无关特定方案的功能
  -> 多个系统概念
  -> 形式、功能与映射
  -> 复杂度与架构决策
  -> 软件易变性分解
  -> 可组合架构与服务契约
  -> 架构验证
  -> 项目设计
  -> 执行反馈与架构复审
```

对应 Skill：

```text
system-thinking-emergence
  -> architecture-strategy-governance
  -> architecture-concept-development
  -> architecture-analysis-mapping
  -> complexity-decomposition
  -> architecture-decision-optimization
  -> volatility-decomposition
  -> composable-architecture
  -> architecture-validation
  -> project-design
```

这条链路是默认参考，不要求每个任务都完整执行。路由原则是：先使用系统架构能力解决会改变系统方向的问题，再使用架构之道能力解决软件结构和交付问题。

## 三、按任务类型选择流程

### 1. 从零创建复杂系统

适用于新产品、平台、软硬件协同系统或边界尚未稳定的系统。

```text
system-thinking-emergence
  -> architecture-strategy-governance
  -> architecture-concept-development
  -> complexity-decomposition
  -> architecture-decision-optimization
  -> volatility-decomposition
  -> composable-architecture
  -> architecture-validation
  -> project-design
```

重点：

1. 先识别受益者、利益相关者、系统边界、环境和价值通路。
2. 把需求转成目标和与特定方案无关的功能。
3. 保留多个概念，再做复杂度、形式-功能映射和架构决策。
4. 系统概念稳定后，识别软件部分的变化来源并重新审查组件/服务边界。
5. 用服务契约和端到端验证检查概念是否能落地。
6. 最后从架构和验证活动建立项目网络，而不是从功能清单直接估工。

### 2. 分析和改造已有系统

适用于遗留系统、平台拆分、单体改造、服务化和架构治理。

```text
architecture-analysis-mapping
  -> system-thinking-emergence
  -> complexity-decomposition
  -> volatility-decomposition
  -> composable-architecture
  -> architecture-validation
  -> project-design
```

重点：

1. 从现有形式、功能、接口、数据流、控制流和伴生系统开始。
2. 检查当前模块是否按功能、组织、数据库表或页面机械切分。
3. 识别变化传播、共享状态、重复业务逻辑和跨边界故障。
4. 按易变性形成候选边界，但同时计算拆分带来的接口、部署、测试和运营成本。
5. 先验证一条有代表性的端到端行为，再将改造活动放入项目网络。

已有架构图但缺少目标时，不要直接使用 `volatility-decomposition` 拆服务，应先回到 `system-thinking-emergence` 或 `architecture-strategy-governance`。

### 3. 只做架构权衡和方案选择

适用于部署方式、服务边界、数据所有权、同步/异步、集中式/分布式或平台复用等选择。

```text
architecture-strategy-governance
  -> architecture-concept-development
  -> complexity-decomposition
  -> architecture-decision-optimization
  -> volatility-decomposition
  -> composable-architecture
  -> architecture-validation
```

如果决策会显著影响交付时间、人员配置或风险，再追加：

```text
architecture-validation -> project-design
```

不要只用 `architecture-decision-optimization` 比分数。先明确目标、硬约束、变化来源和验证证据，再把软件结构和项目影响纳入候选比较。

### 4. 只做软件项目计划

适用于架构和边界基本稳定，但需要估算、排网、压缩计划或重新预测。

```text
architecture-validation
  -> project-design
```

如果活动来源不清、服务责任重叠或验证工作缺失，则回退：

```text
project-design
  -> volatility-decomposition
  -> composable-architecture
  -> architecture-validation
```

## 四、Skill 对应关系

| 系统架构能力 | 架构之道能力 | 组合目的 |
| --- | --- | --- |
| `system-thinking-emergence` | `architecture-way` | 把系统整体、实体关系和涌现连接到软件系统设计与项目设计 |
| `architecture-strategy-governance` | `volatility-decomposition` | 将战略、利益相关者目标和生命周期约束转成软件变化来源与边界判断 |
| `architecture-concept-development` | `volatility-decomposition` | 先比较多个系统概念，再判断每个概念的软件结构如何隔离变化 |
| `architecture-analysis-mapping` | `composable-architecture` | 将形式/功能/映射分析转成服务职责、组合场景和契约审查 |
| `complexity-decomposition` | `volatility-decomposition` | 同时考虑复杂度、分解平面、变化局部化和新增接口成本 |
| `architecture-decision-optimization` | `project-design` | 将架构权衡扩展为时间、成本、风险和执行选项的联合比较 |
| `architecture-concept-development` | `architecture-validation` | 用代表性行为验证概念、形式、接口和系统级结果 |
| `architecture-validation` | `project-design` | 把验证活动转入项目网络，并检查验证资源对关键路径的影响 |

### 组合时的优先级

当两个 Skill 都能处理某个词时，按以下优先级判断：

1. **系统边界、利益相关者、涌现、价值和概念**：优先系统架构能力。
2. **软件组件、服务、变化、契约和组合行为**：优先架构之道能力。
3. **跨层级复杂度和分解**：先用 `complexity-decomposition` 建立整体分解约束，再用 `volatility-decomposition` 选择软件边界。
4. **验证**：系统级验证由 `architecture-validation` 统筹，服务契约细节由 `composable-architecture` 提供输入。
5. **时间、成本、风险和项目执行**：优先 `project-design`，但其活动必须来自架构和验证结果。

## 五、交接数据

两个能力域使用不同的共享状态对象。联合使用时，不必强行合并字段，而应通过以下映射交接。

### 系统架构 -> 架构之道

| `ArchitectureState` | `ArchitectureWayState` | 交接说明 |
| --- | --- | --- |
| `system_context` | `system`、`structure` | 传递系统边界、环境、伴生系统和现有结构 |
| `stakeholders` | `stakeholders` | 保留受益者、责任人和利益冲突 |
| `value_propositions`、`goals` | `goals` | 传递价值、目标、成功条件和优先级来源 |
| `functions`、`concepts` | `requirements`、`structure` | 传递功能、候选概念和选定概念的理由 |
| `forms`、`mappings` | `structure`、`services` | 传递形式、功能承载关系和软件候选责任 |
| `decompositions` | `structure`、`volatility_signals` | 传递分解平面、组内/组间关系和变化线索 |
| `interfaces` | `contracts` | 传递边界、交互、交换内容和责任 |
| `decisions`、`trade_space` | `decisions`、`project_options` | 传递已选架构、未决选择和方案约束 |
| `evidence`、`risks` | `evidence`、`risks` | 保留证据、置信度、风险和验证需求 |

交接时必须注明哪些内容是“已决架构”、哪些仍是“候选”、哪些只是“假设”。

### 架构之道 -> 系统架构

当软件设计暴露出系统层问题时，反向交接：

| `ArchitectureWayState` | 返回字段 | 触发条件 |
| --- | --- | --- |
| `volatility_signals` | `uncertainties`、`decisions` | 变化来源与系统生命周期、产品策略或外部约束冲突 |
| `structure`、`services` | `decompositions`、`forms`、`mappings` | 软件边界改变整体功能、性能、组织或供应链 |
| `contracts`、`composition_scenarios` | `interfaces`、`functions`、`risks` | 契约无法表达系统级行为，或跨边界副作用改变价值通路 |
| `project_network`、`project_options` | `decisions`、`trade_space` | 项目依赖证明当前架构无法并行、验证或按约束交付 |
| `validations`、`feedback` | `evidence`、`uncertainties` | 验证结果推翻系统概念、边界、目标或架构假设 |

反向交接不是失败，而是说明系统设计和项目设计之间形成了有效反馈。

## 六、Agent 协作方式

### 角色分工

- `system-architecture-orchestrator`：编排系统探索、治理、概念、复杂度和架构决策。
- `complex-system-architect`：负责复杂系统架构的综合判断和质量门。
- `architecture-way-lead`：编排易变性分解、可组合性、架构验证和项目设计。

推荐由一个主 Agent 负责当前任务，另一个 Agent 作为阶段性协作者：

```text
system-architecture-orchestrator
  -> architecture-way-lead
  -> system-architecture-orchestrator（必要时复审）
```

不要让两个总控 Agent 同时独立生成两套完整架构。这样会产生重复模型、冲突边界和无法解释的权威来源。

### 推荐交接提示词

从系统架构 Agent 交给架构之道 Agent：

```text
基于下面的系统架构结果继续进行软件系统设计和项目设计。
请不要重新定义已确认的系统目标和系统边界，只检查它们对软件结构的约束。

已确认事实：
{facts}

候选概念与架构决策：
{concepts_and_decisions}

系统边界、功能、形式、接口和约束：
{system_context}

请依次完成：
1. 识别软件部分的变化来源和易变性；
2. 形成组件/服务边界候选；
3. 设计关键组合场景和服务契约；
4. 为高风险行为建立架构验证；
5. 从架构和验证活动建立项目网络；
6. 比较时间、成本和风险不同的执行选项。

请区分事实、假设、候选、计算结果、判断和未决问题。
```

从架构之道 Agent 返回系统架构 Agent：

```text
下面是软件系统设计和项目设计阶段的新证据。
请只复审受影响的系统目标、边界、功能、接口、复杂度和架构决策，
不要无条件重做全部系统架构。

易变性与服务边界：
{structure}

组合场景与契约问题：
{contracts_and_risks}

验证结果：
{validation_results}

项目网络与执行选项：
{project_options}

请输出：
1. 哪些系统级假设被支持或被推翻；
2. 哪些边界、功能、形式或接口需要调整；
3. 对候选架构和权衡空间的影响；
4. 需要重新验证或重新设计的最小范围。
```

## 七、联合输出模板

完整任务建议输出以下结构：

```markdown
# 架构与项目设计结论

## 1. 范围与成功定义
- 任务：
- 系统边界：
- 项目边界：
- 决策期限：

## 2. 事实、假设和未知
| 类型 | 内容 | 来源 | 置信度 | 状态 |
| --- | --- | --- | --- | --- |

## 3. 系统级架构基线
- 受益者与利益相关者：
- 系统目标与价值通路：
- 关键实体、关系和伴生系统：
- 功能、形式和形式-功能映射：
- 候选概念与架构决策：

## 4. 软件结构设计
- 变化/易变性登记：
- 组件/服务边界：
- 组合场景：
- 服务契约：
- 变化传播和复杂度代价：

## 5. 验证
- 关键目标与场景：
- 验证矩阵：
- 结果、证据限制和未验证项：

## 6. 项目设计
- 活动和交付物：
- 依赖网络：
- 关键路径与浮动时间：
- 时间/成本/风险选项：
- 推荐方案和放弃方案：

## 7. 反馈与复审
- 跟踪指标：
- 纠偏触发条件：
- 架构复审触发条件：
- 责任人：
- 未决问题：
```

如果任务只涉及局部能力，可以删减章节，但不能删除与结论直接相关的事实、假设、证据和未决问题。

## 八、常见反模式

### 反模式 1：先拆服务，再寻找理由

问题：把“微服务”“领域服务”或“按团队拆分”当作架构起点。

修正：先由系统架构能力明确目标、功能、约束和复杂度，再由 `volatility-decomposition` 识别变化来源，最后由 `composable-architecture` 检查组合成本。

### 反模式 2：系统架构和软件架构各自维护一套边界

问题：系统图中的边界、软件服务边界和项目责任边界互相矛盾。

修正：使用交接表明确每个边界的目标、变化、契约、责任和验证方式；发现冲突时回退到系统架构或复杂度分解。

### 反模式 3：只做静态架构评审

问题：形式、功能和接口看起来完整，但端到端行为无法运行或无法测试。

修正：用 `architecture-validation` 设计最小代表性验证，并将验证活动放入 `project-design` 的项目网络。

### 反模式 4：只比较工期和人数

问题：选择最快或最便宜的方案，却忽略失败概率、返工、集成等待和架构质量。

修正：用 `project-design` 同时比较时间、成本、风险、质量、资源和反馈速度；没有数据时使用范围和定性判断，不伪造概率。

### 反模式 5：把上游假设传给下游后变成事实

问题：概念候选被当成已批准架构，估算被当成承诺，验证计划被当成验证结果。

修正：所有交接对象保留 `source`、`confidence` 和 `status`，明确“事实 / 假设 / 候选 / 已决 / 未验证”。

## 九、最小调用方式

### 综合架构与项目设计

```text
使用 $complex-system-architecture 和 $architecture-way。

请分析这个系统的目标、边界、利益相关者、候选概念和架构决策，
然后继续按易变性设计软件组件/服务边界，检查关键组合场景和契约，
为高风险行为建立验证计划，最后建立项目网络并比较时间、成本和风险不同的执行方案。

请不要默认采用微服务、云或某种技术栈。
请区分事实、假设、候选、证据、计算结果、决策、风险和未决问题。
```

### 现有系统改造

```text
使用 $architecture-analysis-mapping、$complexity-decomposition、
$volatility-decomposition、$composable-architecture 和 $architecture-validation。

请先反向分析现有系统的形式、功能、接口和映射，
再识别变化传播、共享状态、重复逻辑和复杂度来源，
形成按易变性分解的候选边界，检查端到端组合行为，
并给出最小验证计划和改造前置条件。
```

### 架构已定、项目失控

```text
使用 $architecture-validation 和 $project-design。

请基于当前架构和已有项目数据复核验证缺口、活动依赖、关键路径、
浮动时间、资源约束、时间/成本/风险，并提出可执行的纠偏选项。
不要重新设计没有受到证据影响的系统边界。
```

## 十、完成标准

联合使用完成时，至少应满足：

1. 系统目标、边界、利益相关者和软件项目范围相互一致。
2. 软件组件/服务边界能追溯到变化、行为、复杂度或验证依据。
3. 关键组合场景有契约和可执行验证。
4. 项目活动能追溯到架构、详细设计、实现、集成、测试或部署交付物。
5. 执行方案同时呈现时间、成本、风险、质量和资源取舍。
6. 架构和项目中的不确定性都有证据、责任人和复审条件。
7. 任何验证结果都能反馈到系统架构、软件结构或项目网络中的最小受影响范围。

相关契约和能力目录：

- [系统架构能力目录](system-architecture-product-design/capability-catalog.md)
- [系统架构 Agent 契约](system-architecture-product-design/agent-contracts.md)
- [架构之道能力目录](architecture-way/capability-catalog.md)
- [架构之道 Agent 契约](architecture-way/agent-contracts.md)

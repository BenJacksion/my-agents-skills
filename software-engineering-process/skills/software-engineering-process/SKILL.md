---
name: software-engineering-process
description: 按软件生命周期编排产品思维、系统架构、企业应用架构、本体建模和项目设计 Skills/Agents。适用于跨阶段的软件工程任务、阶段路由、交接和质量门；不用于替代具体编码、测试或生产运维。
metadata:
  source: 本仓库五个能力域的流程化编排，详细规则见 ../../capability-catalog.md 和 ../../agent-contracts.md
  version: "1.0.0"
---

# 软件工程流程编排

把一次软件工程任务组织成可回溯的生命周期，而不是把所有 Skill 一次性调用：

```text
问题与机会
  -> 产品目标
  -> 系统理解
  -> 系统架构
  -> 企业应用设计
  -> 软件结构与项目设计
  -> 实现与集成
  -> 验证与发布
  -> 运行反馈与演进
```

`engineering-task-discipline` 是贯穿 S0-S8 的横向执行约束，不是新增阶段。凡涉及代码、文档或配置变更的任务，都同时遵守它对假设澄清、最小修改、验证证据和中文交付的要求；本 Skill 负责阶段路由、交接和质量门。

`ontology-modeling` 也是专项能力而非独立阶段：在 S2 处理系统语义、身份和关系，在 S4 处理领域/数据/对象/行动模型，在 S7/S8 处理语义约束、映射和版本演进验证。它不替代 `domain-application-modeling` 或 `data-platform-architecture`。

`skill-orchestration` 位于本流程之上，负责多 Skill 任务的选择、依赖顺序、并行边界和交接状态；本 Skill 负责确定软件生命周期阶段及其质量门。单一 Skill 任务不需要额外建立调度图。

## 路由协议

1. 若任务涉及变更，先加载 `engineering-task-discipline`，明确成功标准、范围和验证方式；再判断当前阶段：S0 受理、S1 产品、S2 系统理解、S3 系统架构、S4 企业应用、S5 项目设计、S6 实现、S7 验证发布、S8 运行演进。
2. 每轮只选择一个主阶段和一个主 Agent；专项 Agent 只补充该阶段所需的分析。
3. 缺失信息只有在会改变阶段、边界或决策时才集中提问，其他内容标记为未知。
4. 阶段输出必须包含事实、假设、证据、决策、风险、验证行动和下一阶段入口；涉及变更时还必须给出实际验证结果。
5. 验证或实施反馈推翻上游判断时，回退到最小受影响阶段，不重新启动全部流程。

## 阶段路由

- S1：`product-thinking-lead`，使用 `product-thinking`、`product-discovery`、`product-outcomes-metrics`、`product-assumption-testing`、`product-strategy-prioritization`。
- S2-S3：`system-architecture-orchestrator`，按需使用 `system-thinking-emergence`、`architecture-analysis-mapping`、`architecture-strategy-governance`、`architecture-concept-development`、`complexity-decomposition`、`architecture-decision-optimization`、`complex-system-architecture`。
- S2 专项：当问题涉及共享词汇、概念身份、关系方向或语义边界时，加载 `ontology-modeling`；主 Agent 仍为当前 S2 Agent。
- S4：`enterprise-application-architect`，按需使用企业应用架构域的 7 个 Skills；当问题涉及领域语义、数据映射、对象/链接/行动或规则归属时加载 `ontology-modeling`。
- S5：`architecture-way-lead`，使用 `architecture-way`、`volatility-decomposition`、`composable-architecture`、`project-design`。
- S7：组合 `architecture-validation`、`product-assumption-testing`、`product-outcomes-metrics`；当发布对象包含语义模型或映射时追加 `ontology-modeling` 验证。
- S8：根据反馈回到 S1、S2、S4 或 S5；若词汇、身份、规则或映射发生漂移，追加 `ontology-modeling` 复审，不把反馈直接写成新需求或新架构。

## 阶段门

- 产品门：问题、结果、假设和优先级可追溯；
- 系统门：边界、利益相关者、概念和约束明确；
- 架构门：候选、复杂度、权衡和决策可解释；
- 应用门：五视图、质量属性和数据责任闭合；
- 项目门：结构、契约、验证活动和项目网络闭合；
- 发布门：关键行为有证据，风险有责任人和处理决策；
- 演进门：反馈能定位到最小受影响阶段。

## 范围边界

本 Skill 可以组织实施、测试和运维活动的输入输出，但本仓库没有独立的编码、测试工程、发布工程和生产运维 Skill/Agent。不要虚构这些能力已经存在；把对应工作交给实际工程团队，并保留清晰的架构约束、验收条件和变更记录。

详细阶段契约见 [agent-contracts.md](../../agent-contracts.md)。

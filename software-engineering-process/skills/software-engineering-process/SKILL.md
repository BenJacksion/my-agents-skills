---
name: software-engineering-process
description: 按软件生命周期编排产品思维、系统架构、企业应用架构和项目设计 Skills/Agents。适用于跨阶段的软件工程任务、阶段路由、交接和质量门；不用于替代具体编码、测试或生产运维。
metadata:
  source: 本仓库四个能力域的流程化编排，详细规则见 ../../capability-catalog.md 和 ../../agent-contracts.md
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

## 路由协议

1. 先判断当前阶段：S0 受理、S1 产品、S2 系统理解、S3 系统架构、S4 企业应用、S5 项目设计、S6 实现、S7 验证发布、S8 运行演进。
2. 每轮只选择一个主阶段和一个主 Agent；专项 Agent 只补充该阶段所需的分析。
3. 缺失信息只有在会改变阶段、边界或决策时才集中提问，其他内容标记为未知。
4. 阶段输出必须包含事实、假设、证据、决策、风险、验证行动和下一阶段入口。
5. 验证或实施反馈推翻上游判断时，回退到最小受影响阶段，不重新启动全部流程。

## 阶段路由

- S1：`product-thinking-lead`，使用 `product-thinking`、`product-discovery`、`product-outcomes-metrics`、`product-assumption-testing`、`product-strategy-prioritization`。
- S2-S3：`system-architecture-orchestrator`，按需使用 `system-thinking-emergence`、`architecture-analysis-mapping`、`architecture-strategy-governance`、`architecture-concept-development`、`complexity-decomposition`、`architecture-decision-optimization`、`complex-system-architecture`。
- S4：`enterprise-application-architect`，按需使用企业应用架构域的 7 个 Skills。
- S5：`architecture-way-lead`，使用 `architecture-way`、`volatility-decomposition`、`composable-architecture`、`project-design`。
- S7：组合 `architecture-validation`、`product-assumption-testing`、`product-outcomes-metrics`。
- S8：根据反馈回到 S1、S2、S4 或 S5，不把反馈直接写成新需求或新架构。

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

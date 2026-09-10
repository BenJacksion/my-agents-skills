# 软件工程流程 Agents & Skills

本目录是项目级编排层，用软件工程生命周期组织仓库中的四个能力域：

- `product-thinking/`：发现问题、定义结果、验证假设和做产品取舍；
- `system-architecture-product-design/`：理解复杂系统、生成概念、治理复杂度和做系统级架构决策；
- `enterprise-application-architecture/`：把企业应用落实为领域、数据、开发、运行、物理、分布式、云和数据平台架构；
- `architecture-way/`：按易变性建立软件结构，检查组合与验证，并设计项目网络、时间、成本和风险。

本目录不替代上述能力域，也不把编码、测试、发布或运维的具体专业方法伪装成已有能力。它负责回答：

1. 当前项目处于软件工程的哪个阶段？
2. 这一阶段应调用哪些 Skills 和 Agents？
3. 阶段产物如何交给下一阶段？
4. 什么质量门通过后才能继续？
5. 哪些问题必须回退，而不是继续堆叠方案？

详细编排见：

- [software-engineering-process Skill](skills/software-engineering-process/SKILL.md)
- [能力目录](capability-catalog.md)
- [Agent 契约](agent-contracts.md)
- [项目级总编排 Agent](agents/software-engineering-orchestrator.md)

## 软件工程主流程

```text
问题与机会
  -> 产品目标与优先级
  -> 系统边界与概念
  -> 系统级架构决策
  -> 企业应用设计
  -> 软件结构与项目设计
  -> 实现与集成
  -> 验证与发布
  -> 运行反馈与演进
  -> 下一轮问题与机会
```

这不是强制瀑布流程。每一轮迭代都应经过当前阶段的质量门；当验证或实施反馈推翻上游假设时，沿最小影响范围回退。

## 阶段总览

| 阶段 | 主要问题 | 主 Agent | 关键出口 |
| --- | --- | --- | --- |
| S0 任务受理 | 要解决什么问题？成功如何定义？ | `software-engineering-orchestrator` | 范围、阶段、决策人、成功标准 |
| S1 产品发现 | 谁的问题？为什么值得解决？ | `product-thinking-lead` | 机会、结果、假设、优先级 |
| S2 系统理解 | 系统边界、实体、关系和价值在哪里？ | `system-architecture-orchestrator` | 系统上下文、利益相关者、需求和约束 |
| S3 系统概念与架构 | 哪些概念可行？如何比较和收敛？ | `system-architecture-orchestrator` | 候选概念、分解、权衡和系统架构基线 |
| S4 企业应用设计 | 领域、数据、代码、运行和部署如何闭合？ | `enterprise-application-architect` | 五视图、质量属性、分布式/云/数据方案 |
| S5 软件结构与项目设计 | 软件如何承载变化？如何组织交付？ | `architecture-way-lead` | 组件/服务、契约、验证计划、项目网络和执行选项 |
| S6 实现与集成 | 设计如何变成可运行的软件？ | 项目工程团队 | 代码、集成结果、运行数据和变更记录 |
| S7 验证与发布 | 系统是否满足目标？能否发布？ | `architecture-way-lead` / `product-thinking-lead` | 验证证据、发布决策、结果基线 |
| S8 运行与演进 | 实际结果是否支持继续、调整或停止？ | `software-engineering-orchestrator` | 反馈、架构复审、下一轮优先级 |

## 使用原则

- 先定位阶段，再选择 Skill；不要因为用户提到某个技术名词就直接进入技术选型。
- 每个阶段保留事实、假设、证据、决策、风险和未决问题。
- 主 Agent 维护阶段状态，专项 Agent 提供分析，不生成互相竞争的完整方案。
- 阶段出口必须能追溯到输入和验证行动。
- 代码、测试和生产操作不由本项目现有方法论 Agent 假装完成；应把架构约束、验证条件和项目活动交给实际工程团队。

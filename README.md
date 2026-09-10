# 产品与系统架构 Agents & Skills

将互联网一手来源中的产品思维方法、《系统架构：复杂系统的产品设计与开发》中的系统架构方法、Juval Löwy《架构之道：软件构建的设计方法》的系统设计与项目设计方法，以及《架构真意：企业级应用架构设计方法论与实践》的企业应用架构方法，转化为可路由、可协作、可验证的 Agents 与 Skills。

## 目录

- `product-thinking/`：从用户问题、产品结果、假设实验和优先级取舍中形成产品决策。
- `system-architecture-product-design/`：从系统思维、架构分析、概念创建、复杂度分解到架构决策。
- `architecture-way/`：从易变性分解、可组合架构、架构验证到项目网络、时间/成本/风险和执行方案。
- `enterprise-application-architecture/`：从业务用例、领域与数据到开发、运行、物理、分布式、云和数据平台架构。
- `software-engineering-process/`：按软件生命周期编排上述能力域的 Skills、Agents、阶段门和交接。

## 产品思维

- `product-thinking/README.md`：产品思维能力域说明。
- `product-thinking/agents/`：产品思维负责人 Agent。
- `product-thinking/skills/`：产品思维总入口、产品发现、结果与指标、假设测试、策略与优先级 Skills。
- `product-thinking/research.md`：基于互联网一手来源的产品思维研究与来源清单。

默认链路：

```text
产品发现 -> 结果与指标 -> 假设测试 -> 策略与优先级 -> 持续迭代
```

## 系统架构

- `system-architecture-product-design/README.md`：系统架构能力域说明。
- `system-architecture-product-design/agents/`：系统探索、架构分析、概念设计、复杂度管理、治理和决策分析等 Agent。
- `system-architecture-product-design/skills/`：可独立调用的架构分析、概念开发、复杂度分解、战略治理、决策优化和系统思维 Skills。
- `system-architecture-product-design/source-materials/`：系统架构原始 OCR 与细粒度框架资料。

默认链路：

```text
系统思维 -> 架构分析 -> 概念创建 -> 复杂度分解 -> 决策优化
```

## 《架构之道：软件构建的设计方法》

- `architecture-way/README.md`：能力域说明、书籍定位、核心原则和边界。
- `architecture-way/agents/`：系统设计与项目设计负责人 Agent。
- `architecture-way/skills/`：架构之道总入口、易变性分解、可组合架构、架构验证和项目设计 Skills。
- `architecture-way/research.md`：基于互联网一手来源的书籍研究与来源清单。

默认链路：

```text
易变性分解 -> 可组合架构 -> 架构验证 -> 项目设计 -> 跟踪与反馈
```

## 《架构真意》

- `enterprise-application-architecture/README.md`：企业级应用架构能力域说明、书籍定位和边界。
- `enterprise-application-architecture/agents/`：企业应用总架构、应用设计、分布式与数据架构 Agent。
- `enterprise-application-architecture/skills/`：5 视图、领域建模、架构演进、分布式应用、云端交付和数据平台 Skills。
- `enterprise-application-architecture/research.md`：基于互联网公开书目、目录和内容简介的研究与证据边界。

默认链路：

```text
业务目标/用例 -> 领域与数据 -> 5 视图 -> 质量属性与演进 -> 分布式/云/数据平台
```

## 软件工程流程

- `software-engineering-process/README.md`：项目级生命周期和能力域边界。
- `software-engineering-process/capability-catalog.md`：全部 Skills/Agents 的阶段路由表。
- `software-engineering-process/agent-contracts.md`：阶段状态、质量门、交接和回退规则。
- `software-engineering-process/agents/software-engineering-orchestrator.md`：项目级总编排 Agent。

默认链路：

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

## 使用方式

1. 根据用户问题和路由规则选择对应 Skill 或 Agent。
2. 阅读对应能力域的 `README.md`、`capability-catalog.md` 和目标 `SKILL.md`。
3. 按该能力域的 `agent-contracts.md` 输出事实、假设、证据、决策、风险和下一步验证行动。
4. 缺失信息必须标记为未知；只有当缺失信息会改变方向时才集中提问。

`architecture-way/` 与 `system-architecture-product-design/` 的联合使用方式参阅[架构 Skills 联合使用指南](架构Skills联合使用指南.md)。`enterprise-application-architecture/` 是独立的第三个平级能力域，详见其自身的 `README.md`、`capability-catalog.md` 和 `agent-contracts.md`。

需要按软件工程生命周期选择和串联全部能力时，参阅[软件工程流程](software-engineering-process/README.md)；该流程层只负责编排，不替代各能力域的专业方法。

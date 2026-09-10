# 《架构之道：软件构建的设计方法》Agents & Skills

将 Juval Löwy 的《架构之道：软件构建的设计方法》（英文名 *Righting Software*）提炼为可路由、可协作、可验证的 Agents 与 Skills。

## 书籍定位

本能力域中的“《架构之道：软件构建的设计方法》”专指以下书籍：

- 中文名：《架构之道：软件构建的设计方法》
- 英文名：*Righting Software*
- 作者：Juval Löwy
- 主题：系统设计与项目设计的一体化方法

原始研究见 [research.md](research.md)。研究文件区分“原文明确主张”和“综合推断”，并记录来源类型与原始链接。

两个架构能力域的联合路由、状态交接和 Agent 协作方式见根目录的[架构 Skills 联合使用指南](../架构Skills联合使用指南.md)。

## 一句话总结

《架构之道：软件构建的设计方法》的核心不是先选技术或先拆功能，而是在不确定性下把系统设计和项目设计连接起来：先按易变性建立可组合的系统结构，再从系统结构推导项目网络、人员、时间、成本和风险，比较多个执行方案，并用设计验证和项目反馈持续修正。

## 能力链路

默认编排顺序为：

```text
系统目标与约束
   |
   v
按易变性分解
   |
   v
可组合架构与服务契约
   |
   v
架构验证
   |
   v
项目设计：网络 -> 时间/成本 -> 风险 -> 执行选项
   |
   v
跟踪、反馈与复审
```

这不是强制的线性流程。已有系统结构可以直接进入可组合性或验证；已有架构但项目不可控时，可以直接进入 `project-design`。

## 内容

- `research.md`：互联网一手资料研究、书籍总结和证据标注。
- `skills/`：总入口、易变性分解、可组合架构、架构验证和项目设计 Skills。
- `agents/architecture-way-lead.md`：负责在系统设计与项目设计之间编排的 Agent。
- `capability-catalog.md`：能力地图、来源映射、路由规则和统一数据契约。
- `agent-contracts.md`：共享状态、输入输出、交接、回退和验收规则。

## 核心原则

- 系统设计和项目设计必须相互约束，不能把项目计划当成架构完成后的附属物。
- 组件或服务边界优先依据变化和易变性，而不是简单按功能、部门或名词切分。
- 架构应支持组合：变化应尽量局部化，跨边界组合应通过清晰契约完成。
- 项目不是只有时间和成本两个维度，还要显式处理风险和成功概率。
- 同一个目标通常有多个可行的项目执行方案；比较选项比追求一个“唯一正确计划”更可靠。
- 模型、公式和工具帮助表达判断，不替代架构师、项目负责人和利益相关者的决策。
- 交付前验证系统设计、服务契约和项目设计之间是否闭合；交付后用实际进度与预测反馈修正计划。

## 与现有能力域的边界

`architecture-way/` 专注于软件系统设计与项目设计的连接，尤其是易变性分解、可组合性、服务契约、项目网络和风险。

`system-architecture-product-design/` 继续承载更广义的复杂系统能力，包括系统思维、形式/功能映射、概念生成、跨生命周期分解和架构决策优化。遇到硬件、供应链、产品族、社会技术系统或复杂架构权衡时，应组合现有系统架构 Skills，而不是把这些内容复制到本目录。

需要从产品问题一路编排到项目设计、验证和运行反馈时，参阅根目录的[软件工程流程](../software-engineering-process/README.md)。

## 主要外部来源

- [Righting Software 官方网站](https://rightingsoftware.org/)
- [InformIT 书籍页面与完整目录](https://www.informit.com/store/righting-software-9780136524038)
- [InformIT：Software System Decomposition 样章](https://www.informit.com/articles/article.aspx?p=2995357)
- [InformIT：How to Calculate Risk in Your Projects 样章](https://www.informit.com/articles/article.aspx?p=2995358)
- [Righting Software 官方视频与工具页](https://rightingsoftware.org/videos.html)

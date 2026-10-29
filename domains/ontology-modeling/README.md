# 本体建模

将知识工程的概念、关系、公理与 RDF/OWL 建模，以及 Palantir 的业务对象、关系与行动建模，提炼为一个支持两种模式的 Skill。两者共享业务语义识别，但不假设标准、推理或执行机制相同。

## 内容

- [research.md](research.md)：基于 AnySearch 的一手来源研究、方法总结与证据边界。
- [capability-catalog.md](capability-catalog.md)：模式路由、职责边界和质量门。
- [agent-contracts.md](agent-contracts.md)：调用者的输入输出和交接契约；本能力域不新增独立 Agent。
- [ontology-modeling](skills/ontology-modeling/SKILL.md)：可复用的本体建模 Skill。
- [可复现案例](skills/ontology-modeling/references/executable-example.md)：独立模型、数据、SHACL、查询与 OWL 推理验证，含受控迁移回归。

## 使用方式

调用 `$ontology-modeling`，说明需要回答的问题或执行的业务决策、领域材料、数据样本和目标环境。

首次阅读先看本页和[能力目录](capability-catalog.md)；执行时读取 Skill 及命中的模式参考；需要核查方法依据时再看研究总结。Skill 目录包含独立执行所需内容，可以单独复制安装。

- 知识工程模式：概念与实例、RDF/RDFS/OWL、SHACL、查询与推理验证。
- 运营模式：业务对象、数据映射、链接、行动、权限与反馈验证。
- 联合模式：先定义共用业务词汇，再分别实现和验证；不将 Foundry Ontology 宣称为 OWL 实现。

可直接使用的请求示例：

- “使用 `$ontology-modeling`，根据这些设备与工单数据建立知识工程本体，回答每台设备的开放工单由谁负责，并验证交付数据必须有负责人。”
- “使用 `$ontology-modeling`，评审现有 Foundry 工单指派模型，重点检查主键稳定性、指派条件和通知失败后的状态。”
- “使用 `$ontology-modeling`，将 RDF 模型映射到 Foundry，列出身份、类型、约束和行动的对应关系及无法保留的语义。”

输出通常是一份模型说明，包含范围、模型与数据映射、问题到测试的追溯，以及决策和未决项。仅使用需要的语言与平台能力；概念设计阶段可以先交付验证计划。

遇到类/角色/状态取舍、跨源身份或时间问题时，按需读取[建模选择](skills/ontology-modeling/references/modeling-decisions.md)；已有模型演进和行动失败处理见[演进与行动验证](skills/ontology-modeling/references/evolution-and-operations.md)。

## 运行案例

安装 uv 和 Java 后，在仓库根目录运行；依赖版本、环境要求和验收项见[案例说明](skills/ontology-modeling/references/executable-example.md)。

```bash
uv run --no-project domains/ontology-modeling/skills/ontology-modeling/scripts/verify_example.py
```

脚本验证正常与异常数据、历史查询、时间边界、目标覆盖、受控迁移和 OWL 推理。它不连接 Foundry；平台行动、权限和副作用需要另行验证。

## 边界

本能力域来自公开标准和产品官方文档，不属于已有书籍能力域。只需要应用模块、聚合或分层设计时，使用现有[领域与应用建模](../enterprise-application-architecture/skills/domain-application-modeling/SKILL.md)。本体设计不等于数据库设计，也不默认需要知识图谱、OWL 推理器或 Palantir 平台。

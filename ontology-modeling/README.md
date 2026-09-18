# 本体建模

将知识工程的概念、关系、公理与 RDF/OWL 建模，以及 Palantir 的业务对象、关系与行动建模，提炼为一个支持两种模式的 Skill。两者共享业务语义识别，但不假设标准、推理或执行机制相同。

## 内容

- [research.md](research.md)：基于 AnySearch 的一手来源研究、方法总结与证据边界。
- [capability-catalog.md](capability-catalog.md)：模式路由、职责边界和质量门。
- [agent-contracts.md](agent-contracts.md)：调用者的输入输出和交接契约；本能力域不新增独立 Agent。
- [ontology-modeling](skills/ontology-modeling/SKILL.md)：可复用的本体建模 Skill。

## 使用方式

调用 `$ontology-modeling`，说明需要回答的问题或执行的业务决策、领域材料、数据样本和目标环境。

- 知识工程模式：概念与实例、RDF/RDFS/OWL、SHACL、查询与推理验证。
- 运营模式：业务对象、数据映射、链接、行动、权限与反馈验证。
- 联合模式：先定义共用业务词汇，再分别实现和验证；不将 Foundry Ontology 宣称为 OWL 实现。

## 边界

本能力域来自公开标准和产品官方文档，不属于已有书籍能力域。只需要应用模块、聚合或分层设计时，使用现有[领域与应用建模](../enterprise-application-architecture/skills/domain-application-modeling/SKILL.md)。本体设计不等于数据库设计，也不默认需要知识图谱、OWL 推理器或 Palantir 平台。

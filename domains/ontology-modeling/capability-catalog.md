# 能力目录：本体建模

研究依据见 [research.md](research.md)，入口为 [ontology-modeling](skills/ontology-modeling/SKILL.md)。

## 路由

| 模式 | 适用任务 | 必须验证 | 不承诺 |
| --- | --- | --- | --- |
| 知识工程 | 共享词汇、语义集成、RDF/OWL、逻辑分类与推理 | 能力问题；采用 OWL 时检查推理，采用 SHACL 时检查数据合规和目标覆盖 | OWL 自动拒绝缺失值或重复标识 |
| 运营 | Foundry 对象、链接、行动及业务闭环 | 数据映射、行动条件、权限、状态和外部失败 | 外部系统副作用与对象修改全局原子提交 |
| 联合 | 两种模型之间的业务语义映射 | 身份、类型、关系、规则、时间和信息损失 | 两种平台或语言语义天然等价 |

## 与现有能力分工

- 本体建模负责语义、身份、关系、规则归属与本体层的数据映射。
- `domain-application-modeling` 负责应用领域、聚合、模块与代码分层；不因名词相同就合并职责。
- `data-platform-architecture` 负责数据采集、治理、加工与服务链路；本 Skill 只交接所需数据契约。
- 不为只需术语表的任务强加 OWL，也不为只需查询的模型增加行动体系。

验收按[交接契约](agent-contracts.md)执行；新建、评审与演进使用同一 Skill，按任务裁剪产物。

## 按需深入

- 表达取舍、身份、时间与词汇对齐：[建模选择](skills/ontology-modeling/references/modeling-decisions.md)。
- 版本迁移、状态转换与运营失败：[演进与行动验证](skills/ontology-modeling/references/evolution-and-operations.md)。
- 查询、SHACL、OWL 与受控迁移的实际复现：[案例与验证脚本](skills/ontology-modeling/references/executable-example.md)。

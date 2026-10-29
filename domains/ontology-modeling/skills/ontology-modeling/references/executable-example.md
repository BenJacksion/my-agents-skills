# 可复现案例：设备、工单与指派

用于学习或验证查询、数据契约、OWL 推理和受控模型演进。数据为自行构造；没有连接 Foundry，没有自动创建对象类型、行动或权限。

## 运行

需要 uv、Python 3.10 及以上与 Java；本次验证使用 Python 3.12、Java 17。脚本的内联元数据固定 RDFLib 7.6.0、pySHACL 0.40.1 和 Owlready2 0.48，首次运行需要下载依赖，HermiT 随 Owlready2 分发。

在仓库根目录执行：

```bash
uv run --no-project domains/ontology-modeling/skills/ontology-modeling/scripts/verify_example.py
```

单独复制 Skill 时，在 Skill 目录执行：

```bash
uv run --no-project scripts/verify_example.py
```

[验证脚本](../scripts/verify_example.py)根据自身位置读取数据，不依赖当前工作目录，不修改样例。失败返回非零状态；缺少 Java 时明确报告未运行，不跳过推理后宣布全通过。输出包含依赖版本、Java 版本、HermiT jar 哈希与各测试结果。

## 文件与职责

| 文件 | 用途 |
| --- | --- |
| [model.ttl](../examples/maintenance/model.ttl) | v2 词汇、类型与关系；不混入 shapes |
| [data.ttl](../examples/maintenance/data.ttl) | 工单、设备、员工、指派历史与源记录 |
| [shapes.ttl](../examples/maintenance/shapes.ttl) | 数据契约；包含 SHACL Core 与区间重叠的 SHACL-SPARQL 约束 |
| [assignment-at.rq](../examples/maintenance/assignment-at.rq) | 绑定设备与时间，查当前开放工单在该有效时间的主负责人 |
| [legacy-v1.ttl](../examples/maintenance/legacy-v1.ttl) | 单负责人旧数据；为受控转换提供真实生效时间与快照记录时间 |
| [reasoning.ttl](../examples/maintenance/reasoning.ttl) | 独立的 OWL 限制与分类案例，不参与数据契约校验 |

## 需求到验证的追溯

查询范围是“当前状态为 Open 的工单”；回看指派历史不表示重建了工单的历史状态。所有时间均为 UTC，有效区间左闭右开；本例没有结束时间表示持续有效。t2 允许未指派，不适用旧研究示例“交付工单必须恰好一个负责人”的契约。

| 问题或规则 | 模型元素与样例 | 预期与验证入口 |
| --- | --- | --- |
| 1 月 10 日设备 A 的主负责人？ | t1 的 a1 指派 | `test_historical_owner`：t1/u1；t2/未知 |
| 换人瞬间与 1 月 20 日由谁负责？ | a1 在 15 日结束，a2 同时开始；a3 是 Reviewer | `test_boundary_and_current_owner_ignore_reviewer`：t1/u2，审核人员不混入答案 |
| 没有匹配指派记录怎么办？ | t2 无指派；t1 在首条指派前查询 | `test_no_record_before_first_assignment`：工单仍返回，owner 未绑定；不证明现实世界无人负责 |
| 合并了人员，是否应合并源记录？ | 两条源记录分别 denotes u1 | `test_source_records_are_distinct_from_person`：记录各自保留，不将记录与人声明为同一个体 |
| 每条指派只有一个有效员工？ | AssignmentShape 的 minCount/maxCount/class | 缺负责人、多负责人、缺员工类型分别失败；默认关闭推理 |
| 时间边界和来源是否合规？ | validFrom、validTo、wasDerivedFrom | 起止相等、Primary 区间重叠、缺来源均失败；不同角色并存通过 |
| shape 是否真的选中了数据？ | targetClass 与 targetSubjectsOf | 正常覆盖 2 张工单、3 条指派；删类型仍被选中并失败；空图不能作为交付通过证据 |
| 旧数据能否迁移且保留答案？ | v1 单负责人转为 v2 Primary 指派 | `test_migration_preserves_answer_and_validates`：相同问题答案保留、通过新 shapes、重复转换不新增记录 |
| 历史缺失或身份有歧义怎么办？ | v1 缺生效时间或多个负责人 | `test_migration_rejects_missing_history_and_ambiguous_owner`：拒绝转换，不伪造历史 |
| 迁移来源与标识是否可靠？ | v1 缺快照记录时间，或目标指派标识已被引用 | 对应拒绝用例失败退出转换，保留原始图不变 |

SHACL 在原始数据图运行，`inference="none"`，不混入 OWL 推理结果。缺少员工类型的反例还会单独开启 RDFS 推理，展示 range 补类型后校验通过的差异。这不是缺陷修复，而是两个不同的校验前提。

覆盖数量是本例的固定验收值；新任务应按照自己的范围和 target 核对，不能复制“2/3”作为普遍阈值。SHACL 合规也不证明员工实际在岗、身份匹配正确或平台行动获准执行。

## OWL 推理验证

使用 HermiT 对独立 RDF/XML 转换结果推理，不以手写 Python 判断替代 OWL 一致性检查。案例采用 OWL 2 DL 中的交集、存在/全称限制、等价与互斥构造；未运行自动 profile 合规检查，也不是性能基准。

| 公理与事实 | 预期 |
| --- | --- |
| EmployeeAssignedTicket 等价于 Ticket 且至少 assignedTo 某个 Employee；classified 满足这些事实 | 自动分类为 EmployeeAssignedTicket，原始数据未直接声明此类型 |
| RequiredTicket 只有相同的必要条件 | classified 不因此被反向归入 RequiredTicket |
| required 已属于 RequiredTicket | 推出属于 EmployeeAssignedTicket，但不生成可见的命名负责人记录 |
| OnlyEmployeeTicket 的所有负责人都是 Employee；empty 没有已知负责人 | 全称限制不蕴涵存在负责人，不能推出 EmployeeAssignedTicket |
| unclassified 只关联一个没有员工类型证据的对象 | 不推出 EmployeeAssignedTicket；不等于断言其负责人不是员工 |
| ImpossibleOwner 同时属于互斥的 Employee 和 Machine | 类不可满足，未实例化时全局仍一致；加入该类实例后推理器报告不一致 |

## 运行证据与边界

首次补充时的实际结果见能力域的研究记录。此指南和测试定义预期行为；只有本次命令实际成功退出，才能将目标环境对应检查标为通过。

运营模型的状态转换、并发、幂等和副作用验证见[演进与行动验证](evolution-and-operations.md)，在真实平台执行前均属测试设计。

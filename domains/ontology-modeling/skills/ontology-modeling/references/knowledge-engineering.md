# 知识工程模式

## 选择表达能力

- RDF 表达三元组；RDFS 提供类、子类及属性 domain/range；OWL 增加等价、互斥、限制等形式语义。Turtle 是序列化格式，不是额外的推理体系。
- 查询需要与推理需要分开：先确认能力问题能否用显式事实和 SPARQL 回答，再决定是否需要 OWL。
- 选择 OWL 2 profile 或更丰富表达前核对推理器支持、所需构造和数据规模；不默认 OWL Full。
- 稳定跨源实体优先分配 IRI；blank node 不当作跨数据集持久主键。`owl:sameAs` 表达强同一性，不用于模糊匹配或相似对象。

根据问题选择最小可用表达，再用目标工具验证，而非按“功能越多越好”选择：

| 需求 | 候选 | 选型证据 |
| --- | --- | --- |
| 只查询显式事实并校验交付数据 | RDF、SPARQL、SHACL，可加必要的 RDFS | 查询与数据契约足够时，不增加 OWL 推理 |
| 以大量类及存在关系的分类为核心 | 评估 OWL 2 EL | 检查所需构造是否属于 profile，以及分类规模与实际耗时 |
| 希望通过关系数据库查询改写访问实例 | 评估 OWL 2 QL | 验证查询、映射与目标实现支持，而非假设任意 SPARQL 均可改写 |
| 以规则方式处理 RDF 实例上的可支持推理 | 评估 OWL 2 RL | 核对规则实现的覆盖、派生规模与语义前提，不当作完整 OWL 2 DL 推理器 |
| 需要所选 profile 之外的构造组合 | 评估 OWL 2 DL 与支持该构造的推理器 | 检查全局限制、可判定性边界和实际数据上的资源消耗；不自动升级为 OWL Full |

EL/QL/RL 有重叠，并不是由弱到强的线性等级。参考 [OWL 2 Profiles](https://www.w3.org/TR/owl2-profiles/)；声明 profile 不能代替合规检查和工具实测。

## 必要条件、充分条件与存在

- `A rdfs:subClassOf B` 表达每个 A 都满足 B；已知某对象满足 B，不能因此反推它属于 A。
- `owl:equivalentClass` 给出双向分类承诺；只有定义在所有适用情境都成立时才用，不能为获得自动分类而过度声明等价。
- `someValuesFrom` 要求存在至少一个满足限制的关联对象，但不负责创建可见的命名数据记录。
- `allValuesFrom` 限制已有或可能的关联值；没有关联也可以满足它，因此不表达必填。

先用一个应被分类的正例与一个不应被分类的反例检查公理。[可复现案例](executable-example.md#owl-推理验证)实际运行这些区别，以及不可满足类与全局不一致的区别。

## 防止把语义当校验

- OWL 采用开放世界假设：未记录某关系不表示关系不存在；最小基数不会自动拒绝缺失字段。
- 不采用唯一名称假设：两个 IRI 不必指向不同个体。最大基数限制可能引出个体同一性；只有结合差异断言等条件才可能矛盾，不能当数据库唯一索引。
- RDFS/OWL 的 domain/range 是推理类型的依据，不是拒绝“错误类型”的输入规则。多个 domain 声明不是任选其一。
- 区分“全局本体不一致”和“某个类不可满足”；一个不可满足类未必使无该类实例的本体全局不一致。
- 用 SHACL 表达必填、数量、类型、枚举等数据要求，明确 target、待校验数据图、推理/预处理和严重级别。`sh:closed` 只关闭指定 shape 的属性集合，不是把整个世界改成闭世界。
- 检查 target 实际选中了哪些节点及其数量；零个目标节点也可能返回符合，不能据此认定数据正确。`sh:class` 允许通过子类路径确定类型，不等于要求一条直接的 `rdf:type` 声明；若业务要求原始声明存在，应单独校验该声明。

## 最小示例

以下为自行构造的交付数据示例。目标：查询已进入交付范围的工单负责人；数据规则：每张交付工单恰有一个负责人，且在校验图中满足员工类型。未指派草稿不在本次交付图中；若混入同一图，须调整 target 或采用条件约束。

为了便于阅读，下面将模型、shape 和样例放在一个代码块；实际验证时分别指定数据图和 shapes 图，并固定推理配置。

```turtle
@prefix ex: <https://example.org/ontology/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix sh: <http://www.w3.org/ns/shacl#> .

ex:Ticket a owl:Class .
ex:Employee a owl:Class .
ex:assignedTo a owl:ObjectProperty ;
    rdfs:domain ex:Ticket ; rdfs:range ex:Employee .

ex:TicketShape a sh:NodeShape ;
    sh:targetClass ex:Ticket ;
    sh:property [ sh:path ex:assignedTo ;
                  sh:minCount 1 ; sh:maxCount 1 ; sh:class ex:Employee ] .

ex:ticket-1 a ex:Ticket ; ex:assignedTo ex:employee-1 .
ex:employee-1 a ex:Employee .
```

```sparql
PREFIX ex: <https://example.org/ontology/>
SELECT ?ticket ?owner WHERE {
  ?ticket a ex:Ticket ; ex:assignedTo ?owner .
}
```

## 验证

1. 解析语法；运行问题对应的查询，比对预期结果。
2. 若任务依赖 OWL 推理，用选定推理器检查一致性、不可满足类和预期蕴涵；记录 OWL profile 与推理器版本。只解析 OWL 文件不能证明这些检查通过。
3. 单独运行 SHACL。上例在无推理的显式数据图上：正常数据通过；删除负责人、增加第二负责人、删除员工类型均应失败。若启用 range 推理，最后一例可能通过，需按真实需求选择配置，而不是隐藏差异。
4. 增加身份冲突、单位不一致、历史/当前混淆与跨源同名样本。没有工具时只交付样例和预期，不能声称实际通过。

需要一条命令复现时使用[完整案例](executable-example.md)，其中模型、数据、shapes、查询与推理夹具分别保存；不要求每个业务任务都执行教学案例或采用其中所有技术。

## 来源与适用版本

以 [RDF 1.1](https://www.w3.org/TR/rdf11-concepts/)、[RDFS 1.1](https://www.w3.org/TR/rdf-schema/)、[OWL 2](https://www.w3.org/TR/owl2-primer/)、[SHACL 2017](https://www.w3.org/TR/shacl/) 和 [SPARQL 1.1](https://www.w3.org/TR/sparql11-query/) 为学习基线；实现时按所用工具确认支持范围。

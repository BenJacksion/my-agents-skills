# 知识工程模式

## 选择表达能力

- RDF 表达三元组；RDFS 提供类、子类及属性 domain/range；OWL 增加等价、互斥、限制等形式语义。Turtle 是序列化格式，不是额外的推理体系。
- 查询需要与推理需要分开：先确认能力问题能否用显式事实和 SPARQL 回答，再决定是否需要 OWL。
- 选择 OWL 2 profile 或更丰富表达前核对推理器支持、所需构造和数据规模；不默认 OWL Full。
- 稳定跨源实体优先分配 IRI；blank node 不当作跨数据集持久主键。`owl:sameAs` 表达强同一性，不用于模糊匹配或相似对象。

## 防止把语义当校验

- OWL 采用开放世界假设：未记录某关系不表示关系不存在；最小基数不会自动拒绝缺失字段。
- 不采用唯一名称假设：两个 IRI 不必指向不同个体。最大基数限制可能引出个体同一性；只有结合差异断言等条件才可能矛盾，不能当数据库唯一索引。
- RDFS/OWL 的 domain/range 是推理类型的依据，不是拒绝“错误类型”的输入规则。多个 domain 声明不是任选其一。
- 区分“全局本体不一致”和“某个类不可满足”；一个不可满足类未必使无该类实例的本体全局不一致。
- 用 SHACL 表达必填、数量、类型、枚举等数据要求，明确 target、待校验数据图、推理/预处理和严重级别。`sh:closed` 只关闭指定 shape 的属性集合，不是把整个世界改成闭世界。

## 最小示例

以下为自行构造的工单示例，非真实业务证据。目标：查询工单负责人；数据规则：每张工单恰有一个显式负责人，且负责人已声明为员工。

```turtle
@prefix ex: <https://example.org/ontology/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
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
2. 用选定推理器检查一致性、不可满足类和预期蕴涵；记录 OWL profile 与推理器版本。
3. 单独运行 SHACL。上例在无推理的显式数据图上：正常数据通过；删除负责人、增加第二负责人、删除员工类型均应失败。若启用 range 推理，最后一例可能通过，需按真实需求选择配置，而不是隐藏差异。
4. 增加身份冲突、单位不一致、历史/当前混淆与跨源同名样本。没有工具时只交付样例和预期，不能声称实际通过。

标准依据见[研究来源](../../../research.md)。

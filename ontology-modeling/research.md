# 本体建模研究：知识工程与业务操作层

研究日期：2026-09-18。检索与网页读取均使用 MCP AnySearch；优先采用 W3C、Stanford/Protégé 和 Palantir 官方资料。

## 1. 核心结论

本体建模不是把数据库表改名，也不是画一张名词关系图。它把某个领域的概念、实例、关系、含义和假设显式表达，使不同人和软件能够共享、查询、检验这些知识。[S1]

两条路线需要分开处理：

- 知识工程路线：以 RDF 表达事实，以 RDFS/OWL 表达概念和公理，以推理检验逻辑后果，以 SHACL 检验指定数据图是否满足输入或交换契约，以 SPARQL 回答问题。[S2–S6]
- Palantir 路线：将组织的数据资产映射为业务对象、属性和链接，再通过 Actions、Functions 与安全机制支撑业务决策和执行。[S8–S14]

共同点是共享业务含义；不同点是语义、身份机制、约束执行方式和运行职责。不能把 Foundry Object Type 直接当作 OWL Class，也不能把 Action 当作 RDF 属性或 OWL 推理规则。

## 2. 官方事实：知识工程路线

### 2.1 RDF、RDFS、OWL、SHACL、SPARQL 的职责

| 层 | 官方定义或能力 | 建模时的职责 |
| --- | --- | --- |
| RDF | 图由主语—谓语—宾语三元组组成。[S2] | 表达实例事实和资源之间的关系；Turtle 等是序列化方式，不是另一种本体语义 |
| RDFS | 为 RDF 提供类、属性、子类、子属性、domain/range 等词汇。[S3] | 声明基础类型与层级，并允许据此推导类型 |
| OWL 2 | 描述类、属性、个体及其逻辑公理；可表达等价、不相交、属性特性和限制。[S4] | 支撑自动分类、一致性检查和语义推理 |
| SHACL | 以 shapes 对数据图进行验证；例如值节点少于 minCount 会产生验证结果。[S5] | 检验必填、数量、类型、值域等明确的数据契约 |
| SPARQL | 查询 RDF 图；SELECT 返回变量绑定，CONSTRUCT 返回 RDF 图。[S6] | 将业务问题变成可运行查询并核对预期答案 |

以下是标准语义的综合解释，执行时应同时记录所用推理器、OWL profile 和验证配置：

- RDFS domain/range 通常用于推导类型，不是数据库式“类型不符就拒绝入库”。多个 domain 声明意味着同时属于这些类，而不是任选其一。[S3]
- OWL 采用开放世界假设：没有记录某个事实，不等于该事实为假。没有记录负责人不能单凭缺失数据断言“没有负责人”。[S4]
- OWL 不默认采用唯一名称假设：两个不同名字可能指向同一个个体；需要在确有依据时使用 DifferentIndividuals/differentFrom，不能把所有不同 IRI 自动视为不同业务实体。[S7]
- OWL 的存在限制不负责补出可见数据记录；最大基数限制也可能导致相等性推理，而不是直接产生数据库式重复值错误。逻辑一致不等于数据完整。[S4, S7]
- SHACL 对选定的数据图、目标节点和 shapes 进行检验；是否先进行推理、采用哪种 entailment、是否使用 sh:closed，必须明确。SHACL 不是自动把整个知识系统改成闭世界，也不等同于 OWL 一致性检查。[S5]
- 运行普通图匹配查询不能自动证明 OWL 公理已全部参与推理。查询无答案可能是缺数据、无相应 entailment 或确实不满足模式，不能直接写成领域事实为假。[S4, S6]

### 2.2 需求和建模方法

Stanford 的《Ontology Development 101》给出迭代流程：确定领域与范围、考虑复用、列术语、定义类与层级、定义属性、定义属性限制、创建实例，并通过应用和领域专家反馈持续修订。[S1]

其中 competency questions（能力问题）用于界定本体应当回答什么，也是后续评价模型是否具备足够信息的测试依据。没有唯一正确的本体；模型深度取决于用途。[S1]

该资料以早期 frame-based 建模为背景。其范围界定、术语与层级方法可以借鉴，但其中 slot/facet 不应未经语义转换就当成 OWL 或 SHACL。[S1]

## 3. 官方事实：Palantir 业务操作路线

### 3.1 对象、属性、链接、行动与函数

- Ontology 是位于平台集成数据资产之上的组织操作层，将数据集、虚拟表和模型连接到其现实业务对应物；同时包含语义元素与支持变化的操作元素。[S8]
- Object Type 是现实实体或事件的 schema；Object 是其具体实例。Property 表示该实体或事件的特征。Link Type 定义两个对象类型之间的关系；Link 是两个对象之间的关系实例。[S9]
- Action Type 定义用户能够一次进行的一组对象、属性值和链接编辑，还包括提交时发生的副作用行为。Action 是该定义的一次执行。[S9, S12]
- Functions 在服务端隔离环境执行逻辑，可读取对象属性、遍历链接、计算结果，并支持复杂 Ontology 编辑；复杂编辑可以通过 function-backed action 执行。[S13]
- 官方类型文档称其数据类型受到 RDF/OWL/XSD 概念启发；这不能推导出整个 Foundry Ontology 遵循 OWL 的开放世界、个体相等性或推理语义。[S9]

### 3.2 身份和数据映射

每个 Object Type 都需要 primary key，用于唯一标识其每个实例；title key 是显示名称，不是身份。数据源中的主键必须唯一，而且应确定性生成。每次构建使用随机数或行号生成不稳定主键，可能导致编辑丢失、链接消失。[S10]

Object Type 可选择 backing datasource，配置列到属性的映射；如果所有属性均由 Actions 填充，当前文档还支持无 backing datasource 的类型，但需要相应项目权限和对象安全策略。[S10]

Links 必须有清楚的数据映射。官方创建文档包括通过一侧外键引用另一侧主键的映射，以及多对多关系的数据源配置。[S11] 对关系是否应升格为对象，应由领域语义决定：若关系自身有时间、角色、状态、来源或操作生命周期，宜显式建模为关联/事件对象，而不是只保留一条裸链接。这一判断是方法综合，不是平台强制规则。

当前官方文档还支持 object-backed links，允许以中间对象保存关系元数据。文档同时明确：one-to-one cardinality 表示预期关系，但不被强制执行。因此图上的“1:1”不能替代实际数据质量和操作校验。[S11]

### 3.3 校验、权限与副作用

Submission criteria 可结合用户/群组、参数和对象信息控制 Action 是否可提交，并提供失败提示；官方建议使用 test run 验证条件求值。[S14]

权限不能简化成“能读就一定能写”或“Action 能见就一定能执行”。当前官方说明要求核对对象/链接及数据源可见性、submission criteria、编辑模式和相关编辑权限，并考虑 action log 的权限。[S15]

尤其要注意当前官方文档的安全边界：行列访问控制在 Action 调用时过滤可读内容，不自动延伸为写入保护；下游保护需要结合 markings、分类访问控制以及读写授权配置。[S15]

副作用也不是无条件的跨系统事务承诺：submission criteria 失败时不会触发副作用；通知收件人必须有相应数据权限；通知发送失败时，对象编辑仍可能成功。[S15] 因此通知、Webhook 和外部系统写入应分别定义失败处理、重试和补偿，不把 Action 中的对象编辑事务推广为所有外部副作用的原子性。

## 4. 两种路线的概念对照

下表是帮助沟通的近似对照，不是自动转换规范。

| 建模关切 | 知识工程 | Palantir | 不能省略的区别 |
| --- | --- | --- | --- |
| 类型 | RDFS/OWL Class | Object Type | 前者以类解释和公理为核心，后者包含平台 schema 和操作能力 |
| 实例 | RDF 资源 / OWL Individual | Object | IRI 与 primary key 的作用不同，不能复制唯一性假设 |
| 值特征 | RDF property；OWL datatype property | Property | 值类型、缺失和验证执行机制需独立说明 |
| 对象间关系 | RDF property；OWL object property | Link Type / Link | 图谓词的语义公理不等于链接数据映射 |
| 逻辑限制 | OWL 公理 | 业务逻辑或类型约束 | 不默认存在等价推理能力 |
| 数据质量 | SHACL shapes | 数据管道、value types、应用/Action 校验 | 需要明确在哪一层阻止或报告错误 |
| 变化 | 另行定义更新或应用协议 | Action Type / Action | OWL 公理本身不提供授权事务接口 |
| 运算 | 推理器、查询、外部程序 | Functions | 推理后果与程序业务计算不是同一概念 |
| 安全 | 应用/存储层安全，非 OWL 核心能力 | 对象/属性/数据源权限及 Action 授权 | 推理或查询结果同样可能泄露信息，需单独治理 |

## 5. 可执行建模流程（方法综合）

以下将 [S1] 的迭代方法、W3C 的语义边界和 Palantir 的操作能力组合成实践流程，不声称这是某家官方统一方法。

1. 明确用途与范围：列用户、决策、消费者、维护责任人和排除项。只做共享词汇或数据交换时，不默认增加 OWL 或 Actions。
2. 写能力问题和操作场景：每个问题记录输入、期望答案、所需证据；每个操作记录参与者、前置状态、目标状态和禁止条件。
3. 建术语表并检查复用：给出定义、同义词、正例、反例和来源；只在语义适配时复用，避免以名称相似判断等价。
4. 定义身份：区分业务实体、记录、版本、角色和事件；记录标识范围、跨源匹配、冲突策略、时间有效性，不直接以名字作主键或以 owl:sameAs 合并相似记录。
5. 建最小概念模型：分别列类型、实例、值属性、关系；仅真正的“每个 A 都是 B”使用子类，不把 part-of、状态或实例误建为继承。
6. 为每条关系标注方向、反向含义、双方类型、业务数量、时间、来源和缺失含义。需要自身生命周期的关系升格为对象/事件。
7. 分配规则层：逻辑公理 → OWL；指定数据图合格性 → SHACL；变更前置条件 → Action/应用协议；字段转换与质量修复 → 管道。相同业务规则若跨层出现，标出统一规则来源和一致性测试。
8. 按路线落地：知识工程路线记录 namespace、RDF 数据、OWL profile、推理器、SHACL targets 和 SPARQL；操作路线记录主键、属性/链接映射、读写权威、刷新与用户编辑冲突策略、Actions、Functions 和权限矩阵。
9. 以样例验证：正常、缺失、错类型、冲突身份、多个关系、越权、非法状态、重复提交、并发更新和副作用失败。实际运行与只提供测试设计必须分开标记。
10. 发布并演进：记录版本、弃用、数据迁移和消费者影响；随着能力问题与操作变化做小步修订，不先建立全企业“万能本体”。

## 6. 贯穿示例：工单—设备—人员

以下为教学示例，不是 Palantir 产品配置，也未在 Foundry 实例运行。

范围：维修团队识别待处理工单并指派负责人。能力问题：“设备 A 的开放工单分别由谁负责？”操作问题：“具有调度权限的人能否将开放工单 T 指派给在岗人员 U？”

### 6.1 概念与事实

- 类型：Ticket、Asset、Person。
- 值属性：ticketId、status、createdAt；personId、onDuty。
- 关系：Ticket concerns Asset；Ticket assignedTo Person。
- 身份：工单 ID 必须在约定组织范围内唯一；跨组织 ID 需加作用域。人员显示姓名不作为实体身份。

```turtle
@prefix ex: <https://example.org/maintenance/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ex:Ticket a owl:Class .
ex:Asset a owl:Class .
ex:Person a owl:Class .
ex:assignedTo a owl:ObjectProperty ;
    rdfs:domain ex:Ticket ; rdfs:range ex:Person .
ex:t1 a ex:Ticket ; ex:status "Open" ;
    ex:concerns ex:a1 ; ex:assignedTo ex:u1 .
ex:a1 a ex:Asset .
ex:u1 a ex:Person .
```

domain/range 表达类型语义，不能据此声称“任何错误类型的负责人都被拒绝”。如果交付数据必须恰好一个负责人，需要单独定义数据验证契约。

### 6.2 数据验证与查询

该 shape 只适用于这个明确的数据交换场景：所有交付 Ticket 必须显式给出一个 Person 负责人。若草稿或未指派工单也在图中，应缩小 target 或修改契约。

```turtle
@prefix ex: <https://example.org/maintenance/> .
@prefix sh: <http://www.w3.org/ns/shacl#> .

ex:TicketDeliveryShape a sh:NodeShape ;
    sh:targetClass ex:Ticket ;
    sh:property [
        sh:path ex:assignedTo ;
        sh:minCount 1 ; sh:maxCount 1 ; sh:class ex:Person
    ] .
```

```sparql
PREFIX ex: <https://example.org/maintenance/>
SELECT ?ticket ?assignee WHERE {
  ?ticket a ex:Ticket ; ex:concerns ex:a1 ; ex:status "Open" .
  OPTIONAL { ?ticket ex:assignedTo ?assignee }
}
```

样例图期望返回 t1/u1。OPTIONAL 用于保留当前图中没有负责人绑定的工单；未绑定不证明现实世界没有负责人。是否基于显式图或推理后图执行，要在测试中声明。

### 6.3 操作模型

| 项目 | 示例契约 |
| --- | --- |
| Object Types | Ticket、Asset、Person，各自稳定 primary key；姓名/描述仅作为显示值 |
| Links | Ticket→Asset、Ticket→Person，记录外键/关联数据映射与预期数量 |
| AssignTicket 输入 | ticket、assignee、可选的版本/幂等信息；是否支持该信息需按具体实现核对 |
| 前置条件 | 执行者有调度权限；ticket 为 Open；assignee 在岗；对象与相关数据按授权可见 |
| 变更 | 更新负责人关系，必要时记录指派事件；其编辑与来源刷新冲突策略另行定义 |
| 副作用 | 通知新负责人；发送失败不能直接声称指派已回滚 |
| 审计 | 执行者、时间、参数、前后状态、成功/失败及关联事件 |

最低验收：缺负责人时 SHACL 失败；两负责人时 maxCount 失败；正常查询答案正确；越权/关闭工单/不在岗人员的 Action 被拒绝；通知失败的对象状态和重试方式明确。这里是测试设计，不能替代实际推理器、SHACL 验证器或平台运行证据。

## 7. 常见陷阱与判断规则

- 把本体当表结构：先以问题和业务含义定义模型，再映射物理源。
- 把同义词建成多个类：如果含义一致，保留一个概念及别名；语义相近不等于等价。[S1]
- 把实例当子类：某一台设备是 Asset 的实例，不是 Asset 的子类。
- 以状态堆出大量类：只有分类、约束或关系的语义确实需要时才引入类，否则用属性或显式状态模型。[S1]
- 把所有关系设为传递、对称或 functional：这些是全局语义承诺，先写反例测试。
- 把 unknown、null、false、未适用混为一谈：必须在数据契约和操作协议中分别定义。
- 将 OWL 基数当必填校验：逻辑限制和已交付数据完整性分层处理。
- 草率使用 owl:sameAs：它表示强个体同一性，不是“可能相似”或“便于 join”。
- 使用非确定主键：当前 Palantir 文档明确指出可能损坏编辑和链接连续性。[S10]
- 只检查前端按钮权限：执行端前置条件、对象/属性可见性与写授权均需验证。[S15]
- 将操作成功等同外部系统同步成功：分别记录对象提交、副作用和外部状态。[S15]

## 8. 证据边界与未决事项

- Palantir、Stanford HTML 和 W3C GitHub RDF 文档已通过 AnySearch extract 读取。Stanford HTML 返回内容有长度截断，流程与能力问题段落可读取；不据此声称全文逐页审阅。
- W3C 的 RDF 1.1、RDFS、OWL 2、SHACL、SPARQL TR 页面及部分带日期页面在 AnySearch extract 返回 extract_failed；本文对应基础事实经 AnySearch 官方域定向搜索结果核对，保留正式规范 URL。不能将搜索片段验证说成完整规范审阅。
- 检索期间出现 RDF/SHACL 1.2 的在研文档。本研究以 RDF 1.1、OWL 2、SHACL 2017、SPARQL 1.1 作为稳定学习基线，不声称它们是所有产品的最新支持版本；RDF 1.2 GitHub 页面只用于补充阅读，部署前需要核对正式状态和工具兼容性。[S16]
- 本文不是性能基准、OWL profile 选型报告、完整 Foundry 权限设计或产品部署手册；复杂推理、跨本体集成及安全传播需补充实际工具和部署证据。
- 数据源刷新与用户编辑的冲突、并发版本控制、幂等、外部副作用重试/补偿是必须确认的设计问题，不保证 Foundry 在所有配置下自动实现。
- 本文示例未经过实际平台执行；源码/模型结构验证不代表业务规则已获领域专家确认。

### 本次已运行的检查

使用 RDFLib 7.6.0、pySHACL 0.40.1，在隔离依赖环境中执行：

- 本文 Turtle 与 SHACL 均可解析，SPARQL 返回预期的 t1/u1；正常数据通过，缺少负责人及多个负责人均未通过 SHACL。
- Skill 的知识工程参考示例也通过解析、查询与正常数据校验；缺失负责人、多个负责人、缺失员工类型均按预期失败。开启 RDFS 推理后，range 可补出员工类型，最后一例通过，验证了推理配置对校验结果的影响。
- Skill frontmatter、目录命名、UI 元数据及调用提示、本地相对链接、未完成占位和差异空白检查通过。

以上不是完整 OWL 推理验证，也不是 Foundry Action、权限或外部副作用测试；后者仍需连接真实环境执行。

## 9. 一手来源索引

| 编号 | 一手来源 | 本次核验方式 |
| --- | --- | --- |
| S1 | [Noy、McGuinness：Ontology Development 101](https://protege.stanford.edu/publications/ontology_development/ontology101-noy-mcguinness.html)；[Protégé 说明页](https://protegewiki.stanford.edu/wiki/Ontology101) | extract，HTML 部分截断 |
| S2 | [W3C RDF 1.1 Concepts](https://www.w3.org/TR/rdf11-concepts/) | 官方域搜索；extract 失败 |
| S3 | [W3C RDF Schema 1.1](https://www.w3.org/TR/rdf-schema/) | 官方域搜索；extract 失败 |
| S4 | [W3C OWL 2 Primer](https://www.w3.org/TR/owl2-primer/) | 官方域搜索；extract 失败 |
| S5 | [W3C SHACL Recommendation](https://www.w3.org/TR/shacl/) | 官方域搜索；extract 失败 |
| S6 | [W3C SPARQL 1.1 Query](https://www.w3.org/TR/sparql11-query/) | 官方域搜索；extract 失败 |
| S7 | [W3C Representing Specified Values in OWL](https://www.w3.org/2001/sw/BestPractices/OEP/SpecifiedValues-20050223/) | 官方域搜索；extract 失败；早期建模说明，不替代 OWL 2 规范 |
| S8 | [Palantir Ontology overview](https://palantir.com/docs/foundry/ontology/overview/) | extract |
| S9 | [Palantir Types reference](https://palantir.com/docs/foundry/object-link-types/type-reference/) | extract |
| S10 | [Palantir Create an object type](https://palantir.com/docs/foundry/object-link-types/create-object-type/) | extract |
| S11 | [Palantir Create a link type](https://palantir.com/docs/foundry/object-link-types/create-link-type/) | extract |
| S12 | [Palantir Action types overview](https://palantir.com/docs/foundry/action-types/overview/) | extract |
| S13 | [Palantir Functions overview](https://palantir.com/docs/foundry/functions/overview/) | extract |
| S14 | [Palantir Submission criteria](https://palantir.com/docs/foundry/action-types/submission-criteria/) | extract |
| S15 | [Palantir Action permissions](https://palantir.com/docs/foundry/action-types/permissions/) | extract |
| S16 | [W3C GitHub RDF 1.2 Concepts](https://w3c.github.io/rdf-concepts/spec/) | extract；在研文档辅助阅读，不用于断言正式发布状态 |

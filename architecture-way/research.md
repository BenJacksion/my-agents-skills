# 《架构之道：软件构建的设计方法》研究笔记

> 研究对象：Juval Löwy 的 *Righting Software: A Method for System and Project Design*，中文书名为《架构之道：软件构建的设计方法》。
>
> 研究日期：2026-09-10  
> 研究范围：The Method、系统设计、项目设计、易变性分解、可组合设计、组件/服务边界、系统设计与详细设计的边界、项目网络、关键路径、时间/成本/风险、多种项目方案、核心团队、架构验证、垂直切片、项目执行与反馈。

## 1. 研究口径与证据分级

本文优先使用以下来源：

- Juval Löwy、IDesign 的官方书籍页、文章、培训页和演讲材料；
- 出版社/出版平台的书籍目录、样章和书籍介绍；
- 作者本人参加的专业访谈，包括 Software Engineering Radio；
- 由专业媒体对作者或本书进行的访谈/书评，仅作为补充。

文中每条关键结论都标注：

- **原文明确主张**：来源直接表达了该观点，或出版社目录明确列出该方法/章节；
- **综合推断**：根据多个来源归纳出的工程含义，不把推断冒充为作者原话。

公开资料并未完整公开全书所有正文。因此，涉及“核心团队的精确岗位矩阵”“架构验证的完整检查表”等内容时，本文会明确说明证据边界。

## 2. 核心结论：The Method 是两种设计的联动

### 2.1 The Method 的双重对象

**结论｜原文明确主张｜来源类型：IDesign 官方方法概览 PDF｜原始链接：[The Method: System and Project Design](https://www.idesign.net/Download/IDesign-Method-Management-Overview.pdf)**

The Method 同时处理两件事：

1. **系统设计（system design）**：决定系统由哪些部分构成、各部分如何协作，以及如何用结构隔离易变性；
2. **项目设计（project design）**：把系统设计转化为可执行的项目网络，安排活动、依赖、资源、时间、成本和风险。

作者的关键立场不是“先画架构、再把任务丢给项目经理”，而是把系统结构和交付路径作为一个相互约束的整体来设计。系统设计决定项目中有哪些工作；项目设计反过来检验系统分解是否可实施。

### 2.2 这不是某一种生命周期模型

**结论｜原文明确主张｜来源类型：IDesign 官方方法概览 PDF、作者专业访谈｜原始链接：[The Method PDF](https://www.idesign.net/Download/IDesign-Method-Management-Overview.pdf)；[Software Engineering Radio 第 407 期访谈](https://se-radio.net/2020/04/episode-407-juval-lowy-on-righting-software/)**

The Method 是设计方法，不等同于瀑布、Scrum 或其他单一生命周期。它关注的是：

- 如何形成足够可靠的系统结构；
- 如何把结构转换成可分析的项目计划；
- 如何在执行中用实际反馈修正设计和计划。

因此，它可以嵌入不同的交付流程；流程迭代并不会自动替代系统设计和项目设计。

### 2.3 方法的真正交付物

**结论｜综合推断｜来源类型：IDesign 方法概览、出版社目录、IDesign 培训材料｜原始链接：[The Method PDF](https://www.idesign.net/Download/IDesign-Method-Management-Overview.pdf)；[InformIT 书籍页](https://www.informit.com/store/righting-software-a-method-for-system-and-project-design-9780137529313)；[Project Design Master Class](https://www.idesign.net/Training/Project-Design-Master-Class)**

The Method 的交付物可以理解为三层：

1. **系统结构**：组件/服务、职责、接口、依赖和部署关系；
2. **项目网络**：设计、实现、集成、测试等活动及其依赖；
3. **可校正的执行模型**：对进度、投入、预测、风险和纠偏动作的持续跟踪。

换言之，架构不是一张静态图，项目计划也不是脱离架构的甘特图；二者共同形成“可建造、可测量、可调整”的系统交付模型。

## 3. 基于易变性分解

### 3.1 分解轴不是功能清单，而是变化位置

**结论｜原文明确主张｜来源类型：IDesign 官方方法概览 PDF、出版社软件系统分解样章｜原始链接：[The Method PDF](https://www.idesign.net/Download/IDesign-Method-Management-Overview.pdf)；[Software System Decomposition](https://www.informit.com/articles/article.aspx?p=2995357)**

系统分解的核心问题不是“有哪些名词、页面或数据库表”，而是：

> 哪些决策、规则、技术、外部依赖或实现细节最可能变化？这些变化能否被限制在少数组件或服务内？

系统设计应把易变部分隔离起来，使变化尽量表现为替换、扩展或重新组合，而不是牵动整个系统。

### 3.2 易变性是结构化的设计输入

**结论｜综合推断｜来源类型：IDesign 方法概览、书籍目录中的“Volatility”章节结构｜原始链接：[The Method PDF](https://www.idesign.net/Download/IDesign-Method-Management-Overview.pdf)；[O’Reilly 书籍页](https://www.oreilly.com/library/view/righting-software/9780137529320/)**

可以把易变性分析转成以下设计步骤：

1. 从需求、约束和环境中识别可能变化的因素；
2. 判断变化的影响范围、频率、风险和独立演进需求；
3. 将变化因素封装在边界内；
4. 让稳定部分依赖抽象契约，而不是依赖易变实现；
5. 以组合和替换验证边界是否真的有效。

这里的“变化”不只包括业务规则，也包括技术平台、供应商、协议、存储方式、部署环境、法规政策和性能策略。

### 3.3 易变性分解的价值

**结论｜原文明确主张｜来源类型：出版社软件系统分解样章｜原始链接：[Software System Decomposition](https://www.informit.com/articles/article.aspx?p=2995357)**

合理的边界应降低变化的传播半径。其工程收益包括：

- 变更更容易局部化；
- 团队可以围绕服务或组件形成较清晰的责任；
- 测试、部署和替换的范围更可控；
- 项目网络中的并行工作更容易成立。

但“拆得更细”不是目标。若边界导致大量跨服务协同、共享内部状态或分布式事务，变化反而会扩散，系统会变成分布式单体。

## 4. 可组合设计

### 4.1 组件是可组合的行为单元

**结论｜原文明确主张｜来源类型：IDesign 官方方法概览 PDF、出版社软件系统分解样章｜原始链接：[The Method PDF](https://www.idesign.net/Download/IDesign-Method-Management-Overview.pdf)；[Software System Decomposition](https://www.informit.com/articles/article.aspx?p=2995357)**

The Method 强调通过组件和服务的组合来构成系统行为。组件不是仅按代码目录划分的容器，而是应当：

- 有清晰职责；
- 通过契约与外部协作；
- 隐藏内部实现；
- 可以被替换、重组或复用；
- 在组合时保持依赖方向和变化隔离。

可组合性把架构从“层级图”提升为“行为组合模型”：系统行为来自组件之间的受控协作，而不是来自任意模块间的调用堆叠。

### 4.2 组合必须服从契约和边界

**结论｜综合推断｜来源类型：IDesign 方法概览、出版社软件系统分解样章、出版社“服务契约设计”章节目录｜原始链接：[The Method PDF](https://www.idesign.net/Download/IDesign-Method-Management-Overview.pdf)；[Software System Decomposition](https://www.informit.com/articles/article.aspx?p=2995357)；[InformIT 书籍页](https://www.informit.com/store/righting-software-9780136524038)**

可组合设计不是“任何组件都能调用任何组件”。组合质量取决于：

- 契约是否稳定、最小且表达真实职责；
- 调用方是否只依赖契约，而不依赖内部实现；
- 数据和控制流是否穿越了过多边界；
- 一个组件的变化是否迫使多个组件同步修改；
- 组合后的运行时行为是否可观察、可测试、可部署。

因此，架构评审应同时看静态依赖图和变化传播路径。

## 5. 组件与服务边界

### 5.1 边界的首要依据

**结论｜综合推断｜来源类型：IDesign 易变性分解材料、出版社软件系统分解样章、项目设计材料｜原始链接：[The Method PDF](https://www.idesign.net/Download/IDesign-Method-Management-Overview.pdf)；[Software System Decomposition](https://www.informit.com/articles/article.aspx?p=2995357)；[Project Design Master Class](https://www.idesign.net/Training/Project-Design-Master-Class)**

在 The Method 语境下，组件/服务边界应优先回答四个问题：

1. 这部分是否有相对独立的变化原因？
2. 这部分是否可以用稳定契约对外提供能力？
3. 这部分是否能由相对独立的团队或活动负责？
4. 这部分是否能在系统运行和项目交付中被独立验证？

“一个业务名词一个服务”或“一个数据库表一个服务”都不是充分原则。边界应同时满足变化隔离、行为完整性、协作成本和可验证性。

### 5.2 服务边界与项目边界相互影响

**结论｜原文明确主张｜来源类型：IDesign 官方方法概览 PDF、IDesign 官方服务页｜原始链接：[The Method PDF](https://www.idesign.net/Download/IDesign-Method-Management-Overview.pdf)；[IDesign Services](https://www.idesign.net/Services)**

服务边界不仅影响运行时架构，也影响：

- 服务开发者的责任范围；
- 设计、实现、测试和部署活动的划分；
- 并行开发能否成立；
- 集成点数量和等待关系；
- 进度、成本、风险的估算。

这也是系统设计必须参与项目设计的原因：若一个服务需要很多团队共同修改，或服务间依赖形成密集网络，系统边界和项目网络都需要重新审视。

### 5.3 不要把微服务数量当作架构质量

**结论｜原文明确主张｜来源类型：出版社软件系统分解样章｜原始链接：[Software System Decomposition](https://www.informit.com/articles/article.aspx?p=2995357)**

IDesign 的公开材料将微服务的关键风险描述为分布式单体：服务表面上独立，实际上共享内部状态、强耦合调用或必须同步发布。由此可得一个重要约束：

- 边界应减少耦合，而不是制造更多网络跳转；
- 服务应围绕完整行为和稳定契约，而不是围绕任意代码片段；
- 只有能带来独立演进、独立验证或独立责任的边界，才值得承担分布式系统成本。

## 6. 系统设计与详细设计的边界

### 6.1 系统设计解决“整体如何成立”

**结论｜原文明确主张｜来源类型：出版社目录、IDesign 方法概览 PDF｜原始链接：[InformIT 书籍页](https://www.informit.com/store/righting-software-a-method-for-system-and-project-design-9780137529313)；[The Method PDF](https://www.idesign.net/Download/IDesign-Method-Management-Overview.pdf)**

系统设计应至少确定：

- 系统的主要组件/服务；
- 每个部分的职责和边界；
- 组件之间的接口与交互；
- 关键依赖、资源和部署关系；
- 哪些变化被隔离、哪些约束必须保持；
- 如何通过代表性实现验证架构；
- 这些结构如何转成项目活动和依赖。

系统设计的判断对象是整体性质：耦合、内聚、可变性、可部署性、可验证性、并行性和风险。

### 6.2 详细设计解决“单个部分如何实现”

**结论｜原文明确主张｜来源类型：出版社目录｜原始链接：[InformIT 书籍页](https://www.informit.com/store/righting-software-a-method-for-system-and-project-design-9780137529313)**

公开目录把“系统设计”和“详细设计”作为不同阶段/章节，并单列服务契约设计、组件详细设计、并发和持久化等内容。这表明二者边界不是“架构图”和“代码”之间的模糊分界，而是不同层次的决策：

- **系统设计**：决定有哪些责任单元、它们如何组合、依赖如何传播；
- **详细设计**：决定责任单元内部的类、算法、并发、持久化和实现细节。

详细设计可以展开系统设计，但不应偷偷改变系统边界。若详细设计发现一个服务无法独立实现、契约不稳定或依赖过密，应把问题反馈到系统设计层。

### 6.3 “足够详细”而非“全部先设计完”

**结论｜综合推断｜来源类型：IDesign 方法概览、IDesign 垂直切片材料、专业访谈｜原始链接：[The Method PDF](https://www.idesign.net/Download/IDesign-Method-Management-Overview.pdf)；[IDesign Services](https://www.idesign.net/Services)；[Software Engineering Radio 第 407 期访谈](https://se-radio.net/2020/04/episode-407-juval-lowy-on-righting-software/)**

系统设计的完成标准不是提前写完每个类，而是已经足够明确，可以：

- 设计项目网络；
- 进行初始估算和风险分析；
- 组织核心团队；
- 实现一个有代表性的端到端切片；
- 在切片中暴露结构性问题。

因此，系统设计和详细设计之间应保留反馈通道，而不是把两者当作一次性瀑布闸门。

## 7. 项目设计：从架构到项目网络

### 7.1 项目不是任务清单，而是依赖网络

**结论｜原文明确主张｜来源类型：IDesign 官方方法概览 PDF、IDesign Project Design 培训页｜原始链接：[The Method PDF](https://www.idesign.net/Download/IDesign-Method-Management-Overview.pdf)；[Project Design Master Class](https://www.idesign.net/Training/Project-Design-Master-Class)**

项目设计把工作表示为活动网络：

- 节点代表设计、实现、测试、集成、部署或其他活动；
- 边代表前置关系、资源约束或交付依赖；
- 活动具有时间、投入、责任和风险属性；
- 网络结构决定哪些工作可以并行、哪些工作必须等待。

这种表达比简单任务列表更适合分析软件项目，因为软件工作的困难往往来自依赖关系和等待，而不只是工作项数量。

### 7.2 关键路径决定最短交付时间

**结论｜原文明确主张｜来源类型：IDesign 官方方法概览 PDF、IDesign 项目设计培训材料｜原始链接：[The Method PDF](https://www.idesign.net/Download/IDesign-Method-Management-Overview.pdf)；[Righting Software 2022 演讲材料](https://sddvault.s3.amazonaws.com/presentation-slides/sdd2022/Righting%20Software.pdf)**

在项目网络中，关键路径是决定项目最短持续时间的约束链。它带来几个实际判断：

- 缩短非关键路径活动，不一定缩短项目；
- 关键路径上的依赖、等待和资源冲突需要优先处理；
- 新增人员不必然缩短关键路径，反而可能增加协调成本；
- 架构边界改变后，项目网络和关键路径也会改变。

“还有多少任务”不如“剩余关键路径是什么”更能说明项目还需要多久。

### 7.3 时间、成本和风险是联动变量

**结论｜原文明确主张｜来源类型：IDesign 官方方法概览 PDF、IDesign 项目设计培训页｜原始链接：[The Method PDF](https://www.idesign.net/Download/IDesign-Method-Management-Overview.pdf)；[Project Design Master Class](https://www.idesign.net/Training/Project-Design-Master-Class)**

项目设计需要同时估算：

- **时间**：活动持续时间、等待、关键路径和交付日期；
- **成本**：人员投入、外部资源、返工和协调成本；
- **风险**：技术不确定性、集成风险、人员连续性、依赖和估算误差。

三者不是独立报表。为了缩短时间而增加并行活动，可能提高集成和协调风险；为了降低风险而提前做验证，可能增加前期成本，却减少后期返工。

### 7.4 计划应显式表达风险，而不是隐藏不确定性

**结论｜综合推断｜来源类型：IDesign 项目设计材料、出版社书籍页中的项目计划与风险相关章节｜原始链接：[Project Design Master Class](https://www.idesign.net/Training/Project-Design-Master-Class)；[InformIT 书籍页](https://www.informit.com/store/righting-software-a-method-for-system-and-project-design-9780137529313)**

The Method 的项目网络适合把风险放进结构中处理：

- 对高不确定性活动使用验证性活动，而不是只填一个乐观工期；
- 识别会阻塞多个下游活动的依赖；
- 区分设计不确定性、实现不确定性和集成不确定性；
- 观察关键路径是否因风险事件而转移；
- 为高影响风险设计替代路径或决策点。

这比在计划末尾附一张静态风险清单更有用，因为风险会改变网络本身。

## 8. 多种可行的项目方案

### 8.1 方案空间，而不是唯一计划

**结论｜原文明确主张｜来源类型：IDesign 官方方法概览 PDF、IDesign 项目设计培训页｜原始链接：[The Method PDF](https://www.idesign.net/Download/IDesign-Method-Management-Overview.pdf)；[Project Design Master Class](https://www.idesign.net/Training/Project-Design-Master-Class)**

对于同一系统设计，通常可以形成多种可行项目方案，例如：

- 先做更多系统设计和验证，再扩大实现；
- 尽早做垂直切片，以较早获得架构证据；
- 按服务并行推进；
- 先交付关键路径上的核心能力；
- 以不同团队规模、交付日期或风险容忍度换取不同的时间/成本组合。

项目设计的任务不是寻找“唯一正确排期”，而是找出满足约束的方案空间，并让利益相关者理解各方案的代价。

### 8.2 方案选择是决策问题

**结论｜综合推断｜来源类型：IDesign 方法概览、项目设计培训材料｜原始链接：[The Method PDF](https://www.idesign.net/Download/IDesign-Method-Management-Overview.pdf)；[Project Design Master Class](https://www.idesign.net/Training/Project-Design-Master-Class)**

可把方案比较成一组显式权衡：

| 方案维度 | 需要回答的问题 |
| --- | --- |
| 交付时间 | 哪条关键路径、哪些依赖决定日期？ |
| 成本 | 需要多少持续投入，额外协调成本是多少？ |
| 风险 | 哪些未知被提前验证，哪些风险被推迟？ |
| 架构质量 | 是否仍保持边界、可替换性和可组合性？ |
| 团队连续性 | 是否需要频繁换人、拆分或合并责任？ |
| 反馈速度 | 多早能得到端到端运行证据？ |

最便宜或最快的静态方案未必是总体成本最低的方案；应比较返工、延期和风险暴露后的总成本。

## 9. 核心团队与角色

### 9.1 公开资料明确的角色类别

**结论｜原文明确主张｜来源类型：出版社书籍页、IDesign 官方服务页和培训页｜原始链接：[InformIT 书籍页](https://www.informit.com/store/righting-software-a-method-for-system-and-project-design-9780137529313)；[IDesign Services](https://www.idesign.net/Services)；[Project Design Master Class](https://www.idesign.net/Training/Project-Design-Master-Class)**

公开资料明确出现或反复强调的角色类别包括：

- **系统设计师/架构师**：负责系统结构、关键技术决策、易变性隔离、架构一致性和设计验证；
- **项目经理/项目设计责任人**：负责把系统结构转成项目网络，处理活动、依赖、资源、进度、成本和风险；
- **服务/组件开发者**：负责具体服务或组件的详细设计、实现、测试和交付；
- **客户/业务代表**：提供目标、约束、优先级和验收反馈，参与方案权衡。

书籍目录还单列“项目初始 staffing”“服务与开发者”“规划角色与责任”等内容，说明人员配置和责任分配是项目设计的一部分，不是项目开始后临时补齐的人事问题。

### 9.2 核心团队的职责不是岗位名称本身

**结论｜综合推断｜来源类型：IDesign 服务说明、出版社书籍页、项目设计材料｜原始链接：[IDesign Services](https://www.idesign.net/Services)；[InformIT 书籍页](https://www.informit.com/store/righting-software-a-method-for-system-and-project-design-9780137529313)；[Project Design Master Class](https://www.idesign.net/Training/Project-Design-Master-Class)**

一个有效的核心团队至少要覆盖四类决策：

1. **结构决策**：系统为何这样分解，边界如何保持；
2. **交付决策**：哪些活动先做，如何形成可并行网络；
3. **实现决策**：服务内部如何落地，契约和详细设计是否可行；
4. **反馈决策**：出现新证据时，谁有权修改架构、计划、资源或范围。

核心团队应尽早形成，并保持足够的连续性。否则架构决策、项目计划和实现反馈会在不同人之间传递，导致责任断裂和返工。

### 9.3 证据边界

**结论｜原文明确主张｜来源类型：出版商公开目录与官方公开材料的证据边界｜原始链接：[InformIT 书籍页](https://www.informit.com/store/righting-software-a-method-for-system-and-project-design-9780137529313)；[O’Reilly 书籍页](https://www.oreilly.com/library/view/righting-software/9780137529320/)**

目前可公开核验的目录和官方摘要能够确认角色主题，但不能据此声称作者规定了一个适用于所有组织的固定岗位表。实际团队规模、是否由架构师兼任技术负责人、客户代表的具体职责，都需要结合项目约束决定。

## 10. 架构验证与垂直切片

### 10.1 验证是系统设计的一等活动

**结论｜原文明确主张｜来源类型：出版社目录、IDesign 官方培训/服务材料｜原始链接：[InformIT 书籍页](https://www.informit.com/store/righting-software-a-method-for-system-and-project-design-9780137529313)；[IDesign Services](https://www.idesign.net/Services)**

出版社目录将“设计验证”列为系统设计的重要内容；IDesign 的服务说明明确把架构服务延伸到“垂直切片实现”，用运行中的代表性路径来检验设计和技术选型。

这说明架构验证不是文档审阅的同义词，而是要获得关于系统能否真实运行、组合和交付的证据。

### 10.2 垂直切片的含义

**结论｜综合推断｜来源类型：IDesign 官方服务页、IDesign 演讲材料、专业访谈｜原始链接：[IDesign Services](https://www.idesign.net/Services)；[Righting Software 2022 演讲材料](https://sddvault.s3.amazonaws.com/presentation-slides/sdd2022/Righting%20Software.pdf)；[Software Engineering Radio 第 407 期访谈](https://se-radio.net/2020/04/episode-407-juval-lowy-on-righting-software/)**

垂直切片不是只完成某一层的横向代码，而是沿一条有代表性的端到端行为，贯穿必要的组件/服务、接口、数据、运行时和测试。其验证对象至少包括：

- 组件边界是否足以支撑真实行为；
- 服务契约是否可组合；
- 关键技术选型是否能工作；
- 构建、部署、观测和测试链路是否可用；
- 团队是否能按预期责任边界协作；
- 项目网络中的活动顺序和估算是否合理。

### 10.3 为什么垂直切片应尽早出现

**结论｜综合推断｜来源类型：IDesign 官方服务页与项目设计材料｜原始链接：[IDesign Services](https://www.idesign.net/Services)；[Project Design Master Class](https://www.idesign.net/Training/Project-Design-Master-Class)**

垂直切片把两类未知提前暴露：

- **系统未知**：边界、契约、技术和运行时组合是否成立；
- **项目未知**：活动依赖、协作方式、构建部署、测试和交付节奏是否成立。

因此它是架构验证和项目设计验证的交叉点。若切片失败，优先反馈到系统设计和项目网络，而不是继续按原计划扩大实现规模。

## 11. 项目执行与反馈

### 11.1 执行不是照计划机械推进

**结论｜原文明确主张｜来源类型：IDesign 官方服务页、IDesign 项目设计培训材料、出版社书籍页｜原始链接：[IDesign Services](https://www.idesign.net/Services)；[Project Design Master Class](https://www.idesign.net/Training/Project-Design-Master-Class)；[InformIT 书籍页](https://www.informit.com/store/righting-software-a-method-for-system-and-project-design-9780137529313)**

公开材料把项目跟踪、进度与投入、状态报告、预测和纠偏作为项目设计/管理的一部分。执行过程中至少要持续观察：

- 活动完成情况和剩余工作；
- 实际投入与原估算的偏差；
- 关键路径是否变化；
- 集成点和阻塞依赖是否出现；
- 垂直切片和测试提供了什么新证据；
- 架构边界是否仍能保持；
- 风险是否已经转化为问题或新约束。

### 11.2 反馈回路

**结论｜综合推断｜来源类型：IDesign 服务说明、项目设计材料、作者专业访谈｜原始链接：[IDesign Services](https://www.idesign.net/Services)；[Project Design Master Class](https://www.idesign.net/Training/Project-Design-Master-Class)；[Software Engineering Radio 第 407 期访谈](https://se-radio.net/2020/04/episode-407-juval-lowy-on-righting-software/)**

把这些材料综合起来，The Method 的执行反馈回路可以表示为：

```text
系统设计
  -> 项目网络与方案
  -> 核心团队执行
  -> 垂直切片、测试、集成和进度证据
  -> 更新架构判断、估算、依赖、风险和资源
  -> 继续执行或重新设计
```

这里的反馈不是“每次迭代都必须重写架构”，而是要求新证据能够进入决策模型，并在必要时改变边界、顺序、方案或资源配置。

### 11.3 架构责任要贯穿执行

**结论｜综合推断｜来源类型：IDesign Services、出版社软件系统分解样章｜原始链接：[IDesign Services](https://www.idesign.net/Services)；[Software System Decomposition](https://www.informit.com/articles/article.aspx?p=2995357)**

如果架构师只在项目开始时画图，执行阶段由各团队自由解释，易变性隔离和服务契约很快会被局部便利侵蚀。更符合公开材料的做法是：

- 架构责任参与垂直切片和关键集成；
- 服务/组件实现接受边界和契约检查；
- 进度风险与架构风险放在同一项目网络中观察；
- 对架构偏差及时做局部修正或重新评估方案。

## 12. 一套可操作的阅读与应用框架

以下不是作者原文中的固定清单，而是根据上述资料提炼的应用顺序。

### A. 做系统设计

1. 写清系统目标、约束和成功条件；
2. 列出可能变化的业务、技术、外部依赖和运行环境；
3. 按变化原因和行为责任形成组件/服务候选；
4. 为边界定义稳定、最小、可测试的契约；
5. 检查组合后的依赖、数据流、部署和运行时性质；
6. 选择一条高价值、高风险的端到端行为作为垂直切片；
7. 用切片验证架构和关键技术。

### B. 做项目设计

1. 将系统设计、详细设计、实现、测试、集成和部署拆成活动；
2. 明确活动之间的前置关系和责任归属；
3. 建立项目网络并识别关键路径；
4. 为高不确定性活动加入验证或替代方案；
5. 在时间、成本、风险、团队连续性和反馈速度之间比较多种方案；
6. 选择方案后定义跟踪指标和纠偏触发条件。

### C. 执行和调整

1. 先交付能产生架构证据的垂直切片；
2. 用实际投入、进度、集成结果和测试结果校正估算；
3. 发现边界或依赖问题时回到系统设计层；
4. 发现活动或资源问题时回到项目网络层；
5. 继续跟踪关键路径、风险和架构一致性，直到系统完成。

## 13. 主要判断与局限

### 13.1 最值得保留的判断

**结论｜综合推断｜来源类型：多份官方材料与作者访谈的交叉归纳｜原始链接：见下方“来源列表”**

本书最有辨识度的贡献不是又提供一种画组件图的符号，而是把以下两个通常分离的决策面连接起来：

- 系统如何按易变性分解，形成可组合、可替换的结构；
- 项目如何按活动网络组织，形成可分析、可验证、可调整的交付路径。

这个连接使架构质量直接影响项目时间、成本、风险和团队协作，也使项目执行中的证据能够反过来检验架构。

### 13.2 不能过度解读的地方

**结论｜原文明确主张｜来源类型：公开资料范围说明｜原始链接：[Righting Software 官方站点](https://rightingsoftware.org/)；[InformIT 书籍页](https://www.informit.com/store/righting-software-a-method-for-system-and-project-design-9780137529313)**

公开页面、目录、摘要和演讲材料不足以完整重建全书的：

- 全部术语定义；
- 每一种项目网络计算方式；
- 核心团队的固定组织结构；
- 设计验证的完整模板；
- 所有示例项目的详细数据。

因此本文对这些部分采用“证据明确处直述，跨来源归纳处标注综合推断”的写法，没有把普通博客的二手解释当作主要依据。

## 14. 来源列表

### 作者与 IDesign 官方来源

1. [IDesign：Righting Software 书籍/作者资源页](https://www.idesign.net/Books/Righting-Software)  
   来源类型：作者/咨询公司官方书籍页。用于确认书籍定位、作者及配套资源。

2. [Righting Software 官方站点](https://rightingsoftware.org/)  
   来源类型：作者/书籍官方站点。用于确认 The Method 的书籍语境及配套材料入口。

3. [The Method: System and Project Design](https://www.idesign.net/Download/IDesign-Method-Management-Overview.pdf)  
   来源类型：IDesign 官方方法概览 PDF。核心依据，用于系统设计、项目设计、易变性、项目网络、关键路径、时间/成本/风险及多方案。

4. [IDesign Services](https://www.idesign.net/Services)  
   来源类型：IDesign 官方服务说明。用于架构落地、垂直切片、项目跟踪、状态报告、预测和纠偏等实践证据。

5. [Software System Decomposition](https://www.informit.com/articles/article.aspx?p=2995357)  
   来源类型：出版社公开样章。用于功能分解的局限、变化传播、服务边界、组合行为和系统级测试风险。

6. [Project Design Master Class](https://www.idesign.net/Training/Project-Design-Master-Class)  
   来源类型：IDesign 官方培训课程页。用于项目网络、依赖、关键路径、时间/成本/风险和项目方案设计。

7. [Righting Software 2022 演讲材料](https://sddvault.s3.amazonaws.com/presentation-slides/sdd2022/Righting%20Software.pdf)  
   来源类型：IDesign/作者演讲材料。用于交叉核对项目设计、活动网络、关键路径、验证和实施活动。

### 出版社与出版平台

8. [InformIT：Righting Software 书籍页](https://www.informit.com/store/righting-software-a-method-for-system-and-project-design-9780137529313)  
   来源类型：出版社平台书籍页。用于确认正式书名、作者、出版信息及公开目录主题，包括系统设计、设计验证、详细设计、项目设计、初始 staffing、服务与开发者、跟踪和纠偏。

9. [O’Reilly：Righting Software](https://www.oreilly.com/library/view/righting-software/9780137529320/)  
    来源类型：出版平台书籍页。用于核对书籍目录与章节入口；相关章节包括[系统设计](https://www.oreilly.com/library/view/righting-software/9780137529320/ch02.xhtml)、[设计验证](https://www.oreilly.com/library/view/righting-software/9780137529320/ch05.xhtml)和[服务契约设计](https://www.oreilly.com/library/view/righting-software/9780137529320/ch08.xhtml)。

### 作者本人及专业访谈

10. [Software Engineering Radio 第 407 期：Juval Löwy on Righting Software](https://se-radio.net/2020/04/episode-407-juval-lowy-on-righting-software/)  
    来源类型：作者本人参加的专业播客访谈。用于交叉理解 The Method、系统设计、项目设计及作者对软件工程实践的解释。

11. [InfoQ：Righting Software 书评/作者观点整理](https://www.infoq.com/articles/book-review-righting-software/)  
    来源类型：专业媒体书评/访谈材料。作为补充来源，用于核对作者观点的传播语境；不作为主要证据。

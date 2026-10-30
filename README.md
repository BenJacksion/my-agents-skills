# 产品与系统架构 Agents & Skills

把产品思维、系统架构、企业应用架构、本体建模和项目设计方法转化为可调用、可交接、可验证的 Skills 与 Agents。Skill 保存专业方法，Agent 负责角色和收敛，流程层负责阶段路由。

## 从哪里开始

已有明确问题时，直接选择专项 Skill；需要跨多个专业问题收敛时，再使用综合入口。下表中的链路可按已有证据和任务范围裁剪。

| 当前问题 | 能力域与综合入口 | 常用专项 |
| --- | --- | --- |
| 用户需要什么、怎样判断产品有效 | [产品思维](domains/product-thinking/README.md) / `$product-thinking` | 发现、结果与指标、假设实验、策略与优先级 |
| 系统边界是什么、有哪些概念和架构选项 | [系统架构](domains/system-architecture-product-design/README.md) / `$complex-system-architecture` | 系统思维、现状映射、概念、分解、治理、决策优化 |
| 软件如何隔离变化、组合并按计划交付 | [《架构之道》](domains/architecture-way/README.md) / `$architecture-way` | 易变性分解、可组合架构、架构验证、项目设计 |
| 业务如何落实到应用、数据、运行和部署 | [企业应用架构](domains/enterprise-application-architecture/README.md) / `$enterprise-application-architecture` | 领域建模、5 视图、演进、分布式、云交付、数据平台 |
| 概念、身份、关系和规则如何统一 | [本体建模](domains/ontology-modeling/README.md) / `$ontology-modeling` | RDF/OWL/SHACL、对象—关系—行动、跨模型映射 |
| 工作跨阶段，需明确顺序和交接 | [软件工程流程](orchestration/README.md) / `$software-engineering-process` | 多 Skill 调度、工程任务纪律、阶段门与回退 |

例如：

- “使用 `$product-assumption-testing`，识别这个方案的高风险假设，设计一周内可完成的验证。”
- “使用 `$volatility-decomposition`，根据这些历史变更检查模块边界，给出最小调整与验证方式。”
- “使用 `$software-engineering-process`，把已有产品目标交接为应用架构和项目计划，只补缺少的输入。”

## 阅读与调用

1. 明确问题后先读取目标 `SKILL.md`；只加载它要求的模式参考。
2. 需要定位能力时看对应域的 `capability-catalog.md`；需要角色分工或跨阶段交接时再看 `agent-contracts.md` 和 `agents/`。
3. 需要核查方法出处时读取 `research.md`、章节笔记或原始资料。研究记录保留其采集日期与证据限制。
4. 只交付当前问题所需产物。事实、假设和决策分开记录，未运行的验证标记为计划；达到当前任务的完成条件后结束。

Agent frontmatter 的 `skills` 是能力清单，按当前问题加载；角色名称不要求启动独立进程。下游沿用证据和未知项，不能把上游假设升级为事实。

## 目录与复用边界

各能力域平级维护，来源和专业方法各自归属。每个域都有说明、能力目录和交接契约；流程层串联已有能力，不另建一套专业方法。

```text
.
├── domains/                         # 专业能力域
│   ├── product-thinking/
│   ├── system-architecture-product-design/
│   ├── architecture-way/
│   ├── enterprise-application-architecture/
│   └── ontology-modeling/
├── orchestration/                   # 流程编排、阶段门与工程纪律
├── docs/                            # 跨域使用指南
├── scripts/                         # 仓库校验工具
├── tests/                           # 工具回归测试
├── AGENTS.md                        # 维护规范
└── README.md                        # 使用入口
```

- `skills/<skill-name>/`：执行入口，以及按需读取的参考和 UI 元数据。
- `agents/`：角色协议；它们是 Markdown 定义，需由支持相应角色的运行环境调用。
- `research.md`、章节笔记、`source-materials/`：证据及方法背景，不要求每次执行时全部加载。

部分 Skill 引用能力域内的研究或契约，复用时应保留能力域目录和相对路径；`software-engineering-process` 还依赖所路由的其他能力域。只复制一个 Skill 目录前，检查其中的相对引用与命名依赖。`ontology-modeling` 的执行参考已包含在自身 Skill 目录内。

`skill-orchestration` 管理多 Skill 的依赖与交接，`software-engineering-process` 确定软件生命周期阶段，`engineering-task-discipline` 约束变更与验证。三者按需要组合，不要求普通专项任务进入完整编排。

两个系统架构方法域的分工见[架构 Skills 联合使用指南](docs/architecture-skills-guide.md)。全部生命周期路由和仓库能力覆盖见[流程能力目录](orchestration/capability-catalog.md)。

旧目录已迁入 `domains/`，原 `software-engineering-process/` 改为 `orchestration/`，中文指南改为 `docs/architecture-skills-guide.md`。Skill 调用名和 Agent 名称保持原值；现有安装副本如需同步，应同时更新目录及引用。

## 维护与校验

遵循 [AGENTS.md](AGENTS.md)。完成文档、Skill 或 Agent 变更后，在仓库根目录执行：

```bash
uv run --no-project --with pyyaml==6.0.3 python scripts/validate_repo.py
uv run --no-project --with pyyaml==6.0.3 python -m unittest discover -s tests
```

已安装 PyYAML 的 Python 环境可直接运行上述 Python 命令。检查覆盖目录结构、frontmatter、Skill/Agent 命名与引用、UI 元数据、本地链接及标题锚点、能力目录覆盖和未完成标记；不联网验证外部来源，也不替代专业模型或运行验证。

## 案例、评估与分发

| 需要做什么 | 入口 |
| --- | --- |
| 了解各能力如何共同完成任务 | [跨域工单案例](docs/cases/maintenance/inputs.md)，包括局部与跨阶段入口 |
| 了解产物应写到什么程度 | [决策、验证和交接样例](docs/cases/maintenance/deliverables.md) |
| 复算项目网络与架构权衡 | [定量案例](docs/cases/maintenance/quantitative.md) |
| 判断 Skill 的实际执行质量 | [12 个行为场景与评审协议](docs/evaluation.md)，结构检查与行为结果分开报告 |
| 检查依赖并构建可复用目录 | [依赖与本地分发](docs/distribution.md)，支持完整仓库包和独立本体包 |
| 维护来源、版本与兼容性 | [维护规则](docs/maintenance.md)、[变更记录](docs/changes.md)和[验证记录](docs/validation-results.md) |

[CI 工作流](.github/workflows/validate.yml)执行静态、工具、专业案例与分发验证；其自动检查不代替人工行为评估和实际业务验收。

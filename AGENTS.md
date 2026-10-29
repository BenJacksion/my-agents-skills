# AGENTS.md

本文件约束本仓库内 Agents 与 Skills 的整理、编写和维护方式。

## 入口与职责

- 使用入口和目录说明见 [README.md](README.md)，本文件只维护执行与变更规范。
- Skill 保存专业方法；Agent 负责角色、决策收敛和交接；流程层负责能力选择、阶段门和回退。
- 明确的专项任务直接读取目标 `SKILL.md`；定位能力时再看能力目录，需要协作时再读交接契约。研究资料和模式参考按需加载。
- 复用已有合格产物，只补当前问题缺少的输入；单项任务不要求填写完整状态模板或执行整个生命周期。

## 编码前思考

- 执行任务前先明确成功标准和验证方式。
- 明确假设；不确定且会影响结果时，先提出一个集中的澄清问题。
- 存在歧义时，列出可能解释，不默默选定单一方案。
- 发现明显更简单的做法时，直接指出并优先采用。
- 发现代码或文档逻辑矛盾、职责重叠时，先暂停收敛并请求澄清。

## 简洁优先

- 用最少的文件和内容解决当前问题。
- 不为一次性需求创建抽象层、复杂架构或占位目录。
- 不为了“未来可能用到”增加扩展性、配置项或重复能力。
- 若现有内容可以大幅精简，优先整理为更清晰的结构。

## 精准修改

- 只修改与当前任务直接相关的文件。
- 不顺手优化相邻内容、排版或无关文档。
- 严格匹配项目现有中文文档风格和 Markdown 结构。
- 复杂脚本逻辑添加必要的中文注释，说明原因、约束或不变量。
- 因本次修改产生的无效引用、废弃路径和重复说明可直接删除。
- 发现原有死内容或冗余内容时，除非与任务直接相关，否则只在回复中提醒。

## 目录边界

- `domains/product-thinking/` 是产品思维能力域，内容来自互联网一手来源研究。
- `domains/system-architecture-product-design/` 是系统架构能力域，内容来自《系统架构：复杂系统的产品设计与开发》及其提炼材料。
- `domains/architecture-way/` 是《架构之道：软件构建的设计方法》能力域，内容来自 Juval Löwy 的 *Righting Software* 及其官方/出版社资料。
- `domains/enterprise-application-architecture/` 是企业应用架构能力域，内容来自《架构真意》及其研究和阅读笔记。
- `domains/ontology-modeling/` 是本体建模能力域，内容来自公开标准和产品官方文档。
- 专业能力域统一放在 `domains/` 下平级维护，不把一个能力域的文件放入另一个能力域目录，也不在根目录新增专业能力域。
- `orchestration/` 是项目级流程编排层，只负责按软件生命周期路由现有 Skills/Agents、管理阶段门和交接状态，不承载新的书籍方法论。
- `docs/` 保存跨能力域的使用指南；`scripts/` 和 `tests/` 分别保存仓库维护工具与其测试。
- 原始资料和中间研究放入对应能力域的 `research.md` 或 `source-materials/`。
- 每个能力域及 `orchestration/` 均保留 `README.md`、`capability-catalog.md` 和 `agent-contracts.md`；说明、路由和交接各自维护，避免复制专业方法。

## Skills 规范

- 专业 Skill 放在 `domains/<domain>/skills/<skill-name>/`，流程 Skill 放在 `orchestration/skills/<skill-name>/`，每个目录必须包含 `SKILL.md`。
- Skill 目录名必须与 `SKILL.md` frontmatter 中的 `name` 一致。
- `name` 使用小写字母、数字和短横线，长度不超过 64 个字符，在整个仓库中唯一。
- `description` 同时说明能力、适用场景和不适用边界。
- `SKILL.md` 只写会改变执行判断的说明；避免通用空话和重复方法。
- 本仓库每个 Skill 保留 `agents/openai.yaml`；`interface` 包含 `display_name`、25–64 个字符的 `short_description` 和显式包含 `$skill-name` 的 `default_prompt`。
- 通用执行规则留在 `SKILL.md`，较长或仅特定模式需要的说明放入 `references/`，从入口说明何时读取。
- 新增 Skill 前先检查是否已有能力可以承载，避免拆出重复微技能。
- 新增或改名后更新所属能力域目录及[流程能力目录](orchestration/capability-catalog.md)，并检查 Agent 的 `skills` 引用。

## Agents 规范

- 专业 Agent 放在 `domains/<domain>/agents/<agent-name>.md`，流程 Agent 放在 `orchestration/agents/<agent-name>.md`。
- Agent frontmatter 至少包含 `name`、`description`、`model` 和 `skills`。
- `name` 与文件名一致且在仓库中唯一；`skills` 只引用已存在的 Skill，作为按需使用的能力清单。
- Agent 正文应明确角色、输入、执行协议、边界、输出契约和交接条件。
- Agent 负责角色和编排，不重复保存 Skill 中的详细方法。
- 下游 Agent 不得把上游假设升级为事实。

## 引用与目录迁移

- 本地链接相对于当前文件，核对目标文件及标题锚点；元数据中的资料路径也应有明确的相对基准。
- 移动或改名时同步更新链接、文字路径、能力目录、规范和脚本中的发现路径，检查旧路径残留。
- 移动前后核对文件清单和内容，必要时比较哈希；路径修正与内容修改分开验证，保留已有未提交工作。
- Skill 调用名与目录位置分别管理；单纯调整上层目录不改变 Skill 或 Agent 名称。
- 部分 Skill 依赖能力域内的研究、契约或其他 Skill。复用时保留所需结构；工作区迁移完成不代表个人安装副本已同步。

## 目标驱动执行

- “修复问题”要转化为：复现问题、定位原因、修改并验证。
- “新增校验功能”要转化为：补充异常输入或边界用例，并确保通过。
- “整理文档”要转化为：目录清晰、链接有效、路径一致、重复内容减少。
- 多步骤复杂任务先输出简短计划，并标注每一步验证方式。

## 验证要求

- 文档、Skill、Agent 或目录变更后，在仓库根目录执行统一检查：

  ```bash
  uv run --no-project --with pyyaml python scripts/validate_repo.py
  ```

- 修改校验脚本或测试时，再运行回归用例：

  ```bash
  uv run --no-project --with pyyaml python -m unittest discover -s tests
  ```

- 统一检查覆盖目录结构、frontmatter、命名、Agent 的 Skill 引用、UI 元数据、本地链接与锚点、能力目录覆盖及未完成标记。
- 专业模型、示例代码或计算逻辑发生变化时，补充与风险相称的运行验证；静态校验通过不能替代专业验证或外部来源核验。
- 验证结果标为通过、失败、未运行或不适用，并保留证据或原因；验证计划不得写成已执行结果。
- 最终回复说明修改了什么、验证了什么，以及仍未处理的风险。

## 输出要求

- 回复使用中文。
- 结构清晰，优先简洁。
- 说明事实、假设、证据、决策和未决问题，不混在一起。

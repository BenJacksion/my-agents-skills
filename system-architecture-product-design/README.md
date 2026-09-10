# 系统架构产品设计 Agents & Skills

将《系统架构：复杂系统的产品设计与开发》的方法转化为可路由、可协作、可验证的 Agents 与 Skills，支持从系统思维、架构分析到概念创建、复杂度分解和决策优化的完整工作流。

## 内容

- `agents/`：系统探索、架构分析、概念设计、复杂度管理、治理和决策分析等 Agent。
- `skills/`：可独立调用的架构分析、概念开发、复杂度分解、战略治理、决策优化和系统思维 Skills。
- `agent-contracts.md`：Agent 输入、输出、职责边界、交接条件和失败回退规则。
- `capability-catalog.md`：能力目录、章节映射、路由规则和统一数据契约。
- `chapter-playbook.md`：按原书章节整理的实践方法、产出和质量门槛。
- `book-summary.md`：原书总结、工程化提炼说明和文件清单。
- `source-materials/book-ocr.md`：原书 OCR 文本资料。
- `source-materials/skills-agents-framework.md`：细粒度 Skills/Agents 参考框架。

## 能力链路

默认编排顺序为：

```text
系统思维 -> 架构分析 -> 概念创建 -> 复杂度分解 -> 决策优化
```

根据任务边界可以从中间节点开始。例如，已有系统盘点可以直接使用架构分析；只做模块边界诊断可以从复杂度分解开始。

细粒度能力不重复创建：形式分析、功能分析和架构映射由 `architecture-analysis-mapping` 承载；需求分析和生命周期上下文由 `architecture-strategy-governance` 承载；权衡空间和优化求解由 `architecture-decision-optimization` 承载。架构原则审查作为总控交付前的质量门执行。

## 统一契约

Agent 共享结构化上下文 `ArchitectureState`，并明确区分：

- 事实（facts）
- 假设（assumptions）
- 模型与证据（models / evidence）
- 决策、风险和验证行动（decisions / risks / validations）
- 未决问题与追溯关系（open_questions / traceability）

下游 Agent 不应将上游假设直接升级为事实；缺失信息必须保留并标记为未知。

## 使用方式

1. 根据用户问题和路由规则选择对应 Skill 或 Agent。
2. 阅读目标目录下的 `SKILL.md` 或 Agent 定义，准备最小输入上下文。
3. 按统一契约输出事实、假设、模型、决策、风险和下一步验证行动。
4. 使用 `agent-contracts.md` 中的交接条件检查结果是否可以交给下一个节点。

## 设计原则

- 先明确系统边界、价值和目标，再进行方案比较。
- 保留多个真正不同的概念，避免过早锁定具体解决方案。
- 通过形式、功能、映射和证据建立可追溯性。
- 用分解降低认知负担，同时显式记录接口、组织和运营成本。
- 将模型作为辅助判断的工具，而不是架构师判断的替代品。

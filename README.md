# 产品与系统架构 Agents & Skills

将互联网一手来源中的产品思维方法，以及《系统架构：复杂系统的产品设计与开发》中的系统架构方法，转化为可路由、可协作、可验证的 Agents 与 Skills。

## 目录

- `product-thinking/`：从用户问题、产品结果、假设实验和优先级取舍中形成产品决策。
- `system-architecture-product-design/`：从系统思维、架构分析、概念创建、复杂度分解到架构决策。

## 产品思维

- `product-thinking/README.md`：产品思维能力域说明。
- `product-thinking/agents/`：产品思维负责人 Agent。
- `product-thinking/skills/`：产品思维总入口、产品发现、结果与指标、假设测试、策略与优先级 Skills。
- `product-thinking/research.md`：基于互联网一手来源的产品思维研究与来源清单。

默认链路：

```text
产品发现 -> 结果与指标 -> 假设测试 -> 策略与优先级 -> 持续迭代
```

## 系统架构

- `system-architecture-product-design/README.md`：系统架构能力域说明。
- `system-architecture-product-design/agents/`：系统探索、架构分析、概念设计、复杂度管理、治理和决策分析等 Agent。
- `system-architecture-product-design/skills/`：可独立调用的架构分析、概念开发、复杂度分解、战略治理、决策优化和系统思维 Skills。
- `system-architecture-product-design/source-materials/`：系统架构原始 OCR 与细粒度框架资料。

默认链路：

```text
系统思维 -> 架构分析 -> 概念创建 -> 复杂度分解 -> 决策优化
```

## 使用方式

1. 根据用户问题和路由规则选择对应 Skill 或 Agent。
2. 阅读对应能力域的 `README.md`、`capability-catalog.md` 和目标 `SKILL.md`。
3. 按该能力域的 `agent-contracts.md` 输出事实、假设、证据、决策、风险和下一步验证行动。
4. 缺失信息必须标记为未知；只有当缺失信息会改变方向时才集中提问。

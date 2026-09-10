---
name: product-assumption-testing
description: 拆解产品方案中的高风险假设并设计短周期、可证伪的实验。适用于概念验证、原型测试、MVP、可取性和可行性验证；不用于为既定方案寻找宣传依据。
metadata:
  source: 互联网一手来源综合研究，见 product-thinking/research.md
  version: "1.0.0"
---

# 产品假设测试

把“验证这个想法”拆成一组必须为真的假设，并优先检查影响大、证据弱的部分。实验的目的不是证明团队已经选定的方案，而是尽早降低错误下注的成本。

## 执行步骤

1. 写出方案要推动的用户或业务结果。
2. 用故事地图、反事实提问或 pre-mortem 列出假设。
3. 按风险类型分类：用户是否需要、是否愿意采用、是否能理解和使用、是否技术可行、是否商业可行、是否合规和伦理可接受。
4. 评估每个假设的重要性与现有证据强度，优先验证高重要性、低证据的假设。
5. 为每个优先假设定义最小实验：对象、场景、改变、观察信号、样本或周期、成功标准和失败标准。
6. 选择能最快获得可靠证据的方法，例如访谈、原型、可用性测试、人工服务、灰度、数据分析或技术 spike。
7. 记录结果、证据质量、偏差、结论和下一步；结果可以是继续、调整、停止或回到机会空间。

## 实验约束

- 实验必须回答一个具体问题，不能只收集笼统好感。
- 先写成功/失败标准，避免看到结果后移动门槛。
- 尽量缩短周期，但不得跳过隐私、安全、合规和用户伤害检查。
- 小样本实验可以验证理解和可用性，不能自动推导市场规模。
- 实验结果不是产品成功的证明；它只更新某些假设的可信度。

## 输出

- `target_outcome`：实验服务的用户或业务结果；
- `assumptions`：假设、类型、重要性、证据强度和来源；
- `experiment_cards`：实验对象、方法、周期、成功/失败标准；
- `evidence`：观察结果、数据质量和限制；
- `decision`：继续、调整、停止或转向；
- `next_validation`：下一轮需要学习的内容。

## 质量门槛

- 每个实验都对应明确假设和结果；
- 优先级来自风险与证据，而不是团队偏好；
- 成功与失败标准在实验前确定；
- 结论不超出实验覆盖范围；
- 记录否定结果和未验证风险，不只保留支持方案的证据。

## 来源依据

- [Product Talk: Opportunity Solution Trees](https://www.producttalk.org/opportunity-solution-trees/)
- [Product Talk: Identifying Hidden Assumptions](https://www.producttalk.org/cdh-book-club-august-2026/)
- [GitLab Product Development Flow](https://handbook.gitlab.com/handbook/product-development/how-we-work/product-development-flow/)
- [GOV.UK: How to set performance metrics for your service](https://www.gov.uk/service-manual/measuring-success/how-to-set-performance-metrics-for-your-service)

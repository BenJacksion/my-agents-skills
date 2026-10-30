# 依赖与本地分发

当前提供两种可校验的目录包，不自动写入个人安装目录，也不配置特定运行平台。Agent 是角色文档，运行环境是否支持对应格式需要单独确认。

## 每个 Skill 的分发方式

在仓库根目录运行以下命令，获得全部 Skill 的名称、相对路径和当前支持的分发方式；清单从目录读取，不另维护一份易失真的名称表。

```bash
uv run --no-project --with pyyaml==6.0.3 python scripts/bundle_skills.py --list
```

| 能力范围 | 分发方式 | 依赖与验证边界 |
| --- | --- | --- |
| `ontology-modeling` | 独立 Skill 包 | 执行参考、例子和脚本在 Skill 内；运行案例需要 uv、Python 和 Java |
| 产品思维、系统架构、企业应用架构、《架构之道》及流程 Skills | 完整仓库包 | 保留能力域研究、契约、专项 Skill 和跨域资料引用；执行时仍按需加载 |

完整包是当前保守支持的方式，不代表其中每个 Skill 都依赖其他所有 Skill，也不代表已计算最小依赖闭包。来源元数据中的 `../../research.md` 相对当前 Skill 目录解释；命名调用的能力由同一仓库能力目录解析。

基础校验使用 Python 3.12、PyYAML 6.0.3；定量案例仅用标准库。本体脚本固定其直接依赖并要求 Java；本次工作区运行使用 Java 17.0.12，独立目录复测使用 Java 27，均通过。CI 固定 Java 17，其他平台或版本组合没有默认通过保证。

## 构建与核对

使用尚不存在的输出目录，避免覆盖已有材料：

```bash
uv run --no-project --with pyyaml==6.0.3 python scripts/bundle_skills.py --bundle repository --output .tmp/bundles/repository
uv run --no-project --with pyyaml==6.0.3 python scripts/bundle_skills.py --bundle ontology-modeling --output .tmp/bundles/ontology-modeling
uv run --no-project --with pyyaml==6.0.3 python scripts/bundle_skills.py --verify .tmp/bundles/repository
```

[分发脚本](../scripts/bundle_skills.py)先检查源引用，再复制并生成 `bundle-manifest.json`，列出 Skill 路径、分发类型与每个文件的 SHA-256；检查缺失、修改和额外文件。哈希用于完整性比较，不是来源签名。失败返回非零；复制阶段失败时可能保留新建的未完成输出，不能当成已通过包。

完整包保留当前研究及 `source-materials/`；不复制 Git 历史、个人环境、缓存或生成目录。它是供本地核对的资料包；对外分发需明确原始资料的可分发范围，不将方法提炼与原文授权混为一谈。

干净目录中的复核命令：

```bash
cd .tmp/bundles/repository
uv run --no-project --with pyyaml==6.0.3 python scripts/validate_repo.py
uv run --no-project --with pyyaml==6.0.3 python -m unittest discover -s tests
python scripts/quantitative_examples.py
```

独立本体包内运行 `uv run --no-project scripts/verify_example.py`；完整包中的路径为 `domains/ontology-modeling/skills/ontology-modeling/scripts/verify_example.py`。完整包还应运行这个专业验证入口，静态链接通过不能代替模型运行。

## 更新与兼容

记录旧包清单和新包清单后比较新增、删除、改名与语义变化。在新目录构建并验证后再由使用者切换；不直接覆盖可能含有个人修改的安装副本。目录变化不自动改变 Skill 调用名。

本地包验证不等于模型运行平台的发现、加载和调用测试；行为与加载轨迹按[评估协议](evaluation.md)单独记录。来源及版本维护见[维护规则](maintenance.md)。

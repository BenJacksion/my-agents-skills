"""用临时仓库验证真实缺陷能够被检出，不修改工作区内容。"""

import tempfile
import unittest
from pathlib import Path

from scripts.validate_repo import validate_repo


class ValidateRepoTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.write("domains/example/README.md", "# 示例\n\n## 中文标题\n\n## 中文标题\n")
        self.write("domains/example/capability-catalog.md", "`sample` `lead`\n")
        self.write("domains/example/agent-contracts.md", "# 契约\n")
        self.write("domains/example/skills/sample/SKILL.md", "---\nname: sample\ndescription: 示例方法\n---\n# 方法\n")
        self.write("domains/example/skills/sample/agents/openai.yaml", 'interface:\n  display_name: "示例"\n  short_description: "从输入证据建立可验证的模型与决策，明确责任和后续验证行动"\n  default_prompt: "使用 $sample 处理任务。"\n')
        self.write("domains/example/agents/lead.md", "---\nname: lead\ndescription: 示例角色\nmodel: inherit\nskills:\n  - sample\n---\n" + "\n".join(f"## {h}\n说明\n" for h in ("角色", "输入", "执行协议", "边界", "输出契约", "交接条件")))

    def write(self, path, text):
        dest = self.root / path
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(text, encoding="utf-8")

    def change(self, path, old, new):
        dest = self.root / path
        self.write(path, dest.read_text().replace(old, new))

    def assert_issue(self, message):
        self.assertTrue(any(message in item for item in validate_repo(self.root)), message)

    def test_valid_repository(self):
        self.assertEqual(validate_repo(self.root), [])

    def test_orchestration_skills_are_discovered(self):
        for name in ("README.md", "agent-contracts.md"):
            self.write(f"orchestration/{name}", "# 流程编排\n")
        self.write("orchestration/capability-catalog.md", "2 个 Skills 和 1 个 Agents\n`sample` `lead` `workflow`\n")
        skill = (self.root / "domains/example/skills/sample/SKILL.md").read_text()
        ui = (self.root / "domains/example/skills/sample/agents/openai.yaml").read_text()
        self.write("orchestration/skills/workflow/SKILL.md", skill.replace("name: sample", "name: workflow"))
        self.write("orchestration/skills/workflow/agents/openai.yaml", ui.replace("$sample", "$workflow"))
        self.assertEqual(validate_repo(self.root), [])

    def test_legacy_root_layout_is_rejected(self):
        self.write("legacy/skills/unused/SKILL.md", "# 遗留目录\n")
        self.assert_issue("专业能力域应位于 domains/")

    def test_domain_missing_skills_directory(self):
        self.write("domains/incomplete/README.md", "# 未完成的能力域\n")
        self.assert_issue("缺少 skills/ 目录")

    def test_catalog_accepts_links(self):
        self.write("domains/example/capability-catalog.md", "[sample](skills/sample/SKILL.md) `lead`\n")
        self.assertEqual(validate_repo(self.root), [])

    def test_links_anchors_and_fenced_examples(self):
        self.write("README.md", "[中文](domains/example/README.md#中文标题-1)\n[带空格](<domains/example/a b.md>)\n[引用][ref]\n[ref]: domains/example/README.md#中文标题\n```markdown\n[示例](not-real.md)\n```\n")
        self.write("domains/example/a b.md", "# 示例\n")
        self.assertEqual(validate_repo(self.root), [])
        self.write("README.md", "[失效](domains/example/README.md#不存在)\n")
        self.assert_issue("标题锚点不存在")

    def test_missing_and_escaping_links(self):
        self.write("README.md", "[缺失](missing.md)\n[越界](../outside.md)\n")
        self.assertEqual(sum("本地链接" in x for x in validate_repo(self.root)), 2)

    def test_missing_frontmatter_and_name_mismatch(self):
        self.write("domains/example/skills/sample/SKILL.md", "# 没有元数据\n")
        self.assert_issue("frontmatter")
        self.write("domains/example/skills/sample/SKILL.md", "---\nname: other\ndescription: 示例\n---\n")
        self.assert_issue("name 与路径不一致")

    def test_duplicate_yaml_key(self):
        self.change("domains/example/skills/sample/SKILL.md", "name: sample", "name: sample\nname: other")
        self.assert_issue("YAML 重复键")

    def test_ui_metadata(self):
        self.change("domains/example/skills/sample/agents/openai.yaml", "$sample", "$sample-extra")
        self.assert_issue("default_prompt 未包含")
        self.write("domains/example/skills/sample/agents/openai.yaml", "interface: invalid\n")
        self.assert_issue("interface 必须为映射")

    def test_unknown_agent_skill_and_missing_protocol(self):
        self.change("domains/example/agents/lead.md", "  - sample", "  - absent")
        self.change("domains/example/agents/lead.md", "## 输入", "## 材料")
        self.assert_issue("引用不存在的 Skill")
        self.assert_issue("缺少协议章节：输入")

    def test_missing_skill_file_and_catalog_coverage(self):
        (self.root / "domains/example/skills/empty").mkdir()
        self.write("domains/example/capability-catalog.md", "# 空目录\n")
        self.assert_issue("缺少 SKILL.md")
        self.assert_issue("未登记 Skill sample")
        self.assert_issue("未登记 Agent lead")

    def test_workflow_coverage_and_counts(self):
        self.write("orchestration/capability-catalog.md", "3 个 Skills 和 2 个 Agents\n`sample`\n")
        self.assert_issue("流程目录未覆盖 lead")
        self.assert_issue("数量与实际目录不一致")

    def test_placeholders(self):
        self.write("README.md", "检查 TODO 占位。\n```text\nTODO: 模板示例\n```\n")
        self.assertEqual(validate_repo(self.root), [])
        self.write("README.md", "TODO: 完成说明\n")
        self.assert_issue("存在未完成标记")


if __name__ == "__main__":
    unittest.main()

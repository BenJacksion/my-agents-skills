#!/usr/bin/env python3
"""检查仓库结构、Skill/Agent 元数据和本地 Markdown 引用，不修改文件。"""

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml


NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
LINK = re.compile(r"!?\[[^\]\n]*\]\(\s*(?:<([^>\n]+)>|([^\s)]+))[^\n)]*\)")
REFERENCE = re.compile(r"^ {0,3}\[[^\]\n]+\]:\s*(?:<([^>\n]+)>|(\S+))", re.M)


class UniqueKeyLoader(yaml.SafeLoader):
    """YAML 的重复键会被默认覆盖；这里报告错误，避免静默丢失配置。"""


def unique_mapping(loader, node):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node)
        if key in mapping:
            raise ValueError(f"YAML 重复键：{key}")
        mapping[key] = loader.construct_object(value_node)
    return mapping


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping
)


def prose(text):
    """跳过代码围栏，模板中的示例路径和待填字段不属于文档链接。"""
    lines = []
    fence = None
    for line in text.splitlines():
        marker = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
        if marker:
            token, suffix = marker.groups()
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence) and not suffix.strip():
                fence = None
            continue
        if fence is None:
            lines.append(line)
    return "\n".join(lines)


def anchors(text):
    result = set()
    for heading in re.findall(r"^ {0,3}#{1,6}\s+(.+)$", prose(text), re.M):
        heading = re.sub(r"\s+#+\s*$", "", heading)
        heading = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", heading)
        slug = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
        # 同名标题的锚点依次加后缀，保留中文和下划线。
        candidate, number = slug, 0
        while candidate in result:
            number += 1
            candidate = f"{slug}-{number}"
        result.add(candidate)
    result.update(re.findall(r'<(?:a|h[1-6])\b[^>]*(?:id|name)=[\"\']([^\"\']+)', text))
    return result


def capability_roots(root):
    """专业能力域与流程层分开存放，二者都需要校验 Skill/Agent。"""
    paths = [path for path in root.glob("domains/*") if path.is_dir()]
    if (root / "orchestration").is_dir():
        paths.append(root / "orchestration")
    return sorted(paths)


def validate_markdown(root):
    """也供独立 Skill 分发包使用，链接不得借用包外工作区文件。"""
    root = Path(root).resolve()
    errors = []
    for path in sorted(root.rglob("*.md")):
        if any(part.startswith(".") for part in path.relative_to(root).parts):
            continue
        text = prose(path.read_text(encoding="utf-8"))
        if "source-materials" not in path.parts and re.search(r"\b(?:TODO|TBD|FIXME)\s*[:：]|\[(?:TODO|TBD|FIXME)\]", text):
            errors.append(f"{path.relative_to(root)}: 存在未完成标记")
        for match in list(LINK.finditer(text)) + list(REFERENCE.finditer(text)):
            target = match[1] or match[2]
            url = urlsplit(target)
            if url.scheme or url.netloc:
                continue
            dest = (path.parent / unquote(url.path)).resolve() if url.path else path
            if not dest.is_relative_to(root) or not dest.exists():
                errors.append(f"{path.relative_to(root)}: 本地链接不存在或越出仓库：{target}")
            elif url.fragment and dest.suffix == ".md" and unquote(url.fragment) not in anchors(dest.read_text()):
                errors.append(f"{path.relative_to(root)}: 标题锚点不存在：{target}")
    return errors


def validate_repo(root):
    root = Path(root).resolve()
    errors = []

    def error(path, message):
        errors.append(f"{path.relative_to(root)}: {message}")

    def registered(name, text):
        return bool(re.search(r"(?:`|\[)" + re.escape(name) + r"(?:`|\])", text))

    def load_yaml(path, frontmatter=False):
        try:
            text = path.read_text(encoding="utf-8")
            if frontmatter:
                match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.S)
                if not match:
                    raise ValueError("缺少完整 frontmatter")
                text = match[1]
            data = yaml.load(text, Loader=UniqueKeyLoader)
            if not isinstance(data, dict):
                raise ValueError("YAML 顶层必须为映射")
            return data
        except (OSError, ValueError, TypeError, yaml.YAMLError) as exc:
            error(path, str(exc))
            return {}

    def metadata(path, expected, required):
        data = load_yaml(path, frontmatter=True)
        for key in required:
            if not isinstance(data.get(key), str) or not data[key].strip():
                error(path, f"缺少非空字符串字段 {key}")
        name = data.get("name")
        if not isinstance(name, str) or len(name) > 64 or not NAME.fullmatch(name):
            error(path, "name 格式无效")
        elif name != expected:
            error(path, f"name 与路径不一致，应为 {expected}")
        return data

    domains = capability_roots(root)
    if not domains:
        errors.append("仓库中未找到能力域")
    for path in root.glob("*/skills"):
        if path.is_dir() and path.parent.name != "orchestration":
            error(path.parent, "专业能力域应位于 domains/，流程层应位于 orchestration/")
    skills, agents = {}, {}
    agent_data = []
    for domain in domains:
        for filename in ("README.md", "capability-catalog.md", "agent-contracts.md"):
            if not (domain / filename).is_file():
                error(domain, f"缺少 {filename}")
        if not (domain / "skills").is_dir():
            error(domain, "缺少 skills/ 目录")
            continue
        catalog_path = domain / "capability-catalog.md"
        catalog = catalog_path.read_text() if catalog_path.is_file() else ""
        for folder in sorted((domain / "skills").iterdir()):
            if not folder.is_dir():
                continue
            path = folder / "SKILL.md"
            if not path.is_file():
                error(folder, "缺少 SKILL.md")
                continue
            data = metadata(path, folder.name, ("name", "description"))
            if folder.name in skills:
                error(path, f"Skill 重名：{folder.name}")
            skills[folder.name] = path
            description = data.get("description", "")
            if isinstance(description, str) and (len(description) > 1024 or "<" in description or ">" in description):
                error(path, "description 超长或包含尖括号")
            if not registered(folder.name, catalog):
                error(catalog_path, f"未登记 Skill {folder.name}")
            ui_path = folder / "agents/openai.yaml"
            ui = load_yaml(ui_path).get("interface", {})
            if not isinstance(ui, dict):
                error(ui_path, "interface 必须为映射")
                ui = {}
            for key in ("display_name", "short_description", "default_prompt"):
                if not isinstance(ui.get(key), str) or not ui[key].strip():
                    error(ui_path, f"缺少非空字符串字段 interface.{key}")
            short = ui.get("short_description")
            if isinstance(short, str) and not 25 <= len(short) <= 64:
                error(ui_path, "short_description 长度应为 25–64 个字符")
            prompt = ui.get("default_prompt", "")
            if not isinstance(prompt, str) or not re.search(r"\$" + re.escape(folder.name) + r"(?![a-z0-9-])", prompt):
                error(ui_path, f"default_prompt 未包含 ${folder.name}")
        for path in sorted((domain / "agents").glob("*.md")):
            data = metadata(path, path.stem, ("name", "description", "model"))
            if path.stem in agents:
                error(path, f"Agent 重名：{path.stem}")
            agents[path.stem] = path
            agent_data.append((path, data))
            headings = " ".join(re.findall(r"^## (.+)$", path.read_text(), re.M))
            for label in ("角色", "输入", "执行", "边界", "输出", "交接|停止"):
                if not re.search(label, headings):
                    error(path, f"缺少协议章节：{label}")
            if not registered(path.stem, catalog):
                error(catalog_path, f"未登记 Agent {path.stem}")

    for path, data in agent_data:
        refs = data.get("skills")
        if not isinstance(refs, list) or not refs:
            error(path, "skills 必须为非空列表")
            continue
        for name in refs:
            if not isinstance(name, str) or name not in skills:
                error(path, f"引用不存在的 Skill：{name}")

    errors.extend(validate_markdown(root))

    index = root / "orchestration/capability-catalog.md"
    if index.is_file():
        text = index.read_text()
        for name in skills.keys() | agents.keys():
            if not registered(name, text):
                error(index, f"流程目录未覆盖 {name}")
        count = re.search(r"(\d+) 个 Skills 和 (\d+) 个 Agents", text)
        if count and (int(count[1]), int(count[2])) != (len(skills), len(agents)):
            error(index, "Skills/Agents 数量与实际目录不一致")
    return errors


if __name__ == "__main__":
    repo = Path(__file__).resolve().parents[1]
    problems = validate_repo(repo)
    if problems:
        print("\n".join(problems))
        print(f"校验失败：{len(problems)} 项")
        sys.exit(1)
    packages = capability_roots(repo)
    skill_count = sum(len(list(path.glob("skills/*/SKILL.md"))) for path in packages)
    agent_count = sum(len(list(path.glob("agents/*.md"))) for path in packages)
    print(f"校验通过：{skill_count} 个 Skills，{agent_count} 个 Agents")

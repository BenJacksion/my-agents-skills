"""生成可检查的本地分发目录，或验证目录内文件；不安装、不覆盖已有目录。"""

import argparse
import hashlib
import json
import shutil
from pathlib import Path

try:
    from .validate_repo import capability_roots, validate_markdown, validate_repo
except ImportError:
    from validate_repo import capability_roots, validate_markdown, validate_repo


ROOT = Path(__file__).resolve().parents[1]
ONTOLOGY = Path("domains/ontology-modeling/skills/ontology-modeling")
REPOSITORY_PATHS = ("README.md", "AGENTS.md", ".gitignore", "domains", "orchestration",
                    "docs", "scripts", "tests", ".github")
MANIFEST = "bundle-manifest.json"


def files_under(root):
    files = []
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root)
        if "__pycache__" in relative.parts or path.name == ".DS_Store":
            continue
        if path.is_symlink():
            raise ValueError(f"分发目录不能包含符号链接：{relative}")
        if path.is_file():
            files.append(path)
    return files


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inventory(root):
    """逐项声明当前分发方式；保守整仓分发不意味着执行时加载全部能力。"""
    return [{"name": path.parent.name, "path": str(path.parent.relative_to(root)),
             "bundle": "ontology-modeling" if path.parent.name == "ontology-modeling" else "repository"}
            for domain in capability_roots(root)
            for path in sorted(domain.glob("skills/*/SKILL.md"))]


def verify_bundle(root):
    root = Path(root).resolve()
    manifest = json.loads((root / MANIFEST).read_text(encoding="utf-8"))
    if manifest.get("schema_version") != 1 or not isinstance(manifest.get("files"), dict):
        raise ValueError("不支持的分发清单格式")
    expected = manifest["files"]
    actual = {str(path.relative_to(root)): digest(path)
              for path in files_under(root) if path != root / MANIFEST}
    # 比较整个清单，同时检出新增、删除和修改；不按外部传入路径读取文件。
    if expected != actual:
        raise ValueError("分发包文件清单或 SHA-256 不一致")
    kind = manifest["bundle"]
    if kind == "repository":
        if manifest["skills"] != inventory(root):
            raise ValueError("分发清单中的 Skill 目录与实际不一致")
        errors = validate_repo(root)
    elif kind == "ontology-modeling":
        errors = validate_markdown(root)
        if not (root / "SKILL.md").is_file() or not (root / "scripts/verify_example.py").is_file():
            errors.append("独立本体 Skill 缺少入口或运行脚本")
    else:
        raise ValueError(f"未知分发类型：{kind}")
    if errors:
        raise ValueError("\n".join(errors))
    return manifest


def build_bundle(source, output, kind):
    if Path(output).is_symlink():
        raise ValueError("目标不能是符号链接")
    source, output = Path(source).resolve(), Path(output).resolve()
    base = source / ONTOLOGY if kind == "ontology-modeling" else source
    if kind not in ("repository", "ontology-modeling"):
        raise ValueError(f"未知分发类型：{kind}")
    if output.exists():
        raise ValueError("目标目录已存在，请使用新的输出目录")
    if kind == "repository":
        entries = [source / name for name in REPOSITORY_PATHS if (source / name).exists()]
    else:
        entries = [base]
    if any(output == entry or output.is_relative_to(entry) for entry in entries):
        raise ValueError("输出目录不能位于待打包资料内")
    selected = []
    for entry in entries:
        if entry.is_symlink():
            raise ValueError(f"不能打包符号链接：{entry}")
        selected.extend(files_under(entry) if entry.is_dir() else [entry])
    # 先核对源引用再创建输出；完整包保留资料目录，不擅自删减原始研究。
    errors = validate_markdown(base) if kind == "ontology-modeling" else validate_repo(source)
    if errors:
        raise ValueError("\n".join(errors))
    output.mkdir(parents=True, exist_ok=False)
    hashes = {}
    for path in selected:
        relative = path.relative_to(base)
        target = output / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(path, target)
        hashes[str(relative)] = digest(path)
    skills = inventory(source)
    if kind == "ontology-modeling":
        skills = [{**item, "path": "."} for item in skills if item["name"] == kind]
    manifest = {"schema_version": 1, "bundle": kind, "skills": skills, "files": hashes}
    (output / MANIFEST).write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    verify_bundle(output)
    return manifest


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--list", action="store_true", help="列出每个 Skill 的路径与分发方式")
    mode.add_argument("--bundle", choices=("repository", "ontology-modeling"))
    mode.add_argument("--verify", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        if args.list:
            print(json.dumps(inventory(ROOT), ensure_ascii=False, indent=2))
        elif args.verify:
            manifest = verify_bundle(args.verify)
            print(f"分发包校验通过：{manifest['bundle']}，{len(manifest['files'])} 个文件")
        else:
            if args.output is None:
                parser.error("--bundle 需要 --output")
            manifest = build_bundle(ROOT, args.output, args.bundle)
            print(f"已生成：{args.output}，{len(manifest['files'])} 个文件；引用与哈希校验通过")
    except (ValueError, OSError, KeyError, TypeError) as exc:
        parser.exit(1, f"分发失败：{exc}\n")

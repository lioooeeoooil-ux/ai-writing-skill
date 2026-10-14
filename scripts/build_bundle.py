#!/usr/bin/env python3
"""build_bundle.py — concatenate all rule sources into bundle.md (single-file version).

Run after ANY edit to source files:  python scripts/build_bundle.py
Never edit bundle.md by hand; it is a build artifact.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ORDER = ["SKILL.md", "workflow.md", "checklist.md",
         "references/voice-style.md", "references/red-lines.md",
         "references/platform-checklists.md", "user-profile.md"]

HEADER = """# bundle.md — human-ai-writing 合订本（单文件版）

> 本文件由 scripts/build_bundle.py 自动生成，改动规则请改源文件后重新生成。
> 用法：把全文贴进任何 AI 对话框作为第一条消息，然后说"执行 Step 0，我的选题是：___"。

---

"""

parts = [HEADER]
for rel in ORDER:
    text = (ROOT / rel).read_text(encoding="utf-8")
    # strip YAML frontmatter (only SKILL.md has it)
    if text.startswith("---"):
        text = text.split("---", 2)[2].lstrip()
    parts.append(f"\n\n<!-- ===== {rel} ===== -->\n\n{text.rstrip()}\n")

(ROOT / "bundle.md").write_text("".join(parts), encoding="utf-8")
print(f"bundle.md rebuilt from {len(ORDER)} sources")

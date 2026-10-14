#!/usr/bin/env python3
"""new_draft.py — create a draft workspace: drafts/<slug>/{state.md, chapters/, annotations.md, draft_full.md}

Usage: python scripts/new_draft.py <slug>
drafts/ is gitignored: private WIP never enters the public repo; finished
pieces graduate to examples/bank/ via the 收录标准 there.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

STATE_TEMPLATE = """# {slug} — 写作状态

当前位置: Step 0（选题痛点测试）
下一步: 填写三件套（读者画像/痛点场景/不写替代方案），对话质询等处置
关键决策: （Step 0 后填写：干货/随笔 | 钩型 | 骨架）

## Step 0 三件套
- 读者画像:
- 痛点场景:
- 不写替代方案:

## 第一指令
（Step 1 五要素 + 观点三问通过后，把定稿贴到这里）

## 钩型与骨架
- 选定钩:
- 骨架:
"""

ANNOTATIONS_HEADER = """# 标注台账（格式：[第N章] <ID> <问题> <处置>；ID: G1-G11 / RR1-RR5 / WX1-WX4 / R1-R5 / V-困惑）

"""

def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    slug = re.sub(r"[^\w\u4e00-\u9fff-]", "-", sys.argv[1])
    d = ROOT / "drafts" / slug
    if d.exists():
        print(f"exists: {d}")
        return 1
    (d / "chapters").mkdir(parents=True)
    (d / "state.md").write_text(STATE_TEMPLATE.format(slug=slug), encoding="utf-8")
    (d / "annotations.md").write_text(ANNOTATIONS_HEADER, encoding="utf-8")
    (d / "draft_full.md").write_text("", encoding="utf-8")
    print(f"created: {d}")
    return 0

if __name__ == "__main__":
    sys.exit(main())

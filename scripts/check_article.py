#!/usr/bin/env python3
"""check_article.py — machine-checkable constraints from checklist.md.

Covers: banned AI-flavor phrases, third-person residue, paragraph length,
enumeration-style paragraph openings, and (with --hook) opening-hook length.
Everything else in checklist.md still requires human judgment.

Usage: python check_article.py draft.md [--hook]
Exit code: 0 = pass, 1 = errors found.
"""
import re
import sys

# (phrase, level) — level 2 = error, level 1 = warning
BANNED = [
    ("It's worth noting", 2), ("In summary", 2), ("In conclusion", 2),
    ("For example", 2), ("reportedly", 1), ("studies show", 1),
    ("the author", 2), ("this article", 2),
    ("值得注意", 2), ("综上所述", 2), ("总而言之", 2), ("总的来说", 2),
    ("据报道", 1), ("研究表明", 1), ("显著提升", 1),
    ("作者", 1),  # Chinese third person: warn only, context-dependent
]

# regex form, for phrases needing context guards (avoid matching inside longer words)
BANNED_REGEX = [
    (r"本文(?![件章])", "本文", 1),  # "本文件/本文章" is fine, standalone "本文" is not
]

ENUM_STARTS_EN = ("First", "Second", "Third", "Finally")
ENUM_STARTS_CN = ("首先", "其次", "再次", "最后", "第一，", "第二，", "第三，")

SENTENCE_END = re.compile(r"[。！？!?]|(?<=[a-zA-Z0-9])[.!?]")
CJK = re.compile(r"[\u4e00-\u9fff]")


def line_of(text, idx):
    return text.count("\n", 0, idx) + 1


def paragraphs(text):
    """Split into (line_number, paragraph_text) on blank lines."""
    result, start_line, buf = [], 1, []
    for i, line in enumerate(text.split("\n"), 1):
        if line.strip() == "":
            if buf:
                result.append((start_line, "\n".join(buf)))
                buf = []
            start_line = i + 1
        else:
            if not buf:
                start_line = i
            buf.append(line)
    if buf:
        result.append((start_line, "\n".join(buf)))
    return result


def main():
    args = [a for a in sys.argv[1:] if a != "--hook"]
    if not args:
        print(__doc__)
        return 2
    text = open(args[0], encoding="utf-8").read()
    # <!-- check:off --> ... <!-- check:on --> : quote violations intentionally (e.g. in examples)
    text = re.sub(r"<!-- check:off -->.*?<!-- check:on -->", "", text, flags=re.S)
    errors, warnings = [], []

    for phrase, level in BANNED:
        for m in re.finditer(re.escape(phrase), text):
            msg = f"L{line_of(text, m.start())}: banned phrase \"{phrase}\""
            (errors if level == 2 else warnings).append(msg)
    for pattern, label, level in BANNED_REGEX:
        for m in re.finditer(pattern, text):
            msg = f"L{line_of(text, m.start())}: banned phrase \"{label}\""
            (errors if level == 2 else warnings).append(msg)

    paras = paragraphs(text)
    enum_count = 0
    for line_no, p in paras:
        stripped = p.lstrip("#>* ")
        if stripped.startswith(ENUM_STARTS_EN) or stripped.startswith(ENUM_STARTS_CN):
            enum_count += 1
        n_sent = len(SENTENCE_END.findall(p))
        if n_sent > 5:
            errors.append(f"L{line_no}: paragraph has {n_sent} sentences (max 5)")
    if enum_count >= 3:
        errors.append(f"{enum_count} paragraphs open with enumeration "
                      f"(First/Second/Finally, 首先/其次/最后) — vary openings")

    if "--hook" in sys.argv and paras:
        first = ""
        for line_no, p in paras:  # skip headings, blockquotes, rules, comments, italics notes
            s = p.strip()
            if s and not s.startswith(("#", ">", "<!--", "---", "*")):
                first = s
                break
        n_chars = len(CJK.findall(first))
        n_words = len([w for w in re.split(r"\s+", first) if not CJK.search(w) and re.search(r"[a-zA-Z0-9]", w)])
        total = n_chars + n_words
        if not (80 <= total <= 150):
            errors.append(f"opening hook is ~{total} words/chars, expected 80-150")

    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    print(f"\n{len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

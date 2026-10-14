# human-ai-writing

A human-AI collaborative writing system for long-form tech/product analysis articles.

## Philosophy

This is not a prompt template. It's a **workflow** that treats writing as a multi-step craft:

1. Research with source verification
2. Hook generation with user selection
3. Chapter-by-chapter drafting with human review at each step
4. Self-check before final output
5. Iteration based on feedback

## Repository Structure

```
├── SKILL.md           # Entry point: trigger conditions + loading map (for skill-capable AI hosts)
├── bundle.md          # Single-file generated version — paste wholesale into any chat (do not edit, regenerate via script)
├── workflow.md        # 5-step human-in-the-loop workflow (incl. First Instruction)
├── checklist.md       # Single source of the self-check list (human + machine items)
├── user-profile.md    # Style preferences + maintenance protocol
├── references/
│   ├── voice-style.md      # Role, hook menu (4 types), 3 skeletons, language layer, endings — evidence-based
│   ├── red-lines.md        # R1–R5 red lines & data rules (from 作者A/作者B/own-article teardown)
│   └── platform-checklists.md  # 人人都是产品经理 / 微信公众号 platform checklists + fit decision
├── scripts/
│   ├── check_article.py  # Machine-checkable constraints (banned phrases, paragraph length, hook length)
│   └── build_bundle.py   # Generates bundle.md from source files (run after any rule edit)
└── examples/
    └── sample-article.md # A demo draft written per these rules, with before/after fixes
```

## 启动方式（三种宿主）

- **本对话框（Kimi，有文件权限）**：第一条消息说「读 `/mnt/agents/output/ai-writing-skill/SKILL.md`，执行 Step 0，我的选题是：___」
- **任何普通对话**：贴 `bundle.md`（合订本，由 `scripts/build_bundle.py` 从源文件生成，永不手改）
- **Skill 宿主（Claude Code 等）**：git clone 后挂载仓库目录，宿主自动发现 SKILL.md

## Quick Start

0. If your AI host supports skills (Claude Code, etc.), point it at this repo — the entry point is `SKILL.md` (trigger conditions + loading map)
1. Write the First Instruction (workflow.md Step 1: 角色/受众/核心观点/个人经历/语调); before drafting, read `references/voice-style.md` + `references/red-lines.md`
2. Provide an outline + reference links
3. Follow the workflow in `workflow.md`
4.
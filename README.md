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
├── system-prompt.md   # Voice, sentence patterns, prohibitions, data rules — copy into your AI's system prompt
├── workflow.md        # The 5-step human-in-the-loop workflow
├── checklist.md       # Single source of the self-check list (human + machine items)
├── user-profile.md    # Style preferences + maintenance protocol
├── scripts/
│   └── check_article.py  # Machine-checkable constraints (banned phrases, paragraph length, hook length)
└── examples/
    └── sample-article.md # A demo draft written per these rules, with before/after fixes
```

## Quick Start

1. Copy `system-prompt.md` into your AI assistant's system prompt
2. Provide an outline + reference links
3. Follow the workflow in `workflow.md`
4. Run `python scripts/check_article.py draft.md --hook` on the draft
5. Go through `checklist.md` for the remaining judgment items

## License

MIT

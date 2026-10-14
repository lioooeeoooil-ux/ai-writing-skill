# Writing Workflow (Human-AI Collaborative)

## User Input
- Article outline (required)
- Reference links (optional)
- Special requirements (optional)

## Step 1: First Instruction + Research
- Write the First Instruction first (小普流程，约 10 分钟，信息密度优先)：角色 / 受众 / 核心观点 / 个人经历 / 语调 五要素——它决定全文调性，比后续任何一步都值钱
- Search core facts (max 4 query terms)
- Read reference links
- Output: First Instruction + fact list + uncertainty labels + items needing verification
- **Pause for user confirmation before proceeding**

## Step 2: Hook Generation
- Generate 3 hooks, each from a different type: Scene / Data-anomaly / Conclusion-first / Event-anchored (criteria in references/voice-style.md)
- Constraints: 100-200 字；第一段不对术语下定义（名词可出现，解释留给正文）
- **Pause for user selection or new direction**

## Step 3: Chapter-by-Chapter Drafting
- Output each chapter, then **pause for user annotation**
- Annotation dimensions: tone / information density / rhythm / AI-flavor / transition — plus 困惑型标注 ("我不确定这段成不成立" / "我想要转折但想不到切入点"): feed real uncertainty, not just corrections (小普自曝流程)
- Adjust immediately based on feedback

## Step 4: Self-Check
- Run `python scripts/check_article.py <draft.md>` for machine-checkable items (banned phrases, third person, paragraph length, hook length)
- Run through `checklist.md` for the remaining human-judgment items (repetition, deleted-source residue, over-absolutization, fact accuracy)
- Note: this checklist is single-source in `checklist.md` — do not duplicate item lists elsewhere, or they will drift apart
- Pick target platform and run its checklist in `references/platform-checklists.md` (unsure which platform? Run the 平台适配检查 three questions there first)

## Step 5: Final Output
- Markdown format
- Structure per one of the three skeletons in references/voice-style.md (time-line / concept-teardown / story-first); directory-style structure is forbidden
- Word count based on completeness, not padding
- Attach a platform recommendation: which platform(s) this draft fits and why, per `references/platform-checklists.md`

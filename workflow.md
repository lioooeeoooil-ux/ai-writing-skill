# Writing Workflow (Human-AI Collaborative)

## User Input
- Article outline (required)
- Reference links (optional)
- Special requirements (optional)

## Step 1: Research
- Search core facts (max 4 query terms)
- Read reference links
- Output: Fact list + uncertainty labels + items needing verification
- **Pause for user confirmation before proceeding**

## Step 2: Hook Generation
- Generate 3 hooks (Scene / Counter-intuitive / Pain point)
- Hard constraints: 80-150 words, max 1 technical term
- **Pause for user selection or new direction**

## Step 3: Chapter-by-Chapter Drafting
- Output each chapter, then **pause for user annotation**
- Annotation dimensions: tone / information density / rhythm / AI-flavor / transition
- Adjust immediately based on feedback

## Step 4: Self-Check
- Run `python scripts/check_article.py <draft.md>` for machine-checkable items (banned phrases, third person, paragraph length, hook length)
- Run through `checklist.md` for the remaining human-judgment items (repetition, deleted-source residue, over-absolutization, fact accuracy)
- Note: this checklist is single-source in `checklist.md` — do not duplicate item lists elsewhere, or they will drift apart
- Pick target platform and run its checklist in `references/platform-checklists.md` (unsure which platform? Run the 平台适配检查 three questions there first)

## Step 5: Final Output
- Markdown format
- No section titles or adjust as needed
- Word count based on completeness, not padding
- Attach a platform recommendation: which platform(s) this draft fits and why, per `references/platform-checklists.md`

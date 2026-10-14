# Writing Workflow (Human-AI Collaborative)

## Working Files Convention
- Per-article working files live in `drafts/<slug>/` (gitignored, never committed): `state.md` is the single must-read when resuming; chapters in `chapters/`; annotation log in `annotations.md` (P2 format); assembled draft in `draft_full.md`
- Create a workspace with `python scripts/new_draft.py <slug>`

## User Input
- Article outline (required)
- Reference links (optional)
- Special requirements (optional)

## Step 0: 选题痛点测试（闸口，不过不启动）
Fill the three outputs, then defend them against challenge:

1. 读者画像（一句话）
2. 痛点场景还原（必须含具体的人、时刻、触发）
3. 不写的替代方案（读者没这篇会怎么办——"官方文档够"= 你的角度没增量）

Verdict rules:
- ②写不出真实场景 → 打回：回到真实素材里找（聊天记录/真实抱怨），不是组织语言
- ③弱 → 打回：换角度或换题（痛点多半还在，死的是当前角度）
- ②过③勉强 → 随笔路线（允许无交付物，但 G11 温度守恒提高到 ≥4 处）
- **Pause: verdict before proceeding**

## Step 1: First Instruction + Research
- Write the First Instruction first (作者A流程，约 10 分钟，信息密度优先)：角色 / 受众 / 核心观点 / 个人经历 / 语调 五要素——它决定全文调性，比后续任何一步都值钱
- 核心观点必须过观点三问：①有人反对吗（反方一句话写出来；全网共识=复读，找角度或降格）②我凭什么说（证据五级点名最高可用级；说不出来=整理者身份，行文禁判断者句式）③读者带走什么动作（说不出=只有情绪价值，转随笔路线）
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
- Annotation dimensions: tone / information density / rhythm / AI-flavor / transition — plus 困惑型标注 ("我不确定这段成不成立" / "我想要转折但想不到切入点"): feed real uncertainty, not just corrections (作者A自曝流程)
- Annotation log format (one line each): `[第N章] <ID> <问题> <处置>` — IDs: G1-G11 / RR1-RR5 / WX1-WX4 / R1-R5 / V-困惑；标注优先级：脚本或红线已抓到的记 R-ID，人工独有的才记 G-ID（防双记污染统计）
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

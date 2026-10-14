# Self-Check Checklist

| ID | Check Item | Pass Standard | Fix Action |
|----|-----------|--------------|-----------|
| G1 | Information repetition | Same fact appears only once | Delete duplicate, merge to earliest occurrence |
| G2 | Deleted source residue | Deleted info has no residue | Search keywords across text, confirm clearance |
| G3 | Over-absolutization | "Thoroughly" "Completely" "First time" "Only" etc. softened | Change to "basically" "highly likely" "earlier" "priority" |
| G4 | AI-flavor residue | What R1's banned-phrase list misses (rhythm-level weirdness) | Replace with colloquial transitions |
| G5 | Person consistency | Full text "I" as main | Replace all "the author" "this article" |
| G6 | Number specificity | All numbers have sources or labels | Add sources or change to qualitative description |
| G7 | Paragraph length | Short: 1-2 sentences, Long: max 5 sentences | Split or merge |
| G8 | Hook length | Opening hook 100-200 字 | Rewrite or trim the hook |
| G9 | Ending style | No summary lists | Change to action suggestion or open question |
| G10 | 选题三件套 | Step 0 outputs exist and passed (读者画像/痛点场景/不写替代方案) | 被打回则回到 Step 0，不进入后续 |
| G11 | 温度守恒 | 干货文 ≥2 处、随笔 ≥4 处"具体的人和时刻"（真人/真时间/真对话；"很多人""现代社会"不算；概念拆解型可用对话还原顶替） | 补真实场景，禁抽象主语 |

标注优先级（防双记）：脚本或红线已抓到的记 R-ID，人工独有的才记 G-ID。

## Tool-Assisted Items

The following rows are covered automatically by `scripts/check_article.py` — run it first, then spend human review time on the judgment items above:

- AI-flavor residue (banned phrases)
- Person consistency (third person)
- Paragraph length
- Hook length
- Paragraph-initial enumeration ("First/Second/Finally", "首先/其次/最后")

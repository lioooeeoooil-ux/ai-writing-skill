# Self-Check Checklist

| Check Item | Pass Standard | Fix Action |
|-----------|--------------|-----------|
| Information repetition | Same fact appears only once | Delete duplicate, merge to earliest occurrence |
| Deleted source residue | Deleted info has no residue | Search keywords across text, confirm clearance |
| Over-absolutization | "Thoroughly" "Completely" "First time" "Only" etc. softened | Change to "basically" "highly likely" "earlier" "priority" |
| AI-flavor residue | No "It's worth noting" "In summary" etc. | Replace with colloquial transitions |
| Person consistency | Full text "I" as main | Replace all "the author" "this article" |
| Number specificity | All numbers have sources or labels | Add sources or change to qualitative description |
| Paragraph length | Short: 1-2 sentences, Long: max 5 sentences | Split or merge |
| Hook length | Opening hook 80-150 words / 字 | Rewrite or trim the hook |
| Ending style | No summary lists | Change to action suggestion or open question |

## Tool-Assisted Items

The following rows are covered automatically by `scripts/check_article.py` — run it first, then spend human review time on the judgment items above:

- AI-flavor residue (banned phrases)
- Person consistency (third person)
- Paragraph length
- Hook length
- Paragraph-initial enumeration ("First/Second/Finally", "首先/其次/最后")

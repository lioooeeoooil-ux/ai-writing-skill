# Changelog

## 2026-10-13 — 收拾烂摊子

- **修复**：README Quick Start 路径错误（`skill/xxx.md` → 实际根目录文件），并补全仓库结构图
- **消解规则冲突**：system-prompt 的"允许偶发重复"与 checklist 的"删重复"补判定边界——仅允许修辞性回响，事实性重复仍禁止
- **消除清单漂移风险**：workflow Step 4 的内嵌清单（6 项）是 checklist.md（8 项）的陈旧子集，改为指向 checklist.md 单一事实来源
- **补缺**：checklist 补"Hook 长度"行（workflow 有约束、清单漏了）；新增"机检项"区，标明哪些行由脚本覆盖
- **新增** `scripts/check_article.py`：机检禁用语（中英双语）、第三人称残留、段落句数、段首枚举、hook 长度（--hook）；支持 `<!-- check:off/on -->` 豁免引文
- **新增** `examples/sample-article.md`：规则自我践行的示例成品 + AI 味改前改后对照
- **新增** user-profile 维护协议：每次写作会话后追加 Evolution Log，每月清理失效偏好
- **删除** 过期占位 `.gitkeep`

## 2026-10-13 — 平台层并仓（消除第三处规则源）

- **新增** `references/platform-checklists.md`：合并聊天常用语中的平台适配层——平台适配检查三问 + 决策规则、PM 视角嫁接模板、人人都是产品经理专项清单与平台画像、微信公众号专项清单与平台画像
- **打通流程**：workflow Step 4 增加"按目标平台跑对应清单"，Step 5 增加"附平台投递建议"
- **规则升级**：「不采信今日头条」从常用语红线落进 system-prompt Data Rules 与 user-profile 来源标准（原为含糊的 "Reject certain platforms"）
- 常用语中的 Transitions/Emphasis/Prohibitions/Data Rules 与 system-prompt.md 重复，不另存——system-prompt.md 保持唯一事实来源

## 2026-10-13 — P0：SKILL.md 入口

- **新增** `SKILL.md`：frontmatter 触发契约（name + description 含负面触发："不用于短文案/代码/英文/日常写作"），正文为五步骨架 + 加载地图（何时读哪个文件）+ 红线速记
- README：结构图补 SKILL.md 行，Quick Start 第 0 步指向 SKILL.md
- 设计要点：入口文件不复制任何现有规则，只做路由——规则仍由 system-prompt.md / checklist.md 等单一文件持有

## 2026-10-14 — P1：渐进加载落地（规则由证据重写）

- **拆分并重写**：system-prompt.md 拆为 `references/voice-style.md`（角色/开头/结构/语言/结尾）+ `references/red-lines.md`（R1–R5），原文件删除；每条规则标注证据来源
- **证据来源**：9 篇样本拆解入库 `examples/exemplars/`（作者A5篇含作者自曝流程、作者B2篇、自己2篇+差距诊断）
- **Hook 规则修正**：三选一 → 四种钩菜单（场景/数据反常/结论前置/事件锚），约束改为 100-200 字 + 第一段不对术语下定义
- **结构规则修正**：禁"小标题串流" → 禁"目录式结构"；明确三种骨架（时间线踩坑/概念拆解/故事先行）
- **AI 味判据升级**（作者A归因：概率分布平均值）：口号式小标题 / 先果后因 / 段末总结句
- **workflow Step 1 升级**：新增"第一指令五要素"（角色/受众/核心观点/个人经历/语调，约10分钟）
- **标注机制升级**：新增困惑型标注（"我不确定这段成不成立"）
- **SKILL.md**：加载地图指向新文件；红线速记降级为目录
- 废弃：口语插入配额制、"至多1个技术术语"

## 2026-10-14 — 边界修正：他人拆解去引文化

- 作者A、作者B两份拆解删除全部原文引句，仅保留分析观察 + 原文链接；用户文章拆解全文保留
- 规则：仓库不放他人文章正文，他人内容最多以链接+改述出现


## 2026-10-14 — 匿名化：拆解去名去链

- 第三方拆解统一匿名：作者A（woshipm 5篇+1元文章）、作者B（woshipm 2篇），删除全部文章链接
- 仓库边界更新：他人内容以匿名改述出现，不出现作者姓名与原文链接

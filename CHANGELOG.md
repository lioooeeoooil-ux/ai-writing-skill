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
- **第三方拆解匿名化**：作者A（5篇+1元文章）/作者B（2篇）仅以匿名改述引用，无原文引句、姓名与链接；用户文章拆解全文保留——仓库边界：他人内容 = 匿名改述，不出现姓名与原文链接

## 2026-10-14 — P2：规则编号 + 标注统计 + 选题闸口

- **编号体系**：checklist G1–G11（新增 G10 选题三件套、G11 温度守恒）、平台清单 RR1–RR5 / WX1–WX4；标注优先级防双记（R-ID 记机器抓到的，G-ID 记人工独有的）
- **workflow**：新增 Step 0 选题痛点测试（读者画像/痛点场景/不写替代方案，三档处置：干货/随笔/打回）；第一指令核心观点挂观点三问（有人反对吗/我凭什么说/带走什么动作）；Step 3 标注格式 `[第N章] <ID> <问题> <处置>`
- **温度守恒**：voice-style 新增（干货 ≥2 处/随笔 ≥4 处具体的人和时刻，概念拆解型可用对话还原顶替）
- **统计纪律**（user-profile 维护协议）：每 3 篇文章统计标注 ID，0 命中进观察区、≥5 次升 Step 3；删除权限只给 G/RR/WX，R 系从脚本输出统计
- **启动协议**（README）：三种宿主的第一条消息模板（本对话框读 SKILL.md / 普通对话贴 bundle.md / skill 宿主挂载仓库）
- **新增** `scripts/build_bundle.py` + 生成 `bundle.md` 合订本——单文件版由脚本从源文件生成，杜绝手改 drift

## 2026-10-14 — P3：校验脚本回归测试 + CI

- **tests/**：`run_tests.py`（标准库 unittest 风格，零依赖）+ fixtures 一 ID 一文件（fail/ 按 G7/G8/R1/守卫/豁免/combo 组织，pass/ 含 sample-article 全文过检）；10/10 通过
- **CI**：`.github/workflows/test.yml`，push/PR 自动跑测试 + bundle.md 同步漂移检查（重新生成后 diff，不一致即红）
- 边界确认：G10/G11 与 R1 统计安全结构暂不机检——机检范围由实证决定（P2 统计纪律兜底）

## 2026-10-14 — P4：跨会话状态 + 真例银行

- **drafts/ 工作区约定**（gitignored，永不进公开仓库）：`state.md` 是唯一必读（当前位置/下一步/关键决策），chapters/ 存逐章稿，annotations.md 沿用 P2 标注格式，draft_full.md 是 Step 4 脚本检查对象
- **新增** `scripts/new_draft.py <slug>` 一键生成工作区骨架（已测）
- **断点续写**写入 README 启动方式第 4 条：新会话「读 drafts/<选题>/state.md 和 SKILL.md，从"下一步"继续」——小普"上下文断裂"问题的文件侧解法
- **真例银行** `examples/bank/` 立规：只收走完全流程的案例（state 摘要 + 标注台账 + 终稿），不收半成品、不收他人文章；第一位成员虚位留给 dogfood 文章
- 顺手还账：本地 CHANGELOG 此前已记 P3，本次一并推送

## 2026-10-16 — P5：三闸 + 审查 skill + 机检盲区（dogfood 实战勘误）

- **workflow 新增三闸**：Step 0.5 参考采集闸（10+ 篇、对账制、成句改写边界、无素材选题 15 篇强化）；Step 1.5 素材闸（热点/观点类豁免）；Step 1.6 大纲闸（每章五行+重心章≥30% 硬配比）
- **活稿协议入册**：assistant 每轮输出=可编辑文件；作者修改后以作者版为唯一基线（先 diff 对齐）
- **skills/reviewer/SKILL.md 建制**：写审分离，🔴必修/🟡随标注/🟢记录三色分级，红级打回限一次，终审权归作者
- **checker 升级 G12 机检辅助**：跨段 12 字滑窗重复检测（error）+ 破折号/4-gram 口头禅预警（warning），测试 12/12
- **references/pattern-bank.md**：招式库（结构模板/风格参数/口语骨架/诚实披露三件套）；key-chapter-method.md 立项待作者投喂重心章样本
- **checklist 新增 G12 冷读**：机检看不见的五种伤
- **dogfood 文章入籍**：examples/bank/rag-eval-ledger/（v5 终稿 + 27 条标注台账 + 流程教训：钩子被首章重复证伪、版本数必须对台账、参考必须真调用）

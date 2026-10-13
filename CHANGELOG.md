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

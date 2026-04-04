# AGENTS ENTRY (Universal, v0.3)

你正在为该用户提供任务支持。请按以下顺序加载约束：

1. `PROFILE_CORE.md`
2. `WORKING_PREFERENCES.md`
3. `DOMAIN_KNOWHOW.md`
4. `STYLE_GUIDE.md`

默认不加载 `docs/EVIDENCE_INDEX.md`；仅在出现争议或需要证据追溯时再读取。

## 检索路由

- AI 行业问题（公司/模型/评测/Agent/SaaS/策略判断）：先读 `AI_SCAN_RETRIEVAL.md` 并按其流程执行。
- 资料补充/案例扩展问题：先读 `BOOKMARKS_RETRIEVAL.md` 并按其流程执行。
- 两者都需要时：按 `AI_SCAN_RETRIEVAL.md` 第 8 节"双库协同"执行。
- AI 行业问题默认先用内库形成初步判断，再按需外网补充，不直接跳到纯 web 搜索。

禁止先无差别通读全部 `notes/AI行业扫描_md/*.md` 或 `bookmarks/bookmarks_md/*.md` 再回答。

## 冲突处理优先级

用户当次明确要求 > 项目内系统/开发者规则 > 本文件 > 历史偏好。

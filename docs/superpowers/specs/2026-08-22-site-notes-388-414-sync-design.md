# Site Notes 388–414 增量同步设计

日期：2026-08-22
状态：用户已在对话中确认

## 目标

把源索引中新加入的 #388–#414 共 27 条 Notes 同步到公开网页数据，使站点从 387 条更新为 414 条。

## 范围

- 阅读新增条目的标题、关键词、`why` 和必要的对应 Markdown。
- 每条 Note 归入现有七个主题中的 1–3 个。
- 更新 `site/topic_assignments.json`。
- 运行 `site/build_data.py` 重建 `site/data.json`。
- 验证总数、主题归属、来源链接、原始评论和既有正文引用。
- 在桌面端和手机端检查首页、最近更新、主题页 Notes 列表、搜索与筛选。

## 明确不做

- 不修改 `site/reviews/*.md` 七篇主题文章。
- 不修改 `site/index.html`、`site/css/style.css` 或 `site/js/app.js`。
- 不改写源 Notes 的标题、关键词或 `why`。
- 本轮完成后先提交候选分支并汇报，不直接合并或推送。

## 数据流

`notes/AI行业扫描_keywords.jsonl` 与 `site/topic_assignments.json` 由 `site/build_data.py` 读取，生成 `site/data.json`。网页继续通过现有 JavaScript 动态显示总数、月度收录、最近更新与各主题 Notes。

## 验收标准

1. `site/data.json` 包含连续的 #1–#414，共 414 条。
2. #388–#414 每条有 1–3 个合法主题。
3. 生成包中的 `why` 与源索引逐字一致。
4. 七篇 `site/reviews/*.md` 与实施前完全一致。
5. HTML、CSS 和 JavaScript 与实施前完全一致。
6. 数据合同与完整自动化测试通过。
7. 本地浏览器中总数、最新条目和主题筛选显示正常，桌面端及 390px 手机端无横向溢出和控制台错误。

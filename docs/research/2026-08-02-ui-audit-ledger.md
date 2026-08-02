# 网页 UI 与产品文案审查台账

| Location | Signal | Local intent or contract | Whole-page effect | Decision | Minimal change | Verification | Intentional keep or unresolved lead to disclose |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `site/css/style.css` `.act-tip` | 390px 首页出现横向滚动 | 月度柱图用于展示更新节奏 | tooltip 超出 viewport，移动端整页变宽 | fix | 640px 以下隐藏 hover tooltip，柱图和无障碍标签保留 | 自动合同 + 浏览器 scrollWidth | 无 |
| `:root --ink-3/--ink-4` | 小号灰字对比度不足 | 次要信息仍需可读 | 10–13px 元信息在浅色背景发灰 | fix | 改为 `#5e6976` / `#697481` | 对比度计算 + 页面查看 | 无 |
| 导航与 Hero kicker | `AI·SCAN`、英文档案口号与既有品牌冲突 | 用户明确要“AI 行业扫描 Notes”且姓名淡化 | 页面视觉成熟但品牌像另一套模板 | fix | 恢复中文品牌，姓名只留页尾作者区 | 合同测试 + 全文搜索 | 无 |
| 页面 microcopy | 多组 `FOCUS/INDEX/LATEST/ARTICLE/EVIDENCE/CONTENTS` | 编辑式信息层级可保留，不需要英文装饰词 | 英文标签叠加形成“档案模板”感 | fix | 改为研究主线、七个主题、最近新增、主题文章、证据浏览器、文章目录 | 文本审计 + 页面查看 | `Notes`、`Context`、`Eval` 等领域词保留 |
| `<head>` 描述 | 硬编码 360 条 | 页面计数由 `data.json` 运行时生成 | 新增 Notes 后搜索摘要过期 | fix | 元描述改为“持续更新”，可见计数继续取数据 | 合同测试 | 无 |
| serif + mono + grid background | editorial/terminal 类风格线索 | 这是研究文章与证据索引，不是通用 SaaS 落地页 | serif 用于标题、mono 用于编号和元信息，层级明确 | keep | 不改字体体系；减少不必要的全英文标签 | PC/移动端整体查看 | intentional keep：编辑型阅读场景支持该组合 |
| 蓝色强调与 2px 阅读进度 | 强 accent | 蓝色只用于链接、交互与阅读状态 | 形成清楚的动作和进度提示 | keep | 不新增渐变或多色状态 | 键盘焦点、hover、阅读进度 | intentional keep：颜色有交互职责 |
| 主题 dossier rows | 重复列表组件 | 七个同级主题需要横向比较 | 统一行结构帮助扫描，主副信息有层级 | keep | 保留行式索引，不改成卡片网格 | PC/移动端布局 | intentional keep：重复服务比较 |
| `site/js/app.js` 扫描相似段落 | 代码函数被文本扫描器大量误报 | 路由、搜索、引用卡、目录各自是独立行为 | 删除会破坏功能 | keep | 不按文本相似度合并无关函数 | JS 语法与交互测试 | intentional keep：49 个 code findings 均为结构性误报 |
| `site/index.html` 扫描相似段落 | HTML section 容器被判为重复 | Hero、研究主线、主题、最近更新、作者、文章、证据各有不同任务 | 统一标签结构未抹平层级 | keep | 仅清理重复英文微文案 | 整页阅读与可访问性检查 | intentional keep：23 个 findings 多为标签与容器结构误报 |
| Product copy | 英文模板感、过期数量、品牌漂移 | 用通俗中文说明站点用途与操作 | 影响第一印象和可理解性 | fixed | 品牌和微文案中文化，计数动态化 | 文本审计、合同测试、浏览器 QA | `AI Coding` 等固定主题名为 intentional keep |

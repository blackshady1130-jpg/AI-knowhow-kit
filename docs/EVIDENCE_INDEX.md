# EVIDENCE_INDEX

版本：v0.2  
更新日期：2026-03-02

## 1) 覆盖率说明

- Blog：5/5 文件全文抽取。
- Analysis：`AI行业扫描.xlsx` 第一张表全行读取，184 条有效记录。
- Chat：`conversations-000~003.json` 全会话解析（371 个会话）。
- `chat.html` 已做哈希与大小校验，确认其核心内容与 JSON 导出载荷一致。

## 2) 核心审计文件

- `docs/sources/full_pass_audit_v2.json`：全量覆盖审计与哈希。
- `docs/sources/v2_chat_evidence.json`：聊天偏好、身份线索、任务标签。
- `docs/sources/v2_analysis_evidence.json`：AIreview 结构与关键词。
- `docs/sources/v2_analysis_theme_map.json`：AIreview 主题图谱。
- `docs/sources/v2_blog_style_evidence.json`：博客文风特征。

## 3) 关键统计（v0.2）

- 用户消息（非空文本）：1305（角色节点计数：user 1313 / assistant 4129 / tool 1699 / system 1456）。
- 任务标签（多标签）：
  - `ai_research` 616
  - `mental_health` 305
  - `doc_ppt` 270
  - `coding_data` 213
  - `image_gen` 118
- AIreview 主题关注：
  - Agent/Infra/Coding：59
  - Product/Business/SaaS：46
  - Eval/Benchmark：44
  - Context/Memory/RAG：28

## 4) 证据使用规则

1. 只有“跨会话复现”的信息可进入稳定画像。  
2. 模拟角色、代写场景、引用内容不直接作为事实。  
3. 若新证据与旧结论冲突，先降级为“待验证”，再更新核心文件。  

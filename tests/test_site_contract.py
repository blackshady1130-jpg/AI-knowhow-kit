import json
import re
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
SITE = ROOT / "site"
NOTES_INDEX = ROOT / "notes" / "AI行业扫描_keywords.jsonl"
ASSIGNMENTS = SITE / "topic_assignments.json"
TOPICS = SITE / "topics.json"
DATA = SITE / "data.json"
INDEX = SITE / "index.html"
STYLES = SITE / "css" / "style.css"
APP_JS = SITE / "js" / "app.js"
REVIEWS = SITE / "reviews"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def load_jsonl(path: Path):
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8-sig").splitlines()
        if line.strip()
    ]


class SiteRepositoryStatusContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.readme = README.read_text(encoding="utf-8-sig")

    def test_readme_reports_the_current_public_index(self):
        self.assertIn("当前公开索引（更新至 2026-08）：", self.readme)
        self.assertIn("https://blackshady1130-jpg.github.io/AI-knowhow-kit/#home", self.readme)
        self.assertRegex(self.readme, r"\| `notes/` \|[^\n]+\| 424 条 \|")
        self.assertRegex(self.readme, r"\| `bookmarks/` \|[^\n]+\| 861 条 \|")
        self.assertRegex(self.readme, r"\| `skills/` \|[^\n]+\| 6 个 \|")
        self.assertNotIn("截至 2026-08-02", self.readme)


class SiteDataContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.notes = load_jsonl(NOTES_INDEX)
        cls.assignments = load_json(ASSIGNMENTS)
        cls.topics = load_json(TOPICS)
        cls.bundle = load_json(DATA)

    def test_all_source_notes_have_one_to_three_valid_topic_assignments(self):
        note_ids = {str(note["id"]) for note in self.notes}
        self.assertEqual(len(self.notes), len(note_ids))
        self.assertEqual(note_ids, set(self.assignments))

        valid_topics = {topic["name"] for topic in self.topics}
        for note_id, topics in self.assignments.items():
            self.assertGreaterEqual(len(topics), 1, note_id)
            self.assertLessEqual(len(topics), 3, note_id)
            self.assertTrue(set(topics) <= valid_topics, note_id)

    def test_new_notes_361_to_387_are_classified(self):
        expected = {str(note_id) for note_id in range(361, 388)}
        self.assertTrue(expected <= set(self.assignments))
        for note_id in expected:
            self.assertTrue(self.assignments[note_id], note_id)

    def test_new_notes_415_to_424_are_classified(self):
        expected = {str(note_id) for note_id in range(415, 425)}
        self.assertTrue(expected <= set(self.assignments))
        for note_id in expected:
            self.assertTrue(self.assignments[note_id], note_id)

    def test_generated_bundle_contains_all_notes_and_preserves_authored_why(self):
        self.assertEqual(len(self.notes), self.bundle["meta"]["total_notes"])
        self.assertEqual(len(self.notes), len(self.bundle["notes"]))
        source_why = {int(note["id"]): note.get("why") or "" for note in self.notes}
        bundled_why = {int(note["id"]): note.get("why") or "" for note in self.bundle["notes"]}
        self.assertEqual(source_why, bundled_why)

    def test_review_note_ids_resolve_to_existing_notes(self):
        note_ids = {int(note["id"]) for note in self.bundle["notes"]}
        for topic in self.bundle["topics"]:
            review_ids = topic.get("review_note_ids")
            self.assertIsInstance(review_ids, list, topic["name"])
            self.assertTrue(review_ids, topic["name"])
            self.assertTrue(set(review_ids) <= note_ids, topic["name"])

    def test_source_links_extract_a_safe_primary_http_url(self):
        notes = {int(note["id"]): note for note in self.bundle["notes"]}
        for note in notes.values():
            source_url = note.get("source_url")
            self.assertIsNotNone(source_url, note["id"])
            self.assertTrue(
                not source_url or source_url.startswith(("http://", "https://")),
                f"unsafe source_url for {note['id']}: {source_url}",
            )
        self.assertEqual(
            "https://mp.weixin.qq.com/s/iBVj-bcEtVbOGWEqwWp6EA",
            notes[1]["source_url"],
        )
        self.assertEqual(
            "https://openai.com/index/separating-signal-from-noise-coding-evaluations/",
            notes[360]["source_url"],
        )


class TopicMetadataContractTests(unittest.TestCase):
    PLAIN_TOPIC_NAMES = {
        "评测与基准",
        "架构与工程",
        "模型推理与训练",
        "AI Coding",
        "AI 产品与交互",
        "行业格局与企业战略",
        "AI 安全与影响",
    }

    def test_seven_topics_define_their_role_in_one_research_arc(self):
        topics = load_json(TOPICS)
        self.assertEqual(7, len(topics))
        self.assertEqual(self.PLAIN_TOPIC_NAMES, {topic["name"] for topic in topics})
        for topic in topics:
            for field in ("chapter", "role", "question", "thesis", "article_title"):
                self.assertTrue(topic.get(field), f"{topic['name']} missing {field}")

        coding = next(topic for topic in topics if topic["name"] == "AI Coding")
        strategy = next(topic for topic in topics if topic["name"] == "行业格局与企业战略")
        self.assertEqual("代码开发案例", coding["role"])
        self.assertEqual("市场与商业模式", strategy["role"])

    def test_topics_record_article_review_date(self):
        topics = load_json(TOPICS)
        self.assertEqual(7, len(topics))
        for topic in topics:
            review_updated_at = topic.get("review_updated_at", "")
            self.assertRegex(review_updated_at, r"^\d{4}-\d{2}-\d{2}$", topic["name"])


class ReviewContractTests(unittest.TestCase):
    INSTRUMENTS = {
        "model-training.md": "模型比较清单",
        "architecture-engineering.md": "长程 Agent 运行清单",
        "eval-benchmark.md": "评测检查表",
        "ai-coding.md": "任务分级与成本记录表",
        "product-interaction.md": "权限与人工接管分级表",
        "industry-strategy.md": "AI 项目商业价值检查表",
        "impact-safety.md": "责任与额外人工成本清单",
    }
    ARTICLE_TITLES = {
        "model-training.md": "模型能力是怎样训练出来的",
        "architecture-engineering.md": "长程 Agent 如何运行：Context、状态、权限与恢复",
        "eval-benchmark.md": "如何判断一个 Agent 评测是否可信",
        "ai-coding.md": "AI Coding 如何改变软件开发的成本",
        "product-interaction.md": "AI 产品如何展示状态、管理权限和支持人工接管",
        "industry-strategy.md": "模型降价之后，AI 企业靠什么赚钱",
        "impact-safety.md": "AI 如何改变人的判断、工作和责任",
    }
    NEW_EVIDENCE = {
        "model-training.md": {363, 374, 377, 385},
        "architecture-engineering.md": {369, 370, 377, 382, 384},
        "eval-benchmark.md": {373, 374, 375},
        "ai-coding.md": {370, 373, 374, 386},
        "product-interaction.md": {369, 375, 382},
        "industry-strategy.md": {361, 366, 367, 378, 379, 383},
        "impact-safety.md": {361, 368, 382, 384},
    }

    @classmethod
    def setUpClass(cls):
        cls.review_files = sorted(REVIEWS.glob("*.md"))
        cls.review_text = {
            path.name: path.read_text(encoding="utf-8-sig") for path in cls.review_files
        }

    def test_seven_reviews_are_substantial_and_not_one_shared_template(self):
        self.assertEqual(7, len(self.review_files))
        heading_sequences = []
        for name, text in self.review_text.items():
            chinese_characters = re.findall(r"[\u4e00-\u9fff]", text)
            self.assertGreaterEqual(len(chinese_characters), 1800, name)
            self.assertNotIn("## 2026 年 6—7 月新增观察", text, name)
            self.assertNotIn("## 在研究主线中的位置", text, name)
            self.assertNotIn("### 洞察 1", text, name)
            headings = tuple(re.findall(r"^## .+$", text, flags=re.MULTILINE))
            heading_sequences.append(headings)
        self.assertEqual(7, len(set(heading_sequences)))

    def test_every_review_has_boundaries_specific_instrument_and_falsifiers(self):
        for name, text in self.review_text.items():
            self.assertIn("核心判断", text, name)
            self.assertIn("边界", text, name)
            self.assertIn(self.INSTRUMENTS[name], text, name)
            self.assertRegex(text, r"## .*(证伪|修正|改变)", name)
            falsifier_section = re.split(
                r"^## .*(?:证伪|修正|改变).*$", text, flags=re.MULTILINE
            )
            self.assertGreaterEqual(len(falsifier_section), 2, name)
            numbered_conditions = re.findall(r"^\d+\. ", falsifier_section[-1], flags=re.MULTILINE)
            self.assertGreaterEqual(len(numbered_conditions), 2, name)
            self.assertLessEqual(len(numbered_conditions), 3, name)

    def test_new_evidence_is_integrated_and_all_references_resolve(self):
        note_ids = {int(note["id"]) for note in load_jsonl(NOTES_INDEX)}
        for name, text in self.review_text.items():
            refs = {int(match) for match in re.findall(r"#(\d+)", text)}
            self.assertTrue(refs <= note_ids, f"{name} has broken refs {refs - note_ids}")
            self.assertTrue(self.NEW_EVIDENCE[name] <= refs, f"{name} missing new evidence")

    def test_stale_or_overstated_copy_is_absent(self):
        all_reviews = "\n".join(self.review_text.values())
        self.assertNotIn("这 56 篇", all_reviews)
        self.assertNotIn("证明了 Claude 有意识", all_reviews)
        self.assertNotIn("所有任务都", all_reviews)

    def test_articles_use_plain_titles_and_avoid_packaged_headings(self):
        all_reviews = "\n".join(self.review_text.values())
        for name, expected_title in self.ARTICLE_TITLES.items():
            self.assertTrue(
                self.review_text[name].startswith(f"# {expected_title}\n"),
                name,
            )
        for phrase in (
            "共同定界",
            "实验合同",
            "推理空间",
            "提示词外壳",
            "持续运行的前台",
            "状态可见性决定协作带宽",
            "失败兜底",
            "责任节点",
            "价值捕获",
            "自动带来赋权",
        ):
            self.assertNotIn(phrase, all_reviews, phrase)


class SitePageContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = INDEX.read_text(encoding="utf-8-sig")
        cls.css = STYLES.read_text(encoding="utf-8-sig") if STYLES.exists() else ""
        cls.app_js = APP_JS.read_text(encoding="utf-8-sig") if APP_JS.exists() else ""
        cls.runtime = cls.html + "\n" + cls.app_js

    def test_homepage_leads_with_personal_thesis_and_collaboration_entry(self):
        self.assertIn("关注 AI 如何用于真实工作", self.html)
        self.assertIn('id="research-path"', self.html)
        self.assertIn('id="collaborate"', self.html)
        self.assertIn("阅读七个主题", self.html)
        self.assertIn("联系与合作", self.html)

    def test_homepage_uses_an_editorial_not_generic_ai_landing_page(self):
        self.assertIn('id="home-hero"', self.html)
        self.assertIn('id="topicGrid" class="dossier', self.html)
        self.assertIn('class="dossier-row', self.app_js)
        self.assertNotIn("bg-gradient-to-br", self.html)
        self.assertNotIn("topic.icon", self.runtime)
        self.assertNotIn("17.8 万字", self.html)
        self.assertNotIn("所有 notes 均经过人工 review", self.html)
        self.assertNotIn("LATEST NOTES", self.html)

    def test_site_uses_plain_topic_names_and_limits_personal_name_to_contact(self):
        self.assertIn("AI 行业扫描 Notes", self.runtime)
        self.assertEqual(1, self.runtime.count("Yantao"))
        self.assertNotIn("系统怎样接住", self.runtime)
        self.assertNotIn("AI·SCAN", self.runtime)
        self.assertNotIn("PERSONAL RESEARCH ARCHIVE", self.runtime)
        self.assertIn("esc(t.name)", self.app_js)

    def test_renamed_safety_topic_keeps_old_hash_compatible(self):
        self.assertRegex(self.app_js, r"['\"]AI 影响与安全['\"]\s*:\s*['\"]AI 安全与影响['\"]")
        self.assertRegex(self.app_js, r"TOPIC_ALIASES\[name\]\s*\|\|\s*name")

    def test_note_browser_exposes_cited_recent_and_all_views(self):
        for marker in (
            'data-note-view="cited"',
            'data-note-view="recent"',
            'data-note-view="all"',
            'id="noteSearch"',
            'id="noteType"',
            'id="loadMoreBtn"',
        ):
            self.assertIn(marker, self.runtime)

    def test_notes_have_accurate_provenance_and_native_links(self):
        self.assertIn("索引关键词（原条目无评论）", self.app_js)
        self.assertIn('class="lat-row', self.app_js)
        self.assertIn('<button type="button" class="note-ref"', self.app_js)

    def test_reference_click_does_not_immediately_close_hovered_tooltip(self):
        self.assertNotIn("activeReference === btn", self.app_js)
        self.assertRegex(
            self.app_js,
            r"btn\.addEventListener\('click',\s*e\s*=>\s*\{\s*"
            r"e\.stopPropagation\(\);\s*showReference\(btn\);",
        )

    def test_page_logic_supports_search_filter_and_incremental_loading(self):
        for symbol in (
            "curNoteView",
            "curQuery",
            "curType",
            "visibleNoteCount",
            "renderNoteBrowser",
            "loadMoreNotes",
        ):
            self.assertIn(symbol, self.app_js)

    def test_data_bundle_is_requested_without_stale_browser_cache(self):
        self.assertRegex(
            self.app_js,
            r"fetch\(['\"]data\.json['\"]\s*,\s*\{\s*cache:\s*['\"]no-store['\"]\s*\}\)",
        )

    def test_split_runtime_assets_are_local_and_present(self):
        self.assertTrue(STYLES.exists())
        self.assertTrue(APP_JS.exists())
        self.assertIn('href="css/style.css"', self.html)
        self.assertIn('src="js/app.js"', self.html)

    def test_mobile_layout_hides_activity_tooltips_and_prevents_overflow(self):
        compact = re.sub(r"\s+", "", self.css)
        self.assertIn("overflow-x:hidden", compact)
        self.assertRegex(compact, r"@media\(max-width:640px\).*?\.act-tip\{display:none\}")

    def test_activity_chart_highlights_latest_month_not_highest_count(self):
        self.assertIn("const latestMonth = months[months.length - 1]", self.app_js)
        self.assertIn("k === latestMonth ? ' latest' : ''", self.app_js)
        self.assertNotIn("c === max ? ' peak' : ''", self.app_js)
        self.assertIn(".act-col.latest .act-bar", self.css)

    def test_secondary_text_tokens_meet_readability_baseline(self):
        compact = re.sub(r"\s+", "", self.css).lower()
        self.assertIn("--ink-3:#5e6976", compact)
        self.assertIn("--ink-4:#697481", compact)

    def test_metadata_does_not_hardcode_a_stale_note_count(self):
        head = self.html.split("</head>", 1)[0]
        self.assertNotRegex(head, r"\b(?:360|365|387)\s*条")

    def test_page_distinguishes_review_and_notes_freshness(self):
        self.assertIn("'Notes 更新于 ' + D.meta.generated_at", self.app_js)
        self.assertIn("'文章复核 ' + topic.review_updated_at", self.app_js)
        self.assertIn("'Notes 同步 ' + D.meta.generated_at", self.app_js)
        self.assertNotIn(" · 更新至 ' + D.meta.generated_at", self.app_js)

    def test_app_javascript_parses(self):
        result = subprocess.run(
            ["node", "--check", str(APP_JS)],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
        self.assertEqual(0, result.returncode, result.stderr)


if __name__ == "__main__":
    unittest.main()

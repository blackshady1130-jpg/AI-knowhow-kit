import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
NOTES_INDEX = ROOT / "notes" / "AI行业扫描_keywords.jsonl"
ASSIGNMENTS = SITE / "topic_assignments.json"
TOPICS = SITE / "topics.json"
DATA = SITE / "data.json"
INDEX = SITE / "index.html"
REVIEWS = SITE / "reviews"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def load_jsonl(path: Path):
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8-sig").splitlines()
        if line.strip()
    ]


class SiteDataContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.notes = load_jsonl(NOTES_INDEX)
        cls.assignments = load_json(ASSIGNMENTS)
        cls.topics = load_json(TOPICS)
        cls.bundle = load_json(DATA)

    def test_all_350_notes_have_one_to_three_valid_topic_assignments(self):
        note_ids = {str(note["id"]) for note in self.notes}
        self.assertEqual(350, len(note_ids))
        self.assertEqual(note_ids, set(self.assignments))

        valid_topics = {topic["name"] for topic in self.topics}
        for note_id, topics in self.assignments.items():
            self.assertGreaterEqual(len(topics), 1, note_id)
            self.assertLessEqual(len(topics), 3, note_id)
            self.assertTrue(set(topics) <= valid_topics, note_id)

    def test_generated_bundle_contains_all_notes_and_preserves_authored_why(self):
        self.assertEqual(350, self.bundle["meta"]["total_notes"])
        self.assertEqual(350, len(self.bundle["notes"]))
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


class TopicMetadataContractTests(unittest.TestCase):
    def test_seven_topics_define_their_role_in_one_research_arc(self):
        topics = load_json(TOPICS)
        self.assertEqual(7, len(topics))
        for topic in topics:
            for field in ("chapter", "role", "question", "thesis"):
                self.assertTrue(topic.get(field), f"{topic['name']} missing {field}")

        coding = next(topic for topic in topics if topic["name"] == "AI Coding")
        strategy = next(topic for topic in topics if topic["name"] == "行业格局与企业战略")
        self.assertIn("高反馈验证场", coding["role"])
        self.assertIn("部署与价值捕获", strategy["role"])


class ReviewContractTests(unittest.TestCase):
    REQUIRED_HEADINGS = (
        "## 本章核心判断",
        "## 在研究主线中的位置",
        "## 关键判断",
        "## 2026 年 6—7 月新增观察",
        "## 对实践意味着什么",
        "## 接下来如何证伪",
    )

    def test_all_seven_reviews_follow_the_deep_read_contract(self):
        review_files = sorted(REVIEWS.glob("*.md"))
        self.assertEqual(7, len(review_files))
        for path in review_files:
            text = path.read_text(encoding="utf-8-sig")
            for heading in self.REQUIRED_HEADINGS:
                self.assertIn(heading, text, f"{path.name} missing {heading}")

    def test_every_review_uses_new_evidence_and_all_references_resolve(self):
        note_ids = {int(note["id"]) for note in load_jsonl(NOTES_INDEX)}
        for path in sorted(REVIEWS.glob("*.md")):
            text = path.read_text(encoding="utf-8-sig")
            refs = {int(match) for match in re.findall(r"#(\d+)", text)}
            self.assertTrue(refs <= note_ids, f"{path.name} has broken refs {refs - note_ids}")
            self.assertTrue(
                any(290 <= note_id <= 350 for note_id in refs),
                f"{path.name} does not cite notes 290-350",
            )


class SitePageContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = INDEX.read_text(encoding="utf-8-sig")

    def test_homepage_leads_with_personal_thesis_and_collaboration_entry(self):
        self.assertIn(
            "研究模型如何进入真实组织，并把使用过程变成可验证、可持续改进的学习闭环",
            self.html,
        )
        self.assertIn('id="research-arc"', self.html)
        self.assertIn('id="collaborate"', self.html)
        self.assertIn("沿研究主线阅读", self.html)
        self.assertIn("交流真实工作流", self.html)

    def test_note_browser_exposes_cited_recent_and_all_views(self):
        for marker in (
            'data-note-view="cited"',
            'data-note-view="recent"',
            'data-note-view="all"',
            'id="noteSearch"',
            'id="noteType"',
            'id="loadMoreBtn"',
        ):
            self.assertIn(marker, self.html)

    def test_page_logic_supports_search_filter_and_incremental_loading(self):
        for symbol in (
            "curNoteView",
            "curQuery",
            "curType",
            "visibleNoteCount",
            "renderNoteBrowser",
            "loadMoreNotes",
        ):
            self.assertIn(symbol, self.html)


if __name__ == "__main__":
    unittest.main()

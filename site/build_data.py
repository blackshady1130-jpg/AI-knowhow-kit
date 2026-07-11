#!/usr/bin/env python3
"""Build the GitHub Pages data bundle from note indexes and site sources."""

from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
NOTES_INDEX = ROOT / "notes" / "AI行业扫描_keywords.jsonl"
TOPICS_FILE = SITE / "topics.json"
ASSIGNMENTS_FILE = SITE / "topic_assignments.json"
REVIEWS_DIR = SITE / "reviews"
OUTPUT_FILE = SITE / "data.json"


def load_json(path: Path):
    with path.open("r", encoding="utf-8-sig") as f:
        return json.load(f)


def load_notes(path: Path) -> list[dict]:
    notes: list[dict] = []
    with path.open("r", encoding="utf-8-sig") as f:
        for line_no, line in enumerate(f, 1):
            text = line.strip()
            if not text:
                continue
            try:
                notes.append(json.loads(text))
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSONL at {path}:{line_no}: {exc}") from exc
    return notes


def short_why(text: str | None, limit: int = 220) -> str:
    if not text:
        return ""
    compact = " ".join(str(text).split())
    if len(compact) <= limit:
        return compact
    return compact[:limit].rstrip() + "..."


def fallback_why(note: dict) -> str:
    keywords = [str(item).strip() for item in note.get("keywords", []) if str(item).strip()]
    if keywords:
        return "关键词：" + "、".join(keywords[:8])
    return note.get("title") or ""


def primary_source_url(value: str | None) -> str:
    """Extract a browser-safe primary link while preserving the raw source field."""
    text = str(value or "").strip()
    match = re.search(r"https?://[^\s]+", text)
    if match:
        return match.group(0).rstrip(".,;:!?，。；：！？)]}）】》>\"'")
    bare_x = re.search(r"(?<![\w.])x\.com/[^\s]+", text)
    if bare_x:
        return ("https://" + bare_x.group(0)).rstrip(".,;:!?，。；：！？)]}）】》>\"'")
    return ""


def month_key(value: str | None) -> str:
    if not value:
        return ""
    return str(value)[:7]


def format_date_range(values: list[str]) -> str:
    months = sorted({month_key(v) for v in values if month_key(v)})
    if not months:
        return ""
    if months[0] == months[-1]:
        return months[0]
    return f"{months[0]} ~ {months[-1]}"


def extract_review_note_ids(markdown: str) -> list[int]:
    """Return unique #id references in first-appearance order."""
    seen: set[int] = set()
    result: list[int] = []
    for match in re.finditer(r"#(\d+)", markdown):
        note_id = int(match.group(1))
        if note_id not in seen:
            seen.add(note_id)
            result.append(note_id)
    return result


def main() -> None:
    topics = load_json(TOPICS_FILE)
    assignments_raw = load_json(ASSIGNMENTS_FILE)
    assignments = {int(k): v for k, v in assignments_raw.items()}
    valid_topics = {topic["name"] for topic in topics}

    notes = load_notes(NOTES_INDEX)
    note_ids = {int(note["id"]) for note in notes}

    missing_assignments = sorted(note_ids - set(assignments))
    extra_assignments = sorted(set(assignments) - note_ids)
    if missing_assignments:
        raise SystemExit(f"Missing topic assignments for note ids: {missing_assignments}")
    if extra_assignments:
        raise SystemExit(f"Topic assignments reference unknown note ids: {extra_assignments}")

    site_notes: list[dict] = []
    for note in sorted(notes, key=lambda item: int(item["id"])):
        note_id = int(note["id"])
        note_topics = assignments[note_id]
        unknown_topics = sorted(set(note_topics) - valid_topics)
        if unknown_topics:
            raise SystemExit(f"Note {note_id} has unknown topics: {unknown_topics}")
        why = note.get("why") or ""
        why_short = short_why(why) or fallback_why(note)
        site_notes.append(
            {
                "id": note_id,
                "title": note.get("title") or "",
                "date": note.get("date"),
                "type": note.get("type") or "",
                "url": note.get("url") or "",
                "source_url": primary_source_url(note.get("url")),
                "keywords": note.get("keywords") or [],
                "topics": note_topics,
                "why": why,
                "why_short": why_short,
            }
        )

    for topic in topics:
        review_path = REVIEWS_DIR / topic["review_file"]
        if not review_path.exists():
            raise SystemExit(f"Missing review file: {review_path}")
        topic_notes = [note for note in site_notes if topic["name"] in note["topics"]]
        review = review_path.read_text(encoding="utf-8-sig")
        review_note_ids = extract_review_note_ids(review)
        unknown_review_ids = sorted(set(review_note_ids) - note_ids)
        if unknown_review_ids:
            raise SystemExit(
                f"Review {review_path.name} references unknown note ids: {unknown_review_ids}"
            )
        topic["count"] = len(topic_notes)
        topic["date_range"] = format_date_range([note.get("date") for note in topic_notes])
        topic["review"] = review
        topic["review_note_ids"] = review_note_ids

    data = {
        "meta": {
            "total_notes": len(site_notes),
            "total_topics": len(topics),
            "date_range": format_date_range([note.get("date") for note in site_notes]),
            "total_why_chars": sum(len(note.get("why") or "") for note in site_notes),
            "generated_at": date.today().isoformat(),
        },
        "topics": topics,
        "notes": site_notes,
    }

    OUTPUT_FILE.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        f"Wrote {OUTPUT_FILE.relative_to(ROOT)} "
        f"({len(site_notes)} notes, {len(topics)} topics)"
    )


if __name__ == "__main__":
    main()

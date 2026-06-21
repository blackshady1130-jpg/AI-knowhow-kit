#!/usr/bin/env python3
"""Collect a prototype AI industry weekly digest from local source memory and public feeds."""

from __future__ import annotations

import argparse
import email.utils
import html
import json
import math
import os
import re
import sys
import textwrap
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
import socket
from collections import Counter, defaultdict
from dataclasses import dataclass, asdict
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Any


THEMES = {
    "Agent/Harness": [
        "agent", "agents", "agentic", "harness", "tool use", "tools", "mcp",
        "workflow", "computer use", "browser", "runtime", "scaffold", "skills",
        "multi-agent", "autonomous", "long-horizon", "long horizon", "coding agent",
        "智能体", "上下文工程", "工具调用", "执行环境", "脚手架"
    ],
    "Eval/Benchmark": [
        "eval", "evaluation", "benchmark", "bench", "judge", "rubric",
        "leaderboard", "metric", "verified", "swe-bench", "terminal-bench",
        "评测", "基准", "榜单", "指标", "验证"
    ],
    "Model Training": [
        "training", "post-training", "pretraining", "pre-training", "rlhf", "rlvr",
        "reward", "distillation", "sft", "reasoning", "inference", "scaling",
        "alignment", "fine-tuning", "finetuning", "reinforcement",
        "训练", "后训练", "强化学习", "蒸馏", "推理模型", "奖励"
    ],
    "Context/Memory/RAG": [
        "context", "memory", "rag", "retrieval", "cache", "prompt caching",
        "long context", "knowledge", "compaction", "上下文", "记忆", "检索", "缓存", "知识库"
    ],
    "AI Coding": [
        "coding", "code", "developer", "github", "cursor", "claude code",
        "codex", "software engineering", "pr", "repo", "programming",
        "编程", "代码", "软件工程"
    ],
    "Product/SaaS/Business": [
        "product", "saas", "business", "enterprise", "gtm", "pricing", "roi",
        "deployment", "fde", "startup", "market", "revenue", "customer",
        "产品", "商业", "企业", "收入", "部署", "交付"
    ],
    "Safety/Governance": [
        "safety", "policy", "governance", "risk", "security", "misuse",
        "alignment", "wellbeing", "privacy", "安全", "治理", "风险", "隐私"
    ],
}

CORE_AI_PATTERNS = [
    r"\bai\b", r"\bllm\b", r"\bllms\b", r"\bagent\b", r"\bagents\b", r"\bagentic\b",
    r"\bmodel\b", r"\bmodels\b", r"machine learning", r"\bml\b", r"\bcopilot\b",
    r"\bcodex\b", r"\bopenai\b", r"\banthropic\b", r"\bclaude\b", r"\bgpt\b",
    r"\bbenchmark\b", r"\beval\b", r"\bevaluation\b", r"\breasoning\b",
    r"post-training", r"pre-training", r"fine-tuning", r"\brlhf\b", r"\brlvr\b",
    r"\brag\b", r"\bmcp\b", r"\bharness\b", r"人工智能", r"大模型", r"模型",
    r"智能体", r"评测", r"推理", r"上下文", r"后训练"
]

NOISE_TERMS = [
    "coupon", "discount", "giveaway", "top 100 tools", "tool directory",
    "prompt collection", "sale", "deal", "crypto price", "magic quadrant",
    "recognized as a leader", "named a leader", "gartner"
]


@dataclass
class FeedItem:
    source_id: str
    source_name: str
    source_kind: str
    source_trust_tier: str
    title: str
    url: str
    published: str | None
    summary: str
    topics: list[str]
    score: float
    why: str
    known_in_library: bool


def repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def skill_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if not path.exists():
        return rows
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return rows


def strip_html(value: str) -> str:
    value = re.sub(r"<script[\s\S]*?</script>", " ", value, flags=re.I)
    value = re.sub(r"<style[\s\S]*?</style>", " ", value, flags=re.I)
    value = re.sub(r"<[^>]+>", " ", value)
    value = html.unescape(value)
    return re.sub(r"\s+", " ", value).strip()


def normalize_url(url: str) -> str:
    try:
        parsed = urllib.parse.urlsplit(url.strip())
    except ValueError:
        return url.strip()
    host = parsed.netloc.lower()
    path = parsed.path.rstrip("/")
    return urllib.parse.urlunsplit((parsed.scheme.lower(), host, path, "", ""))


def host_from_url(url: str) -> str | None:
    try:
        return urllib.parse.urlsplit(url).netloc.lower()
    except ValueError:
        return None


def urls_from_text(value: str) -> list[str]:
    return re.findall(r"https?://[^\s\)\]\"<>]+", value or "")


def parse_datetime(value: str | None) -> datetime | None:
    if not value:
        return None
    value = value.strip()
    try:
        dt = email.utils.parsedate_to_datetime(value)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)
    except (TypeError, ValueError):
        pass
    for candidate in (value, value.replace("Z", "+00:00")):
        try:
            dt = datetime.fromisoformat(candidate)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt.astimezone(timezone.utc)
        except ValueError:
            continue
    return None


def text_of(node: ET.Element | None) -> str:
    if node is None or node.text is None:
        return ""
    return node.text.strip()


def first_text(node: ET.Element, names: list[str]) -> str:
    for name in names:
        found = node.find(name)
        if found is not None and found.text:
            return found.text.strip()
    # Namespace fallback.
    for child in node:
        local = child.tag.rsplit("}", 1)[-1]
        if local in {n.rsplit("}", 1)[-1] for n in names} and child.text:
            return child.text.strip()
    return ""


def first_atom_link(entry: ET.Element) -> str:
    for child in entry:
        if child.tag.rsplit("}", 1)[-1] == "link":
            href = child.attrib.get("href")
            rel = child.attrib.get("rel", "alternate")
            if href and rel == "alternate":
                return href
    return ""


def parse_feed(xml_bytes: bytes, source: dict[str, Any]) -> list[dict[str, Any]]:
    root = ET.fromstring(xml_bytes)
    items: list[dict[str, Any]] = []
    local_root = root.tag.rsplit("}", 1)[-1].lower()
    if local_root == "rss" or root.find("channel") is not None:
        channel = root.find("channel")
        if channel is None:
            return []
        for item in channel.findall("item"):
            title = first_text(item, ["title"])
            link = first_text(item, ["link"])
            published = first_text(item, ["pubDate", "date", "{http://purl.org/dc/elements/1.1/}date"])
            summary = first_text(item, ["description", "{http://purl.org/rss/1.0/modules/content/}encoded"])
            guid = first_text(item, ["guid"])
            items.append({
                "title": strip_html(title),
                "url": link or guid,
                "published_raw": published,
                "summary": strip_html(summary),
            })
    else:
        entries = [e for e in root.iter() if e.tag.rsplit("}", 1)[-1] == "entry"]
        for entry in entries:
            title = first_text(entry, ["title"])
            link = first_atom_link(entry)
            published = first_text(entry, ["published", "updated"])
            summary = first_text(entry, ["summary", "content"])
            items.append({
                "title": strip_html(title),
                "url": link,
                "published_raw": published,
                "summary": strip_html(summary),
            })
    return [i for i in items if i.get("title") and i.get("url")]


def fetch(url: str, timeout: int = 12) -> bytes:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "AI_knowhow_kit weekly intel collector/0.1 (+local skill prototype)",
            "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml, */*",
        },
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read()


def theme_hits(title: str, summary: str) -> tuple[list[str], int]:
    text = f"{title}\n{summary}".lower()
    matched: list[str] = []
    hit_count = 0
    for theme, keywords in THEMES.items():
        local_hits = 0
        for kw in keywords:
            if kw.lower() in text:
                local_hits += 1
        if local_hits:
            matched.append(theme)
            hit_count += min(local_hits, 5)
    return matched, hit_count


def has_core_ai_signal(title: str, summary: str) -> bool:
    text = f"{title}\n{summary}".lower()
    return any(re.search(pattern, text, flags=re.I) for pattern in CORE_AI_PATTERNS)


def build_internal_memory(root: Path) -> dict[str, Any]:
    bookmarks = load_jsonl(root / "bookmarks" / "bookmarks_keywords.jsonl")
    notes = load_jsonl(root / "notes" / "AI行业扫描_keywords.jsonl")

    known_urls: set[str] = set()
    known_titles: set[str] = set()
    bookmark_domains: Counter[str] = Counter()
    note_domains: Counter[str] = Counter()
    tag_counts: Counter[str] = Counter()

    for row in bookmarks:
        if row.get("url"):
            known_urls.add(normalize_url(row["url"]))
        title = (row.get("title") or "").strip().lower()
        if title:
            known_titles.add(title)
        domain = row.get("domain")
        if domain and row.get("status") == "active" and row.get("quality_tier") in {"A", "B"}:
            bookmark_domains[domain.lower()] += 1
            for tag in row.get("tags") or []:
                tag_counts[str(tag)] += 1

    for row in notes:
        title = (row.get("title") or "").strip().lower()
        if title:
            known_titles.add(title)
        for url in urls_from_text(row.get("url") or ""):
            known_urls.add(normalize_url(url))
            host = host_from_url(url)
            if host:
                note_domains[host] += 1

    return {
        "bookmarks_count": len(bookmarks),
        "notes_count": len(notes),
        "known_urls": known_urls,
        "known_titles": known_titles,
        "bookmark_domains": bookmark_domains,
        "note_domains": note_domains,
        "tag_counts": tag_counts,
    }


def score_item(
    source: dict[str, Any],
    item: dict[str, Any],
    internal: dict[str, Any],
    now: datetime,
    days: int,
) -> FeedItem | None:
    title = item["title"]
    summary = item.get("summary") or ""
    url = item["url"]
    if not has_core_ai_signal(title, summary):
        return None
    published_dt = parse_datetime(item.get("published_raw"))
    if published_dt and published_dt < now - timedelta(days=days):
        return None

    topics, hit_count = theme_hits(title, summary)
    noise_hits = sum(1 for term in NOISE_TERMS if term in f"{title} {summary}".lower())
    host = host_from_url(url) or host_from_url(source.get("homepage", "")) or ""
    domain_weight = math.log1p(
        internal["bookmark_domains"].get(host, 0) + internal["note_domains"].get(host, 0)
    ) * 0.45

    trust_weight = {
        "primary": 2.4,
        "research": 1.9,
        "expert_blog": 1.7,
        "curated_newsletter": 1.5,
        "signal_source": 1.0,
    }.get(source.get("trust_tier"), 1.0)

    recency_weight = 0.0
    if published_dt:
        age_days = max((now - published_dt).days, 0)
        if age_days <= 3:
            recency_weight = 1.8
        elif age_days <= 7:
            recency_weight = 1.4
        elif age_days <= 14:
            recency_weight = 0.9
        elif age_days <= 30:
            recency_weight = 0.4

    known = normalize_url(url) in internal["known_urls"] or title.strip().lower() in internal["known_titles"]
    score = (
        float(source.get("priority", 1.0))
        + trust_weight
        + min(hit_count * 0.45, 3.2)
        + domain_weight
        + recency_weight
        - noise_hits * 1.3
    )
    if known:
        score -= 0.4
    if not topics:
        score -= 1.6
    if score < 2.5:
        return None

    why_bits = []
    if topics:
        why_bits.append("命中主题：" + "、".join(topics[:3]))
    if source.get("trust_tier") in {"primary", "research"}:
        why_bits.append("一手或研究型来源")
    if domain_weight > 0:
        why_bits.append("该域名已在本地高质量库中多次出现")
    if recency_weight >= 1.4:
        why_bits.append("近期更新")
    if known:
        why_bits.append("本地库已有相关线索，可作为复核/延展")

    return FeedItem(
        source_id=source["id"],
        source_name=source["name"],
        source_kind=source["kind"],
        source_trust_tier=source.get("trust_tier", ""),
        title=title,
        url=url,
        published=published_dt.isoformat() if published_dt else None,
        summary=textwrap.shorten(summary, width=260, placeholder="..."),
        topics=topics,
        score=round(score, 2),
        why="；".join(why_bits) if why_bits else "与本地 AI 行业主题存在弱相关，建议人工复核",
        known_in_library=known,
    )


def render_markdown(
    items: list[FeedItem],
    run_meta: dict[str, Any],
    internal: dict[str, Any],
    skipped_sources: list[dict[str, str]],
    output_json_name: str,
) -> str:
    lines: list[str] = []
    lines.append("# AI 行业资讯聚合样例")
    lines.append("")
    lines.append(f"- 生成时间：{run_meta['generated_at']}")
    lines.append(f"- 时间窗口：最近 {run_meta['days']} 天")
    lines.append(f"- 自动源：尝试 {run_meta['rss_sources_attempted']} 个，成功 {run_meta['rss_sources_ok']} 个，失败 {run_meta['rss_sources_failed']} 个")
    lines.append(f"- 候选：抓到 {run_meta['raw_items']} 条，进入推荐 {len(items)} 条")
    lines.append(f"- 机器可读结果：`{output_json_name}`")
    lines.append("")

    lines.append("## 本地来源地图")
    lines.append("")
    lines.append(f"- bookmarks：{internal['bookmarks_count']} 条；notes：{internal['notes_count']} 条。")
    lines.append("- bookmarks 高频 A/B 域名：")
    for domain, count in internal["bookmark_domains"].most_common(12):
        lines.append(f"  - `{domain}`：{count}")
    lines.append("- bookmarks 高频标签：")
    for tag, count in internal["tag_counts"].most_common(14):
        lines.append(f"  - `{tag}`：{count}")
    lines.append("")

    lines.append("## 推荐候选")
    lines.append("")
    if not items:
        lines.append("本次没有达到阈值的自动候选。需要扩大源或放宽筛选。")
    for idx, item in enumerate(items, 1):
        date = item.published[:10] if item.published else "date n/a"
        known = "；本地已有线索" if item.known_in_library else ""
        lines.append(f"### {idx}. {item.title}")
        lines.append("")
        lines.append(f"- 来源：{item.source_name} / {item.source_trust_tier}")
        lines.append(f"- 日期：{date}")
        lines.append(f"- 分数：{item.score}{known}")
        lines.append(f"- 主题：{', '.join(item.topics) if item.topics else '待人工归类'}")
        lines.append(f"- 链接：{item.url}")
        lines.append(f"- 为什么值得看：{item.why}")
        if item.summary:
            lines.append(f"- 摘要：{item.summary}")
        lines.append("")

    lines.append("## 未自动抓取但应保留的源")
    lines.append("")
    for src in skipped_sources:
        lines.append(f"- {src['name']}：{src['reason']}")
    lines.append("")

    lines.append("## X/Twitter 处理结论")
    lines.append("")
    lines.append("- 当前没有 `X_BEARER_TOKEN`，本次未抓 X 时间线。")
    lines.append("- 第一版建议不要用非官方方式硬扒 X；把 X 当成信号源和人工 URL 输入源。")
    lines.append("- 如果以后开 X API，优先抓自有 lists/bookmarks 或指定账号，成本按资源返回量控制，并设置每周预算。")
    lines.append("")

    lines.append("## 质量判断")
    lines.append("")
    lines.append("- 这一版已经能抓到公开 RSS/Atom/arXiv/官方博客，并用本地 bookmarks/notes 的域名与主题权重排序。")
    lines.append("- 还不是最终 skill：缺少 Anthropic 等无 RSS 站点的 HTML collector，缺少播客转录，缺少人工审稿后的正负样本回灌。")
    lines.append("- 但它已经可以作为 OpenClaw/Codex 这类 agent 的周更情报入口雏形。")
    lines.append("")
    return "\n".join(lines)


def select_diverse_items(scored: list[FeedItem], limit: int) -> list[FeedItem]:
    """Select a source-balanced list so arXiv or one official feed does not flood the digest."""
    sorted_items = sorted(scored, key=lambda i: i.score, reverse=True)
    selected: list[FeedItem] = []
    seen: set[str] = set()
    bucket_counts: Counter[str] = Counter()
    source_counts: Counter[str] = Counter()

    bucket_limits = {
        "arxiv": min(5, max(2, limit // 3)),
        "openai_news": 4,
        "github_blog": 3,
        "substack_or_newsletter": 7,
        "expert_blog": 5,
    }

    def bucket_for(item: FeedItem) -> str:
        if item.source_id.startswith("arxiv_"):
            return "arxiv"
        if item.source_id == "openai_news":
            return "openai_news"
        if item.source_id == "github_blog":
            return "github_blog"
        if item.source_trust_tier == "curated_newsletter":
            return "substack_or_newsletter"
        if item.source_trust_tier == "expert_blog":
            return "expert_blog"
        return item.source_id

    for item in sorted_items:
        key = normalize_url(item.url) or item.title.lower()
        if key in seen:
            continue
        bucket = bucket_for(item)
        if bucket_counts[bucket] >= bucket_limits.get(bucket, 4):
            continue
        if source_counts[item.source_id] >= 4:
            continue
        selected.append(item)
        seen.add(key)
        bucket_counts[bucket] += 1
        source_counts[item.source_id] += 1
        if len(selected) >= limit:
            break

    if len(selected) < limit:
        for item in sorted_items:
            key = normalize_url(item.url) or item.title.lower()
            if key in seen:
                continue
            selected.append(item)
            seen.add(key)
            if len(selected) >= limit:
                break
    return selected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--days", type=int, default=30)
    parser.add_argument("--limit", type=int, default=18)
    parser.add_argument("--catalog", type=Path, default=skill_root() / "references" / "source_catalog.json")
    parser.add_argument("--output-dir", type=Path, default=skill_root() / "outputs")
    args = parser.parse_args()

    root = repo_root()
    internal = build_internal_memory(root)
    catalog = json.loads(args.catalog.read_text(encoding="utf-8"))
    now = datetime.now(timezone.utc)

    raw_items = 0
    scored: list[FeedItem] = []
    skipped_sources: list[dict[str, str]] = []
    source_status: list[dict[str, Any]] = []

    for source in catalog.get("sources", []):
        kind = source.get("kind")
        if kind not in {"rss", "atom"}:
            skipped_sources.append({
                "name": source.get("name", source.get("id", "unknown")),
                "reason": source.get("skip_reason", f"{kind} source is not handled by the RSS collector."),
            })
            source_status.append({"id": source.get("id"), "status": "skipped", "kind": kind})
            continue
        try:
            xml_bytes = fetch(source["feed_url"])
            parsed = parse_feed(xml_bytes, source)
            raw_items += len(parsed)
            kept = 0
            for item in parsed:
                scored_item = score_item(source, item, internal, now, args.days)
                if scored_item:
                    scored.append(scored_item)
                    kept += 1
            source_status.append({
                "id": source["id"],
                "status": "ok",
                "items": len(parsed),
                "kept": kept,
            })
        except (urllib.error.URLError, ET.ParseError, TimeoutError, socket.timeout, OSError, KeyError) as exc:
            source_status.append({
                "id": source.get("id"),
                "status": "failed",
                "error": str(exc),
            })

    deduped: dict[str, FeedItem] = {}
    for item in sorted(scored, key=lambda i: i.score, reverse=True):
        key = normalize_url(item.url) or item.title.lower()
        if key not in deduped:
            deduped[key] = item
    items = select_diverse_items(list(deduped.values()), args.limit)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    output_json = args.output_dir / "latest_digest.json"
    output_md = args.output_dir / "latest_digest.md"

    rss_attempted = [s for s in source_status if s.get("status") != "skipped"]
    run_meta = {
        "generated_at": now.isoformat(),
        "days": args.days,
        "raw_items": raw_items,
        "rss_sources_attempted": len(rss_attempted),
        "rss_sources_ok": sum(1 for s in rss_attempted if s.get("status") == "ok"),
        "rss_sources_failed": sum(1 for s in rss_attempted if s.get("status") == "failed"),
        "source_status": source_status,
    }

    output = {
        "run_meta": run_meta,
        "source_map": {
            "bookmarks_count": internal["bookmarks_count"],
            "notes_count": internal["notes_count"],
            "top_bookmark_domains": internal["bookmark_domains"].most_common(30),
            "top_bookmark_tags": internal["tag_counts"].most_common(30),
            "top_note_domains": internal["note_domains"].most_common(30),
        },
        "items": [asdict(item) for item in items],
        "skipped_sources": skipped_sources,
    }
    output_json.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    output_md.write_text(
        render_markdown(items, run_meta, internal, skipped_sources, output_json.name),
        encoding="utf-8",
    )

    print(f"Wrote {output_md}")
    print(f"Wrote {output_json}")
    print(f"Fetched {raw_items} raw items; recommended {len(items)} items")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

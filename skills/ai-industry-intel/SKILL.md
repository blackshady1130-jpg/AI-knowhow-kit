---
name: ai-industry-intel
description: Discover, collect, rank, and summarize high-signal AI industry information from the AI_knowhow_kit notes/bookmarks corpus plus public feeds. Use for weekly AI intelligence digests, source discovery, source quality audits, and agent-facing recommendation workflows.
---

# AI Industry Intel

## Use When

- The task is to recommend high-quality AI industry content on a weekly or recurring basis.
- The agent needs to use `notes/AI行业扫描_*` and `bookmarks/bookmarks_*` as source memory before widening to public feeds.
- The user asks which AI accounts, blogs, podcasts, newsletters, papers, or official sources should become durable information sources.
- The task needs a practical source catalog rather than a one-off web search.

## Source Order

1. Read `AI_SCAN_RETRIEVAL.md` and `BOOKMARKS_RETRIEVAL.md` for the project retrieval contract.
2. Use `notes/AI行业扫描_keywords.jsonl` for high-signal judgments and topic anchoring.
3. Use `bookmarks/bookmarks_keywords.jsonl` for broader source discovery, high-frequency domains, and A/B quality tiers.
4. Use `references/source_catalog.json` for public sources that can be fetched automatically.
5. Use external web only for current verification, source discovery, or feeds not covered by the local catalog.

## Weekly Digest Workflow

Run:

```bash
python skills/ai-industry-intel/scripts/collect_weekly.py --days 30 --limit 18
```

The script writes:

- `skills/ai-industry-intel/outputs/latest_digest.md`
- `skills/ai-industry-intel/outputs/latest_digest.json`

## Ranking Rules

Prefer items that satisfy several of these conditions:

- Primary source from a model lab, infra/product team, research group, official engineering blog, or original author.
- Strong match to the repo's durable themes: agent/harness, eval/benchmark, model training, context/memory/RAG, AI coding, product/SaaS/business, safety/governance.
- Explains a mechanism, not just a product launch.
- Changes a prior judgment or adds evidence to an existing topic.
- Comes from a domain that already appears frequently in high-quality bookmarks/notes.
- Has a stable URL and public retrieval path.

Demote items that are only tool-listicles, pure funding noise, generic prompt tips, low-context reposts, inaccessible private documents, or WeChat/X links without enough public context.

## X/Twitter Handling

Without an X API bearer token, do not scrape X timelines as the default workflow. Use X as:

- a manual source list of high-signal accounts,
- a source of bookmarked URLs already captured in the local corpus,
- a pointer to the author's blog, paper, newsletter, GitHub repo, podcast, or official post.

If `X_BEARER_TOKEN` is available, an implementation may add an official API collector, but must respect current X API pricing, display, caching, redistribution, deletion, and commercial-use rules.

## Output Shape

A useful digest should contain:

1. Source coverage: what was fetched, skipped, or manual-only.
2. Local source map: high-frequency domains and topic tags from notes/bookmarks.
3. Top recommendations: title, source, URL, date, score, topic fit, why it matters.
4. Boundary notes: inaccessible sources, X/API limits, WeChat/manual-only material.
5. Next actions: which sources to add, remove, or manually review.

## Failure Checks

- If the digest only lists links without explaining why they matter, it fails.
- If it ignores `bookmarks`, it fails.
- If it pretends WeChat or X can be freely and reliably scraped without credentials or policy concerns, it fails.
- If it does not distinguish automatic feeds from manual-only sources, it fails.

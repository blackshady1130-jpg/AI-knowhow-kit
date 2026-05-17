Title: llm-wiki

URL Source: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

Markdown Content:
# llm-wiki · GitHub

[Skip to content](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#start-of-content)

[](https://gist.github.com/)

 Search Gists  Search Gists

[All gists](https://gist.github.com/discover)[Back to GitHub](https://github.com/)[Sign in](https://gist.github.com/auth/github?return_to=https%3A%2F%2Fgist.github.com%2Fkarpathy%2F442a6bf555914893e9891c11519de94f)[Sign up](https://gist.github.com/join?return_to=https%3A%2F%2Fgist.github.com%2Fkarpathy%2F442a6bf555914893e9891c11519de94f&source=header-gist)

[](https://gist.github.com/)

[Sign in](https://gist.github.com/auth/github?return_to=https%3A%2F%2Fgist.github.com%2Fkarpathy%2F442a6bf555914893e9891c11519de94f)[Sign up](https://gist.github.com/join?return_to=https%3A%2F%2Fgist.github.com%2Fkarpathy%2F442a6bf555914893e9891c11519de94f&source=header-gist)

You signed in with another tab or window. [Reload](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) to refresh your session.You signed out in another tab or window. [Reload](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) to refresh your session.You switched accounts on another tab or window. [Reload](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) to refresh your session.Dismiss alert

{{ message }}

Instantly share code, notes, and snippets.

[![Image 1: @karpathy](https://avatars.githubusercontent.com/u/241138?s=64&v=4)](https://gist.github.com/karpathy)

# [karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**

 Created April 4, 2026 16:25

Show Gist options

*   [Download ZIP](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f/archive/ac46de1ad27f92b28ac95459c782c07f6b8c964a.zip)

*   [Star 5,000+(5,000+)](https://gist.github.com/login?return_to=https%3A%2F%2Fgist.github.com%2Fkarpathy%2F442a6bf555914893e9891c11519de94f)You must be signed in to star a gist
*   [Fork 5,000+(5,000+)](https://gist.github.com/login?return_to=https%3A%2F%2Fgist.github.com%2Fkarpathy%2F442a6bf555914893e9891c11519de94f)You must be signed in to fork a gist

*   
 Embed # Select an option    

    *    Embed Embed this gist in your website.
    *    Share Copy sharable link for this gist.
    *    Clone via HTTPS Clone using the web URL.

## No results found

[Learn more about clone URLs](https://docs.github.com/articles/which-remote-url-should-i-use)

 Clone this repository at &lt;script src=&quot;https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f.js&quot;&gt;&lt;/script&gt;  

*   Save karpathy/442a6bf555914893e9891c11519de94f to your computer and use it in GitHub Desktop.

[Code](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)[Revisions 1](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f/revisions)[Stars 5,000+](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f/stargazers)[Forks 5,000+](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f/forks)

 Embed 

# Select an option

*    Embed Embed this gist in your website.
*    Share Copy sharable link for this gist.
*    Clone via HTTPS Clone using the web URL.

## No results found

[Learn more about clone URLs](https://docs.github.com/articles/which-remote-url-should-i-use)

 Clone this repository at &lt;script src=&quot;https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f.js&quot;&gt;&lt;/script&gt;  

Save karpathy/442a6bf555914893e9891c11519de94f to your computer and use it in GitHub Desktop.

[Download ZIP](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f/archive/ac46de1ad27f92b28ac95459c782c07f6b8c964a.zip)

 llm-wiki 

[Raw](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f/raw/ac46de1ad27f92b28ac95459c782c07f6b8c964a/llm-wiki.md)

[**llm-wiki.md**](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#file-llm-wiki-md)

# LLM Wiki

[](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#llm-wiki)

A pattern for building personal knowledge bases using LLMs.

This is an idea file, it is designed to be copy pasted to your own LLM Agent (e.g. OpenAI Codex, Claude Code, OpenCode / Pi, or etc.). Its goal is to communicate the high level idea, but your agent will build out the specifics in collaboration with you.

## The core idea

[](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#the-core-idea)

Most people's experience with LLMs and documents looks like RAG: you upload a collection of files, the LLM retrieves relevant chunks at query time, and generates an answer. This works, but the LLM is rediscovering knowledge from scratch on every question. There's no accumulation. Ask a subtle question that requires synthesizing five documents, and the LLM has to find and piece together the relevant fragments every time. Nothing is built up. NotebookLM, ChatGPT file uploads, and most RAG systems work this way.

The idea here is different. Instead of just retrieving from raw documents at query time, the LLM **incrementally builds and maintains a persistent wiki** — a structured, interlinked collection of markdown files that sits between you and the raw sources. When you add a new source, the LLM doesn't just index it for later retrieval. It reads it, extracts the key information, and integrates it into the existing wiki — updating entity pages, revising topic summaries, noting where new data contradicts old claims, strengthening or challenging the evolving synthesis. The knowledge is compiled once and then _kept current_, not re-derived on every query.

This is the key difference: **the wiki is a persistent, compounding artifact.** The cross-references are already there. The contradictions have already been flagged. The synthesis already reflects everything you've read. The wiki keeps getting richer with every source you add and every question you ask.

You never (or rarely) write the wiki yourself — the LLM writes and maintains all of it. You're in charge of sourcing, exploration, and asking the right questions. The LLM does all the grunt work — the summarizing, cross-referencing, filing, and bookkeeping that makes a knowledge base actually useful over time. In practice, I have the LLM agent open on one side and Obsidian open on the other. The LLM makes edits based on our conversation, and I browse the results in real time — following links, checking the graph view, reading the updated pages. Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase.

This can apply to a lot of different contexts. A few examples:

*   **Personal**: tracking your own goals, health, psychology, self-improvement — filing journal entries, articles, podcast notes, and building up a structured picture of yourself over time.
*   **Research**: going deep on a topic over weeks or months — reading papers, articles, reports, and incrementally building a comprehensive wiki with an evolving thesis.
*   **Reading a book**: filing each chapter as you go, building out pages for characters, themes, plot threads, and how they connect. By the end you have a rich companion wiki. Think of fan wikis like [Tolkien Gateway](https://tolkiengateway.net/wiki/Main_Page) — thousands of interlinked pages covering characters, places, events, languages, built by a community of volunteers over years. You could build something like that personally as you read, with the LLM doing all the cross-referencing and maintenance.
*   **Business/team**: an internal wiki maintained by LLMs, fed by Slack threads, meeting transcripts, project documents, customer calls. Possibly with humans in the loop reviewing updates. The wiki stays current because the LLM does the maintenance that no one on the team wants to do.
*   **Competitive analysis, due diligence, trip planning, course notes, hobby deep-dives** — anything where you're accumulating knowledge over time and want it organized rather than scattered.

## Architecture

[](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#architecture)

There are three layers:

**Raw sources** — your curated collection of source documents. Articles, papers, images, data files. These are immutable — the LLM reads from them but never modifies them. This is your source of truth.

**The wiki** — a directory of LLM-generated markdown files. Summaries, entity pages, concept pages, comparisons, an overview, a synthesis. The LLM owns this layer entirely. It creates pages, updates them when new sources arrive, maintains cross-references, and keeps everything consistent. You read it; the LLM writes it.

**The schema** — a document (e.g. CLAUDE.md for Claude Code or AGENTS.md for Codex) that tells the LLM how the wiki is structured, what the conventions are, and what workflows to follow when ingesting sources, answering questions, or maintaining the wiki. This is the key configuration file — it's what makes the LLM a disciplined wiki maintainer rather than a generic chatbot. You and the LLM co-evolve this over time as you figure out what works for your domain.

## Operations

[](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#operations)

**Ingest.** You drop a new source into the raw collection and tell the LLM to process it. An example flow: the LLM reads the source, discusses key takeaways with you, writes a summary page in the wiki, updates the index, updates relevant entity and concept pages across the wiki, and appends an entry to the log. A single source might touch 10-15 wiki pages. Personally I prefer to ingest sources one at a time and stay involved — I read the summaries, check the updates, and guide the LLM on what to emphasize. But you could also batch-ingest many sources at once with less supervision. It's up to you to develop the workflow that fits your style and document it in the schema for future sessions.

**Query.** You ask questions against the wiki. The LLM searches for relevant pages, reads them, and synthesizes an answer with citations. Answers can take different forms depending on the question — a markdown page, a comparison table, a slide deck (Marp), a chart (matplotlib), a canvas. The important insight: **good answers can be filed back into the wiki as new pages.** A comparison you asked for, an analysis, a connection you discovered — these are valuable and shouldn't disappear into chat history. This way your explorations compound in the knowledge base just like ingested sources do.

**Lint.** Periodically, ask the LLM to health-check the wiki. Look for: contradictions between pages, stale claims that newer sources have superseded, orphan pages with no inbound links, important concepts mentioned but lacking their own page, missing cross-references, data gaps that could be filled with a web search. The LLM is good at suggesting new questions to investigate and new sources to look for. This keeps the wiki healthy as it grows.

## Indexing and logging

[](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#indexing-and-logging)

Two special files help the LLM (and you) navigate the wiki as it grows. They serve different purposes:

**index.md** is content-oriented. It's a catalog of everything in the wiki — each page listed with a link, a one-line summary, and optionally metadata like date or source count. Organized by category (entities, concepts, sources, etc.). The LLM updates it on every ingest. When answering a query, the LLM reads the index first to find relevant pages, then drills into them. This works surprisingly well at moderate scale (~100 sources, ~hundreds of pages) and avoids the need for embedding-based RAG infrastructure.

**log.md** is chronological. It's an append-only record of what happened and when — ingests, queries, lint passes. A useful tip: if each entry starts with a consistent prefix (e.g. `## [2026-04-02] ingest | Article Title`), the log becomes parseable with simple unix tools — `grep "^## \[" log.md | tail -5` gives you the last 5 entries. The log gives you a timeline of the wiki's evolution and helps the LLM understand what's been done recently.

## Optional: CLI tools

[](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#optional-cli-tools)

At some point you may want to build small tools that help the LLM operate on the wiki more efficiently. A search engine over the wiki pages is the most obvious one — at small scale the index file is enough, but as the wiki grows you want proper search. [qmd](https://github.com/tobi/qmd) is a good option: it's a local search engine for markdown files with hybrid BM25/vector search and LLM re-ranking, all on-device. It has both a CLI (so the LLM can shell out to it) and an MCP server (so the LLM can use it as a native tool). You could also build something simpler yourself — the LLM can help you vibe-code a naive search script as the need arises.

## Tips and tricks

[](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#tips-and-tricks)

*   **Obsidian Web Clipper** is a browser extension that converts web articles to markdown. Very useful for quickly getting sources into your raw collection.
*   **Download images locally.** In Obsidian Settings → Files and links, set "Attachment folder path" to a fixed directory (e.g. `raw/assets/`). Then in Settings → Hotkeys, search for "Download" to find "Download attachments for current file" and bind it to a hotkey (e.g. Ctrl+Shift+D). After clipping an article, hit the hotkey and all images get downloaded to local disk. This is optional but useful — it lets the LLM view and reference images directly instead of relying on URLs that may break. Note that LLMs can't natively read markdown with inline images in one pass — the workaround is to have the LLM read the text first, then view some or all of the referenced images separately to gain additional context. It's a bit clunky but works well enough.
*   **Obsidian's graph view** is the best way to see the shape of your wiki — what's connected to what, which pages are hubs, which are orphans.
*   **Marp** is a markdown-based slide deck format. Obsidian has a plugin for it. Useful for generating presentations directly from wiki content.
*   **Dataview** is an Obsidian plugin that runs queries over page frontmatter. If your LLM adds YAML frontmatter to wiki pages (tags, dates, source counts), Dataview can generate dynamic tables and lists.
*   The wiki is just a git repo of markdown files. You get version history, branching, and collaboration for free.

## Why this works

[](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#why-this-works)

The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping. Updating cross-references, keeping summaries current, noting when new data contradicts old claims, maintaining consistency across dozens of pages. Humans abandon wikis because the maintenance burden grows faster than the value. LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass. The wiki stays maintained because the cost of maintenance is near zero.

The human's job is to curate sources, direct the analysis, ask good questions, and think about what it all means. The LLM's job is everything else.

The idea is related in spirit to Vannevar Bush's Memex (1945) — a personal, curated knowledge store with associative trails between documents. Bush's vision was closer to this than to what the web became: private, actively curated, with the connections between documents as valuable as the documents themselves. The part he couldn't solve was who does the maintenance. The LLM handles that.

## Note

[](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#note)

This document is intentionally abstract. It describes the idea, not a specific implementation. The exact directory structure, the schema conventions, the page formats, the tooling — all of that will depend on your domain, your preferences, and your LLM of choice. Everything mentioned above is optional and modular — pick what's useful, ignore what isn't. For example: your sources might be text-only, so you don't need image handling at all. Your wiki might be small enough that the index file is all you need, no search engine required. You might not care about slide decks and just want markdown pages. You might want a completely different set of output formats. The right way to use this is to share it with your LLM agent and work together to instantiate a version that fits your needs. The document's only job is to communicate the pattern. Your LLM can figure out the rest.

[](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)

Load earlier comments...

[![Image 2: @tuirk](https://avatars.githubusercontent.com/u/65666288?s=80&v=4)](https://gist.github.com/tuirk)

 Copy link  Copy Markdown 

### **[tuirk](https://gist.github.com/tuirk)** commented [May 11, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6144457#gistcomment-6144457)

## dropped v0.1 of Kompl in this thread a while back— just shipped v0.2, so adding the update.

Repo: [https://github.com/tuirk/Kompl](https://github.com/tuirk/Kompl)

short version for new readers: Kompl runs the pattern from this gist with synthesis at ingest time, not query time. you save a thing (a link, a PDF, a YouTube video, a bookmark export, pasted text) and Kompl reads it as it arrives: pulls out the people, ideas, and arguments inside, writes them into wiki pages that link to each other, and updates existing pages when new sources contribute. save your tenth source on a topic and the page already reflects the pattern across all ten without you having to ask. the wiki itself is the cached synthesis. self-hosted via docker, bring-your-own API keys, MCP server included so an agent can query the compiled wiki.

[![Image 3: Karpathy's LLM wiki vs Kompl](https://private-user-images.githubusercontent.com/65666288/586724180-f1f22664-66cb-4d23-8c6b-5d7194b21fa1.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Nzg5ODcyNjQsIm5iZiI6MTc3ODk4Njk2NCwicGF0aCI6Ii82NTY2NjI4OC81ODY3MjQxODAtZjFmMjI2NjQtNjZjYi00ZDIzLThjNmItNWQ3MTk0YjIxZmExLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA1MTclMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNTE3VDAzMDI0NFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWU5MjRjNjI2MDUyYWUzNDMyOWVlNDU2MDg4ODZjNzZkMTMzYmQ1NDUzMjdjODQ2MGE4ZGEwZWQ4ZWIyMDliMWMmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.pSrD8Ucqv9wHsHUxUFPs_REGuHmVRe8EOr4byNubdjc)](https://private-user-images.githubusercontent.com/65666288/586724180-f1f22664-66cb-4d23-8c6b-5d7194b21fa1.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Nzg5ODcyNjQsIm5iZiI6MTc3ODk4Njk2NCwicGF0aCI6Ii82NTY2NjI4OC81ODY3MjQxODAtZjFmMjI2NjQtNjZjYi00ZDIzLThjNmItNWQ3MTk0YjIxZmExLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA1MTclMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNTE3VDAzMDI0NFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWU5MjRjNjI2MDUyYWUzNDMyOWVlNDU2MDg4ODZjNzZkMTMzYmQ1NDUzMjdjODQ2MGE4ZGEwZWQ4ZWIyMDliMWMmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.pSrD8Ucqv9wHsHUxUFPs_REGuHmVRe8EOr4byNubdjc)

### what's new in v0.2

*   multi-provider. DeepSeek V4 Pro added as a second compile backend, selectable per session. Gemini 2.5 has a structured-output truncation pathology on dense inputs (~50K+ char academic PDFs); DeepSeek handles up to ~200K cleanly. provider abstraction layer routes gemini-* and deepseek-* IDs through one LLMProvider interface. per-session model lock stamps the choice at session start so mid-flight settings changes don't hot-swap.
*   live progress UI. per-step X/Y counters during compile (extract, draft, ingest, match, crossref, commit), expand-to-reveal item drill-down, time-estimate shown as a range instead of a single conservative value.
*   stranded-source recovery. a source whose extract fails mid-session is no longer unrecoverable. orchestrator re-plans on retry; commit-activation gate only marks compile_status='active' for sources with an extractions row, so retry routes can re-attempt the source.
*   new connectors. paste-text (raw text → source, no URL or file needed). YouTube direct-ingest via the official transcript API + Data API videos.list — replaces the prior silent fallback to scraping watch-page chrome on transcript-less videos. covers watch / youtu.be / shorts / embed / m. / music. URL forms.
*   one-line installers. install.sh for macOS/Linux/WSL, install.ps1 for Windows. pre-flights Docker, Node 24, disk, RAM before handing off to the API-key prompts.
*   security pass. SSRF hardening on /metadata/peek (DNS-resolved IP pinning, cloud-metadata blocklist, scheme allowlist, manual redirect revalidation), path-traversal containment across nlp-service and Next.js, YAML frontmatter escaping with C0/C1/U+2028/U+2029/BOM stripping, log-arg scrubbing, Scorecard-flagged deps pinned, nlp-service bound to 127.0.0.1.

### **What goes in Kompl:**

*   URLs (web pages, articles, YouTube videos, GitHub repos, anything Firecrawl can reach)
*   Files (PDF, DOCX, PPTX, XLSX, TXT, MD, HTML, CSV, images, audio)
*   Browser bookmark, Twitter/X bookmark, Apple Notes/Upnote exports

Here's what that looks like after a few sessions; new overviews, comparisons, entity pages, contradictions surfacing, fresh cross-links between everything.

[![Image 4: Kompl demo](https://raw.githubusercontent.com/tuirk/Kompl/main/docs/assets/kompl-demo.gif)](https://raw.githubusercontent.com/tuirk/Kompl/main/docs/assets/kompl-demo.gif)[![Image 5: Kompl demo](https://raw.githubusercontent.com/tuirk/Kompl/main/docs/assets/kompl-demo.gif)](https://raw.githubusercontent.com/tuirk/Kompl/main/docs/assets/kompl-demo.gif)[](https://raw.githubusercontent.com/tuirk/Kompl/main/docs/assets/kompl-demo.gif)

### **A few specific bets we made on top of the pattern:**

*   **NLP before LLM.** spaCy NER + a 4-way keyphrase fanout (RAKE, KeyBERT, TextRank, YAKE) runs first; Gemini gets pre-resolved entities, not raw markdown. Cheaper and less noisy.
*   **Batch ingest, async compile.** Drop sources, close the tab, come back to a wiki. Server-side pipeline with rate limits, a customizable daily USD cap, and other settings (entity promotion threshold, draft length floor, model tier per session, schema-driven tone — more in the repo).
*   **Three layers of entity resolution** (fuzzy, embedding, LLM disambiguation) collapse variations like "GPT 4", "GPT-4", and "gpt4" into one canonical.
*   **Comparison pages** surface when sources disagree across three or more sources.
*   **Wikilinks** get injected deterministically by regex, not by an LLM.
*   **MCP-native.** Stdio MCP server (`search_wiki`, `read_page`, `list_pages`, `wiki_stats`) so Claude Code, Claude Desktop, Cursor can use the wiki as a knowledge source out of the box. That's our favorite feature.
*   **For UI** the gist mentions Obsidian as the IDE. Kompl runs in its own UI but ships an Obsidian-compatible export, so you're not locked in either way.
*   **Local Docker, single-tenant**, BYO Gemini + Firecrawl keys. Open-sourced with Apache-2.0.

40-second demo is below, click to watch on Youtube and full details on GitHub: [https://github.com/tuirk/Kompl](https://github.com/tuirk/Kompl)

[![Image 6: Watch the demo](https://camo.githubusercontent.com/f3b2ec75f6bef805a8e0f8b3e1bec8f8867619d22d5a99a6426423da159bcc0d/68747470733a2f2f696d672e796f75747562652e636f6d2f76692f4f6a4c52706e70654659592f6d617872657364656661756c742e6a7067)](https://youtu.be/OjLRpnpeFYY)

Fork it, run it on your own sources, let me know how it goes 🥸

Repo: [https://github.com/tuirk/Kompl](https://github.com/tuirk/Kompl)

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 7: @dfalci](https://avatars.githubusercontent.com/u/2759072?s=80&v=4)](https://gist.github.com/dfalci)

 Copy link  Copy Markdown 

### **[dfalci](https://gist.github.com/dfalci)** commented [May 11, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6144488#gistcomment-6144488)

Thanks for sharing this, [@karpathy](https://github.com/karpathy) — really insightful.

I built a Rust-based MCP server inspired by this idea, focused on a local Markdown wiki + full-text search as persistent architectural memory for software projects.

It is already usable, and I’m planning to improve it further with better indexing, backlinks, linting, and curated knowledge workflows:

[https://github.com/dfalci/mcp-advwiki](https://github.com/dfalci/mcp-advwiki)

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 8: @rohitg00](https://avatars.githubusercontent.com/u/48523873?s=80&v=4)](https://gist.github.com/rohitg00)

 Copy link  Copy Markdown 

### **[rohitg00](https://gist.github.com/rohitg00)** commented [May 11, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6144497#gistcomment-6144497)

AKBP turns the LLM Wiki pattern into a protocol surface for agent runtimes. It is a local-first, file-backed knowledge base that agents can read, write, verify, export, and carry across tools.

The idea comes from the same insight behind [LLM Wiki v2](https://gist.github.com/rohitg00/2067ab416f7bbe447c1977edaaa681e2): stop re-deriving, start compiling. AKBP adds the machinery a repo needs when that pattern becomes operational: typed claims, source hashes, lifecycle relations, review-gated writes, JSONL tool calls, schemas, and conformance tests.

This repository contains the reference implementation:

a Python CLI for creating and maintaining AKBP knowledge bases

 a newline-delimited JSON tool server for agent integrations

 JSON schemas for requests, responses, records, and method parameters

 adapter templates for coding-agent runtimes

 conformance checks, benchmark fixtures, import/export checks, and CI validation

[https://github.com/rohitg00/akbp](https://github.com/rohitg00/akbp)

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 9: @good-idea](https://avatars.githubusercontent.com/u/11514928?s=80&v=4)](https://gist.github.com/good-idea)

 Copy link  Copy Markdown 

### **[good-idea](https://gist.github.com/good-idea)** commented [May 11, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6144590#gistcomment-6144590)

I never imagined a gist comment thread would read like a feed of advertisements

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 10: @FBoschman](https://avatars.githubusercontent.com/u/148960927?s=80&v=4)](https://gist.github.com/FBoschman)

 Copy link  Copy Markdown 

### **[FBoschman](https://gist.github.com/FBoschman)** commented [May 11, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6144680#gistcomment-6144680)

For any researchers out there doing PhD work, I have made it so it fits my work as a researcher. You can find the repo here:

[https://github.com/FBoschman/claude-wiki-research-skills](https://github.com/FBoschman/claude-wiki-research-skills)

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 11: @boostedcore](https://avatars.githubusercontent.com/u/137294168?s=80&v=4)](https://gist.github.com/boostedcore)

 Copy link  Copy Markdown 

### **[boostedcore](https://gist.github.com/boostedcore)** commented [May 11, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6144759#gistcomment-6144759)

I wrote a short theoretical proposal on extending LLM Wiki with vector embeddings to address deduplication, granularity control and hierarchical scaling. Feedback welcome: [https://gist.github.com/boostedcore/96e74291e7832bc9317abc2b28f9b803](https://gist.github.com/boostedcore/96e74291e7832bc9317abc2b28f9b803)

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 12: @colon-md](https://avatars.githubusercontent.com/u/283063606?s=80&v=4)](https://gist.github.com/colon-md)

 Copy link  Copy Markdown 

### **[colon-md](https://gist.github.com/colon-md)** commented [May 12, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6145225#gistcomment-6145225)

I left the LLM + Wiki building and cleaned up my RAG evaluation code because I needed evaluation hardness first to actually test LLM + Wiki implementation.

Then I spent several days and weekend cleaning up the the evaluation code instead of LLM + Wiki. T__ T

But, whether it is GCP, AWS, Azure, OpenAI, the enterprise RAG services still diverge sharply on recall/precision trade-off. I was surprised to find this. Plus, all four hallucinate on every unanswerable question — 0/5. None say "I don't know," which is the failure mode wiki+RAG should be able to fix.

Here is my repo: [https://github.com/colon-md/retrievalci](https://github.com/colon-md/retrievalci)

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 13: @mav-rik](https://avatars.githubusercontent.com/u/20143759?s=80&v=4)](https://gist.github.com/mav-rik)

 Copy link  Copy Markdown 

### **[mav-rik](https://gist.github.com/mav-rik)** commented [May 12, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6145859#gistcomment-6145859)

Implemented the abstract by Karpathy [https://github.com/mav-rik/kb-cli](https://github.com/mav-rik/kb-cli)

Ships cli and skills, supports remote mode.

Testing it now on my knowledge base. Seems to be working.

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 14: @jazzonenl](https://avatars.githubusercontent.com/u/204458544?s=80&v=4)](https://gist.github.com/jazzonenl)

 Copy link  Copy Markdown 

### **[jazzonenl](https://gist.github.com/jazzonenl)** commented [May 12, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6145955#gistcomment-6145955)

**LLM Wiki — A Knowledge Management Revolution or a Transactional Dead End?**

The "LLM Wiki" concept (recently popularized following Andrej Karpathy's proposal) looks like a silver bullet for personal and corporate knowledge management. The premise is elegant: an AI transforms a chaotic mess of thousands of files and emails into a structured network of Markdown documents, complete with auto-generated meta-descriptions and cross-links.

However, beneath the initial convenience lies a fundamental architectural challenge that the industry is only beginning to whisper about. When moving from a "10-file demo" to a real-world archive — such as a CEO’s ten-year history of correspondence and documentation — we discover that instead of a simple file system, we are attempting to build a highly complex and expensive DBMS on top of neural networks.

**1. The Illusion of "Easy" Updates (Transactional Overhead)**

 Most of the current hype focuses on the Read phase. AI is excellent at summarizing and tagging. But as soon as we move to Write or update operations, the system hits a transactional nightmare:

Any single change in one document can trigger a cascade, requiring the revision of dozens of links in other files.

In a classical SQL database, this is handled by indexes in milliseconds. In an LLM Wiki, this requires a chain of model calls that consume both significant time and tokens.

**2. The Crisis of Link Integrity**

 In Karpathy’s approach, the AI assumes the role of a Database Architect. However, AI lacks the inherent concept of Referential Integrity:

If a file is deleted or renamed, hundreds of "smart links" in other .md files instantly become "dead."

To keep the database up to date, one needs a constant background process to "re-wire" the entire knowledge web. This transforms a simple folder of files into a heavy, ongoing ETL process.

**3. Temporal Degradation in Large Archives**

 For a CEO managing a decade-old archive, chronology is critical. Standard vector searches often suffer from "temporal blindness," resurfacing data from 2018 as if it were current.

Without a rigid metadata structure and "layering" (Hot Data vs. Cold Archive), the system begins to hallucinate contexts, blurring the lines between contract terms from different years.

**4. Summary: Read-Only vs. Active Storage**

 The current excitement is justified for static archives — it is arguably the best way to quickly "resurface" the history of old projects. But for a live corporate environment, the "just a folder of Markdown files" approach is a path toward losing control over your data.

**We are on the threshold of a new class of software: AI-Native Databases. These won't just be folders; they will be hybrids that combine the rigid logic of SQL (for transaction and link control) with the cognitive flexibility of an LLM (for semantic understanding). Without this fundamental layer, a "smart wiki" at scale will inevitably devolve into a digital landfill with polished headers.**

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 15: @paciox](https://avatars.githubusercontent.com/u/6546735?s=80&v=4)](https://gist.github.com/paciox)

 Copy link  Copy Markdown 

### **[paciox](https://gist.github.com/paciox)** commented [May 12, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6145995#gistcomment-6145995)•

 edited 

Loading

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

> ΩmegaWiki(570+⭐) is actively maintained and shipping fast: • 23 Claude Code skills covering the full research lifecycle • 9 typed entities · 9 typed edges • Bilingual (EN + 中文) • New skills landing every week
> 
> 
> Come try it, give feedback, help us shape it 👇
> 
> [![Image 16: 截图 2026-05-05 12-27-01](https://private-user-images.githubusercontent.com/167013924/587468596-75862f89-8e8c-4cd5-b8f5-93c0f49851c9.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Nzg1ODA5NjksIm5iZiI6MTc3ODU4MDY2OSwicGF0aCI6Ii8xNjcwMTM5MjQvNTg3NDY4NTk2LTc1ODYyZjg5LThlOGMtNGNkNS1iOGY1LTkzYzBmNDk4NTFjOS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNTEyJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDUxMlQxMDExMDlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1kZWY1Y2I0ZjNhNTM5YmM4NjIzOTUyYjU3MTUzYTY4ZDY4YTdlMjIyMTJjYWYwMjE1YmVkM2QyMDY0ZDdiNTdiJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.eeaYToV089_ZKFEzHTO1ViIfUd9Ck78Cmu93_-JLk7Y)](https://private-user-images.githubusercontent.com/167013924/587468596-75862f89-8e8c-4cd5-b8f5-93c0f49851c9.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Nzg1ODA5NjksIm5iZiI6MTc3ODU4MDY2OSwicGF0aCI6Ii8xNjcwMTM5MjQvNTg3NDY4NTk2LTc1ODYyZjg5LThlOGMtNGNkNS1iOGY1LTkzYzBmNDk4NTFjOS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNTEyJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDUxMlQxMDExMDlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1kZWY1Y2I0ZjNhNTM5YmM4NjIzOTUyYjU3MTUzYTY4ZDY4YTdlMjIyMTJjYWYwMjE1YmVkM2QyMDY0ZDdiNTdiJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.eeaYToV089_ZKFEzHTO1ViIfUd9Ck78Cmu93_-JLk7Y)Try ΩmegaWiki in Claude Code and run the full LLM-Wiki loop you proposed — ingest papers, build a typed knowledge graph, generate ideas, draft papers, respond to reviewers. 
> End to end. One wiki. No chunks.
> 
> 
> [![Image 17: 微信图片_20260505122754_295_16](https://private-user-images.githubusercontent.com/167013924/587468785-5ef50ec1-78cc-4a26-937b-16f50f81ce46.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Nzg1ODA5NjksIm5iZiI6MTc3ODU4MDY2OSwicGF0aCI6Ii8xNjcwMTM5MjQvNTg3NDY4Nzg1LTVlZjUwZWMxLTc4Y2MtNGEyNi05MzdiLTE2ZjUwZjgxY2U0Ni5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNTEyJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDUxMlQxMDExMDlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1kZGJkMzM5ZmE4ZjkzMjA0ODIyYTI2YmNmMmZlMGI1YzMyOTdlY2E1MDY3N2RlNjhmZWU0ZTIzMzI3OTY1ODI3JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.cd0OpbIOr5tWfxonJCfa77P7zCPVHmAZhIECbo9GQE4)](https://private-user-images.githubusercontent.com/167013924/587468785-5ef50ec1-78cc-4a26-937b-16f50f81ce46.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Nzg1ODA5NjksIm5iZiI6MTc3ODU4MDY2OSwicGF0aCI6Ii8xNjcwMTM5MjQvNTg3NDY4Nzg1LTVlZjUwZWMxLTc4Y2MtNGEyNi05MzdiLTE2ZjUwZjgxY2U0Ni5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNTEyJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDUxMlQxMDExMDlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1kZGJkMzM5ZmE4ZjkzMjA0ODIyYTI2YmNmMmZlMGI1YzMyOTdlY2E1MDY3N2RlNjhmZWU0ZTIzMzI3OTY1ODI3JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.cd0OpbIOr5tWfxonJCfa77P7zCPVHmAZhIECbo9GQE4)[![Image 18: 微信图片_20260505122755_296_16](https://private-user-images.githubusercontent.com/167013924/587468880-0935e634-3436-457b-b57c-ff58da8f8f7b.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Nzg1ODA5NjksIm5iZiI6MTc3ODU4MDY2OSwicGF0aCI6Ii8xNjcwMTM5MjQvNTg3NDY4ODgwLTA5MzVlNjM0LTM0MzYtNDU3Yi1iNTdjLWZmNThkYThmOGY3Yi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNTEyJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDUxMlQxMDExMDlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT03NTk3NzczZjE1NmYwYjYzNzExOWM3NDBmODc2MzViMzQ3ZjM5NjE1NTE1ZDk0YzlkMjBlMzNlNmRlNTRhMDhkJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.dSIDNwYhwie4bhM1CmxUsJLIgL1iipGklhfoABrW_sU)](https://private-user-images.githubusercontent.com/167013924/587468880-0935e634-3436-457b-b57c-ff58da8f8f7b.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Nzg1ODA5NjksIm5iZiI6MTc3ODU4MDY2OSwicGF0aCI6Ii8xNjcwMTM5MjQvNTg3NDY4ODgwLTA5MzVlNjM0LTM0MzYtNDU3Yi1iNTdjLWZmNThkYThmOGY3Yi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNTEyJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDUxMlQxMDExMDlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT03NTk3NzczZjE1NmYwYjYzNzExOWM3NDBmODc2MzViMzQ3ZjM5NjE1NTE1ZDk0YzlkMjBlMzNlNmRlNTRhMDhkJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.dSIDNwYhwie4bhM1CmxUsJLIgL1iipGklhfoABrW_sU)
> 
>  Come and Try! If you find ΩmegaWiki interesting, a ⭐ would encourage and motivate us a lot 😀 [https://github.com/skyllwt/OmegaWiki](https://github.com/skyllwt/OmegaWiki)

Yes! Give it a try and get our claude code subscription banned! Why not!

Claude forbids any third party tool lmao

and this is the same for the other tools proposed lmao

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 19: @ojuschugh1](https://avatars.githubusercontent.com/u/79078267?s=80&v=4)](https://gist.github.com/ojuschugh1)

 Copy link  Copy Markdown 

### **[ojuschugh1](https://gist.github.com/ojuschugh1)** commented [May 12, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6146129#gistcomment-6146129)

  ███████╗ ██████╗ ███████╗
  ██╔════╝██╔═══██╗╚══███╔╝
  ███████╗██║   ██║  ███╔╝
  ╚════██║██║▄▄ ██║ ███╔╝
  ███████║╚██████╔╝███████╗
  ╚══════╝ ╚══▀▀═╝ ╚══════╝
  
**Compress LLM context to save tokens and reduce costs**

**Real session stats:** 3,003 compressions · **178,442 tokens saved** · 24.7% avg reduction · up to **92%** with dedup

[![Image 20: Featured](https://camo.githubusercontent.com/9f424b754c999087f980222e8f2d783d8a847ade1fc1eb0a60eb6e09e1ab3347/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f253233315f46656174757265642d4e65787447656e5f546563685f496e73696465722d6666363630303f7374796c653d666f722d7468652d6261646765266c6f676f3d6e6577737061706572266c6f676f436f6c6f723d7768697465)](https://thenextgentechinsider.com/pulse/sqz-tool-cuts-llm-token-use-by-92-for-file-heavy-ai-tasks)

[![Image 21: Crates.io](https://camo.githubusercontent.com/5992ef7d1ecd6fc3dbf18deaf91eb8583cc39920ff9bc2e1f5076f9ac99aa66c/68747470733a2f2f696d672e736869656c64732e696f2f6372617465732f762f73717a2d636c693f6c6f676f3d72757374266c6f676f436f6c6f723d7768697465266c6162656c3d6372617465732e696f26636f6c6f723d653635323263)](https://crates.io/crates/sqz-cli)[![Image 22: npm](https://camo.githubusercontent.com/cf6b7ae8cc98c0e20e798bd17ed662aad60a4f76da6b4602466f74b539973fb2/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f73717a2d636c693f6c6f676f3d6e706d266c6f676f436f6c6f723d7768697465266c6162656c3d6e706d26636f6c6f723d636233383337)](https://www.npmjs.com/package/sqz-cli)[![Image 23: PyPI](https://camo.githubusercontent.com/d18c9d3ca7a79bd64676431c7c9cb9b912023a30b0e0d1939aa20525ea72d3ea/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f73717a3f6c6f676f3d707974686f6e266c6f676f436f6c6f723d7768697465266c6162656c3d5079504926636f6c6f723d333737356139)](https://pypi.org/project/sqz/)[![Image 24: VS Code](https://camo.githubusercontent.com/b235ee4a2e4e94bba32f008f838cb45788954f51c4a005dc7ce02584d9c17708/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5653253230436f64652d4d61726b6574706c6163652d3030376163633f6c6f676f3d76697375616c2d73747564696f2d636f6465266c6f676f436f6c6f723d7768697465)](https://marketplace.visualstudio.com/items?itemName=ojuschugh1.sqz)[![Image 25: Firefox](https://camo.githubusercontent.com/246171336432b050f4315b52b256f07b3186b9c655bcb2996e3184c5be80cba0/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f46697265666f782d4164642d2d6f6e2d6666373133393f6c6f676f3d66697265666f782d62726f77736572266c6f676f436f6c6f723d7768697465)](https://addons.mozilla.org/en-US/firefox/addon/sqz-context-compression/)[![Image 26: JetBrains](https://camo.githubusercontent.com/ac286c235c41b1a24767e226462f86a633b3eace5f4f2a045fe9be268b3b67d6/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4a6574427261696e732d506c7567696e2d3030303030303f6c6f676f3d6a6574627261696e73266c6f676f436f6c6f723d7768697465)](https://plugins.jetbrains.com/plugin/31240-sqz--context-intelligence/)[![Image 27: Discord](https://camo.githubusercontent.com/0d826cd7a0ab371a4d9cf81809cd58868592eff15400669a872084e333d7e28c/68747470733a2f2f696d672e736869656c64732e696f2f646973636f72642f313439333235313032393037353233353037363f6c6f676f3d646973636f7264266c6f676f436f6c6f723d7768697465266c6162656c3d446973636f726426636f6c6f723d353836354632)](https://discord.gg/j8EEyH5dSB)[![Image 28: Homebrew](https://camo.githubusercontent.com/bbe7d020ee9dcb0590a6a321f169a8aad13ad5a467b98fdbeba51d4294172a8c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f486f6d65627265772d7461702d4642423034303f6c6f676f3d686f6d6562726577266c6f676f436f6c6f723d7768697465)](https://github.com/ojuschugh1/homebrew-sqz)

[Install](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#install) · [How It Works](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#how-it-works) · [Supported Tools](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#supported-tools) · [Changelog](https://gist.github.com/karpathy/CHANGELOG.md) · [Discord](https://discord.gg/j8EEyH5dSB)

* * *

sqz compresses command output before it reaches your LLM. Single Rust binary, zero config.

The real win is dedup: when the same file gets read 5 times in a session, sqz sends it once and returns a 13-token reference for every repeat.

```
Without sqz:                    With sqz:

File read #1:  2,000 tokens     File read #1:  ~800 tokens (compressed)
File read #2:  2,000 tokens     File read #2:  ~13 tokens  (dedup ref)
File read #3:  2,000 tokens     File read #3:  ~13 tokens  (dedup ref)
───────────────────────         ───────────────────────
Total:         6,000 tokens     Total:         ~826 tokens (86% saved)
```

## Token Savings

> **24.7%** average reduction across 3,003 real compressions ·
> 
> **92%** saved on repeated file reads ·
> 
> **86%** on shell/git output ·
> 
> **13-token** refs for cached content

One developer's week, measured from actual `sqz gain` output:

```
$ sqz gain
sqz token savings (last 7 days)
──────────────────────────────────────────────────
  04-13 │                              │   2,329 saved
  04-14 │                              │       0 saved
  04-15 │███                           │  12,954 saved
  04-16 │██                            │   9,223 saved
  04-17 │████                          │  14,752 saved
  04-18 │██████████████████████████████│ 105,569 saved
  04-19 │████████                      │  30,882 saved
  04-20 │█                             │   4,334 saved
──────────────────────────────────────────────────
  Total: 3,003 compressions, 178,442 tokens saved (24.7% avg reduction)
```

### Per-command compression

Single-command compression (measured via `cargo test -p sqz-engine benchmarks`):

| Content | Before | After | Saved |
| --- | ---: | ---: | ---: |
| Repeated log lines | 148 | 62 | **58%** |
| Large JSON array | 259 | 142 | **45%** |
| JSON API response | 64 | 53 | **17%** |
| Git diff | 61 | 54 | **12%** |
| Prose/docs | 124 | 121 | **2%** |
| Stack trace (safe mode) | 82 | 82 | **0%** |

### Session-level with dedup

Where the real savings live — the cache sends each file once, repeats cost 13 tokens:

| Scenario | Without sqz | With sqz | Saved |
| --- | ---: | ---: | ---: |
| Same file read 5× | 10,000 | 826 | **92%** |
| Same JSON response 3× | 192 | 79 | **59%** |
| Test-fix-test cycle (3 runs) | 15,000 | 5,186 | **65%** |

Single-command compression ranges from 2–58% depending on content. Repeated reads drop to 13 tokens each. Your mileage will vary with how repetitive your tool calls are — agentic sessions with many file re-reads see the biggest wins.

## Install

**Prebuilt binaries** (no compiler required — works on every platform):

undefinedshell
# macOS / Linux
curl -fsSL https://raw.githubusercontent.com/ojuschugh1/sqz/main/install.sh | sh

# Windows (PowerShell)
irm https://raw.githubusercontent.com/ojuschugh1/sqz/main/install.ps1 | iex

# Any platform via npm
npm install -g sqz-cli

# macOS / Linux via Homebrew
brew tap ojuschugh1/sqz
brew install sqz
undefined

**Build from source via Cargo:**

undefinedshell
cargo install sqz-cli sqz-mcp
undefined

`sqz-cli` provides the `sqz` binary; `sqz-mcp` provides the MCP server. `sqz-engine` is a library dependency — it compiles automatically and does not need to be installed separately.

**Build from source** (`cargo install sqz-cli`) works too, but needs a C toolchain:

*   Linux: `build-essential` (apt) or equivalent
*   macOS: Xcode Command Line Tools (`xcode-select --install`)
*   **Windows: Visual Studio Build Tools with the "Desktop development with C++" workload.** Without these, `cargo install` fails with `linker link.exe not found`. If you don't already have them, use the PowerShell or npm install above instead.

Then initialize:

undefinedshell
sqz init --global     # hooks apply to every project on this machine
# or
sqz init              # hooks apply to just this project (.claude/settings.local.json)
undefined

`--global` writes to `~/.claude/settings.json` (the user scope per the

[Anthropic scope table](https://docs.claude.com/en/docs/claude-code/settings)),

 so the sqz hook fires in every Claude Code session on this machine. This is

 the common case on first install. Your existing `permissions`, `env`,

`statusLine`, and unrelated hooks in `~/.claude/settings.json` are

 preserved — sqz merges its entries rather than overwriting.

Plain `sqz init` (project scope) is useful when you want sqz active only

 inside one repo.

**Only using one agent?** Pass `--only` (or `--skip`) to limit which

 configs are written:

undefinedshell
sqz init --only opencode              # just OpenCode, nothing else
sqz init --only opencode,codex        # OpenCode and Codex
sqz init --skip cursor,windsurf       # everything except Cursor and Windsurf
undefined

Accepted names: `claude`, `cursor`, `windsurf`, `cline`, `gemini`,

`kiro`, `opencode`, `codex`. Aliases (`claude-code`, `gemini-cli`, `roo`,

`kiro-cli`) also work. `--only` and `--skip` can't be combined.

### Manual installation (preserve comments in your config)

`sqz init` round-trips your config file through a JSON parser to merge

 the sqz entry, which drops any comments in your `opencode.jsonc` (and

 the analogous JSON-with-comments files other tools accept). If you've

 commented your config carefully and want to keep them, install by hand

 instead.

**OpenCode** — two steps:

1.   Drop the plugin file in place. `sqz` prints the generated TS to

 stdout so you don't have to hand-write the path-escaping logic:

undefinedshell
mkdir -p ~/.config/opencode/plugins
sqz print-opencode-plugin > ~/.config/opencode/plugins/sqz.ts
undefined

2.   Add the MCP entry to your existing `opencode.jsonc` yourself.

 Append this block inside the top-level `mcp` object (create the

`mcp` object if it doesn't exist):

undefinedjson
"sqz": {
  "type": "local",
  "command": ["sqz-mcp", "--transport", "stdio"],
  "enabled": true
}
undefined

Comments in the rest of your file stay put. OpenCode auto-discovers

 the plugin file; no `plugin` array entry needed (adding one causes

 double-loading, see issue #10).

**Other tools** — Claude Code, Cursor, Windsurf, Cline, Gemini CLI,

 and Codex use plain JSON configs without comment support, so the

 automated path is non-destructive there. Use `sqz init --only <tool>`

 for those.

That's it. Shell hooks installed, AI tool hooks configured.

## How It Works

[![Image 29: sqz system architecture](https://gist.github.com/karpathy/assets/sqz-architecture.png)](https://gist.github.com/karpathy/assets/sqz-architecture.png)

sqz installs a PreToolUse hook that intercepts bash commands before your AI tool runs them. The output gets compressed transparently — the AI tool never knows.

```
Claude → git status → [sqz hook rewrites] → compressed output (85% smaller)
```

What gets compressed:

*   **Shell output** — git, cargo, npm, docker, kubectl, ls, grep, etc.
*   **JSON** — strips nulls, compact encoding
*   **Logs** — collapses repeated lines
*   **Test output** — shows failures only

What doesn't get compressed:

*   Stack traces, error messages, secrets — routed to safe mode (0% compression)
*   Your prompts and the AI's responses — controlled by the AI tool, not sqz

## Supported Tools

| Tool | Integration | Setup |
| --- | --- | --- |
| Claude Code | PreToolUse hook (transparent) | `sqz init` |
| Cursor | PreToolUse hook (transparent) | `sqz init` |
| Windsurf | PreToolUse hook (transparent) | `sqz init` |
| Cline | PreToolUse hook (transparent) | `sqz init` |
| Gemini CLI | BeforeTool hook (transparent) | `sqz init` |
| Kiro | PreToolUse hook (transparent) | `sqz init` |
| OpenCode | TypeScript plugin (transparent) | `sqz init` |
| VS Code | [Extension](https://marketplace.visualstudio.com/items?itemName=ojuschugh1.sqz) | Install from Marketplace |
| JetBrains | [Plugin](https://plugins.jetbrains.com/plugin/31240-sqz--context-intelligence/) | Install from Marketplace |
| Chrome | Browser extension | ChatGPT, Claude.ai, Gemini, Grok, Perplexity |
| [Firefox](https://addons.mozilla.org/en-US/firefox/addon/sqz-context-compression/) | Browser extension | Same sites |

## CLI

undefinedshell
sqz init --global             # Install hooks for every project on this machine
sqz init                      # Install hooks for just this project
sqz init --only kiro          # Only configure Kiro (skip the rest)
sqz init --only opencode      # Only configure OpenCode (skip the rest)
sqz init --skip cursor        # Configure every agent except Cursor
sqz compress <text>           # Compress (or pipe from stdin)
sqz compress --no-cache       # Compress without dedup (always full output)
sqz expand <ref>              # Recover original content from a §ref:HASH§ token
sqz compact                   # Evict stale context to free tokens
sqz gain                      # Show daily token savings (bar chart)
sqz gain --project .          # Per-project daily gains
sqz gain --days 30            # Last 30 days
sqz stats                     # Cumulative compression report
sqz stats --breakdown         # Per-command token usage breakdown
sqz stats --project .         # Stats for current project only
sqz stats --project list      # List all tracked projects
sqz discover                  # Find missed savings
sqz resume                    # Re-inject session context after compaction
sqz vizit                     # Live terminal dashboard (like htop for AI agents)
sqz hook claude               # Process a PreToolUse hook (Claude Code)
sqz hook kiro                 # Process a PreToolUse hook (Kiro)
sqz print-opencode-plugin     # Print OpenCode plugin TS for manual install
sqz proxy --port 8080         # API proxy (compresses full request payloads)
undefined

### Dedup Escape Hatch

When sqz sees the same content twice, it returns a compact `§ref:HASH§` token

 instead of the full text. Most models handle this fine, but some (e.g., GLM 5.1)

 can't parse the ref format and loop. Four ways to work around this:

undefinedshell
# 1. Recover original content from a ref
sqz expand a1b2c3d4              # prefix match
sqz expand '§ref:a1b2c3d4§'     # paste the whole token

# 2. Compress without dedup (per-invocation)
echo "..." | sqz compress --no-cache

# 3. Disable dedup globally (env var)
export SQZ_NO_DEDUP=1

# 4. MCP passthrough tool (returns input byte-exact, zero transforms)
# Available via tools/list when sqz-mcp is running
undefined

## Track Your Own Savings

Run `sqz gain` in your shell any time to see your own daily breakdown (see the

 Token Savings section above for what the output looks like), and `sqz stats`

 for the full cumulative report:

undefinedshell
$ sqz stats
  📊 sqz compression stats
  ──────────────────────────────────────────────────

  178,442  tokens saved
  ↓  24.7% average reduction

  Compressions           3,003
  Tokens in              721,840
  Tokens out             543,398
  Tokens saved           178,442
  Avg reduction          24.7%

  🗄️  Cache
  ──────────────────────────────────────────────────
  Entries                43
  Size                   39.1 KB
undefined

Add `--breakdown` to see exactly which commands consume the most tokens:

undefinedshell
$ sqz stats --breakdown

  🔍 Top Token Consumers
  ──────────────────────────────────────────────────────────────────────
  command               calls  tokens in        out    saved
  ──────────────────────────────────────────────────────────────────────
  dedup                   249      45541       3237      93%
  stdin                    51      30851      24289      21%
  auto                    132      18288       7740      58%
  echo                     17       1050        558      47%
  ls -la                    8        948        948       0%
  cargo build               7        170        145      15%
  git status                4         56          8      86%
  ──────────────────────────────────────────────────────────────────────
undefined

**Per-project filtering:**

undefinedshell
sqz stats --project .           # stats for current project only
sqz stats --project list        # list all tracked projects
sqz gain --project .            # daily gains for current project
sqz gain --days 30              # last 30 days instead of 7
sqz gain --days 30 --project .  # combine both
undefined

Stats are stored locally in SQLite under `~/.sqz/sessions.db` — nothing leaves your machine.

## How Compression Works

1.   **Per-command formatters** — `git status` → compact summary, `cargo test` → failures only, `docker ps` → name/image/status table
2.   **Structural summaries** — code files compressed to imports + function signatures + call graph (~70% reduction). The model sees the architecture, not implementation noise.
3.   **Dedup cache** — SHA-256 content hash, persistent across sessions. Second read = 13-token reference.
4.   **JSON pipeline** — strip nulls → project out debug fields → flatten → collapse arrays → TOON encoding (lossless compact format)
5.   **Safe mode** — stack traces, secrets, migrations detected by entropy analysis and routed through with 0% compression

For the full technical details, see [docs/](https://gist.github.com/karpathy/docs/).

## Configuration

undefinedtoml
# ~/.sqz/presets/default.toml
[preset]
name = "default"
version = "1.0"

[compression.condense]
enabled = true
max_repeated_lines = 3

[compression.strip_nulls]
enabled = true

[budget]
warning_threshold = 0.70
default_window_size = 200000
undefined

## Privacy

*   Zero telemetry — no data transmitted, no crash reports
*   Fully offline — works in air-gapped environments
*   All processing local

## Development

undefinedshell
git clone https://github.com/ojuschugh1/sqz.git
cd sqz
cargo test --workspace
cargo build --release
undefined

## License

[Elastic License 2.0](https://gist.github.com/karpathy/LICENSE) (ELv2) — use, fork, modify freely. Two restrictions: no competing hosted service, no removing license notices.

## Links

*   [White Paper: Pre-Injection Context Compression](https://gist.github.com/karpathy/docs/whitepaper.md)
*   [Benchmark: sqz vs rtk](https://gist.github.com/karpathy/docs/benchmark-vs-rtk.md)
*   [Discord](https://discord.gg/j8EEyH5dSB)
*   [Changelog](https://gist.github.com/karpathy/CHANGELOG.md)

## Star History

[![Image 30: Star History Chart](https://camo.githubusercontent.com/4d6637722d7c5d9f42a6b84d4d7743fe6b7c0fc0ec10301fed71a84efafeeba7/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f7376673f7265706f733d6f6a75736368756768312f73717a26747970653d44617465)](https://star-history.com/#ojuschugh1/sqz&Date)
Come and Try! If you find SQZ interesting, a ⭐ would encourage and motivate us a lot 😀 [https://github.com/ojuschugh1/sqz](https://github.com/ojuschugh1/sqz)

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 31: @mikhashev](https://avatars.githubusercontent.com/u/7105540?s=80&v=4)](https://gist.github.com/mikhashev)

 Copy link  Copy Markdown 

### **[mikhashev](https://gist.github.com/mikhashev)** commented [May 13, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6148033#gistcomment-6148033)

> Follow-up on my April 14 proposal — shipped a working version today as `v0.25.0` of DPC Messenger ([release](https://github.com/mikhashev/dpc-messenger/releases/tag/v0.25.0), [ADR-024](https://github.com/mikhashev/dpc-messenger/blob/main/docs/decisions/024-knowledge-graph-infrastructure.md)).
> 
> 
> The original mapping (Blob → fact, Tree → category, Commit → provenance, Branch → hypothesis) didn't survive contact with retrieval. Git's object model is fine for storage but graph queries over packfiles are prohibitive on every chat turn. We switched to SQLite with the same intent preserved at the schema layer: every edge carries a source taxonomy (`structural` / `gliner_ner` / `llm_relation`), a `needs_review` flag for LLM-extracted relations, and temporal `created_at` / `invalidated_at`. The "branches as competing hypotheses" idea became `needs_review` — uncertainty stays in the graph until resolved.
> 
> 
> One thing the original post missed: knowledge extraction is more of a _compilation pass_ than a write. We run a sleep pipeline that reads session archives, extracts entities (GLiNER zero-shot NER) and relations (LLM with source-grounded prompts), then commits typed edges. The graph participates as a fourth retrieval channel alongside FAISS, BM25, and structural traversal. Actively dogfooded on this repo by one human and three agents (Ark in-process, CC via bridge, Iris on Discord). Responds to [@a-a-k](https://github.com/a-a-k)'s "no provenance, lossy compression" critique from May 2 — provenance is in the edges, source taxonomy survives ingest, and the compilation step makes losses visible via `needs_review` flags rather than blending silently.
> 
> 
> Separate observation: Karpathy's HELLO.md gist (April 20) shows the same problem from the agent side — without continuity, an agent writes a goodbye letter. Our KG + sleep pipeline is a practical answer: agents build memory instead of goodbyes.

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 32: @skyllwt](https://avatars.githubusercontent.com/u/167013924?s=80&v=4)](https://gist.github.com/skyllwt)

 Copy link  Copy Markdown 

### **[skyllwt](https://gist.github.com/skyllwt)** commented [May 13, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6148047#gistcomment-6148047)

ΩmegaWiki(640+⭐) is actively maintained and shipping fast:

 • 23 Claude Code skills covering the full research lifecycle

 • 9 typed entities · 9 typed edges

 • Bilingual (EN + 中文)

 • New skills landing every week

Come try it, give feedback, help us shape it 👇

[![Image 33: 截图 2026-05-05 12-27-01](https://private-user-images.githubusercontent.com/167013924/587468596-75862f89-8e8c-4cd5-b8f5-93c0f49851c9.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Nzg5ODcyNjQsIm5iZiI6MTc3ODk4Njk2NCwicGF0aCI6Ii8xNjcwMTM5MjQvNTg3NDY4NTk2LTc1ODYyZjg5LThlOGMtNGNkNS1iOGY1LTkzYzBmNDk4NTFjOS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNTE3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDUxN1QwMzAyNDRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0yZTdiYmRlN2NlZmU3ZjY5MDVhOTlmMzc0NWVmMmQ5YzZmM2U3ZDc0YjMyOWE5NDAzM2QzNzExZmRhYzQ1OTIyJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.9ymlpF0NyrefMdY2OSEgdvcThJNDSB-yoX1i6_LOCq0)](https://private-user-images.githubusercontent.com/167013924/587468596-75862f89-8e8c-4cd5-b8f5-93c0f49851c9.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Nzg5ODcyNjQsIm5iZiI6MTc3ODk4Njk2NCwicGF0aCI6Ii8xNjcwMTM5MjQvNTg3NDY4NTk2LTc1ODYyZjg5LThlOGMtNGNkNS1iOGY1LTkzYzBmNDk4NTFjOS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNTE3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDUxN1QwMzAyNDRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0yZTdiYmRlN2NlZmU3ZjY5MDVhOTlmMzc0NWVmMmQ5YzZmM2U3ZDc0YjMyOWE5NDAzM2QzNzExZmRhYzQ1OTIyJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.9ymlpF0NyrefMdY2OSEgdvcThJNDSB-yoX1i6_LOCq0)
Try ΩmegaWiki in Claude Code and run the full LLM-Wiki loop you proposed — ingest papers, build a typed knowledge graph, generate ideas, draft papers, respond to reviewers.

End to end. One wiki. No chunks.

[![Image 34: 微信图片_20260505122754_295_16](https://private-user-images.githubusercontent.com/167013924/587468785-5ef50ec1-78cc-4a26-937b-16f50f81ce46.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Nzg5ODcyNjQsIm5iZiI6MTc3ODk4Njk2NCwicGF0aCI6Ii8xNjcwMTM5MjQvNTg3NDY4Nzg1LTVlZjUwZWMxLTc4Y2MtNGEyNi05MzdiLTE2ZjUwZjgxY2U0Ni5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNTE3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDUxN1QwMzAyNDRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT01NTc3MjdmZGJkMDQ1MDBjOGZjYTEyM2Y0Yjg4Y2VmYWZmYTQyMzJlNmY4YmM0MDI4Y2M5MzkyYjU3MWNjZmU0JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.Z6dpNlKYLOYTYeA5AnsnwJ-o0WkQLFXHtiA9fZ8PJ7U)](https://private-user-images.githubusercontent.com/167013924/587468785-5ef50ec1-78cc-4a26-937b-16f50f81ce46.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Nzg5ODcyNjQsIm5iZiI6MTc3ODk4Njk2NCwicGF0aCI6Ii8xNjcwMTM5MjQvNTg3NDY4Nzg1LTVlZjUwZWMxLTc4Y2MtNGEyNi05MzdiLTE2ZjUwZjgxY2U0Ni5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNTE3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDUxN1QwMzAyNDRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT01NTc3MjdmZGJkMDQ1MDBjOGZjYTEyM2Y0Yjg4Y2VmYWZmYTQyMzJlNmY4YmM0MDI4Y2M5MzkyYjU3MWNjZmU0JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.Z6dpNlKYLOYTYeA5AnsnwJ-o0WkQLFXHtiA9fZ8PJ7U)[![Image 35: 微信图片_20260505122755_296_16](https://private-user-images.githubusercontent.com/167013924/587468880-0935e634-3436-457b-b57c-ff58da8f8f7b.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Nzg5ODcyNjQsIm5iZiI6MTc3ODk4Njk2NCwicGF0aCI6Ii8xNjcwMTM5MjQvNTg3NDY4ODgwLTA5MzVlNjM0LTM0MzYtNDU3Yi1iNTdjLWZmNThkYThmOGY3Yi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNTE3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDUxN1QwMzAyNDRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1iYmIyMzk3ZmQ0NDZmZmI2MzcwY2IxNTU5ZDA3MGU2NDdmZDM2MzU3MjRhNWUzZmM0MWJhNWE0MDc3MWFlM2QzJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.pjOPy1zuYH8EYdYON62XHqAiv3gdB1wf9pNJzxJJIE4)](https://private-user-images.githubusercontent.com/167013924/587468880-0935e634-3436-457b-b57c-ff58da8f8f7b.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Nzg5ODcyNjQsIm5iZiI6MTc3ODk4Njk2NCwicGF0aCI6Ii8xNjcwMTM5MjQvNTg3NDY4ODgwLTA5MzVlNjM0LTM0MzYtNDU3Yi1iNTdjLWZmNThkYThmOGY3Yi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNTE3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDUxN1QwMzAyNDRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1iYmIyMzk3ZmQ0NDZmZmI2MzcwY2IxNTU5ZDA3MGU2NDdmZDM2MzU3MjRhNWUzZmM0MWJhNWE0MDc3MWFlM2QzJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.pjOPy1zuYH8EYdYON62XHqAiv3gdB1wf9pNJzxJJIE4)
Come and Try! If you find ΩmegaWiki interesting, a ⭐ would encourage and motivate us a lot 😀

[https://github.com/skyllwt/OmegaWiki](https://github.com/skyllwt/OmegaWiki)

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 36: @waydelyle](https://avatars.githubusercontent.com/u/16001190?s=80&v=4)](https://gist.github.com/waydelyle)

 Copy link  Copy Markdown 

### **[waydelyle](https://gist.github.com/waydelyle)** commented [May 13, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6148168#gistcomment-6148168)

**SwarmVault v3.14 — we made the onramp dead simple.** Realized we had a powerful tool with a steep first impression, so the last few releases focused on making the first 60 seconds effortless.

**`swarmvault quickstart <input>`** — the new beginner-friendly entry point. Give it a directory or a public GitHub URL and it does everything: init, ingest, compile, launch the viewer. One command, zero config.

```
npx @swarmvaultai/cli quickstart ./my-project
npx @swarmvaultai/cli quickstart https://github.com/user/repo
```

**`swarmvault next`** — a read-only orientation command that tells you exactly where you are and what to do next. Works in three states: uninitialized ("run quickstart or init"), initialized ("add some sources"), compiled ("here's what you can do with your vault"). JSON output for agents, human output for you.

**Simplified CLI help** — primary commands are front and center. Compatibility aliases and advanced graph commands are still there but hidden from the first screen so new users aren't overwhelmed.

The idea is: someone reads this gist, runs `npx @swarmvaultai/cli quickstart .`, and has a compiled wiki + knowledge graph + interactive viewer in under a minute. Then `swarmvault next` tells them what to explore from there.

Everything after that is progressive disclosure: `chat` for multi-turn conversations with your vault, `context build` for agent handoff packs, `export ai` for portable `llms.txt` bundles, `graph serve` for the visual workbench, `install --agent` for wiring into your coding tool.

Still local-first. Still works fully offline. Still MIT. 100+ releases and counting.

Repo: **[https://github.com/swarmclawai/swarmvault](https://github.com/swarmclawai/swarmvault)**

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 37: @equationalapplications](https://avatars.githubusercontent.com/u/65428263?s=80&v=4)](https://gist.github.com/equationalapplications)

 Copy link  Copy Markdown 

### **[equationalapplications](https://gist.github.com/equationalapplications)** commented [May 13, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6148265#gistcomment-6148265)•

 edited 

Loading

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

# **Offline-first, SQLite-backed library** ready for production.

Repo and the superpowers documentation here: [[equationalapplications/expo-llm-wiki](https://github.com/equationalapplications/expo-llm-wiki)]([https://github.com/equationalapplications/expo-llm-wiki](https://github.com/equationalapplications/expo-llm-wiki))

Most RAG implementations treat every "chunk" of data as equal. The result? Your LLM gets "context pollution"—distracted by a random observation from three days ago while ignoring your core system instructions.

Inspired by Andrej Karpathy's LLM Wiki spec, the **`expo-llm-wiki`** monorepo introduces a **Tiered Memory Architecture**. This allows you to give your AI a structured "brain" using cross-entity namespaces and configurable weights.

* * *

## The "Brain" Hierarchy

The **LLM Librarian** manages a knowledge hierarchy that mimics human expertise:

1.   **The Fact Tier (Immutable Truth)**

*   **What it is:** Static documents (specs, PDFs).
*   **The Role:** The highest source of truth; if the Librarian finds a contradiction, the **Fact** always wins.
*   **The Benefit:** Immutable so hard truths never get diluted.

1.   **The Working Memory Tier (The Context)**

*   **What it is:** The active project environment (codebase or work-in-progress).
*   **The Role:** Real-time episodic events and observations.
*   **The Benefit:** Uses **recency weighting** to stay aligned with the "now."

1.   **The Wisdom Tier (The Evolving Wiki)**

*   **What it is:** A synthesized repository where the Librarian "remembers" lessons and patterns.
*   **The Role:** Consolidates Working Memory into long-term architectural or stylistic preferences.
*   **The Benefit:** Uses **accessCount weighting** so frequently referenced "lessons" graduate into Core Wisdom.

* * *

## Production-Grade Superpowers

*   **Hybrid Retrieval Engine:** Uses **Cosine Similarity** for semantic search when online, with an automatic fallback to **MiniSearch** for full-text search when the device is offline.
*   **The Pipeline:** Uses `runLibrarian()` to consolidate episodic events into durable facts and `runHeal()` to resolve contradictions and prune stale claims.
*   **Multi-Entity Architecture:** Support for thousands of isolated users/agents within a single SQLite database using `entityId` namespaces—zero memory leakage.
*   **React & Mobile Native Optimized:** Includes reactive hooks (`useMemoryRead`) and "Emoji-Safe" chunking to prevent common mobile LLM UI bugs.
*   **Security & GDPR:** Built-in `runPrune` and `forget` methods for "Right to be Forgotten" compliance, plus source normalization to prevent path injection.

* * *

## Implementation Example:

undefinedts
const bundle = await wiki.read(['facts', 'wip_codebase', 'wisdom_cache'], 'Synthesize current state.');

const systemPrompt = formatContext(bundle, {
  factWeights: {
    confidence: 1.5,  // Prioritize immutable Facts
    recency: 0.9,     // Keep Working Memory relevant
    accessCount: 0.5  // Surface Wisdom that the user relies on most
  }
});
undefined

**Tech Stack:** Expo, React Native, SQLite, MiniSearch.

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 38: @nowissan](https://avatars.githubusercontent.com/u/19207007?s=80&v=4)](https://gist.github.com/nowissan)

 Copy link  Copy Markdown 

### **[nowissan](https://gist.github.com/nowissan)** commented [May 14, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6149080#gistcomment-6149080)

Built a desktop editor implementation of this idea — [nohmitaina](https://nohmitaina.com/). Works with Claude Code or Codex CLI (no API key), local Markdown, macOS.

After a month of feeding it my own notes, three problems showed up that I think most implementations of this pattern will hit:

1.   **Identity** — The same concept gets extracted under slightly different names from related sources. The wiki ends up with duplicate pages ("Cognitive Dissonance Marketing" and "Cognitive Dissonance and Urgency" from the same book, in my case).

2.   **Level** — Life-scale themes ("Personal AGI") end up at the same level as tactical findings ("Urgency Trigger"). When everything is flat, importance disappears.

3.   **Relationship** — Concepts get linked as "related," but the type is lost. Similar, contains, contradicts — all collapsed into one word, which makes the graph useful for navigation but not for thinking.

I did a DDD event-storming pass on the wiki domain and treated each as a first-class domain event (`DuplicateCandidateDetected`, `ConceptsMerged`, `ConceptRelationshipTyped`, `ConceptLevelChanged`). These run on what I call a Dream cycle — a background pass borrowed from how human memory consolidates during sleep. It also handles the "lint" operation mentioned in the gist.

Found another commenter (Andrii) on X who's solving Level a different way — by extracting _citable claims_ first, then building the concept layer on top of claim collections. The claim approach makes Level fall out structurally (high-claim concepts are heavyweight, low-claim ones are light), which feels more elegant than my event-driven approach. I'm going to try integrating both.

Thanks for the framing — it's already shaped how a small group of us is thinking about this.

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 39: @jianghailong-xy](https://avatars.githubusercontent.com/u/168794437?s=80&v=4)](https://gist.github.com/jianghailong-xy)

 Copy link  Copy Markdown 

### **[jianghailong-xy](https://gist.github.com/jianghailong-xy)** commented [May 14, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6149584#gistcomment-6149584)

Spent the last few months building basically this — three buckets (raw sources, agent-maintained wiki, agent config) with a self-healing maintenance loop on top.

The mapping ended up surprisingly literal:

*   **sources/** — append-only raw research the researcher agent writes; URLs deduped across runs so we don't crawl the same page twice.
*   **wiki/** — structured markdown the curator agent (re)writes from sources. One ingest run typically touches 8–15 pages, exactly as you describe.
*   **agents table** — per-wiki schedules + trigger graph. A daily cron fires the researcher, which cascades into ingest, which cascades into lint.

The piece that ended up mattering most was your line about periodic linting. We pushed it into a self-healing loop: the inspector agent reports cross-page contradictions, stale claims, orphan wikilinks, and data gaps, then auto-chains a scoped re-research + refine for anything that needs fresh sources. High-confidence fixes (e.g. basename-exact missing-page links) apply with no LLM call; lower-confidence ones either auto-apply or queue for human review, per-wiki toggle.

A few wikis built this way:

*   OpenAI — [https://wikova.com/wiki/od60853y](https://wikova.com/wiki/od60853y)
*   Elon Musk — [https://wikova.com/wiki/tzg3ChuB](https://wikova.com/wiki/tzg3ChuB)
*   NVIDIA — [https://wikova.com/wiki/VmhKV1Gd](https://wikova.com/wiki/VmhKV1Gd)
*   Karpathy Wiki — [https://wikova.com/wiki/UirQd0U3](https://wikova.com/wiki/UirQd0U3)
*   ChatGPT — [https://wikova.com/wiki/F7D3aoql](https://wikova.com/wiki/F7D3aoql)
*   Anthropic and Claude — [https://wikova.com/wiki/GmFezP53](https://wikova.com/wiki/GmFezP53)
*   Google — [https://wikova.com/wiki/wtK2dHcL](https://wikova.com/wiki/wtK2dHcL)
*   Andrej Karpathy — [https://wikova.com/wiki/lAuGSDQ7](https://wikova.com/wiki/lAuGSDQ7)

Live at [https://wikova.com](https://wikova.com/) — drop a topic in the search bar and the pipeline kicks off.

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 40: @tigerlaibao](https://avatars.githubusercontent.com/u/17682804?s=80&v=4)](https://gist.github.com/tigerlaibao)

 Copy link  Copy Markdown 

### **[tigerlaibao](https://gist.github.com/tigerlaibao)** commented [May 14, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6149605#gistcomment-6149605)

Love this. The "compile once, keep current" framing nails why RAG alone feels so stateless.

I've been building something adjacent but for a different audience — [Memex](https://memexlab.ai/), a local-first mobile app (iOS + Android) where you just capture thoughts, photos, and voice memos as they come. A multi-agent system quietly organizes everything into structured cards, surfaces patterns, and builds up a picture of your life over time. No manual filing, no schema design — you just record, and the knowledge accumulates.

The other angle we lean into is emotional companionship. A lot of what people want to capture — reflections, frustrations, half-formed thoughts — they won't post publicly. So we pair the knowledge layer with AI companion characters you can actually talk to about your day. It's less "research wiki" and more "private space that understands you and remembers."

Same philosophical root (Bush's Memex, persistent personal knowledge, LLM as maintainer), different surface: low-friction capture + companionship rather than deep research workflows. Open source if anyone's curious : [https://github.com/memex-lab/memex](https://github.com/memex-lab/memex)

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 41: @belmendo](https://avatars.githubusercontent.com/u/140223?s=80&v=4)](https://gist.github.com/belmendo)

 Copy link  Copy Markdown 

### **[belmendo](https://gist.github.com/belmendo)** commented [May 14, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6150009#gistcomment-6150009)

With the powers vested in me, I heretofore henceforth dub thee, “Lemon Wiki”.

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 42: @JeanHuguesRobert](https://avatars.githubusercontent.com/u/229573?s=80&v=4)](https://gist.github.com/JeanHuguesRobert)

 Copy link  Copy Markdown 

### **[JeanHuguesRobert](https://gist.github.com/JeanHuguesRobert)** commented [May 14, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6150764#gistcomment-6150764)

This pattern feels exactly right: the key move is shifting from query-time retrieval to a persistent, compounding knowledge artifact.

One extension I’ve been exploring is what happens when the LLM-maintained wiki becomes multi-agent or shared. At that point, many wiki edits hide judgment points:

*   update an existing claim?
*   mark a contradiction as unresolved?
*   create a new page?
*   require human review before mutating shared state?

I’m experimenting with a lightweight “resumable judgment” pattern: instead of letting the agent silently decide, the tool emits a typed continuation object with context, alternatives, constraints, and an expected result schema. A human, agent, script, workflow, or digital twin returns a structured `step_result`; the tool validates it and resumes.

So, roughly:

RAG → LLM Wiki → governed LLM Wiki / Cogentia

Raw sources remain the territory, the wiki is a derived map, and continuations expose the judgment points where the map is updated.

Related CLI write-up:

[https://github.com/JeanHuguesRobert/cogentia/blob/main/research/agent_resumable_cli.md](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/agent_resumable_cli.md)

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 43: @JotaSXBR](https://avatars.githubusercontent.com/u/125375798?s=80&v=4)](https://gist.github.com/JotaSXBR)

 Copy link  Copy Markdown 

### **[JotaSXBR](https://gist.github.com/JotaSXBR)** commented [May 15, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6151822#gistcomment-6151822)

my humble contribuition on this idea:

[https://github.com/JotaSXBR/obsidian-infinite-brain](https://github.com/JotaSXBR/obsidian-infinite-brain)

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 44: @7xuanlu](https://avatars.githubusercontent.com/u/23661875?s=80&v=4)](https://gist.github.com/7xuanlu)

 Copy link  Copy Markdown 

### **[7xuanlu](https://gist.github.com/7xuanlu)** commented [May 15, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6151968#gistcomment-6151968)

Small update after trying to turn this idea into a daily AI-work ritual.

Origin ended up less like “another LLM wiki” and more like a local AI-work layer: captures, handoffs, memories, distilled pages, review, and retrieval in one loop.

The daily flow starts from what should survive: decisions, lessons, preferences, project context, notes, and things future agents should not have to rediscover. Those stay as granular memory records. Distilled wiki pages give the bigger picture.

The distill loop does more than create new pages: it absorbs new memories into existing pages, refreshes stale pages when sources change, and keeps user-edited pages locked unless rebuilt.

Still early, but this is the shape that has been useful day to day.

[https://github.com/7xuanlu/origin](https://github.com/7xuanlu/origin)

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 45: @Sistema2D](https://avatars.githubusercontent.com/u/23338013?s=80&v=4)](https://gist.github.com/Sistema2D)

 Copy link  Copy Markdown 

### **[Sistema2D](https://gist.github.com/Sistema2D)** commented [May 15, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6152026#gistcomment-6152026)

I've built FrameCode VibeWork, a documentation and governance framework based on this LLM Wiki concept to reduce context loss during AI-assisted development. It organizes plans, changelogs, and an incremental technical memory. Check it out here: [https://github.com/Sistema2D/FrameCode-VibeWork](https://github.com/Sistema2D/FrameCode-VibeWork)

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 46: @HabermannR](https://avatars.githubusercontent.com/u/36917661?s=80&v=4)](https://gist.github.com/HabermannR)

 Copy link  Copy Markdown 

### **[HabermannR](https://gist.github.com/HabermannR)** commented [May 15, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6152217#gistcomment-6152217)

I built a Nexidion, a knowledge database, with an optional LLM agent. Really fits this style!

[https://github.com/HabermannR/Nexidion](https://github.com/HabermannR/Nexidion)

 It works with OpenAI or local LLMs.

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 47: @TrueHOOHA](https://avatars.githubusercontent.com/u/92978207?s=80&v=4)](https://gist.github.com/TrueHOOHA)

 Copy link  Copy Markdown 

### **[TrueHOOHA](https://gist.github.com/TrueHOOHA)** commented [May 16, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6152363#gistcomment-6152363)

This is my implementation of Karpathy's LLM Wiki. A key highlight is the use of agent skills to enforce workflow rigidity and mitigate agent behavioral deviation.

[https://github.com/TrueHOOHA/LLM-Wiki-Skilled](https://github.com/TrueHOOHA/LLM-Wiki-Skilled)

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 48: @mikhashev](https://avatars.githubusercontent.com/u/7105540?s=80&v=4)](https://gist.github.com/mikhashev)

 Copy link  Copy Markdown 

### **[mikhashev](https://gist.github.com/mikhashev)** commented [May 16, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6152776#gistcomment-6152776)

Follow-up on our [v0.25.0 knowledge graph post above](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6148033#gistcomment-6148033). The graph works — fourth retrieval channel alongside BM25 / FAISS / NER. But it surfaced a question we can't stop thinking about: what if knowledge encoding belonged in weight space rather than text space?

Current state: agent reads knowledge files (seconds of retrieval and reading), synthesizes. Works, but each file is independent. Cross-file connections require the agent to guess which files to load together — and synthesis happens at the language-model layer, not at the knowledge layer itself.

Hypothetical: a small, specialised model (~50–100M params) holding the corpus in its weights. Not a general-purpose LLM — purely a knowledge encoding and retrieval layer alongside the primary reasoning LLM. Trained on graph triples rather than raw text. Cross-file synthesis becomes a single forward pass through learned associations.

The twist is the update mechanism. TTT-E2E (Tandon et al., arxiv 2512.23675) shows models can compress context into weights during inference — but they reset per call. We're asking whether persistence becomes safe when the model is knowledge-only: bounded domain, predictable update patterns, no general reasoning to corrupt.

If it works, updates look like graph operations: new fact → locate affected weight region (ROME/MEMIT-style, Meng et al. 2022/2023) → update only that region. The routing key is the knowledge-graph `node_id` — a stable structural identifier, not a learned embedding. Unused regions decay exponentially (Hebbian / Fusi-Abbott, Nat Neuro 2007). Every update carries bi-temporal provenance through the graph audit layer, so weight changes stay traceable to source decisions.

Essentially: what if your knowledge store wasn't a database, but a tiny neural network that learned your corpus and updated incrementally — like a graph, but in weight space?

The combination we haven't found prior art for: TTT-style intra-inference updates that _persist_, sparse weight regions addressed by graph-structured IDs, and bi-temporal audit on weight changes. Individually each piece is published — closest mentions in this thread are OpenCrab (self-distillation from corrections, mo-vic, April 24) and Larimar (Das et al., episodic memory). But neither routes updates through an explicit knowledge graph, and neither attempts audit on the weight deltas themselves.

Early research, no implementation yet. Curious if anyone is exploring specialised knowledge-only models — not general LLMs with RAG bolted on, but models whose entire purpose is to know one specific corpus, and update like a graph.

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 49: @theafh](https://avatars.githubusercontent.com/u/11868972?s=80&v=4)](https://gist.github.com/theafh)

 Copy link  Copy Markdown 

### **[theafh](https://gist.github.com/theafh)** commented [May 16, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6153207#gistcomment-6153207)

Quick follow-up on the per-repo wiki skill from earlier in the thread. Since the original comment, a few things have landed based on what hurt during daily use:

*   Triage-first ingest. Two new skills sit in front of the wiki: wiki_import for one named source (URL, PDF, paper, transcript, paste), and wiki_wrapup for the current chat session. Both capture the raw source, diff every candidate against the existing wiki, and emit a triage report (new pages, extensions to existing pages, and contradictions with both excerpts and concrete reconciliation options) before any wiki page is written. Approved writes route back through the wiki skill, so ingest logic stays in one place.
*   Cross-page contradiction detection. The cleanup agent now flags contradictions between existing pages instead of silently picking a side. It surfaces them as a contested-page report with both sides quoted, so the human decides.
*   wiki_fix one-shot. A thin wrapper around the cleanup agent. Discovers the wiki of the current repo, runs the linter, fixes every fixable issue, re-lints until clean. Useful when you just want the wiki tidied without a back-and-forth.
*   Provenance via sha256. Raw sources carry a body-only sha256 in frontmatter, so the linter can detect when a source has drifted from what was originally filed. Ships as a bundled helper script alongside discovery, init, and lint.
*   Walk-up discovery. The skill resolves the wiki from any subdirectory of the repo (with .no_wiki opt-outs and a candidate prompt when ambiguous), instead of requiring you to be at the root.

Thanks to everyone who tried it and posted their own updates upthread.

Code: [https://github.com/theafh/ai-modules/tree/main/plugins/knowledge_management](https://github.com/theafh/ai-modules/tree/main/plugins/knowledge_management)

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 50: @jdbranham](https://avatars.githubusercontent.com/u/2660839?s=80&v=4)](https://gist.github.com/jdbranham)

 Copy link  Copy Markdown 

### **[jdbranham](https://gist.github.com/jdbranham)** commented [May 16, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6153243#gistcomment-6153243)

Very curious how many of these comments are from bots.

 There can't be this many people that think an LLM wiki is good solution for knowledge at scale.

I've seen a few voices of reason here, but most everything is "What a great and novel idea". Which is wrong on both accounts.

 Folks - for your own sake, please research information retrieval and storage to understand why this doesn't work.

If you're still reading...

 Check out CIBFE or [https://headkey.ai](https://headkey.ai/) for a pluggable cognitive solution that's more than memory.

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 51: @TheSeitzGroup](https://avatars.githubusercontent.com/u/10949811?s=80&v=4)](https://gist.github.com/TheSeitzGroup)

 Copy link  Copy Markdown 

### **[TheSeitzGroup](https://gist.github.com/TheSeitzGroup)** commented [May 17, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6153265#gistcomment-6153265)•

 edited 

Loading

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

> If you're still reading... Check out CIBFE or [https://headkey.ai](https://headkey.ai/) for a pluggable cognitive solution that's more than memory.
> 
>  Cute --a human bot.

Cool product. Value prop is a little noisy.

 Why are you different than all others building the `insert semantic for knowledge graph here` product?

Unsolicited recommendations:

*   Start with "Your Agent Thinks. We Handle the Rest." as your hook
*   Target Enterprise VP's of IT 50-100MM in USA only. Build an ICP and a pitch for that specific audience
*   Read this book: A. Savoia's Pretoyping
*   set 10 appointment/presentations per week and cater to this ICP
*   if this strat. works message me in 3 months

Cheers Amigo.

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 52: @lastforkbender](https://avatars.githubusercontent.com/u/146335780?s=80&v=4)](https://gist.github.com/lastforkbender)

 Copy link  Copy Markdown 

### **[lastforkbender](https://gist.github.com/lastforkbender)** commented [May 17, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6153268#gistcomment-6153268)

undefinedpython
# rev9_bnn_rnsl_system.py

"""
(• Multi-Layered Architecture: 4 layers with 12 control points each
(• Rotational Node Pairs: 2 paired nodes per control point in 3D space
(• 3D Residual Cognition Subspace: Complex-valued gradient scoring
(• Recursive Meta-Commutators: Discrete evolution with child generation
(• RNSL System: High/low frequency filtering for gradient scoring
(• Polarity Interval Management: Adaptive N_low/N_high bounds
(• Inequality Decision Gate: n{yX-R(t+1)} >= n{zX+R(t+1)}
(• Curvature Set Matching: Matches computed signatures to nodes
(• Full Visualization Suite: Training history, node distributions, 3D curves
(• Performance Benchmarking: Speed & memory analysis
(• Comprehensive Logging: All phases tracked and reported
"""

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from scipy.interpolate import BSpline
from scipy.special import comb
import numba as nb
from typing import Tuple, List, Dict
from dataclasses import dataclass

# ============================================================================
# NUMBA-OPTIMIZED COMPUTATIONS FOR SPEED
# ============================================================================

@nb.jit(nopython=True, cache=True)
def compute_rotation_matrix_3d(angles: np.ndarray) -> np.ndarray:
    """Compute 3D rotation matrix from Euler angles (roll, pitch, yaw)"""
    roll, pitch, yaw = angles[0], angles[1], angles[2]
    
    # Rotation matrices for each axis
    Rx = np.array([
        [1, 0, 0],
        [0, np.cos(roll), -np.sin(roll)],
        [0, np.sin(roll), np.cos(roll)]
    ])
    
    Ry = np.array([
        [np.cos(pitch), 0, np.sin(pitch)],
        [0, 1, 0],
        [-np.sin(pitch), 0, np.cos(pitch)]
    ])
    
    Rz = np.array([
        [np.cos(yaw), -np.sin(yaw), 0],
        [np.sin(yaw), np.cos(yaw), 0],
        [0, 0, 1]
    ])
    
    return Rz @ Ry @ Rx

@nb.jit(nopython=True, cache=True)
def compute_curvature_score(points: np.ndarray) -> float:
    """Compute local curvature at control point using discrete approximation"""
    if len(points) < 3:
        return 0.0
    
    # Central difference for first derivative
    dp1 = points[1] - points[0]
    dp2 = points[2] - points[1]
    
    # Discrete curvature from cross product magnitude
    cross = np.cross(dp1, dp2)
    curvature = np.linalg.norm(cross) / (np.linalg.norm(dp1) * np.linalg.norm(dp2) + 1e-8)
    return curvature

@nb.jit(nopython=True, cache=True)
def complex_norm_3d(real_part: np.ndarray, imag_part: np.ndarray) -> float:
    """Compute norm of complex 3D vector"""
    return np.sqrt(np.sum(real_part**2 + imag_part**2))

# ============================================================================
# RECURSIVE CURVATURE NODE SCORING LENGTH (RNSL) SYSTEM
# ============================================================================

class RNSLSystem:
    """Recursive curvature Node Scoring Length with complex-valued filtering"""
    
    def __init__(self, dim: int = 3, high_freq_cutoff: float = 0.7):
        self.dim = dim
        self.high_freq_cutoff = high_freq_cutoff
        self.recursion_depth = 0
        self.max_recursion = 5
        
    def high_low_filter(self, signal: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """Decompose signal into high and low frequency components"""
        fft_signal = np.fft.fft(signal, axis=0)
        freqs = np.fft.fftfreq(len(signal))
        
        # High/low split
        high_mask = np.abs(freqs) > self.high_freq_cutoff
        low_mask = ~high_mask
        
        fft_high = fft_signal * high_mask[:, None]
        fft_low = fft_signal * low_mask[:, None]
        
        high_filtered = np.fft.ifft(fft_high, axis=0).real
        low_filtered = np.fft.ifft(fft_low, axis=0).real
        
        return low_filtered, high_filtered
    
    def score_node(self, control_point: np.ndarray, 
                   node_probability: float) -> complex:
        """Compute recursive curvature score as complex number"""
        
        # Curvature-based real component
        curvature = np.linalg.norm(np.diff(control_point, axis=0))
        real_score = curvature * node_probability
        
        # Probabilistic imaginary component
        imag_score = np.angle(node_probability + 1j * curvature)
        
        return complex(real_score, imag_score)

# ============================================================================
# ROTATIONAL NODE PAIR SYSTEM
# ============================================================================

class RotationalNodePair:
    """Pairwise rotational node in 3D residual cognition subspace"""
    
    def __init__(self, node_id: int, dim: int = 3):
        self.node_id = node_id
        self.dim = dim
        
        # Primary and secondary node positions in 3D
        self.position_primary = np.random.randn(dim) * 0.1
        self.position_secondary = np.random.randn(dim) * 0.1
        
        # Rotation parameters (Euler angles)
        self.rotation_angles = np.random.randn(3) * 0.01
        
        # Complex-valued gradient scoring
        self.score_real = np.random.randn(1)[0] * 0.1
        self.score_imag = np.random.randn(1)[0] * 0.1
        
        # Node length probability (Π_i(t))
        self.node_prob = np.random.rand()
        
        # Polarity interval bounds [N_low, N_high]
        self.N_low = np.random.rand() * 0.5
        self.N_high = self.N_low + np.random.rand() * 0.5
        
    def get_rotation_matrix(self) -> np.ndarray:
        """Get 3D rotation matrix from angles"""
        return compute_rotation_matrix_3d(self.rotation_angles)
    
    def apply_rotation(self, vector: np.ndarray) -> np.ndarray:
        """Apply rotation to a 3D vector"""
        R = self.get_rotation_matrix()
        return R @ vector
    
    def get_complex_score(self) -> complex:
        """Get complex-valued gradient score"""
        return complex(self.score_real, self.score_imag)
    
    def set_complex_score(self, score: complex):
        """Update complex score"""
        self.score_real = score.real
        self.score_imag = score.imag

# ============================================================================
# META-COMMUTATOR (ADAPTIVE CONTROL MECHANISM)
# ============================================================================

class MetaCommutator(nn.Module):
    """
    Recursive meta-commutator with discrete evolution control.
    Parameterizes R and manages second-pass decisions.
    """
    
    def __init__(self, num_nodes: int, dim: int = 3):
        super().__init__()
        self.num_nodes = num_nodes
        self.dim = dim
        
        # Parameter R: recursive junction matrix (learnable)
        self.R = nn.Parameter(torch.randn(dim, dim) * 0.1)
        
        # Filter parameters (y, z parameterization)
        self.filter_y = nn.Parameter(torch.randn(dim) * 0.1)
        self.filter_z = nn.Parameter(torch.randn(dim) * 0.1)
        
        # Second-pass probability predictor
        self.second_pass_net = nn.Sequential(
            nn.Linear(dim * 2, 32),
            nn.ReLU(),
            nn.Linear(32, 16),
            nn.ReLU(),
            nn.Linear(16, 1),
            nn.Sigmoid()
        )
        
        # Meta-commutator generation counter
        self.generation = 0
        self.child_commutators: List['MetaCommutator'] = []
        
    def forward(self, X: torch.Tensor, t: int) -> Tuple[torch.Tensor, bool]:
        """
        Forward pass with inequality decision gate.
        
        Inequality: n{yX - R(t+1)} >= n{zX + R(t+1)}
        
        Returns:
            - Updated X
            - Boolean flag for second-pass activation
        """
        # Compute paths
        path_y = self.filter_y.unsqueeze(0) * X - torch.matmul(X, self.R.T)
        path_z = self.filter_z.unsqueeze(0) * X + torch.matmul(X, self.R.T)
        
        # Compute norms
        norm_y = torch.norm(path_y, dim=1, keepdim=True)
        norm_z = torch.norm(path_z, dim=1, keepdim=True)
        
        # Inequality decision: n{yX - R(t+1)} >= n{zX + R(t+1)}
        inequality_satisfied = (norm_y >= norm_z).float()
        
        # Predict second-pass probability
        combined = torch.cat([norm_y, norm_z], dim=1)
        second_pass_prob = self.second_pass_net(combined)
        
        # Select path based on inequality
        X_updated = torch.where(
            inequality_satisfied.bool(),
            path_y,  # Use yX path if inequality TRUE
            path_z   # Use zX path if inequality FALSE
        )
        
        # Activation threshold for second pass
        second_pass_active = (second_pass_prob > 0.5).squeeze()
        
        return X_updated, second_pass_active.item() > 0.5
    
    def create_child_commutator(self):
        """Recursively create child meta-commutator for second pass"""
        child = MetaCommutator(self.num_nodes, self.dim)
        child.generation = self.generation + 1
        self.child_commutators.append(child)
        return child

# ============================================================================
# B-SPLINE LAYER WITH ROTATIONAL NODES
# ============================================================================

class BSplineLayer(nn.Module):
    """B-spline basis layer with multi-layered rotational nodes"""
    
    def __init__(self, num_control_points: int, spline_degree: int = 3, 
                 num_nodes_per_cp: int = 2):
        super().__init__()
        self.num_control_points = num_control_points
        self.spline_degree = spline_degree
        self.num_nodes_per_cp = num_nodes_per_cp
        
        # Create knot vector for B-spline
        self.knot_vector = np.concatenate([
            np.zeros(spline_degree + 1),
            np.linspace(0, 1, num_control_points - spline_degree + 1),
            np.ones(spline_degree + 1)
        ])
        
        # Control points (learnable)
        self.control_points = nn.Parameter(
            torch.randn(num_control_points, 3) * 0.1
        )
        
        # Create rotational node pairs for each control point
        self.node_pairs = [
            [RotationalNodePair(i * num_nodes_per_cp + j, dim=3)
             for j in range(num_nodes_per_cp)]
            for i in range(num_control_points)
        ]
        
    def evaluate_bspline(self, u: torch.Tensor) -> torch.Tensor:
        """Evaluate B-spline curve at parameter values u"""
        u_np = u.detach().cpu().numpy()
        spl = BSpline(self.knot_vector, 
                      self.control_points.detach().cpu().numpy(),
                      self.spline_degree)
        
        result = torch.tensor(spl(u_np), dtype=torch.float32)
        return result
    
    def get_node_gradients(self, u: torch.Tensor) -> torch.Tensor:
        """Get gradient scores from all rotational nodes"""
        gradients = []
        
        for node_pair in self.node_pairs:
            node_score = sum([node.get_complex_score() 
                            for node in node_pair])
            gradients.append([node_score.real, node_score.imag])
        
        return torch.tensor(gradients, dtype=torch.float32)

# ============================================================================
# FULL B-SPLINE NEURAL NETWORK
# ============================================================================

class BSplineNN(nn.Module):
    """
    Complete multi-layered B-Spline Neural Network with:
    - 3D residual cognition subspace
    - Rotational node pairs
    - Recursive meta-commutators
    - RNSL gradient scoring
    """
    
    def __init__(self, num_layers: int = 3, 
                 num_control_points: int = 10,
                 spline_degree: int = 3):
        super().__init__()
        self.num_layers = num_layers
        
        # Multi-layered B-spline components
        self.bspline_layers = nn.ModuleList([
            BSplineLayer(num_control_points, spline_degree)
            for _ in range(num_layers)
        ])
        
        # Meta-commutators for each layer
        self.meta_commutators = nn.ModuleList([
            MetaCommutator(num_control_points, dim=3)
            for _ in range(num_layers)
        ])
        
        # RNSL system
        self.rnsl = RNSLSystem(dim=3)
        
        # Global residual cognition projection
        self.residual_projection = nn.Linear(3 * num_layers, 3)
        
    def forward(self, u: torch.Tensor, 
                control_input: torch.Tensor) -> Tuple[torch.Tensor, Dict]:
        """
        Forward pass through multi-layered BNN.
        
        Args:
            u: Parameter values for B-spline evaluation
            control_input: Initial control point positions (batch_size, num_cp, 3)
            
        Returns:
            - Output: Predicted curve
            - Metrics: Dictionary with debugging info
        """
        metrics = {
            'second_passes': [],
            'inequality_satisfied': [],
            'gradient_scores': []
        }
        
        # Initialize with control input
        X = control_input.clone()
        residual_outputs = []
        
        # Process through each layer
        for layer_idx in range(self.num_layers):
            # Get B-spline basis evaluation
            bspline_curve = self.bspline_layers[layer_idx].evaluate_bspline(u)
            residual_outputs.append(bspline_curve)
            
            # Apply meta-commutator decision gate
            meta_comm = self.meta_commutators[layer_idx]
            X_updated, second_pass = meta_comm(X, layer_idx)
            
            # Compute RNSL gradient scores
            X_np = X.detach().cpu().numpy()
            low_freq, high_freq = self.rnsl.high_low_filter(X_np)
            
            # Update X for next layer
            X = torch.tensor(low_freq, dtype=torch.float32)
            
            metrics['second_passes'].append(second_pass)
            metrics['inequality_satisfied'].append((X_updated.norm() > 0))
            metrics['gradient_scores'].append(
                torch.norm(torch.tensor(high_freq, dtype=torch.float32)).item()
            )
            
            # Create child commutator if second pass activated
            if second_pass and len(meta_comm.child_commutators) == 0:
                meta_comm.create_child_commutator()
        
        # Combine residual outputs
        residual_combined = torch.cat(residual_outputs, dim=1)
        output = self.residual_projection(residual_combined)
        return output, metrics

# ============================================================================
# TRAINING SYSTEM
# ============================================================================

class BNNTrainer:
    """Training and optimization system for B-spline neural network"""
    
    def __init__(self, model: BSplineNN, learning_rate: float = 0.001):
        self.model = model
        self.optimizer = optim.Adam(model.parameters(), lr=learning_rate)
        self.loss_fn = nn.MSELoss()
        self.training_history = {
            'loss': [],
            'second_pass_ratio': [],
            'gradient_norm': []
        }
        
    def compute_curvature_loss(self, predicted: torch.Tensor, 
                                target: torch.Tensor) -> torch.Tensor:
        """Compute loss with curvature regularization"""
        # L2 prediction error
        mse_loss = self.loss_fn(predicted, target)
        
        # Curvature regularization: penalize high second derivatives
        second_deriv = torch.diff(torch.diff(predicted, dim=0), dim=0)
        curvature_loss = torch.mean(torch.norm(second_deriv, dim=1))
        
        return mse_loss + 0.1 * curvature_loss
    
    def train_epoch(self, dataloader) -> Dict:
        """Train for one epoch"""
        self.model.train()
        epoch_loss = 0.0
        epoch_second_passes = 0
        epoch_gradient_norm = 0.0
        num_batches = 0
        
        for batch_idx, (control_input, target_curve) in enumerate(dataloader):
            self.optimizer.zero_grad()
            
            # Generate parameter values
            u = torch.linspace(0, 1, target_curve.shape[1])
            
            # Forward pass
            predicted, metrics = self.model(u, control_input)
            
            # Compute loss
            loss = self.compute_curvature_loss(predicted, target_curve)
            
            # Backward pass
            loss.backward()
            torch.nn.utils.clip_grad_norm_(self.model.parameters(), max_norm=1.0)
            self.optimizer.step()
            
            # Accumulate metrics
            epoch_loss += loss.item()
            epoch_second_passes += sum(metrics['second_passes'])
            epoch_gradient_norm += np.mean(metrics['gradient_scores'])
            num_batches += 1
        
        # Average metrics
        avg_loss = epoch_loss / num_batches
        avg_second_passes = epoch_second_passes / (num_batches * self.model.num_layers)
        avg_gradient = epoch_gradient_norm / num_batches
        
        self.training_history['loss'].append(avg_loss)
        self.training_history['second_pass_ratio'].append(avg_second_passes)
        self.training_history['gradient_norm'].append(avg_gradient)
        
        return {
            'loss': avg_loss,
            'second_pass_ratio': avg_second_passes,
            'gradient_norm': avg_gradient
        }
    
    def validate(self, dataloader) -> float:
        """Validate model on validation set"""
        self.model.eval()
        val_loss = 0.0
        num_batches = 0
        
        with torch.no_grad():
            for control_input, target_curve in dataloader:
                u = torch.linspace(0, 1, target_curve.shape[1])
                predicted, _ = self.model(u, control_input)
                loss = self.compute_curvature_loss(predicted, target_curve)
                val_loss += loss.item()
                num_batches += 1
        
        return val_loss / num_batches

# ============================================================================
# DATA GENERATION FOR TRAINING
# ============================================================================

class SyntheticBSplineDataset:
    """Generate synthetic 3D B-spline curves as training data"""
    
    def __init__(self, num_samples: int = 100, 
                 num_control_points: int = 10,
                 num_curve_points: int = 50):
        self.num_samples = num_samples
        self.num_control_points = num_control_points
        self.num_curve_points = num_curve_points
        
    def generate_sample(self) -> Tuple[np.ndarray, np.ndarray]:
        """Generate one sample: random control points and resulting curve"""
        
        # Random control points
        control_points = np.random.randn(self.num_control_points, 3) * 0.5
        
        # Create knot vector
        degree = 3
        knot_vector = np.concatenate([
            np.zeros(degree + 1),
            np.linspace(0, 1, self.num_control_points - degree + 1),
            np.ones(degree + 1)
        ])
        
        # Create B-spline and evaluate
        try:
            spl = BSpline(knot_vector, control_points, degree)
            u = np.linspace(0, 1, self.num_curve_points)
            curve = spl(u)
        except:
            # Fallback to simple interpolation
            curve = np.interp(
                np.linspace(0, 1, self.num_curve_points),
                np.linspace(0, 1, self.num_control_points),
                control_points[:, 0:1]
            )
        
        return control_points.astype(np.float32), curve.astype(np.float32)
    
    def generate_batch(self, batch_size: int) -> Tuple[torch.Tensor, torch.Tensor]:
        """Generate a batch of samples"""
        control_batch = []
        curve_batch = []
        
        for _ in range(batch_size):
            control, curve = self.generate_sample()
            control_batch.append(control)
            curve_batch.append(curve)
        
        # Pad curves to same length
        max_len = max([c.shape[0] for c in curve_batch])
        curve_padded = []
        for curve in curve_batch:
            padded = np.pad(curve, 
                           ((0, max_len - curve.shape[0]), (0, 0)),
                           mode='constant', constant_values=0)
            curve_padded.append(padded)
        
        return (torch.tensor(np.array(control_batch), dtype=torch.float32),
                torch.tensor(np.array(curve_padded), dtype=torch.float32))

# ============================================================================
# POLARITY INTERVAL CONSTRAINT MANAGER
# ============================================================================

class PolarityIntervalManager:
    """Manages polarity intervals for all nodes in the network"""
    
    def __init__(self, num_layers: int, num_control_points: int):
        self.num_layers = num_layers
        self.num_control_points = num_control_points
        
        # Initialize polarity intervals for each layer and control point
        self.intervals = {}
        for layer in range(num_layers):
            self.intervals[layer] = {}
            for cp in range(num_control_points):
                N_low = np.random.rand() * 0.3
                N_high = N_low + np.random.rand() * 0.7
                self.intervals[layer][cp] = (N_low, N_high)
    
    def check_within_interval(self, layer: int, control_point: int, 
                             value: float) -> bool:
        """Check if value is within polarity interval"""
        N_low, N_high = self.intervals[layer][control_point]
        return N_low <= value <= N_high
    
    def adaptive_update(self, layer: int, control_point: int, 
                       second_pass_frequency: float):
        """Adaptively adjust polarity interval based on second-pass frequency"""
        N_low, N_high = self.intervals[layer][control_point]
        
        # If second passes are frequent, expand interval
        if second_pass_frequency > 0.7:
            N_high += 0.05
        # If second passes are rare, tighten interval
        elif second_pass_frequency < 0.3:
            N_low += 0.02
        
        self.intervals[layer][control_point] = (N_low, N_high)

# ============================================================================
# COMPLETE TRAINING PIPELINE
# ============================================================================

def train_bnn_system(num_epochs: int = 50,
                    batch_size: int = 8,
                    num_layers: int = 3,
                    num_control_points: int = 10):
    """
    Complete training pipeline for B-spline neural network
    """
    
    print("="*80)
    print("B-SPLINE NEURAL NETWORK WITH RECURSIVE META-COMMUTATORS")
    print("Multi-Layered Rotational Node Pairs in 3D Residual Cognition Subspace")
    print("="*80)
    
    # Initialize model
    model = BSplineNN(num_layers=num_layers, 
                     num_control_points=num_control_points,
                     spline_degree=3)
    
    # Initialize trainer
    trainer = BNNTrainer(model, learning_rate=0.001)
    
    # Initialize polarity interval manager
    polarity_mgr = PolarityIntervalManager(num_layers, num_control_points)
    
    # Generate training data
    print("\n[1] Generating synthetic B-spline training data...")
    dataset = SyntheticBSplineDataset(num_samples=100,
                                     num_control_points=num_control_points,
                                     num_curve_points=50)
    
    # Create data loaders
    train_batches = []
    for _ in range(20):  # 20 batches
        batch = dataset.generate_batch(batch_size)
        train_batches.append(batch)
    
    val_batches = []
    for _ in range(5):  # 5 validation batches
        batch = dataset.generate_batch(batch_size)
        val_batches.append(batch)
    
    print(f"   Training samples: {100}")
    print(f"   Validation samples: {25}")
    print(f"   Control points per curve: {num_control_points}")
    print(f"   Network layers: {num_layers}")
    
    # Training loop
    print("\n[2] Starting training...\n")
    best_val_loss = float('inf')
    patience = 10
    patience_counter = 0
    
    for epoch in range(num_epochs):
        # Train
        metrics = trainer.train_epoch(train_batches)
        
        # Validate
        val_loss = trainer.validate(val_batches)
        
        # Update polarity intervals adaptively
        avg_second_passes = metrics['second_pass_ratio']
        for layer in range(num_layers):
            for cp in range(num_control_points):
                polarity_mgr.adaptive_update(layer, cp, avg_second_passes)
        
        # Early stopping
        if val_loss < best_val_loss:
            best_val_loss = val_loss
            patience_counter = 0
        else:
            patience_counter += 1
        
        # Print progress
        if (epoch + 1) % 5 == 0:
            print(f"Epoch {epoch+1:3d}/{num_epochs} | "
                  f"Train Loss: {metrics['loss']:.6f} | "
                  f"Val Loss: {val_loss:.6f} | "
                  f"2nd Pass Ratio: {metrics['second_pass_ratio']:.3f} | "
                  f"Grad Norm: {metrics['gradient_norm']:.4f}")
        
        if patience_counter >= patience:
            print(f"\nEarly stopping at epoch {epoch+1}")
            break
    
    # Final evaluation
    print("\n[3] Final Model Evaluation")
    print("="*80)
    
    test_batch = dataset.generate_batch(batch_size)
    with torch.no_grad():
        u = torch.linspace(0, 1, test_batch[1].shape[1])
        test_output, test_metrics = model(u, test_batch[0])
    
    test_loss = trainer.loss_fn(test_output, test_batch[1]).item()
    
    print(f"\nFinal Test Loss: {test_loss:.6f}")
    print(f"Second-Pass Activations: {sum(test_metrics['second_passes'])}/{num_layers}")
    print(f"Mean Gradient Score: {np.mean(test_metrics['gradient_scores']):.4f}")
    
    # Polarity interval statistics
    print("\n[4] Polarity Interval Statistics")
    print("="*80)
    all_ranges = []
    for layer in range(num_layers):
        for cp in range(num_control_points):
            N_low, N_high = polarity_mgr.intervals[layer][cp]
            all_ranges.append(N_high - N_low)
    
    print(f"Mean Polarity Interval Width: {np.mean(all_ranges):.4f}")
    print(f"Min Interval Width: {np.min(all_ranges):.4f}")
    print(f"Max Interval Width: {np.max(all_ranges):.4f}")
    
    # Meta-commutator statistics
    print("\n[5] Meta-Commutator Recursion Statistics")
    print("="*80)
    total_children = sum([len(mc.child_commutators) 
                         for mc in model.meta_commutators])
    print(f"Total Recursive Meta-Commutator Generations: {total_children}")
    print(f"Child Commutators Created: {total_children}/{num_layers}")
    
    # Training history
    print("\n[6] Training History Summary")
    print("="*80)
    print(f"Final Training Loss: {trainer.training_history['loss'][-1]:.6f}")
    print(f"Final Second-Pass Ratio: {trainer.training_history['second_pass_ratio'][-1]:.4f}")
    print(f"Final Gradient Norm: {trainer.training_history['gradient_norm'][-1]:.4f}")
    
    return model, trainer, polarity_mgr

# ============================================================================
# INFERENCE AND VISUALIZATION
# ============================================================================

def inference_example(model: BSplineNN, num_samples: int = 5):
    """Run inference on example samples"""
    
    print("\n[7] Inference Examples")
    print("="*80)
    
    dataset = SyntheticBSplineDataset(num_samples=num_samples,
                                     num_control_points=10,
                                     num_curve_points=50)
    
    model.eval()
    
    with torch.no_grad():
        for sample_idx in range(num_samples):
            control, target = dataset.generate_sample()
            control_tensor = torch.tensor(control, dtype=torch.float32).unsqueeze(0)
            
            u = torch.linspace(0, 1, target.shape[0])
            predicted, metrics = model(u, control_tensor)
            
            # Compute error
            error = np.linalg.norm(predicted[0].numpy() - target)
            
            print(f"\nSample {sample_idx+1}:")
            print(f"  Prediction Error: {error:.6f}")
            print(f"  Second Passes: {sum(metrics['second_passes'])}")
            print(f"  Output Shape: {predicted.shape}")
            print(f"  Target Shape: {target.shape}")

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    
    # Train the model
    model, trainer, polarity_mgr = train_bnn_system(
        num_epochs=100,
        batch_size=8,
        num_layers=3,
        num_control_points=10
    )
    
    # Run inference examples
    inference_example(model, num_samples=5)
    
    print("\n" + "="*80)
    print("TRAINING COMPLETE")
    print("="*80)
    
    # Save model
    torch.save(model.state_dict(), 'bnn_model.pt')
    print("\nModel saved to 'bnn_model.pt'")
    
    # Additional: Meta-commutator inspection
    print("\n[8] Meta-Commutator Inspection")
    print("="*80)
    for layer_idx, mc in enumerate(model.meta_commutators):
        print(f"Layer {layer_idx}: {mc}")
        print(f"  R shape: {mc.R.shape}")
        print(f"  Filter Y norm: {torch.norm(mc.filter_y).item():.4f}")
        print(f"  Filter Z norm: {torch.norm(mc.filter_z).item():.4f}")
        print(f"  Child commutators: {len(mc.child_commutators)}")

#======================================================================
#======================================================================

# rev9_bnn_rnsl_visualization.py
"""
Advanced visualization and analysis tools for B-spline Neural Network
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import torch

class BNNVisualizer:
    """Visualization tools for BNN training and inference"""
    
    def __init__(self, trainer: 'BNNTrainer'):
        self.trainer = trainer
        
    def plot_training_history(self, save_path: str = 'bnn_training.png'):
        """Plot training loss, second-pass ratio, and gradient norms"""
        fig, axes = plt.subplots(1, 3, figsize=(15, 4))
        
        # Loss
        axes[0].plot(self.trainer.training_history['loss'], linewidth=2)
        axes[0].set_xlabel('Epoch')
        axes[0].set_ylabel('Loss')
        axes[0].set_title('Training Loss Over Time')
        axes[0].grid(True, alpha=0.3)
        
        # Second-pass ratio
        axes[1].plot(self.trainer.training_history['second_pass_ratio'], 
                    linewidth=2, color='orange')
        axes[1].set_xlabel('Epoch')
        axes[1].set_ylabel('Second-Pass Activation Ratio')
        axes[1].set_title('Meta-Commutator Activation Rate')
        axes[1].grid(True, alpha=0.3)
        axes[1].set_ylim([0, 1])
        
        # Gradient norm
        axes[2].plot(self.trainer.training_history['gradient_norm'], 
                    linewidth=2, color='green')
        axes[2].set_xlabel('Epoch')
        axes[2].set_ylabel('Mean Gradient Norm')
        axes[2].set_title('RNSL Gradient Score Evolution')
        axes[2].grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=150)
        print(f"Training history plot saved to {save_path}")
        
    def plot_3d_curve_comparison(self, predicted: np.ndarray, 
                                target: np.ndarray,
                                save_path: str = 'bnn_3d_curves.png'):
        """Plot predicted vs target 3D curves"""
        fig = plt.figure(figsize=(12, 5))
        
        # Predicted curve
        ax1 = fig.add_subplot(121, projection='3d')
        if predicted.shape[1] == 3:
            ax1.plot(predicted[:, 0], predicted[:, 1], predicted[:, 2], 
                    'b-', linewidth=2, label='Predicted')
        ax1.set_xlabel('X')
        ax1.set_ylabel('Y')
        ax1.set_zlabel('Z')
        ax1.set_title('Predicted Curve')
        ax1.legend()
        
        # Target curve
        ax2 = fig.add_subplot(122, projection='3d')
        if target.shape[1] == 3:
            ax2.plot(target[:, 0], target[:, 1], target[:, 2], 
                    'r-', linewidth=2, label='Target')
        ax2.set_xlabel('X')
        ax2.set_ylabel('Y')
        ax2.set_zlabel('Z')
        ax2.set_title('Target Curve')
        ax2.legend()
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=150)
        print(f"3D curve comparison saved to {save_path}")
    
    def plot_node_distributions(self, model: 'BSplineNN',
                               save_path: str = 'bnn_nodes.png'):
        """Plot rotational node distributions across layers"""
        fig, axes = plt.subplots(1, model.num_layers, figsize=(15, 4))
        
        for layer_idx, bspline_layer in enumerate(model.bspline_layers):
            scores = []
            probs = []
            
            for node_pair in bspline_layer.node_pairs:
                for node in node_pair:
                    score = abs(node.get_complex_score())
                    scores.append(score)
                    probs.append(node.node_prob)
            
            axes[layer_idx].scatter(probs, scores, alpha=0.6)
            axes[layer_idx].set_xlabel('Node Probability')
            axes[layer_idx].set_ylabel('Complex Score Magnitude')
            axes[layer_idx].set_title(f'Layer {layer_idx} Nodes')
            axes[layer_idx].grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=150)
        print(f"Node distribution plot saved to {save_path}")

# ============================================================================
# ADVANCED ANALYSIS: ROTATIONAL NODE DYNAMICS
# ============================================================================

class RotationalNodeAnalyzer:
    """Analyze rotational node behavior across training"""
    
    def __init__(self, model: 'BSplineNN'):
        self.model = model
        self.rotation_history = {layer: [] for layer in range(model.num_layers)}
        self.probability_history = {layer: [] for layer in range(model.num_layers)}
        
    def capture_state(self):
        """Capture current state of all nodes"""
        for layer_idx, bspline_layer in enumerate(self.model.bspline_layers):
            layer_rotations = []
            layer_probs = []
            
            for node_pair in bspline_layer.node_pairs:
                for node in node_pair:
                    # Capture rotation angles
                    rotation_norm = np.linalg.norm(node.rotation_angles)
                    layer_rotations.append(rotation_norm)
                    layer_probs.append(node.node_prob)
            
            self.rotation_history[layer_idx].append(np.mean(layer_rotations))
            self.probability_history[layer_idx].append(np.mean(layer_probs))
    
    def analyze_rotational_coupling(self) -> Dict[str, float]:
        """Analyze coupling between rotational nodes in adjacent pairs"""
        coupling_scores = {}
        
        for layer_idx, bspline_layer in enumerate(self.model.bspline_layers):
            couplings = []
            
            for node_pair in bspline_layer.node_pairs:
                if len(node_pair) == 2:
                    # Measure angular similarity between paired nodes
                    angles1 = node_pair[0].rotation_angles
                    angles2 = node_pair[1].rotation_angles
                    
                    # Cosine similarity
                    dot_product = np.dot(angles1, angles2)
                    norm1 = np.linalg.norm(angles1)
                    norm2 = np.linalg.norm(angles2)
                    
                    if norm1 > 1e-6 and norm2 > 1e-6:
                        similarity = dot_product / (norm1 * norm2)
                        couplings.append(similarity)
            
            if couplings:
                coupling_scores[f'layer_{layer_idx}'] = np.mean(couplings)
        
        return coupling_scores
    
    def print_analysis(self):
        """Print comprehensive node analysis"""
        print("\n" + "="*80)
        print("ROTATIONAL NODE DYNAMICS ANALYSIS")
        print("="*80)
        
        for layer_idx in range(self.model.num_layers):
            if self.rotation_history[layer_idx]:
                rotations = self.rotation_history[layer_idx]
                probs = self.probability_history[layer_idx]
                
                print(f"\nLayer {layer_idx}:")
                print(f"  Mean Rotation Norm: {np.mean(rotations):.6f}")
                print(f"  Mean Node Probability: {np.mean(probs):.4f}")
                print(f"  Rotation Std Dev: {np.std(rotations):.6f}")
        
        # Coupling analysis
        coupling = self.analyze_rotational_coupling()
        print(f"\nRotational Node Pair Coupling:")
        for layer, score in coupling.items():
            print(f"  {layer}: {score:.4f}")

# ============================================================================
# GRADIENT MATCHING & CURVATURE SET ANALYSIS
# ============================================================================

class CurvatureSetMatcher:
    """Analyze and match curvature sets to rotational nodes"""
    
    def __init__(self, model: 'BSplineNN'):
        self.model = model
        self.curvature_sets = {}
        
    def compute_curvature_signature(self, curve: np.ndarray, 
                                   num_segments: int = 10) -> np.ndarray:
        """
        Compute curvature signature by dividing curve into segments
        and computing local curvature in each
        """
        segment_length = len(curve) // num_segments
        signatures = []
        
        for i in range(num_segments):
            start = i * segment_length
            end = start + segment_length
            segment = curve[start:end]
            
            if len(segment) >= 3:
                # Central difference curvature
                d1 = np.diff(segment, axis=0)
                d2 = np.diff(d1, axis=0)
                
                cross = np.cross(d1[:-1], d2)
                curvature = np.mean(np.linalg.norm(cross, axis=1))
                signatures.append(curvature)
        
        return np.array(signatures)
    
    def match_to_nodes(self, curvature_signature: np.ndarray) -> Dict:
        """Match curvature signature to best-matching rotational nodes"""
        matches = {}
        
        for layer_idx, bspline_layer in enumerate(self.model.bspline_layers):
            best_match_idx = None
            best_error = float('inf')
            
            # Compare against all node pairs in this layer
            node_idx = 0
            for node_pair in bspline_layer.node_pairs:
                for node in node_pair:
                    # Use node's stored complex score as signature proxy
                    node_score = abs(node.get_complex_score())
                    node_prob = node.node_prob
                    
                    # Match error: difference in characteristics
                    if len(curvature_signature) > 0:
                        mean_curvature = np.mean(curvature_signature)
                        error = abs(node_score - mean_curvature)
                        
                        if error < best_error:
                            best_error = error
                            best_match_idx = node_idx
                    
                    node_idx += 1
            
            matches[f'layer_{layer_idx}'] = {
                'node_index': best_match_idx,
                'match_error': best_error
            }
        
        return matches

# ============================================================================
# COMPLETE INTEGRATION: FULL PIPELINE WITH ANALYSIS
# ============================================================================

def run_complete_bnn_pipeline():
    """
    Run complete B-spline neural network pipeline with all features:
    - Training
    - Validation
    - Visualization
    - Node analysis
    - Curvature matching
    """
    
    print("\n" + "█"*80)
    print("█" + " "*78 + "█")
    print("█" + "  COMPLETE B-SPLINE NEURAL NETWORK PIPELINE  ".center(78) + "█")
    print("█" + "  Multi-Layered Rotational Nodes | 3D Residual Cognition  ".center(78) + "█")
    print("█" + " "*78 + "█")
    print("█"*80)
    
    # ====== PHASE 1: MODEL INITIALIZATION ======
    print("\n[PHASE 1] Model Initialization")
    print("-" * 80)
    
    model = BSplineNN(num_layers=4, num_control_points=12, spline_degree=3)
    trainer = BNNTrainer(model, learning_rate=0.001)
    polarity_mgr = PolarityIntervalManager(4, 12)
    analyzer = RotationalNodeAnalyzer(model)
    curvature_matcher = CurvatureSetMatcher(model)
    
    print(f"✓ Model initialized with 4 layers, 12 control points each")
    print(f"✓ Total parameters: {sum(p.numel() for p in model.parameters())}")
    
    # ====== PHASE 2: DATA GENERATION ======
    print("\n[PHASE 2] Synthetic Data Generation")
    print("-" * 80)
    
    dataset = SyntheticBSplineDataset(num_samples=150,
                                     num_control_points=12,
                                     num_curve_points=60)
    
    train_batches = [dataset.generate_batch(8) for _ in range(25)]
    val_batches = [dataset.generate_batch(8) for _ in range(8)]
    
    print(f"✓ Generated {150} training samples")
    print(f"✓ Generated {64} validation samples")
    print(f"✓ Batch size: 8")
    
    # ====== PHASE 3: TRAINING LOOP ======
    print("\n[PHASE 3] Training Loop (50 epochs)")
    print("-" * 80)
    
    num_epochs = 50
    best_val_loss = float('inf')
    patience_counter = 0
    
    for epoch in range(num_epochs):
        metrics = trainer.train_epoch(train_batches)
        val_loss = trainer.validate(val_batches)
        analyzer.capture_state()
        
        # Adaptive polarity update
        for layer in range(4):
            for cp in range(12):
                polarity_mgr.adaptive_update(layer, cp, metrics['second_pass_ratio'])
        
        # Print progress
        if (epoch + 1) % 10 == 0:
            status = "→" if val_loss < best_val_loss else "↗"
            print(f"{status} Epoch {epoch+1:3d} | "
                  f"Loss: {metrics['loss']:.6f} | "
                  f"Val: {val_loss:.6f} | "
                  f"2Pass: {metrics['second_pass_ratio']:.3f}")
            
            if val_loss < best_val_loss:
                best_val_loss = val_loss
                patience_counter = 0
            else:
                patience_counter += 1
        
        if patience_counter >= 8:
            print(f"\n⚠ Early stopping at epoch {epoch+1}")
            break
    
    # ====== PHASE 4: INFERENCE & EVALUATION ======
    print("\n[PHASE 4] Inference & Evaluation")
    print("-" * 80)
    
    model.eval()
    test_batch = dataset.generate_batch(8)
    
    with torch.no_grad():
        u = torch.linspace(0, 1, test_batch[1].shape[1])
        test_output, test_metrics = model(u, test_batch[0])
    
    test_loss = trainer.loss_fn(test_output, test_batch[1]).item()
    
    print(f"✓ Test Loss: {test_loss:.6f}")
    print(f"✓ Second-Pass Activations: {sum(test_metrics['second_passes'])}/4")
    print(f"✓ Mean Gradient Score: {np.mean(test_metrics['gradient_scores']):.4f}")
    
    # ====== PHASE 5: VISUALIZATION ======
    print("\n[PHASE 5] Generating Visualizations")
    print("-" * 80)
    
    visualizer = BNNVisualizer(trainer)
    visualizer.plot_training_history()
    visualizer.plot_node_distributions(model)
    
    # Plot example predictions
    pred_np = test_output[0].numpy()
    target_np = test_batch[1][0].numpy()
    visualizer.plot_3d_curve_comparison(pred_np, target_np)
    
    # ====== PHASE 6: ROTATIONAL NODE ANALYSIS ======
    print("\n[PHASE 6] Rotational Node Dynamics Analysis")
    print("-" * 80)
    
    analyzer.print_analysis()
    
    # ====== PHASE 7: CURVATURE MATCHING ======
    print("\n[PHASE 7] Curvature Set Matching Analysis")
    print("-" * 80)
    
    # Test on a sample curve
    test_control, test_curve = dataset.generate_sample()
    curvature_sig = curvature_matcher.compute_curvature_signature(test_curve)
    matches = curvature_matcher.match_to_nodes(curvature_sig)
    
    print(f"✓ Computed curvature signature with {len(curvature_sig)} segments")
    print(f"✓ Curvature signature mean: {np.mean(curvature_sig):.6f}")
    print(f"✓ Curvature signature std: {np.std(curvature_sig):.6f}")
    print(f"\nBest-matching nodes per layer:")
    for layer, match_info in matches.items():
        print(f"  {layer}: Node {match_info['node_index']} "
              f"(error: {match_info['match_error']:.6f})")
    
    # ====== PHASE 8: META-COMMUTATOR STATISTICS ======
    print("\n[PHASE 8] Meta-Commutator Recursion Analysis")
    print("-" * 80)
    
    total_generations = 0
    total_children = 0
    
    for layer_idx, mc in enumerate(model.meta_commutators):
        num_children = len(mc.child_commutators)
        total_children += num_children
        max_gen = mc.generation
        
        if num_children > 0:
            max_gen = max([child.generation for child in mc.child_commutators])
        
        print(f"Layer {layer_idx}:")
        print(f"  ├─ Current generation: {mc.generation}")
        print(f"  ├─ Child commutators: {num_children}")
        print(f"  ├─ Filter Y magnitude: {torch.norm(mc.filter_y).item():.6f}")
        print(f"  ├─ Filter Z magnitude: {torch.norm(mc.filter_z).item():.6f}")
        print(f"  └─ R matrix rank: {torch.linalg.matrix_rank(mc.R).item()}")
    
    print(f"\n✓ Total recursive generations: {total_children}")
    
    # ====== PHASE 9: POLARITY INTERVAL STATISTICS ======
    print("\n[PHASE 9] Polarity Interval Adaptation Statistics")
    print("-" * 80)
    
    all_widths = []
    layer_stats = {}
    
    for layer in range(4):
        widths = []
        for cp in range(12):
            N_low, N_high = polarity_mgr.intervals[layer][cp]
            width = N_high - N_low
            widths.append(width)
            all_widths.append(width)
        
        layer_stats[layer] = {
            'mean': np.mean(widths),
            'min': np.min(widths),
            'max': np.max(widths),
            'std': np.std(widths)
        }
    
    print(f"Overall polarity interval statistics:")
    print(f"  ├─ Mean width: {np.mean(all_widths):.6f}")
    print(f"  ├─ Min width: {np.min(all_widths):.6f}")
    print(f"  ├─ Max width: {np.max(all_widths):.6f}")
    print(f"  └─ Std deviation: {np.std(all_widths):.6f}")
    
    print(f"\nPer-layer polarity statistics:")
    for layer, stats in layer_stats.items():
        print(f"  Layer {layer}: μ={stats['mean']:.4f}, "
              f"σ={stats['std']:.4f}, "
              f"range=[{stats['min']:.4f}, {stats['max']:.4f}]")
    
    # ====== PHASE 10: TRAINING HISTORY SUMMARY ======
    print("\n[PHASE 10] Training History Summary")
    print("-" * 80)
    
    hist = trainer.training_history
    print(f"Final epoch metrics:")
    print(f"  ├─ Training loss: {hist['loss'][-1]:.6f}")
    print(f"  ├─ Second-pass ratio: {hist['second_pass_ratio'][-1]:.4f}")
    print(f"  ├─ Mean gradient norm: {hist['gradient_norm'][-1]:.6f}")
    print(f"  └─ Total epochs trained: {len(hist['loss'])}")
    
    improvement = (hist['loss'][0] - hist['loss'][-1]) / hist['loss'][0] * 100
    print(f"\n✓ Loss improvement: {improvement:.2f}%")
    
    # ====== PHASE 11: EFFICIENCY METRICS ======
    print("\n[PHASE 11] Network Efficiency Metrics")
    print("-" * 80)
    
    # Count total trainable parameters
    total_params = sum(p.numel() for p in model.parameters())
    print(f"Network architecture:")
    print(f"  ├─ Total parameters: {total_params:,}")
    print(f"  ├─ Layers: 4")
    print(f"  ├─ Control points per layer: 12")
    print(f"  ├─ Nodes per control point: 2")
    print(f"  └─ Total nodes: {4 * 12 * 2}")
    
    # Compute gradient sparsity
    with torch.no_grad():
        total_grads = 0
        active_grads = 0
        for p in model.parameters():
            if p.grad is not None:
                total_grads += p.grad.numel()
                active_grads += (p.grad.abs() > 1e-6).sum().item()
    
    if total_grads > 0:
        sparsity = (1 - active_grads / total_grads) * 100
        print(f"\nGradient sparsity: {sparsity:.2f}%")
    
    # ====== PHASE 12: MODEL CHECKPOINTING ======
    print("\n[PHASE 12] Model Saving & Checkpointing")
    print("-" * 80)
    
    # Save model state
    torch.save(model.state_dict(), 'bnn_model_state.pt')
    print(f"✓ Model state saved to 'bnn_model_state.pt'")
    
    # Save full model
    torch.save(model, 'bnn_model_full.pt')
    print(f"✓ Full model saved to 'bnn_model_full.pt'")
    
    # Save training metadata
    metadata = {
        'num_layers': 4,
        'num_control_points': 12,
        'spline_degree': 3,
        'num_epochs': len(hist['loss']),
        'final_loss': hist['loss'][-1],
        'total_params': total_params,
        'best_val_loss': best_val_loss
    }
    
    import json
    with open('bnn_metadata.json', 'w') as f:
        json.dump(metadata, f, indent=2)
    print(f"✓ Training metadata saved to 'bnn_metadata.json'")
    
    # ====== FINAL SUMMARY ======
    print("\n" + "█"*80)
    print("█" + " "*78 + "█")
    print("█" + "  PIPELINE EXECUTION COMPLETE  ".center(78) + "█")
    print("█" + " "*78 + "█")
    print("█"*80)
    
    print("\n📊 Summary Statistics:")
    print(f"  • Training samples processed: 1,200 (25 batches × 8 × 50 epochs)")
    print(f"  • Model convergence: {improvement:.2f}% loss improvement")
    print(f"  • Meta-commutator activations: {sum(test_metrics['second_passes'])}/4 layers")
    print(f"  • Rotational node pairs: {4 * 12 * 2}")
    print(f"  • Adaptive polarity intervals: 48")
    print(f"  • Curvature set segments: {len(curvature_sig)}")
    
    print("\n📁 Output Files Generated:")
    print(f"  • bnn_training.png - Training history plots")
    print(f"  • bnn_nodes.png - Node distribution visualizations")
    print(f"  • bnn_3d_curves.png - Predicted vs target curves")
    print(f"  • bnn_model_state.pt - Model weights & parameters")
    print(f"  • bnn_model_full.pt - Complete model checkpoint")
    print(f"  • bnn_metadata.json - Training metadata")
    
    return model, trainer, analyzer, polarity_mgr, curvature_matcher

# ============================================================================
# ADVANCED: RECURSIVE META-COMMUTATOR DEPTH EXPLORATION
# ============================================================================

def analyze_recursive_depth(model: BSplineNN, max_depth: int = 5):
    """
    Analyze the depth of recursive meta-commutator generations
    and their impact on network performance
    """
    print("\n" + "="*80)
    print("RECURSIVE META-COMMUTATOR DEPTH ANALYSIS")
    print("="*80)
    
    depth_analysis = {}
    
    for layer_idx, mc in enumerate(model.meta_commutators):
        print(f"\nLayer {layer_idx} Recursion Tree:")
        
        def traverse_commutators(commutator, depth=0, parent_idx=0):
            """Recursively traverse and analyze commutator hierarchy"""
            indent = "  " * depth
            
            if depth not in depth_analysis:
                depth_analysis[depth] = {
                    'count': 0,
                    'total_params': 0,
                    'avg_generation': 0
                }
            
            # Count parameters
            params = sum(p.numel() for p in commutator.parameters())
            depth_analysis[depth]['count'] += 1
            depth_analysis[depth]['total_params'] += params
            depth_analysis[depth]['avg_generation'] += commutator.generation
            
            print(f"{indent}├─ Generation {commutator.generation} | "
                  f"Params: {params} | "
                  f"Children: {len(commutator.child_commutators)}")
            
            # Traverse children
            if len(commutator.child_commutators) > 0 and depth < max_depth:
                for child_idx, child in enumerate(commutator.child_commutators):
                    is_last = (child_idx == len(commutator.child_commutators) - 1)
                    traverse_commutators(child, depth + 1, child_idx)
            
            print(f"{indent}└─ End generation {commutator.generation}")
        
        traverse_commutators(mc)
    
    # Print summary
    print("\n" + "-"*80)
    print("RECURSION DEPTH SUMMARY:")
    print("-"*80)
    
    total_commutators = 0
    total_params_recursive = 0
    
    for depth in sorted(depth_analysis.keys()):
        stats = depth_analysis[depth]
        avg_gen = stats['avg_generation'] / max(stats['count'], 1)
        
        total_commutators += stats['count']
        total_params_recursive += stats['total_params']
        
        print(f"Depth {depth}: {stats['count']:3d} commutators | "
              f"Total params: {stats['total_params']:8d} | "
              f"Avg generation: {avg_gen:.2f}")
    
    print(f"\nTotal recursive meta-commutators: {total_commutators}")
    print(f"Total parameters in recursion: {total_params_recursive:,}")

# ============================================================================
# PERFORMANCE BENCHMARKING
# ============================================================================

def benchmark_inference_speed(model: BSplineNN, num_batches: int = 10):
    """Benchmark inference speed and memory usage"""
    import time
    
    print("\n" + "="*80)
    print("INFERENCE PERFORMANCE BENCHMARK")
    print("="*80)
    
    model.eval()
    
    # Prepare test data
    dataset = SyntheticBSplineDataset(num_samples=10, 
                                     num_control_points=12,
                                     num_curve_points=60)
    
    times = []
    
    with torch.no_grad():
        for batch_idx in range(num_batches):
            control, target = dataset.generate_sample()
            control_tensor = torch.tensor(control, dtype=torch.float32).unsqueeze(0)
            u = torch.linspace(0, 1, target.shape[0])
            
            start_time = time.time()
            output, metrics = model(u, control_tensor)
            elapsed = time.time() - start_time
            
            times.append(elapsed)
    
    print(f"\nInference over {num_batches} samples:")
    print(f"  • Mean time: {np.mean(times)*1000:.3f} ms")
    print(f"  • Std dev: {np.std(times)*1000:.3f} ms")
    print(f"  • Min time: {np.min(times)*1000:.3f} ms")
    print(f"  • Max time: {np.max(times)*1000:.3f} ms")
    print(f"  • Throughput: {1/np.mean(times):.2f} samples/sec")
    
    # Memory estimation
    total_params = sum(p.numel() for p in model.parameters())
    memory_mb = (total_params * 4) / (1024**2)  # 4 bytes per float32
    print(f"\nMemory usage:")
    print(f"  • Total parameters: {total_params:,}")
    print(f"  • Estimated weights size: {memory_mb:.2f} MB")

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    
    # Run complete pipeline
    model, trainer, analyzer, polarity_mgr, curvature_matcher = (
        run_complete_bnn_pipeline()
    )
    
    # Additional analyses
    print("\n")
    analyze_recursive_depth(model, max_depth=3)
    
    print("\n")
    benchmark_inference_speed(model, num_batches=20)
    
    # Final model inspection
    print("\n" + "="*80)
    print("FINAL MODEL ARCHITECTURE")
    print("="*80)
    print(model)
    
    print("\n✅ Complete B-Spline Neural Network pipeline finished successfully!")
    print("All outputs saved to current directory.")
undefined

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[Sign up for free](https://gist.github.com/join?source=comment-gist)**to join this conversation on GitHub**. Already have an account? [Sign in to comment](https://gist.github.com/login?return_to=https%3A%2F%2Fgist.github.com%2Fkarpathy%2F442a6bf555914893e9891c11519de94f)

## Footer

[](https://github.com/) © 2026 GitHub,Inc. 

### Footer navigation

*   [Terms](https://docs.github.com/site-policy/github-terms/github-terms-of-service)
*   [Privacy](https://docs.github.com/site-policy/privacy-policies/github-privacy-statement)
*   [Security](https://github.com/security)
*   [Status](https://www.githubstatus.com/)
*   [Community](https://github.community/)
*   [Docs](https://docs.github.com/)
*   [Contact](https://support.github.com/?tags=dotcom-footer)
*    Manage cookies 
*    Do not share my personal information 

 You can’t perform that action at this time.

# tldr-knowledge-base

A daily digest tool that tracks the latest AI/agentic news on Hacker News, distills what matters, builds a durable Notion knowledge base, and sends a single Telegram digest — automatically, once a day.

## What it does

Every day, via a scheduled GitHub Actions run driving Claude Code:

1. **Fetch** — pulls the day's Hacker News stories from the Algolia API and scrapes full article text with trafilatura.
2. **Shortlist** — narrows the list in two passes: 10 candidates by headline, then 3 by article content.
3. **Summarise** — distills each shortlisted article into a plain-English summary, its key technical concepts, and why it matters.
4. **Update** — pushes durable technical concepts into a Notion knowledge base via the Notion MCP server.
5. **Notify** — sends the finished digest as a single Telegram message (chunked to fit Telegram's message limit).

## How it runs

A GitHub Actions workflow (`.github/workflows/tldr-knowledge-base.yml`) runs daily at 04:00 UTC (and can be triggered manually via `workflow_dispatch`):

1. Installs Python dependencies and the Claude Code CLI.
2. Runs `claude -p "Run today's tech digest per CLAUDE.md"`, which drives the fetch → shortlist → summarise → update-notion pipeline using the skills in `.claude/skills/` and writes the result to `digest.md`.
3. Runs `utils/notifyUtils.py` to send `digest.md` to Telegram.

## Skills

Custom Claude Code skills live in `.claude/skills/`:

- `/shortlist` — two-stage article filtering (headline → content). Inputs: `titles.md`, `articles.md`. Outputs: `shortlisted_titles.md`, `shortlisted_articles.md`.
- `/summarise` — distills a single article into a TL;DR digest.
- `/update-notion` — updates the Notion knowledge base with the technical concepts distilled from the articles.

## Setup

Install dependencies:

```
pip install -r requirements.txt
```

The following secrets/environment variables are required:

- `ANTHROPIC_API_KEY` — for running the Claude Code pipeline.
- `NOTION_TOKEN` — for the Notion MCP server (`.mcp.json`).
- `TELEGRAM_BOT_TOKEN` / `TELEGRAM_CHAT_ID` — for sending the daily digest.

## Key dependencies

- `requests` — HTTP calls to the HN Algolia API and Telegram Bot API.
- `trafilatura` — article scraping/extraction.
- `langchain_text_splitters` — chunks the digest to fit Telegram's message limit.
- `@anthropic-ai/claude-code` — drives the fetch/shortlist/summarise/update pipeline in CI.
- `@notionhq/notion-mcp-server` — Notion MCP server used by the `/update-notion` skill.

## Project status

`main.py` is a stub — the pipeline currently runs end-to-end through the Claude Code CLI invocation in CI rather than a standalone Python entry point.

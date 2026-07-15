# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A daily digest tool that fetches AI/agentic news from Hacker News, shortlists and summarizes the most relevant articles, distills durable concepts into a Notion knowledge base, and sends a single daily notification.

## Pipeline Architecture

The intended end-to-end flow (partially implemented):

1. **Fetch** — `utils/fetchUtils.py` pulls HN stories via the Algolia search API (`fetch_hackernews`) and scrapes article body text via trafilatura (`fetch_article_content`).
2. **Shortlist** — `/shortlist` skill reads `titles.md` → selects 10 by headline → selects 3 by content → writes `shortlisted_titles.md` and `shortlisted_articles.md`.
3. **Summarise** — `/summarise` skill distills each shortlisted article into: plain summary, key technical concepts, why it matters.
4. **Distill** — push durable concepts to Notion (not yet implemented).
5. **Notify** — send a single daily Telegram digest message.

`main.py` is the intended entry point but is currently a stub.

## Skills

Custom Claude Code skills live in `.claude/skills/`:

- `/shortlist` — two-stage article filtering (headline → content). Inputs: `titles.md`, `articles.md`. Outputs: `shortlisted_titles.md`, `shortlisted_articles.md`.
- `/summarise` — distills a single article into a TL;DR.

## Key Dependencies

- `requests` — HTTP calls to the HN Algolia API.
- `trafilatura` — article scraping/extraction.
- `langchain_text_splitters` — Telegram message chunking

## Intermediate Files

Generated markdown files (`titles.md`, `articles.md`, `shortlisted_titles.md`, `shortlisted_articles.md`, `digest.md`) are pipeline artifacts passed between steps, not source. `titles.md` and `test.ipynb` are gitignored.

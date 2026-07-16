---
name: summarise
description: >
  Summarise a tech news article into a TL;DR version.

  Use when:
  - You want to distill the key takeaways and technical concepts from a tech news article into a concise summary.

---

# Summarise

## What You Do

Given 3 shortlisted tech news articles, distill each article into a TL;DR version that captures the key takeaways and technical concepts. The goal is to provide a concise summary that highlights the most important information from each article.

### Inputs

- `shortlisted_articles.md`: a markdown file containing the contents of the shortlisted articles, separated by a `---` line.

### Outputs

- `digest.md`: a markdown file containing the TL;DR summaries of the shortlisted articles, separated by a `---` line.

## Key Summary Content

1. Plain summary of the article.
2. Key technical concepts discussed in the article.
3. Explanation of why the article matters and its potential impact.

## Template

Generate a single markdown file `digest.md` in the project root containing the TL;DR summaries of the 3 articles, each separated by a `---` line. See `.claude/skills/summarise/template/digest_template.md` for the template to use when generating the TL;DR summaries.

## Summary Constraints

- Keep the summary concise. This summary is to be read within a Telegram message, so it should be brief and to the point.
- Telegram messages have a character limit of 4096 characters. As a rule of thumb, try to keep the entire summary under 30 sentences.

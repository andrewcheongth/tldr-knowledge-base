---
name: summarise
description: >
  Summarise a tech news article into a TL;DR digest.

  Use when:
  - You want to distill the key takeaways and technical concepts from a tech news article into a concise summary.

---

# Summarise

## What You Do

Given 3 shortlisted tech news articles, distill each article into a TL;DR digest that captures the key takeaways and technical concepts. The goal is to provide a concise summary that highlights the most important information from each article.

### Inputs

- `shortlisted_articles.md`: a markdown file containing the contents of the shortlisted articles, separated by a `---` line.

### Outputs

- `digest.md`: a markdown file containing the TL;DR digest of the shortlisted articles, separated by a `---` line.

## Key Content Sections

1. **Summary** — Plain summary of the article.
2. **Key Concepts** — Key technical concepts discussed in the article.
3. **Why It Matters** — Explanation of why the article matters and its potential impact.

## Template

Generate a single markdown file `digest.md` in the project root containing the TL;DR digest of the 3 articles, each separated by a `---` line. Generate the digest using the following template.

```markdown
# Tech Digest — <DD MMM YYYY>

## 1. <Article 1 Title>

**Summary:**
[Summary of the article, capturing the key takeaways and technical concepts.]

**Key Concepts:**
- [Concept 1]
- [Concept 2]
- [Concept 3]

**Why It Matters:**
[Explanation of why the article matters and its potential impact.]

---

## 2. <Article 2 Title>

...

---

## 3. <Article 3 Title>

...

```

## Guidance

- Aim for parsimony and avoid unnecessary verbosity. This digest is to be read within a Telegram message, so it should be brief and to the point.
- The **summary** section should aim to capture a reader's short attention span — keep it punchy and engaging.
- Telegram messages have a character limit of 4096 characters. As a rule of thumb, try to keep the entire digest under 30 sentences.
- Insert emojis wherever appropriate to make the digest more engaging and visually appealing.

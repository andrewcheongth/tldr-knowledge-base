---
name: shortlist
description: >
  Shortlist tech news articles for summary.

  Use when:
  - You have a long list of news article metadata and want to narrow it down to 10 based on their headlines.
  - You are given the contents of 10 tech news articles and want to select 3 of the most pertinent ones for summarisation.
---

# Shortlist

## What You Do

Given a list of tech news articles, shortlist the most relevant ones based on their headlines, followed by a second round of shortlisting based on the contents of the articles. The goal is to narrow down the list to 3 articles for summarisation.

### Inputs

- `titles.md`: a markdown file containing the titles of the articles, one per line.
- `articles.md`: a markdown file containing the contents of the articles, separated by a `---` line.

### Outputs

- `shortlisted_titles.md`: a markdown file containing the titles of the shortlisted articles, one per line.
- `shortlisted_articles.md`: a markdown file containing the contents of the shortlisted articles, separated by a `---` line.

## 1. Shortlist based on headlines

Parse the `titles.md` file and select the 10 most relevant articles based on their headlines. Save the shortlisted titles in `shortlisted_titles.md`.

Return the numeric IDs (the number before the |), not the titles themselves, as a JSON array ranked from most to least significant. Write your output to `shortlist.json` in the repo root, containing exactly {"shortlist": [...]}, using the Write tool. Do not include any other commentary in that file.

## 2. Shortlist based on article contents

Parse the `articles.md` file and select the 3 most relevant articles based on their contents. Save the shortlisted articles in `shortlisted_articles.md`, separated by a `---` line.

```markdown
<Article 1>

---

<Article 2>

---

<Article 3>
```

## Selection Criteria

- Relevance to the user's interests or the specified topic.
- Impactfulness of the reported development implied by the headline or article content.
- Reliability of the source, if known.

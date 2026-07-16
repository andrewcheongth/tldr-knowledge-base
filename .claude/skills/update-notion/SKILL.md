---
name: update-notion
description: >
  Update a Notion page with the latest tech news articles.

  Use when:
  - You want to update a Notion page with the latest tech news articles, distilling the key takeaways and technical concepts from each article to build a coherent and informative knowledge base.

---

# Update Notion

## What You Do

Given 3 shortlisted tech news articles, distill the key takeaways and technical concepts from each article and update a Notion page with the information. The goal is to build a coherent and informative knowledge base from the daily contributions of these articles.

### Inputs

- `shortlisted_articles.md`: a markdown file containing the contents of the shortlisted articles, separated by a `---` line.

### Outputs

- Harness Engineering for Coding Agents Notion page: a knowledge base containing the distilled key takeaways and technical concepts from the shortlisted articles, structured in a clear and organized manner.

## Notion MCP

You are given access to the Notion MCP, which grants you read, update, and insert permissions for the Harness Engineering for Coding Agents Notion page.

## Notion Page Structure

The Notion page should be structured like a textbook with clear chapters and sections for each distinct concept. The key technical concepts should be distilled from the articles and organised under the appropriate chapters and sections.

The recommended hierarchy of headings are as follows:

```
Harness Engineering for Coding Agents
├── Part I
│   ├── Chapter 1
│   │   ├── Subchapter 1.1
│   │   └── Subchapter 1.2
│   └── Chapter 2
├── Part II
│   └── Chapter 3
├── (more parts / chapters as needed)
└── Appendices
    ├── Appendix A
    └── Appendix B
```

## Guidance

- You are not required to reference the article for each concept. Simply add the URL to the reference appendix.
- Aim for parsimony and avoid unnecessary verbosity.
- Consider the best way to present the technical concept (e.g. lists, tables, code blocks, equation blocks, tree diagrams, etc.)
- Remember to change the "Last updated" tag to the latest date and time according to the format `<day of week> <DD MMM YYYY> <HH:MM in SGT>` in the Notion page.

## Constraints

- Refrain from radical modifications to the Notion page's existing structure, unless there is a clear way to improve it.

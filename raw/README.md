# Raw Sources — Reference Library

Curated, permanent source documents. The LLM reads from here but never modifies these files.

## Structure

Organize by type. Adapt the subfolders to your needs:

```
raw/
├── exec-comms/       Board decks, leadership Q&As, strategy docs
├── roadmaps/         PRDs, roadmap documents, sprint plans
├── customer/         Customer calls, feedback, support tickets
├── engineering/      Architecture docs, tech specs, ADRs
├── governance/       Policies, compliance, security frameworks
├── metrics/          Adoption data, dashboards, value analyses
├── decks/            Past presentation decks (your own and others') for reference
├── research/         Analyst reports, white papers, market research
└── notes/            Meeting notes, Slack threads, clipped web pages
```

## Conventions

- **Filename**: Use descriptive names. Prefix with date if recency matters: `2026-04-09-quarterly-roadmap.md`
- **Don't edit after filing.** If the source changes, add the new version alongside the old one.
- **Sources vs. inbox**: If you plan to keep a document permanently, file it here. If it's a transient signal to process and discard, put it in `inbox/`.

## How raw sources get here

1. **Direct filing** — you drop a document in the appropriate subfolder
2. **Graduated from inbox/** — an inbox item was processed and deemed worth keeping
3. **Shipped from workspace/** — a completed PRD or decision record moves here for long-term reference

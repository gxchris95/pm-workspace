# Inbox — Signal Queue

Unprocessed inputs waiting to be triaged. Drop stuff here, run skills to process it, then move or delete.

**inbox/ is not raw/.** raw/ is a curated reference library (permanent). inbox/ is a transient processing queue.

## Structure

```
inbox/
├── slack/       Pasted Slack threads
├── jira/        Exported tickets, epics, sprint data
├── meetings/    Meeting notes, recording transcripts
├── surveys/     Survey results, user feedback forms
└── feedback/    Ad-hoc customer/stakeholder feedback
```

## How to use

1. Drop a file in the appropriate subfolder (or just paste content into chat)
2. Run `/intake` — extracts structured requirements
3. Run `/synthesize` (across multiple items) — finds patterns and contradictions
4. Outputs flow to wiki/, workspace/, or raw/ as appropriate
5. Delete or archive the inbox item

## Conventions

- **Filename**: `YYYY-MM-DD-<short-description>.md` (e.g., `2026-04-09-api-latency-complaints.md`)
- **No formatting required** — paste raw content, the skill handles structure
- **Don't curate** — if you're deciding whether something belongs here, just put it in. Curation happens during processing.

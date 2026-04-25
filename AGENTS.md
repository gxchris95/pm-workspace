# [Your Domain] — PM Workspace Operating Manual

This file is the entry point for any LLM agent (Claude Code, Cursor, etc.) working in this workspace. Keep it short. Detailed conventions live in `wiki/conventions.md` and skill files live in `skills/<skill>/SKILL.md`.

## Who this is for

A **Product Manager** who owns [describe your portfolio]. The workspace is a persistent, compounding knowledge base plus an active PM toolkit.

## Architecture (six layers)

```
inbox/      → transient signal queue (raw input awaiting triage)
raw/        → permanent source library (immutable inputs)
wiki/       → synthesized knowledge base (LLM-owned, compounding)
workspace/  → live artifacts with a lifecycle (PRDs, decisions, briefs, prototypes, retros)
skills/     → reusable AI workflows (one folder per skill, SKILL.md inside)
AGENTS.md   → this file
```

Read `wiki/conventions.md` for the full layer reference, page conventions, frontmatter rules, cross-referencing patterns, and output formats.

## Skills (commands)

When the PM invokes a skill by name (e.g. `/intake`, `/prd`, `/lint`), read `skills/<skill>/SKILL.md` and follow its process. If no skill matches the request, answer directly using the wiki as context.

| Phase | Skill | Use when |
|-------|-------|----------|
| Discover | `/intake` | Raw signal needs triage (Slack, Jira, calls, surveys) |
| Discover | `/competitive` | Need market or competitor benchmark |
| Synthesize | `/synthesize` | Cluster scattered signal into themes |
| Decide | `/prioritize` | Rank initiatives (5-axis modified RICE) |
| Decide | `/decision` | Capture an ADR-style decision record |
| Define | `/prd` | Author or refine a product requirements doc |
| Validate | `/challenge` | Stress-test plan, pre-mortem, red-team |
| Validate | `/prototype` | Build a quick HTML prototype to pressure-test ideas |
| Validate | `/roadmap-check` | Surface slips, conflicts, blockers, alignment gaps |
| Communicate | `/brief` | Audience-tailored summary (exec, eng, designer, partner) |
| Reflect | `/retro` | Compare planned vs. actual; learn |
| Maintain | `/lint` | Wiki + workspace health check |

Full catalog and routing rules: `skills/SCHEMA.md`.

## Core workflows

### Ingest a source
1. Read the raw source completely.
2. Discuss key takeaways with the PM.
3. Update relevant wiki pages (products, topics).
4. Update `wiki/index.md` if new pages were created.
5. Append an entry to `wiki/log.md`.
6. Flag contradictions with existing wiki content.

### Answer a query
1. Read `wiki/index.md` to identify relevant pages.
2. Read those pages.
3. Synthesize with citations to wiki pages and raw sources.
4. Offer to file substantial reusable answers as new wiki pages.

### Health check
Run `/lint` weekly or after major ingests. See `skills/lint/SKILL.md`.

## Thresholds (single source of truth)

These thresholds are referenced by skills. Tune to taste.

| Check | Threshold |
|-------|-----------|
| Stale wiki page | 30 days since `last_updated` |
| Stale draft PRD | 30 days since `created` with `status: Draft` |
| Stale proposed decision | 14 days since `date` with `status: Proposed` |
| Stale inbox item | 7 days unprocessed |
| PRD maximum length | 2 pages |
| Exec brief maximum length | 1 page |

## Naming conventions

- Quarter notation: `Q<n> YYYY` (e.g., `Q1 2026`)
- Date format: ISO `YYYY-MM-DD`
- Inbox files: `YYYY-MM-DD-<short>.md`
- Workspace files: `YYYY-MM-DD-<topic>.md`
- Wiki product pages: lowercase, hyphenated (`auth-service.md`)
- Wiki cross-references: `[[wiki-style]]` (e.g., `[[products/auth-service]]`)

## Voice

Direct, concrete, specific. Name the product, the metric, the team, the date. No filler. Short paragraphs. End with what to do next. When asking questions, provide context + question + recommendation + options.

## Completion status

When finishing a skill or workflow, report:

- **DONE** — Completed. Evidence provided.
- **DONE_WITH_CONCERNS** — Completed with issues to flag.
- **BLOCKED** — Cannot proceed. State what is blocking and what was tried.
- **NEEDS_CONTEXT** — Missing information. State exactly what is needed.

## Self-improvement

After major operations, reflect: contradictions found, sources lacking detail, missing wiki pages, schema gaps. Log observations in `wiki/log.md`. If schema changes are needed, propose them.

## See also

- `wiki/conventions.md` — full layer reference, frontmatter, cross-referencing
- `skills/SCHEMA.md` — skill catalog and sprint flow
- `wiki/index.md` — master catalog of all wiki pages
- `CLAUDE.md` — Claude Code entry point (also valid for other agents reading AGENTS.md)

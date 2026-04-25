---
name: lint
description: Health-check the wiki and workspace — contradictions across pages, stale content, missing cross-references, orphan pages, missing product coverage, stale PRDs, and frontmatter compliance. Use this skill whenever the user asks to lint, check the wiki, find inconsistencies, run a health check, audit for staleness, or wants periodic maintenance — typically weekly or after a major ingest.
metadata:
  phase: Maintain
  inputs: [wiki/*, workspace/*, AGENTS.md]
  outputs: [health check report with issues and fixes]
  output_to: inline report (applies fixes with PM approval; logs to wiki/log.md)
---

# Lint — Wiki and Workspace Health Check

## When to use

Periodic maintenance. Run weekly, after major ingests, or when something feels off. This is the quality assurance layer for your entire knowledge system.

Already defined in AGENTS.md as a workflow — this skill provides the detailed checklist.

## Thresholds

Use the values defined in `AGENTS.md` (single source of truth). Defaults if not overridden:

| Check | Threshold |
|-------|-----------|
| Stale wiki page | 30 days since `last_updated` |
| Stale draft PRD | 30 days since `created` with `status: Draft` |
| Stale proposed decision | 14 days since `date` with `status: Proposed` |
| Stale inbox item | 7 days unprocessed |

## Process

### 1. Wiki health

#### Contradictions
Read product pages and topic pages. Flag any place where two pages disagree:

```markdown
### Contradictions Found

| Page A | Page B | Conflict | Suggested Resolution |
|--------|--------|----------|---------------------|
```

#### Stale information
Check `last_updated` frontmatter on all wiki pages. Flag pages past the stale threshold:

```markdown
### Stale Pages

| Page | Last Updated | Days Stale | Likely Cause |
|------|-------------|-----------|-------------|
```

Also check for claims that reference dates in the past: "upcoming in Q1 2026" when Q1 2026 has ended.

**Date sentinel rule**: A `last_updated: YYYY-MM-DD` literal (the unfilled placeholder) should be flagged as `never updated`, not `infinitely stale`. Distinguish these in the report.

#### Missing cross-references
Every dependency should be bidirectional. Topic pages should link to all relevant product pages.

```markdown
### Missing Cross-References

| Page | Should Link To | Reason |
|------|---------------|--------|
```

#### Orphan pages
Pages with no inbound links from any other page.

#### Product coverage
Check if any product mentioned in `raw/` lacks a `wiki/products/` page. Check if any product in `AGENTS.md` taxonomy is missing from `wiki/index.md`.

#### Roadmap currency
Check `wiki/topics/roadmap-timeline.md` for items past their target date without a status update. Run a lightweight `/roadmap-check`.

### 2. Workspace health

#### Stale PRDs
Check `workspace/prds/` for items with `status: Draft` past the stale threshold:

```markdown
### Stale PRDs

| PRD | Created | Days Old | Suggested Action |
|-----|---------|----------|-----------------|
```

#### Orphan decisions
Check `workspace/decisions/` for records with `status: Proposed` past the proposed-decision threshold (decisions should be made or withdrawn).

#### Empty inbox
Check `inbox/` subdirectories. If items have been sitting unprocessed past the inbox threshold, flag them.

### 3. Schema compliance

#### Frontmatter
Every wiki page should have YAML frontmatter with at minimum `last_updated` and `sources`. Product pages need `product`, `status`, `adoption`. Topic pages need `topic`.

```markdown
### Frontmatter Issues

| Page | Missing Fields |
|------|---------------|
```

#### Template compliance
Spot-check 2-3 product pages against `wiki/products/_template.md`. Spot-check 1 topic page against `wiki/topics/_template.md`. Flag missing sections.

#### Skill spec compliance
Optional: run `python scripts/validate.py` and include the output. This validates skill `name`/`description` frontmatter against the agentskills.io spec.

### 4. Produce the report

```markdown
# Lint Report — [DATE]

## Summary
- **Wiki pages checked**: [N]
- **Issues found**: [N] (🔴 [critical] / 🟡 [warning] / 🟢 [info])
- **Auto-fixable**: [N]

## Critical Issues
[must fix — contradictions, broken references, stale claims]

## Warnings
[should fix — stale pages, missing cross-refs, orphan pages]

## Info
[nice to fix — formatting, frontmatter gaps, style inconsistencies]

## Auto-Fix Candidates
[issues the LLM can fix immediately with PM approval]
| # | Issue | Fix | Apply? |
|---|-------|-----|--------|
```

### 5. Apply fixes (with approval)

For each auto-fixable issue, ask the PM before applying. Group simple fixes (frontmatter updates, cross-reference additions) and apply in batch if approved.

After applying fixes, update `wiki/log.md` with a lint entry.

## Tips

- Lint is most valuable when it's boring. If every lint run surfaces emergencies, something upstream is broken.
- Don't fix contradictions by averaging. Surface them for PM decision — one side is usually wrong or outdated.
- Stale pages that nobody asks about might be candidates for deletion, not repair.
- Run lint after every major ingest to catch integration issues early.

## See also

- `/roadmap-check` — deeper roadmap-specific validation
- `/synthesize` — when lint surfaces contradictions worth investigating
- `/intake` — process any stale inbox items found during lint

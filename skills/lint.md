---
skill: lint
trigger: /lint
phase: Maintain
inputs: [wiki/*, workspace/*, AGENTS.md]
outputs: [health check report with issues and fixes]
output_to: [inline report — applies fixes with PM approval]
---

# Lint — Wiki and Workspace Health Check

## When to use

Periodic maintenance. Run weekly, after major ingests, or when something feels off. This is the quality assurance layer for your entire knowledge system.

Already defined in AGENTS.md as a workflow — this skill provides the detailed checklist.

## Process

### 1. Wiki health

#### Contradictions
Read product pages, pillar pages, and topic pages. Flag any place where two pages disagree:

```markdown
### Contradictions Found

| Page A | Page B | Conflict | Suggested Resolution |
|--------|--------|----------|---------------------|
```

#### Stale information
Check `last_updated` frontmatter on all wiki pages. Flag pages not updated in 30+ days:

```markdown
### Stale Pages (not updated in 30+ days)

| Page | Last Updated | Days Stale | Likely Cause |
|------|-------------|-----------|-------------|
```

Check for claims that reference dates in the past: "upcoming in Q1" when Q1 has ended.

#### Missing cross-references
Every product page should link to its pillar. Every pillar should link to its products. Every dependency should be bidirectional.

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
Check `workspace/prds/` for items with `status: Draft` older than 30 days:

```markdown
### Stale PRDs

| PRD | Created | Days Old | Suggested Action |
|-----|---------|----------|-----------------|
```

#### Orphan decisions
Check `workspace/decisions/` for records with `status: Proposed` older than 14 days (decisions should be made or withdrawn).

#### Empty inbox
Check `inbox/` subdirectories. If items have been sitting unprocessed for 7+ days, flag them.

### 3. Schema compliance

#### Frontmatter
Every wiki page should have YAML frontmatter with at minimum `last_updated` and `sources`. Product pages need `product`, `pillar`, `status`, `adoption`.

```markdown
### Frontmatter Issues

| Page | Missing Fields |
|------|---------------|
```

#### Template compliance
Spot-check 2-3 product pages against the template in `AGENTS.md`. Flag missing sections.

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

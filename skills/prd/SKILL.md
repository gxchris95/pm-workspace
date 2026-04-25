---
name: prd
description: Generate or review a Product Requirements Document. Use this skill whenever the user asks to write, draft, scope, spec, or review a PRD, product spec, or feature document. Generation mode produces a complete PRD with problem, solution, scope, requirements, dependencies, risks, timeline, and the SVPG four risks. Review mode produces a 10-dimension scorecard with specific gap callouts. Triggers also include "spec out X", "write requirements for", "review this PRD".
metadata:
  phase: Specify
  inputs: [intake card, synthesis theme, or freeform description]
  outputs: [PRD draft in workspace/prds/]
  output_to: workspace/prds/<product-name>-<feature>.md
---

# PRD — Generate or Review a Product Requirements Document

## When to use

You have a validated requirement (from `/intake` or `/synthesize`) and need to turn it into a spec. Or you have an existing PRD and want a completeness review.

## Mode 1: Generate a PRD

### 1. Read existing formats

Scan `raw/roadmaps/` and `workspace/prds/` for format reference. Match the existing style, depth, and structure used by the team's real PRDs.

### 2. Gather context

Read relevant wiki pages:
- Product page (`wiki/products/<product>.md`) — status, capabilities, dependencies
- Roadmap timeline — where this fits
- Dependencies page — external blockers

### 3. Write the PRD

```markdown
---
title: [Feature / Product Name]
product: [which product this belongs to]
author: [PM name]
status: Draft
created: YYYY-MM-DD
target: Q<n> YYYY
sources: [intake cards, wiki pages, raw sources that informed this]
---

# [Feature / Product Name]

## Problem Statement
What pain exists today. Who feels it. How bad it is. Evidence (quotes, data, intake cards).

## Proposed Solution
What we're building. 2-3 sentences, plain language, no implementation detail.

## Goals & Success Metrics
- Goal 1 → Metric (measurable, with target)
- Goal 2 → Metric

## Scope
### In scope
### Out of scope
### Non-goals

## Requirements
### P0 (must-have for launch)
### P1 (needed soon after)
### P2 (future)

## User Flows
How users interact with this. Step by step.

## Dependencies
- What this depends on (internal products, external teams, infrastructure)
- What depends on this (downstream products, teams waiting)

## Risks
| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|

## Timeline
| Phase | Target | Deliverables |
|-------|--------|-------------|

## Open Questions
Numbered list. Each should have: the question, why it matters, who can answer it.

## Stakeholders
Who needs to review or approve this. Who's informed.
```

### 4. Cross-reference

- Check `workspace/prds/` for related in-flight PRDs — flag overlaps
- Check `wiki/topics/roadmap-timeline.md` — does this fit the timeline?
- Check `wiki/topics/dependencies.md` — any blocked dependencies?

### 5. Flag the four risks (SVPG)

For every PRD, explicitly assess:
- **Value risk** — Will users actually use this? Evidence?
- **Usability risk** — Can users figure it out? Complexity?
- **Feasibility risk** — Can engineering build it in the timeline?
- **Viability risk** — Does it work for the business? Compliance, cost, legal?

## Mode 2: Review an existing PRD

Read the PRD. Score across these 10 dimensions:

1. **Completeness** — Is every section filled? Any "TBD" left unresolved?
2. **Clarity** — Could an engineer start building from this? Could an exec understand the "why"?
3. **Evidence** — Are claims backed by data, quotes, or intake cards? Or just assertions?
4. **Scope discipline** — Is the scope tight? Does every P0 item serve the problem statement?
5. **Dependencies** — Are all dependencies identified? Are any blocked?
6. **Risk coverage** — Are risks realistic? Are mitigations concrete?
7. **Success metrics** — Are they measurable? Can we know if we succeeded?
8. **Timeline realism** — Is it realistic given dependencies and resource pressure?
9. **Open questions** — Are they real blockers or avoidable with a decision?
10. **SVPG four risks** — All four assessed (value, usability, feasibility, viability)?

Output the full 10-row scorecard:

```markdown
## PRD Review: [title]

| Dimension | Score (1-5) | Notes |
|-----------|-------------|-------|
| Completeness | | |
| Clarity | | |
| Evidence | | |
| Scope discipline | | |
| Dependencies | | |
| Risk coverage | | |
| Success metrics | | |
| Timeline realism | | |
| Open questions | | |
| SVPG four risks | | |

**Overall**: Ready / Needs revision / Major gaps

**Top 3 issues**:
1. ...

**Suggested edits**: [specific changes]
```

## Tips

- A PRD is not a feature list. It's a contract between PM and eng about WHAT and WHY. HOW is eng's domain.
- If you can't fill the "Evidence" subsection of Problem Statement, you don't have a PRD yet — you have a hypothesis. Run `/intake` or `/synthesize` first.
- Keep P0 ruthlessly small. If everything is P0, nothing is.

## See also

- `/challenge` — stress-test the PRD before sharing
- `/prototype` — build a quick prototype from the PRD
- `/brief` — summarize the PRD for stakeholders

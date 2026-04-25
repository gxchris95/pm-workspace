---
name: retro
description: Generate a retrospective comparing planned vs. actual for a sprint, month, or quarter — with velocity numbers, root-cause analysis of slips, trends across periods, and concrete action items. Use this skill whenever the user asks for a retro, retrospective, postmortem, "what shipped" review, end-of-quarter summary, or wants to learn from execution patterns.
metadata:
  phase: Reflect
  inputs: [time period (sprint, month, quarter), wiki state, workspace/prds/ status, roadmap-timeline]
  outputs: [retrospective report]
  output_to: workspace/retros/YYYY-MM-DD-retro.md
---

# Retro — Retrospective on What Shipped vs. What Was Planned

## When to use

End of a sprint, month, or quarter. Or when you want a clear-eyed look at execution vs. plan. This is the learning loop that prevents repeating mistakes.

## Process

### 1. Define the period

What time range are we reflecting on? Default to the current quarter if not specified. Use the quarter notation `Q<n> YYYY` (e.g., `Q1 2026`) per `AGENTS.md` conventions.

### 2. Read planned state

Pull the roadmap items that were targeted for this period from `wiki/topics/roadmap-timeline.md`.

```markdown
## What Was Planned for [Period]

| Item | Product | Target | Planned Status |
|------|---------|--------|---------------|
```

### 3. Read actual state

Check each item's actual status. Sources: wiki product pages, workspace PRDs, PM-provided updates.

```markdown
## What Actually Happened

| Item | Planned | Actual | Delta |
|------|---------|--------|-------|
| [item] | Ship in Q1 2026 | Shipped on time | ✅ On track |
| [item] | Ship in Q1 2026 | Slipped to Q2 2026 | 🟡 Late |
| [item] | Ship in Q1 2026 | Not started | 🔴 Missed |
| [unplanned item] | Not planned | Shipped | 🔵 Unplanned win |
```

### 4. Calculate velocity

```markdown
## Velocity

- **Planned items**: [N]
- **Shipped on time**: [N] ([%])
- **Slipped**: [N] ([%])
- **Not started**: [N] ([%])
- **Unplanned items shipped**: [N]
- **Net completion rate**: [%]
```

### 5. Analyze patterns

Look for systemic issues, not just individual slips:

```markdown
## Patterns

### What went well
- [pattern] — evidence: [specific items]

### What didn't go well
- [pattern] — evidence: [specific items]

### Root causes for slips
- [cause] — affected [N] items — example: [specific item]
```

Common root causes to check:
- **Dependency delays** — external teams didn't deliver on time
- **Scope creep** — items grew beyond original spec
- **Resource contention** — too many items competing for same team
- **Unclear requirements** — PRD gaps discovered mid-build
- **Estimation error** — work was harder than expected

### 6. Track trends

If previous retros exist in `workspace/retros/`, compare:

```markdown
## Trends

| Metric | Last Period | This Period | Direction |
|--------|------------|-------------|-----------|
| Completion rate | 60% | 75% | ↑ Improving |
| Avg slip (days) | 21 | 14 | ↑ Improving |
| Unplanned items | 5 | 2 | ↑ Better planning |
```

### 7. Generate action items

```markdown
## Action Items

| # | Action | Owner | Due |
|---|--------|-------|-----|
| 1 | [specific, actionable change] | [role] | [date] |
```

Actions should be concrete changes to process, not vague commitments. Bad: "communicate better." Good: "add dependency status to weekly standup agenda."

### 8. Save

Save to `workspace/retros/YYYY-MM-DD-retro.md`.

## Tips

- Retros are learning tools, not blame tools. Focus on systems and processes, not individuals.
- If completion rate is consistently below 70%, the problem is over-planning, not under-execution.
- Unplanned items that shipped aren't always bad — they might indicate responsiveness. But if they consistently crowd out planned work, there's a prioritization problem.
- The most valuable retro output is the action items. If no one acts on them, stop doing retros and fix the action-item problem first.

## See also

- `/roadmap-check` — compare plan vs. actual before the retro
- `/synthesize` — find patterns across multiple retros
- `/brief` — communicate retro findings to leadership

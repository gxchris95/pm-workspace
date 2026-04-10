---
skill: roadmap-check
trigger: /roadmap-check
phase: Validate
inputs: [wiki/topics/roadmap-timeline.md, wiki/products/*, current date]
outputs: [roadmap health report with slips, conflicts, and risks]
output_to: [inline report — updates wiki if issues found]
---

# Roadmap Check — Validate Roadmap Health

## When to use

Periodic health check on the roadmap. Run weekly, or before planning meetings, or when you suspect things have drifted. Also useful after ingesting new PRDs or sources.

## Process

### 1. Read current state

Read:
- `wiki/topics/roadmap-timeline.md` — the consolidated timeline
- `wiki/overview.md` — current strategic priorities
- `wiki/topics/dependencies.md` — blockers
- Any relevant product pages for items you want to deep-check

Note today's date for temporal comparisons.

### 2. Check for slips

Compare target dates against today:

```markdown
## Slipped Items

| Item | Product | Target Date | Status | Days Late |
|------|---------|-------------|--------|-----------|
```

An item is "slipped" if:
- Target date has passed and status is not "✅" or "Shipped"
- Target quarter has ended with no update

### 3. Check for resource conflicts

Identify quarters where multiple major items compete:

```markdown
## Resource Conflicts

### [Quarter] — [N] major items
| Item | Product | Team/Resource |
|------|---------|---------------|

**Risk**: [describe the conflict]
**Recommendation**: [sequence, defer, or staff up]
```

### 4. Check dependencies

Cross-reference `wiki/topics/dependencies.md`:

```markdown
## Blocked Items

| Item | Blocked By | Blocker Status | Impact if Not Resolved |
|------|-----------|---------------|----------------------|
```

### 5. Check alignment

Do the roadmap items still align with the strategic priorities in `wiki/overview.md`?

```markdown
## Alignment Check

| Strategic Priority | Roadmap Items Supporting It | Gap? |
|-------------------|---------------------------|------|
```

Flag roadmap items that don't map to any strategic priority (orphan work). Flag strategic priorities with no roadmap items (strategy without execution).

### 6. Check staleness

Identify items with no status updates for 30+ days, products with no roadmap items, and roadmap entries that reference products not in the wiki.

### 7. Produce the report

```markdown
# Roadmap Health Report — [DATE]

## Summary
[1-2 sentences: overall health, biggest concern]

## Key Findings

### 🔴 Critical (needs action this week)
- ...

### 🟡 Warning (needs attention this month)
- ...

### 🟢 On Track
- ...

## Slipped Items
[table]

## Resource Conflicts
[analysis]

## Blocked Items
[table]

## Alignment Check
[table]

## Recommendations
1. [specific action]
2. [specific action]
```

### 8. Offer to update

If stale or incorrect information is found, offer to update the relevant wiki pages using the AGENTS.md ingest workflow.

## Tips

- Run this before any planning meeting. It takes 2 minutes and prevents 30 minutes of "wait, what's the status of X?"
- The report is only useful if it's honest. Don't soft-pedal slips. "2 weeks late" is different from "still in progress."
- When items slip, ask "why" before recommending a new date. Pattern of slips suggests a systemic issue, not bad estimation.

## See also

- `/brief` — communicate roadmap status to stakeholders
- `/retro` — review what actually shipped vs. planned
- `/lint` — catch stale roadmap items in the wiki

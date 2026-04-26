# PRD Review — 10-Dimension Scorecard

Score the PRD across these 10 dimensions (1–5 each):

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

## Output format

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

## SVPG four risks (reference)

For every PRD, explicitly assess:
- **Value risk** — Will users actually use this? Evidence?
- **Usability risk** — Can users figure it out? Complexity?
- **Feasibility risk** — Can engineering build it in the timeline?
- **Viability risk** — Does it work for the business? Compliance, cost, legal?

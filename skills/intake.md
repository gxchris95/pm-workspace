---
skill: intake
trigger: /intake
phase: Discover
inputs: [Slack thread, Jira ticket/epic, meeting notes, survey results, ad-hoc request, customer feedback]
outputs: [structured requirement card]
output_to: [workspace/prds/ (if actionable), wiki/ (if knowledge), raw/ (if reference-worthy)]
---

# Intake — Process Raw Signal

## When to use

You have unprocessed signal — a Slack thread, Jira export, meeting transcript, survey result, exec ask, or customer feedback. You need to extract structured, actionable requirements from it.

## Process

### 1. Read the signal completely

Do not skim. Read every message, comment, reply thread. Note who said what.

### 2. Extract the requirement card

For each distinct requirement or ask in the signal, produce:

```markdown
### [Short title]

**Source**: [where this came from — Slack #channel, Jira PROJ-123, meeting on DATE, etc.]
**Who**: [who is asking or affected — names, teams, roles]
**Problem**: [what pain or gap they're describing — their words, not your interpretation]
**Ask (explicit)**: [what they literally asked for]
**Need (implicit)**: [what they actually need — reframe if the ask and the real need diverge]
**Priority signals**:
  - Urgency: [low/medium/high — is there a deadline or forcing function?]
  - Frequency: [one-off ask or recurring theme?]
  - Breadth: [one person or many people/teams?]
  - Impact: [if unaddressed, what happens?]
**Context**: [dates, dependencies, constraints, related products/features]
**Suggested action**: [one of: create PRD, update wiki, file for discussion, needs data, discard]
```

### 3. Challenge the framing

Like gstack's `/office-hours` — push back on the explicit ask. Is the user describing a symptom or the root cause? Would a different framing lead to a better solution? If so, note it under "Need (implicit)."

### 4. Cross-reference the wiki

Read `wiki/index.md`. Does this requirement relate to an existing product, topic, or roadmap item? Note connections. Flag contradictions with existing wiki content.

### 5. Recommend disposition

- **Actionable + scoped** → Create workspace artifact (PRD draft, decision record)
- **Knowledge** → Update relevant wiki page (use AGENTS.md ingest workflow)
- **Reference-worthy source** → File in raw/ under appropriate subfolder
- **Noise** → Note why, discard

### 6. If multiple requirements

Process each separately. Group related ones. Flag duplicates against existing requirements in `workspace/prds/`.

## Output format

Deliver all requirement cards in a single response. End with a summary table:

```markdown
## Intake Summary

| # | Title | Who | Priority | Suggested Action |
|---|-------|-----|----------|-----------------|
| 1 | ... | ... | ... | ... |
```

## Tips

- Quote original language when capturing the problem — don't sanitize away the frustration
- "Many people want X" is not a requirement. Name the people, count them
- If the signal is ambiguous, list what you'd need to clarify before acting
- Check `workspace/prds/` for in-flight PRDs that this might relate to

## See also

- `/synthesize` — run across multiple intake cards to find patterns
- `/prioritize` — rank the extracted requirements
- `/prd` — if the intake surfaces something that needs a PRD

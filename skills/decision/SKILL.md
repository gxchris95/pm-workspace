---
name: decision
description: Structure a product decision with options, tradeoffs, recommendation, and consequences in ADR (Architecture Decision Record) format. Use this skill whenever the user faces a fork in the road, needs to choose between multiple valid options, asks "should we do A or B", wants to document a tradeoff, formalize a call so others can see the reasoning later, or asks to write a decision record / ADR.
metadata:
  phase: Specify
  inputs: [a question or choice that needs to be made, context from wiki/workspace]
  outputs: [decision record in workspace/decisions/]
  output_to: workspace/decisions/<topic>.md
---

# Decision — Structure and Document a Decision

## When to use

You face a choice with multiple valid options and real tradeoffs. You need to think through it rigorously, get alignment, and leave a record.

Format follows Architecture Decision Records (Michael Nygard) adapted for product decisions.

## Process

### 1. Frame the decision

Ask: "What exactly are we deciding?" Scope it to a single decision. If it's compound, break it into separate decisions.

### 2. Gather context

Read relevant wiki pages and workspace artifacts. Understand the constraints, stakeholders, and timeline.

### 3. Write the decision record

```markdown
---
decision: [short title]
status: Proposed
date: YYYY-MM-DD
deciders: [who has authority to make this call]
informed: [who needs to know]
sources: [wiki pages, intake cards, raw sources consulted]
supersedes: [link to prior decision if applicable]
superseded_by: [filled in later if this decision is reversed]
---

# [Decision Title]

## Context

What is the situation? What forces are in tension? Why does this decision need to be made now?

State facts neutrally. Don't argue for an outcome here.

## Options

### Option A: [name]
- **Description**: What this option entails
- **Pros**: [list]
- **Cons**: [list]
- **Cost/effort**: [estimate]
- **Risk**: [what could go wrong]

### Option B: [name]
[same structure]

### Option C: [name] (if applicable)
[same structure]

## Evaluation Criteria

What matters most for this decision? Rank these:
1. [criterion] — why it matters
2. [criterion] — why it matters

## Recommendation

**Option [X]** because [reasoning tied to evaluation criteria].

Specifically:
- It best addresses [top criterion] because [evidence]
- The main risk ([describe]) is mitigable by [mitigation]
- The alternatives fall short on [specific gap]

## Consequences

If we go with this:
- **We gain**: [positive consequences]
- **We accept**: [tradeoffs and costs]
- **We close off**: [options no longer available]
- **We need to**: [follow-up actions]

## Open Questions

Any remaining unknowns that don't block the decision but should be tracked.
```

### 4. Check for bias

Before finalizing, explicitly check:
- **Anchoring** — Are we favoring the first option considered?
- **Sunk cost** — Are we favoring an option because of past investment?
- **Availability** — Are we overweighting recent or vivid information?
- **Groupthink** — Has everyone actually agreed, or just gone silent?

Note any biases detected.

### 5. File it as Proposed

Save to `workspace/decisions/<topic>.md` with `status: Proposed`. Include a deadline for the decision.

### 6. State transitions

Decision records have a defined lifecycle. Apply transitions explicitly:

| From | To | Action | What to update |
|------|-----|--------|----------------|
| Proposed | Accepted | Decider has approved | Set `status: Accepted`, set `accepted_date: YYYY-MM-DD`, append to `wiki/log.md` |
| Accepted | Superseded | Reversed by a new decision | Set `status: Superseded`, set `superseded_by: [link]`. **Do not edit anything else** — the record is immutable once Accepted. The new decision links back via `supersedes:`. |
| Accepted | Deprecated | No longer relevant but not reversed | Set `status: Deprecated`, add a `deprecated_reason:` field |
| Proposed | Rejected | Not adopted | Set `status: Rejected`, keep file for reference |

**Rule**: Once a decision is `Accepted`, treat the body as immutable. Reversals create a new decision with `supersedes:` pointing to the old one.

When transitioning, ask the PM for explicit confirmation before flipping `Accepted` → `Superseded`.

## Tips

- Two options is not a real decision — it's a binary. Find at least three options, including "do nothing."
- If you can't articulate the consequences of each option, you don't understand the options well enough.
- Decisions should be reversible when possible. Note which are one-way doors vs. two-way doors.
- A decision with no deadline isn't a decision — it's a thought exercise. Set a date.

## See also

- `/challenge` — stress-test the chosen option
- `/brief` — communicate the decision to stakeholders
- `/prd` — if the decision leads to building something

---
skill: decision
trigger: /decision
phase: Specify
inputs: [a question or choice that needs to be made, context from wiki/workspace]
outputs: [decision record in workspace/decisions/]
output_to: [workspace/decisions/<topic>.md]
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
status: Proposed | Accepted | Superseded | Deprecated
date: YYYY-MM-DD
deciders: [who has authority to make this call]
informed: [who needs to know]
sources: [wiki pages, intake cards, raw sources consulted]
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

### 5. File it

Save to `workspace/decisions/<topic>.md`. Decision records are **immutable once accepted** — if the decision is later reversed, create a new record that supersedes it (link to original).

## Tips

- Two options is not a real decision — it's a binary. Find at least three options, including "do nothing."
- If you can't articulate the consequences of each option, you don't understand the options well enough.
- Decisions should be reversible when possible. Note which are one-way doors vs. two-way doors.
- A decision with no deadline isn't a decision — it's a thought exercise. Set a date.

## See also

- `/challenge` — stress-test the chosen option
- `/brief` — communicate the decision to stakeholders
- `/prd` — if the decision leads to building something

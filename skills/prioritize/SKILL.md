---
name: prioritize
description: Score and rank PM requirements using modified RICE (Reach × Impact × Confidence × Strategic Alignment / Effort) or a custom framework. Use this skill whenever the user asks to prioritize, rank, sequence, score, bucket, or decide what to do first across a set of requirements, themes, or feature requests — including phrases like "what should we do first", "which of these matters most", or "help me sequence".
metadata:
  phase: Prioritize
  inputs: [intake cards, synthesis themes, existing backlog, strategic context]
  outputs: [scored and ranked requirements, priority recommendation]
  output_to: workspace/prds/ (top items promoted to PRD drafts via /prd)
---

# Prioritize — Score and Rank Requirements

## When to use

You have a set of requirements, themes, or feature requests and need to decide what matters most. Works on output from `/intake`, `/synthesize`, or a freeform list.

## Process

### 1. Gather the items

Collect all requirements to score. Sources:
- Intake cards from `/intake` (in `workspace/intake/`)
- Themes from `/synthesize`
- Items pasted directly by the PM
- Existing items in `workspace/prds/` (if re-prioritizing)

### 2. Establish the scoring framework

Default: **modified RICE** (Reach, Impact, Confidence, Effort) extended with Strategic Alignment.

| Dimension | Scale | What it measures |
|-----------|-------|-----------------|
| **Reach** | 1-5 | How many teams/users/BUs affected? 1 = one team, 5 = platform-wide |
| **Impact** | 1-5 | How much does this move the needle? 1 = marginal, 5 = transformative |
| **Confidence** | 1-5 | How sure are we about reach + impact? 1 = gut feel, 5 = hard data |
| **Effort** | 1-5 | How much work? 1 = trivial, 5 = multi-quarter, multi-team |
| **Strategic Alignment** | 1-5 | How well does this align with current priorities in `wiki/overview.md`? |

**Score = (Reach × Impact × Confidence × Strategic Alignment) / Effort**

> Note: This is a 5-axis modification of standard RICE (R×I×C/E). The 5th axis (Strategic Alignment) is added because PM portfolio prioritization is dominated by alignment with leadership priorities. If the PM prefers standard RICE, drop Strategic Alignment from the formula.

The PM can override the framework. Ask: "Use modified RICE, standard RICE, impact/effort, or a custom framework?"

### 3. Score each item

For each requirement:

```markdown
### [Requirement title]

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Reach | 3 | Affects ~15 teams across multiple products |
| Impact | 4 | Removes a daily pain point |
| Confidence | 3 | 3 intake sources, no quantitative data |
| Effort | 4 | 2 sprints, cross-team dependency |
| Strategic Alignment | 5 | Directly supports Q1 priority |
| **Total** | **45** | (3×4×3×5)/4 |
```

### 4. Rank and bucket

Sort by score. Group into tiers:

```markdown
## Priority Stack

### Tier 1 — Do Now (top 3-5 items)
| Rank | Item | Score | Next Step |
|------|------|-------|-----------|

### Tier 2 — Do Next (next 3-5 items)
| Rank | Item | Score | Next Step |

### Tier 3 — Backlog (everything else)
| Rank | Item | Score | Why not now |
```

### 5. Validate against constraints

Check against real constraints:
- **Resource pressure** — read `wiki/topics/roadmap-timeline.md` for bottleneck quarters
- **Dependencies** — read `wiki/topics/dependencies.md` for blockers
- **Strategic priorities** — read `wiki/overview.md` current priorities
- Flag items that score high but are blocked by external dependencies

### 6. Recommend

End with a clear recommendation:
- Top 3 items to act on (with suggested next step: create PRD, schedule discussion, prototype)
- Items to explicitly defer (with reasoning)
- Items to kill (with reasoning — not everything deserves to live)

## Tips

- Scoring is a tool for conversation, not a replacement for judgment. If the math says one thing and your gut says another, surface both.
- Ask "What happens if we don't do this?" for every Tier 1 item. If the answer is "nothing much," it's not Tier 1.
- Effort estimates from the PM side are usually optimistic. When in doubt, round up.
- Re-prioritize when context changes: new intake, dependency unblocked, strategy shift.

## See also

- `/synthesize` — find patterns before prioritizing
- `/prd` — spec out the top-tier items
- `/decision` — when a prioritization requires a formal tradeoff call

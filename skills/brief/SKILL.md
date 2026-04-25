---
name: brief
description: Generate audience-appropriate summaries (exec, eng, designer, partner team, broad stakeholders). Use this skill whenever the user asks for a summary, brief, update, exec one-pager, status note, or stakeholder communication — including phrases like "write this up for [audience]", "summarize for the leadership team", "I need a one-pager", or "draft a status update".
metadata:
  phase: Communicate
  inputs: [topic, product, decision, or question + target audience]
  outputs: [audience-appropriate summary document]
  output_to: workspace/briefs/<topic>.md
---

# Brief — Generate Audience-Appropriate Summary

## When to use

You need to communicate something to a specific audience — exec, eng leader, designer, partner team, or external stakeholder. Different audiences need different depth, framing, and emphasis.

## Process

### 1. Identify the audience

Ask (or infer): Who is reading this?

| Audience | They care about | They don't want |
|----------|----------------|-----------------|
| **Exec / VP** | Business impact, risk, decisions needed, timeline | Technical details, implementation specifics |
| **Eng Lead** | Architecture, dependencies, feasibility, timeline, unknowns | Business justification they already agree with |
| **Designer** | User flows, pain points, interaction patterns, constraints | Backend systems, data models |
| **Partner team** | What they need to do, when, what's in it for them, who to contact | Your internal prioritization rationale |
| **Broad stakeholders** | What changed, why, what it means for them | Internal deliberation, options not taken |

### 2. Gather context

Read relevant wiki pages, workspace artifacts, and raw sources. Build a complete picture before filtering down.

### 3. Write the brief

Every brief has the same frontmatter; the body differs by audience.

**Common frontmatter (all briefs):**
```yaml
---
brief: [topic]
audience: Executive | Engineering | Designer | Partner | Broad
date: YYYY-MM-DD
author: [PM name]
sources: [wiki pages, workspace docs consulted]
---
```

#### Exec Brief (1 page max)

```markdown
# [Topic] — Executive Brief

## TL;DR
2-3 sentences. What's happening, why it matters, what's needed.

## Context
One paragraph. Enough background to understand the situation.

## Key Data
3-5 bullet points with concrete numbers. No handwaving.

## Options / Recommendation (if decision needed)
State the recommendation clearly. Note key tradeoff.

## Ask
What do you need from the reader? Be specific: approval, budget, headcount, decision by [date].

## Timeline
Key milestones only. No sprint-level detail.
```

#### Engineering Brief

```markdown
# [Topic] — Engineering Brief

## What
What we're building or changing. Plain language, then technical detail.

## Why
Problem statement. User impact. Link to PRD if exists.

## Architecture
How it fits into existing systems. Diagrams welcome. Reference wiki product pages.

## Dependencies
What's blocked, what blocks others. Link to `wiki/topics/dependencies.md`.

## Open Questions
Technical unknowns that need eng input. Number them.

## Timeline
Milestones with dates. Flag items at risk.
```

#### Stakeholder Update

```markdown
# [Topic] — Update for [Audience]

## What changed
Bullet list of what's new since last update.

## What it means for you
Specific impact on the reader's team or workflow.

## What's next
Upcoming milestones, dates, any action needed from them.

## Contact
Who to reach out to with questions.
```

### 4. Apply the pyramid principle

Lead with the conclusion. Support with evidence. Detail last. Every sentence should earn its place — if removing it doesn't change the reader's understanding, remove it.

### 5. Save

Save to `workspace/briefs/<topic>.md`.

## Tips

- An exec brief over 1 page won't be read. Brevity is respect for the reader's time.
- "Let me know if you have questions" is not an ask. "I need a decision on X by Friday" is.
- Use concrete numbers from the wiki, not vague qualifiers. "[X] teams" not "many teams."
- If the audience is mixed, write for the most senior person and add a technical appendix.

## See also

- `/roadmap-check` — validate roadmap claims before briefing
- `/retro` — brief based on retrospective findings
- `/competitive` — add competitive context to the brief

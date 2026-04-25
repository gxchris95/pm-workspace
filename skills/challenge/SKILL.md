---
name: challenge
description: Adversarial "red team" review of a PRD, proposal, plan, or assumption. Stress-tests the problem framing, solution scope, and the SVPG four risks (value, usability, feasibility, viability). Use this skill whenever the user wants to pressure-test something, find weaknesses, hear devil's advocate, get pushback, or stress-test before committing — including phrases like "poke holes in this", "what could go wrong", "tear this apart", or "challenge my assumptions".
metadata:
  phase: Validate
  inputs: [PRD, proposal, plan, roadmap item, or any artifact claiming to solve a problem]
  outputs: [challenge report with identified weaknesses, questions, and recommendations]
  output_to: inline (no file written unless the user requests one in workspace/briefs/)
---

# Challenge — Adversarial Review

## When to use

You have a PRD, proposal, plan, or assumption that needs stress-testing before committing resources. This is the "red team" skill — its job is to find problems, not to be encouraging.

## Process

### 1. Read the artifact completely

Understand what's being proposed, why, for whom, and on what timeline.

### 2. Challenge the problem

- **Is the problem real?** What evidence exists that this is a real pain? Count the sources. If the evidence is thin, say so.
- **Is this the right framing?** Would reframing the problem lead to a simpler or more impactful solution?
- **Is this the right time?** Why now? What happens if we wait 6 months?
- **Who cares?** How many teams/users are affected? Is this a loud minority or a quiet majority?

### 3. Challenge the solution

- **Is this the simplest solution?** What's the cheapest experiment that would validate the core assumption?
- **What happens if we don't build this?** If the answer is "not much," that's a signal.
- **What's the 10x version?** Are we thinking too small? Is there a bigger opportunity hiding inside this request?
- **What's the 0.1x version?** Can we ship something in 1 week that would teach us 80% of what we need to know?

### 4. Run the four risks (SVPG)

| Risk | Question | Assessment |
|------|----------|------------|
| **Value** | Will users actually use this? What's the evidence? | |
| **Usability** | Can users figure it out? What's the complexity? | |
| **Feasibility** | Can eng build it in the stated timeline with available resources? | |
| **Viability** | Does it work for the business — compliance, cost, strategy fit? | |

### 5. Find the hidden assumptions

List every assumption the artifact makes (explicitly or implicitly):

```markdown
## Hidden Assumptions

| # | Assumption | Evidence | Risk if wrong |
|---|-----------|----------|---------------|
| 1 | Users want X | 2 Slack threads | Low adoption, wasted quarter |
| 2 | Eng can deliver in Q1 | No estimate | Slip to Q2, cascading delays |
```

### 6. Check dependencies and timing

- Cross-reference `wiki/topics/roadmap-timeline.md` — is this competing with higher-priority work?
- Cross-reference `wiki/topics/dependencies.md` — is this blocked by something external?
- Is the target quarter already overloaded?

### 7. Deliver the verdict

```markdown
## Challenge Verdict

**Overall**: Strong / Has gaps / Needs rework / Not ready

### What's strong
- [list genuine strengths]

### What's weak
- [list weaknesses with specific evidence]

### Questions that must be answered before proceeding
1. [question] — because [why it matters]

### Recommendations
- [specific, actionable changes]
```

## Rules

- Be specific, not vague. "This seems risky" is useless. "This depends on [dependency X] rollout which has no confirmed date per `wiki/topics/dependencies.md`" is useful.
- Distinguish between "I disagree with the direction" and "there's a factual gap." Both are valid but they're different.
- Always include what's strong. Pure negativity is unhelpful and demoralizing.
- The PM has final authority. This skill informs; it doesn't decide.

## See also

- `/prd` — revise the PRD based on challenge findings
- `/decision` — when the challenge surfaces a fork in the road
- `/competitive` — external perspective to complement internal review

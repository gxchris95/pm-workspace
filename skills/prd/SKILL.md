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

## Mode 1: Generate

1. **Read existing formats.** Scan `raw/roadmaps/` and `workspace/prds/` for format reference. Match the team's style and depth.
2. **Gather context.** Read the product page (`wiki/products/<product>.md`), `wiki/topics/roadmap-timeline.md`, and `wiki/topics/dependencies.md`.
3. **Draft.** Use `references/prd-template.md` as the structure. Fill every section with specifics — products named, dates concrete, evidence cited.
4. **Cross-reference.** Check `workspace/prds/` for in-flight overlaps. Confirm fit with the roadmap timeline. Flag dependency conflicts.
5. **Assess SVPG four risks** — value, usability, feasibility, viability. Every PRD must address all four.
6. **Save** to `workspace/prds/<product>-<feature>.md`.

## Mode 2: Review

1. **Read the PRD** completely.
2. **Score across 10 dimensions** using `references/review-scorecard.md`.
3. **Output the scorecard** with notes per dimension, top 3 issues, and suggested edits.

## Tips

- A PRD is not a feature list. It's a contract between PM and eng about WHAT and WHY. HOW is eng's domain.
- If you can't fill the "Evidence" subsection of Problem Statement, you don't have a PRD yet — you have a hypothesis. Run `/intake` or `/synthesize` first.
- Keep P0 ruthlessly small. If everything is P0, nothing is.

## See also

- `references/prd-template.md` — full PRD scaffold
- `references/review-scorecard.md` — 10-dimension review rubric and SVPG cheat sheet
- `/challenge` — stress-test the PRD before sharing
- `/prototype` — build a quick prototype from the PRD
- `/brief` — summarize the PRD for stakeholders

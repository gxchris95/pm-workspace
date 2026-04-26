---
name: deck
description: Build a presentation deck (slides, PPT, PPTX, Keynote, Marp) for a specific audience using the workspace knowledge base. Use this skill whenever the user asks to build, draft, or create a deck, slides, presentation, pitch, exec readout, board update, all-hands, sprint review, kickoff, or QBR. Applies the Pyramid Principle (lead with the answer), MECE structure, action titles, the 3-second glance test, and audience tailoring (exec / board / eng / design / partner / customer / all-hands). Output is Marp-compatible markdown that exports to PPTX, PDF, and HTML. Triggers also include "make slides for", "deck about", "PPT for", "presentation on", "build a readout".
metadata:
  phase: Communicate
  inputs: [audience, purpose, source wiki pages or artifacts, length / time budget]
  outputs: [Marp markdown deck in workspace/decks/]
  output_to: workspace/decks/<YYYY-MM-DD>-<audience>-<topic>.md
---

# Deck — Build a Presentation from the Knowledge Base

## When to use

You need to present something — to an exec, a board, an eng team, a partner, a customer, or the company. The substance lives in the wiki, raw sources, or workspace artifacts (PRDs, decisions, briefs, retros). This skill turns that substance into an audience-tailored deck without reinventing the content.

## Core principles (non-negotiable)

These come from McKinsey (Pyramid Principle, MECE), Garr Reynolds (signal-to-noise, picture superiority), and Nancy Duarte (3-second glance test). See `references/design-checklist.md` for the full rubric.

1. **Lead with the answer.** First content slide is the recommendation/conclusion, not the agenda.
2. **Action titles.** Every slide title is a sentence stating the conclusion of that slide. Not "Q1 Adoption" — "Q1 adoption hit 38%, beating the 30% target."
3. **One idea per slide.** If you can't summarize the slide in its title, split it.
4. **3-second glance test.** A reader should grasp the slide's point in 3 seconds. Anything more, redesign.
5. **High signal-to-noise.** Remove anything that doesn't carry the message — chart junk, decorative icons, hedging text.
6. **MECE structure.** Sections don't overlap and collectively cover the topic.
7. **Cite sources.** Every quantitative claim and direct quote links back to a source in `raw/` or `wiki/`. No invented numbers, no invented quotes.

## Process

### 1. Confirm the brief

Ask the PM (or extract from the request):
- **Audience** — exec / board / eng / design / partner / customer / all-hands / mixed
- **Purpose** — inform / decide / persuade / align / celebrate
- **Time budget** — slide count or minutes (rule of thumb: 1 slide per 1–2 minutes)
- **The ask** — what the audience must do, decide, or believe by the end
- **Decision needed** — yes/no, and from whom

If any of these are unclear, ask once before drafting.

### 2. Pick the audience profile

Read `references/audiences.md` for the matching profile. It dictates length, tone, vocabulary, depth, and which slides to include or skip.

### 3. Pull source material

- Read the relevant `wiki/products/<product>.md` and `wiki/topics/*` pages.
- Read in-flight workspace artifacts (PRDs, decisions, briefs, retros) tied to the topic.
- Read raw sources (`raw/decks/`, `raw/research/`, `raw/notes/`) for direct evidence.
- Track every source you use — they go into the deck's `sources:` frontmatter.

### 4. Storyboard with SCR

Outline the narrative using **Situation → Complication → Resolution**:
- **Situation** — the current state the audience already accepts (1–2 slides)
- **Complication** — what's changed, broken, or at risk (1–2 slides)
- **Resolution** — the recommendation, what it costs, what it delivers (the bulk of the deck)

For very short decks (≤5 slides), collapse to: ask → 3 supporting points → next steps.

### 5. Slide outline with action titles

Draft the deck as a numbered list of action-title sentences before writing any slide bodies. Review the outline against the brief — does each title carry weight? Cut, merge, or sharpen.

Use the slide patterns in `references/slide-patterns.md` (executive summary, situation, recommendation, evidence chart, comparison, timeline, asks, appendix).

### 6. Build in Marp markdown

Use `references/marp-template.md` as the starting structure. Conventions:
- Marp directives in the frontmatter set theme, paginate, size.
- `---` separates slides.
- `#` is the action title; `##` is an optional subhead.
- `<!-- _class: lead -->` for title/section dividers.
- `<!-- footer: source -->` cites the source for that slide.
- Speaker notes go after `<!-- -->` HTML comments at the bottom of each slide.
- Charts: prefer simple Markdown tables or Mermaid for diagrams; for real charts, link to an image in `assets/` or instruct the PM to drop one in.

### 7. Self-review against the checklist

Run through `references/design-checklist.md`:
- [ ] First content slide states the answer
- [ ] Every title is a complete sentence with a verb
- [ ] No slide has more than one idea
- [ ] Every number is sourced
- [ ] No filler slides (agenda excepted, only if audience expects it)
- [ ] 3-second glance test passes for each slide
- [ ] Section structure is MECE
- [ ] Length matches the audience profile budget

Fix anything that fails before saving.

### 8. Save and report

Save to `workspace/decks/<YYYY-MM-DD>-<audience>-<topic>.md`.

Report back:
- Slide count
- Sources used
- Open questions or gaps the PM should fill (e.g., "need a Q1 retention chart in `assets/`")
- Render command:
  - `skills/deck/scripts/render.sh <file>` (default: pptx)
  - `skills/deck/scripts/render.sh <file> pdf|html|all`
  - Or directly: `marp --pptx <file>` / `marp --pdf <file>`

## Frontmatter for the deck

```yaml
---
title: <Deck title>
audience: exec | board | eng | design | partner | customer | all-hands
purpose: inform | decide | persuade | align | celebrate
date: YYYY-MM-DD
presenter: <name>
duration: <N min>
status: Draft | Reviewed | Final
sources: [wiki/..., workspace/..., raw/...]
marp: true
theme: default
paginate: true
size: 16:9
---
```

## Tips

- **Don't pad.** A 5-slide answer beats a 25-slide one. Cut ruthlessly.
- **Resist bullet sprawl.** If you have 7 bullets, you have 2–3 slides. Or a table.
- **No "Thank you" slide.** End on the ask or the next step.
- **Pre-empt the obvious objection.** Add one slide titled with the objection answered.
- **Appendix is your friend.** Move detail to the appendix; reference it on the day if asked.
- **Pictures > prose** when the picture exists. Don't generate decorative stock imagery.

## See also

- `references/audiences.md` — audience profiles (exec, board, eng, design, partner, customer, all-hands)
- `references/slide-patterns.md` — slide-pattern catalog with action-title examples
- `references/marp-template.md` — starter Marp markdown
- `references/design-checklist.md` — self-review rubric
- `scripts/render.sh` — convenience wrapper for `marp` (renders to pptx, pdf, html, or all)
- `/brief` — write a 1-page summary first; the deck builds from it
- `/prd` — pull the spec context the deck needs to communicate
- `/challenge` — stress-test the recommendation before presenting

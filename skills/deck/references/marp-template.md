# Marp Starter Template

Marp is the recommended renderer (see workspace `README.md`). It exports markdown to PPTX, PDF, and HTML.

## Install / render

```
npm install -g @marp-team/marp-cli
marp --pptx workspace/decks/<file>.md
marp --pdf  workspace/decks/<file>.md
marp        workspace/decks/<file>.md   # HTML preview
```

## Starter file

Copy this as the scaffold for any new deck. Fill the bracketed sections.

````markdown
---
title: [Deck headline message — a full sentence]
audience: exec
purpose: decide
date: 2026-04-25
presenter: [Your name]
duration: 15 min
status: Draft
sources:
  - wiki/products/[product].md
  - workspace/prds/[prd].md
marp: true
theme: default
paginate: true
size: 16:9
header: '[Topic short title]'
footer: 'Confidential — internal only'
---

<!-- _class: lead -->

# [The deck's headline message in one sentence]

[Presenter name] · [Date] · [Audience]

---

# [Executive summary action title — the whole deck in one sentence]

- [Support 1: ≤12 words, complete clause]
- [Support 2: ≤12 words, complete clause]
- [Support 3: ≤12 words, complete clause]

**Ask:** [one sentence — what you need from the audience]

<!-- speaker note: open with the ask, repeat at the end. -->

---

# [Situation action title — the headline metric or status]

[Insert the chart or 1–2 sentence framing here.]

<!-- footer: Source: wiki/topics/adoption.md (last_updated 2026-04-22) -->

---

# [Complication action title — what changed or is at risk]

- [Evidence point 1]
- [Evidence point 2]

**Implication:** [one sentence]

---

# [Recommendation action title — the verb-led answer]

| Option | Cost | Time | Risk |
|--------|------|------|------|
| A: [name] | | | |
| B: [name] | | | |

**Recommended: [A or B] because [one reason].**

---

# [Risks action title — the top risk in plain language]

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| | | | |

---

# [Asks action title — the headline ask]

- **[Person]** — [what they decide / approve / unblock] by **[date]**
- **[Person]** — [next ask] by **[date]**

---

<!-- _class: lead -->

# Appendix

---

# [Appendix slide 1 — the question this answers]

[Detail.]
````

## Conventions

- **Action titles only** — the `#` of every slide is a complete sentence.
- **One idea per slide** — if the title needs an "and", split.
- **Cite via `<!-- footer: ... -->`** for quantitative claims.
- **Speaker notes** go in HTML comments (`<!-- speaker note: ... -->`); Marp `--pptx` puts them in the PPTX notes pane.
- **Tables > bullets** when there are 4+ comparable items.
- **Mermaid diagrams** work natively for architecture, flow, timeline:
  ```mermaid
  flowchart LR
    A[User] --> B[Auth] --> C[App]
  ```
- **Images** go in `workspace/decks/assets/` and reference with `![alt](assets/<file>.png)`.

## Custom theme (optional)

For brand-aligned output, drop a CSS theme file in `workspace/decks/themes/<name>.css` and reference with `theme: <name>` in the frontmatter. Build a theme once, reuse across decks.

## When to skip Marp

If the audience requires a corporate PPTX template (board, partner, customer-external):
1. Generate the deck in Marp markdown first (faster iteration).
2. Hand the markdown to Anthropic's `pptx` skill or paste content into the corporate template manually.
3. Keep the Marp source in `workspace/decks/` as the canonical version — the PPTX is the rendered artifact.

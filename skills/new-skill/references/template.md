# SKILL.md Starter Template

Copy the block below into `skills/<name>/SKILL.md` and fill the bracketed sections.

---

````markdown
---
name: <name>
description: <One sentence on WHAT this skill does. One or more sentences on WHEN to trigger — explicit verbs and synonyms. Use this skill whenever the user asks to <verbs>.>
metadata:
  phase: Discover | Synthesize | Decide | Define | Validate | Communicate | Reflect | Maintain
  inputs: [<expected inputs>]
  outputs: [<artifacts produced>]
  output_to: <path or "inline">
---

# <Skill Name> — <one-line subtitle>

## When to use

<2–3 sentences. The situation that calls for this skill. Be concrete.>

## Process

1. **<Step name>.** <What the agent does. Reference any reads from wiki/, raw/, workspace/.>
2. **<Step name>.** <Next step.>
3. **<Step name>.** <Save / output / report.>

## Tips

- <One-line gotcha or anti-pattern.>
- <Another tip.>

## See also

- `references/<file>.md` — <what's in there>
- `/<related-skill>` — <how it composes>
````

---

## Frontmatter constraints

| Field | Constraint |
|---|---|
| `name` | lowercase, hyphens, ≤64 chars, must match parent directory |
| `description` | ≤1024 chars, must contain "use" or "when" or "whenever" |
| `phase` | one of the eight phases (see SCHEMA.md sprint flow) |
| `output_to` | a path under `workspace/` or `wiki/`, or `inline` |

## Body conventions

- Keep `SKILL.md` under ~100 lines. Push templates and reference material to `references/`.
- Number the `## Process` steps explicitly.
- End with `## See also` linking related skills and references.
- Don't include long markdown templates in `SKILL.md` body — link to `references/<file>.md`.

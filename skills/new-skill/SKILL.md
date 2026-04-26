---
name: new-skill
description: Scaffold a new agentskills.io-compliant skill in this workspace. Use this skill whenever the user asks to add, create, scaffold, or bootstrap a new skill, slash command, or workflow. Generates the skill folder with SKILL.md, evals.json, and a references/ stub, then registers the skill in AGENTS.md and skills/SCHEMA.md. Triggers also include "I want to add a /<name> skill", "create a new workflow for X", "scaffold a skill that does Y".
metadata:
  phase: Maintain
  inputs: [proposed skill name, what it does, when to trigger it, phase, output destination]
  outputs: [new skill folder under skills/<name>/ with SKILL.md, evals.json, references/]
  output_to: skills/<name>/
---

# New Skill — Scaffold a Compliant Skill

## When to use

The user wants to add a new skill (slash command / workflow) to this workspace. This skill creates the folder structure, writes spec-compliant starter files, and registers the skill in the catalog files.

## Process

### 1. Gather inputs

Ask the PM (or extract from the request):

- **`name`** — lowercase, hyphens only, ≤64 chars, must match the parent directory. Validate against `^[a-z][a-z0-9-]{0,63}$`. Reject reserved names (existing skills under `skills/`).
- **`description`** — ≤1024 chars, says **what** and **when**. Push the user to list explicit triggers ("use this skill whenever the user asks to..."). A vague description = a dead skill.
- **`phase`** — Discover | Synthesize | Decide | Define | Validate | Communicate | Reflect | Maintain.
- **`inputs`** — what the skill expects to read.
- **`outputs`** — what artifact it produces.
- **`output_to`** — file path or `inline`.

If any field is unclear, ask once before scaffolding.

### 2. Scaffold the folder

Create:

```
skills/<name>/
├── SKILL.md       # use references/template.md as the starter
├── evals.json     # 10 should_trigger + 10 should_not_trigger placeholders
└── references/
    └── .gitkeep
```

Use `references/template.md` (in this skill's folder) as the SKILL.md scaffold. Fill the frontmatter from step 1. Leave the body sections (`## When to use`, `## Process`, `## Tips`, `## See also`) with prompts the PM should complete.

### 3. Seed the evals

Generate 10 `should_trigger` and 10 `should_not_trigger` placeholder phrases. The PM will refine them, but seed real phrasing — not "trigger 1", "trigger 2".

Spread phrasing variety across the 10 triggers: imperative ("build X"), question ("can you Y"), narrative ("I need Z for tomorrow"). For `should_not_trigger`, include phrases that another existing skill should claim — this prevents collisions.

### 4. Register the skill

Update three files:

- **`AGENTS.md`** — add a row in the skills table: `| <Phase> | /<name> | <one-line use case> |`.
- **`skills/SCHEMA.md`** — add a row in the "Available skills" table: `| /<name> | <Phase> | <what it does> | <output_to> |`. Add the skill name to the sprint flow diagram if relevant.
- **`README.md`** — add a row in the skill table: `| /<name> | <when to use> |`. Add the folder line in the file tree.
- **`GUIDE.md`** — add a row in the lookup table: `| <when you want to> | /<name> |`.

### 5. Validate

Run `python scripts/validate.py`. It must report `OK: all checks passed`. If it fails:

- `name violates spec` — fix the casing/hyphens.
- `name does not match parent dir` — rename the folder or the frontmatter.
- `description should describe WHEN to use the skill` — add "use" or "when" or "whenever" to the description.
- `should_trigger has N items (recommend >=5)` — add more eval cases.

### 6. Report

Tell the PM:

- The new skill folder path.
- The three registry files updated.
- Suggested next steps:
  1. Refine the SKILL.md `## Process` section with concrete steps.
  2. Refine the 10 + 10 eval cases with real user phrasing.
  3. If the SKILL.md grows past ~100 lines, split content into `references/`.
  4. Re-run `python scripts/validate.py` and `python scripts/run-evals.py`.

## Tips

- **Single responsibility.** If you can't name the skill in a single verb, it's two skills. Split it.
- **Start small.** Ship the skill with a minimal process. Iterate after the first 3 real uses.
- **The description is the trigger.** Spend disproportionate time on it. It's the only thing the agent sees during discovery.
- **Don't add a skill for a one-off task.** Skills are for recurring workflows. One-offs go inline.

## See also

- `references/template.md` — the SKILL.md scaffold this skill copies from
- `BEST-PRACTICES.md` — agent-skills best practices (frontmatter, progressive disclosure, anti-patterns)
- `CONTRIBUTING.md` — how to add a skill manually if you can't run this skill
- `skills/SCHEMA.md` — full skill catalog

---
last_updated: YYYY-MM-DD
sources: [AGENTS.md, wiki/conventions.md]
---

# PM Skills — Schema and Catalog

## What this is

Skills are reusable AI workflows for product management. Each skill lives in its own folder under `skills/<name>/` and follows the [agentskills.io](https://agentskills.io) open standard:

```
skills/
├── SCHEMA.md           # this file
├── intake/
│   ├── SKILL.md        # process the LLM follows
│   └── evals.json      # should-trigger / should-not-trigger queries
├── synthesize/
│   ├── SKILL.md
│   └── evals.json
└── ... (one folder per skill)
```

Skills connect to — but do not replace — the wiki (governed by `AGENTS.md`).

## Skill file format

Each `SKILL.md` uses YAML frontmatter compliant with the agentskills.io spec.

**Required (spec):**
- `name` — lowercase, hyphens only, ≤ 64 chars, must match parent directory.
- `description` — what the skill does AND when to use it. Be "pushy" with explicit trigger phrases ("use this skill whenever..."). ≤ 1024 chars.

**Optional (this workspace's PM-specific metadata):**
```yaml
metadata:
  phase: Discover | Synthesize | Decide | Define | Validate | Communicate | Reflect | Maintain
  inputs: [list of expected inputs]
  outputs: [list of artifacts produced]
  output_to: <path or "inline">
```

Body sections (recommended):
- `# <Skill Name>`
- `## When to use`
- `## Process` (numbered steps)
- `## Tips` (optional gotchas, anti-patterns)
- `## See also` (related skills)

### Progressive disclosure

A skill folder may include subfolders to keep `SKILL.md` short:

```
skills/<name>/
├── SKILL.md
├── evals.json
├── references/   # detailed reference docs the skill links to
├── scripts/      # helper scripts the skill invokes
└── assets/       # templates, sample outputs
```

Only `SKILL.md` is loaded into the agent's working context by default. The agent loads references/scripts/assets on demand.

## How layers relate

| Layer | Nature | Lifecycle |
|-------|--------|-----------|
| `inbox/` | Unprocessed, messy, temporary | Arrives → triaged → moved or deleted |
| `raw/` | Curated, organized, permanent | Filed once → read many times |
| `wiki/` | Synthesized, cross-linked, compounding | Continuously updated |
| `workspace/` | Work products in flight | Created → refined → shipped → archived |

`inbox/` is **not** `raw/`. inbox/ is a processing queue — things move through it. raw/ is a reference library — things stay in it. Some inbox items graduate to raw/ when worth keeping.

## Signal lifecycle

1. Signal lands in `inbox/` (Slack thread, Jira export, transcript, survey, ad-hoc ask).
2. PM runs `/intake` on the item.
3. Outputs flow to:
   - `wiki/` — knowledge updated (via AGENTS.md ingest workflow)
   - `workspace/` — artifact created (intake card, PRD, decision, brief)
   - `raw/` — source filed if worth keeping permanently
   - Discarded — one-time signal, no lasting value
4. Inbox item archived or deleted.

## The PM sprint (mental model, not a waterfall)

```
   Discover ──► Synthesize ──► Decide ──► Define ──► Validate ──► Communicate ──► Reflect
      │             │             │           │           │             │             │
   intake       synthesize    prioritize    prd       challenge       brief         retro
   competitive                 decision               prototype       deck
                                                      roadmap-check
                                                      lint (Maintain — runs anytime)
```

The flow shows where each skill fits conceptually — not a required sequence. Jump in anywhere. Run `/challenge` before `/prd` to stress-test assumptions early. Run `/lint` anytime. Run `/brief` mid-discovery to sharpen thinking.

## Available skills

| Skill | Phase | What it does | Output goes to |
|-------|-------|--------------|----------------|
| `/intake` | Discover | Process raw signal → structured requirement card | `workspace/intake/` |
| `/competitive` | Discover | Market landscape analysis and benchmarking | `workspace/briefs/` |
| `/synthesize` | Synthesize | Find patterns, themes, contradictions across inputs | `wiki/topics/` |
| `/prioritize` | Decide | Score and rank initiatives (modified 5-axis RICE) | `workspace/briefs/` |
| `/decision` | Decide | ADR-style decision record (Proposed → Accepted → Superseded) | `workspace/decisions/` |
| `/prd` | Define | Generate or review a 1–2 page PRD with 10-row scorecard | `workspace/prds/` |
| `/challenge` | Validate | Adversarial review — push back on assumptions, find gaps | inline |
| `/prototype` | Validate | Single-file HTML prototype with self-inspection check | `workspace/prototypes/` |
| `/roadmap-check` | Validate | Slips, conflicts, blockers, alignment gaps | inline |
| `/brief` | Communicate | Audience-tailored summary (exec, eng, designer, partner) | `workspace/briefs/` |
| `/deck` | Communicate | Audience-tailored slide deck — Marp markdown (PPTX/PDF on render) | `workspace/decks/` |
| `/retro` | Reflect | Planned vs. actual, velocity, root-cause, action items | `workspace/retros/` |
| `/lint` | Maintain | Wiki + workspace health check | inline |

## Frontmatter conventions for workspace artifacts

Every workspace artifact carries `sources:` so its provenance is traceable. See each skill's `SKILL.md` for the exact frontmatter spec.

## References

This system synthesizes:
- [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) (Karpathy) — three-layer knowledge architecture
- [gstack](https://github.com/garrytan/gstack) (Garry Tan) — AI skills as sprint process
- **GTD** (David Allen) — capture → clarify → organize → reflect → engage
- **PARA** (Tiago Forte) — Projects, Areas, Resources, Archive
- **Shape Up** (Ryan Singer / Basecamp) — appetite-driven shaping
- **Continuous Discovery** (Teresa Torres) — opportunity mapping
- **SVPG** (Marty Cagan) — four risks: value, usability, feasibility, viability
- **ADRs** (Michael Nygard) — structured decision records
- **Dual-Track Agile** — parallel discovery + delivery
- [agentskills.io](https://agentskills.io) — open SKILL.md spec

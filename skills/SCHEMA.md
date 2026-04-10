---
last_updated: 2026-04-09
---

# PM Skills — Schema

## What this is

Skills are reusable AI workflows for product management. Each skill is a markdown file the LLM follows when invoked by name. They connect to — but don't replace — the wiki (governed by `AGENTS.md`).

## System architecture

```
inbox/          → Signal queue: raw, unprocessed inputs (transient)
  ↓ skills/
raw/            → Reference library: curated source documents (permanent)
wiki/           → Knowledge base: synthesized, cross-linked (compounding)
workspace/      → Active artifacts: PRDs, decisions, briefs (lifecycle)
skills/         → AI workflows: this directory
```

## How inbox/, raw/, and wiki/ relate

| Layer | Nature | Lifecycle |
|-------|--------|-----------|
| inbox/ | Unprocessed, messy, temporary | Arrives → processed → moved or deleted |
| raw/ | Curated, organized, permanent | Filed once → read many times |
| wiki/ | Synthesized, cross-linked, compounding | Continuously updated |
| workspace/ | Work products in flight | Created → refined → shipped → archived |

**inbox/ is not raw/.** inbox/ is a processing queue — things move through it. raw/ is a reference library — things stay in it. Some inbox/ items graduate to raw/ when worth keeping.

## Signal lifecycle

1. Signal lands in `inbox/` (Slack thread, Jira export, meeting transcript, survey data, ad-hoc ask)
2. Run a skill: "run `/intake` on this"
3. Outputs flow to:
   - `wiki/` — knowledge updated (via AGENTS.md ingest workflow)
   - `workspace/` — artifact created (PRD, decision, brief)
   - `raw/` — source filed if worth keeping permanently
   - Discarded — one-time signal, no lasting value
4. Inbox item archived or deleted

## The PM sprint

```
Discover → Synthesize → Prioritize → Specify → Prototype → Validate → Communicate → Reflect
   │           │            │           │           │           │            │           │
 intake    synthesize   prioritize    prd      prototype   challenge      brief       retro
                                    decision               roadmap-check
                                                           competitive
                                                           lint
```

Each skill feeds into the next. `/intake` structures raw signal that `/synthesize` finds patterns across. `/synthesize` surfaces priorities that `/prd` specs out. `/challenge` stress-tests PRDs before `/prototype` builds them. `/brief` communicates what `/retro` evaluates.

**Non-linear by design.** The sprint flow is a mental model, not a waterfall. Jump in anywhere. Run `/challenge` before `/prd` to stress-test assumptions early. Run `/lint` anytime. Run `/brief` mid-discovery to sharpen thinking. The phases show where each skill fits conceptually — not a required sequence.

## Skill format

```yaml
---
skill: <name>
trigger: /<name>
phase: Discover | Synthesize | Prioritize | Specify | Prototype | Validate | Communicate | Reflect
inputs: [what it needs]
outputs: [what it produces]
output_to: [where artifacts go]
---

# <Skill Name>

## When to use
## Process
## Output format
```

## Available skills

| Skill | Phase | What it does |
|-------|-------|-------------|
| `/intake` | Discover | Process raw signal → structured requirements |
| `/synthesize` | Synthesize | Find patterns, themes, contradictions across inputs |
| `/prioritize` | Prioritize | Score and rank requirements (RICE, impact/effort, strategic fit) |
| `/prd` | Specify | Generate or review a PRD from requirements |
| `/decision` | Specify | Structure a decision with options, tradeoffs, recommendation |
| `/challenge` | Validate | Adversarial review — push back on assumptions, find gaps |
| `/prototype` | Prototype | Quick interactive prototype or design spec from a PRD |
| `/brief` | Communicate | Generate audience-appropriate summary (exec, eng, design) |
| `/roadmap-check` | Validate | Validate roadmap, flag slips, conflicts, stale items |
| `/competitive` | Discover | Market landscape analysis and benchmarking |
| `/retro` | Reflect | What shipped vs planned, velocity, learnings |
| `/lint` | Maintain | Health check across wiki + workspace (already in AGENTS.md) |

## References

This system synthesizes:
- **LLM Wiki** (Andrej Karpathy) — three-layer knowledge architecture
- **gstack** (Garry Tan) — AI skills as sprint process, specialist personas
- **GTD** (David Allen) — capture → clarify → organize → reflect → engage
- **PARA** (Tiago Forte) — Projects, Areas, Resources, Archive
- **Shape Up** (Ryan Singer / Basecamp) — appetite-driven shaping, bounded problems
- **Continuous Discovery** (Teresa Torres) — opportunity mapping, assumption testing
- **SVPG** (Marty Cagan) — four risks: value, usability, feasibility, viability
- **ADRs** (Michael Nygard) — structured, immutable decision records
- **Dual-Track Agile** — parallel discovery + delivery tracks

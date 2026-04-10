# PM Workspace

A ready-to-use workspace for product managers who want to build persistent, compounding knowledge bases with LLMs.

**New here?** Read `GUIDE.md` first — it explains the pattern, why it works, and how to think about it day-to-day. This README is the setup reference.

## What this is

A folder structure + schema + 12 AI workflows that turn any LLM agent into a disciplined PM assistant. You bring the sources and judgment. The LLM builds and maintains the wiki, writes PRDs, runs competitive analysis, prepares exec briefs, and more.

Works with any agent that reads/writes local files: Claude Code, GitHub Copilot in VS Code, and others.

## Quick start

1. **Copy this `pm-workspace/` folder** to a new location. Rename it to your domain (e.g., `ai-platform-wiki/`).

2. **Edit `AGENTS.md`** — fill in the `[brackets]`:
   - "Who this is for" — describe your portfolio
   - "Key product taxonomy" — list your products, groups, and statuses
   - "Raw sources" table — adjust subfolder names if needed

3. **Drop your sources into `raw/`** — PRDs, exec decks, meeting notes, architecture docs. Loosely organized by type. Start with the most current, authoritative documents.

4. **Open in your LLM agent** and say:
   > *"Read AGENTS.md. Read all sources in raw/. Build the initial wiki."*

5. **Review the output.** Guide corrections. The initial build takes 10-30 minutes depending on volume.

6. **From here:** add sources → ingest → query → lint → repeat. Run skills as needed.

## What's included

```
pm-workspace/
├── README.md              ← You're reading this (setup reference)
├── GUIDE.md               ← The pattern explained (read this first)
├── AGENTS.md              ← Schema — the LLM's operating manual (edit this first)
├── wiki/                  ← Knowledge base skeleton
│   ├── index.md           ← Master catalog (LLM reads this first)
│   ├── log.md             ← Chronological operation log
│   ├── overview.md        ← Portfolio-level synthesis
│   ├── products/
│   │   └── _template.md   ← Copy for each product
│   ├── topics/
│   │   ├── adoption.md
│   │   ├── dependencies.md
│   │   └── roadmap-timeline.md
│   └── stakeholders/
│       └── teams.md
├── skills/                ← 12 PM workflow skills (ready to use)
│   ├── SCHEMA.md          ← Skills system overview
│   ├── intake.md          ← Process raw signals
│   ├── synthesize.md      ← Find patterns across inputs
│   ├── prioritize.md      ← Score and rank requirements
│   ├── prd.md             ← Generate or review PRDs
│   ├── decision.md        ← Structured decision records
│   ├── challenge.md       ← Adversarial review
│   ├── prototype.md       ← Quick prototypes and design specs
│   ├── brief.md           ← Audience-appropriate summaries
│   ├── roadmap-check.md   ← Validate roadmap, flag slips
│   ├── competitive.md     ← Market landscape analysis
│   ├── retro.md           ← What shipped vs. planned
│   └── lint.md            ← Health check across wiki + workspace
├── inbox/                 ← Signal queue (drop unprocessed inputs here)
│   └── README.md
├── workspace/             ← Active work products (PRDs, decisions, briefs)
│   └── README.md
└── raw/                   ← Reference library (curated sources)
    └── README.md
```

## How it works

**Six layers:**

| Layer | Purpose | You do | LLM does |
|-------|---------|--------|----------|
| `inbox/` | Signal queue | Drop raw inputs | Process via skills |
| `raw/` | Reference library | Curate sources | Read during ingest |
| `wiki/` | Knowledge base | Browse, review | Write, update, cross-link |
| `AGENTS.md` | Schema | Co-evolve conventions | Follow as operating manual |
| `skills/` | AI workflows | Invoke by name | Execute step by step |
| `workspace/` | Active artifacts | Review, approve | Generate PRDs, decisions, briefs |

**Three core operations:**

- **Ingest** — Drop a source, LLM reads it, updates every relevant wiki page, flags contradictions.
- **Query** — Ask questions. LLM reads the wiki, synthesizes answers with citations.
- **Lint** — Health check: contradictions, stale pages, orphan links, missed roadmap dates.

**Twelve skills** — invoke by name when you need structured workflows:

| Skill | When to use |
|-------|-------------|
| `/intake` | Process a Slack thread, meeting notes, Jira ticket |
| `/synthesize` | Find patterns across multiple inputs |
| `/prioritize` | Score and rank requirements |
| `/prd` | Write or review a PRD |
| `/decision` | Structure a decision with options and tradeoffs |
| `/challenge` | Stress-test assumptions, find gaps |
| `/prototype` | Quick mockup or design spec |
| `/brief` | Exec summary, stakeholder update |
| `/roadmap-check` | Validate timeline, flag slips |
| `/competitive` | Market landscape analysis |
| `/retro` | What shipped vs. planned, learnings |
| `/lint` | Health check across wiki and workspace |

## Recommended tools

- **[Obsidian](https://obsidian.md/)** — `[[wiki-style links]]` become clickable. Graph view shows wiki shape. Dataview plugin enables dynamic queries over frontmatter.
- **Git** — Free version history. `git diff` after each ingest is the single best trust mechanism.
- **Obsidian Web Clipper** — browser extension that clips articles to markdown directly into `raw/`.

## Tips

- **Start with 3-5 current, authoritative sources.** The latest roadmap, current adoption data, a recent exec deck. Layer in historical context after.
- **Stay hands-on at first.** Review every ingest. Guide corrections. Trust builds over time; batch later.
- **File good conversations back into the wiki.** Comparison tables, exec briefs, analyses — don't let them vanish into chat history.
- **Run `/lint` weekly.** Catches contradictions and stale claims before they reach stakeholders.
- **Treat the wiki as a working draft, not source of truth.** Verify critical claims (dates, numbers, commitments) against raw sources before sending to execs.

## What to customize

- **AGENTS.md** — always customize (your portfolio, products, raw source structure)
- **`raw/` subfolders** — rename to match your org's document types
- **`wiki/topics/`** — add or remove topic pages as needed (governance, cost, security, etc.)
- **Skills** — work out of the box for any PM domain. No changes needed.

## Credits

This system synthesizes patterns from:
- **[LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)** (Andrej Karpathy) — three-layer knowledge architecture
- **[gstack](https://github.com/garrytan/gstack)** (Garry Tan) — AI skills as sprint process
- **GTD** (David Allen), **PARA** (Tiago Forte), **Shape Up** (Ryan Singer / Basecamp)
- **Continuous Discovery** (Teresa Torres), **SVPG** (Marty Cagan), **ADRs** (Michael Nygard)

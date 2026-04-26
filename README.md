# PM Workspace

An AI-powered PM operating system — a persistent knowledge base, 14 structured workflows, and a schema that turns any LLM agent into a disciplined product management partner.

**New here?** Read `GUIDE.md` first — it explains the pattern, why it works, and how to think about it day-to-day. This README is the setup reference.

## What this is

A schema and 14 AI workflows that turn any LLM agent into a disciplined PM partner. You bring the sources and judgment. The LLM builds a persistent wiki, writes PRDs, runs competitive analysis, prepares exec briefs, builds presentation decks, tracks roadmap health, and more — all following structured, repeatable processes.

Works with any agent that reads/writes local files: Claude Code, GitHub Copilot in VS Code, and others. A `CLAUDE.md` is included for Claude Code; other agents will read `AGENTS.md` directly.

## Quick start

1. **Copy this `pm-workspace/` folder** to a new location. Rename it to your domain (e.g., `ai-platform-wiki/`).

2. **Edit `AGENTS.md`** — fill in the `[brackets]`:
   - "Who this is for" — describe your portfolio
   - "Key product taxonomy" — list your products, groups, and statuses
   - "Raw sources" table — adjust subfolder names if needed
   - Replace `[Your Domain]` in `AGENTS.md` and wiki files (`index.md`, `log.md`, `overview.md`) with your actual domain name

3. **Drop your sources into `raw/`** — PRDs, exec decks, meeting notes, architecture docs. Loosely organized by type. Start with the most current, authoritative documents.

4. **Open in your LLM agent** and say:
   > *"Read AGENTS.md. Read all sources in raw/. Build the initial wiki."*

5. **Review the output.** Guide corrections. The initial build takes 10–30 minutes depending on volume.

6. **From here:** add sources → ingest → query → lint → repeat. Run skills as needed.

## What's included

```
pm-workspace/
├── README.md              ← You're reading this (setup reference)
├── GUIDE.md               ← The pattern explained (read this first)
├── AGENTS.md              ← Schema — the LLM's operating manual (edit this first)
├── CLAUDE.md              ← Claude Code entry point (reads AGENTS.md)
├── wiki/                  ← Knowledge base skeleton
│   ├── index.md           ← Master catalog (LLM reads this first)
│   ├── log.md             ← Chronological operation log
│   ├── overview.md        ← Portfolio-level synthesis
│   ├── conventions.md     ← Long-form conventions reference
│   ├── products/_template.md
│   ├── topics/
│   │   ├── _template.md
│   │   ├── adoption.md
│   │   ├── dependencies.md
│   │   └── roadmap-timeline.md
│   └── stakeholders/teams.md
├── skills/                ← 14 skills (one folder each)
│   ├── SCHEMA.md          ← Skills system overview
│   ├── GRAPH.md           ← How skills chain together
│   ├── intake/
│   │   ├── SKILL.md       ← Process raw signals
│   │   └── evals.json
│   ├── synthesize/        ← Find patterns across inputs
│   ├── prioritize/        ← Score and rank requirements
│   ├── prd/               ← Generate or review PRDs
│   ├── decision/          ← ADR-style decision records
│   ├── challenge/         ← Adversarial review
│   ├── prototype/         ← Quick HTML prototypes
│   ├── brief/             ← Audience-tailored summaries
│   ├── roadmap-check/     ← Validate roadmap, flag slips
│   ├── competitive/       ← Market landscape analysis
│   ├── deck/              ← Audience-tailored slide deck (Marp → PPTX/PDF)
│   ├── retro/             ← Planned vs. actual
│   ├── lint/              ← Wiki + workspace health check
│   └── new-skill/         ← Meta-skill: scaffold a new skill
├── inbox/                 ← Signal queue
│   ├── README.md
│   └── _template.md
├── workspace/             ← Active artifacts
│   ├── README.md
│   ├── intake/_template.md
│   ├── prds/_template.md
│   ├── decisions/_template.md
│   ├── briefs/_template.md
│   ├── prototypes/_template.md
│   ├── decks/_template.md
│   └── retros/_template.md
├── raw/                   ← Reference library
│   └── README.md
├── scripts/
│   └── validate.py        ← Spec compliance + frontmatter checker
├── .github/workflows/lint.yml  ← CI: runs validator on push/PR
├── mcp-config.example.json     ← Example MCP server config
└── LICENSE                ← MIT
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

Skills extend these operations with structured, multi-step workflows:

**Fourteen skills** — invoke by name when you need structured workflows:

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
| `/deck` | Build a slide deck for a specific audience (Marp → PPTX/PDF) |
| `/roadmap-check` | Validate timeline, flag slips |
| `/competitive` | Market landscape analysis |
| `/retro` | What shipped vs. planned, learnings |
| `/lint` | Health check across wiki and workspace |
| `/new-skill` | Scaffold a new skill (meta) |

## Recommended tools

- **[Obsidian](https://obsidian.md/)** — `[[wiki-style links]]` become clickable. Graph view shows wiki shape. Dataview plugin enables dynamic queries over frontmatter.
- **Git** — Free version history. `git diff` after each ingest is the single best trust mechanism.
- **Obsidian Web Clipper** — browser extension that clips articles to markdown directly into `raw/`.
- **[Marp](https://marp.app/)** — markdown-based slide decks. Generate presentations directly from wiki content.

## Tips

- **Start with 3-5 current, authoritative sources.** The latest roadmap, current adoption data, a recent exec deck. Layer in historical context after.
- **Stay hands-on at first.** Review every ingest. Guide corrections. Trust builds over time; batch later.
- **File good conversations back into the wiki.** Comparison tables, exec briefs, analyses — don't let them vanish into chat history.
- **Run `/lint` weekly.** Catches contradictions and stale claims before they reach stakeholders.
- **Treat the wiki as a working draft, not source of truth.** Spot-check specific claims (dates, numbers, commitments) against raw sources after each ingest. Use `git diff` to review what changed.
- **Keep the workspace separate from personal notes.** Review LLM-generated content before pulling it into other systems or sharing with stakeholders.

## What to customize

- **`[Your Domain]` placeholders** — replace in `AGENTS.md`, `wiki/index.md`, `wiki/log.md`, `wiki/overview.md`
- **AGENTS.md** — always customize (your portfolio, products, raw source structure)
- **`raw/` subfolders** — rename to match your org's document types
- **`wiki/topics/`** — add or remove topic pages as needed (governance, cost, security, etc.)
- **Skills** — work out of the box for any PM domain. Customize or add new ones as needed. Claude Code users can also wire skills as native slash commands by copying them to `.claude/commands/`.

## See also

- `GUIDE.md` — the pattern explained
- `AGENTS.md` — the LLM operating manual
- `BEST-PRACTICES.md` — agent standard best practices (skill design, AGENTS.md authoring)
- `CONTRIBUTING.md` — how to add or modify skills and wiki pages
- `skills/SCHEMA.md` — skill catalog
- `skills/GRAPH.md` — how skills chain together
- `mcp-config.example.json` — optional MCP server config example

## Credits

This system synthesizes patterns from:
- **[LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)** (Andrej Karpathy) — three-layer knowledge architecture
- **[gstack](https://github.com/garrytan/gstack)** (Garry Tan) — AI skills as sprint process
- **[GTD](https://gettingthingsdone.com/)** (David Allen), **[PARA](https://fortelabs.com/blog/para/)** (Tiago Forte), **[Shape Up](https://basecamp.com/shapeup)** (Ryan Singer / Basecamp)
- **[Continuous Discovery](https://www.producttalk.org/continuous-discovery-habits/)** (Teresa Torres), **[SVPG](https://www.svpg.com/)** (Marty Cagan), **[ADRs](https://adr.github.io/)** (Michael Nygard)

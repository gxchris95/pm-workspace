---
last_updated: YYYY-MM-DD
sources: [AGENTS.md]
---

# Conventions — Detailed Reference

This page is the long-form companion to `AGENTS.md`. It contains the layer-by-layer reference, page conventions, frontmatter rules, cross-referencing patterns, and output formats. `AGENTS.md` keeps the surface short; this file holds the depth.

## Six-layer architecture

```
inbox/          → Signal queue: raw, unprocessed inputs (transient)
  ↓ skills/
raw/            → Reference library: curated source documents (permanent)
wiki/           → Knowledge base: synthesized, cross-linked (compounding)
workspace/      → Active artifacts: PRDs, decisions, briefs (lifecycle)
skills/         → AI workflows: reusable PM process skills
```

### Layer 1 — Inbox (`inbox/`)

Transient processing queue. Drop items here, run `/intake` to triage, then move or delete. **inbox/ is not raw/** — it's a staging area.

Structure: `inbox/{slack, jira, meetings, surveys, feedback}/`
Naming: `YYYY-MM-DD-<short-description>.md`

### Layer 2 — Raw sources (`raw/`)

Immutable inputs. The LLM reads from raw/ but never modifies its contents.

| Location | Contents |
|----------|----------|
| `raw/exec-comms/` | Board decks, leadership Q&As, strategy docs |
| `raw/roadmaps/` | PRDs, roadmap documents, sprint plans |
| `raw/customer/` | Customer calls, feedback, support tickets |
| `raw/engineering/` | Architecture docs, tech specs, ADRs |
| `raw/governance/` | Policies, compliance, security frameworks |
| `raw/metrics/` | Adoption data, dashboards, value analyses |
| `raw/decks/` | Past presentation decks for reference |
| `raw/research/` | Analyst reports, white papers, market research |
| `raw/notes/` | Meeting notes, Slack threads, clipped pages |

When ingesting, always note which raw source(s) informed a wiki page update. Inbox items graduate to raw/ when worth keeping permanently.

### Layer 3 — Wiki (`wiki/`)

LLM-owned synthesized knowledge.

```
wiki/
├── index.md            # Master catalog
├── log.md              # Chronological operation log
├── overview.md         # Portfolio-level synthesis
├── conventions.md      # This file
├── products/           # One page per product
├── topics/             # Cross-cutting concerns
└── stakeholders/       # Teams, customers, dependencies
```

### Layer 4 — Skills (`skills/`)

Each skill is a folder with `SKILL.md` (the process) and `evals.json` (trigger queries). Skills are versioned, hot-swappable, and follow the agentskills.io spec.

### Layer 5 — Workspace (`workspace/`)

Active artifacts with a lifecycle: created → refined → shipped → archived.

Structure: `workspace/{intake, prds, decisions, briefs, prototypes, retros}/`

### Layer 6 — Operating manual (`AGENTS.md` + `CLAUDE.md`)

Agent entry points. `AGENTS.md` is the universal manual; `CLAUDE.md` points Claude Code at it.

## Page conventions

### Product pages — `wiki/products/*.md`
Use `wiki/products/_template.md`.
Required frontmatter: `product`, `status`, `adoption`, `last_updated`, `sources`.
Required sections: Summary, Status & Maturity, Key Capabilities, Adoption, Dependencies, Roadmap, Open Questions, Sources.

### Topic pages — `wiki/topics/*.md`
Use `wiki/topics/_template.md`.
Cross-cutting analysis. Frontmatter: `topic`, `last_updated`, `sources`.

### Stakeholder pages — `wiki/stakeholders/*.md`
`teams.md` is the default rollup. For deeper coverage, add per-stakeholder pages: `wiki/stakeholders/<name>.md` (e.g. `acme-corp.md`, `partner-portal-eng.md`). Use `wiki/stakeholders/_template.md`.
Frontmatter: `stakeholder`, `type` (team / customer / partner / dependency), `last_updated`, `sources`.

### Index — `wiki/index.md`
Master catalog. Every wiki page listed with a one-line summary. Updated on every ingest or page creation. Read this first when answering queries.

### Log — `wiki/log.md`
Append-only chronological record:

```markdown
## [YYYY-MM-DD] <operation> | <subject>
<brief description>
Pages touched: <list>
```

Operations: `ingest`, `query`, `lint`, `update`, `create`, `skill-run`.

## Frontmatter

All wiki pages use YAML frontmatter. Minimum:
- `last_updated: YYYY-MM-DD`
- `sources: []` (list of raw source files)

Product pages add: `product`, `status`, `adoption`.
Topic pages add: `topic`.

## Cross-referencing

- Use `[[wiki-style links]]` for Obsidian compatibility (e.g., `[[products/auth-service]]`).
- Every dependency is bidirectional.
- Topic pages link to all relevant product pages.
- When a product is mentioned, link to its product page.

## Output formats

The PM may request:
- **Markdown page** (default): filed into wiki/
- **Comparison table**: product vs. product or option analysis
- **Executive brief**: 1-page summary, key metrics, decisions needed
- **Slide deck (Marp)**: `---` separators, Marp frontmatter
- **Timeline**: chronological view across products

## Key product taxonomy

Fill this in with your products. Example:

| Product | Status |
|---------|--------|
| Auth Service | Production |
| API Gateway | Production |
| Mobile App | Beta |
| Web Dashboard | Production |

## See also

- `AGENTS.md` — operating manual entry point
- `skills/SCHEMA.md` — skill catalog
- `wiki/index.md` — master wiki catalog

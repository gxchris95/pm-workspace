# [Your Domain] — PM Workspace Schema

This is the schema file for your PM workspace. It tells any LLM agent how this workspace is structured, what conventions to follow, and what workflows to execute.

## Who this is for

This workspace is maintained for a **Product Manager** who owns [describe your portfolio — e.g., "the AI Platform product suite"]. It is a persistent, compounding knowledge base and PM toolkit that synthesizes product documentation, executive communications, roadmaps, governance frameworks, adoption data, and strategic analysis into a navigable, cross-referenced resource — plus active workflows for day-to-day product management.

## Six-layer architecture

```
inbox/          → Signal queue: raw, unprocessed inputs (transient)
  ↓ skills/
raw/            → Reference library: curated source documents (permanent)
wiki/           → Knowledge base: synthesized, cross-linked (compounding)
workspace/      → Active artifacts: PRDs, decisions, briefs (lifecycle)
skills/         → AI workflows: reusable PM process skills (this layer)
```

### Layer 1: Inbox — Signal queue (`inbox/`)

Unprocessed inputs waiting to be triaged. Drop items here, run skills to process, then move or delete. **inbox/ is not raw/** — it's a transient processing queue.

Structure: `inbox/{slack, jira, meetings, surveys, feedback}/`

Naming: `YYYY-MM-DD-<short-description>.md`

### Layer 2: Raw sources (`raw/`)

Raw sources are immutable inputs. The LLM reads from them but never modifies them.

| Location | Contents |
|----------|----------|
| `raw/exec-comms/` | Board decks, leadership Q&As, strategy docs |
| `raw/roadmaps/` | PRDs, roadmap documents, sprint plans |
| `raw/customer/` | Customer calls, feedback, support tickets |
| `raw/engineering/` | Architecture docs, tech specs, ADRs |
| `raw/governance/` | Policies, compliance, security frameworks |
| `raw/metrics/` | Adoption data, dashboards, value analyses |
| `raw/notes/` | Meeting notes, Slack threads, clipped web pages |

When ingesting, always note which raw source(s) informed a wiki page update. Some inbox/ items graduate to raw/ when worth keeping permanently.

### Layer 3: The wiki (`wiki/`)

All LLM-generated and LLM-maintained pages live under `wiki/`. The LLM owns this directory entirely. Structure:

```
wiki/
├── index.md                    # Master index of all wiki pages
├── log.md                      # Chronological operation log
├── overview.md                 # Portfolio-level synthesis
├── products/                   # One page per product
├── pillars/                    # Group-level summaries (optional)
├── topics/                     # Cross-cutting concerns
│   ├── adoption.md
│   ├── dependencies.md
│   ├── roadmap-timeline.md
│   └── ...
└── stakeholders/
    └── teams.md                # Teams, customers, external dependencies
```

### Layer 4: This file (AGENTS.md)

This schema governs all LLM behavior across the workspace. Co-evolve it with the PM as conventions change.

### Layer 5: Skills (`skills/`)

Reusable AI workflows for product management — intake, synthesis, prioritization, PRD generation, adversarial review, and more. Governed by `skills/SCHEMA.md`. Each skill is a markdown file the LLM follows when invoked by trigger name (e.g., `/intake`, `/synthesize`).

Skills connect layers: they process inbox/ items, update wiki/ pages (via this file's workflows), create workspace/ artifacts, and file permanent sources to raw/.

See `skills/SCHEMA.md` for the full skill catalog, format, and sprint flow.

### Layer 6: Workspace — Active artifacts (`workspace/`)

Live work products being actively worked on. Unlike wiki/ (permanent knowledge) or raw/ (permanent reference), workspace items have a lifecycle: created → refined → shipped → archived.

Structure: `workspace/{prds, decisions, briefs, prototypes, retros}/`

---

## Page conventions

### Product pages (`wiki/products/*.md`)

Every product page follows this template:

```markdown
---
product: <product-name>
pillar: [your grouping — e.g., "Platform" | "Consumer" | "Enterprise"]
status: Production | Alpha | Beta | Coming Soon
adoption: <number of teams or users>
last_updated: YYYY-MM-DD
sources: [list of raw source files that informed this page]
---

# <Product Name>

## Summary
2-3 sentence executive summary. What it is, why it matters.

## Status & Maturity
Current production readiness. Known gaps or blockers.

## Key Capabilities
Bullet list of what it does.

## Adoption
Who's using it. Numbers. Key customer or team names.

## Dependencies
What this product depends on. What depends on it.

## Roadmap
Upcoming features, timeline, PRD links.

## Open Questions
Unresolved issues, risks, decisions needed.

## Sources
Links to raw source files that informed this page.
```

### Pillar / group pages (`wiki/pillars/*.md`)

Synthesize across all products in the group. Include: narrative summary, product table with status, group-level metrics, strategic direction, cross-product dependencies.

### Topic pages (`wiki/topics/*.md`)

Cross-cutting analysis pages. Each should synthesize information from multiple products and sources. Include frontmatter with `topic:`, `last_updated:`, `sources:`.

### Index (`wiki/index.md`)

Master catalog. Every wiki page listed with a one-line summary. Organized by section. Updated on every ingest or page creation. The LLM reads this first when answering queries.

### Log (`wiki/log.md`)

Append-only chronological record. Each entry:
```markdown
## [YYYY-MM-DD] <operation> | <subject>
<brief description of what was done>
Pages touched: <list>
```

Operations: `ingest`, `query`, `lint`, `update`, `create`.

---

## Workflows

### Skill routing

When the PM's request matches a skill, invoke that skill instead of answering ad-hoc. Skills have structured, multi-step workflows that produce better results than inline answers.

| Pattern | Skill |
|---------|-------|
| Raw signal, Slack thread, meeting notes, feedback | `/intake` |
| "Find patterns", multiple inputs, themes | `/synthesize` |
| Prioritize, rank, score requirements | `/prioritize` |
| Write a PRD, review a PRD, spec something out | `/prd` |
| Decision needed, compare options, tradeoffs | `/decision` |
| Push back, stress-test, find holes, red-team | `/challenge` |
| Quick prototype, mockup, design spec | `/prototype` |
| Exec brief, stakeholder update, summary for audience | `/brief` |
| Roadmap check, timeline, what slipped | `/roadmap-check` |
| Competitive landscape, market analysis, benchmarking | `/competitive` |
| Retro, what shipped, learnings | `/retro` |
| Health check, find issues, validate consistency | `/lint` |

If no skill matches, answer directly using the wiki as context.

### Ingest a new source

1. Read the source completely.
2. Discuss key takeaways with the PM.
3. Create or update relevant wiki pages (products, topics, pillars).
4. Update `wiki/index.md` if new pages were created.
5. Append an entry to `wiki/log.md`.
6. Note any contradictions with existing wiki content and flag them.

### Answer a query

1. Read `wiki/index.md` to identify relevant pages.
2. Read those pages.
3. Synthesize an answer with citations to wiki pages and raw sources.
4. If the answer is substantial and reusable, offer to file it as a new wiki page.

### Lint / health check

Run periodically. Check for:
- Contradictions between pages
- Stale information (newer sources supersede older claims)
- Missing cross-references (product X mentions product Y but no link)
- Products mentioned in sources but lacking a wiki page
- Orphan pages with no inbound links
- Gaps: important topics not yet covered
- Roadmap items past their target date (check against current date)

---

## Cross-referencing conventions

- Use `[[wiki-style links]]` for Obsidian compatibility: `[[products/your-product]]`
- Every product page should link to its pillar page and vice versa.
- Every dependency should be a bidirectional link.
- Topic pages should link to all relevant product pages.
- When a product is mentioned on any page, link to its product page.

## Frontmatter

All wiki pages use YAML frontmatter. Minimum fields:
- `last_updated: YYYY-MM-DD`
- `sources: []` (list of raw source files)

Product pages add: `product`, `pillar`, `status`, `adoption`.
Topic pages add: `topic`.

## Output formats

The PM may request different output formats:
- **Markdown page** (default): filed into wiki
- **Comparison table**: for product vs. product or option analysis
- **Executive brief**: 1-page summary with key metrics and decisions needed
- **Slide deck (Marp)**: for presentations — use `---` slide separators and Marp frontmatter
- **Timeline**: chronological view of roadmap items across products

## Key product taxonomy

<!-- Fill this in with your products. Example:

| Group | Product | Status |
|-------|---------|--------|
| Platform | Auth Service | Production |
| Platform | API Gateway | Production |
| Consumer | Mobile App | Beta |
| Consumer | Web Dashboard | Production |

-->

| Group | Product | Status |
|-------|---------|--------|
| | | |

---

## Voice

Direct, concrete, specific. Name the product, the metric, the team, the date. No filler. Short paragraphs. End with what to do next.

When asking questions, provide context, the question, a recommendation, and options. Consistent format across all skills and ad-hoc work.

## Completion status

When finishing a skill or major workflow, report status:

- **DONE** — All steps completed. Evidence provided.
- **DONE_WITH_CONCERNS** — Completed, but with issues the PM should know about. List each concern.
- **BLOCKED** — Cannot proceed. State what is blocking and what was tried.
- **NEEDS_CONTEXT** — Missing information. State exactly what is needed.

## Operational self-improvement

After major operations (ingests, lint passes, skill runs), reflect:
- Did anything contradict existing wiki content?
- Did any source lack sufficient detail to update confidently?
- Were there wiki pages that should exist but don't?
- Did the operation reveal a gap in this schema?

Log observations in `wiki/log.md` alongside the operation entry. If a schema change is needed, propose it to the PM.

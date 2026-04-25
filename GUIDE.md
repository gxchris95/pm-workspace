# PM Workspace — Guide

A workspace for the day-to-day work of being a product manager — *and* a knowledge base that gets smarter every time you use it.

You bring sources and judgment. The LLM runs the recurring workflows (intake, PRDs, decisions, briefs, retros) and maintains the wiki. You review and direct.

Based on the [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) pattern by Andrej Karpathy, extended into a full PM operating system.

## The problem

PMs do two kinds of work, and both leak.

**Recurring workflows.** Triage a Slack thread. Write a PRD. Capture a decision. Score initiatives. Draft an exec brief. Run a retro. Stress-test a plan. Each task has a known shape — but you reinvent the format every time, quality is inconsistent, and good outputs vanish into chat history or a one-off Google Doc.

**Compounding context.** PRDs, exec decks, customer calls, meeting notes, competitive intel, adoption data — knowledge accumulates constantly but stays scattered across tools and your own memory. Every stakeholder question, every exec prep, you re-synthesize from scratch. Wikis and Notion databases die because the maintenance burden outgrows the value.

ChatGPT uploads, NotebookLM, and RAG systems solve neither. They retrieve at query time and forget after the session. Nothing accumulates. Nothing standardizes. Output formats drift.

## The pattern

A workspace that does two things at once, and lets each one make the other better.

**Skills run the daily work.** A library of structured workflows — `/intake`, `/prd`, `/decision`, `/prioritize`, `/brief`, `/challenge`, `/prototype`, `/competitive`, `/roadmap-check`, `/retro`, `/lint` — that the LLM follows when you invoke them by name. Same shape every time. Outputs land in the right folder with the right frontmatter, ready to share or revisit.

**The wiki compounds.** Every ingested source, every skill run feeds a persistent, cross-linked knowledge base — product pages, topic pages, a roadmap timeline, an index, a log. The LLM reads new material, integrates it into existing pages, flags contradictions, and keeps the synthesis current. You never write the wiki yourself.

**The two reinforce each other.** The wiki gives skills the context they need — the latest roadmap, current adoption, the most recent decision. Skill outputs feed the wiki — a new PRD updates the product page, a decision updates the dependency map. Daily work and long-term knowledge stop competing for your attention.

You curate sources, invoke skills, and direct attention. The LLM does the rest.

In practice: LLM agent on one side of your screen, Obsidian on the other. The LLM edits, you watch.

## The five layers

Two are about knowledge. Three are about workflow. Start with the first two; add the rest when ready.

### Knowledge layers

| Layer | Role | Who writes |
|-------|------|------------|
| `raw/` | **Source of truth.** PRDs, decks, transcripts, customer notes, architecture docs. Immutable. | You curate. LLM reads only. |
| `wiki/` | **Synthesis.** Product pages, topic pages, timeline, index, log. Compounding. Working draft, not source of truth. | LLM owns. You browse. |

### Workflow layers (add when ready)

| Layer | Role | Lifecycle |
|-------|------|-----------|
| `inbox/` | **Processing queue** for messy signal (Slack threads, meeting notes, Jira exports) before it's triaged. | Arrives → `/intake` → routed → deleted. |
| `workspace/` | **Active artifacts:** PRDs, decisions, briefs, prototypes, retros. | Created → refined → shipped → archived. |
| `skills/` | **Reusable workflows** the LLM follows when invoked by name (e.g. `/intake`, `/prd`, `/lint`). | Stable. You invoke; LLM executes. |

Plus one configuration file:

- **`AGENTS.md`** — the operating manual. Tells any LLM agent how this workspace is structured and what conventions to follow. Co-evolve it as you learn what works for your domain.

### raw vs. inbox — the distinction that matters

This trips people up. Both hold "input documents." They are not the same.

- **`raw/`** is the **permanent reference library.** Curated, immutable. Source of truth. Things that are worth re-reading.
- **`inbox/`** is the **transient signal queue.** Messy, in-flight. Things that need to be triaged and then either filed (graduate to `raw/`), turned into a workspace artifact, or discarded.

When in doubt: if you'd want to find this document in six months, it goes to `raw/`. If it's a fresh thread you need to process, it goes to `inbox/`.

## Three core operations

### Ingest
Drop a source into `raw/` (or process an `inbox/` item). The LLM reads it, discusses takeaways with you, then updates every relevant wiki page — products, topics, timeline, index, log. One exec deck might touch 10–15 pages.

### Query
Ask anything. The LLM reads `wiki/index.md` first to find relevant pages, drills in, synthesizes an answer with citations. File good answers back into the wiki — they compound.

### Lint
Periodic health-check. Contradictions, stale claims, orphan pages, missed roadmap dates, unanswered open questions. Run weekly or after major ingests.

## Quick start (5 minutes)

1. **Copy this folder** to a new location. Rename it to your domain (e.g. `ai-platform-wiki/`).
2. **Edit `AGENTS.md`** — fill in the `[brackets]`: your portfolio, your products, the raw subfolders you want.
3. **Drop 3–5 foundational sources** into `raw/`. The current roadmap. The latest exec deck. A recent customer-research summary. Authoritative, current docs.
4. **Open in your LLM agent** (Claude Code, Cursor, etc.) and say: *"Read AGENTS.md. Read all sources in raw/. Build the initial wiki."*
5. **Review the output.** Read the new wiki pages. Correct what's wrong. Trust builds from here.

From now on: drop new sources → ingest → query → lint → repeat. Use skills when you need structured workflows.

## A day in the life

You come back from a meeting where the eng lead said the auth service slips Q1 → Q2.

You drop the meeting notes into `inbox/meetings/2026-04-10-eng-sync.md` and say *"run /intake on this."*

The LLM:
1. Routes the slip into `wiki/products/auth-service.md` (Q1 → Q2).
2. Updates `wiki/topics/roadmap-timeline.md`.
3. **Flags a contradiction**: a topic page still says "auth and billing both target Q1."
4. Adds an open question: "Does the slip affect mobile's dependency on the new auth flow?"
5. Files the meeting notes to `raw/notes/` because they're worth keeping.
6. Appends to `wiki/log.md`.
7. Deletes the inbox item.

One meeting. Six files touched. Three things you would have forgotten.

## Skills (the workflow shortcuts)

Skills are reusable, multi-step LLM workflows. Invoke by name:

| When you want to... | Use |
|---------------------|-----|
| Triage a Slack thread, ticket, or meeting note | `/intake` |
| Find patterns across many inputs | `/synthesize` |
| Score and rank initiatives | `/prioritize` |
| Draft or review a PRD | `/prd` |
| Capture a decision (ADR-style) | `/decision` |
| Stress-test a plan, find weak assumptions | `/challenge` |
| Build a quick HTML mockup | `/prototype` |
| Validate the roadmap | `/roadmap-check` |
| Compare against competitors | `/competitive` |
| Write a summary for [exec / eng / partner] | `/brief` |
| Review what shipped vs. planned | `/retro` |
| Health-check the wiki | `/lint` |

Full catalog with output locations: `skills/SCHEMA.md`.

## Trust and limitations

The LLM will get things wrong:

- **Overstate certainty.** A tentative meeting comment becomes a firm commitment.
- **Hallucinate links.** `[[products/something]]` to a page that doesn't exist. Obsidian shows broken links in red.
- **Silently rewrite.** Updating one page can subtly shift meaning on others. This is the biggest risk.

Mitigations:
- **`git diff` after every ingest.** The single best trust mechanism.
- **Spot-check 1–2 specific claims** (dates, numbers, commitments) against the raw source before you send anything to execs.
- **Run `/lint` weekly.** Catches contradictions and stale claims.
- **Verify against `raw/`, not against the wiki.** The wiki is synthesis; `raw/` is truth.

## Privacy

Markdown lives on your machine, but LLM API calls send content to the model provider (Anthropic, OpenAI, Google). If your docs contain confidential strategy or PII, your company's data classification rules apply. Local models (Ollama, LM Studio) keep everything on-device. Check your AI usage policy before ingesting sensitive material.

## When this is worth it

- Portfolio of products, sustained over months.
- 20+ sources and growing.
- You routinely synthesize across documents for stakeholder conversations.

It's overkill for: one-off questions, single-product PMs with few sources, or document summarization.

## Scaling

| Size | What you need |
|------|---------------|
| **Small** (1–20 products, <50 sources) | `wiki/index.md` is enough. No extra tooling. |
| **Medium** (20–100 products, 50–200 sources) | Add local search (qmd, BM25, vector). Frontmatter summaries on every page. |
| **Large** (100+ products, 200+ sources) | Split into domain-specific workspaces with a shared `raw/`. Embedding-based retrieval starts to outperform index navigation. |

This is a personal tool by default. Read-only wiki snapshots are easy to share. Multi-editor wikis via git work but need merge-conflict care. Start personal, scale later.

## Recommended tools

- **[Obsidian](https://obsidian.md/)** — `[[wiki-style links]]` become clickable; graph view shows the wiki shape; Dataview enables queries over frontmatter.
- **Git** — free version history. `git diff` after each ingest is the single best trust mechanism.
- **Obsidian Web Clipper** — clip articles directly into `raw/` from the browser.
- **[Marp](https://marp.app/)** — markdown slide decks generated from wiki content.

## What's required vs. optional

Hard requirements: `raw/` + `wiki/` + `AGENTS.md` + three operations (ingest, query, lint). Everything else — `inbox/`, `workspace/`, `skills/`, topic pages, output formats — is optional and modular. Start simple. Add structure as you learn what you need.

## Next

- `README.md` — setup reference and folder tree
- `AGENTS.md` — the LLM's operating manual (edit this first)
- `skills/SCHEMA.md` — full skill catalog
- `wiki/conventions.md` — page conventions and frontmatter rules

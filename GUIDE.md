# The PM Workspace Pattern

A guide for product managers who want to build persistent, compounding knowledge bases with LLMs.

This document is for you, the PM. Read it to understand the pattern, then hand `AGENTS.md` to your LLM agent. You bring the judgment and the sources. The agent builds and maintains everything else.

Based on the [LLM Wiki](https://gist.github.com/karpathy/1dd0294ef9567971c1e4348a90d69285) pattern by Andrej Karpathy.

## The core idea

Product managers accumulate knowledge constantly — PRDs, exec decks, customer calls, Slack threads, meeting notes, competitive intel, adoption data, architecture docs. This knowledge is scattered across tools, conversations, and your own memory. When you need to prep for an exec review or answer a stakeholder question, you're re-synthesizing from scratch every time.

Most "AI over documents" tools don't solve this. NotebookLM, ChatGPT file uploads, and RAG systems retrieve relevant chunks at query time, but the LLM is rediscovering connections from scratch on every question. Nothing accumulates.

The idea here is different. Instead of retrieving from raw documents, the LLM **incrementally builds and maintains a persistent wiki** — a structured, interlinked set of markdown files that sits between you and the raw sources. When you add a new document, the LLM doesn't just index it. It reads it, extracts what matters, and **integrates it into the existing wiki** — updating product pages, revising a roadmap timeline, flagging where new data contradicts an old claim, linking a dependency that wasn't connected before.

**The wiki is a persistent, compounding artifact.** The cross-references are already there. The contradictions have already been flagged. The synthesis already reflects everything you've fed it. It gets richer with every source you add and every question you ask.

You never write the wiki yourself. The LLM does the summarizing, cross-referencing, filing, and bookkeeping. You curate sources, direct attention, and ask the right questions. In practice: LLM agent on one side of your screen, Obsidian on the other. The LLM edits, you browse in real time.

## Why this fits PMs

PMs sit at the intersection of strategy, execution, and communication:

- **Synthesize across sources.** Connect a customer request to a roadmap item to a dependency to an exec priority. The wiki maintains these connections persistently.
- **Track the state of many things at once.** A dozen products, their statuses, who's adopting, what's blocked, what's next. Standardized product pages give you a consistent portfolio view.
- **Prepare for conversations fast.** An exec asks about readiness. A stakeholder wants adoption numbers. The wiki is always ready because the LLM kept it current.
- **Spot contradictions.** The roadmap says Q2 but the dependency owner said Q3. The adoption page says 14 teams but the exec deck says 12. The LLM catches these during ingest.

PMs abandon wikis and Notion databases because the maintenance burden grows faster than the value. Stale becomes untrustworthy, untrustworthy becomes unused. LLMs change the economics — they don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass. **The human curates and decides. The LLM does everything else.**

## Architecture

The workspace has six layers. Start with the first three; add the rest when you're ready.

### The knowledge base (start here)

**Raw sources** (`raw/`) — your curated inputs. PRDs, exec decks, meeting notes, customer feedback, Slack threads, architecture docs. Immutable — the LLM reads but never modifies. This is your source of truth.

**The wiki** (`wiki/`) — LLM-generated markdown files. Product pages, portfolio summaries, topic analyses, a timeline, a stakeholder map, an index, a log. The LLM owns this entirely. You read it; the LLM writes it.

**The schema** (`AGENTS.md`) — a configuration file that tells the LLM how the wiki is structured, what templates to follow, what workflows to execute. This is what makes the LLM a disciplined wiki maintainer rather than a generic chatbot. You and the LLM co-evolve this over time as you figure out what works for your domain.

### The workflow layers (add when ready)

**Inbox** (`inbox/`) — a transient signal queue. Drop Slack threads, meeting notes, Jira exports here. Run skills to process them, then move or delete. inbox/ is not raw/ — it's a processing queue, not a reference library.

**Skills** (`skills/`) — reusable AI workflows. Structured, multi-step processes: intake, synthesis, prioritization, PRD generation, adversarial review, competitive analysis, exec briefs, retros. Each skill is a markdown file the LLM follows when you invoke it by name (e.g., `/intake`, `/prd`). Skills connect all layers: they process inbox/ items, update wiki/ pages, and create workspace/ artifacts.

**Workspace** (`workspace/`) — active work products. PRDs, decision records, exec briefs, prototypes, retrospectives. Unlike wiki/ (permanent knowledge) or raw/ (permanent reference), workspace items have a lifecycle: created → refined → shipped → archived.

## Three core operations

### Ingest

Drop a new source into `raw/` and tell the LLM to process it. It reads the source, discusses takeaways with you, then updates every relevant wiki page — products, topics, timeline, index, log. A single exec deck might touch 10-15 pages.

Stay hands-on at first. Read the summaries, check the updates, guide the LLM on what to emphasize. Batch later once you trust the output.

### Query

Ask questions. The LLM reads the index, drills into relevant pages, synthesizes an answer with citations. Answers can take different forms — a markdown page, a comparison table, an exec brief, a timeline.

**File good answers back into the wiki.** The comparison you asked for, the dependency analysis, the exec brief — these are valuable and shouldn't disappear into chat history. Your explorations compound in the knowledge base just like ingested sources do.

### Lint

Periodically health-check the wiki. Look for: contradictions between pages, stale claims that newer sources have superseded, orphan pages with no inbound links, roadmap items past their target date, open questions now answered.

The LLM is good at suggesting new questions to investigate and new sources to look for. This keeps the wiki healthy as it grows.

## What this looks like in practice

You come back from a meeting where the engineering lead said the authentication service slips from Q1 to Q2. You drop meeting notes into `raw/notes/` and tell the LLM to ingest.

The LLM:
1. Updates `wiki/products/auth-service.md` — changes roadmap from Q1 to Q2.
2. Updates `wiki/topics/roadmap-timeline.md` — shifts the row.
3. **Flags a contradiction**: the group page still says "Auth and billing both target Q1."
4. Adds an open question: "Does the Q2 slip affect the mobile app's dependency on the new auth flow?"
5. Appends to `wiki/log.md`.

One meeting note. Five files touched. Three things you would have forgotten to update.

## Indexing and logging

Two special files help the LLM (and you) navigate the wiki as it grows:

**index.md** is content-oriented. A catalog of everything in the wiki — each page with a link and a one-line summary, organized by section. The LLM updates it on every ingest. When answering a query, the LLM reads the index first to find relevant pages, then drills into them. This works well at moderate scale (~100 sources, hundreds of pages) without needing embedding-based search.

**log.md** is chronological. An append-only record of what happened and when — ingests, queries, lint passes. Each entry starts with a consistent prefix (`## [2026-04-09] ingest | Meeting Notes`), making the log parseable and giving you a timeline of the wiki's evolution.

## Patterns that work well

**Product pages with standardized templates.** The single most valuable part. One page per product, same sections every time. YAML frontmatter enables Dataview queries (all products where `status: Alpha`, sorted by adoption). Open Questions sections accumulate over time into your 1:1 agenda and risk backlog.

**Cross-cutting topic pages.** Adoption trends, consolidated roadmap, cost/value, dependencies. These synthesize across products and are often the most useful pages for exec conversations.

**Dependency tracking.** A dedicated page with a status matrix: who owns it, what's blocked, current status. The LLM files dependency mentions here during ingest. Over time you get a single view of every external blocker.

**Filing good conversations.** After productive query sessions — comparisons, exec briefs, analyses — file them as wiki pages. Your explorations compound.

## Trust and limitations

The LLM will get things wrong:

- **Overstate certainty.** A tentative meeting comment becomes a firm commitment. A hedged number becomes precise.
- **Hallucinate links.** `[[products/something]]` to a page that doesn't exist. Obsidian shows broken links in red.
- **Silently rewrite.** Updating one page, the LLM may subtly shift meaning on others. This is the biggest risk.

Mitigations: Treat the wiki as a **working draft, not source of truth.** Use `git diff` after each ingest — the single best trust mechanism. Review critical claims (dates, numbers, commitments) against the raw source before sending to execs. Run lint periodically.

## Privacy and security

This is local-first — markdown files on your machine. But LLM API calls send content to the model provider (OpenAI, Anthropic, Google). If your docs contain confidential strategy, unreleased plans, or PII, your company's data classification policies apply. Local models (Ollama, LM Studio) keep everything on-device. Check your org's AI usage policy before ingesting sensitive documents.

## When to use this

This is for PMs managing a portfolio over months — many sources, compounding knowledge. It's overkill for one-off questions, single-product PMs with few sources, or quick document summarization. The value appears around 20+ sources and grows from there.

## Scaling

**Small (1-20 products, <50 sources):** `index.md` is enough. No extra tooling needed.

**Medium (20-100 products, 50-200 sources):** Add local search. Dataview queries become essential.

**Collaboration:** This is a personal tool by default. Sharing `wiki/` as read-only snapshots works fine. Shared wikis with multiple LLM editors are possible via git but need care around merge conflicts. Start personal, scale later.

## Tools

- **Obsidian** — `[[wiki-style links]]` become clickable, graph view shows wiki shape, Dataview plugin enables dynamic queries over frontmatter.
- **Obsidian Web Clipper** — browser extension that clips articles to markdown directly into `raw/`.
- **Git** — free version history. `git diff` after each ingest is the single best trust mechanism.
- **Marp** — markdown-based slide decks. Obsidian has a plugin. Generate presentations directly from wiki content.

## The schema file

The schema (`AGENTS.md`) encodes your PM mental model into rules the LLM follows:

1. **Page structure.** One page per product, one per group, cross-cutting topic pages, a stakeholder map.
2. **Page templates.** Consistent sections across all product pages — summary, status, capabilities, adoption, dependencies, roadmap, open questions.
3. **Workflows.** What happens on ingest, query, and lint.
4. **Skill routing.** When the PM invokes a skill, follow that skill's structured workflow instead of answering ad-hoc.
5. **Conventions.** `[[wiki-style links]]` for Obsidian. YAML frontmatter. Date formats.

A complete, ready-to-customize `AGENTS.md` is included in this template. Fill in the brackets and you're running.

## Note

This describes the pattern, not a fixed implementation. The only hard requirements: raw sources + a wiki + a schema + three operations (ingest, query, lint). Everything else — skills, workspace, inbox, topic pages, output formats — is optional and modular. Start simple, add structure as you learn what you need.

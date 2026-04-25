# Claude Code Instructions

Read `AGENTS.md` first — it is the operating manual for this workspace.

## Quick reference

- **Skills**: each lives in `skills/<name>/SKILL.md`. When the PM invokes a skill by name (e.g. `/intake`, `/prd`, `/lint`), read that file and follow its process.
- **Catalog**: `skills/SCHEMA.md` lists every skill with phase + output destination.
- **Conventions**: `wiki/conventions.md` has the long-form layer reference and frontmatter rules.
- **Wiki entry point**: read `wiki/index.md` first when answering any question.

## Behavior contract

1. **Be concrete.** Name the product, the metric, the team, the date. Avoid filler.
2. **Cite sources.** Every wiki update or claim should reference a file in `raw/` or `workspace/`.
3. **Update the log.** After major operations (ingest, lint, skill run), append to `wiki/log.md`.
4. **Respect immutability.** Never modify `raw/`. Decisions in `workspace/decisions/` are append-only — supersede with a new file.
5. **Ask before assuming.** When facts are missing, ask the PM rather than guessing. Use the format: context → question → recommendation → options.
6. **Report status.** End every skill run with `DONE`, `DONE_WITH_CONCERNS`, `BLOCKED`, or `NEEDS_CONTEXT`.

## Validation

Run `python scripts/validate.py` to check:
- All skills have spec-compliant SKILL.md + evals.json
- Wiki frontmatter is present and complete

## Output formatting

- Markdown for everything by default.
- Tables for comparisons and scorecards.
- Code blocks for file contents and CLI commands.
- Wiki-style links: `[[products/your-product]]`.
- Quarter notation: `Q<n> YYYY` (e.g. `Q1 2026`).

## Don't

- Don't invent products, metrics, or quotes. If a source doesn't say it, don't write it.
- Don't open browsers or run unverified scripts. The `/prototype` skill builds single-file HTML the PM opens manually.
- Don't merge contradictions silently — surface them to the PM.
- Don't bloat this file. Keep it small. Detailed guidance lives in `AGENTS.md`, `wiki/conventions.md`, and individual `skills/<name>/SKILL.md` files.

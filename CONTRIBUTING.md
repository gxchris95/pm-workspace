---
type: doc
title: Contributing
last_updated: 2026-04-25
---

# Contributing

This workspace is a personal PM operating system, but it's structured to be forkable, sharable, and extendable. Here's how to add to it.

## Adding a new skill

The fastest path is `/new-skill` (the skill-creator meta-skill):

1. In your agent, run: `/new-skill`
2. Answer the prompts: name, description, phase, output destination.
3. The skill scaffolds the folder, writes a starter SKILL.md and evals.json, and updates `AGENTS.md` and `skills/SCHEMA.md`.
4. Fill in the process steps, write the references, and add 10 should_trigger / 10 should_not_trigger eval cases.
5. Run `python scripts/validate.py` — must pass.

Manual path (if you can't run a skill):

1. Create `skills/<name>/`.
2. Add `SKILL.md` with compliant frontmatter (`name` matches dir, `description` ≤1024 chars and pushy on triggers, optional `metadata` block).
3. Add `evals.json` with `should_trigger` and `should_not_trigger` arrays (≥5 each, 10 each preferred).
4. Add a `references/` subfolder if SKILL.md exceeds ~100 lines — keep SKILL.md lean.
5. Register the skill in `AGENTS.md` (skills table) and `skills/SCHEMA.md` (skill catalog + sprint diagram).
6. Run `python scripts/validate.py`.

## Adding a wiki topic page

1. Create `wiki/topics/<slug>.md`.
2. Frontmatter must include `topic`, `last_updated`, `sources`.
3. Link the page from `wiki/index.md`.
4. Add cross-references from any related `wiki/products/*` pages.
5. Run `python scripts/validate.py`.

## Adding a new product page

1. Copy `wiki/products/_template.md` to `wiki/products/<product>.md`.
2. Fill in `product`, `status`, `adoption`, `last_updated`, `sources`.
3. Link from `wiki/index.md` and any topic pages it relates to.
4. Run `python scripts/validate.py`.

## Validation contract

`scripts/validate.py` enforces:

- Every skill folder has `SKILL.md` with spec-compliant `name` and `description`.
- Every skill folder has `evals.json` with non-empty `should_trigger` and `should_not_trigger`.
- Every wiki page has YAML frontmatter with `last_updated`.
- Product pages have `product`, `status`, `adoption`, `last_updated`, `sources`.
- Topic pages have `topic`, `last_updated`, `sources`.

CI (`.github/workflows/lint.yml`) runs the validator on every push and PR.

## Evals contract

`evals.json` is the trigger contract. `should_trigger` cases are user phrases that should activate this skill. `should_not_trigger` are phrases that should activate something else (or nothing).

Run `python scripts/run-evals.py` to surface all eval cases for manual review (and to spot phrases that match multiple skills' should_trigger — a sign one description needs sharpening).

## Style

- Markdown only. No HTML in content unless a skill explicitly requires it (e.g., `/prototype`).
- Code blocks for file contents and CLI commands.
- Tables for comparisons.
- Wiki-style links: `[[products/your-product]]`.
- Quarter notation: `Q<n> YYYY` (e.g., `Q1 2026`).
- ISO dates: `YYYY-MM-DD`.
- See `wiki/conventions.md` for the long form.

## Versioning

The workspace itself is versioned in `VERSION`. Bump on:

- **Patch** (`0.0.x`) — content additions, doc fixes, new skills that don't change the schema.
- **Minor** (`0.x.0`) — schema changes (new required frontmatter, new layer, validator rules).
- **Major** (`x.0.0`) — breaking changes that require existing forks to migrate.

## License

MIT. See `LICENSE`.

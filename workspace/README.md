# Workspace — Active Work Products

Live artifacts being actively worked on. Unlike wiki/ (permanent knowledge) or raw/ (permanent reference), workspace items have a lifecycle: created → refined → shipped → archived.

## Structure

```
workspace/
├── prds/           PRDs in progress (from /prd skill)
├── decisions/      Decision records — ADR-style (from /decision skill)
├── briefs/         Exec/stakeholder briefs (from /brief skill)
├── prototypes/     Quick prototypes, design specs (from /prototype skill)
├── decks/          Audience-tailored slide decks in Marp markdown (from /deck skill)
└── retros/         Sprint/quarter retrospectives (from /retro skill)
```

## Conventions

- **Filename**: `<product-or-topic>-<short-name>.md` (e.g., `auth-service-rbac-redesign.md`)
- **Frontmatter**: Every file has `status: Draft | In Review | Approved | Shipped | Archived`
- **Shipped artifacts**: Move to archive or link from relevant wiki/ page
- **Cross-reference**: Link to wiki product pages and raw sources. Use `[[wiki-style links]]`.

## What goes here vs. wiki/ vs. raw/

| Content | Goes in |
|---------|---------|
| PRD being written | workspace/prds/ |
| Shipped PRD (for reference) | raw/roadmaps/ or link from wiki product page |
| Product knowledge, status, adoption | wiki/products/ |
| Decision in progress | workspace/decisions/ |

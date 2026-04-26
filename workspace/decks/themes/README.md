# Deck themes

Drop Marp theme CSS files here (e.g. `corporate.css`, `dark.css`).

Reference from a deck's frontmatter:

```yaml
---
marp: true
theme: corporate
---
```

Marp resolves the theme by name when `--theme-set themes/` is passed to the CLI (see `skills/deck/scripts/render.sh`).

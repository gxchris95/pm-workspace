# Import scripts

Optional helpers that drop content into `inbox/` with the right naming and frontmatter so `/intake` can process them.

These are scaffolds — fork and adapt to your tooling. They don't require an MCP server.

## Available

| Script | What it does |
|--------|--------------|
| `slack-export.py` | Ingest a Slack JSON export → one inbox file per thread |
| `jira-csv.py` | Ingest a Jira CSV export → one inbox file per ticket |

## Usage

```bash
python scripts/import/slack-export.py <export.zip>
python scripts/import/jira-csv.py <export.csv>
```

Each script writes to `inbox/<source>/YYYY-MM-DD-<short>.md`. Then run `/intake` on the workspace inbox.

---
skill: synthesize
trigger: /synthesize
phase: Synthesize
inputs: [multiple intake cards, inbox/ items, wiki/ pages, raw/ sources]
outputs: [synthesis report with themes, contradictions, gaps, recommendations]
output_to: [wiki/ (updated pages), workspace/ (if new artifacts needed)]
---

# Synthesize — Find Patterns Across Signals

## When to use

You have multiple inputs — intake cards, inbox items, wiki pages, raw sources — and need to find what's really going on. What themes keep surfacing? What contradicts? What's missing?

## Process

### 1. Gather inputs

Read all specified sources. If no sources specified, default to:
- All items in `inbox/`
- Recent intake cards
- Open items in `workspace/prds/`

### 2. Extract themes

Group related signals. For each theme:

```markdown
### Theme: [name]

**Signal count**: [how many sources mention this]
**Sources**: [list of sources]
**Core insight**: [one sentence — what is this theme really about?]
**Representative quotes**: [2-3 direct quotes from different sources]
**Affected products**: [link to wiki product pages]
**Current state**: [what the wiki says about this today]
```

### 3. Find contradictions

Where do sources disagree? Be specific:

```markdown
### Contradiction: [topic]

- **Source A** says: [quote]
- **Source B** says: [quote]
- **Resolution needed**: [what decision or investigation would resolve this]
```

### 4. Identify gaps

What's frequently asked about but has no answer in the wiki? What problems are described but no product addresses? What assumptions are made that nobody's validated?

```markdown
### Gap: [description]

**Evidence**: [which sources surface this gap]
**Impact**: [who's affected, how badly]
**Suggested action**: [investigate, add to roadmap, update wiki, create PRD]
```

### 5. Volume analysis

Rank themes by signal strength:

```markdown
## Signal Strength

| Theme | Sources | Teams Affected | Urgency | Trend |
|-------|---------|---------------|---------|-------|
| ... | 7 | 4 teams | High | ↑ Growing |
| ... | 3 | 1 team | Medium | → Stable |
```

### 6. Generate recommendations

Prioritized list of actions. Each recommendation should be concrete:
- "Update `wiki/products/genai-gateway.md` — latency section is stale, 3 sources contradict it"
- "Create PRD for X — 5 teams have asked, no product addresses this"
- "Schedule decision: A vs B — two valid approaches, need PM call"

## Output format

```markdown
# Synthesis Report — [DATE]

## Inputs analyzed
[list]

## Top Themes
[ranked by signal strength]

## Contradictions
[if any]

## Gaps
[if any]

## Recommendations
[prioritized action list]
```

## Tips

- Don't average out contradictions — surface them. Contradictions are where the interesting decisions live.
- "Everyone wants this" ← count the sources. If it's 2, say 2.
- Look for what's NOT being said. Absence of signal about a launched product might mean low adoption or low awareness.
- Cross-reference `wiki/topics/roadmap-timeline.md` — are the themes aligned with the roadmap, or is there drift?

## See also

- `/intake` — process raw signals before synthesizing
- `/prioritize` — rank the themes and recommendations
- `/prd` — spec out the top-priority items

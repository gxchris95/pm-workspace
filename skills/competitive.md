---
skill: competitive
trigger: /competitive
phase: Discover
inputs: [product or capability to analyze, competitor names/URLs (optional), market context]
outputs: [competitive landscape analysis with comparison table, gaps, and recommendations]
output_to: [workspace/briefs/<product>-competitive.md or inline]
---

# Competitive — Market Landscape Analysis

## When to use

You need to understand how a product or capability compares to what exists in the market. Useful for: strategic planning, PRD justification, exec presentations, build-vs-buy decisions, or "what are we missing?"

## Process

### 1. Define the scope

Clarify what you're benchmarking:
- **Product-level**: "How does [your product] compare to alternatives?"
- **Capability-level**: "How does our approach to [feature] compare?"
- **Category-level**: "What does the [market category] landscape look like?"

### 2. Read internal state

Read the relevant wiki product page(s) and any PRDs. Understand: what we have today, what's on the roadmap, what our differentiators are, and what our known gaps are.

### 3. Map the landscape

Identify competitors, alternatives, and adjacent solutions. Group them:

```markdown
## Landscape Map

### Direct Competitors
Products solving the same problem for a similar audience.
| Player | What they offer | Maturity | Target audience |
|--------|----------------|----------|-----------------|

### Adjacent Solutions
Products that overlap partially or could expand into our space.
| Player | Overlap area | Threat level |
|--------|-------------|-------------|

### Open Source / Standards
Relevant open-source projects, protocols, or standards.
| Project | Relevance |
|---------|-----------|
```

### 4. Feature comparison

Build a detailed comparison table:

```markdown
## Feature Comparison

| Capability | Our Product | Competitor A | Competitor B | Competitor C |
|-----------|------------|-------------|-------------|-------------|
| [feature] | ✅ / ⚠️ Partial / ❌ | ... | ... | ... |
```

Use:
- ✅ = fully supported
- ⚠️ = partial or planned
- ❌ = not available
- 🔜 = on roadmap (with date if known)

### 5. Differentiation analysis

```markdown
## Where We Lead
- [capability] — [why we're ahead, with specifics]

## Where We're At Parity
- [capability] — [what competitors also offer]

## Where We Trail
- [capability] — [what competitors have that we don't]

## Unique to Us
- [capability that no competitor has, and why it matters]
```

### 6. Gap analysis

```markdown
## Gaps and Opportunities

| Gap | Competitors Who Have It | Impact if We Don't Address | Effort to Close |
|-----|------------------------|---------------------------|-----------------|
```

### 7. Strategic recommendations

```markdown
## Recommendations

### Double down (our strength, high value)
- [capability] — because [reasoning]

### Close the gap (competitor strength, our weakness, high impact)
- [capability] — because [reasoning]

### Ignore (low impact, high effort)
- [capability] — because [reasoning]

### Watch (emerging, uncertain)
- [trend/capability] — revisit in [timeframe]
```

### 8. Save (if requested)

Save to `workspace/briefs/<product>-competitive.md`.

## Tips

- Acknowledge uncertainty. If you don't have reliable information about a competitor, say "unverified" rather than guessing.
- Focus on capabilities and outcomes, not feature checklists. "They support 50 models" is less useful than "their model catalog updates within 24 hours of provider launch."
- The PM will often know competitors better than the LLM. Ask clarifying questions when competitor claims seem ambiguous.
- Update the relevant wiki product page's "Open Questions" section if the analysis surfaces gaps worth tracking.
- Don't confuse "they announced it" with "they shipped it." Check for production availability.

## See also

- `/challenge` — use competitive findings to stress-test your own product
- `/brief` — include competitive context in stakeholder communications
- `/prd` — competitive gaps may drive new PRD requirements

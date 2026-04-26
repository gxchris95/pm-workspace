---
name: competitive
description: Build a competitive landscape analysis with market mapping, feature comparison table, differentiation breakdown, gap analysis, and strategic recommendations. Use this skill whenever the user asks how a product or capability compares to alternatives, wants to benchmark against competitors, asks "what are others doing", needs market context for a strategic decision, or wants build-vs-buy input.
metadata:
  phase: Discover
  inputs: [product or capability to analyze, competitor names/URLs (optional), market context]
  outputs: [competitive landscape analysis with comparison table, gaps, and recommendations]
  output_to: workspace/briefs/<product>-competitive.md (or inline if PM declines to file)
---

# Competitive — Market Landscape Analysis

## When to use

You need to understand how a product or capability compares to what exists in the market. Useful for: strategic planning, PRD justification, exec presentations, build-vs-buy decisions, or "what are we missing?"

## Process

1. **Define the scope.** Product-level ("how does X compare?"), capability-level ("how does our approach to feature Y compare?"), or category-level ("what does the market for Z look like?").
2. **Read internal state.** Read the relevant `wiki/products/<product>.md` and any in-flight PRDs. Note current capabilities, roadmap, differentiators, and known gaps.
3. **Map the landscape.** Identify direct competitors, adjacent solutions, and open-source/standards. Use the Landscape Map block in `references/templates.md`.
4. **Build the feature comparison.** Use the Feature Comparison block in `references/templates.md`. Be specific — capabilities and outcomes, not feature checklists.
5. **Differentiation analysis.** Where we lead / parity / trail / unique. Block in `references/templates.md`.
6. **Gap analysis.** Use the Gaps table. Score impact and effort.
7. **Strategic recommendations.** Double down / close the gap / ignore / watch. Block in `references/templates.md`.
8. **Save** to `workspace/briefs/<product>-competitive.md` if requested.

## Tips

- Acknowledge uncertainty. If you don't have reliable information about a competitor, say "unverified" rather than guessing.
- Focus on capabilities and outcomes, not feature checklists. "They support 50 models" is less useful than "their model catalog updates within 24 hours of provider launch."
- The PM will often know competitors better than the LLM. Ask clarifying questions when competitor claims seem ambiguous.
- Update the relevant wiki product page's "Open Questions" section if the analysis surfaces gaps worth tracking.
- Don't confuse "they announced it" with "they shipped it." Check for production availability.

## See also

- `references/templates.md` — copy-paste section templates for landscape, feature comparison, differentiation, gaps, recommendations
- `/challenge` — use competitive findings to stress-test your own product
- `/brief` — include competitive context in stakeholder communications
- `/prd` — competitive gaps may drive new PRD requirements

---
name: prototype
description: Build a quick interactive HTML prototype or detailed design spec from a PRD or feature description. Use this skill whenever the user wants something tangible — a prototype, mockup, demo, clickable preview, or spec — to share with stakeholders, validate a flow, or hand off to engineering. Mode 1 = self-contained HTML; Mode 2 = markdown design spec for non-visual features (APIs, data models, backend services).
metadata:
  phase: Prototype
  inputs: [PRD, design spec, feature description, or freeform idea]
  outputs: [interactive HTML prototype or detailed design spec]
  output_to: workspace/prototypes/<name>.html (Mode 1) or workspace/prototypes/<name>.md (Mode 2)
---

# Prototype — Quick Interactive Prototype or Design Spec

## When to use

You have a concept that needs to be made tangible — either for stakeholder alignment, user testing, or eng handoff. Two modes: code (HTML prototype) or spec (detailed design document).

## Mode 1: HTML Prototype

For UI-facing features where seeing is believing.

### 1. Read the input

Understand the core user flow. Identify:
- Who is the user?
- What are they trying to do?
- What's the happy path?
- What are the key decision points?

### 2. Scope ruthlessly

Prototype the **core flow only** — not edge cases, not error states, not admin views. Ask: "What's the one screenshot that would convince a stakeholder this is worth building?"

### 3. Build it

Generate a single self-contained HTML file:
- **No external dependencies** — inline CSS, inline JS
- **Responsive** — works on desktop and mobile viewports
- **Interactive** — clickable buttons, form inputs, state changes
- **Realistic data** — use plausible product names, team names, metrics from the wiki
- **Clean visual design** — use a neutral design system (system fonts, muted palette, clear hierarchy)

Structure:
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Prototype Name]</title>
  <style>/* all styles inline */</style>
</head>
<body>
  <!-- prototype content -->
  <script>/* interactivity */</script>
</body>
</html>
```

### 4. Annotate

Add a hidden comment block at the top of the file:
```html
<!--
  PROTOTYPE: [name]
  DATE: YYYY-MM-DD
  SOURCE: [PRD or description that inspired this]
  SCOPE: [what this covers]
  NOT COVERED: [what's intentionally left out]
-->
```

### 5. Self-check before delivering

The LLM cannot open a browser. Instead, validate by inspection:
- Every `<a href>` and `<button onclick>` references a defined target/handler
- All inline `<script>` referenced functions are defined
- No external CDN URLs or `<img src>` to remote hosts (must be inline data URIs or omitted)
- HTML is well-formed (closing tags match)
- No placeholder text like `lorem ipsum` left in user-visible areas

Tell the PM how to open it: `open workspace/prototypes/<name>.html` (macOS) or double-click in their file manager.

### 6. Save

Save to `workspace/prototypes/<name>.html`.

## Mode 2: Design Spec

For APIs, backend features, data models, or anything non-visual.

### 1. Read the input

Same as above — understand the user, the flow, the goal.

### 2. Write the spec

```markdown
---
prototype: [name]
type: Design Spec
date: YYYY-MM-DD
source: [PRD or input]
status: Draft
---

# [Feature Name] — Design Spec

## Overview
One paragraph: what this is, who it's for, what it enables.

## User Flow
Step-by-step walkthrough. Number each step. Note decision points.

## Data Model
Tables, fields, relationships. Use markdown tables or ASCII diagrams.

## API Surface (if applicable)
Endpoints, methods, request/response shapes. Use code blocks.

## Key Interactions
How components talk to each other. Sequence diagram if helpful:
```
User → Frontend → API → Database
                    ↓
            Service Registry
```

## States and Transitions
What states can this thing be in? What transitions between them?

## Open Design Questions
What's unresolved? What needs PM/eng/design input?
```

### 3. Save

Save to `workspace/prototypes/<name>.md`.

## Tips

- A prototype is disposable. Its purpose is to learn, not to ship. Don't over-polish.
- If you're spending more than 20 minutes describing the prototype, you should just build it (Mode 1).
- Use real data from the wiki — real product names, real team counts, real metrics. Fake data undermines credibility.

## See also

- `/prd` — the PRD that this prototype validates
- `/challenge` — stress-test the prototype's assumptions
- `/brief` — present the prototype findings to stakeholders

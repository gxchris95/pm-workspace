# Slide Pattern Catalog

Reusable slide types with action-title examples. Pick patterns; don't invent novel ones.

---

## 1. Title slide

- **Purpose**: set frame, name the speaker, name the date.
- **Action title**: the deck's headline message (not just the topic).
- **Bad**: "Q1 Roadmap Review"
- **Good**: "Q1 shipped 4 of 5 commitments; the slip blocks Q2 in two ways."

---

## 2. Executive summary / TL;DR

- **Purpose**: the whole deck on one slide. Required for exec/board.
- **Pattern**: 1 sentence answer + 3 bullet supports + 1 ask.
- **Action title**: the answer in one sentence.
- **Body**: 3 bullets, each ≤12 words, each independently meaningful.

---

## 3. Situation

- **Purpose**: ground the audience in the current state they accept.
- **Pattern**: 1 chart or 1 number + 1 line of context.
- **Action title**: the headline metric stated as a sentence.
- **Bad**: "Adoption Trends"
- **Good**: "Daily active users grew 38% QoQ to 1.2M."

---

## 4. Complication

- **Purpose**: introduce what's changed, broken, or at risk.
- **Pattern**: the change, the evidence, the implication.
- **Action title**: the complication stated plainly.
- **Bad**: "Challenges We're Facing"
- **Good**: "Auth slipping to Q2 blocks mobile launch and the partner deal."

---

## 5. Recommendation

- **Purpose**: the answer.
- **Pattern**: the recommendation in 1 sentence + 3 reasons + the cost/effort.
- **Action title**: the recommendation as a verb-led sentence.
- **Bad**: "Proposed Path Forward"
- **Good**: "Cut scope on auth-v2 to ship core flows in Q1; defer SAML to Q2."

---

## 6. Evidence / data

- **Purpose**: prove a point with one chart or table.
- **Pattern**: one chart, one takeaway, one source.
- **Action title**: what the chart proves, not what it shows.
- **Bad**: "Conversion Funnel"
- **Good**: "Step 3 drop-off (42%) is the single biggest conversion leak."
- **Rules**: label axes, cite source in footer, no chart junk, no 3D.

---

## 7. Comparison

- **Purpose**: compare options or competitors.
- **Pattern**: 2x2 matrix or side-by-side table.
- **Action title**: the comparison's verdict, not the dimensions.
- **Bad**: "Build vs. Buy"
- **Good**: "Buying gets us to market 3 months sooner with comparable lifetime cost."

---

## 8. Timeline / roadmap

- **Purpose**: show what happens when.
- **Pattern**: horizontal timeline with milestones, dependencies marked.
- **Action title**: the headline of the plan.
- **Bad**: "Q1–Q4 Plan"
- **Good**: "Three releases land in Q1; the Q2 release depends on auth-v2."
- **Rules**: dates ISO format; mark dependencies and risks.

---

## 9. Risks / mitigations

- **Purpose**: show the team has thought about what can go wrong.
- **Pattern**: table — Risk | Likelihood | Impact | Mitigation.
- **Action title**: top risk in plain language.
- **Bad**: "Risks"
- **Good**: "Top risk: vendor lock-in if we adopt their auth library."

---

## 10. Asks / next steps

- **Purpose**: name what the audience must do.
- **Pattern**: who / what / when, in a list.
- **Action title**: the headline ask.
- **Bad**: "Next Steps"
- **Good**: "We need approval to redirect 2 engineers from Project X by Friday."
- **Rules**: every ask names a person and a date.

---

## 11. Section divider

- **Purpose**: signal a transition.
- **Pattern**: large title slide with the section's headline.
- **Use**: only in decks ≥10 slides. Skip in short decks.

---

## 12. Appendix

- **Purpose**: detail kept out of the main flow but available for Q&A.
- **Pattern**: clearly labeled "Appendix" divider, then detail slides.
- **Rules**: every appendix slide must answer a likely question. No dumping.

---

## Anti-patterns (don't ship these)

- **"Agenda"** for an exec audience under 10 slides — wastes a slide.
- **"Thank you"** end slide — end on the ask or next step.
- **"Questions?"** end slide — implied; don't waste a slide.
- **Wall of text** — if it's prose, it's a brief, not a slide.
- **Decorative imagery** — adds noise, not signal.
- **Bullet sprawl** (>5 bullets) — split or convert to a table.
- **3D charts, drop shadows, gradient backgrounds** — visual noise.
- **Logos parade** — only include logos if the logo itself is the message.

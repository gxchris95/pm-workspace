# Design Self-Review Checklist

Run this before saving the deck. Every check must pass for a deck to be Reviewed-status.

## Structure (Pyramid + MECE)

- [ ] First content slide states the answer in one sentence.
- [ ] Section structure is mutually exclusive (no overlap) and collectively exhaustive (no gaps).
- [ ] Narrative follows Situation → Complication → Resolution (or 1-pager: ask → 3 supports → next steps for ≤5-slide decks).
- [ ] Slide count matches the audience profile budget (`references/audiences.md`).

## Titles (action-title rule)

- [ ] Every slide title is a complete sentence with a verb.
- [ ] Every title states the slide's conclusion, not its topic.
- [ ] No title contains generic words alone ("Overview", "Update", "Status", "Background", "Agenda" — exception: agenda for board/partner if expected).
- [ ] Reading only the titles tells the full story.

## Glance test (Duarte)

- [ ] Every slide passes the 3-second test — point grasped at a glance.
- [ ] No slide has more than ~30 words of body text.
- [ ] Type is large enough to read from the back of the room or on a small mobile screen.
- [ ] No slide has more than one chart or one table.

## Signal-to-noise (Reynolds)

- [ ] No decorative imagery, stock photos, or "filler" icons.
- [ ] No 3D charts, drop shadows, gradient backgrounds.
- [ ] No animations except where they reveal information step-by-step with purpose.
- [ ] Color is used to encode meaning (one dominant color, one accent), not to decorate.
- [ ] Every chart has axis labels, units, source, and a takeaway baked into the title.

## Evidence

- [ ] Every quantitative claim cites a source in the slide footer.
- [ ] Every direct quote names the speaker and links to the raw source.
- [ ] No invented numbers, no invented quotes, no "approximately" without a real underlying number.
- [ ] "Unverified" or "estimated" is labeled when the number isn't firm.

## Audience fit

- [ ] Vocabulary matches the audience profile (no internal jargon to externals).
- [ ] Depth matches the time budget.
- [ ] What's in scope vs. appendix is correct for the audience.
- [ ] Length tracks the profile (exec ≤10, board ≤15, all-hands ≤25).

## Asks and outcomes

- [ ] The deck has an explicit ask slide with named owners and dates.
- [ ] No "Thank you" slide, no "Questions?" slide.
- [ ] The closing slide either repeats the ask or names the next concrete step.

## Provenance

- [ ] `sources:` frontmatter lists every wiki page, raw source, and workspace artifact used.
- [ ] No source listed in frontmatter is unused in the deck.
- [ ] Filename matches `<YYYY-MM-DD>-<audience>-<topic>.md` and lives in `workspace/decks/`.

## Final read

- [ ] Read the deck out loud. Anything that doesn't survive being read aloud gets cut.
- [ ] Cut one more slide than feels comfortable. The deck is now the right length.

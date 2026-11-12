# 01 — Clubhouse Editorial

**Thesis:** Every analysis comes back as a coach's letter about your swing, typeset like a long-form golf journal, and the letter says exactly how sure it is.

## Rationale

This direction is for the 11-handicap who practises after work and has not had a lesson in years. He does not want a dashboard. He wants the feeling of a good coach sitting down and writing to him about one swing. A journal fits an honest coach because editorial form already has the habits honesty needs: captions say what a plate shows, footnotes say where a claim comes from, and corrections are printed openly. So the fault chain is a typeset sidebar with footnote evidence markers (¹ ² ³), every measurement sits next to its confidence band, and "Cannot analyse" and "No verified fault found" are set as headlines in the same voice as a verified fault, not as error states. The engraved line-art golfer, drawn as plates with oxblood hairlines (the address line and the 7% bracket), makes the key frames feel like evidence rather than decoration.

## Palette

| Hex | Role |
|---|---|
| `#F3EEE3` | Paper: page background |
| `#FBF8F1` | Sheet: letter sheet, inputs, chat letters |
| `#E9E1D1` | Deep paper: sidebars (fault chain, filming checklist), honesty band |
| `#ECE4D4` | Plate ground behind key frames and diagrams |
| `#1B2420` | Ink: body text, engraving outlines |
| `#1E4636` | Pine: brand, primary buttons, links, pose lines, confidence marks |
| `#4E5D55` | Soft ink: secondary text, captions, datelines (≥4.5:1 on paper) |
| `#7B2331` | Oxblood: the single accent. Faults, feel cue, measurement hairlines, drop caps, unverified labels, destructive actions |
| `#C8BDA8` | Hairline rules |

## Typography

- **Fraunces** (300–600, italic): display. Headlines ("Early extension."), plate captions, the feel-cue pull quote, link names in the fault chain.
- **Source Serif 4** (400/600, italic): long-form reading text. The explanation letter, chat replies, standfirsts.
- **Hanken Grotesk** (400–700): quiet UI sans. Navigation, buttons, labels, datelines, measurements, confidence lines.

## Signature moves

1. **The result is a letter.** Drop cap opening, a standfirst that states the measurement and threshold, and the feel cue set as an oxblood pull quote between hairlines.
2. **Plates as evidence.** Address and impact appear as captioned engraved plates (Plate I and Plate II). An oxblood address line runs up from the backside, and at impact a bracket marks the 7% shift (threshold 4%). The text refers back to the plates by name.
3. **Fault chain with footnotes.** Likely cause, then mechanism, then fault, typeset as a sidebar. Each link carries a footnote marker that resolves to its evidence and confidence band.
4. **Confidence marks.** Three small squares (■■■ / ■■□ / ■□□) sit beside the words "Confidence: high/medium/low" on every measurement, everywhere.

## How the AI chat lives here

"Ask your coach" sits in the right margin column under the fault chain and reads as correspondence. Each message has a header ("FROM RORY · 18:42" or "YOUR COACH"). Coach replies are set on letter sheets and cite the same footnotes and plates as the article ("Plate II … 7% of your body height²"). A seal-and-tick line reads "Answers are based only on this analysis." The sample includes a grounded refusal ("Will this fix my slice?" → "I can't tell from this analysis…"). Suggested prompts are hairline pills. The compose box reads "Write to your coach about this analysis…" with the reminder "No new faults, numbers or drills." On the phone, the chat is a button below the summary.

## Risks / trade-offs

- **Reading-heavy.** The letter voice rewards a sit-down read. At the range, a player with 30 seconds needs the phone summary (headline, plates, feel cue, drill) to carry the moment. The full letter has to stay one tap away and never be the only path.
- **Line-art golfer fidelity.** Engraved figures look calm, but the real key frames will be video stills. The production design has to let real frames sit inside the same plate frame and hairline system without clashing with the engraved style. Engraving may end up reserved for marketing and diagrams.
- **Editorial tone can read as old-fashioned or "premium club"** to younger players. The restraint (one accent, no gold or crests) has to be held firmly so it reads as calm authority, not exclusivity.

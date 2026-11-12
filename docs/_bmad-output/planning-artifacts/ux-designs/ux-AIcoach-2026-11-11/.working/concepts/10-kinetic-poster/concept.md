# 10 · Kinetic Poster

**Thesis:** The swing becomes a poster. A stroboscopic arc and two overlaid silhouettes show at a glance what you felt and what the video measured.

## Rationale

This is for the 11-handicap who practises at the range after work. He doesn't want to read graphs. He wants to *see* the fault the way a coach would draw it on a whiteboard, only bolder. Geometric modernism suits an honest coach because it can only state what it can draw exactly. The address ghost is an outline, the impact body is solid, and the 7% hip shift is one bold arrow drawn to the figure's real scale. Nothing is airbrushed or implied. The confidence system is equally literal: a filled circle means high, a half circle means medium and an outline means low, so honesty is part of the graphics and not small print. Big expressive type gives the verdict ("EARLY EXTENSION", "CANNOT ANALYSE", "No verified fault found.") the weight of a headline. The working parts (upload, checklist, chat) stay crisp and quiet so the app remains usable on a phone at the range.

## Palette

| Hex | Role |
|---|---|
| `#F3EFE6` | Paper: page ground |
| `#E9E3D5` | Paper 2: quiet surfaces, mobility block, toggles |
| `#15171E` | Ink: type, rules, buttons, dark bands (honesty, analysing, key frames on `#1C1F29`) |
| `#2343D8` | Cobalt: measured mechanism, address ghost, chat header, checklist, progress done |
| `#EE4B2B` | Vermilion: the fault, impact silhouette, primary "Analyse swing", rejection |
| `#FFC531` | Yellow: the poster disc behind the golfer, suggested-prompt chips, "possible" badge |
| `#C8D0F5` | Cobalt light: unverified observations, captions on cobalt |

## Typography

- **Unbounded** (600/800/900, tracking -0.03em): display headlines, verdicts, measurements ("7%"), section titles.
- **Instrument Sans** (400/500/600/700): body text, UI, labels, chat, data captions.

## Signature moves

1. **Stroboscopic swing arc.** A fan of club-shaft lines around the hand path is drawn like a chronophotograph, with faded body exposures (half-way back, top, address) behind a solid impact figure. The same arc drives the logo mark, the dropzone and the **analysing progress**, which fills five segments (pose → swing events → measurements → rule table → explanation) along the swing arc.
2. **Ghost vs solid overlay.** The address body is an outline and the impact body is solid. A dashed backside line and a solid backside line sit side by side, with a bold arrow and a giant "7%" between them. The hip shift is drawn at the figure's true scale (7% of figure height).
3. **Confidence glyphs.** Filled, half and outline circles are used everywhere: results, the fault chain, the library and the chat source chips.
4. **Colour-field fault blocks.** Each of the three faults is a flat colour block with one quarter-circle corner.

## How the AI chat lives here

On desktop the chat is a crisp white panel next to the result. On mobile it is a cobalt bar pinned to the bottom of the screen. Its header is cobalt with a small swing-arc mark, and directly under it a paper band states **"Answers are based only on this analysis. It will not add faults, numbers or drills."** Each coach answer is marked by a cobalt dot and line and ends with outlined **source chips** that point back into the result ("Impact key frame", "Hips 7% · high", "Wall drill", "Fault chain · likely cause"). This makes grounding visible. When asked, the coach also says what it is *not* sure about (restricted hip rotation is a likely cause, medium confidence). Suggested prompts are yellow pills. On the no-fault page, an unverified observation sends the player to the chat to ask what it is based on.

## Risks / trade-offs

- **Unbounded is very wide.** Long fault names and translated copy will need smaller sizes or more line breaks. Mobile headlines are capped at about 36px and use two lines.
- **Poster energy versus calm reading.** The overlapping type and arc in the hero, and the dense chronophotograph, can feel busy. Keep the stroboscope to hero and result moments only, never in forms.
- **Contrast limits on vermilion.** White text on vermilion only passes at large sizes, so small text on vermilion is always ink. Yellow is never used for text on paper.

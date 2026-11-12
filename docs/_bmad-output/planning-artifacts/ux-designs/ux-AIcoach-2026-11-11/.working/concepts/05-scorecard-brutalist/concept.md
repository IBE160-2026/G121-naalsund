# 05 · Scorecard Brutalist

**Thesis:** Every swing gets one honest scorecard: ruled cells, a fixed set of rows, and a red pencil circle only where the rule table says so.

## Rationale

AIcoach is for +2 to 15 handicap golfers who already fill in a scorecard every round, so the scorecard is a form they read without being taught. A card has a structure that cannot bend: the same three rows (early extension, loss of posture, over the top) and the same columns (measurement, threshold, confidence, evidence, mark) appear on every result. A fault cannot be slipped in and a doubt cannot be hidden. Empty cells, dashes and "no score" are shown as plainly as a verified fault, which is the product's honesty made visible: "Cannot analyse" is a card with nothing scored and a red line through it, and "No verified fault found" is three dashes. Paper, black rules and one scorer's red give a raw, high-contrast surface that still reads on a phone in daylight at the range. The heavy grotesk numerals make the one number that matters (7% against a 4% threshold) the loudest thing on the page.

## Palette

| Hex | Role |
|---|---|
| `#F4F1EA` | Paper: every page background and cell fill |
| `#111111` | Ink: rules, borders, header bars, body text, filled confidence cell |
| `#D2231E` | Scorecard red: the scorer's circle (verified), red body lines on key frames, rejection headline, warnings, destructive actions |
| `#66645E` | Pencil grey: thresholds, secondary notes, the address reference line, the player's typed questions in the chat |
| `#CBC7BD` | Faint rule (a lighter pencil): ruled lines in the notes section only |

## Typography (Google Fonts)

- **Archivo Black**: display voice and big numerals (`7%`, `EARLY EXTENSION`, `CANNOT ANALYSE`, `3 × 10`).
- **Archivo** 400/600/700/800: tiny tracked caps cell labels, controls, body copy, the coach's answers.
- **Courier Prime** 400/700: typewriter text for data only: measurements, timestamps, file metadata, evidence lines, the player's own notes.

## Signature moves

1. **Scorer's marks as the status system.** Circled in red = verified fault, boxed = possible fault, dash = not found. A legend under each card explains it, the same way a golf scorecard marks birdies and bogeys.
2. **The confidence band as three cells, H M L.** One is filled black. It sits in its own column on every row and on every link of the fault chain.
3. **The page is a card.** The nav is the card's header row. Player, handicap, club, date and frame rate are filled-in header fields. The fault chain is a table with row headers (link, status, evidence, key frame, confidence). Drill and mobility are "next session" cells with reps set like a score (`3 × 10`).
4. **Pose skeleton key frames.** Keypoints and bones, like the pose model's output. A dashed pencil line marks the hip at address and a red line marks the hip at impact, with the 7% gap shown with arrows.

## How the AI chat lives here

The chat is the **notes section at the bottom of the card**: ruled lines with a red margin, speaker tags in the margin column (RORY / COACH). The player's questions are in pencil-grey typewriter text and the coach's answers in ink. The header bar reads "Answers are based only on this analysis". Under each answer, a **"Based on"** row of small cells names the exact parts of the card it used (hips toward the ball 7% · high, impact frame 1.79 s, posture angle 6°, wall drill). This makes the grounding something the player can check. One sample exchange shows the coach declining a question the card cannot answer ("This analysis does not look at your grip…"). Suggested prompts sit as outlined cells above a ruled input with an ASK cell.

## Risks / trade-offs

- **Density and severity.** A brutalist grid can feel like a form or a tax return. A golfer looking for warmth or motivation may find it cold, and the friendlier coach voice has to come entirely from the copy and the feel cue.
- **Thick rules and small caps labels.** The 12px tracked labels and mono data are at the edge of what reads well outdoors on a phone. The mobile version needs larger labels and fewer columns than this sketch shows.
- **The metaphor depends on golf literacy.** Circled/boxed marks only feel natural to players who keep score. The legend is needed, and the "possible = boxed" mark could be read as a bogey (a bad score) rather than "watch this".

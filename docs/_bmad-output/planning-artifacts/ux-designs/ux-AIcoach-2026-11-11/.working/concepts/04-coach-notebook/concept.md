# 04 — Coach's Notebook

**Thesis:** Your swing, printed out and marked up by a coach. The app measures in clean white lines, and the coach writes over them in red marker.

## Rationale

AIcoach is for the 2–15 handicap golfer who hasn't had a lesson in years and practises alone at the range. What they miss is not data. They miss a person who looks at their swing and says "there, that's it." This concept puts the product in that person's notebook: key frames printed and taped to grid paper, a red circle round the hips, a hand-written "hips →", the feel cue on a sticky note, the drill on an index card. Honesty comes from the material itself. The **white lines are the app's measurements, the red marks are the coach's interpretation**, and every page keeps those two layers visibly apart, so the player can always tell what was measured from what was inferred. The hand-made feel makes "Cannot analyse" and "No verified fault found" read as a coach's candid note, not an error screen. The page structure stays strict (one column of verdict, then evidence, then practice), so it reads as warm without getting messy.

## Palette

| Hex | Role |
|---|---|
| `#F7F2E6` | Notebook paper (page ground) |
| `#DCE5E8` | Grid rule lines (24 px squares) |
| `#E5A99E` | Paper margin line |
| `#1E2833` | Ink: text, primary buttons, sketch strokes |
| `#545A62` | Pencil: secondary text, measurements context |
| `#C8402A` | Coach's red marker: fault, annotations, rejection, destructive actions |
| `#2F7A4D` | Green: verified, confidence high, reps, ticks |
| `#94550C` | Amber: confidence medium, possible fault, inferred links |
| `#F8E07A` | Sticky note (feel cue) |
| `#FFFDF8` / `#C6D9E5` / `#E7A196` | Index card, blue card rules, red header rule |
| `#2A4A9A` | Blue ballpoint: player's chat messages, links to the filming guide |
| `#E2D3A6` | Masking tape |
| `#CED7D1` / `#7C9768` / `#252E2A` | Key-frame photo: sky, range grass, golfer silhouette |

## Typography (Google Fonts)

- **Literata** (400, 600, 700, italic 400). The voice for all content: headings, verdicts, evidence, explanation, UI. A sturdy book face that stays readable at 13 px on a phone in daylight.
- **Caveat** (500, 700). Used only for the coach's hand: annotations on key frames, margin notes, the feel-cue sticky note and labels on sketches. It is never used for body text, numbers the player must rely on, or controls.

## Signature moves

1. **Printed key frames with two layers of ink.** Address and impact appear as taped photo prints. The app's crisp white pose lines and the dashed "hip line at address" sit on the photo, and the coach's red circle, "hips →" and "7% of body height" are drawn on top in marker.
2. **Paper objects as the information architecture.** The verdict is an index card, the feel cue a sticky note, the drill and mobility exercise taped index cards with reps in green, the possible fault a dashed amber slip, the unverified observation a dashed scrap stamped "Unverified — confirm with a coach".
3. **Hand-drawn rulers for thresholds.** The measurement is a pencil ruler with the 4% fault threshold dashed and "you: 7%" in marker. Loss of posture gets the same ruler with the 5° potential and 9° fault lines.
4. **Confidence as filled marker dots** (●●● high, ●●○ medium, ●○○ low), always paired with the word, on every measurement and every chain link.

## How the AI chat lives here

The chat feels like texting your coach. It is a taped sheet beside the result, titled "Ask your coach" and tied to "this result: Early extension · 11 Nov". Rory's messages are blue-ink bubbles. The coach's replies are paper bubbles and can include a small pencil sketch: the address and impact stick figures with the hip line and "+7%". A green-ticked note at the top says "Answers are based only on this analysis. No new faults, numbers or drills." The sample thread shows grounding at work. One reply quotes the 7% and the impact frame, one reuses the wall-drill text for a net, and one declines to talk about grip, a red margin note reading "won't guess". Suggested prompts are hand-cut paper chips. On mobile the chat opens from a full-width "Ask your coach about this" bar under the verdict.

## Risks / trade-offs

- **Charm can read as amateur.** The hand-drawn layer has to stay disciplined (Caveat for annotations only, strict grid, real type hierarchy). If Caveat spreads into body text or controls, the product looks like a hobby project and loses the trust the honesty pitch depends on.
- **Wobbly strokes cost implementation effort.** Production needs a small SVG "rough" helper (seeded jitter) for boxes, circles and arrows, plus real-time overlay of the coach marks on frames whose geometry comes from the pose data. That is more work than CSS borders.
- **Density on phones.** Taped cards, rotation and shadows eat width at 390 px. On mobile the rotations and tape should be toned down (the phone frames already flatten them), or the result will feel cramped at the range.

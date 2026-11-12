# 09 · Cairn

**Thesis:** A calm coach in one hand. It builds your answer one stone at a time, with the cause at the base and the fault on top, and it never stacks a stone it cannot balance.

## Rationale

Cairn is for Rory at the range after work: phone in one hand, club in the other, a few minutes between balls. The phone is the main design surface. Each screen holds one thing (fault → why → what to practise → ask the coach), and every action sits in the bottom third within thumb reach. The cairn fits an honest coach because it is literal about evidence: a stone is only placed when the one beneath it holds, so the fault chain reads from the ground up (restricted hip rotation → hips move toward the ball → early extension). The same image covers the honest outcomes. "Cannot analyse" shows the stones lying unstacked on the ground. "No verified fault found" shows one flat, settled stone. An unverified observation is drawn as a dashed outline stone. Warm oat and stone neutrals, a single deep moss accent and a soft serif are meant to lower the player's shoulders instead of grading him. It should not feel bland, because the cairn appears on every surface.

## Palette

| Hex | Role |
|---|---|
| `#F2EDE3` | Oat: page ground |
| `#FBF8F2` | Linen: cards, sheets, inputs |
| `#DDD5C6` | Stone: neutral pebbles, inactive track |
| `#C9BFAE` | Stone dark: dashed outlines, dividers on linen |
| `#E3DBCC` | Hairline |
| `#E4E9DC` | Sage light: feel cue, mobility card, chips |
| `#C8D3BE` | Sage mid: medium-confidence stone fill |
| `#A8B79F` | Sage: leaders, secondary pebbles |
| `#3E5638` | Moss: the one accent; primary buttons, high-confidence stones, body lines on key frames |
| `#2A2925` | Ink: text, phone bezel, destructive confirm |
| `#5C584F` | Ink secondary: supporting text (≥4.5:1 on oat) |
| `#8C8272` | Figure: golfer silhouette in key frames |

## Typography

- **Newsreader** (400/500/600, italic): headlines, fault names, the feel cue (italic), dose numerals ("3 × 10").
- **Nunito Sans** (400/600/700/800): all UI, body, labels, confidence badges. Body text is 15–16 px on the phone, and the smallest size is 12 px.

## Signature move: the cairn

- **Fault chain = cairn.** Stones are stacked with the cause at the bottom. Each stone has a fine leader line to its evidence and confidence.
- **Confidence = stone weight.** High is a solid moss stone, medium is a sage-filled stone with a moss rim, and low is a dashed outline. The text label ("confidence: medium") is always shown as well, so colour is never the only signal.
- **Analysing builds the cairn.** Pose, swing events, measurements, rule table and explanation each place a stone. The stone being placed hovers over a soft shadow, and the next one is a ghost outline.
- **The stepper is pebbles.** Fault · Why · Practise · Ask: finished steps settle to sage, the current step is solid moss, and upcoming steps are dashed.
- **The logo is a three-stone cairn.** The grounded-chat note reuses it as a tiny cairn icon.

## How the AI chat lives here

The chat is the fourth and last step of the stepper: **Ask**. On the phone it opens as a bottom sheet over the dimmed result. A small cairn icon sits next to "Answers are based only on this analysis." Each coach answer ends with a "From:" line that names its sources (impact key frame, hip measurement, wall drill) and shows a thumbnail of the frame. Three suggested questions are shown as full-width chips, so there is no blank-page problem. On desktop the sheet docks under the practice cards as a panel, with the same note and chips. The chat comes after the player has seen the evidence, so it adds to the result and never replaces it.

## Risks / trade-offs

- **Calm can read as low-energy.** Competitive low handicappers may want more data density. The desktop adaptation stays deliberately sparse, so power users may find it slow.
- **The cairn metaphor has to be learned.** Solid, half-tone and outline stones only work with the text labels next to them. If those labels are dropped to save space, the encoding fails. A one-time legend (as on the landing page) is needed.
- **Progressive disclosure hides things.** "Possible fault" and "Over the top: not found" sit one step deeper ("Also checked"). Honest, but a player who stops at the first screen may miss them. The "Also checked: 2 more" link has to stay visible.

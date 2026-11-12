# 08 — Broadcast Telestrator

**Thesis:** Your swing gets the replay-analysis segment: frozen key frames, marker strokes on the hips, on-air stat graphics, and an analyst who tells you how sure he is.

## Rationale

Built for Rory: an 11-handicapper who watches golf on TV and already knows the format: freeze the replay, circle the hips, draw the line the player left. AIcoach's core move is the same as that segment. It contrasts feel with what the frame shows, so the result page is staged as one: hero replay with telestration, a lower third naming the verified fault, then the fault chain run as a sequence of on-air graphics (likely cause → mechanism → fault), each carrying its evidence and confidence meter. The broadcast grammar is also a strong honesty tool. A confidence meter sits in every graphic the way a stat source line does on TV, so it is never hidden. Telestration is reserved for measured evidence. An unverified observation gets a dashed white outline instead, and a rejection shows "NO REPLAY" and does not draw on the frame. The energy keeps a range session moving; the plain-language copy and big slanted type stay readable on a phone in daylight.

## Palette

| Hex | Role |
|---|---|
| `#081226` | Deep navy: studio background, ink on light plates |
| `#0E1C3A` | Panel navy: graphics, cards |
| `#15274D` | Raised navy: active rows, feel-cue strap |
| `#2A3F70` | Rule lines, frame borders |
| `#FFFFFF` | Lower-third plates, headlines |
| `#D3DCEE` / `#A7B4D1` | Body text / secondary text on navy |
| `#FF5B1F` | Signal orange: telestrator marker, REPLAY bug, drill, primary CTA (navy text on it) |
| `#17C2AE` | Confidence teal: confidence meters, "VERIFIED", mobility, grounding note |
| `#4A67A6` / `#334C80` | Golfer figure (near/far limbs) in replay frames |

## Typography (Google Fonts)

- **Barlow Condensed**: italic 800/900 for display, lower thirds, bugs, stat numerals; upright 700 for tickers and timecodes.
- **Barlow**: 400/500/600/700 for body copy, explanations, chat, form fields.

## Signature moves

1. **Telestrator strokes**: thick, freehand signal-orange marker lines drawn over the replay frames: the address hip line, a loop around the hips, and an arrow for the 7% shift. A translucent **ghost of the address pose** sits under the impact frame.
2. **"REPLAY · IMPACT" bug** plus timecode on every key frame, and **lower-third plates** ("EARLY EXTENSION" | "VERIFIED") with a confidence strap underneath.
3. **Slanted confidence meter**: three parallelogram bars with the word HIGH/MEDIUM/LOW. It appears on every measurement, link and fault.
4. The fault chain as **numbered on-air graphics** (1/3, 2/3, 3/3) joined by chevrons. "Likely cause" gets a dashed strap because it is not measured directly.

## How the AI chat lives here

**"Ask the analyst"** is a studio Q&A desk in the result page's right column. Each question carries a white "RORY" name plate, and each answer an orange "ANALYST" plate. A lock note under the header states "Answers are based only on this analysis." An "On the desk" row lists the facts the analyst may use. Answers cite their evidence inline, for example a thumbnail of the telestrated impact frame and "Cited: 7% of body height (confidence: high)", and they link to the drill. An out-of-scope question ("Is my grip causing this?") gets an honest refusal tagged "Outside this analysis — not answered". Suggested prompts sit as chips above the input. On mobile, the desk collapses to a sticky bottom bar.

## Risks / trade-offs

- Broadcast energy can drift into "sports entertainment" and undercut the calm, trustworthy coach. The dense slanted plates need restraint in implementation, keeping one hero graphic per screen.
- Telestration is drawn per fault. The production app would need overlay geometry generated from pose data, not hand-drawn art. The freehand look must be simulated reliably, for example as jittered SVG paths.
- Dark navy with condensed italic caps is less legible in bright range sunlight than a light theme. Body copy stays in upright Barlow at 15px or larger, but a light "day mode" may be needed.

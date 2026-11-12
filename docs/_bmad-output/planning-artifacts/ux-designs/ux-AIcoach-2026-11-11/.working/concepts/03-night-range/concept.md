# 03 — Night Range

**Thesis:** One swing under the floodlights, and the frame tells the truth: the video is the page, and every finding is drawn onto it.

## Rationale
AIcoach's player is Rory at the range after work in a Norwegian November: dark at 16:00, floodlights on, a phone propped on his bag. Night Range is set in that world. Near-black blue-green, floodlight cones, turf stripes, and one hot ball-tracer lime that marks only what matters: the swing path, the glowing hip line at impact, the measured link in the fault chain, and the primary action. An honest coach shows you the frame instead of a score. So every page puts a key frame or the live clip at full size, with the result laid over it as a broadcast-style HUD (address line dashed, impact hip line glowing, "7%" printed next to the gap) rather than in cards. Confidence is drawn as signal bars on every measurement. Amber (sodium light) is kept for caution: Cannot analyse, possible, unverified, low confidence, and the medical notice.

## Palette
| Hex | Role |
|---|---|
| `#060C0B` | Night: page background |
| `#0B1614` | Surface: coach dock, panels |
| `#12211E` | Raised: inputs, user chat bubbles |
| `#223630` / `#2F4A42` | Hairlines, empty confidence bars |
| `#EAF2EE` | Primary text (≈17:1 on night) |
| `#A6BCB3` | Secondary text (≈9:1) |
| `#7A928A` | Tertiary/meta text (≈5:1) |
| `#C6FF3D` | Tracer lime: swing path, hip line at impact, measured values, primary buttons (text `#08110A` on it) |
| `#FFB547` | Sodium amber: Cannot analyse, possible fault, unverified observation, low confidence, warnings |
| `#FFF2D2` | Floodlight: lamp heads and light cones only (low-opacity gradients) |

## Typography
- **Barlow Condensed** 700/800: display, uppercase headlines, fault names, overlay readouts ("EARLY EXTENSION", "7%").
- **Barlow** 400–700: UI and body copy, chat, explanations.
- **IBM Plex Mono** 400/500: timecodes, frame numbers, fps, thresholds and measurement units only (data, not decoration).

## Signature moves
1. **The tracer.** One lime line per screen: ball flight in the hero, the playhead and hip-movement curve in the scrubber, the glowing hip line at impact, the solid "measured" link in the fault chain. The "likely cause" link is dashed, because it is inferred.
2. **The scrubbable swing timeline.** Under the result video: a filmstrip of the swing window (address, top, impact), with the hip-movement curve crossing the dashed 4% threshold exactly at the IMPACT marker. Playhead, frame step and ¼ speed controls.
3. **Overlays, not cards.** Verdict, confidence and measurement sit on the frame, with a leader line to the gap between the address line and the impact hip line. A ghost of the address pose sits under the impact pose.

## The AI coach
A compact dark dock pinned to the right of the result, like a coach standing beside the bay. The first line says "Answers are based only on this analysis. No new faults, numbers or drills." Answers quote the analysis's own numbers and confidence, and carry lime reference chips (e.g. "Impact frame 00:01.42", "Wall drill") that move the scrubber or scroll to that part of the page. The sample includes a refusal ("I can't tell from this analysis — it doesn't measure grip … confirm with a coach") to show the grounding. Below the chat: suggested prompts and a pinned input. On phones the dock becomes a bottom sheet that peeks over the result.

## Risks / trade-offs
- **Dark and moody can turn murky.** Silhouette figures on a dark scene are low-contrast by design. Text contrast is checked, but key frames need real video plus a light scrim behind the overlays, or the HUD gets lost on bright clips (daylight ranges, white nets).
- **Real clips aren't composed like the drawings.** The HUD layout assumes a predictable DTL framing. Badly framed clips that still pass analysis need a fallback that moves the readouts off the video, below the frame.
- **Cinematic can feel like a sports-broadcast brand.** The condensed caps and lime accent must stay functional (only measured/verified things glow), or the honesty message turns into hype.

# 02 · Lab Instrument

**Thesis:** A coach that shows its working.

## Rationale
AIcoach is built for the +2 to 15 handicap player who already distrusts swing apps that hand out graphs and verdicts with no reasons. This concept treats every result like a page from a measurement report. The 7% reading is plotted against the 4% threshold with an error bar, key frames are pose-skeleton plots with keypoint markers and coordinate ticks in body heights, and the fault chain is a schematic in which every block carries its evidence callout and confidence band. The honesty in the PRD (Cannot analyse, No verified fault found, Unverified, possible) is not hidden in empty states. Each one gets an instrument readout of its own, so "refuses to guess" is shown instead of claimed. Swiss discipline keeps a dense page readable: margin labels, one signal colour, hairline rules and no decoration that does not measure something.

## Palette
| Hex | Role |
|---|---|
| `#EEF0F1` | Paper: cool light-grey page ground |
| `#F8F9F9` | Sheet: plots, panels, cards |
| `#111417` | Ink: text, rules, skeleton lines, primary buttons |
| `#3E464D` / `#5C646B` | Secondary / tertiary ink (captions, units, mono metadata) |
| `#E1E5E8` / `#CDD3D7` | Graph-paper grid, minor and major (only under plots and measuring surfaces) |
| `#D2D8DC` | Ghost body capsules behind the skeleton |
| `#E2471A` | Signal: measured value, error bar, confidence meter, the hip keypoint. The only colour |
| `#B23A10` | Signal text on light (AA contrast) |
| `#101316` / `#FF7A4F` | Console ground / signal on dark, used only in the AI chat |

## Typography
- **Inter Tight** (400/500/600/700): display headlines (tight tracking, -0.02 to -0.03em), body copy, coach-voice explanation, feel cue.
- **JetBrains Mono** (400/500/700): only for data. That means measurement IDs (M-01, F-IMP, R-EE, D-01), values, units, axis ticks, timestamps, the analysis log and the chat console. The wordmark sets "AI" in mono and "coach" in Inter Tight, which also stops "AI" reading as "Al".

## Signature moves
1. **Threshold ruler with error bar.** Each measurement is a ruler: the fault threshold is a hard line, the zone above it is hatched, a possible fault has a dashed potential-threshold line, and the value is a diamond with an error bar. Confidence shows twice: as the width of the bar and as a 3-cell meter (`■■■ conf HIGH`).
2. **Key frames as pose plots.** Address and impact are drawn as skeletons with keypoint markers on graph paper, in body-height units. The impact plot overlays the dashed address pose and a dimension line (+0.070 BH) from the address hip line.
3. **Fault chain as a schematic.** Likely cause has a dashed border (inferred), mechanism a solid border (measured), fault a double border (verified). Each block has a leader line to an evidence tag carrying its ID, numbers and confidence band.
4. **Citable IDs everywhere.** Every number has an ID that the explanation, the chat and the analysis log refer back to.

## How the AI chat lives here
"Query this analysis" is a dark terminal console pinned in the right rail of the result page; on a phone it is a bar at the bottom. Its header says *Answers are based only on this analysis* and lists the IDs it is allowed to cite (M-01…M-04, F-ADR, F-IMP, R-EE, D-01, X-01). Each coach reply shows the sources it used, puts inline citations such as `[M-01]` in the signal colour, and can embed a small copy of the cited measurement ruler. When a question falls outside the analysis ("Is my grip causing this?"), the reply says the analysis cannot answer it and is tagged *outside this analysis*. Below the console sits a note: the coach explains, the rule table decides.

## Risks / trade-offs
- **Density can intimidate.** A 15-handicap player at the range may find a lab report cold. The feel cue and the plain-language explanation have to stay large and come first, or the coach's warmth gets lost under the instrumentation.
- **Error bars need teaching.** Few golfers read uncertainty intervals. The 3-cell meter and the HIGH/MEDIUM/LOW words carry the meaning on their own, but the landing page has to explain the convention once (it does, in the "Confidence band" specimen).
- **Precision theatre.** Figures like ±0.6 % BH, 0.93 and frame numbers suggest more accuracy than a 2D-pose MVP may deliver. All values here are synthetic. The real build must show only uncertainty values that the pipeline actually computes.

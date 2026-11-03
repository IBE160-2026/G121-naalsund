# Input reconciliation: research vs PRD + addendum

Date: 2026-11-03. Scope: PRD `prd.md` + `addendum.md`, checked against the two research reports. Decisions recorded in `.memlog.md` are excluded. These are not counted as gaps: history/compare kept as stretch, TrackMan in the next phase, OTT kept with sway as fallback, 30 fps accepted with a warning, English UI, opt-in swing library.

Severity: **H** = changes a requirement or success metric; **M** = a missing caveat, risk or traceability problem; **L** = wording or numeric precision.

---

## Input 1: Competitive research (2026-11-02)

### Missing or weakened recommendations

| # | Sev | Research says | PRD/addendum state | Location |
|---|---|---|---|---|
| C1 | H | Rec 1: **each link** of the fault chain names the measurement behind it, **the key frame and a confidence level**. This is the core differentiator. | FR-10: each link names "the measurement **or rule-table entry**". A rule-table entry alone would pass, so evidence is not required for every link. There is no confidence per link, and "at least one key frame" is required per fault, not per link. Example: the "restricted hip rotation" cause has no measurement in the MVP. | §4.4 FR-10; §3 Glossary "Fault chain" |
| C2 | H | Rec 3: each chain should **end in a body limitation** and its mobility exercise, citing **TPI screening logic** as the domain basis. This is the "clearest open gap". | The over-the-top cause is "Upper body starts the downswing", which is a movement-sequence cause and not a body limitation. "Open books" is attached to it anyway. The PRD never cites TPI as the basis for the cause→mobility mapping (only addendum §E mentions TPI, in passing). The technical research [34] gives physical TPI causes for OTT (hip mobility, separation, glutes/abs). | §4.4 rule table; FR-11 |
| C3 | H | Rec 4: write the success criteria around **plain-language output** (one fault, why, one drill, one exercise). This targets the interpretation-burden complaint. | FR-14 says "plain language without jargon", but there is no test for it. SM-4 checks that the elements are present, not that they are plain-language. SM-7 checks grounding only. No metric checks readability or jargon (e.g. a reviewer check or a banned-term list). | §4.6 FR-14; §10 SM-4/SM-7 |
| C4 | M | Open question: the **Macro Golf Performance** app may already link mobility screening to faults (unconfirmed). Whether Performance Golf SwingScan shows real chains is also unverified. Both threaten the differentiation claim. | Not mentioned. The Vision states the gap as absolute fact ("no competing app shows ... evidence for each link"). The research rated this claim **medium** confidence: about a dozen apps checked, none tried hands-on. | §1 Vision (last paragraph); §11 Open Questions |
| C5 | M | Table stakes (high confidence): an overall swing score is listed among MVP table stakes. | Deferred to the next phase (§8.2), and addendum §E says "deferred deliberately". The memlog has no recorded decision for this. Either log it as a decision or note the competitive risk. | §8.2 "Swing score"; addendum §E |

### Misquoted, overstated or contradicted

| # | Sev | Research says | PRD/addendum state | Location |
|---|---|---|---|---|
| C6 | M | Vendors publish no validation [1][3]; markerless golf accuracy is "unsettled" [25]; small camera changes alter results [11]. | "Existing swing apps **measure well** but leave the player to interpret graphs". This contradicts the accuracy-distrust finding, which the research calls the main trust problem. | §1 Vision ¶1 |
| C7 | L | Price range "roughly $110–200 a year". Performance Golf is **$199–299/yr** (plus $39/mo). Mustard's $149.99/yr is a **2024, stale** figure. | Performance Golf is listed inside "$110–200/yr" with no caveat. The Mustard staleness is not flagged. | addendum §E Pricing |
| C8 | L | "No longer unique": root-cause marketing by Performance Golf, SwingCoach AI, **Mustard ("potential causes") and SR.AI**. Grounded chat in SwingCoach AI **and Caddie AI**, with Sportsbox SAMI moving in ("more to come very soon"). | Lists only Performance Golf and SwingCoach AI. SAMI's trajectory (Gemini, owned by a DeChambeau-led group since April 2026) is not recorded as a risk for next-phase chat. | addendum §E; §9 "Chat" |
| C9 | M | Not in the competitive research: DeepSwing launch monitor "$79.99/yr", "240 fps iPhone, no radar". The research only says DeepSwing "now leads with a launch monitor". | Addendum §F gives these specifics without a traceable source in either research.md. They may come from the brief or digests, but they should be traced. | addendum §F bullet 1 |

### Captured correctly (no action)
- Per-metric confidence as a must-have (FR-7), and capture guidance with an angle check (FR-4, FR-8 non-DTL rejection).
- Free chat kept out of the MVP (§7, §8.2).
- Re-check of competitive claims due **2026-12-01** (§11 Q5). This matches the staleness map. Note that the research also asks for a Refresh "before the final PRD revision or the course hand-in", and for SAMI to be re-checked by **February 2027**. Neither is in the PRD.
- Lesson price of 600–1200 NOK (§2.1).
- Fear of wrong advice → verified rules plus a labelled unverified observation (FR-12, FR-13). The wish for the AI to agree with the player's coach is partly addressed by §11 Q1.

### Minor / not captured
- The research names **strict filming guidelines** as the answer to setup distrust, and **price resentment / paywall before a useful result** as a complaint. The second matters for the later subscription and is not noted in §9.
- Customer voice is thin (small samples from 2022–2025; Reddit and Google Play were blocked). The PRD does not carry this caveat for the user-voice claims in addendum §E.

---

## Input 2: Technical research (2026-11-03)

### Missing or weakened recommendations

| # | Sev | Research says | PRD/addendum state | Location |
|---|---|---|---|---|
| T1 | H | Rec 3: the success criterion is that "high" confidence results are **correct more often than** "low" ones. | FR-7 and SM-5 say "**at least as often**". A tie passes, including the case where confidence carries no information, which is what the research warns against. | §4.3 FR-7 consequence 4; §10 SM-5 |
| T2 | H | Rec 6: define **address as stillness before takeaway**, and **add event detection to the test set**, because the wrist heuristic has no published accuracy. Per-event accuracy varies widely (SwingNet: impact ~98%, top 83.9%, address 31.7%). | FR-6 only tests impact (±2 frames). Address and top are "reported" but never checked against labels, and address is not defined. Also, ±2 frames is not a fixed time: at 30 fps it is ±67 ms, about a quarter of a 0.21–0.26 s downswing; at 240 fps it is ±8 ms. The tolerance needs to be stated in ms or tied to fps. | §4.3 FR-6 consequence 1; §12 |
| T3 | H | Rec 4: speed is a measured acceptance test, **with the clip trimmed to the swing window before pose**, and the report gives the **model choice and median time**. 240 fps × 10 s = 2,400 frames "at the limit". | NFR-1 and SM-8 cover only a **10-second** clip, but FR-5 allows up to **15 s** (3,600 frames at 240 fps). No requirement covers 10–15 s clips. Trimming before pose and median-time reporting appear only in the addendum (§A) and not as acceptance conditions. | §5 NFR-1; §10 SM-8; §4.2 FR-5 |
| T4 | H | Rec 1: thresholds are configurable starting values **with a source and a tuning rule**. Tune on the labelled test videos. "Say **in the PRD** that they come from one patent and are not validated norms." | The PRD says the thresholds are "tuned on the test set, not fixed norms" (§4.4), but the one-patent source appears only in the addendum. There is **no tuning rule**. Thresholds are tuned on the same small set (≥4 clips per fault) that SM-1, SM-2 and SM-3 are measured on, with no held-out split, so the success metrics risk being self-fulfilling. | §4.4 description; §10 SM-1–3; §11 Q3 |
| T5 | M | Loss-of-posture threshold (patent): **>10° change in head–hip–knee–ankle chain angles**. The comparable 2D measure is the ear–hip "forward tilt", about **45–60°** in skilled DTL swings [30]. | The rule table measures a "Posture (**head/shoulder/spine**) angle change". That is a different angle set from the one the 10° threshold was defined on, so the patent value does not transfer directly. This should be noted, or the measure aligned with the patent. | §4.4 rule table row 2; addendum §B |

### Misquoted or numeric mismatches

| # | Sev | Research says | PRD/addendum state | Location |
|---|---|---|---|---|
| T6 | L | Camera **8–12 ft** away [26][27] (≈2.4–3.7 m). | "about **2.5–3.5 m** (8–12 ft)". 2.5–3.5 m is about 8.2–11.5 ft, so the metric and imperial ranges disagree. | §4.2 FR-4 |
| T7 | L | Over-the-top patent rule: >~3 in in front of/above the impact-plane line **or >~6 in in front of/above the player**. The shaft-angle sign is garbled in the extracted text. | Only the 3 in criterion is given; the 6 in alternative and the garbled-text caveat are missing. | addendum §B row 3 |
| T8 | L | 9–10° angle error: source confidence "low-medium (snippet)", from general sports movements, not golf-specific. | Shown as "~9–10° (unverified)". Acceptable, but it omits that the figure is not golf-specific. | addendum §B row 1 |
| T9 | L | SwingNet limits: released weights reach **71.5%** (not 76.1%), trained on **30 fps** YouTube video, the demo needs pre-trimmed single-swing video, and accuracy per view (DTL) is not reported. | Addendum quotes 76.1% with no released-weights caveat or 30 fps/DTL caveats. This matters if SwingNet is the fallback. | addendum §A "Swing events" |
| T10 | M | Not in the technical research: "CaddieSet ... spine angle vs ball speed **r = 0.53**". | Addendum §F cites it with no traceable source in either research.md. | addendum §F bullet 3 |

### Risks not carried into the PRD
- **Camera off the hand line:** the error is not quantified by any source (research open question). Distances depend on camera placement; FR-6 makes distances body-relative but does not address the camera angle. No risk or test is noted.
- **Pose quality on golf is unproven:** Swing Catalyst says its model had "minimal quantitative testing", Litslink says off-the-shelf pose was "not reliable enough for outdoor golf footage", and there is no head-to-head golf comparison. This is not recorded as a delivery risk. Addendum §A covers the one-day prototype but not the fallback if neither model is stable.
- **Shutter/exposure:** blur depends on exposure (1/1000 s or faster), which phone auto exposure does not let the user control. The addendum gives the shutter value, but FR-4 has no "good light / slow-motion mode" rationale beyond "good light". This is minor because the phone camera cannot be controlled.
- **"Potential" band vs confidence:** the research says the potential band is "the natural place to show medium confidence". The PRD creates a separate "possible" status (FR-9) and a confidence band (FR-7) without saying how they relate. A "possible" fault with "high" confidence is currently allowed.

### Captured correctly (no action)
- Three-input composite confidence; raw scores never shown (FR-7, addendum §C).
- Confidence below 120 fps capped at medium; 30 fps is the hard floor (FR-7, FR-8).
- OTT measured from the hand path and capped at "medium"; sway as fallback (FR-7, §4.4 Notes).
- Body-relative distances (FR-6, addendum §A).
- Do not cite the 70% early-extension prevalence (addendum §B).
- Licences: YOLO is AGPL, SwingNet is NC, MediaPipe/RTMPose/rtmlib are Apache-2.0 (NFR-7, addendum §A).
- Numbers checked and correct: RTMPose-m 26.6 ms/frame (desktop i7); MediaPipe Full 18 fps (Pixel 3); SwingNet 76.1% / impact ~98% / top 83.9% / address 31.7%; ~480 frames for a 2 s window at 240 fps vs 2,400; 6 Hz Butterworth (6–10 Hz in guides); patent thresholds 3–6 in / >6 in and 5–10° / >10°; "may vary" up to 3 in / 30°; patent granted 2026-04-21; 7–9 frames for the downswing at 30 fps; shutter 1/1000 s.

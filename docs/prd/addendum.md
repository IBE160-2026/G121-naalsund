# AIcoach PRD — Addendum

Technical and supporting detail for architecture and implementation. Not requirements; the PRD governs. Sources: technical research 2026-11-03, competitive research 2026-11-02, revised brief 2026-11-02.

## A. Pose and analysis approach (for architecture)

- **Candidate pose models:** MediaPipe Pose (Full/Heavy) and RTMPose-m via rtmlib (Apache-2.0). Prototype both in one day on the author's own DTL swing clips; choose on stability of hip, shoulder and wrist landmarks and on laptop speed.
- **Avoid:** YOLO-pose (AGPL-3.0 — requires source release or a paid licence). SwingNet (CC BY-NC 4.0) is acceptable only as a replaceable MVP fallback (NFR-7); it must be removed before a paid launch.
- **Smoothing:** 6 Hz low-pass Butterworth on landmarks (guides suggest 6–10 Hz).
- **Swing events:** Yamamoto wrist-height heuristic first; SwingNet as fallback (paper: 76.1 % of events within ±1 frame; impact ~98 %, top 83.9 %, address 31.7 %; released weights 71.5 %). The heuristic has no published accuracy — measure it on the test set.
- **Trim before pose:** run pose only on the ~2 s swing window (≈480 frames at 240 fps instead of 2,400).
- **Body-relative units:** distances as ratios to a body length measured at address (CaddieSet approach).
- **Week-1 spike:** a 30-minute local timing script on the target laptop supersedes all published CPU figures (RTMPose-m 26.6 ms/frame desktop i7; MediaPipe Full 18 fps Pixel 3 — single, vendor-affiliated sources).

## B. Rule threshold starting values

From one source: Acushnet patent US12608853B1 (granted 2026-04-21), which itself says values "may vary up to about 3 inches" or "30 degrees". Treat as configurable starting points.

| Fault | Potential threshold | Fault threshold | Note |
|---|---|---|---|
| Loss of posture | 5–10° change | >10° change | Patent defines the angle on head–hip–knee–ankle points; the PRD measurement must use the same definition (OQ3). 2D angle error ~9–10° (unverified) is the same size as the threshold — the confidence margin is part of the detector |
| Early extension | 3–6 in | >6 in | Needs body-relative conversion; no source gives one |
| Over the top | — | >~3 in in front of/above impact-plane line (patent also gives ~6 in as an alternative) | Defined on the club shaft; MVP uses hand-path proxy, capped at medium |

Do not cite "about 70 % of amateurs vs under 1 % of tour players" for early extension — no primary source.

## C. Confidence band construction

Pose-model keypoint scores are poorly calibrated (ICML 2024), so the band is a composite of: (1) landmark visibility in the key frames, (2) margin from the threshold, (3) clarity of the swing-event detection. It must be validated (SM-5).

## D. Capture evidence

- At 30 fps the downswing is only ~7–9 frames — hence the confidence cap below 120 fps (FR-7).
- Shutter 1/1000 s or faster recommended (vendor/forum sources only).
- Swing Catalyst: blurry, shaky or low-resolution video reduces accuracy "significantly".

## E. Competitive context

- **Open gaps AIcoach targets:** per-measurement confidence (none of about a dozen apps reviewed), evidence per fault-chain link, mobility exercise tied to the detected fault (TPI links mobility limits to faults, but no app does so in-product).
- **Table stakes:** single phone video, drill per fault, history with side-by-side comparison, an overall score (deferred deliberately).
- **No longer unique:** root-cause marketing (Performance Golf, SwingCoach AI) and grounded chat.
- **User voice:** data "overwhelming", "YOU have to figure out where you are having the issue", fear of "ingraining the wrong things"; praise for jargon-free explanation and key frames with drawings.
- **Pricing benchmark:** consumer tiers mostly $110–300/yr (Sportsbox $109.99, DeepSwing $119.99, Mustard $149.99, SwingCoach AI $199.99, Performance Golf $199–299) vs a 600–1200 NOK lesson.

## F. Launch-monitor notes (next phase)

- DeepSwing v3.4: camera-based launch monitor (240 fps iPhone, no radar), links ball data to swing faults; $79.99/yr. No independent accuracy tests.
- No competitor found importing TrackMan data. FlightScope Badger AI noted as a lead, not researched.
- CaddieSet dataset combines joint features with ball data (spine angle vs ball speed r = 0.53) — a possible research starting point.
- Brief addendum: a single 2D video cannot measure club path, face angle, ball flight or ground forces — the gap launch-monitor data would fill.

## G. Course context

Teacher feedback weighting: process 30 %, functionality 20 %, QA 15 %, design 10 %, code 10 %, README 10 %, repo 5 %. Feedback on the brief and where it is handled: sketches of the filming guide and result screens (→ UX phase), GDPR (now covered in PRD §6.1: retention, consent, LLM data, deletion; export next phase), LLM cost (Open Question 2).

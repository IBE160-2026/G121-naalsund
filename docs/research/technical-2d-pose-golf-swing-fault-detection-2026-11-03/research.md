---
title: 'Technical research: 2D pose golf swing fault detection'
type: 'technical'
topic: '2D pose golf swing fault detection'
decision: 'What the AIcoach PRD can promise on thresholds, confidence rules and speed for detecting early extension, loss of posture and over the top from one down-the-line phone video with local 2D pose'
source: 'native run (2 rounds, 5 researcher digests + 1 lead lookup)'
status: complete
preset: 'standard'
validation: 'normal'
created: '2026-11-03'
updated: '2026-11-03'
claims_verified: 5
claims_unverified: 7  # recon_kit tally over 12 load-bearing ledger claims
---

# Technical research: 2D pose golf swing fault detection

**Decision this research serves:** what the AIcoach PRD can promise on thresholds, confidence rules and speed for detecting early extension, loss of posture and over the top from one down-the-line (DTL) phone video with local 2D pose.

**Effort level:** `standard` preset (3 researchers in round 1, 2 in round 2, about 8 sources per researcher per round, 2 rounds), validation `normal`, red team off. The lead added an inline competitor lookup of 8 tool calls, because the round-2 researcher ran out of budget on this user-requested question. Both dimension sets stopped at the round cap; the open questions are listed below.

## Executive summary

**The plan is feasible, but the PRD should promise a tunable, testable rule system, not literature-backed thresholds, calibrated confidence or a guaranteed speed.**

1. **Starting thresholds exist, but come from one patent, not from research.**
   - TPI defines all three faults clearly from the DTL view, but publishes no numbers [31][33][34].
   - The only numeric thresholds found are in an Acushnet (Titleist parent) patent granted in April 2026 [35]:
     - **Early extension:** hips more than about 6 in past a vertical line at the rearmost hip; 3–6 in is "potential".
     - **Loss of posture:** more than 10° change in the address angles; 5–10° is "potential".
     - **Over the top:** club more than about 3 in in front of and above the impact-plane line.
   - The patent says these values "may vary" by up to 3 in or 30°, so they are starting values to tune on the test videos, not norms.
   - Its two-level structure (fault and "potential") fits the brief's confidence idea well.
2. **Confidence must be built, not read off the model.**
   - All three pose models output per-keypoint scores, MediaPipe as visibility/presence [3][4], RTMPose as SimCC scores [1] and YOLO as keypoint confidence [2]. None is documented as calibrated.
   - An ICML 2024 paper finds that such scores are generally poorly calibrated [6].
   - Markerless 2D pose has about 9–10° mean joint-angle error in sports movements [37]. That is about the same size as the 10° loss-of-posture threshold.
   - The PRD should define confidence as a composite: landmark visibility in the relevant frames, the margin from the threshold, and the certainty of event detection. It should then show it in bands that are checked against the test set.
3. **Speed is plausible, but nobody has measured it on a laptop.**
   - Published CPU figures each come from a single, vendor-affiliated source:
     - RTMPose-m with detector: about 26.6 ms per frame on a desktop i7 [1]. The paper's other CPU figures are single-threaded, but it does not say whether this one is.
     - YOLO26n-pose: about 40 ms per frame on an unnamed CPU [2].
     - MediaPipe: only 2021 phone figures, with Full at about 18 fps on a Pixel 3 CPU [4].
   - A 240 fps clip of 10 s is 2,400 frames, which puts the 2-minute target at the limit. Trimming to the swing and subsampling make it comfortable.
   - The PRD should state speed as an acceptance test measured on the target laptop.

**Biggest caveat:** over the top is hard to detect from pose alone. Both the TPI slot test [34] and the patent rule [35] use the club shaft, and the generic pose models do not track the club. Without a club detector, over the top can only be estimated from the hand path, with lower confidence.

## D1: Pose models and how competitors do it

**Candidates.**
- **MediaPipe Pose Landmarker** (lite / full / heavy): 33 landmarks, each with visibility and presence, and a VIDEO mode that tracks between frames [3][4]. The 2021 browser benchmarks (81 fps for Full) used GPU help, so they say little about CPU speed [5].
  - Its model card reports accuracy only on fitness-style smartphone photos (PDJ 87–94%). It warns of more "jittering" under motion and poor light [4].
- **RTMPose** (via rtmlib or MMPose): the best published CPU speed/accuracy trade-off. RTMPose-m reaches 75.8% COCO AP at "90+ FPS" on an i7-11700 for the pose model alone, and 26.6 ms per frame with the RTMDet detector [1].
  - rtmlib also offers Body26 (with feet) and whole-body models [13].
- **YOLO-pose (Ultralytics):** easy to use, but the nano model is the only size that is fast enough on CPU (40 ms per frame; m size 218 ms) [2]. It is licensed AGPL-3.0, which requires releasing the source or buying a license [12].
- **Licenses:** MediaPipe, MMPose and rtmlib are Apache-2.0 [13][14][15].

**Quality on golf.**
- No head-to-head comparison on golf or fast sports video was found. This is an evidence gap, not a tie.
- The best signal is Swing Catalyst, a commercial golf product that uses RTMPose (title of [8]). It discloses that its general-purpose model "has undergone minimal quantitative testing". It also says fast golf poses and occluded points cause errors, that blurry or low-resolution video "significantly" reduces accuracy, and that it supports only face-on and DTL views [7]. Confidence: high that the vendor says this.
- Monocular 3D models were found "too erroneous" for golf kinematics against marker-based mocap (DTU 2023) [10]. That supports the brief's choice of 2D. Confidence: medium (abstract only).
- A golf patent notes that motion blur and the club head leaving the frame "greatly hinder" club keypoints [40]. Club tracking is a separate, harder problem.

**How competitors do it.**
- None of the apps checked discloses its pose model or publishes DTL validation.
- **Sportsbox AI** publishes its own unreviewed validation against AMM3D: about 2° mean difference on body angles, 30 golfers, face-on only, high-speed shutter [9]. Confidence: medium (vendor self-validation).
- **Swing Catalyst:** 2D only, RTMPose, honest about limitations [7][8].
- **SwingNote:** the user picks the angle (face-on or DTL), pose runs on the device, and "only numeric metrics are sent to the server" [17]. Confidence: medium (developer listing).
- **DeepSwing:** says it runs on-device and detects early extension and sway, with no model or validation disclosed [11]. Confidence: low.
- **Mustard:** a "patented computer vision and AI system" trained on 3D scans; no validation found [18]. Confidence: low.
- **Performance Golf SwingScan and CoachNow/OnForm:** no technical disclosure. CoachNow says its tracking is "NOT a silver bullet" [16][19].
- **Litslink:** a development vendor's case study says off-the-shelf pose models were "not reliable enough for outdoor golf footage" [20]. Confidence: low (snippet).

**Confidence scores.**
- MediaPipe visibility is defined as the probability that a point is in frame and not occluded; presence is the probability it is in frame [4].
- RTMPose SimCC scores and YOLO keypoint confidence come with no calibration claim [1][2].
- Keypoint confidences in standard 2D pose frameworks are poorly calibrated against actual accuracy [6]. Confidence: medium (abstract level).
- Practitioners smooth landmarks and interpolate short gaps. One community guide suggests a 6–10 Hz Butterworth filter [39]. Yamamoto et al. use 6 Hz on DTL wrist data [30].

## D2: Capture and normalization

**Frame rate.**
- The downswing lasts about 0.21–0.26 s in classic studies [29]. TPI's tour data gives a backswing:downswing ratio of about 3.2:1 and a 3D downswing range of 233–296 ms [24].
- At 30 fps that is only about 7–9 frames for the whole downswing. The clubhead moves about 1.5 m between frames at 100 mph [24].
- TPI recommends at least 120 fps (240 as an option for finer timing) and a shutter of 1/1000 s or faster [24]. V1 Sports suggests 240 fps on iPhone [26]. A forum reports that V1 recommends 1/2000 s [25].
- Blur depends on exposure time, not frame rate [25]. Phones in slow-motion mode usually shorten exposure, but auto exposure is not under the user's control.
- Verification: the fps recommendation has only vendor or forum backing (no standards body); the downswing duration is verified across sources.
- Research capture uses 240 Hz from DTL as well (Yamamoto et al., 3.5 m behind the ball) [30].

**Filming guide.** Guides agree on putting the camera at hand height at address, level, on or parallel to the hand line or target line, 8–12 ft away, on a tripod or stable surface [26][27].

**Normalization.**
- CaddieSet scales joint coordinates by the person's bounding-box width and expresses position metrics as ratios relative to address [23].
- A 2025 MDPI paper reportedly normalizes by shoulder width [38]. Confidence: low (snippet only).
- Angles are scale-invariant, so the loss-of-posture rule (degrees) transfers to 2D directly. Distances in inches, as used for early extension and over the top, need converting to a body-relative unit.
- Validity: the only 2D-vs-3D golf study found validated swing time and club angle from manual digitizing (face-on, 240 Hz), not body angles from pose estimation [28].
- No study puts a number on the error from a camera placed off the hand line. Guides only say qualitatively that it distorts plane lines.

## D3: Swing phases (events)

**SwingNet / GolfDB** [21][22]:
- 1,400 YouTube videos at 30 fps, 8 events, about 10.6 ms per frame on CPU.
- 76.1% of events are found within ±1 frame (91.8% excluding address and finish). Impact and mid-downswing are about 98%, top 83.9%, address 31.7% and finish 26.5%.
- Verification: CaddieSet independently reproduces the 76.1% / 91.8% baseline, and gets 78.0% / 94.1% after fine-tuning [23]. The per-event figures are single-source.
- Limits:
  - The code is CC BY-NC 4.0 (acceptable for the course, not for a paid launch).
  - The released weights reach 71.5%.
  - The demo needs a video already cropped and trimmed to one swing.
  - Accuracy per view (DTL vs face-on) is not reported [22].

**Wrist heuristic** (Yamamoto et al. 2023, DTL at 240 Hz) [30]:
- **Address:** the first frame where wrist speed exceeds a threshold, minus 0.125 s.
- **Top:** the wrist's highest point.
- **Impact:** the wrist's lowest point after the top.
- **Finish:** the wrist's highest point after impact.
- A 6 Hz Butterworth filter is applied first.
- This fits the MVP well (same view, no extra model, transparent), but **no accuracy figure is published**. Confidence: high that the method exists, unknown how accurate it is.

**Patent event model:** the Acushnet patent uses P1–P10. Top is found by the transition into the downswing, and impact by a return to an address-like pose [35].

**Audio:** patents use the impact sound to locate impact, but note it is unreliable in noise. No accuracy figures were found [41].

## D4: Fault definitions and starting thresholds

| Fault | TPI definition (DTL) | Numeric starting value | 2D implementation note |
|---|---|---|---|
| Early extension | "Any forward movement (thrust) of the lower body towards the golf ball during the downswing". DTL check: a vertical line behind the tailbone at address [31][32] | Hips more than about 6 in past a vertical line through the rearmost hip point = fault; 3–6 in = potential; values "may vary up to about 3 inches" [35] | Horizontal hip-keypoint displacement toward the ball, address → impact, normalized by a body length. Pixel-to-inch conversion is not described in the patent text read |
| Loss of posture | "Any significant alteration from your body's original set up angles" (no number) [33] | More than 10° change in head–hip–knee–ankle chain angles vs address = fault; 5–10° = potential; "may vary up to about 30 degrees" [35] | Angle change is scale-invariant, so it fits 2D directly. Comparable 2D measure: ear–hip "forward tilt", about 45–60° in skilled DTL swings [30] |
| Over the top | Club above or outside the "slot" (the area between the address shaft line and the club line at lead forearm near parallel, just before the downswing starts) in early downswing [34] | Club more than about 3 in in front of and above the impact-plane line, or more than about 6 in in front of and above the player = fault [35]. The sign of the shaft-angle criterion is garbled in the extracted text | Needs the club shaft. A pose-only proxy compares the hand path in transition with the backswing hand path. No numeric value was found for that proxy |

- **Patent source:** US12608853B1, assignee Acushnet Co, filed 2025-06-24, granted 2026-04-21. It allows 2D or 3D images and 60/120/240 fps [35].
- **Prevalence:** "about 70% of amateurs vs under 1% of tour players" for early extension circulates without a source. GOLF.com 2020 gives it unattributed, and no TPI data was found [36]. **Unverified; do not cite it in the PRD as fact.**
- **Fault chains (domain basis):**
  - **Early extension:** TPI links it to the deep squat, hip bend, lead-hip rotation, trunk–pelvis separation and glute/core strength [31].
  - **Loss of posture:** TPI names its screens: overhead deep squat, toe touch, pelvic tilt, seated trunk rotation, 90/90 and the lat test [33].
  - **Over the top:** TPI links it to weight shift, hip mobility, glutes and abs, and lower/upper-body separation [34].
  - This supports the brief's causes for the first two faults. For over the top, TPI's causes are physical, while the brief's "upper body starts the downswing" is a movement-sequence cause. Both are compatible.

## Cross-dimension insights

1. **The measurement error is about as big as the threshold.** General markerless pose has about 9–10° joint-angle error [37], and the patent's loss-of-posture threshold is 10° [35]. Measuring change from the player's own address pose cancels part of the constant bias, but not jitter. That makes the confidence rule (margin from threshold, smoothed landmarks) part of the detector, not just a label. The "potential" band (5–10°) is the natural place to show medium confidence.
2. **High fps helps detection and hurts speed, so trim the clip first.** 240 fps is needed for event timing and to cut blur [24][30], but 2,400 frames per 10 s strains the 2-minute budget [1][2][4]. Run pose only on the swing window, about 2 s (≈480 frames at 240 fps), or subsample the backswing. The speed target then holds with margin. This is an inference from the sourced numbers, not a measured result.
3. **Over the top is the weak link in the three-fault set.** The definition is club-based [34][35], the generic models do not track the club, and club keypoints are known to suffer from blur [40]. The other two faults need only hip, shoulder and head keypoints, which are the most stable points from DTL.
4. **The industry is doing what AIcoach plans.** A Titleist-family patent from 2026 describes rule thresholds on DTL keypoints with "potential" bands [35]. Swing Catalyst ships generic 2D RTMPose [7][8]. No competitor publishes DTL validation [7][9][11][16][17][18]. A small test set with known answers would therefore be stronger evidence than anything the competitors publish.

## Recommendations (for the PRD)

1. **Write thresholds as configurable starting values with a source and a tuning rule.** Use the patent values [35] for early extension and loss of posture, with a "potential" band, and tune them on the labelled test videos. Say in the PRD that they come from one patent and are not validated norms. *Confidence: medium (one primary source, clear text).*
2. **Express distances relative to the body, angles in degrees.** For example, early extension as hip displacement divided by a body length measured at address (as CaddieSet does with ratios [23]); loss of posture as degree change from address. The conversion factor is a tuning decision for the PRD or architecture; no source gives it. *Confidence: medium.*
3. **Define confidence as a composite with three levels, and test it.** The inputs are:
   - the minimum visibility of the relevant landmarks in the event frames,
   - the margin from the threshold (outside or inside the "potential" band),
   - whether the event detection is clear.

   Do not show raw model scores as confidence [6]. The success criterion: on the test set, "high" confidence results are correct more often than "low" ones. *Confidence: medium-high that raw scores should not be used; medium for the composite design.*
4. **Make the speed criterion a measured acceptance test.** Keep "a 10 s clip in under 2 minutes", but trim to the swing window before running pose, and measure on the target laptop in a week-1 spike. Report the model choice and median time. *Confidence: medium (vendor-only numbers).*
5. **Require slow motion in the filming guide.** Ask for 120 or 240 fps, good light, camera at hand height on the hand line, 8–12 ft away, tripod [24][26][27]. Accept 30 fps only with a warning and capped confidence. *Confidence: medium (vendor/coach guidance, no standards body).*
6. **Detect events with the wrist heuristic first, with SwingNet as a fallback.** The heuristic [30] matches the view and frame rate, and is transparent. SwingNet is reliable for impact (about 98%), less so for top (83.9%), weak on address, and its NC license blocks the later paid launch [21][22]. Define address as stillness before takeaway, and add event detection to the test set, since no accuracy figure exists for the heuristic. *Confidence: medium.*
7. **Prototype both MediaPipe (Full/Heavy) and RTMPose-m in one day, on your own DTL clips.** Pick by how stable the hip, shoulder and wrist points are through the downswing, and by speed. No golf comparison exists. RTMPose has a commercial golf precedent [8] and the best published CPU speed [1]; MediaPipe has VIDEO tracking and a defined visibility score [3][4]. Avoid YOLO unless you accept AGPL [12]. *Confidence: medium.*
8. **Scope over the top honestly.** Either (a) keep it with a hand-path proxy and a confidence capped at "medium", stated in the PRD, or (b) add a simple shaft-line detector as a stretch goal. If neither holds on the test set, replace it with sway, which the patent also defines from DTL [35]. *Confidence: medium.*
9. **Do not cite the 70% early-extension prevalence** without a primary source [36].

## Open questions

- **Laptop CPU speed** of MediaPipe, RTMPose and YOLO-pose: no independent measurement exists. A 30-minute local timing script answers it.
- **Accuracy of the wrist heuristic** for event detection on DTL video: not published. Label events on the test set and measure.
- **Pixel-to-inch conversion** in the Acushnet patent, and the rest of its claims text: only 2 of about 5 sections were read. Reading the rest on Google Patents would answer it.
- **Golf-specific error of 2D pose body angles vs mocap:** not found. The DTU full text [10] and GolfPose (2022) are the leads.
- **A numeric over-the-top hand-path proxy:** not found. It needs your own tuning or a club detector.
- **Effect of camera off the hand line** on DTL measurements: only qualitative. You could film the same swing from two positions to quantify it.
- **TPI's primary data** on early-extension prevalence: not found.

## Source appendix

| # | Supports | Publisher | Pub date | Accessed | Confidence |
|---|---|---|---|---|---|
| [1] | RTMPose CPU latency, accuracy, SimCC scores | [arXiv (Jiang et al., RTMPose)](https://arxiv.org/abs/2303.07399) | 2023-03 | 2026-11-03 | medium (single source for CPU speed) |
| [2] | YOLO26-pose CPU latency, keypoint confidence output | [Ultralytics docs](https://docs.ultralytics.com/tasks/pose/) | 2026 | 2026-11-03 | medium (CPU not named) |
| [3] | MediaPipe Pose Landmarker variants, VIDEO mode, thresholds | [Google AI Edge docs](https://developers.google.com/edge/mediapipe/solutions/vision/pose_landmarker) | unknown | 2026-11-03 | high |
| [4] | BlazePose GHUM speeds, visibility/presence definitions, limits, PDJ accuracy | [Google model card](https://storage.googleapis.com/mediapipe-assets/Model%20Card%20BlazePose%20GHUM%203D.pdf) | 2021-04 | 2026-11-03 | high (as stated; phone hardware) |
| [5] | BlazePose browser fps with GPU | [TensorFlow Blog](https://blog.tensorflow.org/2021/05/high-fidelity-pose-tracking-with-mediapipe-blazepose-and-tfjs.html) | 2021-05 | 2026-11-03 | medium |
| [6] | Keypoint confidences poorly calibrated | [arXiv / ICML 2024](https://arxiv.org/abs/2311.17105) | 2023-11 | 2026-11-03 | medium (abstract level) |
| [7] | Swing Catalyst body-tracking limits and views | [Swing Catalyst support](https://support.swingcatalyst.com/hc/en-us/articles/18829366835100) | 2025-03 | 2026-11-03 | high |
| [8] | Swing Catalyst uses RTMPose + RTMDet | [Swing Catalyst support](https://support.swingcatalyst.com/hc/en-us/articles/18829350333468) | 2025-03 | 2026-11-03 | medium |
| [9] | Sportsbox AI self-validation vs AMM3D (face-on) | [Sportsbox AI help](https://help.sportsbox.ai/sportsbox-ai-accuracy) | ~2025-01 | 2026-11-03 | medium |
| [10] | Monocular 3D pose too inaccurate for golf | [DTU / NLDL 2023](https://orbit.dtu.dk/en/publications/evaluating-current-state-of-monocular-3d-pose-models-for-golf/) | 2023-01 | 2026-11-03 | medium |
| [11] | DeepSwing on-device claims | [Apple App Store](https://apps.apple.com/en/app/deepswing/id6751551257) | unknown | 2026-11-03 | low |
| [12] | Ultralytics AGPL-3.0 | [Ultralytics license](https://www.ultralytics.com/license) | 2026 | 2026-11-03 | high |
| [13] | rtmlib Apache-2.0, models, backends | [GitHub Tau-J/rtmlib](https://github.com/Tau-J/rtmlib) | unknown | 2026-11-03 | high |
| [14] | MMPose Apache-2.0 | [GitHub open-mmlab/mmpose](https://github.com/open-mmlab/mmpose/blob/main/LICENSE) | unknown | 2026-11-03 | high |
| [15] | MediaPipe Apache-2.0 | [GitHub google-ai-edge/mediapipe](https://github.com/google-ai-edge/mediapipe/blob/master/LICENSE) | unknown | 2026-11-03 | high |
| [16] | CoachNow skeleton tracking, no accuracy claims | [CoachNow blog](https://coachnow.com/blog/using-coachnows-ai-tools) | 2025-03 | 2026-11-03 | medium |
| [17] | SwingNote on-device pose, angle selection | [Apple App Store](https://apps.apple.com/app/id6783664876) | 2026-10 | 2026-11-03 | medium |
| [18] | Mustard 3D-model-based analysis claims | [Golf Digest](https://www.golfdigest.com/story/what-an-average-golfer-learned-about-his-swing-new-technology-mustard) | 2024-07 | 2026-11-03 | low (snippet) |
| [19] | Performance Golf SwingScan, no technical disclosure | [Performance Golf](https://pg1.performancegolf.com/quiz/dqfe-lp-01-never-guess) | unknown | 2026-11-03 | low |
| [20] | Off-the-shelf pose unreliable outdoors (vendor case study) | [Litslink](https://litslink.com/case-studies/ai-golf-swing-analyzer) | unknown | 2026-11-03 | low (snippet) |
| [21] | GolfDB dataset, SwingNet PCE per event, CPU time | [arXiv (McNally et al.)](https://arxiv.org/abs/1903.06528) | 2019-03 | 2026-11-03 | high |
| [22] | GolfDB code license, released-weight accuracy, demo limits | [GitHub wmcnally/golfdb](https://github.com/wmcnally/golfdb) | unknown | 2026-11-03 | high |
| [23] | CaddieSet: baseline confirmation, fine-tuned PCE, ratio normalization | [arXiv (CaddieSet)](https://arxiv.org/html/2508.20491) | 2025-08 | 2026-11-03 | medium |
| [24] | Downswing timing, fps and shutter recommendation | [TPI (Cheetham)](https://www.mytpi.com/articles/biomechanics/measuring-the-timing-of-the-golf-swing-from-video) | unknown | 2026-11-03 | medium |
| [25] | Blur depends on exposure; V1 recommends 1/2000 s | [Kinovea forum](https://www.kinovea.org/en/forum/viewtopic.php?pid=4630) | unknown | 2026-11-03 | low |
| [26] | V1 recording guide: DTL distance, 240 fps | [V1 Sports](https://swing-analysis.v1sports.com/swing-analysis/swing-recording.md) | unknown | 2026-11-03 | medium |
| [27] | DTL camera at hand height, on the target line | [Titleist](https://www.titleist.com/teamtitleist/team-titleist/f/golf-tips/54984/online-golf-instruction-how-to-film-your-swing) | unknown | 2026-11-03 | medium |
| [28] | 2D vs 3D validity: swing time and club angle only | [Scientific Reports (Hunter et al.)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9385988/) | 2022-08 | 2026-11-03 | high |
| [29] | Downswing 0.21–0.26 s (classic studies) | [UPM repository (López de Subijana et al.)](https://oa.upm.es/2746/) | unknown | 2026-11-03 | medium (snippet) |
| [30] | Wrist-trajectory event heuristic, DTL 240 Hz, forward-tilt angle | [Frontiers (Yamamoto et al.)](https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2023.1272038/full) | 2023-11 | 2026-11-03 | high |
| [31] | TPI early extension definition and fault chain | [TPI](https://www.mytpi.com/improve-my-game/swing-characteristics/early-extension) | unknown | 2026-11-03 | high |
| [32] | TPI DTL tailbone-line check for early extension | [TPI](https://www.mytpi.com/articles/swing/why-early-extension-causes-a-reduction-of-power-in-the-golf-swing) | unknown | 2026-11-03 | high |
| [33] | TPI loss of posture definition and screens | [TPI](https://www.mytpi.com/improve-my-game/swing-characteristics/loss-of-posture) | unknown | 2026-11-03 | high |
| [34] | TPI over the top definition, slot test, causes | [TPI](https://www.mytpi.com/improve-my-game/swing-characteristics/over-the-top) | unknown | 2026-11-03 | high |
| [35] | Acushnet patent: thresholds, potential bands, events, fps | [Google Patents US12608853B1](https://patents.google.com/patent/US12608853) | 2026-04 | 2026-11-03 | high (text) / medium (interpretation) |
| [36] | 70% early-extension prevalence, unattributed | [GOLF.com](https://www.golf.com/instruction/2020/03/02/chair-fix-problem-plaguing-70-percent-amateur-golfers/) | 2020-03 | 2026-11-03 | low |
| [37] | Markerless pose about 9–10° joint-angle error in sports | [Sports Engineering (Springer)](https://link.springer.com/article/10.1007/s12283-024-00460-w) | 2024 | 2026-11-03 | low-medium (snippet) |
| [38] | MDPI Sensors 2025 golf similarity paper, shoulder-width normalization | [MDPI Sensors](https://www.mdpi.com/1424-8220/25/22/7073) | 2025-11 | 2026-11-03 | low (snippet) |
| [39] | Practitioner smoothing and gap interpolation for MediaPipe | [skills.sh community guide](https://skills.sh/feniix/kinemotion/mediapipe-pose-detection) | unknown | 2026-11-03 | low |
| [40] | Club motion blur and the hosel leaving the frame hinder club keypoints | [USPTO patent 12711647](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12711647) | unknown | 2026-11-03 | low (snippet) |
| [41] | Audio locates impact but is unreliable in noise | [Google Patents US10080947](https://patents.google.com/patent/US10080947) | unknown | 2026-11-03 | low (snippet) |

## Staleness map

Computed with `recon_kit.py staleness`. The windows are taken from the technical pack: performance 6 months, licensing and competitor 6 months, capability 12 months, and patterns, events, capture, validity and thresholds 24 months. Undated pages that were current when accessed (Ultralytics docs and license, TPI) are entered as 2026-01.

| Claim | Class | Pub | Re-check | Stale now? |
|---|---|---|---|---|
| [35] Acushnet patent thresholds | threshold | 2026-04 | 2028-04 | no |
| [24] fps / shutter recommendation | capture | 2026-01* | 2028-01 | no |
| [2] YOLO26n-pose CPU speed | performance | 2026-01* | 2026-07 | yes |
| [12] Licenses (AGPL / Apache) | licensing | 2026-01* | 2026-07 | yes |
| [37] Markerless angle error 9–10° | validity | 2024 | 2026-01 | yes |
| [30] Wrist heuristic for events | event-detection | 2023-11 | 2025-11 | yes |
| [7][9][17] Competitor pose disclosures | competitor | 2025-03 | 2025-09 | yes |
| [6] Keypoint confidence calibration | capability | 2023-11 | 2024-11 | yes |
| [1] RTMPose-m CPU speed | performance | 2023-03 | 2023-09 | yes |
| [4] MediaPipe model-card speeds | performance | 2021-04 | 2021-10 | yes |
| [21] SwingNet PCE | event-detection | 2019-03 | 2021-03 | yes |

\* undated page, current when accessed.

**What "stale" means here:** the speed figures are old or vendor-only, and the age of the source is not the main problem. All three performance claims are superseded by a local benchmark on your own laptop (recommendation 4), which is cheaper than another search. SwingNet and the wrist heuristic are foundational methods; check them for newer work only if you choose SwingNet. **Earliest re-check that matters: now**, through the week-1 speed and model spike. Re-check licenses and competitor disclosures before a real (paid) launch.

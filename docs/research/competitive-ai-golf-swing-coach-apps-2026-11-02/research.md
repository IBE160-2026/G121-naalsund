---
title: 'Competitive research: AI golf swing coach apps'
type: 'competitive'
topic: 'AI golf swing coach apps'
decision: 'PRD differentiation for AIcoach: is the fault-chain / plain-language coaching / honest-confidence gap real, and which features are table stakes vs differentiators'
source: 'native run (2 rounds, 5 researcher digests)'
status: complete
preset: 'standard'
validation: 'normal'
created: '2026-11-02'
updated: '2026-11-02'
claims_verified: 5
claims_unverified: 3
claims_disputed: 1  # recon_kit tally over 9 ref-level claims (12 ledger lines; refs [1] and [15] carry several claims)
---

# Competitive research: AI golf swing coach apps

**Decision this research serves:** PRD differentiation for AIcoach: is the fault-chain / plain-language coaching / honest-confidence gap real, and which features are table stakes versus differentiators.

## Executive summary

**The gap is real, but it is narrower than the brief assumes. Reframe the differentiation around showing the evidence, not around the words "root cause".**

1. **Saying "we find the root cause" no longer sets you apart.** Performance Golf (about 5K ratings, very active) markets a "Root Swing Flaw … creating a chain reaction of symptoms" and names early extension as a symptom [16][17]. SwingCoach AI says it "finds the one fault causing the others" [15], and Mustard has a "potential causes" step [12]. What none of them shows is the chain itself: each link drawn from the player's own measurements, with evidence. None independently validates its claim either [15][16][17]. AIcoach's fault chain stands out only if it is explicit, built from the player's measurements, and checked against test videos with known answers.
2. **Two gaps are open, and the brief already plans for both.**
   - **Confidence per metric:** none of the roughly dozen live apps checked shows how confident it is in each measurement [1][8][12][15][16]. SwingCoach AI comes closest, and it only refuses to give a number when the angle is poor [15].
   - **A mobility exercise tied to the detected fault:** no swing-analysis app does this. DeepSwing added generic fitness content in August 2026, but not linked to faults [8][9]. TPI already publishes the link between mobility limits and faults (for example, a limited deep squat leading to early extension), so the idea is established rather than invented [24]. It just isn't built into an app.
3. **Users' biggest problem is not knowing what to do with the data.** Sportsbox is called "overwhelming" and "not beginner friendly" [1]. A Mustard reviewer writes "YOU have to figure out where you are having the issue" [11]. What users praise is plain-language explanation of the cause, drills that match the problem, and drawings on key frames [11][12]. That directly supports AIcoach's plain-language, coach-style output. Caveat: this rests on small samples, most from 2022–2025, and Reddit and Google Play could not be read.

**The biggest caveat:** grounded AI chat is no longer new. SwingCoach AI's Coach tab answers from the user's own analyses [15]. Sportsbox, the market leader (3.8K ratings, acquired in April 2026 by a group led by Bryson DeChambeau), shipped a Gemini-based coach called SAMI in September 2026. SAMI still answers preset questions only, but the vendor says "more to come very soon" [1][4]. Your course MVP already leaves free chat out, and this research supports that choice.

## Feature teardown

| Competitor | Capture | Explains causes | Confidence per metric | Drills / mobility | AI chat | Status |
|---|---|---|---|---|---|---|
| **Sportsbox 3D Golf** | 1 phone video turned into a 3D body model, no sensor [1] | Diagnose tab and Swing Flaw assessments; no chains between faults found [1][3] | None; no published validation [1][3] | 50+ practice drills; no mobility [2] | SAMI beta, Gemini, preset questions only [1][4] | Market leader; 4.9★ from 3.8K ratings [1] |
| **Performance Golf PG1 / SwingScan** | Phone camera, claims "3D motion-capture", 17 data points [16] | Markets a "root swing flaw" and a symptom chain [16][17] | None [17] | 100+ programs and drills; no mobility [16] | Human instructors ($99 review) [16] | Very active; about 5K ratings [16] |
| **Mustard** | 1 down-the-line video, no clubface [11][12] | Pre-written "potential causes" for each fault, from named coaches [12] | None [12] | Drills of 90 seconds or less; no mobility [12] | None found [11] | Active; 1.2K ratings [11] |
| **DeepSwing** | 1 video, face-on or down-the-line, 2D, analysed on the phone [8][9] | Maps ball misses to swing checks; says it can't see the clubface [8] | None; speed is "estimated" [8] | Drill per check; generic fitness since Aug 2026 [8][9] | Voice cues, no LLM [9] | Active (v3.4, Oct 2026); now leads with a launch monitor [8][9] |
| **SwingCoach AI** | 1 video, face-on or down-the-line [15] | "Finds the one fault causing the others" [15] | Declines to give a number when the view is poor; no graded confidence [15] | One drill per analysis; no mobility [15] | Coach tab grounded in the user's own analyses [15] | Too few ratings to display [15] |
| **HackMotion** | Wrist sensor, not video [6] | 13 wrist faults mapped to ball flight [6] | None [6] | Real-time biofeedback drills [6] | None [6] | No subscription; one-time purchase [7] |
| **Caddie AI, Swing IQ, Birdi, 18Birdies** | Phone video [18][19][20][21] | No root-cause claim [18][19][20] | None [18][19][20] | Drills [18][19][20] | Caddie AI has free chat over swing history [18] | Small or stale [18][19][20][21] |
| **Zepp Golf** | Sensor | — | — | — | — | Dead: US listing removed, last update 2019 [10] |

V1 Golf is a manual analysis tool whose chat connects to a human coach, so it is not an AI-coach competitor [14].

**Table stakes (an MVP must have these):** single-phone-video capture, an overall swing score, a drill for each fault, single-video capture and a drill for each fault [1][8][11][15]; history with side-by-side comparison of two swings [1][8][21].
**No longer unique:** root-cause marketing [15][16][17]; AI chat grounded in the user's own swing [15]; Caddie AI's chat also draws on swing history [18].
**Still open:** confidence per metric, a mobility exercise tied to the detected fault, and a fault chain where each step shows its evidence [15][16][17][24].

## Positioning

- **Sportsbox** leads with "the #1 Swing Analysis Tool on Tour" and serves golfers, coaches and academies [3]. DeChambeau calls SAMI "not a replacement for coaches" [4], and wants it to show "the five greatest deviators" in a swing [5]. The tour-level 3D promise is gated behind price: the $109.99/yr tier shows six measurements, and the full set costs $399.99/yr [2].
- **Performance Golf** sells a promise: "shave 5+ strokes off your handicap in 30 days", with no validation given [16].
- **Mustard** sells famous coaches' names (Justin Rose, Golf Digest), but the coaching is pre-written plans [12][13].
- **DeepSwing** is shifting its focus to a camera-based launch monitor and course GPS [8].
- **Nobody positions on honesty about accuracy** (inferred from the positioning reviewed [3][12][16]). That space is free, and it fits the distrust users voice [23].

## Customer voice

- **Interpretation burden.** Users say the data is "overwhelming", "not beginner friendly" and "very technical", and that they need to "know what you're looking for" [1][22]. A reporter testing Sportsbox also describes a learning curve [28]. A Mustard reviewer writes "YOU have to figure out where you are having the issue" [11]. One Sportsbox reviewer: "data is meaningless unless you understand the cause and effect relationships" [1] (2022, stale). Confidence: medium. It is consistent across several sources, but the samples are small and few are recent.
- **What earns praise:** a jargon-free video explaining the problem, a "potential causes" section, drills that match the problem, and key frames with drawings that give "confidence" [11][12].
- **Distrust tied to camera setup.** Small changes in camera position change the results [11]. Users value strict filming guidelines [23].
- **Distrust of AI is moderate.** Golfers fear "generic rubbish or wrong answers" and "ingraining the wrong things", and want the AI to agree with their coach [23]. Mixed: one Sportsbox user said "some of the tips have actually made my ball striking feel worse" [1].
- **Price resentment.** Mustard's roughly $24–30 a month and its paywall before any useful result both draw complaints [11][29].
- Nobody asks outright for "why" explanations. That demand is inferred from the complaints and praise above.

## Pricing (context for the later subscription)

| App | Price |
|---|---|
| Sportsbox | Free (5 swings/month) · $109.99/yr · $399.99/yr (full data) · $799.99/yr (coach) [2] |
| Performance Golf | $39/mo · $199–299/yr [16] |
| SwingCoach AI | $39.99/mo · $199.99/yr · 5 analyses for $2.99 [15] |
| Mustard | $24.99/mo or $149.99/yr (2024); cheaper tiers now also listed [11][12] |
| DeepSwing | Pro $9.99/mo · Complete $14.99/mo or $119.99/yr [9] |
| HackMotion | One-time purchase, no subscription [7]; about $275–915 according to search snippets of the product pages (low-medium confidence, possibly promotional) |

Most consumer tiers cost roughly $110–200 a year. The NOK comparison against a single lesson in your brief (600–1200 NOK) fits that range.

## Cross-dimension insights

- **Accuracy is the trust problem, and nobody is answering it.** Users distrust results that change with camera setup [11] and value strict filming guidelines [23]. Vendors publish no validation [1][3]. Academic work on markerless pose for golf is still unsettled [25]. Confidence per metric plus strict filming guidance therefore answers a real complaint, not just a nice-to-have.
- **Mobility tied to a fault is the cause-and-effect idea extended to the body.** TPI already maps body limits to swing faults [24], and the one app reported to find a hip-turn root cause gets praised for it [26] (that source is conflicted). The fault chain becomes AIcoach's own when it ends in a body limitation and a mobility exercise, because no app closes that loop [8][15][16].
- **Wrong advice is the main risk of AI coaching.** The fear users name is generic or wrong advice [23], and a harmful tip already appears in reviews [1]. Your brief already plans verified rules for three faults plus clearly labelled unverified observations. That is the right response, and no competitor checked makes that distinction visible; the nearest is SwingCoach AI declining to give a number when the view is poor [15].

## Contrary evidence

The red-team pass was off. The strongest counter-evidence found during verification:
- **Root cause:** "no app explains causes" is **disputed**. Performance Golf, SwingCoach AI and SR.AI all market root-cause or symptom chains [15][16][17][27]. The differentiation claim has been narrowed accordingly.
- **Accuracy:** the reply "within 99% accuracy of AMM", attributed to Sportsbox's developer in one digest, could **not be located** a second time. The quote came from a review reply [1]. According to a search snippet (not in the appendix), Sportsbox's chief science officer co-founded AMM, so even if the claim exists it is not independent. Unverified.

## Recommendations (for the PRD)

1. **Make "explainable fault chain" a requirement, not "root-cause detection".** Each link names the measurement behind it, the key frame and a confidence level. Recommended in the PRD's differentiation section. *Confidence: medium. The absence of competitors doing this is checked across roughly a dozen live apps, but no app was tried hands-on.*
2. **Keep a confidence level on every metric as a must-have, and add capture guidance** (camera position, a check on the angle). This answers the setup-distrust complaint. *Confidence: medium-high.*
3. **End each chain with a mobility exercise tied to the body limitation**, citing TPI-style screening logic as the domain basis. This is the clearest open gap. *Confidence: medium, based on absence across roughly a dozen live apps and a TPI source that is a methodology source, not a competitor.*
4. **Write the success criteria around plain-language output** (one fault, why, one drill, one exercise), not around how many metrics are shown. That targets the interpretation-burden complaint. *Confidence: medium. Small, older samples.*
5. **Keep free chat out of the MVP.** Grounded chat exists in small apps and Sportsbox is moving into it [1][15][18], so it is table stakes later, not something that sets AIcoach apart now. *Confidence: high for the MVP decision.*
6. **Table stakes for the PRD baseline:** single phone video, a drill for each fault, history with comparison of two swings. *Confidence: high.*

## Open questions

- How deep SAMI really goes, and which tier includes it. This needs a hands-on trial or a review; re-check by February 2027.
- Whether Performance Golf's SwingScan really shows chains or only names one root fault. This needs a hands-on trial (paid).
- Recent (≤ 12 months) customer voice from Reddit and Google Play. Both were blocked for these tools; you could run a drafted prompt in your own research tool.
- The Macro Golf Performance app (mobility self-screen plus drills) may already link screening results to faults. Not confirmed.

## Source appendix

| # | Supports | Publisher | Pub date | Accessed | Confidence |
|---|---|---|---|---|---|
| [1] | Sportsbox features, changelog (SAMI beta, preset questions), reviews | [Apple App Store: Sportsbox 3D Golf](https://apps.apple.com/us/app/sportsbox-3d-golf/id1578921026) | 2026-10-26 (v2.54.0) | 2026-11-02 | high (features); medium (reviews) |
| [2] | Sportsbox tiers and prices, measurements per tier | [Sportsbox pricing](https://www.sportsbox.ai/pricing) | 2026-10-26 | 2026-11-02 | high |
| [3] | Sportsbox positioning; no accuracy answer | [Sportsbox homepage](https://www.sportsbox.ai/) | undated | 2026-11-02 | medium |
| [4] | Acquisition, SAMI, Gemini | [Business Wire (vendor PR)](https://www.businesswire.com/news/home/20260407643695/en/) | 2026-04-07 | 2026-11-02 | medium |
| [5] | DeChambeau's stated aims for SAMI | [GolfMagic](https://www.golfmagic.com/news/bryson-dechambeau-google-ai-golf-training-tool) | 2026-04 | 2026-11-02 | high |
| [6] | HackMotion sensor, 13 faults, no AI | [HackMotion](https://hackmotion.com/choose-hackmotion/) | undated | 2026-11-02 | high |
| [7] | HackMotion one-time pricing | [HackMotion pricing](https://www.hackmotion.com/pricing/) | undated (©2026) | 2026-11-02 | medium |
| [8] | DeepSwing features, miss mapping, fitness, launch monitor | [deepswing.io](https://deepswing.io) | 2026-10-13 | 2026-11-02 | high |
| [9] | DeepSwing changelog, pricing, reviews | [Apple App Store: DeepSwing](https://apps.apple.com/us/app/deepswing/id6751551257) | ~2026-10-31 | 2026-11-02 | high |
| [10] | Zepp Golf dormant | [AppGoblin](https://appgoblin.info/apps/738428692) | undated | 2026-11-02 | medium |
| [11] | Mustard listing and reviews | [Apple App Store: Mustard](https://apps.apple.com/us/app/mustard-golf-swing-analysis/id6499280777) | ~2026-10-28 | 2026-11-02 | medium |
| [12] | Mustard causes/drills structure, pricing (2024) | [Plugged In Golf](https://pluggedingolf.com/mustard-golf-app-review/) | 2024-10-09 | 2026-11-02 | medium (stale) |
| [13] | Mustard launch positioning | [Warner Bros. Discovery press](https://press.wbd.com/us/media-release/golf-digest-mustard-launch-groundbreaking-ai-powered-platform-mustard-golf-help-every) | 2024 | 2026-11-02 | medium |
| [14] | V1 Golf: manual analysis, human chat | [Apple App Store: V1 Golf](https://apps.apple.com/us/app/id349715369) | ~2026-09 | 2026-11-02 | high |
| [15] | SwingCoach AI root cause, abstaining, Coach tab, pricing | [Apple App Store: SwingCoach AI](https://apps.apple.com/us/app/id6760660742) | 2026-09-10 | 2026-11-02 | high (claims made); unverified (efficacy) |
| [16] | Performance Golf PG1 features, root-cause claim, pricing | [Apple App Store: Performance Golf](https://apps.apple.com/us/app/-/id1664475856) | ~2026-10 | 2026-11-02 | high (claims made) |
| [17] | SwingScan "chain reaction of symptoms" | [Performance Golf SwingScan](https://pg1.performancegolf.com/quiz/dqfe-lp-01-never-guess) | 2026 | 2026-11-02 | medium (marketing) |
| [18] | Caddie AI free chat over swing history | [Apple App Store: Caddie AI](https://apps.apple.com/app/id6759304353) | ~2026-07 | 2026-11-02 | medium |
| [19] | Swing IQ: LLM via sampled frames, no root cause | [Apple App Store: Swing IQ](https://apps.apple.com/us/app/id6775244693) | ~2026-09 | 2026-11-02 | high |
| [20] | Birdi: drills, no chat, stale | [Apple App Store: Birdi](https://apps.apple.com/us/app/id6756025251) | ~2026-04 | 2026-11-02 | medium |
| [21] | 18Birdies AI Coach (2020) | [18Birdies](https://18birdies.com/clubhouse/18birdies-ai-coach-how-it-works/) | 2020-03-18 | 2026-11-02 | low (stale) |
| [22] | "Need to know what you're looking for" | [Golf Monthly forum](https://forums.golfmonthly.com/threads/sportsbox-ai-has-anyone-tried-it-swing-analysis.119354/) | 2025-10-24 | 2026-11-02 | medium |
| [23] | AI distrust, filming guidelines, agreement with coach | [Golf Monthly forum](https://forums.golfmonthly.com/threads/building-a-swing-analysis-tool-would-love-honest-feedback-from-golfers-coaches.119755/latest) | 2026-03 | 2026-11-02 | medium |
| [24] | Mobility limits linked to early extension | [TPI](https://cdn.site.mytpi.com/improve-my-game/swing-characteristics/early-extension) | undated | 2026-11-02 | medium (snippet) |
| [25] | Markerless golf accuracy unsettled | [Frontiers in Sports and Active Living](https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2023.1272038/epub) | 2023 | 2026-11-02 | medium (snippet) |
| [26] | Mustard found hip-turn root cause (investor-conflicted) | [Golf Digest](https://www.golfdigest.com/story/what-an-average-golfer-learned-about-his-swing-new-technology-mustard) | ~2024 | 2026-11-02 | low (snippet, conflicted) |
| [27] | SR.AI root-cause claim | [Apple App Store: SR.AI](https://apps.apple.com/app/id6741165328) | 2026 | 2026-11-02 | low (snippet) |
| [28] | Sportsbox learning curve (reporter) | [GeekWire](https://www.geekwire.com/2024/this-startup-helped-bryson-dechambeau-win-the-u-s-open-now-it-wants-to-improve-your-golf-swing/) | 2024 | 2026-11-02 | medium (snippet, stale) |
| [29] | Mustard price complaints (aggregated reviews) | [JustUseApp](https://justuseapp.com/en/app/6499280777/mustard-golf-swing-analysis/reviews) | undated | 2026-11-02 | low |

## Staleness map

Re-check dates come from `recon_kit.py staleness`, using these windows: features 3 months, pricing 3 months, trajectory 6 months, sentiment 12 months.

| Claim | Class | Published | Re-check by | Stale now? |
|---|---|---|---|---|
| Mustard pricing $24.99/mo (2024 media) | pricing | 2024-10 | 2025-01-01 | **yes** |
| Interpretation burden is the main user complaint | sentiment | 2025-09 | 2026-09-01 | **yes** |
| Sportsbox acquisition / SAMI on Gemini | trajectory | 2026-04 | 2026-10-01 | **yes** |
| Root-cause marketing exists (SwingCoach AI, Performance Golf, Mustard) | features | 2026-09 | 2026-12-01 | no |
| Grounded chat exists in small apps | features | 2026-09 | 2026-12-01 | no |
| No app shows per-metric confidence | features | 2026-10 | 2027-01-01 | no |
| No app ties a mobility exercise to a detected fault | features | 2026-10 | 2027-01-01 | no |
| SAMI answers preset questions only | features | 2026-10 | 2027-01-01 | no |
| Competitor pricing table | pricing | 2026-10 | 2027-01-01 | no |
| AI distrust is moderate; users want the AI to agree with their coach | sentiment | 2026-03 | 2027-03-01 | no |

Three claims are already stale: Mustard's current pricing, recent customer sentiment, and SAMI's current state. They are flagged above and do not decide any recommendation on their own. **The earliest live re-check is 2026-12-01**, for the root-cause and grounded-chat claims. That falls right around your MVP deadline, so run a Refresh before the final PRD revision or the course hand-in.

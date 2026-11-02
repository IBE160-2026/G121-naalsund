# Teardown B, round 1: DeepSwing, Zepp Golf, AI-coach apps (Mustard, Sportsbox 3D Golf, V1 Golf)

- **Competitors covered:** DeepSwing (Deep Platforms GmbH), Zepp Golf (Zepp Inc.), Mustard Golf (QualiaOS / Golf Digest), Sportsbox 3D Golf (Sportsbox AI), V1 Golf (V1 Sports). V1 is a side check: it is a manual/human-coach analyzer, not an AI coach.
- **Accessed:** 2026-11-02
- **Method:** 18 tool calls: 8 searches and 10 fetches (3 fetches failed with 403/404). Primary sources are App Store listings including version history, plus deepswing.io. Secondary sources are Plugged In Golf and AppGoblin.
- **Date note:** App Store version histories omit the year for recent entries. I inferred the year from the version sequence: entries after a dated 12/2025 entry are 2026. Confidence on those dates is medium.

## Claims

Format: claim | source URL | publisher | pub_date | accessed | confidence | class

### DeepSwing
1. Active and shipping fast. More than 25 iOS releases since 1.0.1 (2025-10-26). v3.3.0 to v3.3.2 landed Sep 25 to Oct 15 (2026). v3.4.0 shipped about 2 days before access (about 2026-10-31). | https://apps.apple.com/us/app/deepswing/id6751551257 | Apple App Store (Deep Platforms GmbH) | undated listing | 2026-11-02 | high | status/release
2. v3.4 repositions the app into three areas: AI Coach, a camera-based **Launch Monitor** (240 fps iPhone on a tripod, "no radar"; ball speed, launch, direction, carry, total; GSPro/simulator feed) and **Golf GPS** (12,000+ courses). The US App Store title now reads "DeepSwing: Golf Launch Monitor". Launch Monitor and GPS are iPhone only, with Android "coming soon". | https://deepswing.io | Deep Platforms | "As of October 13, 2026" | 2026-11-02 | high | release/positioning
3. Capture: a single phone video. Face-on and down-the-line views, autocapture that detects the view and trims the clip, multi-swing sessions, Apple Watch remote, a second iPhone/iPad as camera, and import of slow-mo or library videos. 2D pose/clubhead analysis; the "3D" appears only in the range/hole maps and the "3D Ghost Overlay". No sensor. | deepswing.io + App Store listing | Deep Platforms | Oct 2026 | 2026-11-02 | high | feature
4. **On-device analysis**: "core analysis runs right on your device", and videos are not uploaded for analysis. This is a privacy differentiator. | https://deepswing.io | Deep Platforms | Oct 2026 | 2026-11-02 | medium (vendor claim, not verified) | capability-claim
5. Metrics: Swing Score built from 20+ checks (the App Store says 27), automatic phase detection, swing plane and over-the-top measured from the clubhead path, tempo, and estimated clubhead/ball speed from face-on video, with history per club. | deepswing.io; App Store | Deep Platforms | Oct 2026 | 2026-11-02 | high | feature
6. **Accuracy/confidence: none quantified.** Speed and spin are labelled "estimated", and the listing only advises good light and a steady tripod. No per-metric confidence is shown. | deepswing.io; App Store | Deep Platforms | Oct 2026 | 2026-11-02 | high | feature (absence)
7. Partial **cause-to-effect**: each miss type (slice, hook, push, pull, fat, thin) is mapped to a common cause, a fix direction and the checks examined. The site admits it does not measure the clubface and infers the miss tendency. v3.4 adds a "stuck" club-path explanation and "explains why the ball flew" by linking launch-monitor output to swing faults. This is miss-to-fault mapping, not fault-to-fault causal chains (e.g. mobility to compensation). | deepswing.io; App Store v3.4 notes | Deep Platforms | Oct 2026 | 2026-11-02 | medium | feature
8. Drills: a drill per check, a searchable drill library, a weekly training plan generated from 3 questions, a 7-chapter starter guide, and **golf fitness (mobility and strength) content added in v3.2 (Aug 2026)**. | deepswing.io; App Store | Deep Platforms | Aug to Oct 2026 | 2026-11-02 | high | feature/release
9. No LLM or chat coach found. "Live Coach" gives real-time voice, visual and haptic cues plus voice commands (v2.1, Feb 2026). | App Store; deepswing.io | Deep Platforms | 2026 | 2026-11-02 | high (for absence on own pages) | feature
10. History and comparison: sessions with filters and favorites; side-by-side, phase-synced two-swing comparison; export with overlays. | deepswing.io | Deep Platforms | Oct 2026 | 2026-11-02 | high | feature
11. Pricing (US IAPs): Pro $9.99/mo, Pro $59.99 (likely yearly), Complete $14.99/mo or $119.99/yr, Launch Monitor $79.99/yr or $159.99 lifetime, Total Lifetime $249.99, Watch GPS $29.99/yr. Free GPS on iPhone. AI Coach has a 7-day trial on the yearly plan. Launch Monitor gives 5 free shots per week. | App Store; deepswing.io | Deep Platforms | Oct 2026 | 2026-11-02 | high | pricing
12. Positioning: "Your golf swing. Analyzed by AI." Aimed at all levels, from beginners ("clear first step") to low handicappers and coaches (frame-level detail). Small user base: 52 ratings on the US store, while the site claims 4.7 from 136 ratings on iOS and 4.4 from 68 on Google Play. | deepswing.io; App Store | Deep Platforms | Oct 2026 | 2026-11-02 | medium | positioning

### Zepp Golf
13. **Dormant or delisted.** The US App Store URL returns 404. AppGoblin says "removed from the US App Store and no longer live", with the last store update on **2019-01-14**. | https://appgoblin.info/apps/738428692 | AppGoblin (aggregator) | undated | 2026-11-02 | medium-high (404 confirmed directly) | status
14. The Zepp Golf 2 sensor is listed as "no longer available" at a retailer. The product was sensor-based (clip-on IMU), not video-first. Non-US App Store pages (fr, ru) were still indexed, so they may persist regionally (unverified). | https://www.coolblue.nl/en/product/729872/zepp-golf-2.html | Coolblue | undated | 2026-11-02 | low-medium | status

### Mustard Golf
15. Active: v1.7.7 shipped about 2026-10-28, and roughly 25 releases since 07/2025. Notable releases: web billing (v1.4.0, Apr 2026), slow-mo drill reports (v1.3/1.4, Apr 2026), self-paced plans (v1.7.0, Jul 2026). Most notes are generic. iPhone only. 4.7 from 1.2K ratings. | https://apps.apple.com/us/app/mustard-golf-swing-analysis/id6499280777 | Apple App Store (QualiaOS) | undated | 2026-11-02 | high | status/release
16. Capture: single phone video recorded in-app or imported, with virtual body markers. The AI is built on 3D models of pro and amateur swings, with no sensors. Reader comments (2024) say it analyzes **down-the-line only** and does not evaluate the clubface. A 2026 App Store reviewer says camera position affects results and that posture, grip and alignment are outside the model. | https://pluggedingolf.com/mustard-golf-app-review/ ; App Store | Plugged In Golf; Apple | 2024-10-09; undated | 2026-11-02 | medium | feature
17. Output: Overall Score, Swing Path Score, and body/hands ratings for backswing and downswing, plus improvement priorities and strengths. No accuracy or confidence display found. | pluggedingolf.com review | Plugged In Golf | 2024-10-09 (older than 3 months) | 2026-11-02 | medium | feature
18. **Cause explanation**: each improvement plan follows "define the issue" video, then "potential causes", then drills (90 seconds or less). The causes are curated coach content (Mark Blackburn, Michael Jacobs, Justin Rose, Jason Goldsmith), not generated per swing. There is no way to enter your own problem (e.g. a slice) and no short game. | pluggedingolf.com review; App Store | Plugged In Golf | 2024-10-09 | 2026-11-02 | medium | feature
19. No AI chat or LLM coach found in the listing or review. Progress means re-uploading after drills; one App Store reviewer reports a once-weekly upload cadence and asks for old-vs-new video comparison (so comparison is likely absent or weak). | App Store | Apple | 2026 | 2026-11-02 | medium | feature
20. Pricing: free tier shows the top fault. Premium was $24.99/mo or $149.99/yr per 2024 media. Current US IAPs also list $9.99/mo, $49.99/yr and $28.99/$172.99 variants, which suggests price testing or a cheaper tier. | App Store; Plugged In Golf; WBD press | Apple; PIG | 2026 / 2024 | 2026-11-02 | medium | pricing
21. Positioning: co-launched by Golf Digest (Warner Bros. Discovery) and Justin Rose. Big-name coach brand, "help every golfer" improve. The gap between claim and product: coach names are the brand, while the coaching is pre-scripted plans. | https://press.wbd.com/us/media-release/golf-digest-mustard-launch-groundbreaking-ai-powered-platform-mustard-golf-help-every | WBD press | 2024 (undated in results) | 2026-11-02 | medium | positioning

### Sportsbox 3D Golf (closest LLM-coach rival)
22. **Acquired April 2026** by an investor group led by Bryson DeChambeau, which announced "**SAMI**" (Sportsbox AI Motion Intelligence), billed as "agentic AI coaching". Search snippets say it is built on Google Gemini (the press release fetch returned 403, so the Gemini detail is unverified). | https://www.businesswire.com/news/home/20260407643695/en/ | BusinessWire | 2026-04-07 | 2026-11-02 | medium | release/status
23. **SAMI Beta shipped in v2.53.0 (Sep 23, 2026)**: an AI assistant from the home screen that answers **preset questions** (using the app, understanding the data, improving the swing) with general and personalized guidance from swing data. v2.54.0 (Oct 26) still calls it Beta with "more coming". So it is not yet free-form chat. | https://apps.apple.com/us/app/sportsbox-3d-golf/id1578921026 | Apple App Store (Sportsbox AI) | 2026-09-23 / 10-26 | 2026-11-02 | high | release/feature
24. Other generative-AI features: "AI Highlights" tips for Player subscribers (v2.48, Apr 2026); "Roast My Swing" AI diagnosis (v2.43, Oct 2025) with text-to-speech (v2.51, Jul 2026). | App Store | Apple | 2025–2026 | 2026-11-02 | high | feature/release
25. Capture: **single phone video turned into a 3D body model** (markerless, no sensors). Face-on and DTL views, auto swing detection, import supported. Metrics: sway, turn, tilt, side bend, pelvis/chest opening, tempo, speed factors, Swing Score, and a Diagnose tab (Swing Flaw, Speed, Consistency assessments). Tour-average reference ranges with guidance were added in v2.52 (Sep 2026). | App Store | Apple | 2025–2026 | 2026-11-02 | high | feature
26. **No accuracy or confidence figures** in the listing. Only a testimonial ("Like a Trackman for the swing"). Reviews cite bugs, crashes and a "not beginner-friendly" experience. | App Store | Apple | 2026 | 2026-11-02 | high | feature (absence)
27. Comparison and progress are strong: a Comparison tab with 3D-over-3D avatar overlay (v2.46, Jan 2026), 2D video overlay (v2.48), comparison against tour-pro models, goals, Practice Mode, and a coach/student workflow (shared sessions, messaging, credits). Drills are weak (only drill-video tweaks; no clear library). No mobility/fitness prescriptions found. | App Store | Apple | 2026 | 2026-11-02 | high | feature
28. Pricing (US IAPs, periods not shown): Player $15.99 and $109.99 (likely monthly/yearly); Pro $79.99 and $799.99 (coach tier). 4.9 from 3.8K ratings, which is the largest user base among these apps. | App Store | Apple | 2026 | 2026-11-02 | medium (billing periods inferred) | pricing

### V1 Golf (checked, low relevance)
29. A video analyzer with manual drawing tools, skeletal tracking, ball tracing, side-by-side/overlay comparison with pro models and pressure-plate integration. Its chat connects to a **human** coach, and the listing mentions no AI auto-diagnosis or LLM. Latest v5.15.0 (Sep 23, likely 2026), mostly generic notes. Plus $9.99/mo or $79.99/yr, Advanced V1sion $14.99/$119.99, online lesson $59.99. | https://apps.apple.com/us/app/id349715369 | Apple App Store (V1 Sports) | undated | 2026-11-02 | high | feature/pricing
30. V1 markets "AI golf coaching tools" to **instructors** (Coach platform), not consumers. | https://grow.v1sports.com/grow/ai-golf-coaching-tools | V1 Sports | undated | 2026-11-02 | low (not fetched) | positioning

## Cross-cutting takeaways
- **No competitor shows per-metric accuracy or confidence.** This is an open differentiator.
- **Cause-to-effect is shallow everywhere.** Mustard uses curated "potential causes" per fault; DeepSwing maps ball miss to swing checks; Sportsbox has diagnosis assessments. None was found explaining fault chains (e.g. restricted hip turn causing early extension) or linking body limitations to faults.
- **LLM chat is only just arriving.** Sportsbox SAMI is Beta with preset questions since Sep 2026. No free-form, swing-grounded chat was verified in any app.
- **Mobility/fitness**: only DeepSwing (v3.2, Aug 2026) adds generic golf-fitness content. None ties exercises to a detected fault.

## Leads worth chasing
- Sportsbox SAMI: roadmap to free-form chat, Gemini grounding, and which tier includes it (Player vs Pro). Try sportsbox.ai blog or help center; GeekWire and BusinessWire returned 403.
- 18Birdies AI Coach (video swing analyzer with drill recommendations), in its 2026 state. Not fetched.
- Newer low-rating LLM-ish apps: SwingCoach AI (id6760660742, 50+ languages, 5-swing pack), Birdi – AI Golf Pro (id6756025251), Swing IQ (id6775244693), Performance Golf SwingFix AI, AIGolfChat (id6745116443). Check whether any offers free-form chat over the user's swing.
- Mustard: confirm current tiers ($9.99 vs $24.99/mo) and whether face-on analysis or video comparison now exists.
- DeepSwing Android parity and Google Play listing; independent accuracy tests of DeepSwing's camera launch monitor.

## Looked for, not found
- Any published accuracy, validation study or per-metric confidence UI (DeepSwing, Mustard, Sportsbox, V1).
- An LLM or free-form chat coach in DeepSwing, Mustard or V1 (V1 chat is with a human).
- Fault-to-fault causal explanations, and mobility screening linked to swing faults, in any app.
- An official Zepp end-of-life notice. Only the US App Store 404 and an aggregator saying "removed" (last update 2019).
- Golf media reviews of Mustard or Sportsbox from 2026 (the only review fetched is from 2024).
- A Mustard pricing page or help docs. Not located within budget.

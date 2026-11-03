# D1 round 2 — lead inline lookup: competitor pose technology

Questions owned: how Performance Golf SwingScan, Mustard, OnForm/CoachNow, SwingCoach AI and similar apps do pose analysis (2D/3D, on-device/cloud, angles, validation). Run inline by the lead (8 tool calls) because R2-A ran out of budget on this user-requested question.

## Claims

1. Mustard says it analyses uploaded swing video against 3D models and motion-capture data from thousands of pro and amateur swings, using a "patented computer vision and AI system". It started as a baseball pitching app (Tom House), and Golf Digest is a minority investor. No accuracy validation was found. | https://www.golfdigest.com/story/what-an-average-golfer-learned-about-his-swing-new-technology-mustard (search snippet; page returned 403) + https://www.justinrose.com/2024/mustard-app-how-average-golfers-can-improve-through-new-ai-technology/ (search snippet) | Golf Digest; JustinRose.com | 2024-07 | accessed 2026-11-03 | low (marketing-adjacent, investor-affiliated, snippets only) | competitor
2. Performance Golf SwingScan: the landing page has no technical detail. The sister product SwingFix AI describes a three-step flow (record on a phone, then AI finds the swing flaws) and discloses no model or validation. | https://pg1.performancegolf.com/quiz/dqfe-lp-01-never-guess ; https://www.performancegolf.com/swingfix-ai/swingfix-ai-benefits (search snippets) | Performance Golf | unknown | accessed 2026-11-03 | low | competitor
3. CoachNow AI skeleton tracking "automatically detects and tracks the movements of athletes", "regardless of the shooting angle", "even when the athlete is standing sideways". It does not say 2D or 3D, does not name a model, makes no numeric accuracy claim, and the author calls it "NOT a silver bullet". | https://coachnow.com/blog/using-coachnows-ai-tools | CoachNow | 2025-03 | accessed 2026-11-03 | medium (primary, qualitative) | competitor
4. A third-party listing describes OnForm as overlaying an AI "skeleton" on any video and turning 2D video into 3D analysis with 12 swing metrics. No official technical page was found. | https://www.saashub.com/onform (search snippet) | SaaSHub (aggregator) | unknown | accessed 2026-11-03 | low | competitor
5. SwingNote Golf AI Coach: the user selects the camera angle (face-on or down-the-line). Pose data is "extracted right on your device", and from v1.7.0 "only numeric metrics are sent to the server" and videos are not stored. The listing names no model. | https://apps.apple.com/app/id6783664876 | Apple App Store listing (developer text) | 2026-10 | accessed 2026-11-03 | medium (primary, developer claim) | competitor
6. SwingCoach AI listing: frame-by-frame analysis of the phases address, takeaway, top, downswing, impact and finish to identify faults. No camera or model detail. | https://mwm.ai/apps/swingcoach-ai/6760660742 (search snippet) | mwm.ai (app aggregator) | unknown | accessed 2026-11-03 | low | competitor
7. A developer case study for an AI golf swing analyser reports that it had to handle face-on and down-the-line angles, left- and right-handed players and occlusion from hats and clubs, and that "off-the-shelf pose models were not reliable enough for outdoor golf footage". | https://litslink.com/case-studies/ai-golf-swing-analyzer (search snippet; page returned 403) | Litslink | unknown | accessed 2026-11-03 | low (snippet only, vendor case study) | capability
8. Apps such as Swing4Eagle (Face-On / Down-the-Line / Auto) and BirdieBud (face-on and DTL capture) make the user pick or auto-detect the camera angle. Angle-specific analysis is the norm. | https://apps.apple.com/app/swing4eagle/id6776530825 ; https://marlvel.ai/api/llm/apps/sports/birdiebud-golf-swing-coach (search snippets) | App Store; marlvel.ai | unknown | accessed 2026-11-03 | low | competitor

## Leads worth chasing
- Mustard's patent (search the assignee "Mustard" on Google Patents) for its pipeline.
- A hands-on trial of SwingScan or Mustard (paid), as already flagged in the competitive research.

## Looked for but not found
- Any competitor that discloses its pose model, or publishes accuracy validation for DTL footage (apart from Sportsbox's face-on study from round 1).
- SwingCoach AI and Performance Golf technical pages.

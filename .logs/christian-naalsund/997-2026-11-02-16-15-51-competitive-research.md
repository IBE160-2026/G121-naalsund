# Competitive research

## 2026-11-02 kl. 16:15 — Christian Naalsund

### Task
Run BMad Deep Recon (competitive) to check whether AIcoach's planned differentiators are real (fault chains, plain-language coaching, honest confidence), and to sort features into table stakes and differentiators as input to the PRD.

### Plan
- Approved plan: explore shape, `standard` preset (3 researchers, 2 rounds), validation `normal`, red team off.
- Competitors: Sportsbox AI, HackMotion, DeepSwing, Zepp Golf, plus AI-coach apps found during the search.
- Dimensions: feature teardown, positioning, customer voice, pricing (light). Trajectory dropped.
- Round 1: A = Sportsbox + HackMotion, B = DeepSwing + Zepp + AI coaches, C = customer voice.
- Round 2: D = newer LLM coach apps, E = second-source checks on the key claims.
- Finalize: mechanical citation check, then a semantic citation check by a fresh-context agent, then the HTML briefing.
- Process memory: `docs/research/competitive-ai-golf-swing-coach-apps-2026-11-02/.memlog.md`

### Result
- `docs/research/competitive-ai-golf-swing-coach-apps-2026-11-02/`, committed in `e1c4fca` and pushed to `origin/main`:
  - `research.md` (status complete, 29 sources)
  - `research-briefing.html`
  - `digests/` (5 researcher digests)
  - `.memlog.md`
- Main findings:
  - "Root cause" is already marketed, so it is not a differentiator. Performance Golf SwingScan, SwingCoach AI and Mustard all claim it. The open space is an explicit chain where each step shows its evidence (measurement, key frame, confidence).
  - Open gaps:
    - Confidence per metric: no app checked has it.
    - A mobility exercise tied to the detected fault: no app has it. TPI publishes the logic.
  - Grounded chat already exists in small apps (SwingCoach AI). Sportsbox shipped the SAMI beta (Gemini, preset questions) in September 2026. This supports keeping free chat out of the MVP.
  - Biggest user complaint: "I don't know what to do with the data". Small, older samples.
- Semantic citation check: 9 minor mismatches and 4 uncited sentences, all fixed. The core claims hold.
- Claims tally (`recon_kit`, 9 claims): 5 verified, 3 unverified, 1 disputed.
- At the user's request, the effort level (`standard`: 3 researchers × 2 rounds, ~8 sources per round, ~95 tool calls) is now shown in `research.md` and the briefing header.

### Open items
- Use the findings in the PRD: frame the differentiation as an "explainable fault chain + confidence per metric + mobility tied to the fault", not as "root-cause detection".
- Refresh the competitive research before the final PRD or the course hand-in. The earliest re-check date is 2026-12-01.
- Recent customer voice (≤ 12 months, Reddit and Google Play) is missing because those sites were blocked. Possible fix: a Deep Recon draft prompt run in your own research tool.
- The configured document standard (`bmad-review` with the structure and prose lenses) was not applied to `research.md`.

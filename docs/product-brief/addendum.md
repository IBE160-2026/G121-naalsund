---
title: AIcoach Brief Addendum
created: 2026-09-19
---

# Addendum: depth that does not belong in the brief

## Competitive landscape (user-supplied research, not independently verified)
- Existing apps: Sportsbox AI (3D skeleton from phone video, personalized target model, trends), Zepp Golf, DeepSwing, HackMotion (wrist-focused).
- Single 2D phone video cannot measure club path, face angle, ball flight, or ground reaction forces reliably. Elite players already use TrackMan, GEARS, K-Vest, force plates.
- Camera pose estimation is strong for relative within-person tracking, weaker for absolute biomechanical precision.
- Rules of Golf prohibit AI-generated advice during a competitive round, so any tool is practice/preparation only.
- Suggested gap: most apps measure well and communicate poorly; an LLM coach layer that translates numbers into feel-based cues and drills.

## Feature candidates (user-supplied, pending selection)
Foundation (table stakes): guided multi-angle capture; 3D checkpoint scoring against a personalized target model; session history and trends; drill prescriptions tied to faults; optional launch monitor / wrist-sensor pairing.

Signature candidates: fault chains (causal explanation, e.g. early extension traced to restricted hip turn); cue memory (reuse phrasing that worked for this player); honest confidence score on every metric; drift-watch (flag slow mechanical change before it shows in scores); one-tap coach handoff (2-minute brief for a human coach).

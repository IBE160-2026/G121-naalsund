---
title: AIcoach Product Brief
status: final
created: 2026-09-19
updated: 2026-09-19
---

# AIcoach — Product Brief

## Problem
Good golf coaching is expensive and hard to reach. Most golfers get a lesson now and then, or none, and try to fix their swing from videos and guesswork. Feel and reality often disagree in golf, so unguided practice can reinforce the wrong thing. Existing swing apps measure well but leave the player to interpret graphs and lists of deviations.

## Vision
AIcoach is a web app that replaces the coach for golfers who cannot afford or access one, and grows toward replacing the coach at every level. The AI is the coach: the player talks to it the way they would talk to their own coach.

The player uploads face-on and down-the-line swing videos. The AI finds where the problem comes from, explains it in plain language, and prescribes drills plus generic mobility and gym work to fix it.

## Target user
- **Primary:** golfers between +2 and 15 handicap who want to improve and lack regular access to a coach.
- **Also usable by:** everyone else, including beginners and elite players (elite players as a complement to their coach in v1).

## What makes it different
- **Fault chains.** Instead of a flat list of deviations, AIcoach traces cause to effect, for example early extension caused by a restricted hip turn, the way a coach reasons. First upload result: the fault chain, one drill and one mobility exercise.
- **Cue memory.** The AI learns which drills and phrasing actually change this player's swing. Progress is judged from the next swing videos, not from how the swing feels. If a drill does not work, it tries an alternative.
- **Honest measurement.** Uses existing 3D pose technology on two phone videos. Every metric shows a confidence level; AIcoach does not claim launch-monitor precision.

## Boundaries
- Mobility and gym advice is generic and educational, not medical. AIcoach recommends seeing a physio when a specific problem surfaces.
- Practice and preparation tool only: the Rules of Golf bar AI advice during competitive rounds.

## Scope and phasing
Solo project, course deadline early December 2026. Revenue model: subscription, introduced at real launch and not part of the course MVP.

| Phase | Contents |
|---|---|
| **Course MVP (early Dec)** | Account, conversational coach chat, and video upload (face-on and down-the-line); pose analysis with confidence levels; fault chain explained in plain language; one drill and one mobility exercise; upload history so a second video can be compared with the first |
| **First real release** | Cue memory that learns what works from follow-up videos; alternative drills when one fails; swing score built from fault-chain findings and shown with its confidence; subscription |
| **Later** | Launch-monitor data import (for example TrackMan) for club path, face angle and ball flight; features for elite players |

## Open questions
- Subscription price, benchmarked against a 600-1200 NOK lesson.
- Tech stack and pose-estimation approach.
- GDPR handling of video and coaching-memory data.
- Success metrics: measurable swing improvement, or weekly return rate?

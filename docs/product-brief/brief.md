---
title: AIcoach Product Brief
status: revised
created: 2026-09-19
updated: 2026-11-02
---

# AIcoach — Product Brief

## Summary
AIcoach is a web app that gives golfers coach-style feedback on their swing. The player films one swing from down-the-line with a phone and uploads it. The app finds up to three known swing faults with 2D pose estimation and a rule table, shows the likely cause behind each fault (a *fault chain*), and gives one drill and one mobility exercise per fault. A language model explains the result in plain language. The course MVP is deliberately narrow: one angle, three faults, a fixed library of drills and exercises, and checks against test videos whose correct answers are decided in advance.

## Problem
Good golf coaching is expensive and hard to reach. Most golfers get a lesson now and then, or none, and try to fix their swing from videos and guesswork. Feel and reality often disagree in golf, so unguided practice can reinforce the wrong thing. Existing swing apps measure well but leave the player to interpret graphs and lists of deviations.

## Target user
**Primary:** golfers between +2 and 15 handicap who want to improve and lack regular access to a coach.

**Usage situation:** the player is at the driving range or in a net with a phone. They film a swing, upload it, read the result, and practise the drill in the same session or the next one.

## Solution: user flow (course MVP)
1. **Sign in.** The player creates an account. Their videos and results are private to them.
2. **Film.** A short guide shows how to film from down-the-line: phone at hip height, on the hand line, whole body and club in frame, one swing per clip.
3. **Upload.** The player uploads the clip (mp4/mov, up to 15 seconds).
4. **Analysis.** The app runs 2D pose estimation locally, measures the swing, and checks it against the rule table for three faults. If the video is too poor to analyse (low pose confidence, wrong angle, body out of frame), the app says so and repeats the filming tips instead of guessing.
5. **Result.** For each detected fault the player sees:
   - the fault and the measurement that triggered it, with a confidence level
   - the likely cause from the fault-chain table
   - one drill and one mobility exercise from a fixed library
   - a short plain-language explanation from the language model, built only from these facts
6. **History (if time allows).** The player uploads a new swing and sees it next to the previous one for at least one measurement.

## Faults in the course MVP (draft)
All three faults are visible from down-the-line. Thresholds and confidence rules are set and tuned against the test videos and documented in the PRD.

| Fault | How it is measured (2D landmarks) | Likely cause (fault chain) | Drill | Mobility exercise |
|---|---|---|---|---|
| Early extension | Hips move toward the ball between address and impact | Restricted hip rotation | Wall drill (glutes stay on the wall) | 90/90 hip rotation |
| Loss of posture | Head and shoulders rise during the downswing | Weak hip hinge or tight hamstrings | Alignment stick head drill | Hip-hinge / hamstring mobility |
| Over the top | Hand path in transition is above the backswing path | Upper body starts the downswing | Pump drill | Thoracic rotation (open books) |

The fault-chain table, thresholds and drill library live in a separate analysis module that can be tested without the web app or the language model.

## What makes it different
- **Fault chains.** Instead of a flat list of deviations, AIcoach traces cause to effect, the way a coach reasons.
- **Honest measurement.** Every measurement shows a confidence level, and the app refuses to analyse a video it cannot read. AIcoach does not claim launch-monitor precision.
- **Controlled AI.** The language model explains results; it does not decide them. Faults, causes and drills come from the rule table, so they can be tested.

## Success criteria (course MVP)
1. **Detection:** on the labelled test set (at least 4 videos per fault plus 3 swings without the faults), the app finds the labelled fault in at least 75 % of fault videos and reports no fault on at least 2 of the 3 clean swings.
2. **Complete result:** for a test video with clear early extension, the result shows the fault, its measurement and confidence, the likely cause, one drill and one mobility exercise.
3. **Rejects poor input:** a test video filmed face-on, or with the body partly out of frame, gives a "cannot analyse" message with filming tips, not a fault.
4. **Grounded explanation:** the AI explanation names only the faults, causes, drills and exercises from the analysis. Tested with fixed analysis inputs and a check on the output.
5. **Speed:** a 10-second clip is analysed in under 2 minutes on an ordinary laptop.
6. **Privacy:** a signed-in user cannot see or open another user's videos or results.
7. **Runs for the examiner:** the app runs locally by following the README, with pose estimation running locally and an LLM test mode, so no paid account or project keys are needed.
8. **Comparison (if time allows):** a second video on the same account can be compared with the previous one for at least one measurement.

## Quality assurance
- **Test videos with correct answers.** A small set of swings filmed of myself (consent to publish) and labelled in advance with which faults they show. The labels are checked by a coach if possible. The set lives in the repo and is used as automated tests throughout the project.
- **Rules as tables.** Faults are written as thresholds and fault chains as tables, so each rule can be unit-tested with fixed landmark data.
- **LLM test mode.** The language model is behind an interface with a mock, so tests and the examiner can run without an API key.

## Boundaries
- Mobility and gym advice is generic and educational, not medical. AIcoach recommends seeing a physio when a specific problem surfaces.
- Practice and preparation tool only: the Rules of Golf bar AI advice during competitive rounds.
- Uploaded user videos are stored outside Git. Secrets go in `.env`, with `.env.example` in the repo.

## Not included in the course MVP
- Face-on video, two angles together, and 3D pose
- Free conversation with the coach (chat)
- Faults beyond the three above
- Cue memory, alternative drills when one fails, and swing score
- Personalised gym or mobility plans
- Launch-monitor import (for example TrackMan)
- Subscription and payment
- Native mobile app

## Scope and phasing
Solo project, course deadline early December 2026.

| Phase | Contents |
|---|---|
| **Course MVP (early Dec)** | Account; filming guide; upload of one down-the-line video; local 2D pose with confidence; three faults with rule-based fault chains; one drill and one mobility exercise per fault; AI explanation. If time allows: history and comparison of two videos |
| **First real release** | Face-on video and more faults; conversational coach chat; cue memory that learns what works from follow-up videos; alternative drills; swing score shown with its confidence; subscription |
| **Later** | Two-angle 3D analysis; launch-monitor data import (for example TrackMan); features for elite players |

## Vision
Long term, AIcoach should replace the coach for golfers who cannot afford or access one, and grow toward replacing the coach at every level. In that future the player talks to the AI the way they would talk to their own coach, and it learns which cues actually change their swing. The course MVP is the first step: proving that the app can find a fault, explain its cause and prescribe a fix reliably on one angle.

## Open questions
- Pose library and tech stack (planned: an established library that runs locally, for example MediaPipe). Decided in the architecture.
- Exact thresholds for the three faults, set from the test videos.
- My own golf background as the basis for judging the test-video labels, and whether a coach can check them.
- GDPR: how long videos are stored, and deleting a user's data.
- Subscription price for the real launch, benchmarked against a 600–1200 NOK lesson.

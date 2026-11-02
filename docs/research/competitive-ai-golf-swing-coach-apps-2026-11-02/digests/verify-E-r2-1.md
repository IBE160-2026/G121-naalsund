# Verify E, round 2, pass 1: golf swing app claims V1-V4

Accessed 2026-11-02 · Verification researcher · Budget: about 18 tool calls; 19 used (16 web searches/fetches plus 1 that failed because reddit.com is blocked).
Method: short web queries plus fetches. Reddit is NOT reachable (search API returned HTTP 400 "domain not accessible"). Fetches of mygolfspy.com and geekwire.com returned HTTP 403. The Google Play page came back truncated or empty. Where a fetch failed, the evidence below comes from search-engine snippets of those pages and is marked "snippet".

Confidence scale: H = primary or independent source read directly; M = snippet or secondary; L = marketing or unsourced.

---

## V1. Sportsbox shows no per-metric confidence; its accuracy claims are generic
**Verdict: partly verified (absence confirmed, not proven); the "99% of AMM" quote could not be found.**
I found no independent accuracy test of Sportsbox and no Sportsbox validation figures. Neither the App Store listing nor its release notes mention accuracy or confidence. I could not locate the developer-reply quote "within 99% accuracy of AMM", so it remains unverified. It may still exist, for example in Google Play review replies, which I could not read.

| claim | source URL | publisher | pub_date | accessed | conf | indep? |
|---|---|---|---|---|---|---|
| The App Store listing and release notes (through v2.54.0, Oct 26) contain no accuracy or confidence claim, and none of the visible developer replies mentions AMM or "99%" | https://apps.apple.com/us/app/sportsbox-3d-golf/id1578921026 | Apple App Store (vendor-authored listing) | rolling; v2.54.0 2026-10-26 | 2026-11-02 | M (only a partial review set is visible) | n (vendor listing) |
| A dev contractor validated 2D-to-3D lift accuracy against a Gears mocap ground truth and reported outdoor-footage accuracy problems in the prototype; no numbers published | https://litslink.com/case-studies/ai-golf-swing-analyzer | LITSLINK (vendor's contractor) | undated | 2026-11-02 | M (snippet) | n (vendor-affiliated) |
| Sportsbox's chief science officer Phil Cheetham co-founded AMM. AMM is the in-house reference, which makes it a conflict of interest, not independent validation | search snippet (cbinsights / bio) | various aggregators | n/a | 2026-11-02 | M | partial |
| Academic: golf-specific markerless accuracy is "still no clear answer" (Qualisys vs Simi markerless comparison on the golf swing) | https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2023.1272038/epub (and related 2023 comparison per snippet) | Frontiers / academic | 2023 | 2026-11-02 | M (snippet; older than 12 months) | y |
| Konstanz dissertation: smartphone joint kinematics vs marker-based system judged "feasible"; error magnitudes not in snippet | https://kops.uni-konstanz.de/entities/publication/9ae1120b-3e6a-486a-baa5-b91fb08f2ad1 | Univ. Konstanz | n/a | 2026-11-02 | L-M | y |
| Patent literature notes that hands at address and head/hand confusion are known failure modes of markerless golf tracking | https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9669260 | USPTO | older | 2026-11-02 | M | y |
| A German review says the data is "comparable to lab systems" but gives no error figures | https://www.ki-syndikat.de/tools/sportsbox-ai/ | KI-Syndikat (blog) | n/a | 2026-11-02 | L | y (opinion) |

**Implication:** markerless golf accuracy is academically unsettled, and Sportsbox publishes no per-metric error figures. A per-metric confidence UI therefore remains a credible gap, though the evidence is absence of evidence.

---

## V2. SAMI answers preset questions only; no free-form causal coaching yet
**Verdict: verified for the current shipped state. The "preset questions" wording comes from the vendor's own release notes, and there is no independent hands-on review. The tier that includes SAMI is unverified.**

| claim | source URL | publisher | pub_date | accessed | conf | indep? |
|---|---|---|---|---|---|---|
| v2.53.0 (Sep 23): SAMI launched, "can answer a list of preset questions and requests to provide general and personalized guidance" | https://apps.apple.com/us/app/sportsbox-3d-golf/id1578921026 | App Store (vendor-authored) | 2026-09-23 | 2026-11-02 | H (primary) | n |
| v2.54.0 (Oct 26): "Beta version of our AI golf expert, SAMI"; pick from preset questions on how to use Sportsbox, understanding the data and improving your swing; "More to come in this area very soon!" | same | same | 2026-10-26 | 2026-11-02 | H | n |
| Announced 2026-04-07 with the DeChambeau-led acquisition (eight-figure deal); built on Google Gemini; agentic features to roll out starting with AI Highlights for 3D Player and 3D Player Plus tiers on iOS | https://www.businesswire.com/news/home/20260407643695/en/ | Business Wire (vendor press release) | 2026-04-07 | 2026-11-02 | H for the claim being made | n |
| Independent restatement of Gemini, beta and tiers; SAMI "designed to act as a conversational AI coach" (intent, not tested) | https://www.geekwire.com/2026/golf-star-bryson-dechambeau-leads-acquisition-of-seattle-area-startup-sportsbox-ai/ | GeekWire | 2026-04-07 | 2026-11-02 | M (snippet; 403 on fetch) | y (but restates the PR) |
| DeChambeau's stated aspiration: "here's the five greatest deviators in your golf swing" and "tailor to what you need for that exact day"; the article does not say whether questions are free-form | https://www.golfmagic.com/news/bryson-dechambeau-google-ai-golf-training-tool | GolfMagic | 2026-04 | 2026-11-02 | H (fetched) | y |
| 3D Player costs $109.99/yr (sign-up page); a consumer tier at $15.99/mo or $110/yr (GeekWire) | https://3dgolf.sportsbox.ai/sign-up?plansType=players | Sportsbox | current | 2026-11-02 | M | n |

Caveats: the April 2026 tier statement concerns AI Highlights, not SAMI. Neither the App Store listing nor the press coverage says which tier gets SAMI. Expect this feature claim to go stale fast, because the vendor explicitly says "more to come very soon". Re-check by about Feb 2027.

---

## V3. No mainstream app explains fault-to-fault causal chains
**Verdict: disputed. "No app does this" is too strong. Several apps market root-cause or symptom-chain diagnosis, and TPI's public content explicitly maps physical limitations to swing faults. None of these claims is independently validated, though. The defensible version is: "no independently validated, transparent causal-chain explanation".**

| claim | source URL | publisher | pub_date | accessed | conf | indep? |
|---|---|---|---|---|---|---|
| Performance Golf (PG1 / SwingScan AI): "identifies your root swing flaw"; fixing the root flaw "automatically eliminates 3-4 of your 'symptom' swing flaws". This is a fault-to-fault chain claim (marketing) | https://pg1.performancegolf.com/pg1-pdp ; https://shop.performancegolf.com/pages/pg1-acc | Performance Golf | 2026 (current) | 2026-11-02 | L (marketing, snippet) | n |
| SwingCoach AI (iOS): each swing gives "one goal, one root cause, and one clear fix" and tracks persistent faults across sessions | https://apps.apple.com/app/id6760660742 | App Store (vendor-authored) | 2026 | 2026-11-02 | M (snippet) | n |
| SR.AI listing: "traces issues back to their root cause and prioritizes"; human coach review during beta | search snippet (apps.apple.com/app/id6741165328) | App Store | 2026 | 2026-11-02 | L-M | n |
| TPI: "any limitation in performing a full deep squat or full hip bend can force a player to early extend". This is a physical-limitation-to-fault mapping on the web, paired with a physical screen | https://cdn.site.mytpi.com/improve-my-game/swing-characteristics/early-extension | Titleist Performance Institute | undated | 2026-11-02 | M (snippet) | n/a (methodology source, not an app competitor) |
| Titleist: early extension is often caused by ankle mobility / squat pattern; fail the self-screen, then consult a professional | https://titleist.com/instruction/stop-early-extension | Titleist | undated | 2026-11-02 | M | n/a |
| Macro Golf Performance app: "Golf Mobility Self Screening" plus "Golf Drills - To fix your swing faults" (whether it links screen results to faults is unconfirmed) | https://apps.apple.com/us/app/id6450019231 | App Store (vendor) | n/a | 2026-11-02 | L | n |
| GolfForever: plans are built from a personal assessment; I found no swing-fault linkage | https://insidegolf.ca/read/8328-golfforever-introduces-new-mobile-app,-course-management-series-from-justin-leonard | Inside Golf | 2019 (stale) | 2026-11-02 | M | y |
| MyGolfSpy "I Hired an AI Golf Coach" tested a ChatGPT custom GPT on still photos (it flagged a bent lead arm causing inconsistent strikes; a local coach disagreed). It is not a causal-chain product, and it shows the risk of AI over-diagnosis | https://mygolfspy.com/news-opinion/first-look/i-hired-an-ai-golf-coach/ | MyGolfSpy | undated (pre-video GPT era, probably 2023-24, so stale) | 2026-11-02 | M (snippet; 403) | y |
| A Sportsbox App Store user review: "All of this data is meaningless unless you understand the cause and effect relationships". This points to unmet demand for causal explanation | https://apps.apple.com/us/app/sportsbox-3d-golf/id1578921026 | App Store user review | 2022-10-15 (stale) | 2026-11-02 | M | y (user) |

**Implication:** root-cause marketing is crowded (Performance Golf, SwingCoach AI, SR.AI). The mobility-to-fault link is established TPI doctrine, but it is not productised in a mainstream swing-analysis app that I could find. That is a weaker but more defensible differentiation claim.

---

## V4. The main user complaint is interpretation burden
**Verdict: unverified as "the main complaint"; directionally supported. A few independent voices confirm it, but I had no Reddit access and the Play reviews were unreadable, so I could not establish whether it is the main complaint versus others such as price, accuracy or setup.**

| claim | source URL | publisher | pub_date | accessed | conf | indep? |
|---|---|---|---|---|---|---|
| App Store user: "This is not beginner friendly info"; "tons of data"; beginners "should probably get a coach before you consider this app" | https://apps.apple.com/us/app/sportsbox-3d-golf/id1578921026 | App Store user review | 2022-10-15 (older than 12 months, stale) | 2026-11-02 | M | y |
| A GeekWire reporter found the data hard to parse at first, with a learning curve, and doubted mainstream golfers would adopt it alone | https://www.geekwire.com/2024/this-startup-helped-bryson-dechambeau-win-the-u-s-open-now-it-wants-to-improve-your-golf-swing/ | GeekWire | 2024 (stale) | 2026-11-02 | M (snippet) | y |
| KI-Syndikat: 20+ parameters, watchlists and trends; best for handicaps of about 8-25 and coaches who work deliberately with the data | https://www.ki-syndikat.de/tools/sportsbox-ai/ | KI-Syndikat | n/a | 2026-11-02 | L-M | y |
| Golf Digest "what an average golfer learned ... Mustard" (possible counter- or confirming voice; not read) | https://www.golfdigest.com/story/what-an-average-golfer-learned-about-his-swing-new-technology-mustard | Golf Digest | n/a | not read | n/a | y |

No sentiment within the last 12 months was retrieved. All confirming voices are from 2022-2024.

---

## New leads
- Golf Digest Mustard pieces: `artificial-intelligence-mustard-case-study-study` and `what-an-average-golfer-learned-about-his-swing-new-technology-mustard`. Possible independent hands-on evidence for V3 and V4. The case-study snippet says Mustard checks against "3D data models and motion capture from thousands of" swings.
- Performance Golf SwingScan AI ("47+ flaw patterns", root-flaw-to-symptom claims) is the strongest V3 counter-example; it needs a hands-on check.
- SwingCoach AI (id6760660742) and SR.AI (id6741165328) are new root-cause entrants.
- Macro Golf Performance (id6450019231): check whether its mobility self-screen links to fault drills, which would be V3 counter-evidence.
- Konstanz dissertation: get the error magnitudes for smartphone vs marker-based kinematics (V1 baseline).
- golf.com "Sportsbox AI exposed flaws" (Play Smart column): a hands-on view, not yet read.
- FlightScope Badger AI (MyGolfSpy "Can a launch monitor replace your coach"): an AI assistant comparable to SAMI.

## Looked for, not found
- Any Sportsbox validation study vs AMM, Gears or Vicon with numbers (queries: "Sportsbox AI 3D Golf accuracy validation study", "Sportsbox AI accuracy compared AMM 3D help", "Sportsbox '99%' accuracy AMM"). I found no help-center accuracy article or independent test from MyGolfSpy or Golf Digest.
- The "within 99% accuracy of AMM" developer reply was not located. It is not visible in the App Store reviews, and Google Play could not be read.
- Independent hands-on reviews of SAMI (query: "Sportsbox SAMI AI coach review"): only press and PR coverage. I found no Google Cloud customer story for Sportsbox and no YouTube write-ups.
- The subscription tier that includes SAMI: not stated anywhere I found.
- Reddit (r/golf, r/GolfSwing): blocked for this tool, so no data.
- Google Play reviews for Sportsbox and Mustard: the page fetch returned truncated or empty content.
- A GolfForever mobility-to-fault link: none found. I did not search the TPI consumer app specifically.

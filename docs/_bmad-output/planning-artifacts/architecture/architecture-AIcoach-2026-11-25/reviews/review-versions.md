# Review — technology versions and fit (reality check)

- **Spine:** `../ARCHITECTURE-SPINE.md` (Stack table; AD-3, 13, 15, 18, 20, 21, 22, 25)
- **Reviewer lens:** is every committed technology current, existing and fit, checked against live registries rather than training data
- **Date:** 2026-11-25
- **Method:** PyPI JSON API (`https://pypi.org/pypi/<pkg>/json`), `npm view`, Docker Hub tag API, GitHub releases API, nodejs.org `dist/index.json`, endoflife.date API, official docs pages, plus inspecting downloaded wheels and the `create-next-app` tarball (ELF `DT_NEEDED` parsed with a small Node script). The spine was not modified.

## Verdict

The stack is current. Every named version exists and is the latest or very close to it, as of today. Two fit problems need a spine change before scaffolding:

1. **OpenCV packaging conflict.** Both pose backends pull in non-headless `cv2` builds, which clash with the spine's `opencv-python-headless`.
2. **MediaPipe system libraries.** MediaPipe 1.x has a hard link-time dependency on EGL/GLES, so `python:3.13-slim` needs extra apt packages. This settles a Deferred `[ASSUMPTION]`.

A few rows also need small corrections: uv, TypeScript, shadcn, bcrypt and pydantic-ai.

## Summary table

| # | Item | Spine says | Status | Suggested spine correction |
| --- | --- | --- | --- | --- |
| 1 | Python | 3.13 | verified (advisory) | Optional: 3.14. 3.13 has been security-only since 2026-10-01. |
| 2 | uv | 0.12 | **changed** | `0.13` |
| 3 | FastAPI / Starlette / Uvicorn | 0.165 / 1.10 / 0.54 | verified | — (Range: see #3) |
| 4 | SQLAlchemy + asyncpg / Alembic / aiosqlite | 2.1 + 0.32 / 1.20 | verified | Write `sqlalchemy[asyncio]` (2.1 installs greenlet only through that extra) |
| 5 | Pydantic / pydantic-settings | 2.14 / 2.16 | verified | — |
| 6 | pydantic-ai (OpenRouter) | 2.74 | verified, **refine** | Name `pydantic-ai-slim[openrouter]` 2.74 and lock it |
| 7 | PyJWT / bcrypt | 2.15 / 5.0 | verified, **fit issue** | AD-20: reject passwords over 72 bytes (bcrypt 5 raises `ValueError`) |
| 8 | mediapipe | 1.2.3 | verified, **fit issue** | Tasks API only; apt `libegl1 libgles2`; `.task` model baked into the image |
| 9 | opencv-python-headless | 5.1.0 | **changed** | `opencv-contrib-python-headless` 5.1 + uv `exclude-dependencies` for the other cv2 builds |
| 10 | rtmlib + onnxruntime | 0.0.16 + 1.32 | verified | Bake model files into the image; weight licences are on the pre-launch list |
| 11 | numpy / scipy | 2.5 / 1.18 | verified | — |
| 12 | pytest | 9.2 | verified | — |
| 13 | Node.js | 26 LTS | verified | — |
| 14 | Next.js / React | 16.4 / 19.3 | verified | AD-25: `allowedDevOrigins` for the laptop's LAN IP in dev |
| 15 | TypeScript | "create-next-app 16.4 default" | **changed (make explicit)** | `5.x (create-next-app pins ^5)`; do not take TS 7 |
| 16 | Tailwind CSS | 4.3 | verified | — |
| 17 | shadcn/ui | "CLI latest at init" | **changed** | Pin `shadcn@4.23` and choose `--base` explicitly (Base UI is now the default) |
| 18 | TanStack Query / zod / openapi-typescript | 5.108 / 4.6 / 7.13 | verified | — |
| 19 | Vitest / Playwright | 5.1 / 1.65 | verified | — |
| 20 | PostgreSQL | 18 | verified | Pin `postgres:18`; `latest` is now 19 |
| 21 | Caddy | 2.11 | verified | AD-16/21: map Caddy's bare 413 to the error envelope in the frontend |
| 22 | Docker Engine + Compose | 29.x | verified | — |
| 23 | FFmpeg | distro / winget | unverifiable (not registry-checked) | — |

---

## Details and evidence

### 1. Python 3.13 — verified (advisory)

- endoflife.date: 3.13 latest is 3.13.18 (2026-10-25). Bugfix support **ended 2026-10-01**, and security support runs to 2029-10-31. 3.14 is the active bugfix line (support until 2027-10-01). 3.15 came out on 2026-10-09.
- Every native dependency has cp313 **and** cp314 wheels for manylinux x86_64 and win_amd64: onnxruntime, asyncpg, SQLAlchemy, numpy and scipy (all checked). onnxruntime 1.32.0 has **no cp315** wheels, so 3.15 is ruled out.
- mediapipe 1.2.3 ships `py3-none` wheels that list 3.10 to 3.14.
- **Suggestion:** 3.13 is acceptable for a 3-week MVP. 3.14 would put the project on a line that still gets bugfixes, at no compatibility cost. This is the author's choice and not a blocker.

### 2. uv 0.12 → 0.13 — changed

- PyPI `uv`: latest **0.13.10** (2026-11-24). GitHub `astral-sh/uv` latest release `0.13.10`. The 0.13 line has been shipping since at least 2026-11-03.
- **Correction:** Stack row `uv | 0.13`. The setup guide's "0.12+" still holds, but update it to match.

### 3. FastAPI 0.165 / Starlette 1.10 / Uvicorn 0.54 — verified

- PyPI: fastapi **0.165.0** (2026-11-18), starlette **1.10.0** (2026-10-24), uvicorn **0.54.0** (2026-09-25). All list Python 3.13.
- fastapi `requires_dist`: `starlette>=1.6.0`, `pydantic>=2.9.0`. Neither has an upper bound, so 1.10 is allowed.
- **Range requests (AD-21):** in the starlette 1.10.0 wheel, `starlette/responses.py` `FileResponse` sets `accept-ranges: bytes`, parses `range` and `if-range`, returns 206 through `_handle_single_range` / `_handle_multiple_ranges`, and returns `416` with `Content-Range: bytes */size` for unsatisfiable ranges (lines ~291–444). iOS `<video>` playback is covered **if the media endpoints return `FileResponse`**, not a `StreamingResponse`.
- **Suggestion (wording only):** AD-21 could say "served with Starlette `FileResponse`" so an implementer doesn't hand-roll streaming.

### 4. SQLAlchemy 2.1 + asyncpg 0.32 + aiosqlite, Alembic 1.20 — verified

- PyPI: sqlalchemy **2.1.9** (2026-11-16), asyncpg **0.32.0** (2026-10-06, cp313 manylinux x86_64 + win_amd64 wheels present), aiosqlite **0.22.1** (2025-12-23, py3-none-any, MIT), alembic **1.20.1** (2026-10-22, `SQLAlchemy>=2.0`).
- sqlalchemy 2.1 `requires_dist`: the base install needs only `typing-extensions`. `greenlet>=1` comes **only** with `extra == "asyncio"`, and the `postgresql-asyncpg` and `aiosqlite` extras pull in `sqlalchemy[asyncio]`.
- **Correction:** the Stack row should name `sqlalchemy[asyncio]` (the setup guide already does). Without that extra, the async engine fails at runtime with a missing-greenlet error.
- Fit note (not a version issue): AD-8 relies on `SELECT … FOR UPDATE`. On SQLite (the aiosqlite test path), SQLAlchemy leaves out `FOR UPDATE`, so the 50-clip race is tested only on Postgres. Add one test against Postgres, or accept the gap.

### 5. Pydantic 2.14 / pydantic-settings 2.16 — verified

- PyPI: pydantic **2.14.4** (2026-11-19), pydantic-settings **2.16.3** (2026-11-13). pydantic-ai-slim needs `pydantic>=2.12`, which this satisfies.

### 6. pydantic-ai 2.74 with an OpenRouter provider — verified, refine

- PyPI: pydantic-ai / pydantic-ai-slim **2.74.0**, uploaded **2026-11-25 (today)**. Releases come almost every day (2.71 on 11-19, 2.73 on 11-24). There is also a parallel 1.107.x maintenance line.
- `pydantic-ai-slim` has an `openrouter` extra (`openai<4,>=3.50.0`).
- The wheel contains `pydantic_ai/models/openrouter.py` (`class OpenRouterModel(OpenAIChatModel)`, `OpenRouterModelSettings`, `OpenRouterUsageConfig{include: bool}`) and `pydantic_ai/providers/openrouter.py` (`class OpenRouterProvider`). The provider reads `os.getenv('OPENROUTER_API_KEY')` and **raises an error if the key is missing**.
- Cost: `pydantic_ai/usage.py` uses `genai_prices` and a gateway-reported cost, and OpenRouter usage accounting can be turned on through `OpenRouterUsageConfig`. That supports "tokens and cost logged per call" (AD-18, OQ2).
- **Correction:** Stack row → `pydantic-ai-slim[openrouter] | 2.74` (the full `pydantic-ai` installs every provider SDK). Lock it with `uv.lock`, because 2.74.0 is hours old.
- AD-23 note: build the OpenRouter adapter only when the key is set. Building `OpenRouterProvider()` without a key raises an error, which would break "never fails because a key is missing".

### 7. PyJWT 2.15 / bcrypt 5.0 — verified, fit issue

- PyPI: pyjwt **2.15.1** (2026-09-28), bcrypt **5.0.0** (2025-09-25, cp313 wheels, Apache-2.0).
- bcrypt 5.0.0 changelog (PyPI description): "Passing `hashpw` a password longer than 72 bytes now raises a `ValueError`. Previously the password was silently truncated."
- **Correction (AD-20):** add "passwords are limited to 72 bytes (UTF-8). A longer password is a 422 `password_too_long`, checked before hashing." Without this, a long passphrase is an uncaught 500.

### 8. mediapipe 1.2.3 — verified, fit issue (settles a Deferred assumption)

- PyPI: mediapipe **1.2.3** (2026-11-11). Licence "Apache 2.0" (with LICENSE and NOTICE). Classifiers cover Python 3.10–3.14 and OS MacOS, Windows and POSIX Linux. The wheels are `py3-none-manylinux_2_28_x86_64` (43 MB), `py3-none-win_amd64`, win_arm64, macOS arm64 and linux aarch64. They load `libmediapipe.so` through ctypes and so don't depend on the CPython ABI, which means they work on 3.13.
- **PoseLandmarker exists:** the wheel contains `mediapipe/tasks/python/vision/pose_landmarker.py` (`PoseLandmarkerOptions`, `num_poses`, `detect_for_video`).
- **The legacy `mp.solutions.pose` is gone:** the wheel has no `solutions/` package, and `mediapipe/__init__.py` imports only `mediapipe.tasks.python`. Many tutorials still use `mp.solutions.pose`, so the adapter must use the Tasks API.
- **The model is not in the wheel:** no `*.task` file is bundled. The `pose_landmarker_{lite,full,heavy}.task` file has to be downloaded once and baked into the image or `DATA_DIR`. That's also needed for "pose never leaves the laptop" and offline examiner runs.
- **System libraries:** the ELF dynamic section of `mediapipe/tasks/c/libmediapipe.so` (linux x86_64) lists `DT_NEEDED: libEGL.so.1, libGLESv2.so.2, libm.so.6, libpthread.so.0, libdl.so.2, librt.so.1, libc.so.6`. These are hard link-time dependencies, so `import mediapipe` fails in `python:3.13-slim` unless **`libegl1` and `libgles2`** are installed with apt.
- Python dependencies: `opencv-contrib-python` (non-headless, see #9), `matplotlib`, `sounddevice~=0.5` (imported lazily in a `try` in `audio_record.py`, so PortAudio isn't needed for pose), `absl-py`, `flatbuffers`, `numpy`.
- **Corrections:**
  - Move the Deferred row "`[ASSUMPTION]` the mediapipe system libraries in `python:3.13-slim`" to settled: the backend Dockerfile installs `ffmpeg libegl1 libgles2`.
  - AD-13 adds: "the MediaPipe adapter uses the Tasks `PoseLandmarker` in `VIDEO` mode; the `.task` model file is vendored at build time, never fetched at runtime."
  - The setup guide comment "(+ libgl1/libegl1 if mediapipe needs them)" should read `libegl1 libgles2`. `libgl1` is needed only if a non-headless OpenCV gets in (see #9).

### 9. OpenCV — changed (packaging conflict)

- PyPI: opencv-python-headless **5.1.0.95** (2026-11-17). opencv-contrib-python, opencv-contrib-python-headless and opencv-python are all 5.1.0.95. 5.x is a new major line (5.0.0.93 in 2026-07, and 4.14.0.94 is still being released).
- **Conflict:** `mediapipe` requires `opencv-contrib-python`. `rtmlib` requires **both** `opencv-contrib-python` and `opencv-python`. The spine names `opencv-python-headless`. All of these install the same top-level `cv2` package, so with two or three of them in one environment the files overwrite each other, and uninstalling one breaks `cv2`. A non-headless build also needs `libGL.so.1`/`libglib2.0` in a slim image.
- **Correction:**
  - The Stack row becomes `opencv-contrib-python-headless | 5.1`.
  - Add to `backend/pyproject.toml`:

    ```toml
    [tool.uv]
    exclude-dependencies = ["opencv-python", "opencv-contrib-python", "opencv-python-headless"]
    ```

    uv's settings reference documents `exclude-dependencies` as "prevent it from being installed, even if it's requested by transitive dependencies".
  - AD-15's "OpenCV (headless)" then holds for both backends.
- **Spike item:** rtmlib 0.0.16 (2026-08-04) and mediapipe declare no OpenCV version bound. Confirm they work on OpenCV 5.1; if not, pin `opencv-contrib-python-headless==4.14.*`.

### 10. rtmlib 0.0.16 + onnxruntime 1.32 — verified

- PyPI: rtmlib **0.0.16** (2026-08-04) is `py3-none-any`, `Requires-Python >=3.10`, licence "Apache License 2.0" (LICENSE file in the wheel). Its dependencies are `numpy, onnxruntime, opencv-contrib-python, opencv-python, tqdm` (the cv2 conflict is in #9).
- PyPI: onnxruntime **1.32.0** (2026-11-13), MIT, `>=3.11`, with cp313 wheels for manylinux_2_28 x86_64 and win_amd64.
- rtmlib downloads its ONNX models (YOLOX detector + RTMPose `body7`) **at runtime** from `download.openmmlab.com` (URLs in `rtmlib/tools/solution/body.py`). For offline or examiner runs, vendor them at image build time, the same as the MediaPipe `.task` file.
- Unverified: the licence of the RTMPose `body7` **weights**, which follows from the licences of their training datasets. This doesn't matter for the MVP. Add it to the same "remove or check before a paid launch" list as SwingNet in AD-14.
- Fit: rtmlib is a 0.0.x single-maintainer library. AD-13's port keeps that risk contained.

### 11. numpy 2.5 / scipy 1.18 — verified

- PyPI: numpy **2.5.5** (2026-11-15, `>=3.12`), scipy **1.18.1** (2026-08-21, `>=3.12`). Both have cp313 wheels. opencv 5.1 needs `numpy>=2`, which this satisfies.

### 12. pytest 9.2 — verified

- PyPI: pytest **9.2.0** (2026-10-27).

### 13. Node.js 26 LTS — verified

- nodejs.org `dist/index.json`: `v26.13.1` (2026-11-10), `lts: "Lithium"`. endoflife.date: Node 26 became LTS on 2026-10-28, EOL 2029-04-30. Docker tags `node:26-slim`, `node:26-alpine` and `node:26-trixie-slim` exist (updated 2026-11-24).
- `next@16.4.x` `engines.node: ">=20.9.0"`. Vitest 5.1.2 engines `^22.12.0 || ^24.0.0 || >=26.0.0`. Playwright 1.65.1 `>=20`. tailwindcss 4.3.5 `>=20`. Everything is compatible with 26.

### 14. Next.js 16.4 / React 19.3 — verified, plus one dev-mode fit issue

- npm: next **16.4.6**, react / react-dom **19.3.1**. Next's peer range is `react ^18.2.0 || ^19.0.0`.
- `output: 'standalone'`: still documented and supported (nextjs.org/docs/app/api-reference/config/next-config-js/output, lastUpdated 2026-11-18). The Dockerfile must still `cp -r public .next/standalone/ && cp -r .next/static .next/standalone/.next/` and run with `HOSTNAME=0.0.0.0`. Standalone also copies `.env`/`.env.production` into the output, so keep `.env` out of the frontend build context.
- **AD-25 dev over the LAN:** Next "blocks cross-origin requests to dev-only assets and endpoints during development by default" and allows only `localhost` and the hostname the server started with (docs page `allowedDevOrigins`, lastUpdated 2026-08-26). A phone that opens `http://<laptop-ip>:8080` while the frontend runs `npm run dev` behind Caddy will have its HMR and dev assets blocked.
- **Correction:** in AD-25 or the setup guide, add `allowedDevOrigins: [process.env.LAN_HOST]` (or the laptop's IP) to `next.config` for dev. The Compose demo (production build) is not affected.

### 15. TypeScript — changed (make it explicit)

- npm: `typescript` dist-tag `latest` = **7.0.2** (the native port). `next` = 7.1.0-dev.
- The `create-next-app@16.4.6` tarball (`dist/index.js`) writes `devDependencies: { typescript: "^5", "@types/node": "^20", "@types/react": "^19", "@types/react-dom": "^19" }`. **The default is TypeScript 5.x, not 7.**
- `openapi-typescript@7.13.0` `peerDependencies: { typescript: "^5.x" }`. Upgrading to TS 7 would break the peer range of the AD-21 type generator.
- **Correction:** Stack row → `TypeScript | 5.x (create-next-app 16.4 pins ^5; stay on 5 — openapi-typescript 7.13 peers ^5.x)`. Optionally bump `@types/node` to match Node 26.

### 16. Tailwind CSS 4.3 with `@theme` tokens — verified

- npm: tailwindcss **4.3.5**, @tailwindcss/postcss 4.3.5, @tailwindcss/turbopack 4.3.5.
- tailwindcss.com/docs/theme shows v4.3: theme variables are "defined using the `@theme` directive"; `@theme inline` is for variables that reference other variables; there are no examples with `tailwind.config.js`.
- The `create-next-app@16.4.6` template `app/globals.css` uses `@import "tailwindcss";` + `@theme inline { --color-background: var(--background); … }`. It pins `tailwindcss: "4.3.3"`, plus `@tailwindcss/turbopack` when Turbopack is the bundler and `@tailwindcss/postcss` otherwise.
- AD-22's "Tailwind v4 `@theme` tokens copied from DESIGN.md" is current. Use `@theme inline` where tokens point at `:root` variables (which is shadcn's pattern too).

### 17. shadcn/ui — changed

- npm: `shadcn` CLI **4.23.0**.
- ui.shadcn.com/docs/tailwind-v4: "Only new projects start with Tailwind v4 and React 19"; the `default` style is deprecated in favour of `new-york`; `tailwindcss-animate` is replaced by `tw-animate-css` (npm 1.4.0); tokens are `:root`/`.dark` variables (OKLCH) mapped through `@theme inline`.
- The docs don't name Next.js 16 explicitly, but CLI v4 (March 2026) scaffolds a Next template (`shadcn init -t next`), and the peer ranges allow React 19.3 (`@base-ui/react@1.9.0` peers `react ^17 || ^18 || ^19`; `@radix-ui/react-dialog@1.3.1` peers `^19.0`).
- **Since July 2026, Base UI is the default primitive library** (ui.shadcn.com/docs/changelog/2026-07-base-ui-default). Radix needs `-b radix`, and React Aria is a third option. "CLI latest at init" therefore decides the primitive library implicitly.
- **Correction:** Stack row → `shadcn CLI 4.23 (pinned: npx shadcn@4.23.0 init --base <base-ui|radix>)`, and record the choice in `components.json`. AD-22 can say "primitives: shadcn/ui on Base UI (CLI default)" or Radix, whichever is chosen.

### 18. TanStack Query 5.108 / zod 4.6 / openapi-typescript 7.13 — verified

- npm: @tanstack/react-query **5.108.4** (peer `react ^18 || ^19`), zod **4.6.7**, openapi-typescript **7.13.0** (latest; last published 2026-02-11).
- openapi-typescript describes itself as "Convert OpenAPI 3.0 & 3.1 schemas to TypeScript".
- In the FastAPI 0.165.0 wheel, `fastapi/applications.py` sets `openapi_version` to `"3.1.0"` by default ("FastAPI will generate OpenAPI version 3.1.0"). The two are compatible.
- Note: FastAPI's default `separate_input_output_schemas=True` produces `Foo-Input` / `Foo-Output` component names when request and response models differ. This is expected and fine for generated types. openapi-typescript hasn't had a release in 9 months, which is acceptable but worth watching.

### 19. Vitest 5.1 / Playwright 1.65 — verified

- npm: vitest **5.1.2** (peer `vite ^6 || ^7 || ^8`, engines include Node >=26), @playwright/test **1.65.1** (Node >=20). Next 16.4 lists `@playwright/test ^1.51.1` as an optional peer.

### 20. PostgreSQL 18 — verified

- Docker Hub `library/postgres` tag `18` exists (last updated 2026-11-24). Tags `18.7`, `18-trixie` and so on also exist. endoflife.date: 18 latest is 18.7 (2026-11-09), EOL 2030-11-14.
- **`latest`, `19` and `19.0` now exist**, so the image must be pinned to `postgres:18`. The spine and setup guide already do this.
- docker-library docs: from 18 on, `PGDATA=/var/lib/postgresql/18/docker` and the `VOLUME` is `/var/lib/postgresql`, so mounts must target `/var/lib/postgresql`. The setup guide already does this correctly.

### 21. Caddy 2.11 `request_body max_size` — verified

- GitHub `caddyserver/caddy` latest release **v2.11.9** (2026-11-05). Docker Hub `caddy:2.11` and `caddy:2.11-alpine` exist. `caddy:2.12` returns 404 (not released).
- caddyserver.com/docs/caddyfile/directives/request_body gives the syntax `request_body [<matcher>] { max_size <value>  set <body_content> }`. `max_size` accepts go-humanize sizes. If `Content-Length` is over the limit, "the request is rejected with HTTP status `413` right away". `read_timeout`/`write_timeout` were removed (use `timeouts`).
- The setup guide's Caddyfile (`handle /api/* { request_body { max_size 300MB } reverse_proxy … }`) is valid.
- Fit notes:
  - go-humanize `300MB` = 300,000,000 bytes, while `300MiB` = 314,572,800. The backend's limit must use the same unit, or the two layers disagree near the edge (AD-16, "enforced by Caddy and by the backend").
  - Caddy's 413 is a bare response, **not** the `{"error":{"code",…}}` envelope (AD-21). The frontend upload client must map a raw 413 to the `file_too_large` code. Alternatively, set Caddy's limit slightly above the backend's so the backend's envelope normally wins.

### 22. Docker Engine 29.x + Compose — verified

- GitHub `moby/moby`: `docker-v29.10.1` (2026-11-24). `docker/compose` latest `v5.8.0` (2026-11-17). The spine doesn't pin Compose, and that's fine.

### 23. FFmpeg — unverifiable here

- Not checked against a registry. The Debian package version depends on the `python:3.13-slim` base (now trixie: `python:3.13-slim-trixie` exists), and the winget package is `Gyan.FFmpeg`. The H.264 `playback.mp4` transcode (libx264) is in Debian's `ffmpeg` package. Confirm it in the backend-image spike.

---

## Corrections to the spine, in priority order

1. **Stack + AD-15:** `opencv-python-headless` → `opencv-contrib-python-headless 5.1`, plus `[tool.uv] exclude-dependencies = ["opencv-python","opencv-contrib-python","opencv-python-headless"]`, because mediapipe and rtmlib pull in clashing non-headless `cv2` builds.
2. **AD-13 + Deferred:** the mediapipe assumption is settled. `libmediapipe.so` needs `libEGL.so.1` + `libGLESv2.so.2`, so apt-install `libegl1 libgles2`. mediapipe 1.x is Tasks-API only (no `mp.solutions`). Vendor the `.task` and RTMPose ONNX models at build time.
3. **Stack:** uv `0.12` → `0.13` (0.13.10 latest).
4. **Stack:** TypeScript → `5.x` explicitly. create-next-app 16.4.6 pins `^5`, npm `latest` is 7.0.2, and openapi-typescript 7.13 peers `^5.x`.
5. **Stack + AD-22:** shadcn pinned to `4.23` with an explicit `--base`. Base UI has been the default since July 2026, not Radix.
6. **AD-20:** limit passwords to 72 bytes, because bcrypt 5.0 raises `ValueError` instead of truncating.
7. **Stack + AD-18/23:** `pydantic-ai-slim[openrouter] 2.74` (released today, so lock it). Build `OpenRouterProvider` only when the key is set, because it raises an error without one.
8. **AD-25 / AD-16:** Next dev behind Caddy over the LAN needs `allowedDevOrigins` for the laptop's IP. Map Caddy's bare 413 into the error envelope, and use the same MB/MiB unit in both layers.

Advisory (no change required): Python 3.13 is security-only since 2026-10-01, and 3.14 is fully supported by every dependency. AD-21 could name `FileResponse` for Range support. AD-8's `FOR UPDATE` isn't exercised on SQLite.

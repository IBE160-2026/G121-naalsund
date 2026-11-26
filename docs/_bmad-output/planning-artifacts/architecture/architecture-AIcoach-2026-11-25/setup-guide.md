---
title: AIcoach — Setup Guide (MVP)
status: final
created: 2026-11-25
updated: 2026-11-25
companion_of: ARCHITECTURE-SPINE.md
sources:
  - ../../../../../.docs/planning-artifacts/architecture/technology.md
---

# AIcoach — Setup Guide (MVP)

How to set up, run and configure AIcoach for the MVP. This guide adapts the reference stack in `.docs/planning-artifacts/architecture/technology.md`, which describes the Pytagoras website v2, to AIcoach's scope: one player-facing app running on one laptop and reached over local Wi-Fi, with zero paid accounts. The binding decisions live in `ARCHITECTURE-SPINE.md`, and the `AD-n` references below point there.

## 1. What we keep from technology.md, and what we drop

| technology.md | AIcoach MVP | Why |
| --- | --- | --- |
| FastAPI + Uvicorn, uv, SQLAlchemy 2 async + asyncpg, Alembic, Pydantic 2 | **Keep** | Python is needed for pose estimation anyway (AD-1, AD-13). |
| Next.js App Router, React, Tailwind v4, shadcn/ui, TanStack Query, zod | **Keep** (Next 16.4, React 19.3) | Matches the UX spec; shadcn is restyled with `DESIGN.md` tokens (AD-22). |
| Caddy as the only public entry, single origin, `/api/*` → backend | **Keep**, plain HTTP on port 8080 on the LAN | The phone reaches the laptop over Wi-Fi (AD-3). |
| Postgres 16 (Docker locally, Supabase in production) | **Postgres 18 in Docker only** | Local only (NFR-2). |
| Supabase Storage (private buckets) | **Local disk behind a `FileStore` interface** | Clips must not leave the laptop (NFR-2). Supabase can be added later (AD-4). |
| Local email/password, bcrypt, HS256 JWT | **Keep**, with the JWT in an httpOnly cookie | `<video>` and `<img>` requests need the cookie (AD-20). |
| pydantic-ai → OpenRouter, mock without a key | **Keep**, with a grounding check on every output | FR-14, FR-15, FR-20 (AD-18, AD-19). |
| Zero-config / mock fallback | **Keep, as a hard rule** | The examiner runs the app with no keys (NFR-4, AD-23). |
| `FEATURE_*` flags in two layers (backend + `NEXT_PUBLIC_*`) | **Backend flags only, read by the frontend at runtime from `/api/config`** | Cutting the chat needs no rebuild (AD-23). |
| pytest + aiosqlite, Vitest, Playwright | **Keep** | NFR-3. |
| Docker Compose locally | **Keep**: `docker compose up` is the canonical run | UJ-5, examiner run (AD-25). |
| Redis, Railway, Cloudflare, R2 backup, watchdog | **Drop** | No public hosting in the MVP. |
| Stripe, Vipps, Resend, Fiken, `COMPANY_*` | **Drop** | No payments, email or invoices (PRD §8.2). |
| Content service, capability tokens, JWKS (§6.8) | **Drop** | One app, one database. |
| Cutover / migration (§6.10) | **Drop** | Nothing to migrate. |
| Rule of thumb: never `rollback()` on the shared session; `ON CONFLICT DO NOTHING` | **Keep** | Consistency conventions. |

## 2. Tools to install on the laptop

| Tool | Version | Windows install | Used for |
| --- | --- | --- | --- |
| Docker Desktop | Engine 29.x | docker.com | `docker compose up` (demo and examiner) and the dev database and proxy |
| uv | 0.13+ | `winget install astral-sh.uv` (or `uv self update`) | Python 3.14 and dependencies (`uv` installs Python itself) |
| Node.js | 26 LTS | `winget install OpenJS.NodeJS.LTS` | the frontend in dev |
| FFmpeg | any recent | `winget install Gyan.FFmpeg` | `ffprobe` and `ffmpeg` in dev on the host (the backend image has its own) |
| Git | any | — | repo |

No accounts are needed. **OpenRouter** is optional: without a key the app runs in mock mode.

## 3. Environment variables (`.env`)

`.env` is git-ignored and `.env.example` is committed. In the legend, 🔴 means secret, ⚪ optional (the app works without it) and 🟡 plain config.

### 3.1 Core

| Variable | Type | Default | Notes |
| --- | --- | --- | --- |
| `APP_ENV` | 🟡 | `local` | `local` (dev) or `demo` (Compose, examiner). `docker-compose.yml` sets `APP_ENV=demo` explicitly for the backend. "Seeding" of the sample clips is a startup check only: it creates no accounts and stores no clips, because no clip may be stored without the library consent (FR-18). |
| `DATABASE_URL` | 🔴 | `postgresql+asyncpg://aicoach:aicoach@db:5432/aicoach` | In dev on the host, use `localhost:5432`. |
| `POSTGRES_USER` / `POSTGRES_PASSWORD` / `POSTGRES_DB` | 🔴 | `aicoach` / `aicoach` / `aicoach` | Used by the `db` service. The defaults are fine locally because the database port is not exposed to the LAN. |
| `JWT_SECRET` | 🔴⚪ | empty | If empty, the app generates one on first start and stores it in `DATA_DIR/system/` (AD-20). Never reuse a Pytagoras key. |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | 🟡 | `43200` | 30 days, as in technology.md. |
| `DATA_DIR` | 🟡 | `/data` (container) | Clips, playback copies, key frames and the generated secret. In dev, point it **outside the repo**, for example `D:/aicoach-data` (AD-4). |
| `HTTP_PORT` | 🟡 | `8080` | The port Caddy listens on, on all interfaces. |

### 3.2 Analysis

| Variable | Type | Default | Notes |
| --- | --- | --- | --- |
| `POSE_BACKEND` | 🟡 | set after the week-1 spike | `mediapipe` or `rtmpose` (AD-13). |
| `MODELS_DIR` | 🟡 | `/app/models` (container) | Pose model files listed in `models/MANIFEST.yaml`. They are fetched when the image is built and never downloaded at runtime (AD-13). In dev: `backend/models`, filled by `uv run python -m app.fetch_models`. |
| `EVENT_DETECTOR` | 🟡 | `wrist` | `swingnet` only as a fallback, off by default (AD-14, NFR-7). |
| `RULES_PATH` | 🟡 | `config/rules.yaml` | The rule table (AD-11). |
| `MAX_UPLOAD_MB` | 🟡 | `300` | Must match the Caddy `request_body` limit (AD-16). |
| `MAX_CLIP_SECONDS` / `MAX_CLIPS_PER_PLAYER` | 🟡 | `15` / `50` | FR-5, FR-19; served to the frontend by `/api/config`. |
| `ANALYSIS_TIMEOUT_SECONDS` | 🟡 | `600` | After this the analysis is marked `failed` (AD-5). |
| `SLOW_ANALYSIS_SECONDS` | 🟡 | `180` | When the UI shows "taking longer than it should" (EXPERIENCE). |
| `EVAL_DATA_DIR` | 🟡⚪ | empty | Folder holding the tuning and evaluation clips, outside Git (AD-24). |

### 3.3 Language model (optional)

| Variable | Type | Default | Notes |
| --- | --- | --- | --- |
| `LLM_MODE` | 🟡 | `auto` | `auto` uses OpenRouter if a key is set and mock otherwise; `mock` forces mock mode. |
| `OPENROUTER_API_KEY` | 🔴⚪ | empty | Get one at openrouter.ai/keys. Empty means mock mode (FR-15). |
| `OPENROUTER_MODEL` | 🟡 | chosen at P2 start | `[ASSUMPTION]` a small, cheap model. Cost is logged for every call (OQ2). |
| `LLM_TIMEOUT_SECONDS` | 🟡 | `20` | On timeout, the explanation uses the template and the chat returns 503 (AD-6, AD-23). |
| `AI_USD_NOK` | 🟡 | `10.5` | Converts the cost log to NOK (from technology.md). |

### 3.4 Features and dev

| Variable | Type | Default | Notes |
| --- | --- | --- | --- |
| `FEATURE_CHAT` | 🟡 | `true` | Set to `false` at the 2026-12-08 cut: the endpoints return 404 and the UI hides the composer (AD-23). |
| `FEATURE_HISTORY` | 🟡 | `false` | P3 stretch (FR-16, FR-17). |
| `BACKEND_UPSTREAM` / `FRONTEND_UPSTREAM` | 🟡 | `backend:8000` / `frontend:3000` | In dev: `host.docker.internal:8000` / `host.docker.internal:3000` (AD-25). |
| `DEV_LAN_ORIGIN` | 🟡 | empty | Dev only: the laptop's Wi-Fi IP (for example `192.168.1.23`). `next.config.ts` adds it to `allowedDevOrigins`, so `npm run dev` accepts a phone. Not needed for `docker compose up`. |

There are no `NEXT_PUBLIC_*` variables. The frontend gets everything it needs from `GET /api/config` while it runs.

## 4. First-time scaffold (once, in `G121-naalsund/`)

```powershell
# Backend: app + engine as a uv workspace (AD-1)
uv init backend --app --python 3.14
uv init backend/engine --package --name aicoach-engine
cd backend
uv add fastapi "uvicorn[standard]" "sqlalchemy[asyncio]" asyncpg alembic pydantic-settings pyjwt bcrypt python-multipart pyyaml "pydantic-ai-slim[openrouter]"
uv add --package aicoach-engine numpy scipy opencv-contrib-python-headless pydantic pyyaml
uv add --package aicoach-engine mediapipe        # and/or: rtmlib onnxruntime (spike)
uv add --dev pytest pytest-asyncio httpx aiosqlite import-linter
cd ..
```

In `backend/pyproject.toml`, keep exactly one `cv2` package. mediapipe and rtmlib pull in other OpenCV builds that overwrite it:

```toml
[tool.uv]
exclude-dependencies = ["opencv-python", "opencv-contrib-python", "opencv-python-headless"]
```

```powershell
# Frontend (AD-22). create-next-app 16.4 pins TypeScript ^5; keep 5.x (openapi-typescript 7 needs it)
npx create-next-app@16 frontend --ts --tailwind --eslint --app --src-dir --use-npm --import-alias "@/*"
cd frontend
npx shadcn@4.23.0 init      # choose the base (Base UI is the default, or Radix) explicitly; it is recorded in components.json
npm i @tanstack/react-query zod
npm i -D openapi-typescript vitest @playwright/test
cd ..
```

**API types (AD-21):** FastAPI uses `openapi_url="/api/openapi.json"` and `docs_url="/api/docs"`. Running `uv run python -m app.export_openapi` writes `frontend/openapi.json`, which is committed. `npm run gen:api` (= `openapi-typescript openapi.json -o src/shared/api/schema.d.ts`) generates the types from it, so no backend has to be running.

**`next.config.ts`:** set `output: "standalone"`, and in dev `allowedDevOrigins: process.env.DEV_LAN_ORIGIN ? [process.env.DEV_LAN_ORIGIN] : []`.

`.gitignore` must include:
- `.env` and `/data/`
- `*.mp4` and `*.mov`, apart from `samples/` (`!samples/*.mp4` if the samples are mp4)
- `backend/models/*` apart from `!backend/models/MANIFEST.yaml`
- `node_modules/` and `.venv/` This closes the open item "add the upload folder to .gitignore when the stack is chosen".

## 5. Compose and Caddy (seed)

`docker-compose.yml`, in outline:

```yaml
services:
  db:
    image: postgres:18
    environment: [POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB]
    volumes: [pgdata:/var/lib/postgresql]      # Postgres 18 image: mount the parent dir
    ports: ["127.0.0.1:5432:5432"]             # host only, never the LAN
    healthcheck: { test: ["CMD-SHELL", "pg_isready -U $${POSTGRES_USER}"], interval: 5s }
  backend:
    build: ./backend                            # python:3.14-slim + apt ffmpeg libegl1 libgles2; fetches model files at build (AD-13)
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000   # exactly one process, never --workers (AD-5)
    env_file: .env
    volumes: [data:/data, ./config:/app/config:ro, ./samples:/app/samples:ro, ./eval:/app/eval:ro]
    depends_on: { db: { condition: service_healthy } }
  frontend:
    build: ./frontend                           # node:26-alpine, next build, standalone
  proxy:
    image: caddy:2.11
    ports: ["0.0.0.0:${HTTP_PORT:-8080}:8080"]
    volumes: [./Caddyfile:/etc/caddy/Caddyfile:ro]
    environment: [BACKEND_UPSTREAM, FRONTEND_UPSTREAM]
volumes: { pgdata: {}, data: {} }
```

`Caddyfile`:

```caddyfile
:8080 {
	handle /api/* {
		request_body {
			max_size 300MB
		}
		reverse_proxy {$BACKEND_UPSTREAM:backend:8000}
	}
	handle {
		reverse_proxy {$FRONTEND_UPSTREAM:frontend:3000}
	}
}
```

`300MB` in Caddy means 300,000,000 bytes, and the backend uses the same decimal unit. Caddy's 413 has no JSON body, so the frontend turns it into `upload_too_large` (AD-16).

## 6. Running

### 6.1 Demo / examiner (UJ-5, the README path)

```powershell
copy .env.example .env      # no edits needed: mock mode, generated JWT secret
docker compose up --build
```

Open `http://localhost:8080`, create an account (tick the box), choose "New swing" and drop a clip from `samples/`. You get a complete result in mock mode.

### 6.2 Dev (hot reload)

```powershell
# .env: DATABASE_URL=...@localhost:5432/..., DATA_DIR=D:/aicoach-data,
#       BACKEND_UPSTREAM=host.docker.internal:8000, FRONTEND_UPSTREAM=host.docker.internal:3000
docker compose up db proxy
cd backend;  uv run alembic upgrade head; uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
cd frontend; npm run dev
```

Always browse through `http://localhost:8080`, not port 3000, so that the single origin and the cookie work (AD-3).

### 6.3 Phone on the same Wi-Fi (NFR-2)

1. Find the laptop's Wi-Fi IPv4 address: `ipconfig` → "Wireless LAN adapter Wi-Fi" → IPv4 Address (for example `192.168.1.23`).
2. Allow the port through Windows Firewall, once, in an administrator PowerShell:
   `New-NetFirewallRule -DisplayName "AIcoach 8080" -Direction Inbound -LocalPort 8080 -Protocol TCP -Action Allow -Profile Private`
3. Make sure the Wi-Fi network is set to **Private** in Windows (Settings → Network → Wi-Fi → network profile).
4. On the phone, open `http://192.168.1.23:8080`.
5. Dev only (`npm run dev`): set `DEV_LAN_ORIGIN=192.168.1.23` in `.env`, or Next blocks the phone's dev assets.

Guest or public Wi-Fi often blocks traffic between devices ("client isolation"). If the phone can't reach the laptop, use a phone hotspot with the laptop connected to it.

## 7. Engine and evaluation (no web app)

```powershell
# Quick loop on the host (dev)
cd backend
uv run aicoach-engine analyse ..\samples\ee-01.mp4 --out D:\tmp\ee-01   # prints the AnalysisResult JSON (FR-6)
uv run pytest                                                          # add -m pg for the Postgres-only tests

# Numbers that count: in the backend container, so they match the demo (AD-24)
docker compose run --rm -v "${env:EVAL_DATA_DIR}:/eval-data:ro" -e EVAL_DATA_DIR=/eval-data backend aicoach-engine eval --split tuning
docker compose run --rm -v "${env:EVAL_DATA_DIR}:/eval-data:ro" -e EVAL_DATA_DIR=/eval-data backend aicoach-engine eval --split evaluation   # never for tuning
docker compose run --rm backend aicoach-engine bench /app/samples/ee-01.mp4 --runs 5                                                       # NFR-1 median
```

The labels live in `eval/labels.yaml` (committed). Event frames are 0-based indices into the full clip at its own frame rate (AD-14). The clips live in `EVAL_DATA_DIR`, which is not committed. **Back that folder up**, for example to a USB drive or a private cloud folder: losing the test set before 12-15 means losing SM-1 to SM-5.

## 8. Week-1 spike checklist (sets `POSE_BACKEND`)

1. Film 3–5 down-the-line clips at 120 or 240 fps (at hand height, 3 m behind the hands line).
2. Time MediaPipe Pose (Full and Heavy) against RTMPose-m on the target laptop, on the trimmed swing window only.
3. Compare how stable the hip, shoulder and wrist landmarks are at address, top and impact.
4. Check the `ffprobe` fps **and duration** on an iPhone slow-motion clip exported through the phone's file picker (the `[ASSUMPTION]` in AD-15). If it comes out as a slowed 30 fps file or runs longer than 15 s, update AD-15 before any upload stories start.
5. Check that the chosen backend runs in `python:3.14-slim` with `ffmpeg libegl1 libgles2`, and whether its wheels exist for linux/arm64.
6. Put the model files in `models/MANIFEST.yaml` (URL, SHA-256, licence).
7. Record the choice in the architecture memlog, then set `POSE_BACKEND` in `.env.example`.

## 9. Before the hand-in (2026-12-15)

- [ ] `docker compose up --build` on a clean machine, with `.env` copied from `.env.example`, gives a full mock result (SM-10).
- [ ] No player clips in Git (`git ls-files "*.mp4" "*.mov"` lists only `samples/`).
- [ ] `.env.example` has every variable from §3 with safe defaults, and contains no secrets.
- [ ] The README links to this guide's §6.1 and §6.3.
- [ ] Any non-commercial component (SwingNet) is listed for removal before a paid launch (NFR-7).
- [ ] Next phase (public hosting): follow technology.md §5–§8 — Railway, Supabase Postgres and Storage (a second `FileStore`), TLS, backups, rate limits on auth and chat.

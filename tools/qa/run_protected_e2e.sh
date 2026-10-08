#!/usr/bin/env bash
# Browser QA of protected graded assignments without Docker: builds the throwaway QA fixture,
# migrates a SQLite database, starts the API and the Vite dev server, runs
# frontend/e2e/protected-graded.spec.ts in Chromium and stops both servers.
#
#   tools/qa/run_protected_e2e.sh [WORK_DIR]
#
# Needs a Python environment with backend/requirements.txt (PYTHON=...), frontend dependencies
# installed with npm ci (FRONTEND_DIR=..., default frontend/) and Playwright's Chromium
# (npx playwright install chromium). Everything the run writes goes to WORK_DIR, never the repo.
set -euo pipefail
REPO="$(cd "$(dirname "$0")/../.." && pwd)"
WORK="${1:-$(mktemp -d)}"
PY="${PYTHON:-python3}"
FRONTEND="${FRONTEND_DIR:-$REPO/frontend}"
API_PORT="${API_PORT:-8000}"
WEB_PORT="${WEB_PORT:-5173}"
mkdir -p "$WORK"
WORK="$(cd "$WORK" && pwd)"

"$PY" -B "$REPO/tools/qa/build_protected_fixture.py" "$WORK/fixture" > "$WORK/fixture.json"
rm -f "$WORK/qa.db"
export DATABASE_URL="sqlite:///$WORK/qa.db"
export CONTENT_ROOT="$WORK/fixture/content"
export PRIVATE_ASSESSMENTS_ROOT="$WORK/fixture/private"
export COOKIE_SECURE=false
export ALLOWED_ORIGINS="http://127.0.0.1:$WEB_PORT,http://localhost:$WEB_PORT"
(cd "$REPO/backend" && "$PY" -B -m alembic upgrade head > "$WORK/migrate.log" 2>&1)

(cd "$REPO/backend" && exec "$PY" -B -m uvicorn courselab.main:app --host 127.0.0.1 --port "$API_PORT") \
  > "$WORK/api.log" 2>&1 &
API_PID=$!
(cd "$FRONTEND" && API_PROXY_TARGET="http://127.0.0.1:$API_PORT" \
  exec node_modules/.bin/vite --host 127.0.0.1 --port "$WEB_PORT" --strictPort) > "$WORK/web.log" 2>&1 &
WEB_PID=$!
trap 'kill "$API_PID" "$WEB_PID" 2>/dev/null || true' EXIT

for _ in $(seq 1 60); do
  curl -fs "http://127.0.0.1:$WEB_PORT/api/v1/health" > /dev/null 2>&1 && break
  sleep 1
done
cd "$FRONTEND"
E2E_BASE_URL="http://127.0.0.1:$WEB_PORT" E2E_PROTECTED_FIXTURE=1 \
  node_modules/.bin/playwright test e2e/protected-graded.spec.ts --reporter=list

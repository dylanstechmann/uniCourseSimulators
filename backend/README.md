# Lattice CourseLab learner API

This milestone provides server-owned guest/account state, enrollment, course and lesson reading, notes, bookmarks, learner-marked progress, immutable attempts, deterministic formative checks, practice gradebook evidence, export and account deletion. PostgreSQL is the Docker deployment database; SQLite is used only by portable pytest fixtures and explicit local development fallback.

Run migrations before serving from `/app` in the API image:

```sh
alembic upgrade head
uvicorn courselab.main:app --host 0.0.0.0 --port 8000
```

The root Docker Compose configuration wires this service to PostgreSQL and the frontend. `DATABASE_URL` overrides all database settings for CI. Otherwise `DATABASE_PASSWORD_FILE` points to a private secret file, and `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER` select the connection. Passwords are read at process start and escaped by SQLAlchemy rather than interpolated into an unescaped URL. Never print the resulting connection URL. `CONTENT_ROOT` selects a read-only content package directory (image default `/content`).

`ALLOWED_ORIGINS` is a comma-separated exact origin list. Every mutation requires a permitted `Origin`. Private mutations also require `X-CSRF-Token` returned by `/api/v1/auth/session`. Cookies are HttpOnly, SameSite Lax, scoped to `/api`, and secure by default; set `COOKIE_SECURE=false` only for local HTTP. Session tokens are stored as SHA-256 hashes. Guest sessions last 30 days; accounts seven days. Guest-to-account registration preserves the same learner ID and data. Logout revokes the calling session. Account deletion removes all the learner's records and sessions. Expired guest records require an operator retention/cleanup policy before public deployment.

Course, lesson and source endpoints are public. They use explicit Pydantic learner views and never return `solution_spec`, `answer` or `feedback.solution`. The software does not serve the content folder as static files. Only records explicitly tagged `public-practice-authoring` are readable or gradeable through this unrestricted practice interface; restricted and untagged questions are excluded, including their contribution to the practice gradebook. The migrated practice authoring keys are already public repository material; they must not become secret production exam keys. Future restricted keys belong in a private runtime store. Markdown and notes are data, never executed HTML; the frontend must sanitize Markdown and render notes as text.

The enabled choice graders support zero-based single-choice indices and explicit partial-credit multiple-select policies. Numeric practice accepts finite decimal results with absolute and relative tolerance and a constrained SI/biological unit subset. Relative tolerance is combined with absolute tolerance against the authored answer after exact unit conversion; values are bounded. Optional significant-figure requirements (1–12) are checked only after the numerical value falls within tolerance. Precision is read from the learner's decimal/scientific-notation string: for example, `80` has one significant figure, while `80.` and `8.0e1` have two. The learner sees the required count before submitting. Numerically correct results do not demonstrate reasoning. Missing unit requirements retain the original practice policy, and supplied incompatible units are rejected. Physical symbol and prefix case is preserved; `mV` and `MV` are different. Unknown and affine units fail closed; contextual `pH`, assay `units`, and `mol ATP` labels are only accepted as their exact authored labels. Authored formative variants are selected reproducibly from a signed, expiring token; the resolved variant and specification digest are stored with the attempt. Variant metadata exposes no answer or solution, and these repository practice items are not production exam keys. Symbolic/structured/code/file/design responses, timed exams, and manual overrides are not enabled. Feedback has diagnosis, targeted hint, next step and exact lesson ID, and never asserts that reasoning was assessed. Gradebook aggregation is the best practice result per question, with raw objective evidence counts; it never labels these as mastery or formal grades.

`capabilities.py` defines disabled isolated runner and feedback interfaces. No submitted code or LLM request is executed. A future runner requires ephemeral isolated containers with no network or host mounts, no Docker socket, a read-only base filesystem, bounded writable temporary space, strict CPU/memory/time limits and allowlisted dependencies. Tests verify that a malicious or infinite-loop programming submission has no execution route.

All learner queries filter by the authenticated principal; request-supplied user IDs cannot select another learner. Attempts are append-only through the API and pinned to the enrollment's course version. If a package version changes, new version-dependent operations are blocked pending an explicit enrollment migration. The selected authored variant and its specification digest are pinned per attempt. Variant tokens expire after seven days; deployments that need tokens to survive API restarts must configure a stable `VARIANT_TOKEN_SECRET` of at least 32 bytes. Server responses label timestamps as UTC with `Z`. Concurrent conflicting writes return a safe 409 requiring a retry, rather than leaking database errors; atomic upsert and client retry policies remain production hardening work.

The single-worker development rate limiter is in memory. A production deployment needs a shared rate limiter at the trusted reverse proxy, resource limits, guest-retention policy, email verification/recovery, operator monitoring, and regular backups. Request bodies are capped at 64 KiB and note/response fields are bounded. Response headers prevent caching learner data and disable MIME sniffing. No provider keys, database passwords or learner records are committed.

Backend checks run through the workspace `dev` service:

```sh
cd /workspace/lattice-courselab-backend-wt/backend
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/pytest
.venv/bin/ruff check .
```

The tests cover schema rejection, alternate numeric forms, wrong units, tolerance edges, mutated keys, prompt-injection text, disabled code execution, private answer-field exclusion, cookie/token/CSRF/origin protections, owner isolation, persistence, guest conversion, password hashing, expiry, immutable history, export/deletion, traversal protection and Alembic schema compatibility. A browser sanitizer requires its own frontend tests; server text storage tests do not substitute for them.

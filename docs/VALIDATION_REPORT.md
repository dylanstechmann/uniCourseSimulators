# Validation report

## Scope and result

2026-10-05; synthetic local learner data only. Milestones 1 and 2 are implemented. Milestone 3 remains in progress; the deterministic grading increments are described below. A Milestone 4 curriculum-map increment is implemented and tested, while subject-matter review and map refinement remain. All 25 course packages are **partial**; zero are beta, complete or externally reviewed. No instructor review, semester equivalence, university credit, security certification or public production deployment is asserted.

The preceding data-interpretation increment passed **229 tests with 1 skipped** across backend (167), course authoring (37 plus 1 skipped), frontend unit (16), Playwright (5), and legacy state tests (4). Its inventory was 25 packages, 101 lessons, 103 questions, 202 cards and 25 cases, with zero content errors and 125 disclosed depth/coverage warnings. Its API integration check graded 105 supported practice specifications. Current incremental results follow.

## Milestone 4 curriculum-map increment

The new map contains 25 existing partial package nodes plus 37 explicit **catalog-only** subject nodes in eight pathways (62 nodes total). The JHU pathway lists organic chemistry, biochemistry, molecular biology, cell biology, and all eight requested advanced areas. Its links are curriculum references only; no Johns Hopkins teaching text or assessment was copied. The supplied catalogue URL ending in `regenerative-stem-cell-technologies-master-science/` could not be opened; the repository links the verified 2026–27 canonical catalogue page and the public degree/course page instead. This creates no affiliation, equivalency, admission, or credit claim.

The versioned schema and content validator check catalog maturity, pathway/topic coverage, package and source references, duplicate descriptions, placeholders, package/catalog ID collisions, and prerequisite cycles across both node types. The FastAPI `/api/v1/curriculum` response contains maturity and prerequisite metadata; Playwright confirmed the live endpoint serves 62 nodes and 8 pathways. The accessible catalog explorer exposes dependencies and lets learners open related partial packages while marking planned areas as not yet authored.

Validation for this increment: **235 tests passed, 1 skipped** across content authoring (40 plus 1 skipped), backend (168), frontend (17), Playwright (6), and legacy-state tests (4). Content validation reports 25 packages, 101 lessons, 103 questions, 202 cards and 25 cases; zero errors and 125 disclosed depth/coverage warnings. Ruff and frontend lint passed; the TypeScript/Vite production build passed (202 modules). The API content integration check passed for 25 packages and 105 supported practice specifications. Live health and curriculum endpoint checks passed (healthy, 62 nodes, 8 pathways, 37 catalog-only nodes). The bundle/security scan reported 0 findings across 365 files; `npm audit --audit-level=high` reported no known vulnerabilities. Docker Compose rebuilt and reported database, API and web healthy, with the migration service complete.

## Previous published increment: deterministic data interpretation

Grader policy `practice-v7` enables one composite item in a supplemental original statistics lesson. It asks for a unit-checked mean difference and a choice of the strongest evidence-bounded conclusion. Each field receives separate points; omitted fields receive zero; unknown fields reject the response; malformed or injection-like text cannot earn credit. The grader does not score prose, keyword overlap, or reasoning. Public learner DTOs include only field identifiers, prompts, options, units and points. The hidden answer specifications remain server-side and the production frontend bundle scan found no private answer markers.

The new statistics manifest is version 0.1.1 and remains **partial**. Its added lesson explains sample contrasts, uncertainty requirements and limits on causal inference, and provides two original retrieval cards that appear behind reveal controls in the lesson reader. Its source map labels the material original and MIT OCW 18.05 link-only comparator. No MIT material was copied or adapted. The public course remains a short package, not a semester course.

Current commands and results: `docker compose up --build -d --wait --wait-timeout 180` (PASS; API, web and PostgreSQL healthy; Alembic migration service exited successfully); `docker compose run --rm --no-deps api pytest -q -p no:cacheprovider` (167 passed); `python tools/validate_content.py --root .` (25 courses, 101 lessons, 103 questions, 202 cards, 25 cases; 0 errors, 125 warnings); `docker compose run --rm --no-deps api python -m courselab.check_content /content` (25 packages, 105 supported specifications passed); root `pytest tests/content` (37 passed, 1 skipped); frontend `npm run lint`, `npm test` (16 passed), and `npm run build` (PASS); `npm run test:e2e` (5 passed, including retrieval-card reveal plus data-interpretation partial-credit and persistence paths); `npm run test:legacy` (4 passed); `docker compose run --rm --no-deps api ruff check --no-cache .` (PASS); `python tools/check_security.py --bundle frontend/dist` (363 files, 0 findings); `npm audit --audit-level=high` and `uv run --project backend --with pip-audit pip-audit -r backend/requirements.txt` (0 known vulnerabilities each). The full Compose scenario exercised guest enrollment, lesson viewing, a split-field submission, feedback display, and reload persistence. The API health endpoint returned `status: ok`; Alembic reports `0002 (head)`.

## Milestone 3 incremental validation

The implementation includes multiple-select partial credit, version-pinned question digests, explicit package-version updates, numeric grader v5, reproducible authored variants, and objective evidence v1. Objective points aggregate the best score once per distinct tagged question; retry counts remain visible but cannot inflate breadth. The provisional study indicator requires three distinct questions, at least 80% coverage of tagged questions, and at least 80% of possible points on attempted questions. The API returns its policy version and thresholds; the learner view explains that a positive indicator is not a mastery certification. The numeric implementation parses a bounded, documented subset of SI and biological units into exact rational scales and seven base dimensions, converts learner values into the authored unit, combines absolute and bounded relative tolerance against the authored answer, checks optional author-provided dimensions, and enforces optional 1–12 significant-figure requirements after the value passes tolerance. Decimal precision is counted from the learner's notation; the reader exposes the required precision as accessible question metadata and explanatory helper text. Contextual `pH`, `units`, and `mol ATP` labels are exact-label-only and cannot be composed; unknown and affine units fail closed. Numeric input length, decimal magnitudes, unit expression length, token count, exponents, relative tolerance, and significant-figure policy values are bounded. The digest is omitted from learner DTOs because it fingerprints answer-bearing content. Public lesson DTOs expose required precision and the selected authored prompt/options, never answer keys. Historical attempts remain unchanged with their recorded grader version and null digest where previously absent.

Authored variants are a finite choice among explicitly written forms, selected deterministically from a signed seven-day seed token bound to course, content version, and question. The example biology bank has three distinct forms for one practice item. The API returns a whitelisted prompt/options DTO plus the opaque token; the attempt resolves and grades the matching server-side specification and records its variant ID and digest. The learner history shows that variant and its feedback details. This does not generate numeric parameter variants and does not secure public practice material as an exam bank.

The symbolic plugin uses SymPy 1.14.0 behind an AST allowlist and explicit length, depth, node-count, degree, term-count, variable-count and operation-count limits. It accepts rational arithmetic with declared variables and typed assumptions, normalizes learner `^` powers to mathematical precedence, and compares forms using targeted rational cancellation. Python calls, attributes, subscripts, undeclared names, unsupported functions and expressions outside the limits fail closed. An original quotient-rule item in Calculus I version 0.1.1 exercises alternate-form grading; the course remains partial. The item answer is excluded from its public lesson DTO, the actual Compose-backed browser submission earned formative credit and saved feedback, and injection text earned zero points. This is not a general symbolic calculus engine and it does not assess derivation or domain restrictions.

Commands for this increment included `docker compose build api`, `docker compose run --rm --no-deps api pytest -q -p no:cacheprovider`, `docker compose run --rm --no-deps api ruff check --no-cache .`, `python tools/validate_content.py --root .`, `docker compose run --rm --no-deps api python -m courselab.check_content /content`, `npm run lint`, `npm test`, `npm run build`, `npm run test:e2e`, `npm run test:legacy`, `npm audit --prefix frontend --audit-level=high`, `uv run --project backend --with pip-audit pip-audit -r backend/requirements.txt`, `python tools/check_security.py --bundle frontend/dist`, and `docker compose up --build -d`. All passed after correcting two expected test totals for the new practice item. The local Compose API and web services reported healthy; Alembic remained at `0002 (head)`.

## Previous Milestone 3 validation snapshot

The following command list, tables and notes record the earlier variant/objective-evidence increment before bounded symbolic grading was added. They are retained as a historical baseline; the current increment results are listed above.

Commands run from the repository root or its `frontend`/`backend` subdirectory as applicable:

```sh
uv run --project backend --with pytest --with ruff --with jsonschema python -m pytest -q
uv run --project backend --with pytest --with ruff --with jsonschema ruff check backend/courselab backend/tests
npm --prefix frontend run lint
npm --prefix frontend run test
npm --prefix frontend run build
npm audit --prefix frontend --audit-level=high
npm --prefix frontend run test:e2e
uv run --project backend --with pytest --with ruff --with jsonschema python tools/validate_content.py
uv run --project backend --with pytest --with ruff --with jsonschema python tools/check_security.py --bundle frontend/dist
npm run test:legacy
docker compose up --build -d --wait --wait-timeout 180
docker compose exec -T api alembic current
docker compose exec -T api python -c "import urllib.request; print(urllib.request.urlopen('http://127.0.0.1:8000/api/v1/health').read().decode())"
```

| Check | Result |
| --- | --- |
| Combined backend/content-security pytest | 173 passed, 1 skipped; 1 upstream Starlette/httpx deprecation warning |
| Ruff | All checks passed |
| Frontend lint/format | Passed |
| Vitest | 14 passed across 6 files |
| TypeScript/Vite build | Passed; 202 modules |
| npm audit | 0 known vulnerabilities |
| Playwright | 3 passed; guest enrollment, both choice types, a seeded variant submission, objective evidence state, feedback, notes, progress, account export/deletion, and hidden-solution checks |
| axe | No detected WCAG 2/2.1 A/AA violations in catalog, lesson, and practice gradebook views |
| Legacy state tests | 4 passed |
| Content validator | 25 courses, 100 lessons, 101 base questions, 200 cards, 25 cases; 0 errors and 125 explicit warnings |
| API content integration | 25 course packages and 103 supported specifications including authored variant forms |
| Source/bundle boundary scan | 362 files; 0 findings, including the production JavaScript bundle |
| Docker Compose/PostgreSQL | Services healthy; migration `0002 (head)`; health status `ok`; local origins only |
| Production Compose configuration | Valid with synthetic hostname, non-secret path, and validation-only token key |
| GitHub Actions | PASS for objective-evidence commit `b699162`; [workflow run](https://github.com/dylanstechmann/uniCourseSimulators/actions/runs/37376974796). |

The migration test confirms preexisting attempts survive with no invented specification digest. Numeric grader tests recalculate conversion and absolute/relative-tolerance boundaries for rates, compound concentration/time units, lengths, acceleration, percentages and derived units; they also check significant-figure counts across decimal/exponent notation and integer trailing zeros, a 12-figure upper bound, invalid policies, negative/zero answers, dimensions, exact-label contextual units, unknown/affine units, malformed/incompatible units, alternate micro symbols, exponent bounds, and SI case distinctions. The deployed-content integration check grades all 101 published practice specifications and verifies learner DTOs omit solution data. An API test confirms precision metadata is public while answer specifications remain private, and that an in-tolerance answer with excess precision receives a specific diagnostic. A version-upgrade API test verifies old attempts remain in history, are excluded from the new-version aggregate, and only current-version work contributes to that gradebook. For browser tests, the workspace container joined the app network and temporarily added `http://web` to its allowed-origin list; the application was then recreated with only documented localhost origins. The end-to-end flow persisted guest enrollment, lesson practice, feedback, notes and progress and verified that public lesson DTOs omit answer specifications. These checks do not amount to a penetration test or prove code-execution isolation; the arbitrary-code runner and LLM feedback providers remain disabled.

The historical Milestone 1 and 2 validation record follows. Its counts describe the state before this M3 increment.

## Baseline and milestone 1

Before changes, inspected README, LICENSE, docs, app/data/pathways, HTML and CSS. Started the unchanged static reader on localhost:4173 in the shared development container. Used the first cell-biology practice item, saved a synthetic note and reloaded; result/note persisted without console errors. [CURRENT_STATE_AUDIT.md](CURRENT_STATE_AUDIT.md) records behavior, counts and limitations.

Milestone 1 renamed the product, retained a backed-up storage migration, introduced schemas/maturity/provenance, and preserved 25 partial packages: 100 readings/questions, 200 cards and 25 cases. Integrated checks passed 34 content tests, 4 state tests and JavaScript syntax checks. Browser regression confirmed the new identity and retained state. Intermediate failures from a short robotics hint and a pytest invocation from the wrong directory were corrected. Legacy asset URLs were versioned to resolve stale module caching.

Local milestone 1 commit: `5ad7563`; published GitHub milestone 1: `ccefbba1fa721e655c83793471c3597427c4b19c`. Checkout and remote originally had separate histories. Publication uses non-forced Git Data API commits preserving the remote parent chain; local/remote commit IDs differ.

## Milestone 1 and 2 automated commands and results

The shared workspace Linux development service used Node 24/Python 3.11; runtime images use Node 24/Python 3.12. Run from the repository root, then backend as shown:

```sh
python3 -m venv /tmp/courselab-final
/tmp/courselab-final/bin/pip install -r requirements-dev.txt -r backend/requirements.txt
/tmp/courselab-final/bin/python tools/validate_content.py
/tmp/courselab-final/bin/python -m pytest tests -q
npm run test:legacy
/tmp/courselab-final/bin/ruff check backend tools tests
/tmp/courselab-final/bin/python tools/check_security.py --bundle frontend/dist
cd backend
/tmp/courselab-final/bin/python -m pytest -q
/tmp/courselab-final/bin/python -m courselab.check_content ../content
```

| Check | Actual final result |
| --- | --- |
| Content/schema validator | PASS; 25 courses, 100 lessons/questions, 200 cards, 25 cases; 0 errors |
| Explicit warnings | 100 preserved short readings; 25 incomplete outcome-coverage warnings |
| Content/security pytest | 36 passed, 79.28 seconds |
| Legacy state tests | 4 passed |
| Ruff | All checks passed |
| Source/bundle boundary scan | 356 source files; 0 findings |
| Backend pytest | 71 passed, 11.25 seconds |
| API/content integration | 25 packages and 100 supported practice specifications passed |

Backend coverage includes ownership, session/password handling, CSRF/Origin, guest conversion, export/delete, immutable attempts, malformed/injection input, units, tolerance/alternate numeric forms, unsupported specifications, restricted-question denial, hidden solution fields, and Alembic upgrade/downgrade/schema comparison. One upstream Starlette TestClient/httpx deprecation warning remains. Automated backend fixtures use SQLite; real PostgreSQL was also exercised below.

```sh
cd frontend
npm ci
npm run lint
npm run test
npm run build
npm audit --audit-level=high
npx playwright install --with-deps chromium
npm run test:e2e
```

| Check | Actual final result |
| --- | --- |
| ESLint/Prettier | PASS |
| Vitest | 9 passed in 6 files, 27.21 seconds |
| TypeScript/Vite production build | PASS; 202 modules |
| npm audit | 0 known vulnerabilities |
| Chromium Playwright | 3 passed, 5.0 seconds |
| axe catalog/lesson scans | 0 detected WCAG 2/2.1 A/AA violations in those views |

The workspace test container could not reach the loopback-bound application through `host.docker.internal`. Final Playwright joined the application's network through an untracked workspace override, used `E2E_BASE_URL=http://web`, and temporarily allowed that exact test origin. Final Compose restored default localhost/127.0.0.1 origins. CI tests on the Ubuntu host's localhost and needs no workspace override.

The initial integrated browser workflow caught a real gradebook DTO mismatch: API limitations are a string, while frontend code iterated an array. Corrected the TypeScript type/rendering, added a regression fixture, rebuilt and passed all browser tests. CRLF formatting failures were corrected with LF normalization and `.gitattributes`.

The browser flow covers guest enrollment, reading, submission/feedback, notes/read marks/bookmarks, reload persistence, gradebook/history, account conversion preserving enrollment, export and deletion. Public DTO tests exclude assessment answer/solution specifications. nginx returns 404 for authoring banks, legacy answer-bearing JavaScript and `/.env`. Bundle scans reject private assessment markers. Public authoring practice specifications remain discoverable in the repository; worked examples are intentionally public readings. No restricted production exam keys, real learner exports, API keys or database passwords are committed. These bounded scans are not a penetration test.

An initial Python audit found advisories in older Starlette/pytest dependencies. Updated to FastAPI 0.142.2, Starlette 1.7.0 and pytest 9.1.1, reran 71 backend tests and the dependency audit: no known vulnerabilities reported. [backend/DEPENDENCY_AUDIT.md](../backend/DEPENDENCY_AUDIT.md) records details. Container operating-system scanning is not included.

## Full Compose and PostgreSQL persistence

From the repository root:

```sh
docker compose up --build -d --wait --wait-timeout 180
docker compose ps
docker compose exec -T api alembic current
docker compose restart db api
docker compose up --build -d --wait --wait-timeout 180
```

Default Compose started with newly initialized CourseLab volumes and no manually supplied password. Credential initialization and Alembic exited 0; migration is `0001 (head)`. PostgreSQL/API/web became healthy. Build-time content validation passed. HTTP health reported `status: ok` and disabled programming/LLM capabilities. Only nginx localhost:8080 is published; database/API ports remain internal.

A separate browser check enrolled a guest in biology, submitted the correct first choice and received 1/1 practice points with reasoning explicitly unassessed. Saved a synthetic note and marked a lesson read. After PostgreSQL/API restart and API recreation, reload retained note, read mark, enrollment and feedback. The gradebook retained 1/4 available practice points and the saved attempt/version/time. No browser console errors appeared. This checks database persistence beyond browser storage.

The preserved legacy reader runs separately on localhost:4173 with historical synthetic note/result retained. It is excluded from the default application image because its public practice answers cannot protect restricted assessments.

## Backup, restore and production configuration

Restored a custom archive into a newly created disposable database:

```sh
docker compose exec -T db pg_dump -U courselab -d courselab --format=custom --file=/tmp/courselab-validation.dump
docker compose exec -T db createdb -U courselab courselab_restore_check_20261005
docker compose exec -T db pg_restore -U courselab -d courselab_restore_check_20261005 --no-owner --no-acl --single-transaction --exit-on-error /tmp/courselab-validation.dump
```

All exited 0. Both active/restored databases contained 2 synthetic users, 2 attempts, 2 notes and 2 progress rows. Active data was not overwritten. Removed only the disposable database/archive afterward. This is a local logical restore rehearsal, not off-host disaster recovery or application cutover validation.

`docker compose -f compose.production.yaml config --quiet` passed with a validation-only hostname and existing non-secret path. Caddy configuration validation passed in a network-disabled container with `COURSELAB_DOMAIN=example.invalid`; a formatting warning was corrected and validation rerun. No production service, certificate issuance or public HTTPS was tested. [DEPLOYMENT.md](DEPLOYMENT.md) gives migration, secret permissions, proxy/domain/HTTPS and binary-safe backup/restore commands plus hardening limits.

## Sources, migration and remaining work

28 official sources are registered. No third-party instructional assets were copied/adapted. MIT software licensing is retained with documented separate educational-content/OCW boundaries. Institutional references establish curriculum alignment only.

`python tools/validate_content.py --check-links` exited 1: 26 references were reachable; JHU degree-details and admission-requirements pages returned HTTP 403 to the probe. Official page research was possible earlier. A 403 does not establish that a link is broken, but the automated live-link gate has not passed.

`node tools/migrate_prototype.mjs` correctly refused an overwrite (expected exit 1). Rehearsals require `--output` with a fresh directory. Git whitespace checks passed.

GitHub Actions configuration runs content/security, backend/frontend lint/tests/builds, Compose and browser flows with diagnostics. Hosted CI passed for objective-evidence commit `b699162` in addition to the local checks above.

Milestone 3 remains in progress: wider unit coverage, structured/data/design rubrics, numeric parameter generation, weighted categories, robust objective mastery from diverse assessments, appeals/overrides, broader evidence-linked misconception feedback, provider interfaces and an isolated code worker still need implementation and verification. The symbolic plugin supports rational expressions only; general symbolic calculus remains unsupported. Code execution and LLM providers remain disabled. Eight pathways, a visual graph, full original 14-week biology, remaining recalculation/mutation/accessibility gates and actual qualified review remain milestones 4–6. [ROADMAP.md](ROADMAP.md) records exact work and production hardening gaps.

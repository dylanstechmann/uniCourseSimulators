# Validation report

## Scope and result

2026-10-05; synthetic local learner data only. Milestones 1 and 2 are implemented. Milestone 3 remains in progress; the deterministic grading increments are described below. A Milestone 4 curriculum-map increment is implemented and tested, while subject-matter review and map refinement remain. All 25 course packages are **partial**; zero are beta, complete or externally reviewed. The appeal workflow provides individual formative-score review, but no qualified course-content review, semester equivalence, university credit, security certification or public production deployment is asserted.

## Current increment: product rename and progress review

The product and public GitHub repository are now **uniStemCourseSimulators**. UI, metadata, API title, normalized package names, schema namespaces, exported filename and documentation use the new identity. Existing browser notebooks are sanitized into a v3 key with retained old keys/backups; migration write failures keep readable prior data available in memory. The existing local Compose project identity is pinned in an untracked `.env` to preserve both database and credential volumes. Technical Python/database/session/configuration identifiers remain stable. No course maturity changed.

[PROGRESS_REVIEW.md](PROGRESS_REVIEW.md) assesses the six milestones against actual code/content. [ROADMAP.md](ROADMAP.md) now prioritizes reviewer identity, saved-variant/digest reconstruction, semester assessment workflows and substantive biology instruction. The review found unresolved instructor impersonation and appeal fidelity defects; passing existing tests does not resolve them. Public instructor access must remain disabled. The biology syllabus was corrected to its actual version 0.3.2 and seven-question inventory.

Local checks ran through the workspace `dev` container (Python 3.11 and Node 24); Compose uses Python 3.12. Commands inside the development container used `/tmp/uni-review/bin/python` and `/tmp/uni-review/bin/ruff` from a temporary environment installed from both requirement files. All current tests passed: **285 total**—195 backend, 52 root content/security checks, 22 Vitest, 9 Playwright and 7 legacy migration tests. The root suite had no skipped tests because SymPy was present. Its warnings include the upstream Starlette/httpx test-client deprecation. A final targeted catalog check verifies the renamed title and accessible brand.

| Command/check | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 101 lessons, 106 questions, 203 cards, 25 cases; zero errors, 125 disclosed depth/objective warnings |
| `python -m pytest tests -q` | 52 passed |
| `cd backend; python -m pytest -q` | 195 passed |
| `python -m courselab.check_content ../content` | PASS: 25 packages / 108 supported specifications |
| `npm run test:legacy` | 7 passed, including both previous keys, precedence, retained backups, malformed prior values and denied writes |
| `ruff check backend tools tests` | PASS |
| Frontend `npm run lint`, `npm test`, `npm run build` | PASS; 22 unit tests, TypeScript/Vite build of 203 modules |
| `python tools/check_security.py --bundle frontend/dist` | PASS: source/bundle scan, zero findings; public DTO exclusions also exercised by E2E |
| `docker compose up --build -d --wait --wait-timeout 180` | PASS: PostgreSQL/API/web healthy; credential/migration services exit 0; Alembic `0003 (head)` |
| `E2E_BASE_URL=http://host.docker.internal:8080 npm run test:e2e` | 9 passed against the complete Compose application; enrollment, reading, submissions, partial credit, feedback, notes/progress, upgrade/export/delete, appeal and reload persistence |
| Development and production Compose configuration | PASS; fresh development default resolves to `uni-stem-course-simulators`; production checked with validation-only domain/secret placeholders |

The initial container frontend test launch encountered a Windows-installed Rollup optional dependency. `npm ci` inside the Linux development container repaired the environment without changing dependency versions; tests/build then passed. Playwright Chromium and its Linux dependencies were installed inside that development container. Its bridge URL was temporarily allowed as a mutation origin and the existing synthetic reviewer was temporarily allowlisted for the local appeal test. After testing, the API was restored to its default localhost origins and empty instructor allowlist. Only loopback web access is published.

Data continuity was checked immediately before and after container recreation, before E2E added synthetic records: 77 users, 77 enrollments, 84 attempts and 6 progress records were unchanged. No volume was removed or copied, no live database password rotated, and no learner record was rewritten for branding. The untracked environment pin contains only the existing project identity. Source scanning is a bounded automated check, not a penetration test or proof against every possible secret. Live-source probes and dependency audits were not repeated for this identity-only increment; the previously recorded JHU HTTP 403 probe limitations remain unresolved. No public HTTPS deployment or external academic review is asserted.

## Previous increment: practice-v10 fixed-axis graph-coordinate practice

The deterministic graph grader awards separate partial credit for learner-entered x and y coordinates. The statistics practice lesson supplies bounded axes, labeled points, and replicate data; learners calculate group means, enter each coordinate, and receive a live SVG preview plus a screen-reader-readable source table. Expected coordinates, tolerances and criterion evidence remain server-side. The authoring validator independently recalculates each plotted mean and checks source-coordinate mapping. This narrow profile does not grade graph choice, axis selection, uncertainty bars, interpolation, model fit, or interpretation.

The statistics package advances to version 0.1.2 and stays **partial**. Its graph task is a bounded formative exercise; it does not turn the package into a full statistics course or establish course mastery.

Final local validation for this increment: **281 tests passed, 1 skipped** across backend (195), course authoring (49 plus 1 skipped), frontend unit (22), Playwright (9), security-boundary unit tests (2), and legacy state (4). The content validator reports 25 course packages, 101 lessons, 106 questions, 203 retrieval cards and 25 cases, with zero errors and 125 explicit depth/coverage warnings. The API integration checker passed for 25 packages and 108 supported practice specifications. Ruff, frontend lint/Prettier, TypeScript/Vite production build (203 modules), and the source/bundle boundary scan (368 source files, 0 findings) passed. The npm and Python dependency audits reported no known vulnerabilities. Production Compose configuration passed with validation-only placeholder values.

`docker compose up --build -d --wait --wait-timeout 180` passed; database, API and web were healthy and the migration service exited successfully. Alembic reports `0003 (head)`, `/api/v1/health` returns `ok`, and `/api/v1/curriculum` returns 62 nodes across 8 pathways. Browser checks exercised enrollment, lesson and retrieval tools, graded submissions, feedback, saved progress, appeals, the graph plot's 2.5/3 pointwise partial credit and reload persistence, CSV credit, and accessibility. All 9 Playwright tests passed. The graph source table, SVG preview and feedback view had no detected WCAG 2/2.1 A/AA violations; public DTO tests confirm answer specifications remain excluded. The appeal E2E temporarily allowlisted its synthetic reviewer account, then restored the API to an empty allowlist. All checks use synthetic learner data and do not establish public production deployment, penetration testing or security certification.

## Previous published increment: practice-v9 bounded CSV analysis uploads

The server now grades a bounded CSV upload against an authored numeric-table specification. It accepts UTF-8 CSV with an optional byte-order mark, caps the base64 payload at 32 KiB, limits rows, columns and cell sizes, checks exact ordered headers and authored row keys, rejects duplicate or malformed data, and reuses the deterministic numeric/unit grader for each cell. Partial credit is reported per rubric check. The grader parses data only; it does not execute uploaded files or submitted code. The public lesson DTO exposes only the CSV media type and size limit.

Foundations of Cell and Molecular Biology version 0.3.2 adds an original replicate-count and mean-signal upload exercise. The content validator checks its schema, rubric mapping and point total, then independently recalculates the authored counts and means. The course remains **partial**: the upload exercise does not supply a semester of instruction, a full laboratory sequence, or general-purpose data-analysis grading.

Final local validation for this increment: **266 tests passed, 1 skipped** across backend (188), course authoring (44 plus 1 skipped), frontend unit (21), Playwright (9), and legacy state (4). The content validator reports 25 course packages, 101 lessons, 105 questions, 202 retrieval cards and 25 cases, with zero errors and 125 explicit depth/coverage warnings. The API integration checker passed for 25 packages and 107 supported practice specifications. Ruff, frontend lint/Prettier, TypeScript/Vite production build (203 modules), and the source/bundle boundary scan (367 source files, 0 findings) passed. Production Compose configuration also passed with validation-only placeholder values.

`docker compose up --build -d --wait --wait-timeout 180` passed; database, API and web were healthy and the migration service exited successfully. Alembic reports `0003 (head)`, `/api/v1/health` returns `ok`, and `/api/v1/curriculum` returns 62 nodes across 8 pathways. Browser checks exercised enrollment, lesson practice, feedback, notes, progress persistence, account flows, appeal review, CSV partial credit and persistence, accessibility scans, and absence of answer specifications from public DTOs. The appeal E2E requires a configured instructor allowlist, so the synthetic reviewer was enabled for that run and the development API was restored to the default empty allowlist afterward. These checks use synthetic data and do not establish a public production deployment, penetration test or security certification.

## Previous published increment: practice-v8 structured analytic rubric

The deterministic grader now supports two-to-twenty explicit analytic criteria mapped one-to-one to structured response fields. Criterion points must match field points and sum to the parent total. The first increment supports keyed single-choice fields and uses the existing deterministic choice grader for each criterion. Unknown fields reject the whole item; missing fields receive no points; malformed and prompt-injection text cannot earn credit. Criteria and evidence anchors stay server-side while the learner sees the prompt, options and points. No natural-language reasoning or keyword matching is scored.

Foundations of Cell and Molecular Biology version 0.3.1 adds an original four-criterion formative item on delivery controls, promoter occupancy, motif dependence, and limits on causal inference. It is mapped to the existing experimental-logic outcome and is explicitly limited to the short partial course. The syllabus and package still lack a 12–15 week schedule, substantial weekly work, laboratories, exams, and an integrative project; this increment does not change maturity.

Final local suite for this increment: **254 tests passed** (backend 177, content authoring 46, frontend unit 19, Playwright 8, legacy state 4). Content validation reports 25 packages, 101 lessons, 104 questions, 202 cards and 25 cases; zero errors and 125 explicit depth/coverage warnings. The deployed content check grades 106 supported practice specifications. Ruff, frontend lint/Prettier, TypeScript/Vite build (203 modules), and source/bundle scan (367 files, 0 findings) passed. Playwright exercised the structured response's 3/4 partial credit, criterion-level feedback, reload persistence and accessibility scan, along with the existing enrollment, data-interpretation and audited appeal paths.

`docker compose up --build -d --wait --wait-timeout 180` passed; database, API and web were healthy and the migration service exited successfully. Alembic reports `0003 (head)`, the API health endpoint reports `ok`, and the curriculum endpoint returns 62 nodes and 8 pathways. Production Compose configuration passed with validation-only placeholders. These are local checks using synthetic data; they do not establish a deployment or security certification.

## Prior increment: audited learner appeals and manual formative adjustments

Alembic revision `0003` stores each learner appeal separately from its immutable attempt and records one append-only instructor decision. An operator-configured registered-account email allowlist gates the instructor queue. A current-version appeal can be adjusted, upheld or declined; stale-version prompts cannot be scored against an unavailable question. Adjustments appear as effective formative scores while the automatic score/result remain intact. Ownership, self-review denial, CSRF, score bounds, duplicate reviews, reviewer anonymization and learner deletion have backend coverage. The interface includes a learner request form, accessible instructor queue and gradebook/history labels. This is a narrow formative appeals feature, not staffed course grading or protected examination infrastructure.

Final local checks for this increment: **244 tests passed** (backend 172, content authoring 43, frontend unit 18, Playwright 7, legacy-state 4). Frontend lint/Prettier, TypeScript/Vite production build (203 modules), Ruff, the 25-package content validator (101 lessons, 103 questions, 202 cards and 25 cases; 0 errors and 125 explicit depth/objective warnings), and the source/bundle security scan (367 files, 0 findings) passed. The full browser flow exercised enrollment, lesson practice, appeal submission, an allowlisted human score adjustment, reload persistence and gradebook display; the instructor review view had no detected WCAG 2/2.1 A/AA violations. The backend suite emitted upstream Starlette/httpx and Python `datetime.utcnow()` deprecation warnings; they did not fail tests.

`docker compose up --build -d --wait --wait-timeout 180` passed after the final rebuild. PostgreSQL, API and web reported healthy; the credential initialization and migration services exited successfully. Alembic reports `0003 (head)`, `/api/v1/health` returns `ok`, and `/api/v1/curriculum` returns 62 nodes across 8 pathways. `docker compose -f compose.production.yaml config --quiet` also passed with a synthetic hostname and validation-only secret placeholders. These checks use synthetic local accounts and do not establish a public deployment or a security audit.

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
| GitHub Actions | PASS for objective-evidence commit `b699162`; [workflow run](https://github.com/dylanstechmann/uniStemCourseSimulators/actions/runs/37376974796). |

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

Default Compose started with newly initialized named volumes under the then-current project identity and no manually supplied password. Credential initialization and Alembic exited 0; migration is `0001 (head)`. PostgreSQL/API/web became healthy. Build-time content validation passed. HTTP health reported `status: ok` and disabled programming/LLM capabilities. Only nginx localhost:8080 is published; database/API ports remain internal.

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

Milestone 3 remains in progress: broader structured/data/design rubrics, numeric parameter generation, weighted categories, robust objective mastery from diverse assessments, broader evidence-linked misconception feedback, provider interfaces and an isolated code worker still need implementation and verification. The symbolic plugin supports rational expressions only; general symbolic calculus remains unsupported. Code execution and LLM providers remain disabled. Eight pathways and a visual graph are present, while the full original 14-week biology course, remaining recalculation/mutation/accessibility gates and qualified course-content review remain future work in milestones 4–6. [ROADMAP.md](ROADMAP.md) records exact work and production hardening gaps.

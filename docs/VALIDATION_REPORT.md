# Validation report

## Scope and result

2026-10-06; synthetic local learner data only. Milestones 1 and 2 are implemented. Milestone 3 remains partial; deterministic graders and prototype graded-assignment and review workflows are described below. A Milestone 4 curriculum-map increment is implemented and tested, while subject-matter review and map refinement remain. All 25 course packages are **partial**; zero are beta, complete or externally reviewed. Human score review is limited to saved attempts and does not constitute course-content review. No semester equivalence, university credit, security certification or public production deployment is asserted.

## Current increment: assessment-protection toggle, six geroscience lessons, a time-to-event lesson (2026-10-08, second pass)

Written by an AI coding assistant.

- **Assessment protection toggle.** `grading_policy.assessment_protection` is `open` (default) or `protected`; the operator variable `ASSESSMENT_PROTECTION` (`course`, `protected`, `open`) can force either. In protected mode a graded assessment must read from the private store; a public source is refused when the plan is built and when questions are served, so switching a live deployment to protected closes open graded assessments. The plan response reports the mode in force and the plan view labels it. Open mode does not make keys secret and says so. Practice items are public in both modes. Documented in `docs/DEPLOYMENT.md` and `docs/AUTHORING_GUIDE.md`; 7 backend tests and 1 frontend test.
- **Geroscience 0.3.0.** Six original lessons (genome instability and repair; proteostasis, autophagy and mitochondria; nutrient sensing and lifespan interventions; regeneration across species; reading an aging-intervention paper; evidence tiers from model to human) of about 870 to 1,200 words each, with synthetic tables, worked examples, 31 practice items, 24 cards and link-only references whose identifiers were checked on 2026-10-08 (title resolution only; claim support is a reading judgement). Their objectives are linked to the four course outcomes, so no geroscience outcome is unlinked. The lessons state that no intervention is claimed to slow or reverse human aging.
- **Transport, bioreactors and programming 0.2.0.** One original lesson each: oxygen limits in thick constructs (zero-order uptake, critical thickness, a diffusion-to-consumption ratio), sizing oxygen supply (kLa, supportable cell density, static-dish medium depth, limits of empirical correlations), and testing a scientific function (known-answer tests, float tolerances, seeds, provenance). Parameters are synthetic; each has 5 to 6 items with computed keys and 4 cards; their modules reuse the packages' existing curriculum-comparator sources.
- **Statistics 0.2.0.** One lesson on censoring, a hand-checkable Kaplan-Meier table, median survival and rate/hazard ratios, with five items and four cards.
- Tests: `tests/content/test_new_geroscience_and_statistics_lessons.py` (labelling, synthetic data, no advice phrases, outcome links, link-only sources, labels unchanged).

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 150 lessons, 400 questions, 340 cards, 25 cases; 0 errors; 123 disclosed warnings (98 legacy-depth, 25 objective-coverage) |

| `python -m pytest tests -q` | 108 passed |
| `cd backend; python -m pytest -q` | 1049 passed, 2 skipped |
| `python tools/check_security.py` | 464 source files, 0 findings |
| `ruff`, `node --test` legacy, `verify.sh --frontend` (lint, unit tests including the protection label, build, bundle scan) | PASS |

Not run here: Docker Compose and the Playwright end-to-end suite. Nothing here is reviewed; the lessons were not read by a subject-matter expert, and the references were checked for existence, not for support of each sentence.

## Previous increment: homework companions, a third lab, specifications and objective items (2026-10-08)

Written by an AI coding assistant. Foundations of Cell and Molecular Biology advances from 0.18.0 to **0.19.0** and remains `partial`, unreviewed and `formative-only`. The increment adds:

- Seven open formative homework companions (Homework 2 to 8) with synthetic datasets, a recalculated CSV summary check, a graph or data-interpretation check where it fits, structured control logic, a multiple-select item and three retrieval cards each (160 practice points in total).
- A third synthetic virtual lab (week 14, lineage-marker time course, 21 practice points) with fraction-versus-count reasoning.
- Two practice items for the lesson-3 free-energy objective, which had none.
- Specification-only documents for the midterm, cumulative final and integrative project (`content/courses/cell-biology/assessment-specs/`): draft blueprints generated from `course.json`, requirements, a draft project rubric and reviewer checklists. They contain no items, keys or scoring and have not been reviewed.
- 96 practice items, one for each lesson objective that had no assessment mapping in the 24 other packages (55 numeric, 41 single choice). Every numeric key is computed in the authoring script from the numbers in its prompt, and the item feedback carries the explanation because the legacy readings are brief.
- `tools/objective_coverage.py` and the generated [gap report](COURSE_GAP_REPORT.md). It shows that no lesson objective lacks an assessment mapping or practice item, and that 91 of 101 course outcomes are still not linked from any lesson objective, which is why the validator's `objective-coverage` warning (25) is unchanged and was deliberately not silenced.
- Tests: `tests/content/test_cell_biology_integrity.py` (links resolve, every CSV key has a recalculation, example tables equal the keys, specifications hold no keys, labels unchanged, gap report current) and `backend/tests/test_authored_items.py`, which grades every public practice item against its own key and checks that a deliberately wrong answer earns nothing (688 checks, 2 symbolic items skipped).

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 140 lessons, 347 questions, 300 cards, 25 cases; 0 errors; 123 disclosed warnings (98 legacy-depth, 25 objective-coverage) |
| `python -m pytest tests -q` | 84 passed (75 before; 9 new integrity tests; inventory and schedule pins updated) |
| `cd backend; python -m pytest -q` | 936 passed, 2 skipped (248 before; the new authored-item tests) |
| `python tools/check_security.py` | 452 source files, 0 findings |
| `ruff` | clean |
| `node --test` legacy | 7 passed |
| `verify.sh --frontend` (lint, unit tests, build, bundle scan) | PASS |

Not run in this container: Docker Compose, the Playwright end-to-end suite, the production compose file. What the new material does not show: no review of any kind, no accessibility check by a person, no measured workload, no protected answer package, and no evidence that the generated synthetic datasets teach well. The practice keys are public by design.

## Previous increment: Geroscience & Regenerative Biology original lessons (2026-10-07)

Geroscience & Regenerative Biology advances to **0.2.0** and remains `partial`. Four original lessons with explicitly synthetic data follow the four preserved compact units. The package adds 15 formative items, 16 cards and 21 link-only scientific references, each checked against its PubMed title and DOI on 2026-10-07; findings are summarized qualitatively without reproducing source data. Every lesson objective now links to a course outcome. The four legacy checks are retagged to the objectives their prompts assess, and the change is recorded in each item's provenance. Every keyed answer was graded by the production grader (full credit for the key, zero for representative wrong answers, partial credit for split data-interpretation responses), and a new content test independently recalculates each numerical key from the lesson tables.

| Current command/check | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 132 lessons, 211 questions, 275 cards, 25 cases; 0 errors; 123 disclosed warnings |
| `python -m courselab.check_content ../content` | PASS: 25 packages / 215 supported practice specifications |
| `python -m pytest tests -q` | 75 passed (inventory pins updated; new geroscience recalculation test) |
| `cd backend; python -m pytest -q` | 248 passed |

## Previous increment: spaced retrieval queue and unassessed objectives (2026-10-07)

Adds Alembic revision `0008` (`card_reviews`), an append-only record of each learner self-rating with the card-text SHA-256, policy version and resulting schedule. `retrieval-schedule-v1` is deterministic and unit-tested: 10-minute relearn after `again`, then 1 day, 6 days and interval × ease for `good`; `hard`/`easy` adjust interval and ease; ease stays within 1.3–3.0 and intervals are capped at 365 days. `GET /api/v1/reviews/{course}` returns due, not-yet-reviewed and later cards for lesson-published cards only; `POST /api/v1/courses/{course}/cards/{card}/reviews` requires session, CSRF and a current enrollment. Edited card text starts a new schedule. Learner export and deletion include the new rows. The gradebook now lists authored objectives with no tagged item as `no items`; the response schema accepts that status, which the uncommitted draft omitted. Ratings do not change scores, objective evidence or grades, and no retention benefit is claimed.

| Current command/check | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 128 lessons, 196 questions, 259 cards, 25 cases; 0 errors; 123 disclosed warnings |
| `python -m pytest tests -q` (Linux dev container, Python 3.12) | 74 passed |
| `cd backend; python -m pytest -q` | 248 passed (17 new retrieval/gradebook tests, including Alembic `check` against the new metadata) |
| `ruff check backend tools tests` | PASS |
| `cd frontend; npm run lint` | PASS |
| `cd frontend; npx vitest run` | 35 passed (4 new review-queue tests) |
| `cd frontend; npm run build` | PASS |
| `python tools/check_security.py --bundle frontend/dist` | PASS; 0 findings across 424 source files |
| `npm run test:legacy` | PASS |
| Compose/Playwright E2E | Not run locally: this Linux container has no Docker engine. Hosted CI runs the Compose E2E job. |

## Previous increment: protected assessment-source boundary (2026-10-06)

Added an optional protected assessment root distinct from public course content. Graded manifests can refer to `private://` sources resolved only below the configured per-course directory; Docker Compose mounts that directory read-only for server-side use. Public/private root overlap, path traversal, file or course-directory symlink escape, absent configuration and missing files fail closed. Existing enrollment snapshots pin the source SHA-256; learner APIs omit both answer specifications and private source paths. No real answer key was added, no current course uses the private source, and all 25 packages remain formative-only. This is infrastructure for future assessed coursework, not a new graded assignment or course maturity change.

| Current command/check | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 128 lessons, 196 questions, 259 cards, 25 cases; 0 errors; 123 disclosed warnings |
| `backend/.venv/Scripts/python.exe -m pytest tests -q` | 72 passed, 2 skipped |
| `backend/.venv/Scripts/python.exe -m pytest backend/tests -q` | 229 passed, 1 skipped; one upstream Starlette/httpx deprecation warning |
| `backend/.venv/Scripts/ruff.exe check backend tools tests` | PASS |
| `cd frontend; npm run lint` | PASS |
| `cd frontend; npm test -- --run` | 31 passed |
| `cd frontend; npm run build` | PASS: TypeScript and Vite production build (206 modules) |
| `cd frontend; $env:E2E_BASE_URL='http://localhost:8080'; npm run test:e2e` | 20 passed against the final rebuilt Compose app |
| `npm run test:legacy` | 7 passed |
| `docker compose config --quiet` | PASS |
| `docker compose -f compose.production.yaml config --quiet` | PASS with documented sample environment values |
| `docker compose up --build -d --wait --wait-timeout 180` | PASS: API, database, and web healthy; existing database volume preserved |
| `docker compose exec -T api python -m courselab.check_content /content` | PASS: 25 packages / 200 supported practice specifications |
| `docker compose exec -T api alembic current` and `/api/v1/health` | PASS: `0007 (head)`; health `ok`; programming runner and LLM feedback disabled |
| Protected mount write probe in API container | PASS: mount is read-only |
| `python tools/check_security.py --bundle frontend/dist` | PASS; 0 findings across 418 source files |
| `git diff --check` | PASS |
| Hosted GitHub Actions run [37560199350](https://github.com/dylanstechmann/uniStemCourseSimulators/actions/runs/37560199350) | PASS: content/backend and frontend/E2E jobs |

The source resolver and API tests confirm the key is read only from the private mount, is not returned in course/lesson/assessment DTOs, and is not substituted from similarly named public files. A missing key blocks graded enrollment-plan creation. Symlink-escape tests are skipped because this Windows host does not permit creating test symlinks; lexical traversal and root-overlap rejection passed. No current catalog course is affected because none references a private source.

Published in commit `86188bbcba2828ae00fbade1a86cfa737e4b309c`; the hosted content/backend and frontend/E2E jobs completed successfully.

## Previous increment: Week 11 signaling-dynamics virtual lab (2026-10-06)

Foundations of Cell and Molecular Biology advances from 0.17.0 to **0.18.0** and remains `partial`. The new original 2–3 hour lab uses 120 explicitly synthetic pERK/total-ERK observations across six treatment conditions, five times, and four preparation blocks. Learners summarize 24 condition/time cells, plot 15 selected time points, calculate a vehicle-adjusted inhibitor effect, and distinguish rescue, vehicle, and pathway-control evidence. Four retrieval cards support spaced review. It is interactive formative practice; answer specifications are public, scores are ungraded, and the activity is not one of the course's three grade-bearing labs.

Validation reports 25 packages, 128 lessons, 196 questions, 259 cards, and 25 cases; there are zero errors and 123 explicitly disclosed limitation/depth warnings. The lesson and data do not use copied OCW or third-party figures/data. The public course package remains partial: the eight graded homework sets, one remaining lab, summative midterm/final, cumulative project, measured workload, complete objective coverage, and independent scientific/accessibility review are unfinished. Public practice answer specifications are not protected exam keys.

| Current command/check | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 128 lessons, 196 questions, 259 cards, 25 cases; 0 errors; 123 disclosed warnings |
| `backend/.venv/Scripts/python.exe -m pytest tests/content/test_content_validation.py -q` | 67 passed, 1 skipped |
| `backend/.venv/Scripts/python.exe -m pytest tests -q` | 69 passed, 1 skipped |
| `cd backend; .venv/Scripts/python.exe -m pytest tests -q` | 226 passed; one upstream Starlette/httpx deprecation warning |
| `cd backend; .venv/Scripts/ruff.exe check .` | PASS |
| `cd frontend; npm run lint` | PASS |
| `cd frontend; npm test -- --run` | 31 passed |
| `cd frontend; npm run build` | PASS: TypeScript and Vite production build (206 modules) |
| `cd frontend; $env:E2E_BASE_URL='http://localhost:8080'; npm run test:e2e` | 20 passed, including the Week 11 summary upload, plot, calculation, controls, and practice-only gradebook status |
| `npm run test:legacy` | 7 passed |
| `docker compose up --build -d --wait --wait-timeout 180` | PASS: API, database, and web healthy; existing data volume preserved |
| `docker compose exec -T api python -m courselab.check_content /content` | PASS: 25 packages / 200 supported practice specifications |
| `docker compose exec -T api alembic current` and `/api/v1/health` | PASS: `0007 (head)`; health `ok` |
| `python tools/check_security.py --bundle frontend/dist` | PASS; 0 findings across 417 source files |
| `git diff --check` | PASS |
| Hosted GitHub Actions run `37555835879` | PASS: content/backend and frontend/E2E jobs |

The existing grader interface limited attempts to 20 fields, below the maximum 40 coordinates from a 20-point plot. It now accepts up to 40 fields, with regression coverage for the boundary; graph component totals use stable summation so full credit returns exactly the configured point value. The new Playwright journey validates the data-analysis flow against the live local Compose app. No arbitrary learner code is executed by this lab.

Published at commit `93f97ea1a4b9cfb973df34aa78831e39bfb0551a`; [hosted GitHub Actions run `37555835879`](https://github.com/dylanstechmann/uniStemCourseSimulators/actions/runs/37555835879) completed successfully, with both content/backend and frontend/E2E jobs passing.

## Previous increment: Week 3 open formative homework companion (2026-10-06)

Foundations of Cell and Molecular Biology advanced from 0.16.0 to **0.17.0** and remains `partial`. Week 3 includes an original 2–3 hour homework companion on protein trafficking, localization and fractionation evidence. It pairs a 12-preparation synthetic M6P-receptor dataset with five deterministic public practice items: a CSV summary, fixed-axis plot, signed contrast with a bounded inference, structured control/rescue reasoning, and route/topology multiple select. Four CC BY 4.0 retrieval cards reinforce assay limits. The autograder checks summary cells and selected structured responses; it does not grade prose, test uncertainty inference, or establish mechanism. All answer specifications are visible in this public repository, the activity is explicitly ungraded, and it does not count as one of eight required graded homework sets.

Validation at that increment reported 25 packages, 127 lessons, 192 questions, 255 cards and 25 cases, with zero errors and 123 disclosed limitation/depth warnings. Its root suite passed 68 tests with 1 skipped; backend passed 224 with the upstream Starlette/httpx deprecation warning; frontend unit tests passed 31; Playwright passed 19; and legacy migration tests passed 7. The published increment at commit `708dd2ca88f7e187afa333a4758f56e4d449fc44` passed [hosted GitHub Actions run `37551413785`](https://github.com/dylanstechmann/uniStemCourseSimulators/actions/runs/37551413785): both content/backend and frontend/E2E jobs completed successfully.

## Previous increment: first interactive data-analysis lab (2026-10-06)

Foundations of Cell and Molecular Biology advanced from 0.15.0 to **0.16.0** and remains `partial`. Week 5 now includes the first authored lab in the proposed three-activity sequence: an original 2–3 hour virtual fluorescence-data-analysis lesson, eight-row synthetic CSV, instructor rubric, and four-question formative assessment worth 13 ungraded practice points. The learner uploads per-condition counts/means, plots batch-level percentages on fixed axes, interprets imaging controls, and reports a descriptive 9-percentage-point contrast. An API change allows `lab`-typed practice assessments to use the existing answer-free, enrollment-version-pinned endpoint, still restricted to explicitly public formative items. This package does not supply microscope images, simulate equipment, execute wet-lab procedures, grade prose, or count toward a course grade.

Validation passes for 25 packages, 126 lessons, 187 questions, 251 cards, and 25 cases, with 0 errors and 123 disclosed limitation/depth warnings. The complete root suite passed **67 tests with 1 skipped**; backend passed **224** with one upstream Starlette/httpx deprecation warning; frontend unit tests passed **31**; Playwright passed **18**; and legacy-state tests passed **7**. The new browser flow opens the lab in the course reader, opens its typed lab assessment from the practice gradebook, submits a CSV summary, plots both condition means, scores four evidence choices, and checks the 9-point value. Compose rebuilt while preserving the existing database volume; API, database, and web are healthy; Alembic is `0007 (head)`; and the integration validator supports 191 practice specifications. The answer-free public DTO boundary test passes; authoring keys remain explicitly public formative practice, and no secure exam key was added. Frontend lint/format and production build pass (206 modules), Ruff passes, `git diff --check` passes, and the security-boundary scan reports 0 findings across 413 source files.

| Current command/check | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 126 lessons, 187 questions, 251 cards, 25 cases; 0 errors; 123 disclosed warnings |
| `backend/.venv/Scripts/python.exe -m pytest tests -q` | 67 passed, 1 skipped |
| `cd backend; .venv/Scripts/python.exe -m pytest -q` | 224 passed; one upstream Starlette/httpx deprecation warning |
| `cd backend; .venv/Scripts/ruff.exe check .` | PASS |
| `cd frontend; npm test -- --run` | 31 passed |
| `cd frontend; npm run lint; npm run build` | PASS: formatting/lint and TypeScript/Vite production build (206 modules) |
| `cd frontend; $env:E2E_BASE_URL='http://localhost:8080'; npm run test:e2e` | 18 passed, including upload, fixed-axis plot, and structured lab practice |
| `npm run test:legacy` | 7 passed |
| `docker compose up --build -d --wait --wait-timeout 180` | PASS: API, database, and web healthy; existing data volume preserved |
| `docker compose exec -T api python -m courselab.check_content /content` | PASS: 25 packages / 191 supported practice specifications |
| `docker compose exec -T api alembic current` and `/api/v1/health` | PASS: `0007 (head)`; health `ok` |
| `python tools/check_security.py --bundle frontend/dist` | PASS; 0 findings across 413 source files |

The eight homework sets, two remaining lab activities, summative midterm/final, cumulative project, measured workload, comprehensive objective coverage, and independent scientific/accessibility reviews remain incomplete. The course stays partial; the virtual lab does not satisfy the missing homework, exams, or capstone.

After the current browser suite, the local synthetic database remained at 82 users, 82 enrollments, 90 attempts, and 6 progress records. The lab increment was published at commit `f485075f025e7bd97d4562ed62d1cf82cb49c79e`; [hosted GitHub Actions run `37547670931`](https://github.com/dylanstechmann/uniStemCourseSimulators/actions/runs/37547670931) completed successfully. Week 12 passed hosted run `37540473521`. Week 14 was published at commit `a372fb31eb1d706ddc94f5e09a9c81266ad82629`; hosted run `37544794562` completed successfully.

## Previous increment: week-14 potency and integrative study design (2026-10-06)

Version 0.15.0 added two original lessons on developmental potency/lineage evidence and integrative regenerative experiment design; six mapped objectives; seven deterministic public formative questions worth 13 practice points; four retrieval cards; misconception entries; layered feedback; and link-only curriculum/scientific/ethics sources. Explicitly synthetic examples support a 22.5% construct-fraction calculation and a 13-percentage-point descriptive contrast. The lesson bounds marker identity, function, uncertainty, and translational claims; it is not a complete capstone or graded coursework. It was published at commit `a372fb31eb1d706ddc94f5e09a9c81266ad82629`; hosted run `37544794562` completed successfully.

## Previous increment: week-13 cell-cycle and cell-fate evidence (2026-10-06)

Week 13 advanced the package to 0.14.0 with two original lessons, six objectives, seven formative items (13 points), four retrieval cards, five misconception entries, and six link-only sources. Synthetic cell-cycle and cell-state data supported reasoning about DNA-content, EdU, mitotic, recovery, senescence-associated, and apoptosis measurements. The increment passed its then-current tests and was published at commit `dd7a7ff06805dd0cd5e333df109783d5c7d6c95e`; its GitHub Actions status was not available from the combined-status check.

## Previous increment: week-12 cytoskeleton, matrix, and mechanobiology (2026-10-06)

Week 12 advanced the package to version 0.13.0 with two original lessons, six objectives, seven formative questions, four retrieval cards, a synthetic hydrogel-mechanics dataset, and link-only sources. Its 64-pass/1-skip root suite, 223 backend tests, 31 frontend tests, 15 browser tests, 407-file security scan, 173-specification integration check, and healthy Compose stack passed. Hosted Actions run `37540473521` completed successfully for commit `2f0fb1c66d4e40fe2c4efa462643b6c9750f00ea`.

## Previous increment: week-10 inheritance and variant evidence (2026-10-06)

Foundations of Cell and Molecular Biology advanced from 0.10.0 to **0.11.0** and remains `partial`. Week 10 adds two original lessons on inheritance/penetrance and variant-to-phenotype evidence; six mapped learning objectives; seven deterministic public formative questions worth 13 practice points; four retrieval cards; four misconception entries; layered feedback for pedigree and variant interpretation; and link-only source records for MIT OCW and NCBI Bookshelf references. Synthetic isogenic-edit data are labeled as teaching data. The new numerical answer distinguishes transmission probability from phenotype probability (50% × 80% penetrance = 40%); the evidence lesson distinguishes a predicted molecular effect from demonstrated pathogenicity. The practice set is not graded coursework. No homework set, virtual lab, midterm, final, or project is claimed complete.

Content validation passes for 25 packages, 117 lessons, 155 questions, 235 cards, and 25 cases, with 0 errors and 123 disclosed depth/objective warnings. The focused content regression set passed 5 tests; the complete root suite passed **62 tests with 1 skipped**, backend passed **223**, frontend unit tests passed **31**, Playwright passed **13**, and legacy-state tests passed **7**. Docker Compose rebuilt successfully; the API, database, and web services are healthy; existing database data was preserved; Alembic remains at `0007 (head)`; and `/api/v1/health` reports `ok`. The learner integration validator supports 159 practice specifications. The new browser journey enrolled a guest, opened the week-10 set, submitted the penetrance calculation and structured isogenic-data response, and verified deterministic feedback. Frontend lint/format and production build pass (206 modules), Ruff passes, and the security-boundary scan reports 0 findings across 403 source files. The prior week-9 GitHub Actions run completed successfully; week-10 CI will run on publication. All authored answers remain explicitly public practice specifications; no exam key was added.

| Current command/check | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 117 lessons, 155 questions, 235 cards, 25 cases; 0 errors; 123 disclosed warnings |
| `backend/.venv/Scripts/python.exe -m pytest tests -q` | 62 passed, 1 skipped |
| `cd backend; .venv/Scripts/python.exe -m pytest tests -q` | 223 passed; one upstream Starlette/httpx deprecation warning |
| `cd backend; .venv/Scripts/ruff.exe check .` | PASS |
| `cd frontend; npm test -- --run` | 31 passed |
| `cd frontend; npm run lint; npm run build` | PASS: formatting/lint and TypeScript/Vite production build (206 modules) |
| `cd frontend; npm run test:e2e` | 13 passed, including week-10 numeric and structured practice submission |
| `npm run test:legacy` | 7 passed |
| `docker compose up --build -d --wait --wait-timeout 180` | PASS: API, database, and web healthy; existing data volume preserved |
| `docker compose exec -T api python -m courselab.check_content /content` | PASS: 25 packages / 159 supported practice specifications |
| `docker compose exec -T api alembic current` and `/api/v1/health` | PASS: `0007 (head)`; health `ok` |
| `python tools/check_security.py --bundle frontend/dist` | PASS; 0 findings across 403 source files |

The eight homework packages, three full data/virtual-lab activities, summative midterm/final, integrative project, measured workload, comprehensive objective coverage, and independent scientific/accessibility reviews remain incomplete. Weeks 11–14 are still outlines and the course remains partial.

## Previous increment: week-9 RNA processing and protein regulation (2026-10-06)

Foundations of Cell and Molecular Biology advanced from 0.9.1 to **0.10.0** and remains `partial`. Week 9 adds two original lessons on RNA processing/isoform evidence and translation/protein turnover; six mapped learning objectives, each tagged to at least one practice item; original, explicitly synthetic RNA and protein datasets; eight deterministic public formative questions (14 points, including seeded variants); four retrieval cards; five misconception entries; layered instructor-style feedback; and link-only provenance for MIT OCW and NCBI Bookshelf references. The practice set is not graded coursework. No homework set, virtual lab, midterm, final, or project is claimed complete.

Content validation passes for 25 packages, 115 lessons, 148 questions, 231 cards, and 25 cases, with 0 errors and 123 disclosed depth/objective warnings. The focused content regression set passed 6 tests; the complete root suite passed **61 tests with 1 skipped**, backend passed **223**, frontend unit tests passed **31**, Playwright passed **12**, and legacy-state tests passed **7**. The CI content check and development Compose build passed; the API integration validator supports 152 practice specifications. Compose API, database, and web are healthy; existing database data was preserved, Alembic remains at `0007 (head)`, and the health endpoint reports `ok`. The new browser journey enrolled a guest, opened the week-9 set, submitted a numeric isoform fraction and a structured synthesis/turnover response, and verified deterministic feedback. The existing public DTO boundary test still passes. Frontend lint/format and production build pass (206 modules); Ruff passes. The security-boundary scan reports 0 findings across 401 source files. All authored answers remain explicitly public practice specifications; no exam key was added.

| Current command/check | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 115 lessons, 148 questions, 231 cards, 25 cases; 0 errors; 123 disclosed warnings |
| `backend/.venv/Scripts/python.exe -m pytest tests -q` | 61 passed, 1 skipped |
| `cd backend; .venv/Scripts/python.exe -m pytest tests -q` | 223 passed; one upstream Starlette/httpx deprecation warning |
| `cd backend; .venv/Scripts/ruff.exe check .` | PASS |
| `cd frontend; npm test -- --run` | 31 passed |
| `cd frontend; npm run lint; npm run build` | PASS: formatting/lint and TypeScript/Vite production build (206 modules) |
| `cd frontend; npm run test:e2e` | 12 passed, including week-9 numeric and structured practice submission |
| `npm run test:legacy` | 7 passed |
| `docker compose up --build -d --wait --wait-timeout 180` | PASS: API, database, and web healthy; existing data volume preserved |
| `docker compose exec -T api python -m courselab.check_content /content` | PASS: 25 packages / 152 supported practice specifications |
| `docker compose exec -T api alembic current` and `/api/v1/health` | PASS: `0007 (head)`; health `ok` |
| `python tools/check_security.py --bundle frontend/dist` | PASS; 0 findings across 401 source files |

The eight homework packages, three full data/virtual-lab activities, summative midterm/final, integrative project, measured workload, comprehensive objective coverage, and independent scientific/accessibility reviews remain incomplete. Weeks 10–14 are still outlines and the course remains partial.

## Previous increment: week-8 cumulative practice set (2026-10-06)

Foundations of Cell and Molecular Biology advanced from 0.9.0 to **0.9.1** and remains `partial`. Week 8 now contains a self-paced 12-question cumulative practice set spanning selected outcomes from weeks 1–7. It reuses the existing openly answer-bearing formative bank, totals 31 practice points, provides immediate per-question feedback, and is explicitly labeled **ungraded and not a midterm** in the syllabus, schedule, UI, README, and crosswalk. No summative exam, protected exam key, homework sequence, or new lesson was created.

The new learner endpoint requires enrollment and an assessment pinned to the selected package version. It accepts only `type: practice`, `mode: practice` records sourced from `question-banks/practice.json`; it verifies the pinned SHA-256, checks every referenced item is explicitly marked public formative practice, verifies the point total, and returns only whitelisted question DTOs. Restricted visibility, source mutation, incorrect type/source, and unknown assessment IDs fail closed. Seeded variants keep their signed course/version/question token. The course-level gradebook UI opens these practice sets and submits through the existing immutable formative-attempt workflow. The repository's authored answer specifications remain public by design and are not secure exam content.

Validation on 2026-10-06: root suite **59 passed, 1 skipped**; backend **223 passed**; frontend **31 passed**; Playwright **11 passed**; legacy-state **7 passed**. Content validation reports 25 packages, 113 lessons, 140 questions, 227 cards, and 25 cases with 0 errors and 123 explicitly disclosed depth/objective warnings. API/content integration passes for 25 packages and 142 supported practice specifications. The source/bundle security scan reports 0 findings across 399 files. Frontend lint/format and TypeScript/Vite production build pass (206 modules). Development Compose is healthy, with existing data volumes preserved; Alembic remains at `0007 (head)` and `/api/v1/health` is healthy.

| Current command/check | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 113 lessons, 140 questions, 227 cards, 25 cases; 0 errors; 123 disclosed warnings |
| `backend/.venv/Scripts/python.exe -m pytest tests -q` | 59 passed, 1 skipped |
| `cd backend; .venv/Scripts/python.exe -m pytest tests -q` | 223 passed; one upstream Starlette/httpx deprecation warning |
| `cd backend; .venv/Scripts/ruff.exe check .` | PASS |
| `cd frontend; npm test` | 31 passed |
| `cd frontend; npm run lint` and `npm run build` | PASS: formatting/lint and production bundle (206 modules) |
| `cd frontend; npm run test:e2e` | 11 passed, including version-pinned week-8 practice, per-question grading, and reload persistence |
| `npm run test:legacy` | 7 passed |
| `docker compose up --build -d --wait --wait-timeout 180` | PASS: database, API, and web healthy; existing volumes preserved |
| `docker compose exec -T api python -m courselab.check_content /content` | PASS: 25 packages / 142 supported practice specifications |
| `docker compose exec -T api alembic current` | PASS: `0007 (head)` |
| `python tools/check_security.py --bundle frontend/dist` | PASS; 0 findings across 399 files |

The dedicated browser journey enrolled as a guest, opened the week-8 practice set, submitted a formative response, saw feedback, reloaded, reopened the set, and saw the saved feedback. An axe WCAG 2.1 A/AA scan on the loaded practice view reported zero violations. No summative-exam flow exists to test.

## Previous increment: week-7 chromatin and transcription (2026-10-06)

Foundations of Cell and Molecular Biology advanced from 0.8.0 to **0.9.0** and remains `partial`. Week 7 adds two original developed lessons, seven deterministic formative questions, four retrieval cards, seven misconception entries, two feedback templates, mapped lesson objectives, and per-module source provenance. The short gene-expression prototype remains supplementary. Accessibility/RNA, ChIP-qPCR, and reporter examples use explicitly synthetic data. The lessons separate input, IgG/mock, positive/negative-locus, and no-template controls and distinguish chromatin accessibility, occupancy, reporter activity, direct binding, and endogenous causal evidence.

The proposed teaching block now runs through week 7; week 8 is reserved for a proposed midterm and retrieval consolidation. No week-8 exam questions, answer key, rubric, assessment record, release policy, dates, or deadlines exist. Weeks 9–14 remain outlines. The repository inventory is 25 packages, 113 lessons, 140 formative questions, 227 retrieval cards, and 25 self-assessed cases. All packages remain partial and no external reviewer is claimed.

Validation on 2026-10-06: **327 tests passed and 1 skipped** across root (59 passed, 1 skipped), backend (221), frontend unit tests (30), Playwright (10), and legacy storage (7). Content validation reports 25 packages, 113 lessons, 140 questions, 227 cards, and 25 cases: 0 errors and 123 disclosed depth/objective warnings (98 legacy-depth, 25 objective-coverage). The API/content integration check passes for 25 packages and 142 supported practice specifications. The source/bundle security-boundary scan reports 0 findings across 397 files. Frontend lint/format and the TypeScript/Vite production build passed (205 modules). Rebuilt development Compose services are healthy, Alembic is `0007 (head)`, and `/api/v1/health` is `ok`; programming and LLM providers remain disabled. Existing database/credential volumes were preserved. Playwright now submits and grades week-7 chromatin, ChIP percent-input/control, and reporter items; the answer-specification boundary test passed.

| Current command/check | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 113 lessons, 140 questions, 227 cards, 25 cases; 0 errors; 123 disclosed warnings |
| `backend/.venv/Scripts/python.exe -m pytest tests -q` | 59 passed, 1 skipped |
| `cd backend; .venv/Scripts/python.exe -m pytest -q` | 221 passed; one upstream Starlette/httpx deprecation warning |
| `cd backend; .venv/Scripts/ruff.exe check .` | PASS |
| Frontend `npm run lint`, `npm test -- --run`, and `npm run build` | PASS: 30 unit tests, TypeScript build, 205 production modules |
| `npm run test:e2e` against rebuilt Compose | 10 passed, including week-7 lesson submissions and answer-specification DTO exclusion |
| `npm run test:legacy` | 7 passed |
| `docker compose exec -T api python -m courselab.check_content /content` | PASS: 25 packages / 142 supported practice specifications |
| `docker compose exec -T api alembic current` and `/api/v1/health` | PASS: `0007 (head)`; health `ok`; programming runner and LLM feedback disabled |
| `docker compose up --build -d --wait --wait-timeout 180` | PASS: database, API, and web healthy; existing volumes preserved |
| `python tools/check_security.py --bundle frontend/dist` | PASS; 0 findings across 397 files |
| `git diff --check` | PASS |

New source records link to MIT OCW 7.28x as a curriculum comparator and to NCBI Bookshelf, Haring et al.'s CC BY 2.0 ChIP-qPCR methods article, and ENCODE standards as references. The project uses links/citations only and redistributes none of their text, figures, tables, or data. Live-link probing was not repeated; the prior report records two JHU pages that return HTTP 403 to the automated client.

## Previous increment: week-6 DNA replication and repair

Foundations of Cell and Molecular Biology advanced from version 0.7.0 to **0.8.0** while remaining `partial`. Week 6 adds two original lessons, seven deterministic formative items, four retrieval cards, misconception entries, two feedback templates, objective mappings, and per-module provenance. The lessons address strand polarity and replication, model-discriminating density predictions, lesion-specific repair candidates, and interpretation limits for perturbation and rescue evidence. The UV lesion-signal series is explicitly synthetic; it is not presented as historical measurements, mutation frequency, or proof of direct catalysis.

MIT OCW 7.28x Molecular Biology is a link-only curriculum comparator. Meselson and Stahl (1958) and NCBI Bookshelf replication/repair chapters are link-only scientific references. The instructional prose and questions are original; no source text, figures, table, or dataset was copied. All packages remain partial and no reviewer is fabricated.

The inventory is 25 packages, 111 lessons, 133 formative questions, 223 retrieval cards, and 25 self-assessed cases. Weeks 1–6 now have two developed lessons each; week 4 retains its short prototype capsule and week 7 has one compact gene-expression reading. Weeks 8–14 remain outlines. Eight homework sets, three full data/lab activities, midterm, cumulative final, integrative project, measured workload, and independent academic/accessibility review remain unfinished.

Validation on 2026-10-06: **326 tests passed and 1 skipped** across root (58 passed, 1 skipped), backend (221), frontend unit tests (30), Playwright (10), and legacy storage (7). Content-authoring tests passed (56, 1 skipped). Frontend lint/format and TypeScript/Vite build passed (205 modules). Content validation reports 25 packages, 111 lessons, 133 questions, 223 cards, and 25 cases: 0 errors and 123 disclosed depth/objective warnings (98 legacy-depth, 25 objective-coverage). The API/content integration check passes for 25 packages and 135 supported practice specifications. The security-boundary scan reports 0 findings across 396 files. Rebuilt development Compose services are healthy, Alembic is `0007 (head)`, and `/api/v1/health` is `ok`; programming and LLM providers remain disabled. Existing database volumes were preserved.

| Current command/check | Result |
| --- | --- |
| `uv run --with jsonschema python tools/validate_content.py` | PASS: 25 packages, 111 lessons, 133 questions, 223 cards, 25 cases; 0 errors; 123 disclosed warnings |
| `uv run --project backend --with pytest --with ruff --with jsonschema python -m pytest tests -q` | 58 passed, 1 skipped |
| `docker compose run --rm --no-deps api pytest -q -p no:cacheprovider` | 221 passed; upstream Starlette/httpx and Python `datetime.utcnow()` deprecation warnings |
| Frontend `npm run lint`, `npm run test`, and `npm run build` | PASS: lint/format, 30 unit tests, TypeScript build and 205 production modules |
| Playwright `npm run test:e2e` against rebuilt Compose | 10 passed, including week-6 replication/repair submissions and deterministic feedback; guest enrollment, saved progress, and answer-key DTO boundary |
| `docker compose exec -T api python -m courselab.check_content /content` | PASS: 25 packages / 135 supported practice specifications |
| Compose health and migration | PASS: database, API, and web healthy; Alembic `0007 (head)`; API health `ok` |
| `python tools/check_security.py --bundle frontend/dist` | PASS; 0 security-boundary findings across 396 files |

Ruff (`backend/courselab`, `backend/tests`, and `tests`) and `git diff --check` passed. Link reachability was not re-run: the previous report records two JHU public pages returning HTTP 403 to the automated client. This does not affect offline schema/content validation.

## Previous increment: week-5 cell measurement and fractionation

Foundations of Cell and Molecular Biology advanced from version 0.6.0 to **0.7.0** while remaining `partial`. Week 5 adds two original lessons: conventional-light microscopy resolution, sampling, contrast, labeling controls, and colocalization limits; then differential fractionation, marker recovery, contamination, and bounded localization claims. Six deterministic practice items cover a resolution estimate, confocal contrast, colocalization inference, marker recovery, structured fraction analysis, and multi-marker design. Four spaced-retrieval cards, five misconception entries, two feedback templates, objective mappings, and source/license records were added. The bead-pair and marker-panel data are explicitly synthetic teaching data.

MIT OCW 7.016 Lecture 29 is linked as a curriculum comparator. Waters (2009), Claude (1946), and the NCBI Bookshelf methods chapter are link-only scientific or methods references. No lecture, article, chapter, figure, or data was copied or adapted. The course has no external reviewer and its review status remains unreviewed.

Weeks 1–5 now each have two developed lessons; week 4 retains its compact prototype capsule. Week 7 remains one compact gene-expression reading, and weeks 6 and 8–14 remain outlines without authored instructional sequences. The eight proposed homework sets, three full data/lab assignments, midterm, cumulative final, and integrative project are not present. All 126 practice questions are formative; the package has no course grade, semester-equivalence, credit, or prerequisite-equivalency claim. All 25 course packages remain partial; none meets the complete-course standard.

Validation on 2026-10-06: **325 tests passed and 1 skipped** across root (57 passed, 1 skipped), backend (221), frontend unit tests (30), Playwright (10), and legacy storage (7). Frontend lint/format and TypeScript/Vite build passed (205 modules). Content validation reports 25 packages, 109 lessons, 126 questions, 219 cards, and 25 cases: 0 errors and 123 disclosed depth/objective warnings (98 legacy-depth, 25 objective-coverage). The API/content check passes for 25 packages and 128 supported practice specifications. Ruff and `git diff --check` pass. The source/bundle security-boundary scan reports 0 findings across 393 files. Rebuilt development Compose services are healthy, Alembic is `0007 (head)`, and `/api/v1/health` is `ok`; programming and LLM providers remain disabled. Existing database volumes were preserved.

| Week-5 command/check | Result |
| --- | --- |
| `uv run --with jsonschema --with pytest python tools/validate_content.py` | PASS: 25 packages, 109 lessons, 126 questions, 219 cards, 25 cases; 0 errors; 123 disclosed warnings |
| `uv run --with jsonschema --with pytest python -m pytest tests -q` | 57 passed, 1 skipped |
| Backend pytest suite | 221 passed; one upstream Starlette/httpx deprecation warning |
| Frontend lint/format, Vitest, and Vite build | PASS: 30 unit tests; 205 production modules |
| Playwright against the rebuilt Compose stack | 10 passed, including week-5 numeric units, fraction rubric, saved progress, and answer-key DTO boundary |
| `docker compose exec -T api python -m courselab.check_content /content` | PASS: 25 packages / 128 supported practice specifications |
| Compose health and migration | PASS: database, API, and web healthy; Alembic `0007 (head)`; API health `ok` |
| Ruff, `git diff --check`, and `python tools/check_security.py --bundle frontend/dist` | PASS; 0 security-boundary findings across 393 files |

## Previous increment: week-4 enzyme mechanisms and kinetic inference

Foundations of Cell and Molecular Biology advanced from version 0.5.0 to **0.6.0** while remaining `partial`. Week 4 now has two substantial original lessons alongside the retained short prototype capsule: catalytic mechanisms/free-energy coupling, then initial-rate fitting and reversible-inhibitor patterns. Six new deterministic formative items cover equilibrium, coupled ΔG, Vmax at Km, model-based rate prediction, inhibitor-pattern/assay controls, and Km versus binding affinity. Four retrieval cards, misconception entries, layered-feedback templates, source records and independent numerical recalculation tests were added. The inhibitor table is explicitly synthetic and is not presented as published data.

The scope comparator is MIT OCW 5.07SC Biological Chemistry I, whose undergraduate Module I includes sessions on enzyme catalysis and enzyme kinetics/inhibition; it is linked only. Briggs and Haldane (1925) and Johnson and Goody (2011) are linked as research references. No source text, figure, problem, or dataset was copied or adapted. The course remains unreviewed.

Weeks 1–4 now each have two developed lessons; week 4 retains one additional compact prototype reading. Week 7 still has one compact gene-expression capsule; weeks 5–6 and 8–14 remain without authored lesson sequences. The eight proposed homework sets, three data/lab activities, midterm, cumulative final and integrative project are still absent. All 120 questions remain formative; no course grade or semester-equivalence claim is enabled.

Validation on 2026-10-06: root **54 passed, 1 skipped**; backend **221 passed** (one upstream Starlette/httpx deprecation warning); frontend **30 unit tests passed**, lint/format and TypeScript/Vite build passed (205 modules); Playwright **10 passed**, including enrollment, week-4 lesson reading, numeric unit checks, inhibitor rubric scoring and saved feedback; legacy storage tests **7 passed**. Content validation reports 25 packages, 107 lessons, 120 questions, 215 cards and 25 cases: 0 errors and 123 explicit depth/objective warnings (98 legacy-depth, 25 objective-coverage). The API/content check passes for 25 packages and 122 supported practice specifications. Ruff and `git diff --check` pass. Source and bundle security-boundary scans found 0 issues across 391 files. Rebuilt Compose services are healthy, Alembic is `0007 (head)`, and `/api/v1/health` is `ok`; programming and LLM providers remain disabled. Existing database volumes were preserved.

| Command/check | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 107 lessons, 120 questions, 215 cards, 25 cases; 0 errors; 123 disclosed depth/objective warnings |
| `python -m pytest tests/content -q` | 54 passed, 1 skipped |
| `cd backend; python -m pytest tests -q` | 221 passed; 1 upstream deprecation warning |
| `ruff check backend tools tests`; `git diff --check` | PASS |
| Frontend `npm run lint`, `npm test -- --run`, `npm run build` | PASS; 30 unit tests; 205 modules built |
| `npm run test:e2e` against `http://localhost:8080` | 10 passed, including week-4 numerical and structured-inference submissions |
| `node tests/legacy/state.test.mjs` | 7 passed |
| `python -m courselab.check_content ../content` | PASS: 25 packages / 122 supported practice specifications |
| `python tools/check_security.py` and `python tools/check_security.py --bundle frontend/dist` | PASS: 391 files, 0 findings |
| `docker compose up --build -d --wait --wait-timeout 180`; Alembic and health queries | PASS: database, API, and web healthy; `0007 (head)`; health `ok` |

These checks verify the current software paths and authored package structure; they do not establish full-course quality, mastery, course-level human grading, or institutional equivalency.

## Previous increment: cell-biology weeks 1–3 and trafficking lessons

Foundations of Cell and Molecular Biology advanced from version 0.4.0 to **0.5.0** while remaining `partial`. Week 3 now has two substantial original lessons: organelle compartments and protein targeting, followed by protein sorting and vesicle traffic. Both lessons include worked reasoning, explicitly synthetic experimental datasets, controls, limits on causal inference, formative questions and retrieval cards. The source map links one MIT OCW scope comparator and five primary articles as link-only references; no source text, figure or data was adapted. The source schema and validator now distinguish link-only research references and prohibit treating them as adaptation permissions.

The syllabus and assessment crosswalk now identify weeks 1–3 as the only weeks with two developed lessons each. Week 4 and week 7 remain short capsules; weeks 5–6 and 8–14 remain unauthored. The course still lacks the planned eight homework sets, three laboratory/data activities, midterm, cumulative final and integrative project. All 114 practice questions remain formative, and no course grade is awarded. The course remains unreviewed and has no external reviewer. This increment does not establish semester equivalence.

Validation on 2026-10-06: root **53 passed, 1 skipped**; backend **221 passed** (one upstream Starlette/httpx deprecation warning); frontend **30 unit tests passed**, lint/format and TypeScript/Vite build passed (205 modules); Playwright **10 passed**; legacy storage tests **7 passed**. Content validation reports 25 packages, 105 lessons, 114 questions, 211 cards and 25 cases: 0 errors and 123 explicit depth/objective warnings (98 legacy-depth, 25 objective-coverage). The API/content check passes for 25 packages and 116 supported practice specifications. Ruff passes. Source and bundle security-boundary scans found 0 issues across 389 files. Rebuilt Compose services are healthy, Alembic is `0007 (head)`, and `/api/v1/health` is `ok`; programming and LLM providers remain disabled. Existing database volumes were preserved.

| Command/check | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 105 lessons, 114 questions, 211 cards, 25 cases; 0 errors; 123 disclosed depth/objective warnings |
| `python -m pytest tests/content -q` | 53 passed, 1 skipped |
| `cd backend; python -m pytest tests -q` | 221 passed; 1 upstream deprecation warning |
| `ruff check backend tools tests`; `git diff --check` | PASS |
| Frontend `npm run lint`, `npm test -- --run`, `npm run build` | PASS; 30 unit tests; 205 modules built |
| `npm run test:e2e` against `http://localhost:8080` | 10 passed, including week 3 lessons/practice and answer-key exposure checks |
| `node tests/legacy/state.test.mjs` | 7 passed |
| `python -m courselab.check_content ../content` | PASS: 25 packages / 116 supported practice specifications |
| `python tools/check_security.py` and `python tools/check_security.py --bundle frontend/dist` | PASS: 389 files, 0 findings |
| `docker compose up --build -d --wait --wait-timeout 180`; Alembic and health queries | PASS: database, API, and web healthy; `0007 (head)`; health `ok` |

These checks confirm current application paths and authored package structure. They do not establish full-course quality, a security audit, course-level human grading, workload, mastery, or institutional equivalency.

## Previous increment: cell-biology scope and the first two developed weeks

Foundations of Cell and Molecular Biology advanced from version 0.3.2 to **0.4.0** without changing its `partial` maturity. The manifest and syllabus now record a proposed 14-week undergraduate scope and an outcome-to-assessment crosswalk. Weeks 1 and 2 contain four original, substantial readings (about 700–790 words each), with worked biochemical and membrane-transport examples. Weeks 4 and 7 retain brief enzyme and gene-expression capsules; weeks 3, 5–6, and 8–14 have no authored lessons. The 14-week plan is not 14 weeks of instruction and does not establish semester equivalence.

The initial weeks add explicit lesson objectives linked to the four intended course outcomes, four original deterministic practice items, four retrieval cards, a focused misconception catalog, and instructor-style feedback templates. A new Playwright flow opens the pH, protein-variant, and membrane-transport lessons, submits the associated practice responses, and checks the returned scores. All questions remain formative; solution specifications are public practice material and no live package awards a course grade. The content remains unreviewed. The proposed eight homework sets, three lab/data activities, midterm, cumulative final, and integrative project are not authored or enabled. Workload has not been measured.

New teaching text is original and under the repository's CC BY 4.0 content license. MIT OCW 7.01SC Fundamentals of Biology and 7.28x Molecular Biology are linked as curriculum comparators only; no text, figure, problem, or exam was copied or adapted. The sources are the [MIT 7.01SC syllabus](https://ocw.mit.edu/courses/7-01sc-fundamentals-of-biology-fall-2011/pages/syllabus/) and [MIT OCW terms](https://ocw.mit.edu/pages/privacy-and-terms-of-use/); the terms' license does not clear third-party assets or imply MIT endorsement.

Validation on 2026-10-06: root **54 passed, 1 skipped**; backend **221 passed** (one upstream Starlette/httpx deprecation warning); frontend **30 unit tests passed**, lint/format and TypeScript/Vite build passed (205 modules); Playwright **10 passed**; legacy storage tests **7 passed**. Content validation reports 25 packages, 103 lessons, 110 questions, 207 cards, and 25 cases: 0 errors and 123 explicit depth/objective warnings (98 legacy-depth, 25 objective-coverage). The API/content check passes for 25 packages and 112 supported practice specifications. Ruff passes. Source and bundle security-boundary scans found 0 issues across 387 files. Rebuilt Compose services are healthy, Alembic is `0007 (head)`, and `/api/v1/health` is `ok`; programming and LLM providers remain disabled. Existing database volumes were preserved.

Both GitHub Actions jobs passed after the browser assertion was narrowed to the reader's level-one heading in [run 37516239260](https://github.com/dylanstechmann/uniStemCourseSimulators/actions/runs/37516239260).

| Command/check | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 103 lessons, 110 questions, 207 cards, 25 cases; 0 errors; 123 disclosed depth/objective warnings |
| `python -m pytest tests -q` | 54 passed, 1 skipped |
| `cd backend; python -m pytest tests -q` | 221 passed; 1 upstream deprecation warning |
| `ruff check backend tools tests` | PASS |
| Frontend `npm run lint`, `npm test -- --run`, `npm run build` | PASS; 30 unit tests; 205 modules built |
| `npm run test:e2e` against `http://localhost:8080` | 10 passed, including new week 1–2 instruction and autograding flow |
| `node tests/legacy/state.test.mjs` | 7 passed |
| `python -m courselab.check_content ../content` | PASS: 25 packages / 112 practice specifications |
| `python tools/check_security.py` and `python tools/check_security.py --bundle frontend/dist` | PASS: 387 files, 0 findings |
| `docker compose up --build -d --wait --wait-timeout 180`; Alembic and health queries | PASS: database, API, and web healthy; `0007 (head)`; health `ok` |

These checks confirm the current software paths and authored package structure. They do not establish full-course quality, a security audit, course-level human grading, workload, mastery, or institutional equivalency.

## Previous increment: graded-assignment appeals and manual review

Alembic revision 0007 adds a one-appeal-per-submission learner workflow and a separate append-only instructor decision record. Learners can request a review of a graded result; authorized reviewers can uphold, decline, or adjust within the assignment's score bounds. The original deterministic score and feedback remain immutable. Adjusted results are surfaced as effective scores and feed the weighted gradebook. Instructor review reconstructs only answer-free question views and verifies the pinned course source and question digest; stale or unavailable specifications can only be declined. Self-review is blocked. Learner export, account deletion, reviewer anonymization, and gradebook override counts include these records.

The graded-assignment workflow still runs only against synthetic test fixtures because **none of the 25 shipped course packages contains graded assignments**. No live catalog course awards a weighted course grade. Programming assignments remain disabled, and no historical content archive is available for regrading old versions. Course maturity is unchanged: 25 partial, 0 beta, 0 complete, 0 externally reviewed.

Validation on 2026-10-06: backend **221 passed** (one upstream Starlette/httpx deprecation warning); root content/security suite **53 passed, 1 skipped**; frontend **30 unit tests passed**, lint/format and TypeScript/Vite build passed (205 modules); Playwright **9 passed** against the rebuilt Compose stack; legacy storage migration **7 passed**. Ruff passed. Content validation found 25 packages, 101 lessons, 106 questions, 203 cards and 25 cases: zero errors and 125 explicit depth/objective warnings. The API/content check passed for 25 packages and 108 practice specifications. The source/bundle security scan found zero issues in 382 files. Compose services are healthy, Alembic is at `0007 (head)`, both review tables exist, and `/api/v1/health` is `ok`; programming and LLM providers remain disabled. Both GitHub Actions jobs passed in [run 37511037086](https://github.com/dylanstechmann/uniStemCourseSimulators/actions/runs/37511037086).

| Command/check | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages; 0 errors; 125 disclosed depth/objective warnings |
| `python -m pytest tests -q` | 53 passed, 1 skipped |
| `cd backend; python -m pytest tests -q` | 221 passed; 1 upstream deprecation warning |
| `ruff check backend tools tests` | PASS |
| `node tests/legacy/state.test.mjs` | 7 passed |
| Frontend `npm run lint`, `npm test -- --run`, `npm run build` | PASS; 30 unit tests; 205 modules built |
| `npm run test:e2e` against `http://localhost:8080` | 9 passed |
| `python -m courselab.check_content ../content` | PASS: 25 packages / 108 practice specifications |
| `python tools/check_security.py --bundle frontend/dist` | PASS: 382 files, 0 findings |
| `docker compose up --build -d`; `alembic current`, review-table query and `/api/v1/health` | PASS: services healthy; Alembic `0007`; both review tables exist; health `ok` |

Playwright covers guest enrollment, lesson viewing, formative submission/feedback, progress and persistence, plus existing appeal flows and protection of public question views. Graded-assignment appeal, score bounds, stale-source decline, immutable automatic scores, weighted-grade updates and anonymization are covered by backend API tests and frontend component tests on synthetic fixtures. Existing user and database volumes were preserved during rebuild. These local synthetic checks do not constitute a security audit or full course-quality review.

## Previous increment: deterministic graded-assignment submission and weighted gradebook

Alembic revision 0006 adds append-only graded submissions tied to learner enrollment, course version, assessment and attempt number. An enrolled learner receives a whitelisted question view with no answer keys, then submits a complete response for server-side deterministic grading. The API verifies the enrollment-pinned source file hash and question mapping, enforces release time, a strict deadline and attempt limits, stores scores and criterion feedback, serves learner-owned attempt history, and includes selected results in the weighted gradebook. The React workspace provides the assignment response form, immediate feedback and refreshed gradebook. Export and account deletion include the new records.

The executable submission path uses a synthetic test fixture because **none of the 25 shipped course packages currently contains graded assignments**. Consequently no live catalog course awards a weighted course grade. At the time of this increment, graded appeals/manual overrides, archived historical content and code execution were not implemented. This increment did not change course maturity: 25 partial, 0 beta, 0 complete, 0 externally reviewed.

Validation on 2026-10-06: backend **218 passed** (one upstream Starlette/httpx deprecation warning); root content/security suite **53 passed, 1 skipped**; frontend **27 unit tests passed**, lint/format and TypeScript/Vite build passed (205 modules); Playwright **9 passed** against the rebuilt Compose stack. Ruff passed after correcting import ordering in two existing utility/test files. Content validation found 25 packages, 101 lessons, 106 questions, 203 cards and 25 cases: zero errors and 125 explicit depth/objective warnings. The API/content check passed for 25 packages and 108 practice specifications. The source/bundle security scan found zero issues in 381 files. Compose services are healthy, Alembic is at `0006 (head)`, the `graded_submissions` table exists, and `/api/v1/health` is `ok`; programming and LLM providers remain disabled. GitHub Actions passed both jobs for the graded-workflow commit in [run 37505270475](https://github.com/dylanstechmann/uniStemCourseSimulators/actions/runs/37505270475) and for its LF-normalized tree in [run 37505850315](https://github.com/dylanstechmann/uniStemCourseSimulators/actions/runs/37505850315).

| Command/check | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages; 0 errors; 125 disclosed depth/objective warnings |
| `python -m pytest tests -q` | 53 passed, 1 skipped |
| `cd backend; python -m pytest tests -q` | 218 passed; 1 upstream deprecation warning |
| `ruff check backend tools tests` | PASS |
| `node tests/legacy/state.test.mjs` | 7 passed |
| Frontend `npm run lint`, `npm test -- --run`, `npm run build` | PASS; 27 unit tests; 205 modules built |
| `npm run test:e2e` against `http://localhost:8080` | 9 passed |
| `python -m courselab.check_content ../content` | PASS: 25 packages / 108 practice specifications |
| `python tools/check_security.py --bundle frontend/dist` | PASS: 381 files, 0 findings |
| `docker compose up --build -d`; PostgreSQL migration query and `/api/v1/health` | PASS: services healthy; Alembic `0006`; graded-submission table exists; health `ok` |
| GitHub Actions | PASS: both jobs passed for the graded-submission implementation and LF-normalized tree |

Playwright covers the existing guest enrollment, lesson, formative submission/feedback, progress and persistence flows; graded-assignment request/result/history behavior is covered by backend API tests and frontend component tests on a synthetic fixture. Existing user and database volumes were preserved during rebuild. These local synthetic checks do not constitute a security audit or full course-quality review.

## Previous increment: enrollment-versioned assessment plans

The course schema now supports grade categories and weights, points or equal-assignment aggregation, assignment titles/weeks, release and deadline timestamps, attempt limits, and highest/latest attempt selection. The validator rejects weight/category mismatches, duplicate IDs, graded work in formative-only packages, invalid date order, and invalid attempt rules. Alembic revision 0005 adds enrollment/version-scoped `assessment_plans` and `assessment_instances`; enrollment captures policy and assignment metadata plus a source-file SHA-256, and an explicit content-version update appends a new snapshot while preserving the old metadata. The authenticated learner plan endpoint omits internal paths, question IDs, digests, and answer keys. The course workspace displays the plan alongside the existing practice gradebook.

The weighted-grade core uses `Decimal`, is separately unit-tested for category aggregation, attempt selection/limits, missing and unreleased work, exact-deadline boundaries, late/unknown attempts, invalid scores, and repeatability. This is a calculation core only: there is not yet a graded-assignment submission/result store or a route connecting saved scores to the calculator. The visible practice gradebook remains formative. Current content stays at 25 partial courses, with no course grade configured.

Validation on 2026-10-06: **308 tests passed** across the root content/security suite (54), backend suite (213), frontend unit suite (25), Playwright (9), and legacy storage tests (7). Ruff, frontend lint/Prettier, TypeScript/Vite build (204 modules), the API/content integration checker (25 packages and 108 supported practice specifications), and source/bundle security scan (378 source files, zero findings) passed. Content validation reported 25 packages, 101 lessons, 106 questions, 203 cards and 25 cases; zero errors and 125 explicit depth/objective warnings. The rebuilt Compose stack is healthy, PostgreSQL reports Alembic `0005`, and Playwright against the real stack verifies enrollment, lesson reading, practice submission and feedback, progress/gradebook persistence, and the new no-course-grade statement. Existing persistent volumes were preserved.

| Command/check | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages; 0 errors; 125 disclosed depth/objective warnings |
| `python -m pytest tests -q` | 54 passed |
| `cd backend; python -m pytest -q` | 213 passed |
| `ruff check backend tools tests` | PASS |
| Frontend `npm run lint`, `npm test`, `npm run build` | PASS; 25 unit tests; 204 modules built |
| `npm run test:e2e` against `http://localhost:8080` | 9 passed, including assessment-plan display and formative-only status |
| `node tests/legacy/state.test.mjs` | 7 passed |
| `python tools/check_security.py --bundle frontend/dist` | PASS: 378 source files, zero findings |
| `python -m courselab.check_content ../content` | PASS: 25 course packages and 108 supported practice specifications |
| `docker compose up --build -d`; PostgreSQL migration query and `/api/v1/health` | PASS: stack healthy; Alembic `0005`; assessment snapshot tables exist |

The test output includes existing Starlette/httpx and `datetime.utcnow()` deprecation warnings. The course-grade calculation is not active for any live package; assignment submission enforcement, result persistence, protected graded question delivery, and gradebook integration remain roadmap work. The hashed snapshots are metadata/version evidence, not full immutable content archives and do not support historical regrading.

## Previous increment: operator-provisioned review and variant-pinned restoration

Self-declared registration emails no longer grant reviewer access. Alembic revision 0004 adds an `is_instructor` role that defaults to false for all existing users. Only the operator CLI can grant or revoke it; operators must verify identity and authority out of band. Instructor decisions now reconstruct the saved variant and compare the question digest. The authorized API returns only the safe public question DTO, including actual options and structured-response fields; it never returns the grader key. Adjusting/upholding fails closed if the version is stale, the attempt was unpinned, or the installed specification changed. Without immutable package archives, older attempts can only be declined.

Lesson reloads now restore the learner's latest attempted variant for the current content version. A signed v2 token pins that variant while the verifier continues accepting v1 tokens; the attempt and appeal feedback therefore stay paired with the exact prompt that was answered. A same-user reload regression test covers this behavior.

Validation on 2026-10-06: **291 tests passed**—199 backend, 52 content/security, 24 frontend unit, 9 Playwright and 7 legacy migration tests. Frontend lint/Prettier, TypeScript typecheck, production build (203 modules), Ruff, content validation (25 packages, 101 lessons, 106 questions, 203 cards, 25 cases; zero errors and 125 explicit depth/coverage warnings), and source/bundle security scan (372 files, zero findings) passed. Production Compose configuration passed with validation-only placeholders. The full Compose application built and reported healthy; Alembic reached `0004 (head)`. The browser suite covered course reading, enrollment, submission, feedback and persistence; an unprivileged registrant was denied the instructor API. New browser-runner cleanup removes synthetic accounts created in each E2E run. The migration did not remove or rewrite preexisting learner records.

The first hosted workflow attempt exposed a reload-only mismatch: a newly randomized prompt replaced the question variant tied to a saved attempt, hiding its feedback in the lesson view. After variant-pinned restoration, local Playwright passed all 9 tests and [GitHub Actions run 37415386582](https://github.com/dylanstechmann/uniStemCourseSimulators/actions/runs/37415386582) passed both jobs, including Compose startup and all Playwright checks.

Before and after E2E validation, the existing database contained 82 users, 82 enrollments, 90 attempts and 6 progress records. Five synthetic guest records from the first E2E run were identified by their creation window and removed; the final counts returned to the same baseline. The test-origin bridge `http://host.docker.internal:8080` was temporarily enabled to let the browser container reach the loopback-published app, then the API was recreated with localhost origins only. Existing database and credential volumes remained in place. These are local synthetic-data checks, not a penetration test, production deployment or security certification.

## Previous increment: product rename and progress review

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

The initial container frontend test launch encountered a Windows-installed Rollup optional dependency. `npm ci` inside the Linux development container repaired the environment without changing dependency versions; tests/build then passed. Playwright Chromium and its Linux dependencies were installed inside that development container. This earlier validation temporarily used an email allowlist for a synthetic reviewer; that authorization flaw was discovered in the later progress review and is closed by the current increment above. Only loopback web access is published.

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

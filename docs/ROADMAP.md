# Milestone roadmap

Finish each earliest milestone to a tested runnable state and commit separately. Later requirements remain explicit. No complete courses exist; migration is not semester development or external review.

## 1 — Audit, identity, schemas and maturity

Completed and tested: observed baseline, audit, rename, retained state migration, documented schemas, 25 preserved partial packages, source/license registry and migration guidance. Integrated validation passed with 34 content tests, 4 state tests and browser regression. Warnings disclose historical brevity and incomplete objective coverage.

## 2 — Full-stack reader and durable state

Implemented and tested: React/TypeScript, FastAPI/Pydantic, PostgreSQL SQLAlchemy/Alembic, one-command Docker, guest/accounts and guest-to-account conversion, enrollment, lessons, deterministic choice/numeric practice submission and feedback, notes/bookmarks, export/delete, immutable attempts and practice gradebook. Ownership, CSRF, malformed data, public DTO exclusions, migrations, unit tests, browser flows and basic automated accessibility checks are covered. See the validation report for exact commands and operational evidence. Preserved study tools/calculators are in `legacy/`; editable browser scores are never imported as server grades.

Milestone 2 does not implement weighted university grades, robust objective mastery based on diverse assessment evidence, exams or a full-semester calendar. Milestone 3 now adds a conservative provisional practice indicator, but current gradebook values remain formative study evidence only.

## 3 — Full grading and instructor feedback (in progress)

Implemented increments: deterministic multiple-select with explicit all-or-nothing and clamped equal-share correct-minus-incorrect policies; learner-facing scoring rules; response-shape/duplicate/index checks; an original biology practice item; SHA-256 question-specification digests for new attempts; and an explicit package-version update path preserving previous attempt records. Alembic migration 0002 adds a nullable digest; historical attempts remain unpinned and retain practice-v1. Numeric grader v3 converts a constrained, documented subset of SI and biological units with exact rational scales, dimensional checks, bounded product/quotient/power parsing and absolute tolerance in the authored unit. Grader v4 adds bounded relative tolerance using `absolute + relative × |answer|`. Grader v5 checks optional lexical significant-figure requirements (1–12) only after unit conversion and tolerance. Objective evidence v1 reports best points per distinct tagged item, separates retry counts from breadth, and exposes a provisional study indicator only after at least three distinct items, 80% objective-item coverage and 80% best-point performance. The thresholds and policy version are visible to learners; the UI explicitly says this does not certify mastery. Tests cover conversion, incompatibility, unsupported units, matched dimensions, tolerance boundaries, precision notation, invalid policies, objective breadth/retries, and adversarial inputs.

Implemented this turn: finite authored formative variants selected reproducibly from signed seven-day tokens, bound to course/version/question; resolved prompts/options/specs stay server-side except for the whitelisted learner DTO; variant IDs and exact per-variant digests are saved per attempt. Each variant is validated as a standalone resolved question. The biology seed now includes three distinct forms for one formative check. This does not generate randomized numeric parameters and does not add protected exam variants.

Remaining: broader unit coverage; bounded SymPy; structured, graph/table/data, upload and design rubrics; numeric parameter generation with independent recalculation; category weights; robust objective mastery from diverse assessments, retention and transfer; appeals/audited overrides; evidence-linked misconception feedback; credential-safe optional providers; and an actually isolated code worker. Unknown and affine units fail closed; a few contextual legacy labels are exact-label-only. Digests detect specification changes but do not archive old packages; versioned content archiving and regrading still need design. Add adversarial/mutation tests for every plugin. Code stays disabled until isolation is demonstrated; never mount a Docker socket in the API or worker.

## 4 — Broad catalog and graph

Eight pathways and separate engineering subject entries with acyclic dependencies. Expand sciences/biology/chemistry/computing/regeneration/aging/translation as catalog-only or outlined. Map official JHU references without copied text/equivalency. Test graph/provenance and visualization.

## 5 — Deep Cell and Molecular Biology

Original 14-week syllabus; substantial lessons (two weekly where appropriate), eight homework sets, three data/virtual-lab/simulation activities, midterm, cumulative final, integrative project, seeded bank, specs/rubrics, cards, misconception/feedback catalog and module provenance. Independent scientific/numeric checks; actual human review. Remain beta until complete gates pass; never generate filler or reviewers.

## 6 — Full gates and deployment

Already delivered early: schema/structural depth/provenance/review-status gates, duplicate checks, CI configuration, local Compose, production Compose/Caddy example, deployment/backup instructions, frontend/backend/Playwright suites, basic axe checks and bundle/secret scans. These foundations do not constitute all full-course quality gates.

Remaining: independent recalculation for every numeric item; dimensional/tolerance and grader mutation coverage; a real completion-evidence pipeline combining test artifacts and actual human review; broader accessibility/manual assistive-technology and exam/appeal flows; resolution of the two JHU HTTP 403 live-link probes; and production operation hardening. A successful local restore rehearsal does not establish an off-host encrypted backup/disaster-recovery process. Public HTTPS deployment, separate least-privilege application/migration database roles, distributed throttling, recovery/retention policies and resource limits need operator review and validation. No complete or externally reviewed badge is allowed without its evidence.

## Preserved migration backlog

Six calculators, cards, case self-assessment and notebooks remain available in the legacy reader until React replacements are tested. Pathway inconsistencies and merged subjects require review rather than destructive replacement.

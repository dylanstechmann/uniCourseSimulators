# Progress review: uniStemCourseSimulators

## Update after private assessment-source boundary (2026-10-06)

Graded assessment sources can now load from a separate operator-mounted, read-only directory using confined `private://` references. Public and private roots must be disjoint; traversal and symlink escapes are rejected. Missing keys fail closed, and the existing enrollment snapshot continues to pin the source SHA-256. Compose mounts the private root only into API/migration containers; `.local/private-assessments/` is Git-ignored. Tests confirm answer specs and paths do not appear in learner APIs. This is source-handling infrastructure only: no private key or graded course package has been added, all 25 packages remain formative-only, and no course grade is enabled. The next content task is a complete Week 4 enzyme-kinetics homework package mapped to its authored instruction; it must remain inactive until its protected answer package and all reviews are provisioned.

## Update after week 11 signaling lab (2026-10-06)

The cell-biology package advanced to 0.18.0 and remains partial. Week 11 now has an original 2–3 hour virtual data-analysis lab built around 120 openly documented synthetic pERK/total-ERK observations across six conditions, five times, and four independent preparation blocks. It adds a 24-cell CSV summary check, 15 time-course plot points, a baseline-adjusted inhibitor calculation, five explicit rescue/control choices, and four retrieval cards. The answer specifications are public; the lab is ungraded and does not count as a grade-bearing lab. The course still lacks all eight graded homework packages, one additional lab, summative exams, a cumulative project, measured workload, and independent course review. The course remains partial and no university equivalency is claimed.

Reviewed 2026-10-06 against the requested six milestones. The content and breadth measurements below use commit `68defd74b8c98d8cac0556de3de72b8219bf987f`; the current increment changes only instructor authorization, appeal context, documentation and tests, so those content measurements are unchanged. Its review fixes passed the validation recorded in [VALIDATION_REPORT.md](VALIDATION_REPORT.md). This review inspects application code, manifests, readings, assessments, schemas, validator, tests and deployment configuration. Automated passing tests demonstrate covered behavior; they do not establish academic adequacy or production security.

## Update after week 5 course authoring (2026-10-06)

The detailed inventory and findings below describe the exact review snapshot named above. Since that snapshot, the cell-biology package has advanced to version 0.7.0 and remains `partial`: weeks 1–5 now each have two substantial lessons, with week 4 retaining its short capsule and week 7 retaining its compact gene-expression prototype. Current repository inventory is 25 partial packages, 109 lessons, 126 formative questions, 219 retrieval cards, and 25 self-assessed cases. No course meets the complete standard; workload, full homework/lab/exam/project sequences, and independent academic review are still outstanding.

The week-5 increment passed content validation, 57 root tests (1 skipped), 221 backend tests, 30 frontend tests, 10 Playwright tests, 7 legacy tests, and local Compose health checks. See the week-5 entry in [VALIDATION_REPORT.md](VALIDATION_REPORT.md) for the recorded commands and limits. Its next-step recommendation has since been addressed by the week-6 increment below.

## Update after week 6 course authoring (2026-10-06)

The cell-biology package advanced to version 0.8.0 and remains `partial`. Week 6 now has two original lessons on replication models and repair evidence, seven formative items, four retrieval cards, a selected misconception catalog, and layered feedback examples. Its UV lesion-signal series is explicitly synthetic; the qualitative isotope-density exercise is a model prediction rather than a transcription of historical measurements. The new source mapping uses MIT OCW 7.28x only as a topic comparator and links scientific references without copying their text, figures, or data.

The catalog now contains 25 partial packages, 111 lessons, 133 formative questions, 223 retrieval cards, and 25 self-assessed cases. Weeks 1–6 have two substantial lessons each; week 4 retains its compact prototype capsule and week 7 its single compact gene-expression reading. Weeks 8–14 remain outlines. The eight planned homework sets, three complete lab/data activities, midterm, final, cumulative project, workload evidence, and independent academic/accessibility review are still outstanding. No course is complete or externally reviewed.

Validation passed: content authoring tests 56 (1 skipped), full root suite 58 (1 skipped), backend 221, frontend 30, Playwright 10, and legacy 7; frontend lint/build passed, Compose services are healthy, the API health endpoint is `ok`, and the API reports 135 supported practice specifications. The full Playwright learner flow covers enrollment, lesson access, assignment submission, deterministic feedback and saved progress, including the new replication and repair items. Details and exact command results are in [VALIDATION_REPORT.md](VALIDATION_REPORT.md).

The next priority is to develop a coherent week 7 sequence and reconcile its calendar with the crosswalk's proposed midterm placement. Continue with substantive homework and laboratory packages only after their instruction, controls, solution specs, and independent checks are defined. Preserve `partial` maturity until the full-course gates and qualified reviews are actually satisfied.

## Update after week 7 course authoring (2026-10-06)

The cell-biology package advanced to version 0.9.0 and remains `partial`. Week 7 now contains two original lessons on chromatin accessibility/regulatory DNA and transcription-factor occupancy/reporter evidence, seven deterministic formative items, four retrieval cards, two feedback templates, seven new misconception entries, objective mappings, and per-module provenance. The original compact gene-expression lesson is retained as supplemental material. New examples and data are synthetic; ChIP-qPCR and reporter results are taught with separate control roles and explicit limits on occupancy, direct binding, and endogenous causal claims.

The 14-week proposal now keeps weeks 1–7 as the teaching block and reserves week 8 for a proposed midterm. That is a calendar decision only: week 8 has no exam, answer key, rubric, assessment record, or release policy. Weeks 9–14 still have no authored lesson sequences. The repository now contains 25 partial packages, 113 lessons, 140 formative questions, 227 retrieval cards, and 25 self-assessed cases; zero courses meet the complete or external-review standard.

Validation passed: content validation (25 packages; 0 errors and 123 disclosed depth/objective warnings), root suite 59 passed/1 skipped, backend 221 passed, frontend 30 passed, Playwright 10 passed, legacy 7 passed, lint/build, and local Compose/API integration. The API reports 142 supported practice specifications; Alembic is `0007 (head)`, health is `ok`, and the source/bundle boundary scan reports 0 findings across 397 files. See the current increment in [VALIDATION_REPORT.md](VALIDATION_REPORT.md) for commands and limits.

Next, author week 8–14 instruction and the substantive homework, three data/lab activities, midterm, final, and integrative project. Week 4 and week 7 still need their planned homework/data-analysis packages. Measure learner workload and obtain independent subject-matter and accessibility reviews. Preserve `partial` maturity until the full course package passes the documented gates.

## Overall assessment

The repository is a working local formative learning and practice platform. Infrastructure has progressed substantially: React/TypeScript, FastAPI, PostgreSQL, migrations, durable learner records, bounded deterministic graders and a curriculum graph exist. The central educational deliverable—a substantive university course—remains unfinished. **Zero courses are complete, beta or externally reviewed.** No credit, university equivalency, affiliation or admission eligibility is implied.

| Milestone | Current assessment | Main remaining work |
| --- | --- | --- |
| 1: Audit, identity, schemas, maturity | Substantially delivered | Maintain accurate documentation and migration compatibility |
| 2: Full-stack reader and persistence | Delivered for local formative study | Semester calendar, scheduled assessments and richer learner tools |
| 3: Grading and instructor feedback | Partial | The current increment closes email-impersonation and same-version variant/digest review defects. Semester assignments/exams, weighted policies, broader reasoning assessment and immutable historical content remain |
| 4: Catalog and dependencies | Planning metadata delivered | Qualified review of scope, sequencing and prerequisites |
| 5: Full biology vertical slice | Not delivered | Original 14-week instruction and aligned semester assessment sequence |
| 6: Full quality gates/deployment | Foundations delivered | Trusted completion evidence, academic/accessibility review, operational hardening |

## What works now

- Local Docker Compose startup with private database/credential volumes, Alembic migrations including operator-provisioned review roles, a same-origin API proxy and a separate frontend image.
- Public course reading; guest/account sessions and conversion; enrollment, reading marks, notes/bookmarks, immutable attempts, feedback history, practice gradebook and learner export/delete.
- Choice/multiple-select, constrained numerical units/tolerances/significant figures, bounded rational-expression equivalence, fielded data/rubric responses, small CSV numeric tables and fixed-axis coordinate grading. These are narrowly specified formative graders, with explicit unsupported cases.
- Append-only appeal decisions and effective formative-score overrides. Instructor roles are granted only through an operator CLI after out-of-band identity review; registration cannot grant access. Variant attempts are reconstructed from their saved ID, and changes are accepted only when the current course version and question-specification digest match. Older content cannot be restored because immutable package archives do not exist.
- Eight pathway maps and prerequisite validation across 62 nodes. The JHU map includes all four requested foundational topics and the advanced topic list, with link-only provenance and equivalency caveats.
- Source registry, separate software/content licenses, public DTO exclusions, CSRF/ownership checks, safe Markdown, CI, backend/frontend/content tests and basic browser accessibility checks.

Evidence: `compose.yaml`, `backend/courselab/{db,main,grading,content,evidence}.py`, `frontend/src/components/`, `content/curriculum-map.json`, `.github/workflows/ci.yaml`. Python execution and optional LLM providers are disabled interfaces; their availability has not been implemented or validated.

## Content depth and alignment

| Inventory at the reviewed baseline | Actual scope |
| --- | --- |
| 25 course packages | All `partial` and `unreviewed` |
| 37 additional subject nodes | `catalog-only`; no enrollable instructional package |
| 101 readings | 100 at most 100 words including headings; approximately 7,833 words in total |
| 106 questions | 57 numeric, 43 single choice, one each of six other types |
| 203 retrieval cards / 25 cases | Primarily prototype prompts and self-assessment checklists |
| 101 practice inventories | No graded homework/lab/exam/project inventories |
| Semester weeks/workload | No populated week schedules or measured workload estimates |

Foundations of Cell and Molecular Biology has four readings totaling approximately 308 words, seven questions, eight cards and one self-assessed case. One question has three authored forms. It lacks the requested 14-week instruction, eight substantive homework sets, three activities, midterm, cumulative final and integrative project. Its case uses zero-point checklist criteria rather than a developed analytic performance rubric.

Assessment development has outpaced instruction: a structured item asks about ChIP-qPCR and motif-mutant reporters, but the linked gene-expression reading does not explain those methods or provide worked experimental examples. Expand instruction alongside assessment, including controls, uncertainty and causal reasoning.

Only seven of 13 biology course/lesson objectives have an assessment or question mapping; all four course outcomes remain unmapped. Eight of nine lesson-objective records lack a course-outcome link, and all eight cards lack objective mappings. Reference presence does not prove the assessment exercises the claimed cognitive level. See `content/courses/cell-biology/course.json`, `question-banks/practice.json`, `modules/` and `rubrics/case-studio.json`.

Module provenance and licensing boundaries are strengths. Current biology source alignment points broadly to two comparator courses; it is not an exact source-unit/topic/assessment crosswalk or evidence of comparable coverage. The developed course needs a documented scope comparison, explicit omissions and real scientific review. Public catalogs inform the knowledge map; they do not validate equivalency.

## Material findings

| Priority | Finding and consequence | Required resolution |
| --- | --- | --- |
| Addressed in current increment | A registrant could previously claim an allowlisted email and obtain reviewer access. | `INSTRUCTOR_EMAILS` authorization is removed. All accounts default to no role; only the operator CLI changes the persisted role, and self-registration still fails closed. The operator must verify identity outside the application. |
| Addressed for the installed package; historical limitation remains | The previous queue showed the base prompt for variant attempts and could not detect same-version edits. | The queue resolves the stored variant and checks its question-specification digest before exposing the prompt/options. Adjust/uphold fail closed on missing, stale or changed content. Old package versions are not archived, so old appeals can only be declined. |
| Addressed in current increment | After a page reload, a fresh random variant could replace the prompt attached to a saved attempt and hide its feedback. | Lesson loading now reuses the latest attempted variant for the learner and current content version; a signed pin token reproduces that exact question, and a regression test checks restored feedback/status. |
| P1 course delivery | API/result schemas and gradebook cover formative practice only. Best per-question scores are not category-weighted semester grades. | Add assessment instances, homework/lab/project/exam categories, release/deadline/attempt policies, protected key storage and weighted calculation. |
| P1 before complete status | Completion evidence currently trusts manifest booleans and a nonempty execution list, without trusted artifact/result verification or content/commit binding. | Generate evidence from actual CI runners, bind it to content/software hashes and require actual human signoff. |
| P2 learner coverage | Retrieval cards reveal answers without persisted spacing. Objectives without tagged items disappear from evidence views. Course DTO/UI omit weekly scheduling and grading policy. | Add review ratings/history/due queue, show unassessed objectives, expose typed weeks/assessment policies and learner calendar. |
| P2 extensibility | Content loader hardcodes `question-banks/practice.json`; API/grader remain large modules. | Resolve manifest-defined banks and split routers/services around tested grader contracts. |
| P2 production | Email verification/recovery, shared throttling, retention, least-privilege DB roles, resource limits and public HTTPS operation remain unvalidated. | Implement and validate these before handling real learner records publicly. |

Code evidence: reviewer checks/registration in `backend/courselab/main.py` (`require_reviewer`, `register`); appeals in `instructor_appeal_record` and `review_appeal`; digest storage in `submit`; completion evidence in `tools/validate_content.py`; retrieval in `LessonStudy.tsx`; objective initialization in `evidence.py`; public manifest fields in `content.py` and course views in `CourseWorkspace.tsx`.

Live-link probes are optional and not a mandatory CI check. Two JHU URLs denied the automated client with HTTP 403 in the recorded prior run; this is an unresolved access/probe result, not proof that the pages are missing. Link checks should cover instructional links as well as registry URLs and distinguish denied access from broken destinations. Independent recalculation currently covers selected CSV/graph keys, not every numerical item. A disabled runner cannot establish isolation against malicious code or infinite loops.

## Recommended execution order

1. Implement a manifest-driven graded-assessment model: assignment instances, homework/lab/project categories, deadlines, release and attempt policies, weighted calculations, and protected assessment-key storage. Keep current practice scores clearly formative.
2. Draft the 14-week cell/molecular-biology scope, source map and assessment crosswalk, then author substantial teaching, worked experimental examples, homework and data/lab activities in sequence. Address methods already referenced by questions (including ChIP-qPCR and reporter controls). Do not mark the package beta until its course materials meet the documented gates.
3. Add immutable content-package archives so appeal review can load historical prompts/specifications rather than only decline after an update. Extend learner scheduling, spaced retrieval and objective coverage including unassessed objectives.
4. Build trusted hash-bound quality evidence, independently recalculate every numerical key, broaden mutation/adversarial tests, validate instructional links, and obtain actual subject-matter/accessibility review before any complete badge.
5. Complete production hardening and recovery rehearsal before serving valuable learner records: separate least-privilege database roles, email verification/recovery, distributed throttling, retention, resource limits and a verified off-host backup process. Implement code execution only with demonstrated isolation.

The [roadmap](ROADMAP.md) tracks acceptance criteria. Existing useful content and legacy tools remain available. Branding now matches the renamed public repository. Historical browser storage identifiers and the untracked local Compose-volume identity remain only to preserve existing learner and database data; they are not product names. No course maturity label has advanced.

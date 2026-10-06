# Progress review: uniStemCourseSimulators

Reviewed 2026-10-05 against the requested six milestones. Implementation baseline: commit `68defd74b8c98d8cac0556de3de72b8219bf987f`. This review inspected application code, manifests, readings, assessments, schemas, validator, tests and deployment configuration. Rename validation is recorded separately in [VALIDATION_REPORT.md](VALIDATION_REPORT.md). Automated passing tests demonstrate the covered behavior; they do not establish academic adequacy or production security.

## Overall assessment

The repository is a working local formative learning and practice platform. Infrastructure has progressed substantially: React/TypeScript, FastAPI, PostgreSQL, migrations, durable learner records, bounded deterministic graders and a curriculum graph exist. The central educational deliverable—a substantive university course—remains unfinished. **Zero courses are complete, beta or externally reviewed.** No credit, university equivalency, affiliation or admission eligibility is implied.

| Milestone | Current assessment | Main remaining work |
| --- | --- | --- |
| 1: Audit, identity, schemas, maturity | Substantially delivered | Maintain accurate documentation and migration compatibility |
| 2: Full-stack reader and persistence | Delivered for local formative study | Semester calendar, scheduled assessments and richer learner tools |
| 3: Grading and instructor feedback | Partial | Secure reviewer identity, faithful appeal reconstruction, assignment/exam model, weighted policies, broader reasoning assessment |
| 4: Catalog and dependencies | Planning metadata delivered | Qualified review of scope, sequencing and prerequisites |
| 5: Full biology vertical slice | Not delivered | Original 14-week instruction and aligned semester assessment sequence |
| 6: Full quality gates/deployment | Foundations delivered | Trusted completion evidence, academic/accessibility review, operational hardening |

## What works now

- Local Docker Compose startup with private database/credential volumes, Alembic revisions through `0003`, a same-origin API proxy and a separate frontend image.
- Public course reading; guest/account sessions and conversion; enrollment, reading marks, notes/bookmarks, immutable attempts, feedback history, practice gradebook and learner export/delete.
- Choice/multiple-select, constrained numerical units/tolerances/significant figures, bounded rational-expression equivalence, fielded data/rubric responses, small CSV numeric tables and fixed-axis coordinate grading. These are narrowly specified formative graders, with explicit unsupported cases.
- Append-only appeal decisions and effective practice score overrides. Their authorization/content reconstruction limitations below must be addressed before public instructor use.
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
| P1 before public instructor access | Registration stores a self-declared email; reviewer authorization checks that string against `INSTRUCTOR_EMAILS`. A first registrant can claim an allowlisted address and gain review privileges. | Provision immutable account roles or verify email ownership before granting authority. Keep the allowlist empty on public installations. |
| P1 assessment validity | Instructor queue loads the base question, ignoring the saved `variant_id`. Review decisions check course version but do not compare the stored specification digest. A variant or same-version edit can produce the wrong review context. | Reconstruct the saved variant, verify its digest, expose the actual options/rubric and fail closed when unavailable. Archive immutable content versions. |
| P1 course delivery | API/result schemas and gradebook cover formative practice only. Best per-question scores are not category-weighted semester grades. | Add assessment instances, homework/lab/project/exam categories, release/deadline/attempt policies, protected key storage and weighted calculation. |
| P1 before complete status | Completion evidence currently trusts manifest booleans and a nonempty execution list, without trusted artifact/result verification or content/commit binding. | Generate evidence from actual CI runners, bind it to content/software hashes and require actual human signoff. |
| P2 learner coverage | Retrieval cards reveal answers without persisted spacing. Objectives without tagged items disappear from evidence views. Course DTO/UI omit weekly scheduling and grading policy. | Add review ratings/history/due queue, show unassessed objectives, expose typed weeks/assessment policies and learner calendar. |
| P2 extensibility | Content loader hardcodes `question-banks/practice.json`; API/grader remain large modules. | Resolve manifest-defined banks and split routers/services around tested grader contracts. |
| P2 production | Email verification/recovery, shared throttling, retention, least-privilege DB roles, resource limits and public HTTPS operation remain unvalidated. | Implement and validate these before handling real learner records publicly. |

Code evidence: reviewer checks/registration in `backend/courselab/main.py` (`require_reviewer`, `register`); appeals in `instructor_appeal_record` and `review_appeal`; digest storage in `submit`; completion evidence in `tools/validate_content.py`; retrieval in `LessonStudy.tsx`; objective initialization in `evidence.py`; public manifest fields in `content.py` and course views in `CourseWorkspace.tsx`.

Live-link probes are optional and not a mandatory CI check. Two JHU URLs denied the automated client with HTTP 403 in the recorded prior run; this is an unresolved access/probe result, not proof that the pages are missing. Link checks should cover instructional links as well as registry URLs and distinguish denied access from broken destinations. Independent recalculation currently covers selected CSV/graph keys, not every numerical item. A disabled runner cannot establish isolation against malicious code or infinite loops.

## Recommended execution order

1. Close the reviewer-identity and appeal reconstruction defects with adversarial regression tests.
2. Implement the minimum graded-assessment and immutable content model required by the biology course: manifest bank resolution, assignment instances, weights, release rules and protected keys.
3. Author the 14-week biology scope/assessment blueprint, then develop substantial weekly teaching, worked experimental examples, homework and lab activities alongside those workflows. Release honest partial increments; avoid more breadth-only seeds.
4. Finish calendar/deadline views, spaced retrieval and objective coverage, including missing-evidence states.
5. Build trusted quality evidence and obtain actual scientific/accessibility review before any complete badge. Finish isolated execution/provider integrations only when real assignments require them.
6. Complete public deployment hardening and recovery rehearsal before serving valuable learner records.

The [roadmap](ROADMAP.md) tracks acceptance criteria. Existing useful content and legacy tools remain available. This rename/review increment fixes branding, storage compatibility and stale syllabus metadata; the substantive defects identified here are documented outstanding work.

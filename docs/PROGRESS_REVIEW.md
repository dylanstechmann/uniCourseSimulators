# Progress review: uniStemCourseSimulators

## Update after the geroscience schedule (2026-10-08, tenth pass)

Written by an AI coding assistant. Geroscience is the second package with a proposed week-by-week structure (14 weeks, 18 readings including a synthetic lifespan lab and a study-design lesson). Like cell biology, it has no graded homework, exams or project, no measured workload and no human review, so it remains `partial`. The remaining distance to a complete course is the same list: graded work with protected keys, workload evidence and named review.

## Update after the research-skill lessons (2026-10-08, ninth pass)

Written by an AI coding assistant. Ten lessons aimed at research practice: multiple testing, effect sizes and regression to the mean, algorithmic cost, floating-point pitfalls, biomarker reliability and surrogate endpoints, Mendelian randomization, binding equilibria, Starling forces, sensor lag and robot-joint budgets. The package count with only one new lesson is now small; the remaining distance to a semester course is week-by-week sequencing, graded work and human review.

## Update after the outcome-linking lessons (2026-10-08, eighth pass)

Written by an AI coding assistant. Twelve lessons were written specifically for the 19 course outcomes that no lesson objective addressed, so every outcome in every package now has at least one lesson objective and practice items behind it. Twelve packages are at 0.3.0. This closes a measured mapping gap; it does not make any package a semester course, and the validator's outcome-to-assessment warning remains because assessments do not list outcome ids directly. Nothing is reviewed or graded.

## Update after the biomechanics, physics and engineering lessons (2026-10-08, sixth pass)

Written by an AI coding assistant. Nine more lessons connect the engineering and physics packages to the biology track: cell indentation and viscoelasticity, stiffness versus ligand density, least-squares calibration, Markov chains for cell states, long-bone bending, impact forces, the membrane as a capacitor, sensor loading and ADC resolution, and incubator temperature control. Calculus 3 and robotics followed in a seventh pass, so every package now has at least one lesson-length original reading (19 of 101 outcomes still unlinked). Unlinked course outcomes: 25 of 101. Nothing is reviewed or graded; a lesson-length reading per package is still far from a semester course.

## Update after the chemistry and mathematics lessons (2026-10-08, fifth pass)

Written by an AI coding assistant. Eight lessons now give the biology packages their quantitative footing: solution preparation and error, buffers, rate laws, functional groups and slow chemical damage, growth-model derivatives, accumulation integrals, a perfused-chamber ODE with a numerical check, and equilibrium stability. Each uses synthetic values and connects to a biology or bioengineering use. Nine packages remain at legacy depth: calculus 3, linear algebra, physics mechanics, physics electromagnetism, circuits, signals and control, robotics, statics and materials, and cellular biomechanics. Unlinked course outcomes fell to 48 of 101. Nothing is reviewed or graded.

## Update after eight lessons in genetics, biochemistry, physiology and biomaterials (2026-10-08, third pass)

Written by an AI coding assistant. Development continued in the four thin packages closest to the owner's interest in aging and regeneration. Each went from 0.1.0 to 0.2.0 with two original lessons of about 810 to 990 words, a worked problem that differs from the body text, six or seven practice items whose keys are computed in the authoring script and graded to full credit by the real grader, and four retrieval cards: Hardy–Weinberg departures and carrier frequency; heritability and polygenic scores; enzyme kinetics and inhibition fingerprints; actual versus standard free energy, coupling and redox; oxygen delivery and the Fick principle; renal clearance; hydrogel degradation and release time scales; scaffold porosity, stiffness and permeability. No new third-party sources were added; the modules reuse each package's existing curriculum-comparator source ids. Course outcomes with no linking lesson objective fell from 79 to 65 of 101. A fourth pass then added genetics lessons 7 (three-point mapping and interference) and 8 (designing a controlled perturbation experiment), which link the last two genetics outcomes (63 of 101 remain unlinked).

What is still true: 15 of the 25 packages have only legacy readings; none of these lessons was reviewed by a subject-matter expert; everything is formative and ungraded.

## Update after the toggle and the first deep lessons outside cell biology (2026-10-08, second pass)

Written by an AI coding assistant. Direction from the owner: assessments need not be protected, so protection became an explicit toggle (`open` by default, `protected` opt-in, with an operator override), and development continued toward the topics the owner cares about (aging, regeneration, research and engineering practice).

New original lessons of roughly 700 to 1,200 words each, with synthetic data, worked examples and computed practice keys: six in geroscience (genome instability and repair; proteostasis, autophagy and mitochondria; nutrient sensing and lifespan interventions; regeneration across species; reading an aging-intervention paper; evidence tiers from model to human), one in statistics (time-to-event data), and one each in transport (oxygen limits in thick constructs), bioreactors (sizing oxygen supply) and programming (testing a scientific function and provenance). The geroscience lessons deliberately do not claim that any intervention slows or reverses human aging; they teach how to judge such claims. Ten lesson-length readings now exist outside cell biology, where before the other packages averaged about 70 words per lesson.

What is still true: 19 of the 25 packages still have only the 60 to 80-word legacy readings plus one practice item per objective; no lesson was reviewed by a subject-matter expert; references were checked for existence, not for support of each sentence; nothing is graded. The largest remaining gap is still authored instruction in the thin packages, followed by named human review.

## Earlier update after the homework, lab and objective-coverage increment (2026-10-08)

Written by an AI coding assistant. The 2026-10-06 review found grader development ahead of instruction. This increment adds content rather than machinery: open formative companions for Homework 2 to 8, a third synthetic lab, specification-only documents for the midterm, final and project, and one practice item for each of the 96 lesson objectives that had none in the other 24 packages (plus two for the lesson-3 objective in cell-biology). All 8 homework companions and 3 labs are public, ungraded and unreviewed.

What is measured now (see [the generated gap report](COURSE_GAP_REPORT.md)): every lesson objective has an assessment mapping and a practice item; 91 of 101 course outcomes are still not linked from any lesson objective, so the `objective-coverage` validator warning remains at 25. Eight items per thin package is still far below a course, the legacy readings are still about 60 to 80 words each, and 98 legacy-depth warnings remain. Adding items did not add teaching; those readings need real authoring. The cell-biology package is the only one with a deep lesson sequence.

What stayed true: no maturity label changed, nothing is graded, no reviewer is named, no answer package was created, and the specification documents are not exams. The next useful work needs people: a qualified reviewer for the cell-biology package, a decision on whether to build protected assessments at all, and authoring of the thin packages' lessons.

## Earlier update after Geroscience & Regenerative Biology lessons (2026-10-07)

Geroscience & Regenerative Biology advances from 0.1.0 to 0.2.0 and remains `partial` and unreviewed. Each of its four compact legacy units is now followed by an original lesson of roughly 1,100–1,300 words: survival curves, Gompertz mortality hazards and healthspan endpoints; genetic and pharmacologic senescent-cell clearance with dropout-aware efficacy and mechanism-linked toxicity; clonal hematopoiesis and heterochronic blood-sharing evidence, including an assay-specificity case; and epigenetic clocks with partial reprogramming. All tables are explicitly synthetic teaching data. Twenty-one link-only scientific references were checked against PubMed records and summarized qualitatively; no source text, figure or dataset is reproduced. The package gains 15 formative items (numeric, single-choice, multiple-select and data-interpretation), 16 retrieval cards, objective-to-outcome links for all 20 lesson objectives, and corrected objective tags on its four legacy checks. A new content test independently recalculates every new numerical key. The first objective of each legacy unit still has no tagged item, and there is no schedule, homework, laboratory, exam or capstone. Repository inventory: 25 partial packages, 132 lessons, 211 formative questions, 275 cards and 25 cases.

## Update after spaced retrieval and unassessed-objective visibility (2026-10-07)

Two P2 learner-coverage findings are addressed. First, authored lesson objectives that no practice item is tagged to now remain in the gradebook as `no items` instead of disappearing; this also fixes a response-schema defect in the uncommitted draft of that change, which would have rejected the new status for any real course with an untagged objective. Second, retrieval cards now have persisted spaced review: enrolled learners self-rate a revealed card, the server appends the rating with a digest of the card text and computes the next review with the deterministic `retrieval-schedule-v1` rule, and a course Review queue separates due, not-yet-reviewed and later cards. Editing a card restarts its schedule, export/delete cover the new records, and ratings never alter practice scores, objective evidence or grades. Typed week/calendar views remain open, and no claim is made that this schedule improves retention for these materials. Course maturity is unchanged: all 25 packages remain `partial`.

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
| P2 learner coverage | Addressed 2026-10-07: retrieval ratings, history and a due queue persist, and unassessed objectives stay visible as `no items`. Course DTO/UI still omit weekly scheduling. | Expose typed weeks and a learner calendar. |
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

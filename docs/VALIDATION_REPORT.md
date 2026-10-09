# Validation report

## Scope and result

2026-10-06; synthetic local learner data only. Milestones 1 and 2 are implemented. Milestone 3 remains partial; deterministic graders and prototype graded-assignment and review workflows are described below. A Milestone 4 curriculum-map increment is implemented and tested, while subject-matter review and map refinement remain. All 25 course packages are **partial**; zero are beta, complete or externally reviewed. Human score review is limited to saved attempts and does not constitute course-content review. No semester equivalence, university credit, security certification or public production deployment is asserted.

## Current increment: General Chemistry II lessons, relaxation lab and proposed schedule (0.4.0, 2026-10-09)

Developed with Codex assistance. General Chemistry II advances from 0.3.1 to 0.4.0 while remaining partial, unreviewed and formative-only. Seven original lessons develop free energy and equilibrium, coupled acid mass/charge balance, empirical/mechanistic rates, reversible/sequential kinetics, electrochemical amount accounting, ligand balance and limited coordination models, and competing solubility/complexation. One synthetic reporting-background/plateau lab and a proposed 14-week sequence complete the increment. There are 71 new items and 32 cards; the package contains 15 readings, 97 items and 52 cards. Week 12 pairs two readings. All 26 preexisting question objects and 20 cards are unchanged.

Separate calculations check all 64 numeric keys, including 18 preserved keys, and all 14 CSV cells. Root finding, component ODE integration, acid ratio normalization and free-metal balance provide alternative calculations alongside conservation and domain checks. The lab distinguishes the independent blank background from the independent equilibrium plateau, fits t00/t20 and predicts reserved t60. New numeric checks request bare numbers in stated scales; ten preserved items require units, with no significant-figure/dimensional enforcement added. The [AI-assisted check record](reviews/ai-assisted/general-chemistry-2-0.4.0.md) documents methods and repairs. The same AI assistant authored content and checks; this is not independent chemical or human review.

Three primary OpenStax Chemistry 2e pages were retrieved as link-only factual references for free energy, mechanisms and coordination properties. No teaching prose, worked problem, figure or dataset was imported, source permissions were not broadened, and no new paper identifier was introduced.

| Command/check (Linux development container, Python 3.12.3) | Result |
|---|---|
| `python -B tools/validate_content.py` | PASS: 25 packages, 337 lessons, 1816 questions, 1088 cards, 25 cases; 0 errors; 98 legacy-depth warnings |
| `bash /workspace/.claude/skills/courselab-dev/scripts/verify.sh --log-dir /workspace/courselab-session-artifacts/codex-general-chemistry-2-2026-10-09/verification` | PASS: content, legacy (7), security (705 source files, 0 findings), ruff, root (1730), backend (3889 passed, 2 existing symbolic-builder skips) |
| `python -B /workspace/courselab-session-artifacts/codex-general-chemistry-2-2026-10-09/check_grader.py` | PASS: all 97 package items earn full credit |
| `python -B -m pytest tests/content/test_general_chemistry_two_recalculations.py tests/content/test_new_geroscience_and_statistics_lessons.py tests/content/test_learner_visible_number_formatting.py -q -p no:cacheprovider` | PASS after presentation/assertion repairs: 503 focused checks |
| `ruff check tests/content/test_general_chemistry_two_recalculations.py` | PASS after renaming three ambiguous variables; file formatted |
| `python -B tools/objective_coverage.py --check docs/COURSE_GAP_REPORT.md` | PASS: generated report matches |
| `python3 -B /workspace/.claude/skills/regen-guardrails/scripts/claims_scan.py --repo uniStemCourseSimulators` | PASS: 0 HIGH, MED or LOW findings |

Draft length inspection prompted a substantive reversible initial-condition paragraph before integration. An arithmetic spot-check corrected displayed ln K from 38.683145 to 38.683746; the practice key was already correct. Initial lint failed on three ambiguous variable names, then passed after renaming and formatting. The first focused suite had 493 passes and ten failures: seven standard limitation headings were missing, two number-format checks found long decimal displays, and one exact floating-point comparison needed a tolerance. Standard sections, scientific-notation displays and a tolerant assertion repaired these checks; numeric keys did not change. The complete real-grader check passed all 97 items on its first run, and all numeric-key calculations passed on their first run. The full six-step local run passed on its first run. A preliminary nonexistent `cases/` path read was replaced by the manifest's preserved self-assessment entry.

Logs remain outside git in `courselab-session-artifacts/codex-general-chemistry-2-2026-10-09/verification`. Frontend checks, the Docker Compose application stack and Playwright were not run locally for this content increment; publication CI runs them. No person reviewed the chemistry or measured workload.

## Previous increment: General Chemistry I lessons, buffer lab and proposed schedule (0.4.0, 2026-10-09)

Developed with Codex assistance. General Chemistry I advances from 0.3.1 to 0.4.0 while remaining partial, unreviewed and formative-only. Seven new lessons cover atom/amount/photon accounting, bonding and geometry, reaction extent, gases and model deviations, energy and calorimetry, equilibrium and activity conventions, and acid–base discrepancy checks. One synthetic buffer lab and a proposed 14-week sequence complete the increment. There are 71 new public items and 32 cards; the package contains 14 readings, 91 items and 48 cards. All 20 preexisting question objects and 16 cards are unchanged.

Separate calculations check all 59 numeric keys, including 13 preserved keys, and all 14 CSV summary cells. The lab distinguishes a common reporting offset, independently supplied composition, nominal inventory approximations and full ideal charge balance beyond base exhaustion. Six authored items require significant figures, three also require units; explicit backend responses exercise conversions, precision, wrong units and near misses. The [AI-assisted check record](reviews/ai-assisted/general-chemistry-1-0.4.0.md) documents methods, repairs and source-access limits. The same AI assistant authored content and checks; this is not independent chemical or human review.

Two factual references were added as link-only records with no quotation, adaptation or redistribution permissions. NIST's defining-constants page was retrieved; the official indexed IUPAC pH definition was verified, but direct page, plain-text and PDF access returned HTTP 403. This restriction is disclosed in the source record and course limitations. No full-page IUPAC access or imported teaching material is claimed.

| Command/check (Linux development container, Python 3.12.3) | Result |
|---|---|
| `python -B tools/validate_content.py` | PASS: 25 packages, 329 lessons, 1745 questions, 1056 cards, 25 cases; 0 errors; 98 legacy-depth warnings |
| `bash /workspace/.claude/skills/courselab-dev/scripts/verify.sh --log-dir /workspace/courselab-session-artifacts/codex-general-chemistry-1-2026-10-09/verification` | PASS: content, legacy (7), security (694 source files, 0 findings), ruff, root (1615), backend (3747 passed, 2 existing symbolic-builder skips) |
| `python -B /workspace/courselab-session-artifacts/codex-general-chemistry-1-2026-10-09/check_grader.py` | PASS: all 91 package items earn full credit, including precision formatting and the repaired CSV specification |
| `python -B -m pytest tests/content/test_general_chemistry_one_recalculations.py tests/content/test_new_geroscience_and_statistics_lessons.py tests/content/test_learner_visible_number_formatting.py -q -p no:cacheprovider` | PASS: 473 focused checks before the CSV output-column repair; the full run covers the repaired specification |
| `python -B -m pytest tests/test_general_chemistry_precision.py -q -p no:cacheprovider` from `backend/` | PASS: 6 precision/unit checks |
| `ruff check tests/content/test_general_chemistry_one_recalculations.py backend/tests/test_general_chemistry_precision.py` | PASS on the initial run; both files subsequently formatted |
| `python -B tools/objective_coverage.py --check docs/COURSE_GAP_REPORT.md` | PASS: generated report matches |
| `python3 -B /workspace/.claude/skills/regen-guardrails/scripts/claims_scan.py --repo uniStemCourseSimulators` | PASS: 0 HIGH, MED or LOW findings |

The first two-file focused run had 87 passes and one long-decimal display failure; photon feedback was shortened without changing its rounded key. The initial precision suite had five passes and one failure because authored kPa units were outside the current explicit unit grammar. The pressure prompt/key/tolerance now use correctly rounded pascals for the same physical result, and Pa/MPa conversions pass. The first complete real-grader check rejected the uppercase output column `mean_pH`; upload instructions and specifications now use `mean_ph`, while the supplied raw-data header `reported_pH` remains unchanged. The complete grader rerun passed all 91 items. No chemical calculation key failed, and the full six-step local run passed on its first run. A preliminary report-check invocation used unavailable bare `python`; rerunning with the configured venv interpreter passed.

Logs remain outside git in `courselab-session-artifacts/codex-general-chemistry-1-2026-10-09/verification`. Frontend checks, the Docker Compose application stack and Playwright were not run locally for this content increment; publication CI runs them. No person reviewed the chemistry or measured workload.

## Previous increment: Calculus III lessons, flux-balance lab and proposed schedule (0.4.0, 2026-10-09)

Developed with Codex assistance. Calculus III advances from 0.3.1 to 0.4.0 while remaining partial, unreviewed and formative-only. Seven new lessons cover vector geometry, partial and total derivatives, Hessians and feasible constraints, multiple integrals and Jacobians, line integrals and Green, surface flux and divergence, and Stokes with spatial conservation. One synthetic boundary-flux lab and a proposed 14-week sequence complete the increment. There are 71 new public items and 32 cards; the package contains 14 readings, 91 items and 48 cards. All 20 preexisting item objects and 16 cards are unchanged.

Separate calculations check all 62 numeric keys, including 16 preserved keys, and all 12 CSV summary checks. The lab distinguishes signed outward transfer, face-area weighting, a common offset and the source/storage assumptions required for a sink interpretation. The [AI-assisted check record](reviews/ai-assisted/calculus-3-0.4.0.md) documents methods and repairs. The same AI assistant authored content and checks; this is not independent mathematical or human review.

| Command/check (Linux development container, Python 3.12.3) | Result |
|---|---|
| `python -B tools/validate_content.py` | PASS: 25 packages, 321 lessons, 1674 questions, 1024 cards, 25 cases; 0 errors; 98 legacy-depth warnings |
| `bash /workspace/.claude/skills/courselab-dev/scripts/verify.sh --log-dir /workspace/courselab-session-artifacts/codex-calculus-3-2026-10-09/verification` | PASS: content, legacy (7), security (682 source files, 0 findings), ruff, root (1516), backend (3599 passed, 2 existing symbolic-builder skips) |
| `python -B /workspace/courselab-session-artifacts/codex-calculus-3-2026-10-09/check_grader.py` | PASS: all 91 package items earn full credit |
| `python -B -m pytest tests/content/test_calculus_three_recalculations.py tests/content/test_new_geroscience_and_statistics_lessons.py tests/content/test_learner_visible_number_formatting.py -q -p no:cacheprovider` | PASS: 459 focused checks |
| `ruff check tests/content/test_calculus_three_recalculations.py` | PASS after style repairs and formatting |
| `python -B tools/objective_coverage.py --check docs/COURSE_GAP_REPORT.md` | PASS: generated report matches |
| `python3 -B /workspace/.claude/skills/regen-guardrails/scripts/claims_scan.py --repo uniStemCourseSimulators` | PASS: 0 HIGH, MED or LOW findings |

An authoring-script quoted-apostrophe syntax error was repaired before mutation. A provisional box total was corrected to 8 before integration by comparing faces and volume divergence. The initial lint run autofixed 13 assigned lambdas and still failed on one ambiguous variable name, then passed after its repair. The first two-file focused suite passed 88 checks. Stronger numerical methods were added before the full run; the first expanded suite then had 458 passes and one exact floating-point equality failure in parameter invariance. A tight tolerance repaired that assertion; the final suite passed 459. No authored mathematical key failed, and the full six-step local run passed on its first run.

Logs remain outside git in `courselab-session-artifacts/codex-calculus-3-2026-10-09/verification`. Frontend checks, the Docker Compose application stack and Playwright were not run locally for this content increment; publication CI runs them. No person reviewed the mathematics or measured workload.

## Previous increment: Calculus II lessons, force-work lab and proposed schedule (0.4.0, 2026-10-09)

Developed with Codex assistance. Calculus II advances from 0.3.2 to 0.4.0, retaining partial, unreviewed and formative-only status. Seven new lessons cover integration structure and domains, improper limits and comparison, positive and alternating series, power-series radii/endpoints, Taylor and accumulated error, and geometric/radial integrals. One synthetic force-work lab and a proposed 14-week sequence complete this increment. There are 71 new items and 32 cards; the package contains 14 readings, 91 items and 48 cards. All 20 preexisting items and 16 preexisting cards are unchanged.

Separate calculations check all 62 numeric keys, including 16 preserved keys, and all ten lab CSV cells. The lab distinguishes a known force offset, numerical sampling, input rounding and an integrated geometric-tail certificate. The [AI-assisted record](reviews/ai-assisted/calculus-2-0.4.0.md) documents methods, focused-check failures and repairs. The same AI assistant authored content and checks; these are not independent mathematical or human review.

| Command/check (Linux development container, Python 3.12.3) | Result |
|---|---|
| `python -B tools/validate_content.py` | PASS: 25 packages, 313 lessons, 1603 questions, 992 cards, 25 cases; 0 errors; 98 legacy-depth warnings |
| `bash /workspace/.claude/skills/courselab-dev/scripts/verify.sh --log-dir /workspace/courselab-session-artifacts/codex-calculus-2-2026-10-09/verification` | PASS: content, legacy (7), security (670 source files, 0 findings), ruff, root (1417), backend (3457 passed, 2 existing symbolic-builder skips) |
| `python -B /workspace/courselab-session-artifacts/codex-calculus-2-2026-10-09/check_grader.py` | PASS: all 91 package items earn full credit |
| `python -B -m pytest tests/content/test_calculus_two_recalculations.py tests/content/test_new_geroscience_and_statistics_lessons.py tests/content/test_learner_visible_number_formatting.py -q -p no:cacheprovider` | PASS: 442 focused checks |
| `ruff check tests/content/test_calculus_two_recalculations.py` | PASS after style correction and formatting |
| `python -B tools/objective_coverage.py --check docs/COURSE_GAP_REPORT.md` | PASS: generated report matches |
| `python3 -B /workspace/.claude/skills/regen-guardrails/scripts/claims_scan.py --repo uniStemCourseSimulators` | PASS: 0 HIGH, MED or LOW findings |

The initial focused two-file run had 83 passes and two display-format failures; small errors and the long logarithm bound now use scientific notation in learner-facing prose. Exact numeric keys are unchanged. A lint autofix converted one assigned lambda to a named function. The first three-file run passed 428 checks before inspection caught a missed extension of the common lesson list; the corrected list adds fourteen structural/objective checks and the final run passed 442. No mathematical key failed, and the full six-step run above passed on its first run. Logs remain outside git under `courselab-session-artifacts/codex-calculus-2-2026-10-09/verification`. Frontend checks, the Docker Compose application stack and Playwright were not run locally for this increment; publication CI runs them. No person reviewed the mathematics or measured workload.

## Previous increment: Calculus I lessons, washout lab and proposed schedule (0.4.0, 2026-10-09)

Developed with Codex assistance. Calculus I advances from 0.3.1 to 0.4.0, retaining partial, unreviewed and formative-only status. Seven new lessons cover limits and derivative definitions, composite/implicit and related rates, constrained optimization, accumulation/substitution, numerical calculus and error, local approximation/Newton iteration, and the original semilog washout case. One synthetic-data lab and a proposed 14-week sequence complete this increment. There are 71 new items and 32 cards; the package has 14 readings, 92 items and 48 cards. All 21 preexisting item objects are unchanged.

Separate calculations check all 64 numeric keys, including the 18 preexisting ones, and all 14 lab CSV cells. The lab distinguishes a known additive background from an apparent zero-background decay rate and checks a reserved late prediction. The [AI-assisted record](reviews/ai-assisted/calculus-1-0.4.0.md) documents methods, failed focused checks and authoring repairs. These checks are not human or independent scientific review.

| Command/check (Linux development container, Python 3.12.3) | Result |
|---|---|
| `python -B tools/validate_content.py` | PASS: 25 packages, 305 lessons, 1532 questions, 960 cards, 25 cases; 0 errors; 98 legacy-depth warnings |
| `bash /workspace/.claude/skills/courselab-dev/scripts/verify.sh --log-dir /workspace/courselab-session-artifacts/codex-calculus-1-2026-10-09/verification` | PASS: content, legacy (7), security (660 files, 0 findings), ruff, root (1321), backend (3315 passed, 2 existing symbolic-builder skips) |
| `python -B /workspace/courselab-session-artifacts/codex-calculus-1-2026-10-09/check_grader.py` | PASS: all 92 package items earn full credit, including the preserved symbolic item |
| `python -B -m pytest tests/content/test_calculus_one_recalculations.py tests/content/test_new_geroscience_and_statistics_lessons.py tests/content/test_learner_visible_number_formatting.py -q -p no:cacheprovider` | PASS: 421 focused checks |
| `python -B -m pytest tests/content/test_calculus_one_recalculations.py tests/content/test_learner_visible_number_formatting.py -q -p no:cacheprovider` | PASS after style conversion: 78 checks |
| `python -B tools/objective_coverage.py --check docs/COURSE_GAP_REPORT.md` | PASS: generated report matches |
| `python3 -B /workspace/.claude/skills/regen-guardrails/scripts/claims_scan.py --repo uniStemCourseSimulators` | PASS: 0 HIGH, MED or LOW findings |

The first focused run had 77 passes and one test-string membership error; the assertion was repaired. The first lint run found 21 assigned-lambda style violations, converted to named functions before the full run. No numeric key failed, and the full verification above passed on its first run. Logs remain outside git under `courselab-session-artifacts/codex-calculus-1-2026-10-09/verification`. Frontend, the Docker Compose application stack and Playwright were not run locally for this increment; publication CI runs them. No person reviewed the content or measured workload.

## Previous increment: linear algebra lessons, sensor lab and proposed schedule (0.3.0, 2026-10-09)

Claude's four recovered drafts were corrected and extended with Codex assistance. Linear Algebra for Modeling & Robotics advances from 0.2.1 to 0.3.0, retaining partial, unreviewed and formative-only status. Seven new lessons cover rank and identifiability, projection and QR, symmetric spectra, SVD, conditioning and ridge, centered PCA, and the existing displacement case. One synthetic sensor-geometry lab and a proposed 14-week schedule complete this increment. There are 71 new public items and 32 cards; the package has 14 readings, 91 items and 48 cards. The 20 preexisting items are unchanged.

All 69 numeric item keys and four CSV cells agree with recalculation by separate matrix operations. The lab explicitly distinguishes paired opposite demonstration errors from its separate independent-noise model. The [AI-assisted check record](reviews/ai-assisted/linear-algebra-0.3.0.md) documents corrections, failed runs and limits; these checks are not human review.

| Command/check (Linux development container, Python 3.12.3) | Result |
|---|---|
| `python -B tools/validate_content.py` | PASS: 25 packages, 297 lessons, 1461 questions, 928 cards, 25 cases; 0 errors; 98 legacy-depth warnings |
| `bash /workspace/.claude/skills/courselab-dev/scripts/verify.sh --log-dir /workspace/courselab-session-artifacts/codex-linear-algebra-2026-10-09/verification-final` | PASS: content, legacy (7), security (649 files, 0 findings), ruff, root (1232), backend (3173 passed, 2 existing symbolic-builder skips) |
| `python -B /workspace/courselab-session-artifacts/claude-resume-2026-10-08/selfcheck.py linear-algebra linear-algebra-` | PASS: all 91 package items earn full credit |
| `python -B -m pytest tests/content/test_linear_algebra_recalculations.py tests/content/test_new_geroscience_and_statistics_lessons.py -q -p no:cacheprovider` | PASS: 407 focused content checks |
| `python -B -m pytest tests/content/test_content_validation.py::test_private_assessment_validator_loads_and_validates_key_only_from_separate_root tests/content/test_learner_visible_number_formatting.py tests/content/test_linear_algebra_recalculations.py -q -p no:cacheprovider` | PASS: 82 regression checks |
| `python -B tools/objective_coverage.py --check docs/COURSE_GAP_REPORT.md` | PASS: generated report matches |
| `python3 -B /workspace/.claude/skills/regen-guardrails/scripts/claims_scan.py --repo uniStemCourseSimulators` | PASS: 0 HIGH, MED or LOW findings |

The first full root run had 1229 passes and three failures: a stale synthetic private-fixture inventory count, a long decimal display, and an earlier literal test assertion loaded before its repair. The fresh full run above includes all corrections. Logs are retained outside git in `courselab-session-artifacts/codex-linear-algebra-2026-10-09/verification-final`. Frontend, the Docker Compose application stack and Playwright were not run locally for this increment; publication CI runs them. No person reviewed this content or measured its workload.

## Previous patch: differential equations prompt clarification (0.3.1, 2026-10-08)

Written by Codex. Three Euler-boundary prompts now ask for a nonnegative result and explain the zero value
at equality; the resonance statements item specifies the lesson's lightly damped, directly forced system.
No key, tolerance, points, option order or objective mapping changed, as checked against commit `2c930c9`.
The version and syllabus advance to 0.3.1; all counts and partial/unreviewed/formative-only labels stay the same.
Review: [differential-equations-0.3.1.md](reviews/ai-assisted/differential-equations-0.3.1.md).

- `python -B /workspace/courselab-session-artifacts/codex-resume-2026-10-08/check_prompt_patch.py`: all 92 solution specifications, options, points and objective mappings unchanged; the three linear Euler boundary factors are zero.
- `python -B tools/validate_content.py`: PASS, 0 errors, 98 legacy-depth warnings.
- `python -B /workspace/courselab-session-artifacts/claude-resume-2026-10-08/selfcheck.py differential-equations differential-equations-`: all 92 items earn full credit.
- `python -B -m pytest tests/content/test_new_geroscience_and_statistics_lessons.py tests/content/test_ai_assisted_checks.py -k differential_equations -q -p no:cacheprovider`: 81 passed, 967 deselected.

These checks ran in the same Linux development container and courselab venv as the full preceding run below.
The preceding commit's CI also passed both content/backend and frontend/browser jobs. No human review.

## Previous increment: differential equations gets a proposed 14-week schedule, seven lessons and a decay-fitting lab (2026-10-08, twenty-fifth pass)

Written by an AI coding assistant. Differential Equations for Living & Engineered Systems moves from 0.2.2 to 0.3.0 and stays `partial`, unreviewed and formative-only.

- **Proposed 14-week schedule** (`duration.weeks`) and a regenerated syllabus: the four short prototype units sit in weeks 1, 4, 6 and 11 beside the original lessons; week 13 is a lab and week 14 a lesson that prepares the existing course case. The manifest says the schedule is not evidence of semester equivalence.
- **Seven lessons (7 to 13)**, each about 970 to 1,180 words with a worked example, common mistakes, nine items and four cards: forced first-order systems (steps, ramps, sinusoids, decaying inputs and pulses in a perfused chamber); resonance and damping of a spring–mass–damper; phase portraits of linear systems; logistic growth (exact solution, fitting, extrapolation); linearization and bistability in a toggle switch; stiff equations and implicit methods; and a fitted model that predicts negative counts (model structure, step size, validation).
- **Virtual lab 1**: synthetic cell counts after a growth factor is removed, three wells at each of seven times (21 rows). Eight items (a 14-cell summary upload by time, the early-window decay rate, the zero crossing and the 48 h prediction of a straight-line fit, the first-order prediction at 48 h, a data-interpretation item on the ratio of observed to predicted counts, a structured item and a multiple-select item).
- **Review record:** [differential-equations-0.3.0.md](reviews/ai-assisted/differential-equations-0.3.0.md). All 74 numeric keys in the package, including the 14 that predate this pass, agree with independent recalculation (numerical integration of the chamber, the driven oscillator, the linear flows, the logistic equation, the toggle switch and the Michaelis–Menten depletion; finite-difference Jacobians; bisection for the Euler limits), as do the lab keys against its CSV and the numbers the lessons quote without asking for them. All 71 new items earn full credit under the real grader on the first run. Seven drafting problems, including a false statement about a forecast exceeding the carrying capacity, were fixed before the commit.
- Tests: 78 recalculation and statement checks for differential equations; the schedule, the no-protocol statements, the syllabus outcomes and the lab keys against its CSV have tests; the inventory pins moved to 289 lessons, 1,390 questions and 896 cards.

Codex continued the staged pass on 2026-10-08, recovered Claude's completed verification, reread the new
lessons and lab, and corrected five further details documented in the review record. These include the strict
Euler stability bound (at least 251 equal steps, rather than 250), nonnegativity at the positivity boundary,
degenerate phase portraits, the capstone's distinguishable residuals, and the resonance peak's damping
condition and forcing mechanism. No answer key or tolerance changed. The existing recalculation test now
checks both sides of the integer Euler step bound. A fresh full run after those corrections passed:

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 289 lessons, 1390 questions, 896 cards, 25 cases; 0 errors; 98 disclosed legacy-depth warnings |
| `bash /workspace/.claude/skills/courselab-dev/scripts/verify.sh --log-dir /workspace/courselab-session-artifacts/codex-resume-2026-10-08/de-verification` | PASS: content, legacy (7), security (637 files, 0 findings), ruff, root (1140), backend (3031 passed, 2 symbolic-builder checks skipped) |
| `python /workspace/courselab-session-artifacts/claude-resume-2026-10-08/selfcheck.py differential-equations differential-equations-` | PASS: all 92 package items earn full credit under the real grader |
| `python3 -B /workspace/.claude/skills/regen-guardrails/scripts/claims_scan.py --repo uniStemCourseSimulators` | PASS: 0 HIGH, MED or LOW findings |

Local logs are retained outside the repository in the workspace's `courselab-session-artifacts/codex-resume-2026-10-08/de-verification` directory. Not run locally: frontend checks, the Docker Compose application stack, or Playwright for this pass. Not reviewed by a person.

## Previous increment: signals and control gets a proposed 14-week schedule, seven lessons and a step-test identification lab (2026-10-08, twenty-fourth pass)

Written by an AI coding assistant. Signals, Systems & Feedback Control moves from 0.3.1 to 0.4.0 and stays `partial`, unreviewed and formative-only.

- **Proposed 14-week schedule** (`duration.weeks`) and a regenerated syllabus: the four short prototype units sit in weeks 1, 4, 8 and 12 beside the original lessons; week 11 is a lab and week 14 a lesson that prepares the existing course case. The manifest says the schedule is not evidence of semester equivalence.
- **Seven lessons (7 to 13)**, each about 960 to 1,290 words with a worked example, common mistakes, eight or nine items and four cards: poles, zeros, partial fractions and the final value theorem; second-order systems (damping, overshoot, a pressure line); Bode plots (decibels, phase, delay); stability margins (gain, phase and delay margins); PI control (cancellation tuning, Ziegler–Nichols, windup); sampling, aliasing and a discrete PI controller; and a sensor filter that makes a fast loop oscillate (phase lag, crossover, a safe retuning sequence).
- **Virtual lab 1**: synthetic step tests of an incubator-like chamber at three power levels, two runs of 61 samples each (366 rows). Nine items (a 9-cell summary upload, gain, delay, an interpolated 63.2% time, time constant, a PI gain, a data-interpretation item on the linearity of the gain, a structured item and a multiple-select item).
- **Review record:** [signals-control-0.4.0.md](reviews/ai-assisted/signals-control-0.4.0.md). All 73 numeric keys in the package, including the 13 that predate this pass, agree with independent recalculation (numerical integration, bisection on the complex frequency response, a DFT for the aliases and a delay-differential simulation of the loop), as do the lab keys against its CSV and the numbers the lessons quote without asking for them. All 71 new items earn full credit under the real grader on the first run. Seven drafting problems, including a dataset that was only 97.5% settled and three schema violations, were fixed before the commit.
- Tests: 78 recalculation and statement checks for signals and control; the schedule, the no-controller-settings statements, the syllabus outcomes and the lab keys against its CSV have tests; the inventory pins moved to 281 lessons, 1,319 questions and 864 cards.

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 281 lessons, 1319 questions, 864 cards, 25 cases; 0 errors; 98 disclosed legacy-depth warnings |
| `verify.sh` | see the PROGRESS.md entry for this pass |

Not run: frontend checks, Docker Compose, Playwright for this pass. Not reviewed by a person.

## Previous increment: statics and materials gets a proposed 14-week schedule, seven lessons and a fatigue-lives lab (2026-10-08, twenty-third pass)

Written by an AI coding assistant. Statics & Mechanics of Materials moves from 0.3.2 to 0.4.0 and stays `partial`, unreviewed and formative-only.

- **Proposed 14-week schedule** (`duration.weeks`) and a regenerated syllabus: the four short prototype units sit in weeks 1, 3, 4 and 8 beside the original lessons; week 12 is a lab and week 14 a lesson that prepares the existing course case. The manifest says the schedule is not evidence of semester equivalence.
- **Seven lessons (7 to 13)**, each about 1,050 to 1,520 words with a worked example, common mistakes, eight or nine items and four cards: stress concentrations (holes, notches, the fatigue notch factor); fatigue (Basquin, Goodman, Miner); buckling of slender struts (Euler load, slenderness); principal stresses, Mohr's circle and the Tresca and von Mises criteria; beam deflection and the flexural modulus; brittle strength and the Weibull distribution; and a failure analysis and accelerated test plan for a scaffold that meets a static strength target and collapses under cyclic perfusion.
- **Virtual lab 1**: synthetic fatigue lives of 20 specimens at four stress amplitudes, with two run-outs at the cutoff (20 rows). Eight items (a 12-cell summary upload by level, the scatter at one level, a fitted slope and Basquin exponent, a data-interpretation item on the bias of two treatments of the run-outs, an extrapolated life, a structured item and a multiple-select item).
- **Review record:** [statics-materials-0.4.0.md](reviews/ai-assisted/statics-materials-0.4.0.md). All 74 numeric keys in the package, including the 17 that predate this pass, agree with independent recalculation, as do the lab keys against its CSV and the numbers the lessons quote without asking for them. All 68 new items earn full credit under the real grader on the first run. Eleven drafting problems, including a reversed statement, a worked example with an impossible result and a sentence on run-outs with the wrong direction of bias, were fixed before the commit.
- Tests: 78 recalculation and statement checks for statics and materials; the schedule, the no-design-basis statements, the syllabus outcomes and the lab keys against its CSV have tests; the inventory pins moved to 273 lessons, 1,248 questions and 832 cards.

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 273 lessons, 1248 questions, 832 cards, 25 cases; 0 errors; 98 disclosed legacy-depth warnings |
| `verify.sh` | see the PROGRESS.md entry for this pass |

Not run: frontend checks, Docker Compose, Playwright for this pass. Not reviewed by a person.

## Previous increment: cellular biomechanics gets a proposed 14-week schedule, seven lessons and a stiffness and ligand-density lab (2026-10-08, twenty-second pass)

Written by an AI coding assistant. Cellular Biomechanics & Mechanobiology moves from 0.2.1 to 0.3.0 and stays `partial`, unreviewed and formative-only.

- **Proposed 14-week schedule** (`duration.weeks`) and a regenerated syllabus: the four short prototype units sit in weeks 1, 5, 8 and 10 beside the original lessons; week 13 is a lab and week 14 a lesson that prepares the existing course case. The manifest says the schedule is not evidence of semester equivalence.
- **Seven lessons (7 to 13)**, each about 900 to 1,100 words with a worked example, common mistakes, seven to nine items and four cards: oscillatory rheology (storage and loss moduli); micropillar traction forces; bonds under force and the molecular clutch; cortical tension and micropipette aspiration; the Hill function and how to choose stiffness levels; applying strain to cells (engineering and true strain, Poisson contraction, strain rate); and decoupling stiffness from ligand density and mobility, which prepares the course case.
- **Virtual lab 1**: a synthetic crossed design of stiffness (three levels) and ligand density (two levels), three gels per condition and ten cells per gel (180 rows). Eight items (an 18-cell summary upload by gel and cell counts and means, main effect, ligand effect, interaction, a gel-level standard error with an interpretation, the (wrong) cell-level standard error, a structured item and a multiple-select item), four cards and a week-13 practice assessment.
- **Review record:** [cellular-biomechanics-0.3.0.md](reviews/ai-assisted/cellular-biomechanics-0.3.0.md). All 61 numeric keys in the package, including the 9 that predate this pass, agree with independent recalculation, as do the lab keys against its CSV and the numbers the lessons quote without asking for them. All 64 new items earn full credit under the real grader on the first run. Four drafting problems were found and fixed before the commit, including a first version of the lab data that contradicted its own point.
- Tests: 65 recalculation and statement checks for cellular biomechanics; the schedule, the no-protocol statements, the syllabus outcomes and the lab keys against its CSV have tests; the inventory pins moved to 265 lessons, 1,180 questions and 800 cards.

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 265 lessons, 1180 questions, 800 cards, 25 cases; 0 errors; 98 disclosed legacy-depth warnings |
| `verify.sh` | see the PROGRESS.md entry for this pass |

Not run: frontend checks, Docker Compose, Playwright for this pass. Not reviewed by a person.

## Previous increment: transport gets a proposed 14-week schedule, seven lessons and an oxygen depth-profile lab (2026-10-08, twenty-first pass)

Written by an AI coding assistant. Thermodynamics & Transport in Bioengineering moves from 0.3.2 to 0.4.0 and stays `partial`, unreviewed and formative-only.

- **Proposed 14-week schedule** (`duration.weeks`) and a regenerated syllabus: the four short prototype units sit in weeks 1, 3, 9 and 12 beside the original lessons; week 8 is a lab and week 14 a lesson that prepares the existing course case. The manifest says the schedule is not evidence of semester equivalence.
- **Seven lessons (7 to 13)**, each about 900 to 1,250 words with a worked example, common mistakes, seven or eight items and four cards: transient diffusion and the error function; advection, diffusion and the Péclet number (with the mass-transfer coefficient); oxygen in a spheroid (critical radius, anoxic core and rim); Michaelis–Menten uptake and the limits of zero order; lumped heat transfer and the Biot number; residence time, wash-in and washout and tanks in series; and a perfused construct with a hypoxic center, which prepares the course case.
- **Virtual lab 1**: synthetic oxygen depth profiles in cell-laden slabs of three thicknesses (three constructs each, 81 rows). Eight items (a 12-cell summary upload, a consumption rate, a critical thickness, the depth at which oxygen reaches zero, an anoxic thickness, a single-choice item, a structured item and a multiple-select item), four cards and a week-8 practice assessment.
- **Review record:** [transport-0.4.0.md](reviews/ai-assisted/transport-0.4.0.md). All 67 numeric keys in the package, including the 17 that predate this pass, agree with independent recalculation, as do the lab keys against its CSV and the numbers the lessons quote without asking for them (including a numerical table checked by a separate solver). All 62 new items earn full credit under the real grader on the first run. Five drafting problems were found and fixed before the commit, including a worked example whose answer was negative.
- Tests: 72 recalculation and statement checks for transport; the schedule, the no-protocol statements, the syllabus outcomes and the lab keys against its CSV have tests; the inventory pins moved to 257 lessons, 1,116 questions and 768 cards.

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 257 lessons, 1116 questions, 768 cards, 25 cases; 0 errors; 98 disclosed legacy-depth warnings |
| `verify.sh` | see the PROGRESS.md entry for this pass |

Not run: frontend checks, Docker Compose, Playwright for this pass. Not reviewed by a person.

## Previous increment: bioreactors gets a proposed 14-week schedule, seven lessons and a kLa lab (2026-10-08, twentieth pass)

Written by an AI coding assistant. Bioreactors & Tissue Culture Engineering moves from 0.3.2 to 0.4.0 and stays `partial`, unreviewed and formative-only.

- **Proposed 14-week schedule** (`duration.weeks`) and a regenerated syllabus: the four short prototype units sit in weeks 1, 5, 9 and 12 beside the original lessons; week 7 is a lab and week 14 a lesson that prepares the existing course case. The manifest says the schedule is not evidence of semester equivalence.
- **Seven lessons (7 to 13)**, each about 950 to 1,250 words with a worked example, common mistakes, eight or nine items and four cards: Monod growth and yield; chemostat steady states, washout and cell-specific perfusion; mixing and scale-up (power, tip speed, mixing time under three criteria); shear, eddies and the Kolmogorov scale; dissolved-oxygen control and the capacity limit; factorial design of experiments (effects, interactions, noise and curvature from center points); and designing a scale-down experiment, which prepares the course case.
- **Virtual lab 1**: synthetic dynamic gassing-out curves at three agitation speeds (three runs each, 63 rows). Eight items (a 9-cell summary upload, two kLa estimates, a speed exponent with an interpretation, a supportable cell density, a probe-lag check, a structured item and a multiple-select item), four cards and a week-7 practice assessment.
- **Review record:** [bioreactors-0.4.0.md](reviews/ai-assisted/bioreactors-0.4.0.md). All 65 numeric keys in the package, including the 12 that predate this pass, agree with independent recalculation, as do the lab keys against its CSV and the numbers the lessons quote without asking for them. All 65 new items earn full credit under the real grader on the first run. Seven drafting problems were found and fixed before the commit, including a statement that contradicted the lesson's own numbers and a sentence whose meaning was reversed.
- Tests: 70 recalculation and statement checks for bioreactors; the schedule, the no-protocol statements, the syllabus outcomes and the lab keys against its CSV have tests; the inventory pins moved to 249 lessons, 1,054 questions and 736 cards.

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 249 lessons, 1054 questions, 736 cards, 25 cases; 0 errors; 98 disclosed legacy-depth warnings |
| `verify.sh` | see the PROGRESS.md entry for this pass |

Not run: frontend checks, Docker Compose, Playwright for this pass. Not reviewed by a person.

## Previous increment: biomaterials gets a proposed 14-week schedule, seven lessons and a degradation time-course lab (2026-10-08, nineteenth pass)

Written by an AI coding assistant. Biomaterials & Tissue Engineering moves from 0.2.2 to 0.3.0 and stays `partial`, unreviewed and formative-only.

- **Proposed 14-week schedule** (`duration.weeks`) and a regenerated syllabus: the four short prototype units sit in weeks 1, 3, 9 and 13 beside the original lessons; week 12 is a lab and week 14 a lesson that prepares the existing course case. The manifest says the schedule is not evidence of semester equivalence.
- **Seven lessons (7 to 13)**, each about 1,000 to 1,200 words with a worked example, common mistakes, seven or eight items and four cards: protein adsorption, wettability and surface coverage; hydrogel networks, modulus and mesh size; polymer chain scission, molecular weight and erosion mode; vascular scaffold wall stress, buckling, flow and wall shear stress; biocompatibility evidence and the unit of analysis; cells for a scaffold (seeding, doublings, passages and a volume check); and reading a failure in a degrading vascular scaffold, which prepares the course case.
- **Virtual lab 1**: a synthetic degradation time course (seven time points, three specimens each, 21 rows) with molar mass, mass and modulus. Eight items (a 20-cell summary upload, bonds cleaved, a rate constant, a modulus half-time with an interpretation, a time to a threshold, the first day of mass loss, a structured item and a multiple-select item), four cards and a week-12 practice assessment.
- **Review record:** [biomaterials-0.3.0.md](reviews/ai-assisted/biomaterials-0.3.0.md). All 59 numeric keys in the package, including the 10 that predate this pass, agree with independent recalculation, as do the lab keys against its CSV and the numbers the lessons quote without asking for them. All 63 new items earn full credit under the real grader on the first run. Seven drafting problems were found and fixed before the commit, including a rate constant that would have given a wrong sense of the time scale.
- Tests: 64 recalculation and statement checks for biomaterials; the schedule, the no-protocol statements, the syllabus outcomes and the lab keys against its CSV have tests; the inventory pins moved to 241 lessons, 989 questions and 704 cards.

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 241 lessons, 989 questions, 704 cards, 25 cases; 0 errors; 98 disclosed legacy-depth warnings |
| `verify.sh` | see the PROGRESS.md entry for this pass |

Not run: frontend checks, Docker Compose, Playwright for this pass. Not reviewed by a person.

## Previous increment: statistics gets a proposed 14-week schedule, seven lessons and a nested-design lab (2026-10-08, eighteenth pass)

Written by an AI coding assistant. Probability, Biostatistics & Experimental Design moves from 0.3.2 to 0.4.0 and stays `partial`, unreviewed and formative-only.

- **Proposed 14-week schedule** (`duration.weeks`) and a regenerated syllabus, which now also lists the package's fifth outcome: the four short prototype units sit in weeks 1, 4, 6 and 8 beside the original lessons; week 12 is a lab and week 14 a lesson that prepares the existing course case. The manifest says the schedule is not evidence of semester equivalence.
- **Seven lessons (9 to 15)**, each about 1,000 to 1,400 words with a worked example, common mistakes, seven or nine items and four cards: sources of variability and pseudoreplication; comparing two groups (Welch and paired t statistics, intervals for a difference); power and sample size; regression, calibration and inverse prediction; permutation, bootstrap and rank-based methods; base rates, positive predictive value and replication; and planning a confirmatory study from a pilot, which prepares the course case on a pilot with p = 0.04 for one of 18 biomarkers.
- **Virtual lab 1**: synthetic nested readings (four animals per group, three readings each, 24 rows). Seven items (a 16-cell per-animal summary upload, a technical SD, two data-interpretation items that compare the reading-level and animal-level t tests, an intraclass correlation, a structured item and a multiple-select item), four cards and a week-12 practice assessment.
- **Review record:** [statistics-0.4.0.md](reviews/ai-assisted/statistics-0.4.0.md). All 57 numeric keys in the package, including the 17 that predate this pass, agree with independent recalculation, as do the lab keys against its CSV and the numbers the lessons quote without asking for them. All 58 new items earn full credit under the real grader. Six drafting problems were found and fixed before the commit, including two lab items that used a unit the grader does not support.
- Tests: 65 recalculation and statement checks for statistics; the schedule, the no-protocol statements, the syllabus outcomes and the lab keys against its CSV have tests; the inventory pins moved to 233 lessons, 926 questions and 672 cards.

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 233 lessons, 926 questions, 672 cards, 25 cases; 0 errors; 98 disclosed legacy-depth warnings |
| `verify.sh` | see the PROGRESS.md entry for this pass |

Not run: frontend checks, Docker Compose, Playwright for this pass. Not reviewed by a person.

## Previous increment: biochemistry gets a proposed 14-week schedule, six lessons and an enzyme-kinetics lab (2026-10-08, seventeenth pass)

Written by an AI coding assistant. Biochemistry I: Proteins, Enzymes & Metabolism moves from 0.3.2 to 0.4.0 and stays `partial`, unreviewed and formative-only.

- **Proposed 14-week schedule** (`duration.weeks`) and a regenerated syllabus: the four short prototype units sit in weeks 1, 5, 9 and 12 beside the original lessons; week 7 is a lab and week 14 a lesson that prepares the existing course case. The manifest says the schedule is not evidence of semester equivalence.
- **Six lessons (8 to 13)**, each about 1,000 to 1,250 words with a worked example, common mistakes, seven items and four cards: amino acids, charge and isoelectric points; protein folding and stability; glycolysis, energy charge and why AMP is a sensitive signal; mitochondrial bioenergetics (proton-motive force, ATP yield, leak); flux control, pool sizes and the layers of regulation; and reading a metabolic perturbation, which prepares the course case on a respiratory-chain inhibitor that lowers ATP and raises lactate.
- **Virtual lab 1**: synthetic replicate initial rates for an enzyme with and without a competitive inhibitor (36 rows). Seven items (a 10-cell summary upload, a double-reciprocal fit with an interpretation, apparent Km, an inhibition constant, a structured item and a multiple-select item), four cards and a week-7 practice assessment.
- **Review record:** [biochemistry-0.4.0.md](reviews/ai-assisted/biochemistry-0.4.0.md). All 63 numeric keys in the package, including the 15 that predate this pass, agree with independent recalculation, and the lab fit recovers the parameters its data were built from. All 49 new items earn full credit under the real grader. Six drafting problems were found and fixed before the commit, including a capstone sentence that contradicted its own numbers and a significant-figures request that the grader would have scored wrongly.
- Tests: 63 recalculation tests for biochemistry; the schedule, the no-protocol statements and the lab keys against its CSV have tests; the recalculation helper now uses the validator's absolute-plus-relative tolerance; the inventory pins moved to 225 lessons, 868 questions and 640 cards.

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 225 lessons, 868 questions, 640 cards, 25 cases; 0 errors; 98 disclosed legacy-depth warnings |
| `verify.sh` | see the PROGRESS.md entry for this pass |

Not run: frontend checks, Docker Compose, Playwright for this pass. Not reviewed by a person.

## Previous increment: physiology gets a proposed 14-week schedule, seven lessons and a scratch-assay lab (2026-10-08, sixteenth pass)

Written by an AI coding assistant. Human Physiology for Engineers moves from 0.3.2 to 0.4.0 and stays `partial`, unreviewed and formative-only.

- **Proposed 14-week schedule** (`duration.weeks`) and a regenerated syllabus: the four short prototype units sit in weeks 1, 3, 5 and 11 beside the original lessons; week 13 is a lab and week 14 a lesson that prepares the existing course case. The manifest says the schedule is not evidence of semester equivalence.
- **Seven lessons (8 to 14)**, each about 950 to 1,350 words with a worked example, common mistakes, seven or eight items and four cards: balance and feedback gain (with heat balance); membrane potential (Nernst, GHK, extracellular potassium); hemodynamics; respiratory mechanics and gas exchange (ventilation, the alveolar gas equation, compliance, shunt); skeletal muscle mechanics (length–tension, Hill's relation, power); tissue repair and closure kinetics; and compensation and reserve.
- **Virtual lab 1**: a synthetic scratch assay with a control, a migration inhibitor and a division block, four independent experiments each and five time points (60 rows). Seven items (a 9-cell summary upload, a rate with an interpretation, three ratio or speed items, a structured item and a multiple-select item), four cards and a week-13 practice assessment.
- **Review record:** [physiology-0.4.0.md](reviews/ai-assisted/physiology-0.4.0.md). All 57 numeric keys in the package, including the 17 that predate this pass, agree with independent recalculation; all 56 new items earn full credit under the real grader. Five drafting problems were found and fixed before the commit, including an inconsistent resting heat loss and a learning objective with no item.
- Tests: 57 recalculation tests for physiology (plus a check that the closed-form load for peak muscle power matches a grid search); the schedule, the no-advice statements and the lab keys against its CSV have tests; the inventory pins moved to 218 lessons, 819 questions and 612 cards.

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 218 lessons, 819 questions, 612 cards, 25 cases; 0 errors; 98 disclosed legacy-depth warnings |
| `verify.sh` | see the PROGRESS.md entry for this pass |

Not run: frontend checks, Docker Compose, Playwright for this pass. Not reviewed by a person.

## Previous increment: number-formatting defects fixed and common-mistakes sections backfilled (2026-10-08, fifteenth pass)

Written by an AI coding assistant. No answer key, tolerance or objective changed. Thirteen packages move up one patch version and stay `partial`, unreviewed and formative-only.

- **Number-formatting defects in learner-visible text.** Reading the earlier lessons for the backfill showed text such as "0.15000000000000002 mol/m³" and "2.0e-10 mmol per cell per hour". A scan of every reading, prompt, option, solution, card and worked-example summary found about 40 instances in eight packages (bioreactors, transport, biochemistry, calculus 2, differential equations, physics EM, statics and materials, programming). They came from early authoring batches that ran before the notation converter existed. They are rewritten as 2.0×10⁻¹⁰ and 0.15, or placed in code spans where they are Python literals (programming). One value, 1.12e+07, was rewritten as 1.125×10⁷ because the exact value is 1.125×10⁷ and rounding it to 1.12 or 1.13 would be arbitrary.
- **New guard.** `tests/content/test_learner_visible_number_formatting.py` scans readings (outside code spans) and learner-visible JSON text for raw exponent notation and long floating-point runs. It fails on the previous commit's content (2 failures) and passes now. The programming package is exempt because it teaches Python literals.
- **Common-mistakes sections** were added to 22 original lessons in ten packages that lacked one (biochemistry 5 and 6; biomaterials 5 and 6; bioreactors 5; differential equations 5; geroscience 5 to 14; organic chemistry 5; physiology 5 and 6; programming 5; statistics 6; transport 5). Each bullet names a mistake that the lesson's own text addresses. The two labs and the short statistics unit 5 have a different structure and were left alone. The earlier AI-assisted check of genetics had found the same gap there.
- Tests: two version pins (statistics 0.3.2, geroscience 0.5.2) were updated. No assertion about maturity or review changed.

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 210 lessons, 762 questions, 580 cards, 25 cases; 0 errors; 98 disclosed legacy-depth warnings |
| `verify.sh` | see the PROGRESS.md entry for this pass |

Not run: frontend checks, Docker Compose, Playwright for this pass. Not reviewed by a person.

## Previous increment: genetics gets a proposed 14-week schedule, six lessons and an association lab (2026-10-08, fourteenth pass)

Written by an AI coding assistant. Genetics & Genomics moves from 0.4.2 to 0.5.0 and stays `partial`, unreviewed and formative-only.

- **Proposed 14-week schedule** (`duration.weeks`) and a regenerated syllabus: the four short prototype units sit in weeks 1, 4, 9 and 11 beside original lessons; week 12 is a lab and week 14 a follow-up design lesson with the course case. The manifest says the schedule is not evidence of semester equivalence.
- **Six lessons (10 to 15)**, each 1,000 to 1,400 words with a worked example, common mistakes, six items and four cards: epistasis, complementation and modified dihybrid ratios; X-linked inheritance with Bayesian carrier risk; nondisjunction and maternal age; mutation rates, the fluctuation test and somatic mutation; measuring gene expression with normalization and false-discovery control; and the follow-up design of an association locus (fine-mapping, allele-specific expression, perturbation).
- **Virtual lab 1**: a synthetic case–control study of 100 people in two populations, three variants, with a CSV. One variant's strong pooled signal is entirely confounded by population, one is a real association that survives stratification, and one is null. Seven items (12-cell summary upload, two data-interpretation items, two numeric items, a structured item and a multiple-select item), four cards and a week-12 practice assessment.
- **Common-mistakes sections** for lessons 5 to 8, which the earlier AI-assisted check found missing.
- **Four link-only references** (records resolved; three abstracts read; one scanned 1943 paper not read, which the lesson says).
- **Learner-facing limitations** recomputed for the package; one new limitation says the family calculations give no counselling or medical advice.
- **Review record:** [genetics-0.5.0.md](reviews/ai-assisted/genetics-0.5.0.md). All 43 new keys agree with independent recalculation and earn full credit under the real grader. Seven drafting problems were found and fixed before the commit, among them a wrong oogenesis simplification and a schema violation that the validator caught.
- Tests: 24 new numeric keys are recalculated independently (50 recalculation tests in all); the schedule, the no-advice statement and the lab's keys against its CSV (including pooled, stratified and Mantel–Haenszel odds ratios) have tests; the inventory pins moved to 210 lessons, 762 questions and 580 cards.

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 210 lessons, 762 questions, 580 cards, 25 cases; 0 errors; 98 disclosed legacy-depth warnings |
| `verify.sh` | see the PROGRESS.md entry for this pass |

Not run: frontend checks, Docker Compose, Playwright for this pass. Not reviewed by a person.

## Previous increment: reviewer guide, an AI-assisted check of genetics, and stale limitation text (2026-10-08, thirteenth pass)

Written by an AI coding assistant. The owner said friends, relatives, university contacts, freelancers, and the owner with AI could all review, and that AI with data processing would do best. The repository's standard still requires actual human review for `complete` and named, qualified, independent review for `externally reviewed`. So AI checks are recorded as a separate, labelled layer that changes no label.

- **[Reviewer guide](REVIEWER_GUIDE.md)**, a [lesson review form](review-templates/lesson-review.md) and a GitHub "Course feedback" issue form. They describe three kinds of review (reader feedback, AI-assisted check, subject-matter review), what each can change, and how a named review is recorded.
- **[AI-assisted check of genetics 0.4.1](reviews/ai-assisted/genetics-0.4.1.md).** All 23 numerical keys agree with an independent recalculation, kept as tests in `tests/content/test_ai_assisted_checks.py` together with an exact noncentral-t power calculation. No key was wrong. Six text findings were fixed in genetics 0.4.2. The most important: the perturbation lesson advised 4 replicates per group, which gives about 66% power; the exact t-test needs 6 for 80%.
- **Stale learner-facing limitations** in all 25 packages were replaced with text computed from each package: items per unit and lesson, and how many numerical answers require a unit or check significant figures or dimensions. Geroscience no longer says it lacks a 14-week schedule, statistics no longer describes "one supplemental original unit", and cell biology no longer says some objectives are unassessed. These changes are folded into the unpublished x.y.1 versions, and their history entries say so.

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 203 lessons, 719 questions, 552 cards, 25 cases; 0 errors; 98 disclosed legacy-depth warnings |
| `verify.sh` | all steps PASS: root 247 passed (26 new recalculation tests); backend 1689 passed, 2 skipped; security scan 0 findings; ruff clean; legacy 7/7 |

Not run: Docker Compose, Playwright for this pass. Not reviewed by a person.

## Previous increment: browser QA of protected graded assignments, and three fixes it found (2026-10-08, twelfth pass)

Written by an AI coding assistant, after the owner asked for the protected, graded mode to be tested automatically rather than by hand. Details, commands and limits are in [QA_PROTECTED_GRADED.md](QA_PROTECTED_GRADED.md).

- **Harness.** `tools/qa/build_protected_fixture.py` builds a throwaway deployment outside the repository (genetics switched to a graded, protected policy, three QA assignments whose keys live only in a private store, a sentinel string in every private solution). `tools/qa/run_protected_e2e.sh` migrates a SQLite database and starts the API and the Vite dev server. It then runs `frontend/e2e/protected-graded.spec.ts` in Chromium. The spec is skipped in the default Compose run because the committed packages are formative-only. No committed package changed its grading mode, and no answer key was committed.
- **Defects found and fixed, each with a regression test that fails without the fix:**
  1. The grade calculation re-checked protection without the pinned source paths. Every protected graded course therefore answered 409 on its gradebook, which also hid the assessment plan and the assignment (`main.py`; `test_protected_course_gradebook_counts_private_graded_work`).
  2. Graded submissions accepted only `[a-z0-9_-]` question ids, while content ids may contain `:` and `.`. An assignment written with the usual `lesson:slug` ids could never be submitted (`schemas.py`; `test_graded_assignment_accepts_authored_colon_and_dot_question_ids`).
  3. The assignment view did not count a just-saved attempt, so the counter stayed at 0 and the form stayed open after the last allowed attempt. The server still refused the extra attempt (`GradedAssessment.tsx`; new unit test).
- **After the fixes,** both protected browser tests pass. The run covered the plan, accessibility (axe), incomplete submissions, wrong and right attempts with unit diagnosis, the attempt limit, the policy-based course grade, a human-review request, persistence after reload, refusals for past-deadline and unreleased work, and the data export. No API response or page text contained the private sentinel, `solution_spec` or `private://`.

| Command/check (this container, Python 3.12.3, Node with Vite 7, Chromium headless shell 153, 2026-10-08) | Result |
| --- | --- |
| `tools/qa/run_protected_e2e.sh` (protected spec) | first run: 3 defects; after fixes: 2 passed |
| `playwright test` (whole suite, committed content, Vite dev server instead of nginx) | 19 passed, 2 skipped (protected spec), 1 failed: the nginx-only check that `/content`, `/legacy` and `/.env` return 404, which the Vite dev server does not provide. CI runs it against nginx. |
| `verify.sh --frontend` | all steps PASS: root 221 passed; backend 1689 passed, 2 skipped; frontend 37 unit tests, lint, build (208 modules), bundle scan 0 findings; security 522 files, 0 findings; ruff clean; legacy 7/7 |

Not run: Docker Compose with a protected course, other browsers, load or security testing beyond the leak checks. Not reviewed by a person.

## Previous increment: assessments list the course outcomes they cover; syllabi brought up to date (2026-10-08, eleventh pass)

Written by an AI coding assistant, following the owner's decision that assignments can list the course outcomes they cover.

- **Outcome mapping, derived rather than asserted.** Each assessment with items now also lists the course outcomes that its own items assess: item → the lesson objective it is tagged to → that objective's `course_outcome_ids`. 255 outcome ids were added across 25 packages. Rubric-only cases list none, and neither do the 92 practice assessments of the short prototype units, whose 184 objectives are not linked to any outcome (linking them is a judgement for a subject-matter reviewer; the gap report lists them). Every course outcome is now listed by at least one assessment, so the validator's `objective-coverage` warning is gone (warnings: 123 → 98, all legacy-depth). A listed outcome means at least one item touches it, not that it is assessed in depth.
- **New validator rules.** `unsupported-outcome-mapping` rejects an outcome that none of the assessment's items assesses (including on rubric-only cases), and `syllabus-version` rejects a syllabus that does not state the manifest version.
- **Stale syllabi fixed.** 23 of 25 syllabi still said "Version: 0.1.0", listed only the four original units and described "one public formative check and two retrieval cards" per unit. They were regenerated from the manifests: current version, every lesson with its reading type and item and card counts, the current practice description and limitations. Cell biology and geroscience keep their hand-written week tables (version line updated).
- Every package moves up one patch version with a history entry (for example genetics 0.4.0 → 0.4.1, geroscience 0.5.0 → 0.5.1, cell biology 0.19.0 → 0.19.1); all stay `partial`, unreviewed and formative-only. No reading, item or key changed.
- Tests: the inventory test now asserts no objective-coverage warning; new tests check that each assessment lists exactly the outcomes its items assess, that unsupported mappings and stale syllabus versions are rejected, and that syllabi list every lesson; five version pins were updated.

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 203 lessons, 719 questions, 552 cards, 25 cases; 0 errors; 98 disclosed legacy-depth warnings |
| `verify.sh` | all steps PASS: root 221 passed; backend 1687 passed, 2 skipped; security 518 files, 0 findings; ruff clean; legacy 7/7 |

Not run for this increment: frontend checks, Docker Compose, Playwright. Not reviewed by a subject-matter expert.

## Previous increment: a proposed 14-week geroscience schedule, a lifespan lab and a design lesson (2026-10-08, tenth pass)

Written by an AI coding assistant. Geroscience & Regenerative Biology moves to 0.5.0 and stays `partial`, unreviewed and formative-only.

- **Proposed 14-week schedule** in `course.json` (`duration.weeks`) and the syllabus: weeks 1 to 12 pair the compact prototype units with the original lessons; week 13 is a lab and week 14 a design lesson with the course case. The manifest says the schedule is not evidence of semester equivalence. The syllabus sections on structure, assessment and limitations were regenerated from the manifest (the previous text still described version 0.2.0 and eight units).
- **Virtual lab 1** (`labs/01-lifespan-cohort-censoring-and-survivor-bias.md`, `labs/lifespan-cohort.csv`): 24 synthetic animals, two censored at study end, and a grip-strength measure taken only in survivors. Five items (CSV summary with recalculated keys, Kaplan–Meier median, a naive-mean lower bound, structured bias reasoning, supported conclusions), four cards, one week-13 practice assessment.
- **Lesson 16, designing a credible aging-intervention study**: endpoints, Schoenfeld's event count for a survival comparison, animals needed, and safeguards (randomization, blinding, both sexes, several sites, pre-registration).
- **Test harness fix:** `backend/tests/test_authored_items.py` wrote numeric keys as raw floats, so an integer key with a three-significant-figure requirement (821) was submitted as "821.0" and failed. It now writes keys to the required significant figures, keeping trailing zeros, as a learner would. All 1,432 authored-item checks pass.
- New tests check that every geroscience lesson is scheduled exactly once, that no assessment is graded, that the package stays partial and unreviewed, and that the lab's keys match its CSV (including a recomputed Kaplan–Meier median).

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 203 lessons, 719 questions, 552 cards, 25 cases; 0 errors; 123 disclosed warnings |
| `verify.sh` | all steps PASS: root 216 passed; backend 1687 passed, 2 skipped; security 518 files, 0 findings; ruff clean; legacy 7/7 |

Not run: frontend checks, Docker Compose, Playwright. Not reviewed by a subject-matter expert.

## Previous increment: ten research-skill lessons (2026-10-08, ninth pass)

Written by an AI coding assistant. Ten original lessons of about 820 to 900 words, each with common mistakes, a worked problem, six items and four cards: statistics (multiple testing with Bonferroni and Benjamini–Hochberg; effect sizes, confidence intervals and regression to the mean), programming (algorithmic cost and data structures; floating-point rounding and cancellation, with runnable Python snippets), geroscience (biomarker reliability, smallest detectable change and surrogate endpoints, stating no claim that any intervention changes human aging), genetics (Mendelian randomization), biochemistry (binding equilibria, ligand depletion, Hill cooperativity), physiology (Starling forces and edema), signals and control (convolution and sensor lag) and robotics (joint torque budget, encoder resolution, backlash and failure limits). Statistics, programming, biochemistry, physiology, signals and control, and robotics move to 0.3.0; geroscience and genetics to 0.4.0; all stay `partial`. 60 keys were graded to full credit. The authoring pipeline's notation converter was changed to leave fenced and inline code untouched, and a test checks that the Python snippet keeps its `1e8` literals. Two existing tests pinned the statistics and geroscience versions and were updated; their maturity and review assertions are unchanged.

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 201 lessons, 708 questions, 544 cards, 25 cases; 0 errors; 123 disclosed warnings |
| `verify.sh` (first run) | content, legacy, security (505+ files, 0 findings), ruff, backend (1665 passed, 2 skipped) PASS; root pytest 2 failed on version pins |
| `python -m pytest tests -q` after the pin update | 212 passed |

Not run: frontend checks, Docker Compose, Playwright. Not reviewed by a subject-matter expert.

## Previous increment: twelve lessons that link every course outcome (2026-10-08, eighth pass)

Written by an AI coding assistant. Twelve original lessons of about 810 to 910 words, each with common mistakes, a worked problem, six items and four cards, written for the 19 course outcomes that no lesson objective linked to: bioreactors (cell-culture mass balance), transport (perfusion tubing: balances, Reynolds number, pressure drop), calculus 1 (limits, continuity and net change), calculus 2 (Taylor error bounds), calculus 3 (constrained optimization and polar integrals), circuits (RC frequency response and aliasing), general chemistry 1 (polarity, partitioning and calorimetry), general chemistry 2 (Nernst equation and metal centers), organic chemistry (SN1/SN2 and stereochemistry), physics EM (induction, flow meters and current limits, with a synthetic limit that is explicitly not safety guidance), physics mechanics (centrifuge rotation) and statics (forearm equilibrium). The twelve packages move to 0.3.0 and stay `partial`. 72 keys were graded to full credit. Pre-commit checks caught three short feedback strings, three readings under 800 words, a source id not used by the package and a muscle-stress example whose synthetic area gave an implausible stress; all were fixed.

The [gap report](COURSE_GAP_REPORT.md) now shows 0 of 101 course outcomes without a linking lesson objective. The validator's `objective-coverage` warning still appears for all 25 packages: it counts a course outcome as covered only when an assessment lists the outcome id directly, which no package (including cell biology) does. Listing outcome ids on assessments is an authoring-policy decision for a reviewer, so the warning was left in place rather than silenced.

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 191 lessons, 648 questions, 504 cards, 25 cases; 0 errors; 123 disclosed warnings |
| `verify.sh` | all steps PASS: root 190 passed; backend 1545 passed, 2 skipped; security 505 files, 0 findings; ruff clean; legacy 7/7 |

Not run: frontend checks, Docker Compose, Playwright. Not reviewed by a subject-matter expert.

## Previous increment: calculus 3 and robotics lessons (2026-10-08, seventh pass)

Written by an AI coding assistant. Calculus 3 (gradients in a synthetic concentration field: partial and directional derivatives, steepest ascent, Fick's law and what fraction of the concentration differs across a cell) and robotics (planar two-link arm: forward and inverse kinematics, reachability, singularity, joint-error propagation for lab positioning), each 0.2.0 and still `partial`, with six items whose keys were graded to full credit and four cards. Every package now has at least one lesson-length original reading. Unlinked course outcomes: 19 of 101.

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 179 lessons, 576 questions, 456 cards, 25 cases; 0 errors; 123 disclosed warnings |
| `verify.sh` | all steps PASS: root 166 passed; backend 1401 passed, 2 skipped; security 493 files, 0 findings; ruff clean; legacy 7/7 |

Not run: frontend checks, Docker Compose, Playwright. Not reviewed by a subject-matter expert.

## Previous increment: biomechanics, linear algebra, physics and engineering lessons (2026-10-08, sixth pass)

Written by an AI coding assistant. Nine original lessons of about 830 to 950 words, each with a common-mistakes section, a worked problem, six items and four cards, all with synthetic values: cellular biomechanics (Hertz indentation and viscoelastic relaxation; separating substrate stiffness from ligand density with a 2×2 factorial and traction forces), linear algebra (least-squares calibration with normal equations and residuals; Markov chains for cell-state transitions), statics and materials (bending of a long bone), physics mechanics (impact forces), physics EM (the membrane as a capacitor), circuits (sensor loading and ADC resolution) and signals and control (proportional control of an incubator). Seven packages move to 0.2.0 and stay `partial`. 54 keys were graded to full credit by the real grader. Two authoring defects were caught before commit: a hint below the schema's minimum length, and prompts whose very small SI answers invited a ×10ⁿ notation the grader does not parse; those answers now use scaled units (nN, pC, MV/m). Unlinked course outcomes: 25 of 101. Only calculus 3 and robotics remain at legacy depth.

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 177 lessons, 564 questions, 448 cards, 25 cases; 0 errors; 123 disclosed warnings |
| `verify.sh` | all steps PASS: root 162 passed; backend 1377 passed, 2 skipped; security 491 files, 0 findings; ruff clean; legacy 7/7 |

Not run: frontend checks (no frontend change), Docker Compose, Playwright. Not reviewed by a subject-matter expert.

## Previous increment: chemistry and mathematics lessons (2026-10-08, fifth pass)

Written by an AI coding assistant. Eight original lessons of about 830 to 900 words, each with a common-mistakes section, a worked problem, six or seven items and four cards, all with synthetic values: general chemistry 1 (solution preparation, dilution and propagated error), general chemistry 2 (buffer design, capacity and ionization; integrated rate laws and Arrhenius), organic chemistry (acyl reactivity, side-chain ionization, glycation and a modification-versus-turnover steady state that makes no claim about any person), calculus 1 (derivatives in exponential and logistic growth), calculus 2 (integrals as accumulation, trapezoid and Simpson with an error bound, improper integrals) and differential equations (a well-mixed perfused chamber with Euler stability; equilibria, harvesting and a two-compartment eigenvalue analysis). The six packages move to 0.2.0 and stay `partial`. 49 keys were graded to full credit by the real grader. The lesson tests found two gaps before commit (a missing synthetic label and an objective with no item); both were fixed. Unlinked course outcomes: 48 of 101.

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 168 lessons, 510 questions, 412 cards, 25 cases; 0 errors; 123 disclosed warnings |
| `verify.sh` | all steps PASS: root 144 passed; backend 1269 passed, 2 skipped; security 482 files, 0 findings; ruff clean; legacy 7/7 |

Not run: frontend checks (no frontend change), Docker Compose, Playwright. Not reviewed by a subject-matter expert.

## Previous increment: genetics lessons 7 and 8 (2026-10-08, fourth pass)

Written by an AI coding assistant. Genetics moves to 0.3.0 (still `partial`) with two more original lessons: three-point mapping (gene order from double-crossover classes, interval distances, coefficient of coincidence and interference, Haldane's map function) and designing a controlled gene-perturbation experiment (tool choice, specificity controls including rescue, ΔΔCt quantification and its assumptions, biological versus technical replication, a normal-approximation sample size). Synthetic counts and Ct values; 12 items whose keys were graded to full credit by the real grader; 8 cards. Every genetics course outcome is now linked from a lesson objective; package-wide, 63 of 101 outcomes remain unlinked.

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 160 lessons, 461 questions, 380 cards, 25 cases; 0 errors; 123 disclosed warnings |
| `verify.sh` (root and backend pytest, security, ruff, legacy) | all steps PASS: root 128 passed; backend 1171 passed, 2 skipped; security 474 files, 0 findings; ruff clean; legacy 7/7 |

Docker Compose, Playwright and the frontend checks were not run (no frontend change). Not reviewed by a subject-matter expert.

## Previous increment: two lessons each in genetics, biochemistry, physiology and biomaterials (2026-10-08, third pass)

Written by an AI coding assistant.

- **Genetics, biochemistry, physiology and biomaterials 0.2.0** (all still `partial`). Each package gains two original lessons of about 810 to 990 words, each with a worked problem that is not a repeat of the body text, six or seven formative items and four cards: Hardy–Weinberg departures and carrier frequency; heritability and polygenic scores; enzyme kinetics and inhibition fingerprints; actual versus standard free energy, coupling and redox; oxygen delivery and the Fick principle; renal clearance; hydrogel degradation and release; scaffold porosity, stiffness and permeability. All parameters are synthetic. Numeric keys are computed in the authoring script from the prompt values, and all 49 keys were graded to full credit by the real grader before commit. No third-party source was added.
- The [gap report](COURSE_GAP_REPORT.md) was regenerated: course outcomes with no linking lesson objective fell from 79 to 65 of 101.
- Tests: the 2026-10-08 lesson checks now cover these eight lessons; inventory pins were updated to the new counts.

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 158 lessons, 449 questions, 372 cards, 25 cases; 0 errors; 123 disclosed warnings (98 legacy-depth, 25 objective-coverage) |
| `python -m pytest tests -q` | 124 passed (after the pin fix) |
| `cd backend; python -m pytest -q` | 1147 passed, 2 skipped |
| `python tools/check_security.py` | 472 source files, 0 findings |
| `ruff`, `node --test` legacy | PASS |

The first full run of `verify.sh` failed one root test because an inventory pin (401 → 450 with the private fixture) had not been updated; it was fixed and the root suite rerun. The frontend was not changed, so `--frontend` was not run. Docker Compose and Playwright were not run. No lesson was reviewed by a subject-matter expert.

## Previous increment: assessment-protection toggle, six geroscience lessons, a time-to-event lesson (2026-10-08, second pass)

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

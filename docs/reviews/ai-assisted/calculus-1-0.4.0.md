# Calculus I 0.4.0 — AI-assisted mathematical and authoring checks

Date: 2026-10-09. Codex authored the new content and the separate check implementation. The checks use numerical methods independent of the answer-generating formulas, but the same AI assistant produced both. This is not independent scientific review or human review. The package stays **partial, unreviewed and formative-only**.

## Scope

Seven new readings (lessons 7–13, approximately 940–1,040 words each), one approximately 930-word synthetic washout lab, 71 new public items, 32 cards and a proposed 14-week sequence. The package now contains 14 readings, 92 items and 48 cards. Four compact prototype readings, all 21 preexisting items and the original washout self-assessment checklist are preserved. No new source identifier, third-party text or dataset was introduced.

New topics are limits and derivative definitions; composite/implicit functions and related rates; curve shape and constrained optimization; accumulation, moving bounds and substitution; finite differences and quadrature with error budgets; linearization, Newton iteration and elasticity; and semilog washout interpretation. The lab has 21 constructed observations at seven times, with a known additive background and balanced offsets. A zero-background endpoint model underpredicts a reserved late observation. These data establish no real sensor error distribution, clearance parameter or biological mechanism.

## Separate calculations

`tests/content/test_calculus_one_recalculations.py` checks all 64 numeric item keys, including the 18 preexisting ones, plus 14 CSV summary cells. It imports no scratchpad authoring code. It uses central numerical differentiation for product, chain, implicit and related-rate formulas; numerical integration for accumulation, substitution and moving bounds; root finding for decay rates, half-lives, growth timing and stationary geometry; integration of piecewise linear and quadratic interpolants for trapezoid/Simpson keys; direct numerical remainder checks; and calculations from the committed CSV. Central-difference keys are also checked as interval averages of the analytic rate, rather than repeated endpoint subtractions.

Additional checks cover strict epsilon–delta neighborhoods, continuity versus differentiability, null derivative denominators, vertical tangents, tied boundary minima, curvature sign changes, feasible height constraints, quadrature error bounds, worst-case noise amplification, local approximation domains, Newton improvement in the stated example, finite versus infinitesimal relative response, positive corrected log ratios, background curvature and alternative explanations. The preserved symbolic derivative is independently checked by numerical values away from its excluded denominator point. The whole-package grader check includes that symbolic item rather than skipping it.

The schedule check ensures each reading appears once, references resolve, the lab precedes the case in weeks 13 and 14, the syllabus matches the authored outcomes and version, and review/grading labels remain conservative. These checks do not establish workload, learner effectiveness, assistive-technology accessibility or full-course mastery.

## Authoring corrections and failed commands

- An accidental invisible character in the new semilog filename was removed before integration; its final path is ASCII and stable.
- The lab initially named background interpretation in the later capstone as a prerequisite. Its instructions now require the preceding growth and numerical-calculus lessons and introduce the background model within the lab itself; the capstone follows in week 14.
- `python -B -m pytest tests/content/test_calculus_one_recalculations.py tests/content/test_learner_visible_number_formatting.py -q -p no:cacheprovider` initially had 77 passes and one failed test assertion. It compared a phrase to an entire option string with list membership instead of checking the phrase within the option; repaired. No numeric key failed.
- `ruff check backend tools tests` initially failed on 21 E731 assigned-lambda style violations in the new test file. `ruff check --select E731 --fix --unsafe-fixes tests/content/test_calculus_one_recalculations.py` converted them to named functions, followed by formatting and the full lint check. No numerical method changed.
- The inventory pins include both the public total of 1,532 questions and the synthetic private-fixture total of 1,533. The 98 disclosed legacy-depth warnings remain; no new warning was hidden.

## Verification commands and limits

Commands run as `vscode` in the existing Linux development container, using `/home/vscode/.cache/venvs/courselab` and repository working directory `/workspace/uniStemCourseSimulators`.

- `python -B tools/validate_content.py`: PASS, 25 packages / 305 lessons / 1532 questions / 960 cards / 25 cases, zero errors and 98 legacy-depth warnings.
- `python -B /workspace/courselab-session-artifacts/codex-calculus-1-2026-10-09/check_grader.py`: PASS, all 92 items earn full credit, including the preserved symbolic item.
- `python -B -m pytest tests/content/test_calculus_one_recalculations.py tests/content/test_new_geroscience_and_statistics_lessons.py tests/content/test_learner_visible_number_formatting.py -q -p no:cacheprovider`: 421 passed after the assertion repair; the final full run includes the subsequent style conversion.
- `bash /workspace/.claude/skills/courselab-dev/scripts/verify.sh --log-dir /workspace/courselab-session-artifacts/codex-calculus-1-2026-10-09/verification`: full results are recorded in [the validation report](../../VALIDATION_REPORT.md).

The full run passed all six requested steps: content (zero errors, 98 warnings), seven legacy tests, security (660 files, zero findings), ruff, 1,321 root tests and 3,315 backend tests with two existing symbolic-builder skips. The post-style-conversion focused run also passed all 78 checks.

Authoring artifacts and logs are retained outside git in `courselab-session-artifacts/codex-calculus-1-2026-10-09`. `apply.py` checks the original version before mutation and is a one-time integration artifact, not a general update or production migration.

Frontend checks, the Docker Compose application stack and Playwright are not run locally for this content increment; publication CI runs them. No person reviewed the content or measured workload, and no exam, institutional grade or real experiment is provided.

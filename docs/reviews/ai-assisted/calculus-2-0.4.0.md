# Calculus II 0.4.0 — AI-assisted mathematical and authoring checks

Date: 2026-10-09. Codex authored the content and the separate check implementation. The checks use alternative numerical and finite-sum calculations where practical, but the same AI assistant produced both. This is not independent mathematical review or human review. The package remains **partial, unreviewed and formative-only**.

## Scope

Seven new original readings (lessons 7–13, approximately 825–915 words each), one approximately 940-word synthetic force-work lab, 71 new public formative items, 32 cards and a proposed 14-week schedule. The package contains 14 readings, 91 items and 48 cards. Four compact prototype readings, all 20 preexisting item objects, all 16 preexisting cards and the radial-concentration self-assessment checklist are preserved. No new source identifier, third-party text, figure or dataset was added.

Topics cover integration methods and domain checks; improper limits, comparisons and principal values; positive-series tests and tails; alternating convergence and signed remainder certificates; power-series radii and endpoints; Taylor polynomials and accumulated error; and geometric, parametric and annular integrals. The radial lesson clarifies concentration units and distinguishes a cross-sectional amount from an amount per cylinder length.

The lab constructs 15 readings at five positions from F(x)=10x/(1−0.2x) N over 0≤x≤2 m, with dimensionally stated coefficients, a known 1 N sensor offset and balanced ±0.05 N repeat offsets. CSV means are rounded to four decimals. Corrected sampled-rule answers use these committed values; the separate series calculation uses the exact generating function. The four-term geometric work approximation is about 27.4453 J, its exact positive error about 0.2611 J, and its integrated tail bound about 0.2844 J. These data establish no real actuator behavior, noise distribution or experimental result.

## Separate calculations

`tests/content/test_calculus_two_recalculations.py` recalculates all 62 numeric item keys, including 16 preserved keys, and all ten CSV summary checks. It imports no authoring artifacts. Numerical quadrature checks definite integrals directly. Variable transformations remove improper endpoints: u=1/x for reciprocal tails, x=u² for the square-root singularity, and u=1/(1+t) for shifted inverse-square rates. Finite sums check geometric, telescoping and power-series values. Search over successive indices checks that selected sufficient orders are the first under the stated bound.

Trapezoid and Simpson answers are checked by numerically integrating piecewise linear and quadratic interpolants, rather than repeating the author's rule weights. Taylor and geometric accumulated-error keys are checked by quadrature of pointwise bounds. Radial totals are checked both by annular integration and by the substitution s=r²/R². CSV checks recompute counts and means directly from committed observations and verify their embedded source-value lists.

Additional checks cover antiderivative differentiation, divergent internal singularities, harmonic dyadic blocks, the inconclusive ratio limit of one, alternating remainder signs and actual errors, expansion domains and endpoint distinctions, integrated Taylor remainders, repeated curve traversal, the radial half factor, constant offset contribution, positive force-tail error and the scope of a truncation guarantee. A separate real-grader run confirms all 91 package items earn full credit for their authored correct responses. Grader acceptance alone does not establish that a mathematical key is correct.

The schedule check verifies fourteen sequential weeks, complete lesson coverage, the final lab and preserved case references, current counts, and conservative maturity/review/grading labels. Standard authoring checks verify that each new reading has three assessed objectives linked to outcomes and four cards. These checks establish neither measured workload, accessibility nor learner effectiveness.

## Authoring repairs and failed checks

- `python -B -m pytest tests/content/test_calculus_two_recalculations.py tests/content/test_learner_visible_number_formatting.py -q -p no:cacheprovider` initially returned **83 passed, 2 failed**. Both failures were display-format checks: long decimals in the logarithm certificate and small Taylor errors. Learner-facing strings now use Unicode scientific notation; exact numeric specifications are preserved. No mathematical key failed.
- `ruff check tests/content/test_calculus_two_recalculations.py --fix --unsafe-fixes` corrected one E731 assigned-lambda style issue and exited successfully. Formatting followed; the final lint check passed. The numerical method did not change.
- The first focused three-file run passed 428 checks. Inspection showed the intended extension of the common lesson list had not matched its multiline source. The seven new lessons were then explicitly added, and the rerun passed **442** checks, including their fourteen structural/objective checks.
- The public inventory is 313 lessons, 1,603 questions and 992 cards. The synthetic private-fixture inventory adds one question and expects 1,604. The 98 disclosed legacy-depth warnings remain unchanged.

## Verification commands and limits

Commands run as `vscode` in the existing Linux development container, using `/home/vscode/.cache/venvs/courselab` from repository directory `/workspace/uniStemCourseSimulators`.

- `python -B tools/validate_content.py`: PASS, 25 packages / 313 lessons / 1603 questions / 992 cards / 25 cases, zero errors and 98 legacy-depth warnings.
- `python -B /workspace/courselab-session-artifacts/codex-calculus-2-2026-10-09/check_grader.py`: PASS, all 91 items earn full credit.
- `python -B -m pytest tests/content/test_calculus_two_recalculations.py tests/content/test_new_geroscience_and_statistics_lessons.py tests/content/test_learner_visible_number_formatting.py -q -p no:cacheprovider`: PASS, 442 focused checks.
- `ruff check tests/content/test_calculus_two_recalculations.py`: PASS after style conversion and formatting.
- `bash /workspace/.claude/skills/courselab-dev/scripts/verify.sh --log-dir /workspace/courselab-session-artifacts/codex-calculus-2-2026-10-09/verification`: results are recorded in [the validation report](../../VALIDATION_REPORT.md).

The full local run passed all six steps: content (zero errors, 98 disclosed warnings), seven legacy tests, security (670 source files, zero findings), ruff, 1,417 root tests and 3,457 backend tests with two existing symbolic-builder skips.

Authoring artifacts and logs are retained outside git in `courselab-session-artifacts/codex-calculus-2-2026-10-09`. The one-time integration script checks the original version and module count before mutation; do not rerun it against the expanded package or treat it as a general migration. Committed content is the final source of truth.

Frontend checks, the Docker Compose application stack and Playwright are not run locally for this content increment; publication CI runs them. No person reviewed the mathematics or measured workload. The package supplies no exam, institutional grade, real experiment or complete laboratory sequence.

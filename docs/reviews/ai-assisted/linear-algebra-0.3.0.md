# Linear algebra 0.3.0 — AI-assisted arithmetic and authoring checks

Date: 2026-10-09. Claude authored four recovered drafts; Codex corrected them, wrote three additional lessons and a synthetic lab, and performed these checks. The arithmetic checks use separate matrix operations from the authoring scripts, but the same AI assistant wrote the final content and tests. This is not independent scientific review or human review. The package stays **partial, unreviewed and formative-only**.

## Scope

Seven new readings (lessons 7–13, about 890–1,130 words each), one 939-word synthetic lab with ten signal pairs, 71 new public items and 32 cards, and a proposed 14-week schedule. The package now has 14 readings, 91 items and 48 cards. Four short prototype readings remain. The original case checklist is preserved and paired with the new displacement analysis in week 14. No source identifier or third-party material was added.

The lab deliberately pairs opposite signal errors, which target the weak singular direction. Its separate independent-noise uncertainty question names a different noise model. Mean error cancels by construction while parameter RMSE is 2 for poor geometry and 0.025 for improved geometry. These are synthetic demonstrations, not measurements or a real sensor specification.

## Recalculation method

`tests/content/test_linear_algebra_recalculations.py` covers every one of the 69 numeric item keys, including the 14 that predate this increment, plus the four CSV summary cells. It imports no scratchpad authoring code. Methods include rational elimination for rank; partial-pivot Gauss–Jordan solves; a constrained KKT solve for minimum norm; centered regression for QR fit coefficients; power iteration and determinant identities for positive symmetric spectra, rather than the author's quadratic-root formula; entrywise SVD reconstruction; direct ridge normal-equation solving instead of spectral shrinkage; centered covariance and projected reconstruction; inverse-matrix covariance propagation; and row-by-row solves of the committed lab CSV.

Further checks cover quoted worked-example numbers, orthogonal residuals, null-space solution families and inconsistency, the 90° dominant-axis case, repeated eigenvalues, rectangular SVD zero modes, the small-matrix storage boundary, calibration bias, weak-direction validation separation, scaling and held-out preprocessing. Schedule checks ensure every lesson appears once, references resolve, the lab and case occur in weeks 13 and 14, and maturity/review/grading labels stay unchanged. These checks do not establish accessibility, workload, learner effectiveness or comprehensive mastery.

## Corrections before publication

- Replaced the tangent-only dominant-eigenvector rule with half of `atan2`, explained sign/axis ambiguity, the quadrant issue and repeated eigenvalues; updated the item and card.
- Specified rectangular Σ, possible reflections, shared nonzero spectra and different zero multiplicities of AᵀA and AAᵀ. Updated the general SVD statement and card accordingly.
- Replaced the garbled small-example storage count with six numbers, and required `k(m + n + 1) < mn` as well as acceptable approximation error. Removed unsupported claims that discarded components are necessarily noise.
- Distinguished the Gram matrix's squared condition number from the measurement problem's physical sensitivity; QR avoids added numerical sensitivity but does not add information.
- Replaced a rank-item feedback claim that more equations make solvability "less likely" with the actual column-space consistency criterion.
- Made the QR intercept item self-contained by supplying R and Qᵀb; removed unnecessary cross-item references elsewhere in the QR set.
- Expanded one feedback string that violated the schema's ten-character minimum and four worked-example summaries below the 35-word minimum. Corrected a final decimal in ridge feedback; the numeric key already matched the independent solve.

No preexisting answer key, tolerance, points, option or objective mapping was altered. The 71 new items all earned full credit under the real grader; backend authored-item tests also exercise wrong responses.

## Commands and results

Commands run in the existing Linux development container as `vscode`, using `/home/vscode/.cache/venvs/courselab` and repository working directory `/workspace/uniStemCourseSimulators`. Full-run results are recorded in [the validation report](../../VALIDATION_REPORT.md).

- `python -B tools/validate_content.py`: after repairs, PASS, 25 packages / 297 lessons / 1,461 questions / 928 cards / 25 cases, zero errors and 98 disclosed legacy-depth warnings. The first draft run failed on the short feedback and summaries; one invalid bank produced cascading reference errors. All were resolved.
- `python -B /workspace/courselab-session-artifacts/claude-resume-2026-10-08/selfcheck.py linear-algebra linear-algebra-`: PASS, all 91 items earn full credit.
- `python -B -m pytest tests/content/test_linear_algebra_recalculations.py tests/content/test_new_geroscience_and_statistics_lessons.py -k linear_algebra -q -p no:cacheprovider`: the initial targeted run had 77 passes and one test failure from expecting a literal phrase absent from the reading. A first assertion repair still expected a phrase used only in the item prompt, so the subsequent unfiltered run had 406 passes and one failure. The assertion now checks the reading's actual phrase, "batch and treatment are confounded". The full run includes all newly parameterized lesson checks, which the initial name filter does not select.
- `ruff check tests/content/test_linear_algebra_recalculations.py`: initially failed on three ambiguous `l` variables; renamed and formatted before the full run.
- An initial validator invocation omitted the container working directory and could not find `tools/validate_content.py`; rerun with the correct directory.

The first full `verify.sh` run passed content, legacy, security, ruff and backend checks, but root pytest reported 1,229 passes and three failures: a missed inventory pin for the one-item private test fixture (1,391 became 1,462), a nine-place decimal rejected by the learner-number formatting policy (rendered instead as 1.12847 × 10⁻⁴), and the already-corrected PCA literal assertion loaded when that run began. None was an incorrect numeric key. All three were repaired before a fresh full run in the `verification-final` log directory.

The final full run passed all six requested steps: content validation (0 errors, 98 warnings), seven legacy tests, security (649 files, 0 findings), ruff, 1,232 root tests and 3,173 backend tests with two existing symbolic-builder skips. The 407-check unfiltered content run and the 82-check regression run also passed.

Logs and authoring scripts are retained outside the repository under `courselab-session-artifacts/codex-linear-algebra-2026-10-09`. The integration script is a one-time authoring artifact, not an idempotent migration; do not rerun it against the expanded package. Preserved original drafts remain in the separate Claude recovery directory.

Frontend, Docker Compose application and Playwright checks were not run locally for this content increment; publication CI runs those suites. No named instructor, subject-matter, accessibility or workload review occurred.

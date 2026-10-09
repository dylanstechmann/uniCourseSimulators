# Calculus III 0.4.0 — AI-assisted mathematical and authoring checks

Date: 2026-10-09. Codex authored the instruction and separate numerical checks. Alternative calculations are used where practical, but the same AI assistant produced both. This is not independent mathematical review or human review. The package remains **partial, unreviewed and formative-only**.

## Scope

Seven new readings (lessons 7–13, approximately 845–920 words each), one approximately 1,015-word synthetic boundary-flux lab, 71 public formative items, 32 cards and a proposed 14-week schedule. The package contains 14 readings, 91 items and 48 cards. Four compact prototype readings, all 20 preexisting question objects, all 16 preexisting cards and the oxygen-flux self-assessment checklist are preserved. No new source identifier, third-party text, figure or dataset was added.

Topics develop vectors, planes and spatial curves; partial derivatives, differentiability and total change; Hessians, regular constraints and feasible boundaries; multiple integrals and Jacobian measures; line integrals, potentials and Green; oriented surface flux and divergence; and Stokes with source/sink/storage signs. Theorems are qualified by their geometry, orientation, smoothness and domain assumptions, with punctured-field counterexamples.

The lab constructs 18 outward-normal density readings on six faces of a box, using J=(−2x,−3y,−4z), a known common offset and balanced repeat offsets. Corrected face transfer is −18, matching divergence −9 times volume 2. Interpreting the inward supply as a uniform sink of 9 additionally requires steady storage and no source. Neither the construction nor the theorem identifies a real tissue parameter or experimental noise law.

## Separate calculations

`tests/content/test_calculus_three_recalculations.py` checks all 62 numeric keys, including 16 preserved keys, and all 12 CSV summary cells, without importing authoring artifacts. It uses finite differences for partials, path rates, tangents and Hessians; numerical Newton steps for stationary quadratic points; root finding for edge optima and a preserved vessel optimum; quadrature for curve lengths and geometric totals; numerical integration of line segments and circles for work/circulation; parameterized spherical surface integration; and explicit six-face box integration for transfer.

The ball volume is checked by Cartesian disk slices, and its radial-density total by cylindrical cross-sectional integration, providing a different route from the spherical authoring formula. Ellipse area uses a boundary-area integral. Green and Stokes values are checked by direct oriented line integrals. Surface graph area and flux use a cross product; box divergence values are also compared with signed face integrals. CSV cells recompute committed counts/means and verify their embedded source-value lists. Mathematical answer acceptance is separately checked under the real grader for all 91 package items.

Additional checks cover normalization and cross-product reversal, reparameterization, partial-derivative counterexamples, degenerate Hessians, all rectangle edge candidates, both-sign constrained maximizers, region order reversal and density averages, path reversal and domain holes, graph normal reversal, variable diffusivity, tilted Stokes area, an excluded singular shell with inner-boundary cancellation, and source/storage assumptions. Schedule and authoring checks cover every reading, fourteen weeks, three assessed objectives per new lesson, cards, syllabus counts and conservative labels.

These checks are calculations and selected counterexamples, not proof of every stated theorem. They establish neither measured workload, assistive-technology accessibility nor learner effectiveness. Old numeric keys retain their existing tolerances and unit conventions.

## Repairs and failed commands

- The first `python -B /workspace/courselab-session-artifacts/codex-calculus-3-2026-10-09/apply.py` failed with a quoted-apostrophe syntax error before any mutation. The string was repaired; the guarded rerun succeeded.
- A provisional surface lesson draft's box transfer was corrected to 8 before integration, using both face contributions 4+2+2 and the volume integral of 2x+2. The committed lesson teaches the consistent result.
- `ruff check tests/content/test_calculus_three_recalculations.py --fix --unsafe-fixes` initially found 14 issues, fixed 13 assigned lambdas and exited nonzero for one ambiguous variable name. That name was changed and the final lint check passed.
- `python -B -m pytest tests/content/test_calculus_three_recalculations.py tests/content/test_learner_visible_number_formatting.py -q -p no:cacheprovider` first passed all 88 checks. The numerical methods were then strengthened for stationary points, edge selection and helix length before the full run.
- The first expanded three-file focused run had **458 passed, 1 failed**. A parameter-invariance assertion used exact equality against a finite-difference length of 9.99999999996332. It now uses a tight numerical tolerance. No authored key failed.
- Inventory pins now expect 321 lessons, 1,674 public items and 1,024 cards, with 1,675 items in the synthetic private-fixture case. The 98 disclosed legacy-depth warnings are unchanged.

## Verification commands and limits

Commands use the existing Linux development container as `vscode`, with `/home/vscode/.cache/venvs/courselab`, from `/workspace/uniStemCourseSimulators`.

- `python -B /workspace/courselab-session-artifacts/codex-calculus-3-2026-10-09/check_grader.py`: PASS, all 91 package items earn full credit.
- `python -B -m pytest tests/content/test_calculus_three_recalculations.py tests/content/test_new_geroscience_and_statistics_lessons.py tests/content/test_learner_visible_number_formatting.py -q -p no:cacheprovider`: final results are recorded in [the validation report](../../VALIDATION_REPORT.md).
- `ruff check tests/content/test_calculus_three_recalculations.py`: PASS after repairs and formatting.
- `bash /workspace/.claude/skills/courselab-dev/scripts/verify.sh --log-dir /workspace/courselab-session-artifacts/codex-calculus-3-2026-10-09/verification`: full results are recorded in the validation report.

The final focused suite passed 459 checks. The full local run passed content (zero errors, 98 disclosed warnings), seven legacy tests, security (682 source files, zero findings), ruff, 1,516 root tests and 3,599 backend tests with two existing symbolic-builder skips.

Authoring artifacts and logs remain outside git in `courselab-session-artifacts/codex-calculus-3-2026-10-09`. The integration script checks the original version/module count and all reading lengths before mutation. It is a one-time artifact, not a general update migration. Committed content is authoritative.

Frontend checks, the Docker Compose application stack and Playwright are not run locally for this content increment; publication CI runs them. No person reviewed the mathematics or measured workload. No exam, university credit, real experiment or complete laboratory sequence is supplied.

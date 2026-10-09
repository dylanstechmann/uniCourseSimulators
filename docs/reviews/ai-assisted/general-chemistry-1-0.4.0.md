# General Chemistry I 0.4.0 — AI-assisted chemical and authoring checks

Date: 2026-10-09. Codex authored the instruction and separate numerical checks. Alternative calculations are used where practical, but the same AI assistant produced both. This is not independent chemical review or human review. The package remains **partial, unreviewed and formative-only**.

## Scope and sources

Seven new readings (lessons 7–13, approximately 875–945 words each), one approximately 1,000-word synthetic buffer lab, 71 public formative items, 32 cards and a proposed 14-week sequence. Package totals are 14 readings, 91 items and 48 cards. Four compact prototype readings, all 20 prior question objects, all 16 prior cards and the original buffer self-assessment checklist are preserved.

Topics are atomic/amount/photon accounting, Lewis and geometry models, reaction extent, ideal gases and model deviations, energy/calorimeter accounting, equilibrium extents and activities, and buffer discrepancy checks. Examples stipulate synthetic amounts and parameters and provide no chemical handling procedure or biological recommendation. Selected real molecular examples illustrate introductory models rather than new measured material properties.

Two factual references were added as **link-only** entries, with quotation/adaptation/redistribution permissions false and no imported assets. [NIST SP 330 Section 2](https://www.nist.gov/pml/special-publication-330/sp-330-section-2) was retrieved and supports the defining SI constants. The [IUPAC pH entry](https://goldbook.iupac.org/terms/view/P04524) was verified from its official indexed definition; direct page, plain-text and PDF retrieval returned HTTP 403. The source record and course limitations disclose that restriction. No full-page IUPAC access is claimed. No new PMID, DOI, NCT or paper link was introduced, and no third-party teaching prose, figure or dataset was copied. The existing MIT chemistry source remains a scope comparator.

## Synthetic buffer construction

The nominal case has HA=0.050 mol and A⁻=0.030 mol. Independent synthetic composition instead supplies HA=0.056 and A⁻=0.024 mol, preserving total 0.080 mol in fixed 0.50 L. Six acid-equivalent conditions and a separate reference produce 21 deliberately balanced reports. The ideal model retains acid mass balance, water and electroneutrality and uses a stipulated pK_a of 4.8.

The reference identifies a common +0.08 reporting offset. Corrected q10 pH is 4.1280, versus nominal inventory-ratio prediction 4.322879. Calibration correction does not remove the independently supplied composition mismatch. At q30 the actual base is exhausted, and full balance gives pH approximately 1.913375 rather than a logarithm of a negative formal inventory. These values establish no real acid parameter, activity coefficient, instrument noise distribution or unique cause from pH alone.

## Separate calculations and grader boundaries

`tests/content/test_general_chemistry_one_recalculations.py` recalculates all 59 numeric keys, including 13 preserved keys, and all 14 CSV summary cells. It imports no authoring artifacts. Decimal arithmetic checks photon and amount scales; conservation and root finding check dilution, partitioning and extents; component vectors check dipole magnitude; kinetic energy is inverted for RMS speed; reaction/solution energy balances check calorimetry; and direct-concentration cubic roots check the buffer construction independently of the author's logarithmic charge-balance search.

Additional checks cover atomic identity and input precision, Lewis/dipole limits, mass and charge conservation, excess-ion accounting, gas partial-pressure sums, state constraints, calorimeter signs, Hess scaling, reaction-constant conventions, activity quotients, positive buffer species and charge balance, independent composition, log-scale averaging, source rights/access disclosures and the proposed schedule. The checks are selected calculations and counterexamples, not proofs of every chemical claim or evidence of learner effectiveness.

Six new items enforce specified significant figures, three of them also requiring units. `backend/tests/test_general_chemistry_precision.py` checks scientific-notation alternatives, supported equivalent unit scales, wrong precision, missing/wrong units, malformed responses and numerical near misses. It uses explicit responses rather than constructing them from the key. The complete real-grader check confirms all 91 items earn full credit for their authored correct responses, including required precision formatting. No grading implementation was changed.

## Failed checks and repairs

- `python -B -m pytest tests/content/test_general_chemistry_one_recalculations.py tests/content/test_learner_visible_number_formatting.py -q -p no:cacheprovider` initially had **87 passed, 1 failed**: an overly long decimal in photon feedback. The displayed value was shortened; the rounded numeric key did not change.
- `python -B -m pytest tests/test_general_chemistry_precision.py -q -p no:cacheprovider` from `backend/` initially had **5 passed, 1 failed** because the authored unit `kPa` is outside the current explicit unit grammar. The pressure item now asks for SI pascals, with the same physical result, correctly rounded key and matching absolute tolerance. Tests cover Pa/MPa conversion without broadening the grader.
- The first complete `check_grader.py` failed on the CSV specification's uppercase `mean_pH` output column. The upload grammar requires lowercase names, so instructions/specifications now use `mean_ph`. The raw supplied data column `reported_pH` remains unchanged. The complete grader rerun passed all 91 items.
- The final expanded root focused suite passed **473** checks, and the precision suite passed all **6** checks. Initial lint passed; formatting was applied. No chemical calculation key failed; pressure reporting units/rounding were revised for supported grading.
- Inventory pins expect 329 readings, 1,745 public items and 1,056 cards, with 1,746 items in the synthetic private-fixture case. The 98 disclosed legacy-depth warnings remain unchanged.

## Verification commands and limits

Commands run as `vscode` in the existing Linux development container using `/home/vscode/.cache/venvs/courselab`, from `/workspace/uniStemCourseSimulators` unless the backend working directory is stated.

- `python -B tools/validate_content.py`: PASS, 25 packages / 329 lessons / 1745 questions / 1056 cards / 25 cases, zero errors and 98 legacy-depth warnings.
- `python -B /workspace/courselab-session-artifacts/codex-general-chemistry-1-2026-10-09/check_grader.py`: PASS, all 91 items, including precision formatting and the corrected CSV column.
- `python -B -m pytest tests/content/test_general_chemistry_one_recalculations.py tests/content/test_new_geroscience_and_statistics_lessons.py tests/content/test_learner_visible_number_formatting.py -q -p no:cacheprovider`: PASS, 473 focused checks before the CSV output-column repair; the full run covers the repaired specification.
- `python -B -m pytest tests/test_general_chemistry_precision.py -q -p no:cacheprovider` from `backend/`: PASS, six precision/unit checks.
- `bash /workspace/.claude/skills/courselab-dev/scripts/verify.sh --log-dir /workspace/courselab-session-artifacts/codex-general-chemistry-1-2026-10-09/verification`: full results are recorded in [the validation report](../../VALIDATION_REPORT.md).

The complete local run passed content (zero errors, 98 disclosed legacy-depth warnings), seven legacy checks, security (694 source files, zero findings), ruff, 1,615 root tests and 3,747 backend tests with two existing symbolic-builder skips. The generated objective report matched, and the claims scan had zero findings. A preliminary report-check invocation used unavailable bare `python`; the configured venv interpreter passed.

Artifacts and logs remain outside git in `courselab-session-artifacts/codex-general-chemistry-1-2026-10-09`. Integration is a guarded one-time artifact, not an update migration. Committed content is authoritative.

Frontend checks, the Docker Compose application stack and Playwright are not run locally for this content increment; publication CI runs them. No person reviewed the chemistry or measured workload. The package supplies no exam, institutional credit, real experiment or complete laboratory sequence.

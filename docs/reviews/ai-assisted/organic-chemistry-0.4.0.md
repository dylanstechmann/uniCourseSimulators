# Organic Chemistry 0.4.0 — AI-assisted chemical and authoring checks

Date: 2026-10-09. Codex authored the instruction and separate checks. Alternative calculations are used where practical, but the same AI assistant produced both. This is not independent chemical or human review. The package remains **partial, unreviewed and formative-only**.

## Scope and sources

Seven original readings (lessons 7–13, approximately 900–1,025 words each), one approximately 960-word synthetic peak-calibration lab, 71 public formative items, 32 cards and a proposed 14-week sequence. Package totals are 14 readings, 91 items and 48 cards. All 20 prior questions, 16 prior cards, four compact prototypes and the original amide self-assessment checklist are preserved.

New lessons cover formula/electron flow, conformation and Fischer mapping, substitution/elimination competition, carbonyl/acyl/proton bookkeeping, enolate/aldol atom mapping, spectroscopic constraints and reaction-network evidence. Each has four numeric and five conceptual choices, reflecting the spatial, connectivity and mechanism questions that cannot be reduced to a numeric amount. The original text Fischer diagram includes a full verbal viewpoint description. No drawn mechanism or written proof is automatically graded.

Six primary OpenStax Organic Chemistry sections were retrieved on 2026-10-09 and registered as link-only factual references: [resonance rules](https://openstax.org/books/organic-chemistry/pages/2-5-rules-for-resonance-forms), [Fischer projections](https://openstax.org/books/organic-chemistry/pages/25-2-representing-carbohydrate-stereochemistry-fischer-projections), [SN2](https://openstax.org/books/organic-chemistry/pages/11-2-the-sn2-reaction), [aldol connectivity](https://openstax.org/books/organic-chemistry/pages/23-1-carbonyl-condensations-the-aldol-reaction), [NMR splitting](https://openstax.org/books/organic-chemistry/pages/13-6-spin-spin-splitting-in-1h-nmr-spectra) and [proton equivalence](https://openstax.org/books/organic-chemistry/pages/13-7-1h-nmr-spectroscopy-and-proton-equivalence). Quotation, adaptation and redistribution permissions are false; imported assets are empty. No source teaching prose, worked problem, drawing or dataset was copied. Existing MIT links remain scope comparators. No new PMID, DOI, NCT or paper link was introduced.

## Synthetic reporting construction

The lab supplies an independently identified enantiomeric pair A/B with positive/negative optical labels under matching conditions; no R/S descriptors are given. Reports are area_A=3+2n_A and area_B=3+n_B in arbitrary area units, with amount in micromoles. Unequal factors are assigned end-to-end reporting gains, not claimed intrinsic UV absorption differences between enantiomers in the same achiral environment. No actual detector or separation is validated.

A zero-amount blank and two independent 10 µmol pure standards identify offsets 3/3 and gains 2/1. Four constructed mixtures have amount ratios 9:1,7:3,5:5,2:8. Three simultaneous channel offsets −0.2, zero and +0.2 around each central report produce 21 rows. They deliberately covary, balance around the mean and establish no independent noise law.

Mix_2 calibrated amounts 7 and 3 µmol yield signed A excess 40%, whereas blank-corrected area ratio 14:3 yields about 64.7059%. Mix_3 calibrated amounts are equal despite unequal areas. Identity, linearity, no coelution and absence of other components are supplied assumptions; one blank and one amount standard per channel do not independently demonstrate linearity over a range. Optical sign and retention alone do not assign absolute configuration.

## Separate calculations and conceptual checks

`tests/content/test_organic_chemistry_recalculations.py` checks all 40 numeric keys (eight preserved) and all 21 CSV cells without authoring imports. Equilibrium/root calculations, normalized conformer weights, component RK4 integration of hydrolysis and parallel routes, and direct calibration reconstruction provide alternative calculations. The component ODE checks conserve amounts and distinguish finite conversion from branch fraction.

Additional checks use a three-dimensional determinant for the stated Fischer map, swaps and page rotations; bond-order/formal-charge ledgers for resonance and carbonyl addition; a heavy-atom/hydrogen ledger for donor/acceptor aldol connectivity and separate dehydration; enumeration of neighboring proton spin configurations for triplet/quartet line counts; and calibration reconstruction for every blank, standard and mixture. These are selected mathematical and chemical consistency checks rather than proofs of every teaching claim, actual mechanism or learner effectiveness.

New numeric items request bare numbers in stated scales. Four preserved items require units. No significant-figure or dimensional enforcement and no grading implementation change is claimed. The proposed schedule, source permissions and partial/formative labels are also checked.

## Authoring corrections and verification

The first `apply.py` invocation failed before any content mutation because an unescaped apostrophe in a retrieval-card string caused a syntax error. The string was repaired and integration rerun successfully. A preliminary skill-file read used the repository directory rather than the workspace location; the already established workspace authoring rules remain applicable.

The first `ruff check tests/content/test_organic_chemistry_recalculations.py` passed, and formatting was applied. The focused command `python -B -m pytest tests/content/test_organic_chemistry_recalculations.py tests/content/test_new_geroscience_and_statistics_lessons.py tests/content/test_learner_visible_number_formatting.py -q -p no:cacheprovider` passed all 504 checks on its first run. The actual-grader command `python -B /workspace/courselab-session-artifacts/codex-organic-chemistry-2026-10-09/check_grader.py` also passed all 91 items on its first run.

Separate `python -B tools/validate_content.py` initially failed with 193 reported errors. The underlying schema defect was the six-character feedback solution `C2–C3.`; bank rejection then caused cascading unknown-reference errors. A full verification attempt in `verification` had started before that result was inspected, failed its content step and was stopped. Expanding the explanation to state donor-alpha/acceptor-carbonyl connectivity repaired the schema without changing its key. Separate validation then passed. The lab text also now calls its publicly supplied construction amounts declared rather than hidden.

The fresh complete run in `verification-final` passed content (345 readings, 1887 questions, 1120 cards, zero errors and 98 disclosed warnings), seven legacy checks, security (716 source files, zero findings), ruff, 1,832 root tests and 4,031 backend tests with two existing symbolic-builder skips. This full run covers the explanation repair. The objective report matched, and the claims scan had zero findings. No numeric key failed or changed.

Exact verification commands, focused results and any subsequent failures/repairs are recorded in [the validation report](../../VALIDATION_REPORT.md). Artifacts and logs remain outside git in `courselab-session-artifacts/codex-organic-chemistry-2026-10-09`. Integration and documentation updates are guarded one-time authoring artifacts; committed content is authoritative.

Frontend checks, the Docker Compose application stack and Playwright are not run locally for this content increment; publication CI runs them. No person reviewed the chemistry or measured workload. One data lab, a text diagram and a proposed schedule do not establish a full laboratory sequence, accessibility review or semester equivalence. New examples supply no synthesis, handling or instrument-operation procedure.

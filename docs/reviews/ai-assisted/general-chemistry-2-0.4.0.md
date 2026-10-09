# General Chemistry II 0.4.0 — AI-assisted chemical and authoring checks

Date: 2026-10-09. Codex authored the instruction and separate numerical checks. Alternative calculations are used where practical, but the same AI assistant produced both. This is not independent chemical review or human review. The package remains **partial, unreviewed and formative-only**.

## Scope and sources

Seven new readings (lessons 8–14, approximately 840–915 words each), one approximately 940-word synthetic relaxation lab, 71 public formative items, 32 cards and a proposed 14-week sequence. Package totals are 15 readings, 97 items and 52 cards. Week 12 pairs a compact prototype with the new ligand-balance lesson. All 26 prior question objects, 20 prior cards and the original redox/metal self-assessment case remain unchanged.

Topics are standard/current free energy, coupled diprotic speciation, empirical rates and mechanism compatibility, reversible/sequential kinetics, electrochemical stoichiometry/work, ligand balance and limited octahedral models, and solubility/complexation. New examples stipulate synthetic parameters and provide no chemical handling procedure, device design or biological recommendation.

Three OpenStax Chemistry 2e primary pages were retrieved on 2026-10-09: [16.4 Free Energy](https://openstax.org/books/chemistry-2e/pages/16-4-free-energy), [12.6 Reaction Mechanisms](https://openstax.org/books/chemistry-2e/pages/12-6-reaction-mechanisms), and [19.3 Coordination properties](https://openstax.org/books/chemistry-2e/pages/19-3-spectroscopic-and-magnetic-properties-of-coordination-compounds). They are link-only factual references with quotation, adaptation and redistribution permissions false and no imported assets. Existing MIT chemistry and biochemistry references remain scope comparators. No teaching prose, worked problem, figure or dataset was copied, and no new PMID, DOI, NCT or paper link was introduced.

## Synthetic trajectory and separate evidence

The supplied closed A/B model has total 1.0 mM, equilibrium A=0.20 and B=0.80 mM, forward constant 0.048 min⁻¹ and reverse constant 0.012 min⁻¹. Initial A=1.0 mM relaxes as 0.20+0.80exp(−0.060t). Six time points and a separate zero-A blank produce 21 constructed reports. A common +0.0500 mM reporting background is added; central reports are rounded to four decimals, with deliberately balanced offsets of −0.0050, zero and +0.0050.

Blank correction does not remove the physical equilibrium plateau. Independent equilibrium composition supplies that plateau and the directional ratio, rather than estimating them from the same two fitted time points. The t00/t20 displacement fit gives λ approximately 0.059991 min⁻¹ and forward constant approximately 0.047993 min⁻¹. Reserved t60 prediction is about 0.221871 mM, agreeing with its corrected mean 0.2219 at the declared rounding scale. A blank-corrected zero-plateau endpoint fit instead gives about 0.032494 min⁻¹. This difference is explained by the stipulated equilibrium plateau, without uniquely identifying a real mechanism.

The supplied full table is public, so exclusion of t60 from fitting is an analytical instruction, not an enforced blind test. Balanced repeats establish neither independent sampling nor a real instrument-noise distribution. The preserved redox/metal case is a separate discussion, not an invented connection to the A/B chemistry.

## Separate calculations

`tests/content/test_general_chemistry_two_recalculations.py` covers all 64 numeric keys, including 18 preserved keys, and all 14 CSV checks. It imports no authoring artifacts. Root finding checks equilibrium ratios, temperature crossings, rate inversions, free metal balance and solubility. Successive acid ratios provide a second species-fraction construction. Component differential equations are integrated by RK4 for reversible trajectories and a sequential intermediate, rather than importing the author's exponential keys. Metal and ligand totals, admissible quadratic roots, diprotic mass/charge/equilibrium balance, electron occupancies, pairing energies, electrochemical equation scaling, target charge efficiency and reserved prediction are also checked.

The checks test selected calculations and counterexamples rather than every chemical claim, real measurement validity or learner effectiveness. New numeric items explicitly request a bare number in a stated scale; ten preserved items require units. No new significant-figure or dimensional enforcement is claimed. No grading implementation changed.

## Authoring corrections and verification

Before focused testing, draft length inspection found the reversible-kinetics reading below the structural threshold. A substantive paragraph about initial conditions below equilibrium and conserved-total direction was added. A separate arithmetic spot-check corrected a displayed `ln K` from 38.683145 to 38.683746; its stored numeric key was already correct and did not change. Preliminary reads of a nonexistent `cases/` path were corrected by using the manifest's preserved self-assessment entry.

The initial lint command `ruff check tests/content/test_general_chemistry_two_recalculations.py` failed on three ambiguous variable names and passed after renaming and formatting. The first focused command `python -B -m pytest tests/content/test_general_chemistry_two_recalculations.py tests/content/test_new_geroscience_and_statistics_lessons.py tests/content/test_learner_visible_number_formatting.py -q -p no:cacheprovider` had 493 passes and ten failures: seven missing standard limitation headings, two long-decimal formatting checks and one exact floating-point comparison. The repaired run passed all 503 checks. No numeric key changed, and every numeric-key calculation passed on the first run.

The real-grader command `python -B /workspace/courselab-session-artifacts/codex-general-chemistry-2-2026-10-09/check_grader.py` passed all 97 items. The complete six-step local verification passed on its first run: content (337 readings, 1816 questions, 1088 cards, zero errors and 98 disclosed legacy-depth warnings), seven legacy checks, security (705 source files, zero findings), ruff, 1,730 root tests and 3,889 backend tests with two existing symbolic-builder skips. The generated objective report matched and the claims scan had zero findings.

Full verification commands, focused results, any failures and repairs are recorded in [the validation report](../../VALIDATION_REPORT.md). Authoring artifacts and logs remain outside git in `courselab-session-artifacts/codex-general-chemistry-2-2026-10-09`. Integration is a guarded one-time artifact, not an update migration. Committed content is authoritative.

Frontend checks, the Docker Compose application stack and Playwright are not run locally for this content increment; publication CI runs them. No person reviewed the chemistry or measured workload. One lab and a proposed schedule do not establish a full laboratory sequence or semester equivalence.

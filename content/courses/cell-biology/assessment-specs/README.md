# Cell Biology assessment candidates

Biology 0.34.0 has a complete set of **inactive drafts** for the proposed semester assessments. The candidates are separate review artifacts; they are not listed as graded assessments in the course manifest, have no live submission route, and do not contribute to a course grade. The package remains partial, unreviewed and formative-only.

The public candidate inventory and artifact hashes are in the generated [assessment candidate audit](../../../../docs/ASSESSMENT_CANDIDATE_REPORT.md). It records the exact public versions and the unresolved gates without reading private keys. Keep those hashes fixed during review. A content change requires a new candidate version and matching key binding.

## Homework candidates

| Candidate | Authored version | Public packet | Draft scope |
| --- | --- | --- | --- |
| Homework 1 | 0.20.0 | [Instructions](homework-01-candidate.md), [pulse-chase data](homework-01-candidate-pulse-chase.csv), [answer-free DTOs](homework-01-candidate.json) | Seven items, 25 machine-check points; trafficking and pulse-chase evidence. |
| Homework 2 | 0.21.0 | [Instructions](homework-02-candidate.md), [fluorescence data](homework-02-candidate-fluorescence.csv), [answer-free DTOs](homework-02-candidate.json) | Eight items, 25 points; calibration, blanks, rate windows and model limits. |
| Homework 3 | 0.22.0 | [Instructions](homework-03-candidate.md), [lesion/reference data](homework-03-candidate-lesion-reference.csv), [answer-free DTOs](homework-03-candidate.json) | Eight items, 25 points; repair evidence, normalization and survivor selection. |
| Homework 4 | 0.23.0 | [Instructions](homework-04-candidate.md), [ChIP data](homework-04-candidate-chip.csv), [reporter data](homework-04-candidate-reporter.csv), [answer-free DTOs](homework-04-candidate.json) | Eight items, 25 points; matched controls, percent input and reporter evidence. |
| Homework 5 | 0.24.0 | [Instructions](homework-05-candidate.md), [baseline data](homework-05-candidate-baseline.csv), [chase data](homework-05-candidate-chase.csv), [answer-free DTOs](homework-05-candidate.json) | Eight items, 25 points; RNA composition and labeled protein-cohort loss. |
| Homework 6 | 0.25.0 | [Instructions](homework-06-candidate.md), [clone data](homework-06-candidate-clones.csv), [answer-free DTOs](homework-06-candidate.json) | Eight items, 25 points; nested clone evidence and fictional genotype probabilities. |
| Homework 7 | 0.26.0 | [Instructions](homework-07-candidate.md), [matrix data](homework-07-candidate-matrix.csv), [answer-free DTOs](homework-07-candidate.json) | Eight items, 25 points; matrix mechanics, ligand availability and localization. |
| Homework 8 | 0.27.0 | [Instructions](homework-08-candidate.md), [cell-fate data](homework-08-candidate-fate.csv), [answer-free DTOs](homework-08-candidate.json) | Eight items, 25 points; time-resolved cell-state denominators and re-entry. |

## Cumulative and laboratory candidates

| Candidate | Authored version | Public packet | Draft scope |
| --- | --- | --- | --- |
| Midterm | 0.28.0 | [Specification](midterm-specification.md), [candidate](midterm-candidate.md), [observations](midterm-candidate-observations.csv), [answer-free DTOs](midterm-candidate.json) | 16 cases, 100 machine-check points and two fixed forms. |
| Final | 0.29.0 | [Specification](final-specification.md), [candidate](final-candidate.md), [observations](final-candidate-observations.csv), [answer-free DTOs](final-candidate.json) | 28 cases, 150 machine-check points and two fixed forms. |
| Lab 1 | 0.30.0 | [Candidate](lab-01-candidate.md), [observations](lab-01-candidate-observations.csv), [answer-free DTOs](lab-01-candidate.json) | One case, 12 machine-check points and two fixed forms. |
| Lab 2 | 0.31.0 | [Candidate](lab-02-candidate.md), [observations](lab-02-candidate-observations.csv), [answer-free DTOs](lab-02-candidate.json) | One case, 12 machine-check points and two fixed forms. |
| Lab 3 | 0.32.0 | [Candidate](lab-03-candidate.md), [observations](lab-03-candidate-observations.csv), [answer-free DTOs](lab-03-candidate.json) | One case, 12 machine-check points and two fixed forms. |

The three draft lab candidates are separate from the existing open formative lab activities. Their written explanation and design prompts are not machine scored.

## Integrative project

The [project specification](integrative-project-specification.md), [portfolio instructions and human rubric](integrative-project-portfolio.md), and [limited machine-check candidate](integrative-project-candidate.md) describe a five-milestone portfolio. The reproducible synthetic teaching data are in [culture-level observations](integrative-project-candidate-cultures.csv) and [candidate observations](integrative-project-candidate-observations.csv); [the generator](generate_project_dataset.py) contains no grading keys. The machine-check subset has three cases, 18 points and two fixed forms. It is not a project grade. The seven-criterion human rubric has no accepted weights, submission process or grading policy.

## Review and activation status

All answer keys and candidate-specific grading checks remain outside Git. Public JSON files contain answer-free candidate metadata and learner DTOs. Same-AI calculations, mutations, fixture delivery and automated checks are development evidence only; they do not count as independent review.

Before a candidate can be accepted, the review must record the exact reviewed hashes and version and address:

- independent recalculation from the public raw observations, with comparison to the separately held key;
- grader-boundary and mutation cases, including malformed or incomplete responses and unit/tolerance edges;
- qualified scientific and assessment review of assumptions, controls, independent units, causal claims and objective coverage;
- manual accessibility and fairness review, plus measured learner workload and accommodations;
- human scoring for written explanations, plots, uncertainty and experimental design;
- protected form assignment, attempt/retake rules, historical source archives and appeal replay; and
- operator decisions for identity, release, grading, retention and incident handling.

The [audit report](../../../../docs/ASSESSMENT_CANDIDATE_REPORT.md) lists every candidate's hashes and gates. No reviewer or workload result is recorded here because neither has occurred. Candidate edits must preserve prior versions and key bindings; do not replace an external key in place. No draft is active, and no review or grade is implied by the presence of these files.

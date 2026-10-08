# Integrative project: specification and rubric (not authored)

**Course:** Foundations of Cell and Molecular Biology. **Planned week:** 14, with milestones across weeks 10 to 14. **Status:** specification only; not authored, not graded, not reviewed.

## What this document is not

- It is a **specification**, not an exam. No question, answer key, scoring script or protected answer package exists for this component, and none was created or committed.
- It does not make the course graded. The package remains `formative-only` and `partial`, with no deadlines, categories or weighted grade, and nothing here raises a maturity label or claims review.
- The planned item types and point allocations are a first draft by an AI coding assistant. They need review by a qualified subject-matter reviewer and an assessment reviewer before any item is written. No reviewer has examined this specification.

## Purpose

Learners would analyze a supplied synthetic multi-layer dataset, state a bounded conclusion, name alternative explanations and design a follow-up. The project would exercise outcomes O2 to O4 together. It is not an independent research project, uses no real samples and makes no claim about any therapy.

## Proposed dataset requirements (to be built)

A single original synthetic dataset with at least three layers (for example a molecular readout, a cellular readout and a cell-state or mechanics readout), at least two perturbations with a rescue or control, four independent units per condition, a documented data dictionary, and deliberately included confounds (for example unequal cell number or a viability trend) that the learner is expected to notice. The dataset and its generator are published; the answer specification is not.

## Milestones (proposed)

| Milestone | Week | Deliverable | Checked by |
|---|---:|---|---|
| M1 | 10 | Question, data dictionary reading, independent units identified | Auto-check of unit identification plus human feedback |
| M2 | 11 | Analysis plan: summaries, controls, alternatives | Human rubric |
| M3 | 13 | Calculated summaries and one figure with text alternative | CSV and graph auto-checks plus human rubric |
| M4 | 14 | Limits, alternatives and follow-up design | Human rubric |
| M5 | 14 | Short methods note with the analysis steps | Human rubric |

Automatic checks cover only deterministic numeric and coordinate cells; every prose element needs a human grader. Without a human grader the project cannot be graded, and the platform must not present an automatic score as a project grade.

## Analytic rubric (draft)

Four levels per criterion would map to 3, 2, 1 and 0 points; weights are not set. The levels below show the top, middle and lowest descriptions.

| Criterion | Full evidence | Partial evidence | Little or no evidence |
|---|---|---|---|
| Question and scope | Question is specific, answerable with the supplied synthetic dataset, and bounded to in-vitro evidence. | Question is relevant but broad or partly unanswerable with the data. | Question is vague, unanswerable, or makes a clinical claim. |
| Evidence summary | Summarizes replicate-level data with the correct independent unit and units; no pseudoreplication. | Mostly correct summaries; a unit or replicate error does not change conclusions. | Treats technical measurements as independent or misreports values. |
| Controls and alternatives | Names the controls present and absent and at least two alternative explanations with the data that would separate them. | Names controls or alternatives but not how to separate them. | Does not engage with controls or alternatives. |
| Quantitative reasoning | Calculations are correct, shown, and carry units; uncertainty or its absence is stated. | Minor calculation or presentation errors. | Calculations missing or wrong in ways that change conclusions. |
| Inference and limits | Conclusions follow from the data and state what is not shown (mechanism, generality, function, clinical meaning). | Conclusions mostly bounded; one overreach. | Conclusions overreach the data or imply clinical benefit. |
| Follow-up design | A testable next experiment with perturbation, readout, controls and independent unit. | A plausible next step missing a control or unit. | No testable follow-up. |
| Communication and reproducibility | Clear figure with text alternative, labelled axes with units, and a short methods note that lets another person redo the analysis. | Understandable but incomplete methods or figure labelling. | Unclear or not reproducible. |

## Conduct and delivery

- Collaboration and tool-use rules, including whether AI tools may be used and how use is disclosed, are a policy decision for whoever offers the course; none is set here.
- Submission formats are limited to what the platform parses safely (UTF-8 CSV, text and coordinates). The platform does not execute submitted code; code execution stays disabled until isolation is demonstrated.
- Human grading uses the existing appeal and instructor-decision workflow; automatic scores remain separate from human decisions.

## Protection and delivery requirements (for whoever builds it)

## Accessibility and conduct requirements

- Every figure, plot and gel image has a text alternative and a data table; no item depends on colour alone.
- Time limits state a base time and an extended-time rule; the interface never requires a mouse for graph-coordinate items.
- Items use plain language and units; no item requires recall of a licensed figure or text.
- Practice items (public keys) are never reused as exam items.
- An accessibility review by a qualified person is required before activation; none has been done.

## Review checklist for a future qualified reviewer

- [ ] Dataset supports the milestones without a hidden answer being required.
- [ ] Rubric criteria are observable and the levels distinguishable.
- [ ] Workload estimate measured, not assumed.
- [ ] Accessibility and fairness reviewed by named people.
- [ ] Policy on collaboration and AI-tool use set by the course owner.
- [ ] Reviewer details recorded only after the review has happened.

# Cell and Molecular Biology: proposed scope and assessment crosswalk

**Crosswalk status:** planning document, version 0.4.0. It is not a set of authored assignments. **The course remains partial.** Only weeks 1–2 have two developed lessons and current formative items; compact legacy lessons remain in weeks 4 and 7; other planned weeks have no instructional packages or assessment specifications.

## Intended course outcomes

- **O1 — Structure and function:** Relate molecular structure and chemical environment to plausible biological function, and state what those observations do not establish.
- **O2 — Quantitative models:** Apply membrane, enzyme, and free-energy models while checking assumptions, units, and limits.
- **O3 — Information flow:** Trace genetic information through DNA replication, RNA processing, regulation, translation, and phenotype.
- **O4 — Experimental reasoning:** Evaluate perturbations, measurements, controls, uncertainty, alternatives, and the scope of causal claims.

The IDs below refer to the course outcomes in `course.json`. New lesson-objective IDs are created only as corresponding instruction and assessments are authored; this outline does not substitute for that mapping.

## Proposed weekly map

| Week | Learning focus and measurable performance | Outcome alignment | Assessment design intent | Evidence now |
| --- | --- | --- | --- | --- |
| 1 | Distinguish covalent connectivity from intermolecular forces; use chemical groups and solvent context to predict plausible molecular interactions. | O1, O4 | Low-stakes question set on functional groups, interaction changes, and limits of structure-based predictions. | Two original lessons; public formative items only. |
| 2 | Use residue environment to make a bounded protein-variant prediction; calculate a monovalent ion's equilibrium potential and distinguish channels from pumps. | O1, O2, O4 | Practice set on protein-variant evidence and electrochemical equilibrium; later add a short data worksheet. | Two original lessons; public formative items only. |
| 3 | Compare organelle and trafficking models; infer whether localization, abundance, or activity is the altered phenotype from matched measurements. | O1, O3, O4 | **Homework 1:** interpret microscopy, fractionation, and localization controls. | Scope only; no lesson or assignment file. |
| 4 | Interpret enzyme-rate curves, distinguish `Km` from a binding constant, and calculate whether a coupled reaction can be favorable. | O2, O4 | **Homework 2:** fit or compare initial-rate data, propagate simple uncertainty, and justify model limits. | One compact prototype reading and a single formative item; not a developed week. |
| 5 | Select a measurement for a cell-biological claim and explain resolution, specificity, dynamic range, and calibration limits. | O1, O4 | **Lab 1:** compare synthetic microscopy and fractionation measurements with controls; state what each readout cannot show. | Scope only; no activity or data file. |
| 6 | Trace replication and repair from strand polarity and template rules; distinguish a sequence observation from a repair-mechanism claim. | O3, O4 | **Homework 3:** analyze replication/repair perturbation results and positive, negative, and loading controls. | Scope only; no lesson or assignment file. |
| 7 | Integrate weeks 1–6 by explaining a molecular mechanism, solving a bounded quantitative problem, and evaluating experimental evidence. | O1, O2, O3, O4 | **Midterm:** mixed mechanism, data, and short structured-control items; answer specifications and rubric required before use. | Planned only; no exam or protected answer key. |
| 8 | Distinguish transcriptional association, direct occupancy, cis-element dependence, and a causal effect in the tested system. | O3, O4 | **Homework 4:** analyze a reporter and ChIP-qPCR design with matched controls, replicates, and inference boundaries. | One compact legacy gene-expression reading and formative experimental-logic item; not a developed week. |
| 9 | Predict how RNA processing, translation, and protein turnover can produce different RNA and protein measurements. | O1, O3, O4 | **Homework 5:** reconcile RNA, protein, and localization results without inferring one layer from another. | Scope only; no lesson or assignment file. |
| 10 | Separate variant association, molecular mechanism, and phenotype; use segregation or perturbation evidence without overgeneralizing. | O1, O3, O4 | **Homework 6:** compare alternative genotype-to-phenotype models with explicit assumptions. | Scope only; no lesson or assignment file. |
| 11 | Trace a receptor input through a signaling network and predict how feedback or a second perturbation changes the observed response. | O2, O3, O4 | **Lab 2:** analyze an original synthetic time-course with vehicle, inhibitor, and rescue controls. | Scope only; no simulation, data, or assignment. |
| 12 | Distinguish cytoskeletal organization, adhesion, and matrix mechanics as candidate causes of a measured cell response. | O1, O2, O4 | **Homework 7:** design a controlled perturbation and select measurements that separate cell number, viability, and state. | Scope only; no lesson or assignment file. |
| 13 | Interpret cell-cycle, senescence, and cell-death evidence; distinguish cell-state markers from functional potency claims. | O1, O3, O4 | **Homework 8 and Lab 3:** analyze a synthetic lineage/time-course dataset and identify ethical and technical limits of the proposed cell-state inference. | Scope only; no lesson, lab, data, or rubric. |
| 14 | Integrate molecular evidence into a testable model, defend design choices, and state alternative explanations and next experiments. | O1, O2, O3, O4 | **Cumulative final and integrative project:** synthesize a cell-biology dataset and present a reproducible experimental plan with an analytic rubric. | Planned only; no final, project package, rubric, or graded workflow. |

## Assessment inventory and maturity

| Component | Planned distribution | Current state |
| --- | --- | --- |
| Weekly formative practice | Every developed week; explicit scoring and feedback | Several public practice questions exist for the seed lessons and the new first two weeks. They test selected claims only. |
| Homework | Eight sets, H1–H8, mapped above | None of the eight full homework packages is authored. No homework contributes to a course grade. |
| Data or virtual lab | Three activities, L1–L3, mapped above | The existing cell-biology CSV item summarizes a small supplied table; it is not a lab sequence or simulation. No new lab is enabled by this outline. |
| Midterm | Week 7 | Not authored. |
| Cumulative final | Week 14 | Not authored. |
| Integrative project | Week 14, with milestones to be designed | Not authored; no project rubric or solution specification exists. |
| Retrieval practice | Spaced retrieval across core outcomes | Current cards are revealable static prompts; review history and scheduled spacing are not implemented. |

All present questions are formative and their public practice keys are not suitable for secure exams. This package has no deadlines, weighted categories, summative grade, or verified workload estimate. The future assessment inventory must be written and tested before any graded-course mode is configured. Objective-to-assessment coverage in the proposed weeks is a design target, not evidence of achieved coverage or mastery.

## Scope comparator and provenance

The sequence is an original planning proposal informed at the topic level by the public scope of MIT OpenCourseWare 7.01SC Fundamentals of Biology and 7.28x Molecular Biology. These are **link-only comparators** in `../../sources/registry.json`; the course does not reproduce or adapt their lectures, figures, problems, exams, or text. No MIT endorsement, course equivalence, prerequisite equivalence, or credit transfer is implied. Every new module requires a per-reading provenance entry in `source-map.json`; third-party assets require separate affirmative license review.

## Completion work still required

Author and review the weeks 3–14 lessons, the eight substantive homework sets, three data/lab activities, midterm, cumulative final, and integrative project. Map every actual learning objective to valid assessments; add answer specifications, independent numerical checks, unit/tolerance and grader mutation tests, accessibility alternatives, misconception-specific feedback, workload evidence, and qualified scientific and accessibility reviews. Preserve `partial` status until the entire course package passes the documented gates.

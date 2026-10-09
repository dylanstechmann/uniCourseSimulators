# Cumulative final: specification with inactive authoring draft

**Course:** Foundations of Cell and Molecular Biology. **Planned week:** 14. **Status:** specification plus inactive draft; not accepted, not graded, not reviewed.

## What this document is not

- This is a **specification**. A separate inactive candidate now has original questions and external machine keys; no protected answer package is committed. No accepted exam or project grade exists.
- It does not make the course graded. The package remains `formative-only` and `partial`, with no deadlines, categories or weighted grade, and nothing here raises a maturity label or claims review.
- The planned item types and point allocations are a first draft by an AI coding assistant. They need review by a qualified subject-matter reviewer and an assessment reviewer before any form is accepted or activated. The owner authorized inactive draft authoring before review; that authoring does not satisfy review gates. No reviewer has examined this specification.

## Scope and purpose

The final would sample all lessons, with extra weight on integration across layers (structure, kinetics, information flow, signaling, mechanics, cell state, potency) and on the experimental-reasoning outcome O4. It would measure application and evaluation of evidence; it would not measure laboratory technique or clinical judgement, and a result would say nothing about any therapy.

## Format (proposed)

- 150 points, one sitting, base time from a measured pilot, extended-time rule.
- At least 40 percent of points in multi-step data items (data interpretation, CSV summary, graph coordinates, structured control logic) built on new synthetic datasets that mirror, but do not repeat, the homework and lab designs.
- A fixed share of points reserved for integration items that span two or more lessons; each such item lists all objective IDs it covers.

## Blueprint (draft)

28 lessons, 70 objective-link occurrences covering 69 distinct objectives (one objective is reused across lessons). Points are proportional to objective count with a two-point floor. Objectives from lessons already sampled on the midterm are sampled again at a new level where the verb allows (apply, then evaluate).

| Lesson | Title | Objectives | Objective numbers | Points | Planned item types (draft) |
|---|---|---:|---|---:|---|
| cell-biology-1 | Covalent architecture, functional groups, and biological molecules | 3 | 1, 2, 3 | 7 | numeric; single choice |
| cell-biology-5 | Water, pH, and noncovalent interactions | 2 | 2, 1 | 4 | multiple select; structured |
| cell-biology-6 | Protein sequence, structure, and variant evidence | 2 | 1, 2 | 4 | data interpretation; numeric |
| cell-biology-2 | Membranes, transport, and electrochemical gradients | 2 | 1, 2 | 4 | single choice; multiple select |
| cell-biology-7 | Organelle compartments, membrane topology, and protein targeting | 2 | 1, 2 | 4 | structured; data interpretation |
| cell-biology-8 | Protein sorting, vesicle traffic, and experimental inference | 2 | 1, 2 | 4 | numeric; single choice |
| cell-biology-3 | Enzymes and cellular energetics | 2 | 1, 2 | 4 | multiple select; structured |
| cell-biology-9 | Enzyme catalysis, reaction mechanisms, and free energy | 2 | 1, 2 | 4 | data interpretation; numeric |
| cell-biology-10 | Initial-rate evidence and reversible enzyme inhibition | 2 | 1, 2 | 4 | single choice; multiple select |
| cell-biology-11 | Cell imaging: resolution, contrast, and quantitative limits | 2 | 1, 2 | 4 | structured; data interpretation |
| cell-biology-12 | Cell fractionation: enrichment, contamination, and recovery | 2 | 1, 2 | 4 | numeric; single choice |
| cell-biology-13 | DNA structure, genome organization, and semiconservative replication | 2 | 1, 2 | 4 | multiple select; structured |
| cell-biology-14 | DNA damage, repair pathways, and evidence of lesion removal | 2 | 1, 2 | 4 | data interpretation; numeric |
| cell-biology-4 | Gene expression and experimental logic | 3 | 1, 2, 3 | 7 | single choice; multiple select |
| cell-biology-15 | Chromatin accessibility and regulatory DNA | 2 | 1, 2 | 4 | structured; data interpretation |
| cell-biology-16 | Transcription-factor occupancy and reporter evidence | 2 | 1, 2 | 4 | numeric; single choice |
| cell-biology-17 | RNA processing and isoform evidence | 3 | 1, 2, 3 | 7 | multiple select; structured |
| cell-biology-18 | Translation and protein turnover | 3 | 1, 2, 3 | 7 | data interpretation; numeric |
| cell-biology-19 | Inheritance, penetrance, and pedigree evidence | 3 | 1, 2, 3 | 7 | single choice; multiple select |
| cell-biology-20 | Variant mechanism and isogenic evidence | 3 | 1, 2, 3 | 7 | structured; data interpretation |
| cell-biology-21 | Receptors, signaling pathways, and network logic | 3 | 1, 2, 3 | 7 | numeric; single choice |
| cell-biology-22 | Signaling dynamics, feedback, and perturbation evidence | 3 | 1, 2, 3 | 7 | multiple select; structured |
| cell-biology-23 | Cytoskeletal systems, adhesion, and extracellular matrix | 3 | 1, 2, 3 | 7 | data interpretation; numeric |
| cell-biology-24 | Matrix mechanics and mechanotransduction | 3 | 1, 2, 3 | 7 | single choice; multiple select |
| cell-biology-25 | Cell-cycle control, checkpoints, and mitosis | 3 | 1, 2, 3 | 6 | structured; data interpretation |
| cell-biology-26 | Quiescence, senescence, apoptosis, and cell-fate evidence | 3 | 1, 2, 3 | 6 | numeric; single choice |
| cell-biology-27 | Developmental potency, stem-cell states, and lineage evidence | 3 | 1, 2, 3 | 6 | multiple select; structured |
| cell-biology-28 | Integrative regenerative-biology study design | 3 | 1, 2, 3 | 6 | data interpretation; numeric |

## Item requirements

Same as the midterm, plus: every integration item names the layers it connects, states the independent unit, and has at least one wrong option that reflects a documented misconception from `misconceptions.md`.

## Protection and delivery requirements (for whoever builds it)

- Learner-facing instructions, datasets and stems live in the public package; `solution_spec` and answer-bearing feedback live only in the protected store, referenced as `private://assignments/<file>.json` under `<private-root>/courses/cell-biology/assignments/`, mounted through `COURSELAB_PRIVATE_ASSESSMENTS_PATH` (see `docs/DEPLOYMENT.md`). The answer file is never committed, including on a temporary branch.
- Use authored variants with fixed seeds (`authored-variants-v1`) so retakes and appeals can be reproduced; record the variant and digest per attempt.
- The strict-deadline policy is the only supported late-work rule. Release, due time and attempt limits are set in the assessment schedule, not in this document.
- Content is archived by hash before use so an appeal can load the version the learner saw; until immutable archives exist, changed content can only be declined on appeal.
- Every numeric key is independently recalculated by a second method before activation, and every grader has mutation tests (alternate correct forms, wrong units, near misses, malformed input, misleading keywords).

## Accessibility and conduct requirements

- Every figure, plot and gel image has a text alternative and a data table; no item depends on colour alone.
- Time limits state a base time and an extended-time rule; the interface never requires a mouse for graph-coordinate items.
- Items use plain language and units; no item requires recall of a licensed figure or text.
- Practice items (public keys) are never reused as exam items.
- An accessibility review by a qualified person is required before activation; none has been done.

## Review checklist for a future qualified reviewer

- [ ] Coverage spans all four outcomes and all lessons; no lesson is untested.
- [ ] Integration items test integration, not recall of two facts.
- [ ] Keys independently recalculated; grader mutation tests pass.
- [ ] Accessibility and fairness reviewed by named people.
- [ ] Pilot data support the time limit; no item is trivial or unanswerable.
- [ ] Reviewer details recorded only after the review has happened.

## Current inactive implementation

See the [final candidate](final-candidate.md). This draft uses bounded numeric/categorical fields and two fixed authored forms, with external keys and inspectable mappings. Planned written design, uncertainty and any broader item-type mix require human review and implementation; the candidate is not an accepted realization of every blueprint requirement. Independent and qualified reviews, workload and release policy remain absent.

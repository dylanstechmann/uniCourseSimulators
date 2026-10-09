# Midterm: specification with inactive authoring draft

**Course:** Foundations of Cell and Molecular Biology. **Planned week:** 8. **Status:** specification plus inactive draft; not accepted, not graded, not reviewed.

## What this document is not

- This is a **specification**. A separate inactive candidate now has original questions and external machine keys; no protected answer package is committed. No accepted exam or project grade exists.
- It does not make the course graded. The package remains `formative-only` and `partial`, with no deadlines, categories or weighted grade, and nothing here raises a maturity label or claims review.
- The planned item types and point allocations are a first draft by an AI coding assistant. They need review by a qualified subject-matter reviewer and an assessment reviewer before any form is accepted or activated. The owner authorized inactive draft authoring before review; that authoring does not satisfy review gates. No reviewer has examined this specification.

## Scope and purpose

The midterm would sample the teaching block of weeks 1 to 7: molecular structure and interactions, proteins and membranes, trafficking, enzyme kinetics, imaging and fractionation, replication and repair, and chromatin and transcription evidence. It would measure whether a learner can apply quantitative models and evaluate experimental evidence in those lessons. It would not measure laboratory skill, retention beyond the exam window, or readiness for any other course. Week 8's existing cumulative practice set is ungraded review and is not a substitute.

Course outcomes assessed: O1 structure and function, O2 quantitative models, O3 information flow, O4 experimental reasoning (outcome IDs in `course.json`).

## Format (proposed)

- 100 points, one sitting, a base time to be set from a measured pilot (none exists), with an extended-time rule.
- Mix of item types the platform already grades deterministically: numeric with units and significant figures, single choice, multiple select, structured choice, data interpretation, CSV summary upload and graph coordinates. Written explanations are not auto-scored; if they are wanted they need a human rubric and a human grader.
- Each item references exactly the objective IDs it assesses; each lesson's objectives must be hit at least once before the form is accepted.

## Blueprint (draft)

16 lessons, 34 objective-link occurrences covering 33 distinct objectives (one objective is reused across lessons). Points are proportional to objective count with a two-point floor.

| Lesson | Title | Objectives | Objective numbers | Points | Planned item types (draft) |
|---|---|---:|---|---:|---|
| cell-biology-1 | Covalent architecture, functional groups, and biological molecules | 3 | 1, 2, 3 | 8 | numeric; single choice |
| cell-biology-5 | Water, pH, and noncovalent interactions | 2 | 2, 1 | 6 | multiple select; structured |
| cell-biology-6 | Protein sequence, structure, and variant evidence | 2 | 1, 2 | 6 | data interpretation; numeric |
| cell-biology-2 | Membranes, transport, and electrochemical gradients | 2 | 1, 2 | 6 | single choice; multiple select |
| cell-biology-7 | Organelle compartments, membrane topology, and protein targeting | 2 | 1, 2 | 6 | structured; data interpretation |
| cell-biology-8 | Protein sorting, vesicle traffic, and experimental inference | 2 | 1, 2 | 6 | numeric; single choice |
| cell-biology-3 | Enzymes and cellular energetics | 2 | 1, 2 | 6 | multiple select; structured |
| cell-biology-9 | Enzyme catalysis, reaction mechanisms, and free energy | 2 | 1, 2 | 6 | data interpretation; numeric |
| cell-biology-10 | Initial-rate evidence and reversible enzyme inhibition | 2 | 1, 2 | 6 | single choice; multiple select |
| cell-biology-11 | Cell imaging: resolution, contrast, and quantitative limits | 2 | 1, 2 | 6 | structured; data interpretation |
| cell-biology-12 | Cell fractionation: enrichment, contamination, and recovery | 2 | 1, 2 | 6 | numeric; single choice |
| cell-biology-13 | DNA structure, genome organization, and semiconservative replication | 2 | 1, 2 | 6 | multiple select; structured |
| cell-biology-14 | DNA damage, repair pathways, and evidence of lesion removal | 2 | 1, 2 | 6 | data interpretation; numeric |
| cell-biology-4 | Gene expression and experimental logic | 3 | 1, 2, 3 | 8 | single choice; multiple select |
| cell-biology-15 | Chromatin accessibility and regulatory DNA | 2 | 1, 2 | 6 | structured; data interpretation |
| cell-biology-16 | Transcription-factor occupancy and reporter evidence | 2 | 1, 2 | 6 | numeric; single choice |

Types rotate through the grader's supported set so that no lesson is assessed with one format only; the actual choice should follow the objective's verb (calculate, compare, justify) once a reviewer assigns them.

## Item requirements

1. Each item has a stem, a stated unit and tolerance where numeric, a stated scoring rule and a misconception-targeted feedback entry (hidden until release).
2. Datasets are original and synthetic and labelled so; stems state the independent unit.
3. At least a quarter of the points should require evaluating a control or alternative explanation rather than recalling a fact.
4. No item may rely on the learner knowing an answer from a public practice item verbatim.
5. A form is accepted only when the coverage check (`tools/objective_coverage.py` extended to the form) shows every objective hit.

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

- [ ] Each objective is assessed at the level its verb implies.
- [ ] Every key independently recalculated; units and tolerances justified.
- [ ] No item can be answered by keyword matching or prompt injection.
- [ ] Reading level, bias and accessibility checked by a named person.
- [ ] Pilot with synthetic learner data confirms time and item statistics.
- [ ] Reviewer name, role, reviewed version and date recorded in `course.json` `review` (not before).

## Current inactive implementation

See the [midterm candidate](midterm-candidate.md). This draft uses bounded numeric/categorical fields and two fixed authored forms, with external keys and inspectable mappings. Planned written design, uncertainty and any broader item-type mix require human review and implementation; the candidate is not an accepted realization of every blueprint requirement. Independent and qualified reviews, workload and release policy remain absent.

# Homework 1 candidate: pulse-chase sorting and recovery evidence

**State:** inactive candidate for review, authored with substantial Codex assistance. It is not an available graded assignment and contributes no course grade. No scientific, assessment or accessibility reviewer has approved it. Current course version: 0.20.0, partial, unreviewed and formative-only.

## Preparation and purpose

Read [organelle compartments and protein targeting](../modules/03a-organelle-compartments-and-protein-targeting.md) and [protein sorting and vesicle traffic](../modules/03b-protein-sorting-and-vesicle-traffic.md). The separate open Homework 1 companion remains available for practice. This candidate uses a new dataset and new questions; the open companion is not being relabeled as protected material.

The task connects membrane topology, paired time-course observations, preparation-specific normalization, material recovery and bounded experimental inference. A numerical result supports only the quantity actually measured. A difference in a lysosome-enriched fraction can reflect transport, turnover, recovery or multiple processes. The task asks you to keep those alternatives visible while choosing an additional discriminating measurement.

The seven proposed machine-scored items total 25 points. That allocation is a review draft, not course grading. A separate written discussion below has no automated score or proposed grade weight. No deadline, time limit or attempt limit has been selected; workload has not been measured. The candidate is not listed in the Practice gradebook and has no live submission route. Do not infer that a draft point total satisfies the course's assessment requirements.

## Experimental construction

Download the [synthetic pulse-chase table](homework-01-candidate-pulse-chase.csv). Wild-type receptor, a cytosolic-tail motif mutant and a motif-repaired clone each have four independently propagated culture preparations. Preparation codes w01–w04, m01–m04 and r01–r04 identify those culture preparations. Each preparation supplies matched chase observations at 0, 30 and 90 minutes from aliquots of the same preparation. Aliquots and time points are repeated observations within that preparation; they are not new independently propagated cultures. There is one clone per condition, so preparation replication does not estimate variability across independently engineered clones.

A soluble M6P-bearing hydrolase receives a synthetic pulse label. The dataset follows intact labeled cargo recovered in a lysosome-enriched fraction, intact cargo in the medium, other intact cell-associated cargo and a separately recorded fragment pool. These four recorded pools are stipulated to be disjoint for this paper exercise. They need not recover every initially labeled molecule. Fragment label is not synonymous with secreted intact hydrolase; missing recovery is not automatically degradation or secretion. No real experiment or wet-lab procedure was performed.

Each culture has its own time-zero pulse input, and that same denominator applies to all chase observations from it. Pulse inputs differ across preparations. First express each chosen amount as a percentage of its matched pulse input, then average those preparation-level percentages. Dividing a pooled amount sum by a pooled input sum answers a differently weighted question. Preserve the preparation identities when calculating 90-minus-30-minute changes. A mean over every chase row can erase the intended endpoint and create a misleading replicate count.

## Data dictionary

| Column | Meaning and scale |
|---|---|
| condition | wt, motif_mutant or motif_repaired; three separate groups |
| preparation | Independently propagated culture identifier, repeated across its three chase observations |
| chase_min | Minutes since the pulse, with values 0, 30 and 90 |
| pulse_input_nmol | Preparation-specific initial labeled amount in nanomoles; repeated as a denominator |
| lysosome_intact_nmol | Intact label recovered in the lysosome-enriched fraction, nanomoles |
| medium_intact_nmol | Intact label in conditioned medium, nanomoles |
| other_intact_nmol | Other recovered intact cell-associated label, nanomoles |
| fragments_nmol | Recovered fragment label, nanomoles; separate from intact pools |
| lysosome_marker_recovery_pct | Recovery percentage for a reference marker in the fraction-processing check |
| binding_index | Matched ligand-binding index, normalized on a stated reference scale near 100 |
| receptor_abundance_index | Whole-cell receptor-abundance index on a stated reference scale near 100 |
| viability_pct | Viability percentage for that preparation |

The final three channels and marker recovery are stipulated control measurements, not independent cultures. Similar values can constrain alternatives without proving equivalence, fraction purity, a direct tail-adaptor interaction or equal recovery of marker and cargo. No statistical test, uncertainty estimate or biological functional readout is supplied. Repeating an index across chase rows adds no independent information.

## Response rules

For the amount item, enter a value and a compatible amount unit with exactly three significant figures. For the relative-change item, include a percent unit and exactly four significant figures. Unit conversion is permitted by the supported numeric grader. The signed percentage-point contrast requests a bare number in that explicit scale; it does not enforce significant figures or a dimension label. Keep percentage-point differences separate from relative percent change.

The summary upload must be a small UTF-8 CSV with the exact column order shown in its item and one unique row per listed condition. Do not put formulas in cells. Report percentages as numbers on the 0–100 scale, without percent symbols inside the table. Preparation counts must be exact; component means have the stated tolerance. Upload scoring covers those nine numeric cells only, not your analysis script, uncertainty discussion or scientific explanation.

Single-choice responses select one listed option per field. Each structured field has one point and receives credit independently. Multiple-select scoring uses the explicitly stated correct-minus-incorrect rule. The displayed option numbers in this document start at one for reading; software DTO indexes start at zero. No reasoning credit is awarded merely for selecting the scored categorical option.

## Item stems and proposed allocation

### Item 1 — 2 proposed points

For wt preparation w01 at 90 min, sum the intact lysosome, medium, other and fragment amounts. Report recovered label in an amount unit with exactly three significant figures.

### Item 2 — 2 proposed points

For each preparation calculate the 90-minus-30 min lysosome percentage-point increment using its pulse input. Average those increments within each condition. Report mutant mean increment minus wt mean increment as a bare signed number in percentage points (not a relative percent change).

### Item 3 — 2 proposed points

Calculate 100 times (mean wt lysosome percentage at 90 min minus mean mutant lysosome percentage at 90 min) divided by mean wt lysosome percentage at 90 min. Report the descriptive relative decrease with a percent unit and exactly four significant figures.

### Item 4 — 9 proposed points

At 90 min, normalize each amount to its own preparation pulse input before averaging. Upload a UTF-8 CSV with exact columns condition,preparations,mean_lysosome_pct,mean_medium_pct and one row each for wt,motif_mutant,motif_repaired. Counts are exact; mean tolerance is 0.005 percentage points. The three chase times are repeated observations of each preparation, not additional independent cultures.

### Item 5 — 2 proposed points

Select all statements compatible with the declared soluble M6P-bearing cargo and receptor route. Scoring is two points times (the number of correct options selected minus the number of incorrect options selected) divided by the total number of correct options, clamped from zero to two.

1. The lumen-facing ligand-binding part of the receptor and its cytosolic tail occupy different membrane sides.

2. Every vesicle transport step requires soluble lumenal cargo to cross the lipid bilayer.

3. A tail-motif change must abolish the receptor ligand-binding site even if binding measurements are similar.

4. A receptor can recycle after cargo release while the hydrolase proceeds toward a degradative compartment.

5. Similar binding values prove a particular cytosolic adaptor binds the receptor directly.

### Item 6 — 4 proposed points

Choose one response for each independent criterion about controls in this pulse-chase construction.

**normalization (1 point):** Which denominator matches each outcome?

1. The largest pulse input in the dataset.

2. That preparation's time-zero pulse input.

3. Its lysosome-marker recovery percentage.

**replication (1 point):** What is the biological replicate unit?

1. Each culture preparation; its chase observations are repeated measures.

2. Each chase row is a new independent culture.

3. Each measurement column is an independent culture.

**fraction (1 point):** What does a similar marker-recovery percentage support?

1. It makes every fraction pure.

2. It proves cargo recovery equals marker recovery.

3. It checks one aspect of fraction processing without proving purity or cargo-specific recovery.

**missing (1 point):** How should an unexplained difference between input and recovered label be described?

1. It is automatically secreted cargo.

2. It is missing from the displayed recovery ledger; additional accounting is needed.

3. It proves receptor degradation.

### Item 7 — 4 proposed points

Choose one response per criterion for a bounded interpretation and discriminating follow-up.

**repair (1 point):** What does movement toward the wt pattern after motif repair add?

1. Evidence consistent with a contribution of the altered locus in this construction; independent repaired clones remain useful.

2. Proof that all trafficking abnormalities share this mechanism.

3. Proof of direct adaptor binding.

**mechanism (1 point):** Which additional study addresses direct tail-adaptor interaction most directly?

1. A higher viability percentage alone.

2. A declared binding assay with tail/adaptor controls and independent replication, considered alongside cell trafficking.

3. Another endpoint mean with no adaptor measurement.

**timecourse (1 point):** What does the paired late increment describe?

1. A constant microscopic transport rate with no competing destinations.

2. A validated lysosomal functional activity.

3. A descriptive net change in the measured fraction across that interval, with transport, turnover and recovery alternatives.

**design (1 point):** Which follow-up best addresses the incomplete recovery ledger?

1. Measure intact and fragment label across cell-associated and medium pools over time with recovery controls and independent cultures.

2. Set every missing amount to zero and call it secretion.

3. Pool all chase rows as independent biological replicates.

## Written discussion for human review

Write a short account of the measured direction and timing of the cargo-distribution differences, retaining the preparation unit and the distinction between amounts and normalized percentages. Explain how incomplete recovery limits a statement about secretion or degradation. Use the binding, abundance, viability and fraction-process channels to discuss at least two alternative explanations, then propose a time-resolved or independent interaction measurement that makes different predictions under those explanations. State what the repaired clone adds and why one clone per condition cannot settle all genotype-related alternatives.

A future human reviewer should assess whether the response names the measured quantity, uses matched denominators and preparation pairing, accounts for omitted material, separates process controls from mechanism, and connects a proposed measurement to competing predictions. Descriptors are: absent or incompatible reasoning, partly correct reasoning with a material omission, and coherent reasoning with explicit assumptions and limitations. These descriptors are a draft discussion rubric, not scored software criteria or a released grade policy. No written response has been assessed by a human or AI grader.

## Accessibility, provenance and limits

All essential observations are in the CSV with plain-text labels and explicit units. The task requires no color discrimination, image reading, custom graph or timed interaction. A screen-reader/manual workflow review and a measured workload study remain required; these design choices are not evidence that accessibility or fairness passed. An equivalent accessible table format should be checked with a qualified reviewer before any deployment rather than silently changing what is assessed.

The construction is an original exercise based on the existing course lessons. No new outside source, paper identifier, third-party data, prose, problem or figure was introduced. Original instructions and synthetic observations are CC BY 4.0 with substantial AI assistance. The answer package is held outside the repository for review, but a public dataset and question stems do not prevent a learner from solving the task independently or guarantee assessment security. No physical measurement, unique trafficking mechanism, lysosomal function, clinical outcome or university credit is established. Independent recalculation, qualified review and operator release decisions remain outstanding.

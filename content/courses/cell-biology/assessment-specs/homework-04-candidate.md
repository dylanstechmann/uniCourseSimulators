# Homework 4 candidate: ChIP denominators and reporter claim boundaries

**State:** inactive candidate for review, developed with substantial Codex assistance. It is not served as graded coursework and contributes no course grade. Authored Biology package: 0.23.0, partial, unreviewed and formative-only. No independent numerical, scientific, assessment or accessibility reviewer has approved the packet.

## Preparation and purpose

Read [Chromatin accessibility and regulatory DNA](../modules/07a-chromatin-accessibility-and-regulatory-dna.md) and [Transcription-factor occupancy and reporter evidence](../modules/07b-transcription-occupancy-and-reporter-evidence.md). The open Homework 4 companion remains practice with public keys. This separate candidate has new data and stems; those practice answers have not been relabeled as confidential material.

The task distinguishes starting-material normalization, nonspecific pull-down, motif-dependent reporter activity and causal contribution at a native locus. A ChIP percent-input value is not a percentage of cells with bound factor. Cross-linked recovery can include indirectly associated complexes. A plasmid reporter does not recreate native copy number, chromatin or neighboring regulatory context. Agreement between proxies cannot identify every hidden causal link.

Eight proposed machine-scored items total 25 points. Their allocation is a review draft; it does not select a course-grade policy. Written reasoning is unscored, workload has not been measured, and no deadline, time limit or live attempt policy has been chosen. The candidate is not in the Practice gradebook and has no live submission route. All activation gates remain open.

## Two separate observation sets

The [ChIP table](homework-04-candidate-chip.csv) contains control, knockdown and restored conditions, each with four independently cultured preparations. Culture IDs are c01–c04, k01–k04 and s01–s04. Each culture contributes a candidate, known positive and unrelated negative locus, with two technical qPCR wells for each input/specific-IP/IgG comparison: 72 rows. Loci, DNA channels and duplicate wells do not add biological cultures. There is one engineered line per condition; these cultures do not estimate variability across independent engineered clones.

The [reporter table](homework-04-candidate-reporter.csv) contains four separately prepared transfection cultures per condition (rc01–rc04, rk01–rk04 and rs01–rs04). Each preparation is split across promoter-only, candidate WT, motif-disrupted and positive constructs. These splits support within-preparation comparisons under the stated construction. They do not add independent preparations. ChIP and reporter culture IDs refer to different samples; row numbers and condition labels do not authorize a paired cross-assay correlation.

Every value is a deterministic synthetic teaching observation. No physical experiment, sampling distribution, calibrated standard curve, technical-error distribution or assay uncertainty was measured. The supplied amplification factors and backgrounds are assumptions of the exercise, not validation data for a real assay. No significance test or population interval is requested.

## ChIP data dictionary and analysis contract

| Column | Meaning |
|---|---|
| condition, culture | Perturbation group and independently cultured preparation |
| locus | candidate, positive or negative amplicon |
| technical_well | Duplicate measurement label 1 or 2, not another culture |
| input_fraction | Fraction f of original chromatin represented by the input aliquot, as a fraction rather than a percent |
| amplification_factor | Stipulated common per-cycle multiplication A for this amplicon in input, specific IP and IgG; greater than one |
| cq_input | Input aliquot threshold cycle, dimensionless cycle scale |
| cq_specific | Specific-antibody IP threshold cycle |
| cq_igg | Matched IgG threshold cycle |

First average the two Cq values separately for each culture/locus/channel. Under the stated common threshold and constant amplification relation, initial amount is proportional to A^(−Cq). The IP amount divided by the represented input-aliquot amount is therefore A^(mean Cq_input−mean Cq_IP). Multiplying by f converts to fraction of the original input, and multiplying by 100 reports percent input:

**specific percent input = 100f A^(mean Cq_input−mean Cq_specific)**

Use the same transformation for matched IgG. Then calculate specific percent input divided by IgG percent input for fold enrichment over IgG. This fold has a different denominator and scale from percent input. The lesson's ideal doubling expression is recovered at A=2; this candidate explicitly supplies other amplicon factors. Do not silently replace them with 2 or treat amplification factor 1.9 as an exponent of 0.9. Fractions and fold values must retain their defined scales.

The prescribed duplicate-Cq averaging acts on the logarithmic measurement before exponentiation. Averaging independently transformed well percentages is generally different. This packet assesses the declared summary rule; it does not establish an optimal estimator for real noisy data. Culture-level percent input is calculated before averaging the four cultures in a condition. Use only the candidate locus for the summary item. Technical wells and controls do not change that culture count.

This simplified model assumes the represented input fraction is correct, common applicable amplicon efficiency, a consistent threshold/linear range, and compatible sample dilution/recovery. Real analysis needs those quantities checked, antibody validation and preparation controls. Input, IgG, positive locus, negative locus and no-template control have different roles. No-template Cq data are not supplied; contamination clearance is not claimed. Positive/negative loci do not prove direct binding or replace the other controls.

## Reporter data dictionary and analysis contract

Each of the four construct prefixes (promoter, wt, mutant, positive) has columns firefly_au, firefly_background_au, renilla_au and renilla_background_au. Both channels are arbitrary detector units and include their separately listed backgrounds. Calculate for each construct:

**ratio = (firefly_au−firefly_background_au)/(renilla_au−renilla_background_au)**

Then divide each construct's ratio by the promoter-only ratio from the same preparation. This defines the normalized reporter value. Require positive corrected reference and promoter-only denominators; all supplied denominators satisfy this exercise's model. A missing/zero denominator is a limitation to flag, not a fabricated value. Subtracting backgrounds after taking a ratio has a different scale.

Compute the normalized WT-minus-mutant contrast within each preparation before averaging it by condition. The signed group contrast is mean knockdown minus mean control; a relative percent decrease instead divides by the specified control baseline. The composite item asks for relative decrease of group mean WT normalized values, not WT-minus-mutant contrasts.

The construction assumes linear channels and an applicable shared multiplicative loading/recovery factor within a construct. Co-reporter correction is useful only if the reference's biological meaning is not independently altered by treatment. These raw channels intentionally differ by loading, construct and condition; that is not measured proof that biological reference expression is stable. Independent reference, viability, construct identity, DNA amount and cell-state controls remain necessary. Ratios of pooled signal sums or division by another preparation's promoter-only value are different transformations.

This synthetic reporter dataset has matched construct splits and informative controls, but no native-locus edit, endogenous RNA readout or direct biochemical binding assay. Motif disruption can affect overlapping motifs or DNA structure. Restoration toward control strengthens a factor-dependent interpretation in these conditions without proving a direct interaction or the identity of an endogenous target.

## Separate worked illustration

These values are unrelated to the candidate datasets. An input fraction of 0.025, A=2, mean input Cq 24 and mean specific-IP Cq 22 give 100×0.025×2²=10 percent input. If matched IgG gives 0.5 percent input, the specific/IgG enrichment is 20-fold, not 20 percent input.

A reporter channel with firefly 74/background 14 and renilla 35/background 5 has corrected ratio 60/30=2. If its matched promoter-only corrected ratio is 0.5, its normalized reporter value is 4. This arithmetic does not demonstrate native transcriptional causation or direct factor binding.

## Response rules

The standalone percent-input item requires a percent unit and exactly three significant figures. Its absolute tolerance is 0.005 percentage points. A compatible dimensionless fraction unit is converted to percent by the grader, retaining the lexical three-significant-figure requirement. Bare fold enrichment and normalized reporter items require exactly three significant figures with absolute tolerance 0.005 on their declared dimensionless scale. The signed reporter contrast is bare with tolerance 0.005 and no significant-figure rule. Units such as percent must not be appended to a bare fold/contrast response.

The summary CSV uses the exact header/row IDs declared in its item. Counts are exact, means use absolute tolerance 0.005 in each column's declared scale, and cells are bare decimals without unit strings or lexical significant-figure enforcement. Counts refer only to independent ChIP cultures. The reporter summary is separately calculated from the four independent reporter preparations; no pairing between assays is scored or implied. Nine cells carry one proposed point each. Headers, duplicate rows and unknown row IDs can invalidate the upload.

The composite percent decrease requires a percent-compatible unit and exactly three significant figures with tolerance 0.01 percentage points. Its numerical and categorical fields each carry one proposed point. Structured fields are scored as explicit choices, not prose. Multiple-select scoring is stated in the item and penalizes incorrect selections. The choices below are numbered for reading; a future protected UI maps them to its own controls. There is no current submission endpoint for this candidate.

## Draft item packet

### Item 1 — 2 proposed points

For control culture c01 at the candidate locus, average its two technical Cq values separately for input and specific IP. Use the listed input fraction and amplification factor to estimate specific-IP percent input. Report exactly three significant figures with a percent unit.

### Item 2 — 2 proposed points

For control c01 at the candidate locus, divide its specific-IP percent input by its matched IgG percent input, both calculated after technical Cq averaging. Report exactly three significant figures as a bare fold enrichment, not a percent.

### Item 3 — 2 proposed points

For control reporter preparation rc01, subtract each channel's listed background, calculate WT and promoter-only firefly/renilla ratios, then divide WT by the matched promoter-only ratio. Report exactly three significant figures as a bare dimensionless normalized reporter value.

### Item 4 — 2 proposed points

For each reporter preparation subtract backgrounds, normalize WT and mutant ratios to its own promoter-only ratio, then calculate WT minus mutant. Report the mean knockdown contrast minus the mean control contrast as a bare signed difference in normalized reporter units. This is not a relative percent change.

### Item 5 — 9 proposed points

Upload exact columns condition,chip_cultures,mean_specific_pct_input,mean_reporter_motif_contrast with rows control,knockdown,restored. Use the candidate ChIP locus only, averaging technical Cq before percent input and cultures before group means. Independently summarize WT-minus-mutant reporter contrasts after within-preparation normalization. ChIP cultures and reporter preparations are different samples, matched only by condition. Counts are exact; numerical means have absolute tolerance 0.005 in their declared column scales.

### Item 6 — 2 proposed points

Compare the mean WT normalized reporter value in control and knockdown preparations.

**decrease_pct (1 point):** Report the relative decrease from the control mean to the knockdown mean as a percent. Report exactly 3 significant figures.

**inference (1 point):** Which claim is supported by this reporter comparison?

1. It proves that the candidate element directly activates the nearest endogenous gene.

2. It describes reduced activity of this engineered reporter under knockdown; endogenous target identity and direct binding remain untested.

3. It measures the percentage of candidate chromatin occupied by the factor.

### Item 7 — 4 proposed points

Select one response for each distinct assay or endogenous-evidence criterion.

**input (1 point):** What do input and IgG separately address?

1. Input estimates nonspecific antibody pull-down, while IgG measures starting chromatin.

2. Input normalizes the represented starting chromatin; matched IgG estimates nonspecific pull-down.

3. Both measure the number of cells expressing the target gene.

**efficiency (1 point):** Which checks support the Cq transformation and contamination boundary?

1. Matched amplicon efficiency and linear-range checks, plus a separate no-template qPCR control.

2. The positive locus replaces input, IgG and no-template controls.

3. Technical duplicate wells are independent cultures.

**reference (1 point):** When does a co-reporter remove a shared loading/recovery factor?

1. Whenever its signal is nonzero, even if knockdown regulates it independently.

2. Only when reporter DNA is integrated at the native locus.

3. Under linear channels with applicable background correction and a reference whose biological meaning is not independently altered by the perturbation.

**endogenous (1 point):** Which follow-up tests contribution at the proposed endogenous target?

1. Repeat the same plasmid assay with more technical wells only.

2. Use verified independent native-element perturbations and matched neutral controls, measure endogenous/nearby RNA and cell state, and assess rescue.

3. Assign the nearest gene as the target because ChIP enriched the region.

### Item 8 — 2 proposed points

Select all supported statements. Scoring is two points times (correct selections minus incorrect selections) divided by the number of correct options, clamped from zero to two.

1. The regulatory DNA sequence is cis-acting, while the factor whose abundance is reduced acts in trans.

2. Cross-linked ChIP enrichment proves direct base-specific binding by the recovered factor.

3. More technical qPCR wells establish more independent biological cultures.

4. A motif change can alter overlapping motifs or DNA structure; reporter evidence alone does not identify the native target gene.

5. Similar positive-locus recovery proves that the reference reporter is unaffected by knockdown.

## Unscored written discussion and draft reviewer guide

Explain the two assay denominators, preserve biological units, and identify one control for each untested causal link. Describe a native-element perturbation with independent edits/guides, neutral controls, target and nearby RNA readouts, verification, cell-state/viability checks and a suitable restoration experiment. Discuss why co-reporter stability, PCR efficiency and antibody specificity cannot be concluded from the numerical summary alone.

For discussion only, reviewers may use absent/partial/adequate descriptors for denominator correctness, biological replication, control specificity and causal boundaries. Adequate work names the measured quantity, its assumptions, an alternative explanation and a matched test. These descriptors are an unscored draft; scripts, explanations, plots, uncertainty and experimental design are not graded by this item packet. Fairness, workload and manual accessibility have not been evaluated.

## Provenance and activation requirements

Original instructions, stems and synthetic observations: CC BY 4.0, developed with substantial Codex assistance. Existing original lessons supply scientific context; no outside text, problem, table, figure, identifier or dataset was copied or adapted. No new citation-resolution pass is claimed. This is a paper/data exercise, not a wet-lab protocol, an actual experiment or a clinical claim.

The key and candidate-specific checks remain outside Git. Public metadata binds key and prerequisite-reading hashes; it contains answer-free DTOs. Local artifacts and temporary protected-API fixtures are development evidence, not production provisioning approval. The internal intended assessment role does not activate coursework. Earlier candidates retain their authored versions and key bindings.

Independent recalculation, qualified subject and assessment review, grader-mutation review, manual accessibility/fairness review, measured workload and operator provisioning/release decisions remain absent. Passing same-AI checks cannot satisfy these gates. All four candidates remain inactive.

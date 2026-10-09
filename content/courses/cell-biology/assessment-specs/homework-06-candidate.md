# Homework 6 candidate: nested clone evidence and genotype probabilities

**State:** inactive candidate for review, authored with substantial Codex assistance for Biology 0.25.0. The course remains partial, unreviewed and formative-only. This packet is not in the Practice gradebook, contributes no course grade and has no live submission route. Independent review is missing and workload has not been measured. No deadline, time limit, attempt or release policy is set. Keys and candidate-specific tests remain outside Git.

Read [Inheritance, penetrance and pedigree evidence](../modules/09a-inheritance-penetrance-and-pedigree-evidence.md) and [Variant mechanism and isogenic evidence](../modules/09b-variant-mechanism-and-isogenic-evidence.md). Open Homework 6 remains public practice. This separate candidate has new synthetic clone data and item stems. Its probability example concerns a fictional fluorescence-defined trait, not clinical risk, genetic counselling or diagnosis.

## Construction and independent units

The [clone/culture table](homework-06-candidate-clones.csv) has reference, knockin and corrected groups, each with four separately derived clones. Each clone supplies two independently cultured replicates:24 culture rows nested in 12 clones. Names q01–q04,v01–v04,z01–z04 designate distinct clones; suffix a/b denotes a repeated culture of that clone. Numerals across groups do not imply paired clone ancestry or a paired design. The stipulated intended genotype is a construction label, not supplied sequence validation. Actual independent derivation, intended/off-target/copy-number confirmation, background matching and clone-selection controls would be needed for real evidence.

Count independent clones for the requested group summary, not cultures, cells or assay channels. The two cultures estimate within-clone variation and do not create two independent edited genotypes. Clones share a parental background, so they do not represent randomly sampled organisms or unrelated donors. This synthetic nested design has equal culture counts per clone; treating cultures as equally weighted can coincide with equal clone means for some quantities. Correct scored values cannot certify the implemented hierarchy; methods and uncertainty remain ungraded.

Every value is deterministic teaching data, not a physical experiment. No assay calibration, uncertainty distribution, sequence-verification dataset or workload pilot was measured. All inference is limited to the stated construction. A correction toward reference supports reversibility under controls, not proof of a specific molecular route or organismal phenotype.

## Data dictionary

| Column | Meaning |
|---|---|
| condition,clone,culture | Group, separately derived clone and its repeated culture |
| viable_cells_thousands | Viable-cell count represented by the protein/activity preparation in thousands |
| recovery_fraction | Stipulated common represented recovery fraction, positive and at most one |
| protein_signal_ug,protein_background_ug | Protein mass assay signal and its matched background, micrograms |
| activity_signal_nmol_min,activity_background_nmol_min | Product-formation rate assay signal and background,nmol/min |
| response_positive_cells,response_cells_assayed | Cells above a prespecified synthetic response threshold and total viable cells counted in a separate matched readout |

Protein and activity scales are stipulated calibration units. The count assay measures a threshold-positive fraction, not tissue function or a molecular pathway. A counted cell is sampled within a culture; repeated cells are not independent edited clones. Total assayed cells are a different denominator from the whole represented protein preparation's viable count.

## Analysis contract

For each culture subtract the matched protein and activity backgrounds. Correct protein mass by recovery_fraction, then divide by viable_cells_thousands to report µg per1,000 viable cells. Protein-specific activity is corrected activity divided by corrected protein; common recovery cancels only under the declared applicable shared-factor model. Its scale is nmol min⁻¹ µg⁻¹. It is distinct from total activity per culture or activity per viable cell. Both assays must be linear and compatible, the protein denominator must be positive and appropriately specific, and the activity interval must be applicable. Those requirements are assumptions here, not measured real-assay validation.

Calculate these ratios per culture before averaging its two cultures into a clone summary. Then average four clone summaries with equal clone weight. Do not pool raw activity/protein/cell sums. Pooling weights preparations by their amounts and can mix culture differences with the genotype comparison. Background subtraction must precede division. All supplied denominators are positive; flag unavailable/near-limit denominators rather than inventing values.

The composite compares equal-clone mean protein amounts between knockin and reference as a percent. It asks a ratio of the two declared group means, not an average of invented cross-group clone pairings. Similar specific activity with lower protein per cell can fit an abundance contribution to reduced total activity. It does not distinguish synthesis, folding, degradation, localization, assay interference or clonal effects. An orthogonal pulse/chase or localization experiment addresses one link, not every hidden step.

## Separate inheritance model

The fictional A/a × a/a example stipulates ordinary Mendelian segregation, applicable observation conditions, a defined fluorescence threshold and conditional probabilities for both genotype classes. Use the law of total probability: sum each genotype's transmission probability times its threshold-positive probability. Transmission and phenotype probability are different. A noncarrier branch cannot be set to zero when a nonzero value is given. The model has no clinical meaning or penetrance estimate for people.

An observed pedigree fraction depends on genotype confirmation, trait definition, age, recruitment and shared ancestry/environment. Dominance compares genotype phenotypes under stated conditions; it does not specify frequency or a universal biochemical mechanism. Penetrance concerns whether a defined phenotype appears, whereas expressivity concerns its form or degree among those expressing it. Family referral and linked ancestry can affect association without establishing the tested base as a molecular cause.

## Separate worked illustration

Unrelated data: protein signal2.3µg/background0.3 gives2.0µg, with recovery0.5 and viable count40thousand. Recovery-corrected amount is2/0.5/40=0.10µg per1,000 cells. Activity signal17/background1 gives16nmol/min, so specific activity is16/2=8nmol min⁻¹ µg⁻¹ under common recovery. That does not identify protein removal as the cause of a lower amount.

For an unrelated fictional trait with carrier transmission0.25, carrier threshold probability0.40 and noncarrier probability0.20, the total is0.25×0.40+0.75×0.20=0.25. This illustrates conditional branches, not patient risk.

## Response and discussion rules

Eight machine-scored draft items total25 proposed points. Bare protein values use the declared µg-per1,000-cells scale and absolute tolerance 0.000005; bare specific activity uses its stated scale with tolerance 0.005. Both require exactly three significant figures, with no textual unit conversion enforced for these bare scales. Percent responses require compatible units and three significant figures: standalone tolerance 0.005 percentage points; composite tolerance 0.01. CSV cells are bare decimals with the stated column tolerances, exact clone counts and no lexical significant-figure enforcement. Nine cells carry one point each. Numeric/categorical composite fields each carry one point; structured fields score choices, and multiple-select scoring is in the stem. All written methods, nested uncertainty, plots, scripts, mechanism arguments and study design are ungraded.

For unscored discussion, distinguish sampling levels, denominators, transmission and phenotype, and identify a targeted follow-up with clone/edit/recovery/state controls. Draft adequate-work descriptors require a named measurement, unit, alternative and matched test; they are an unscored guide rather than qualified rubric review. No clinician or subject/assessment/accessibility reviewer approved this packet.

## Item packet

### Item 1 — 2 proposed points

For knockin culture v01a, subtract activity and protein backgrounds and divide corrected activity by corrected protein. Report exactly three significant figures as a bare number on the declared nmol min⁻¹ µg⁻¹ scale. This is not activity per cell.

### Item 2 — 2 proposed points

For knockin v01a, subtract protein background, correct by recovery_fraction, and divide by viable_cells_thousands. Report exactly three significant figures as a bare µg-per-1,000-viable-cells value.

### Item 3 — 2 proposed points

For knockin v01a, report response_positive_cells/response_cells_assayed as a percent with exactly three significant figures. Counted cells are within a culture, not independent clones.

### Item 4 — 2 proposed points

In a separate fictional nonclinical trait model, A/a × a/a has ordinary Mendelian transmission with no distortion. Probability of meeting a prespecified fluorescence threshold by the stated age is0.60 for A/a and0.10 for a/a. Report the unconditional threshold-positive probability per offspring as a percent with three significant figures; include both genotype branches.

### Item 5 — 9 proposed points

Upload exact columns condition,clones,mean_protein_ug_per_1000_cells,mean_specific_activity with rows reference,knockin,corrected. Compute corrected per-cell protein and protein-specific activity per culture, average the two cultures within each clone, then give equal weight to the four clone summaries. Counts are exact; protein means have tolerance0.000005 on the µg-per-1,000-cells scale, specific-activity means tolerance0.005 on nmol min⁻¹ µg⁻¹ scale.

### Item 6 — 2 proposed points

Use the equal-clone condition summaries of recovery-corrected protein per1,000 viable cells.

**protein_pct (1 point):** Report knockin mean protein divided by reference mean protein as a percent. Report exactly 3 significant figures.

**inference (1 point):** What does lower protein amount with similar protein-normalized activity support?

1. It uniquely identifies accelerated proteasomal degradation caused directly by the variant.

2. It is consistent with less measured protein contributing to lower total activity; synthesis, removal, localization, clone effects and assay validity still need tests.

3. It proves a clinical phenotype and a penetrance estimate in people.

### Item 7 — 4 proposed points

Select one response for each inheritance or clone-evidence criterion.

**pedigree (1 point):** What is needed before interpreting a referred family's observed carrier fraction as penetrance?

1. The allele must be molecularly dominant in every tissue.

2. A defined trait/age, confirmed genotypes, inclusion independent of outcome where possible, and attention to shared ancestry/environment and ascertainment.

3. One affected carrier defines penetrance for all future offspring.

**clone (1 point):** Which design strengthens the edited-cell comparison?

1. Independent derivations, mock edits, sequence/copy-number checks, matched culture state and reciprocal introduction/correction.

2. More assay wells from one selected clone only.

3. Assume every corrected clone is identical because its intended base was changed.

**mechanism (1 point):** Which measurements help separate synthesis from removal?

1. An allele annotation alone gives a degradation constant.

2. Protein amount alone uniquely identifies catalytic loss.

3. Matched nascent-protein and multi-time chase with assay/recovery/state controls and appropriate references.

**association (1 point):** What can explain a genotype–trait association without direct action by the tested base?

1. All measured associations are necessarily causal.

2. Linkage, ancestry/recruitment, environment and measurement selection can alter the association; functional and replicated designs address different alternatives.

3. Dominance means the allele is common.

### Item 8 — 2 proposed points

Select all supported statements. Scoring is two points times (correct selections minus incorrect selections) divided by the number of correct options, clamped from zero to two.

1. Dominance compares heterozygote phenotype with homozygotes for a stated trait; it does not specify allele frequency or a universal biochemical mechanism.

2. Four offspring of A/a × A/a must contain exactly one A/A, two A/a and one a/a.

3. A synonymous annotation proves no possible RNA or context-dependent effect.

4. Penetrance describes a conditional probability under defined observation conditions; expressivity describes how the phenotype appears among those expressing it.

5. A cell-assay change establishes pathogenicity without organism-level evidence.

## Provenance and activation

Original packet and constructed observations: CC BY 4.0 with substantial Codex assistance. Existing original lessons supply context; no outside source, prose, problem, figure,dataset or identifier was imported and no new citation-resolution pass is claimed. This is a paper/data exercise, not a wet-lab protocol, clinical interpretation or result. Public DTOs bind the external key and prerequisite-reading hashes; earlier candidates retain their authored files, versions and bindings. Local artifacts and temporary delivery tests do not approve deployment. Independent recalculation, grader-mutation/subject/assessment/manual accessibility review, measured workload and operator provisioning/release remain absent. All six candidates remain inactive.

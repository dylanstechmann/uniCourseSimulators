# Homework 5 candidate: RNA composition and protein-cohort loss

**State:** inactive candidate for review, authored with substantial Codex assistance for Biology 0.24.0. The course is partial, unreviewed and formative-only. This packet contributes no course grade, is absent from the Practice gradebook and has no live submission route. Keys remain outside Git. Independent numerical, scientific, assessment and accessibility review is missing; workload has not been measured. No deadline, time limit, attempt policy or release approval is set.

Read [RNA processing and isoform evidence](../modules/08a-rna-processing-and-isoform-evidence.md) and [Translation and protein turnover](../modules/08b-translation-and-protein-turnover.md). The open Homework 5 companion remains public practice. This separate packet uses new stems and constructed observations rather than relabeling practice answers as confidential.

## Observation units and construction

The [baseline table](homework-05-candidate-baseline.csv) contains four independently cultured preparations in each of control, depleted and restored conditions. IDs c01–c04, d01–d04 and r01–r04 denote different cultures. Baseline RNA, short-pulse target labeling and protein channels are matched aliquots from that culture. The [chase table](homework-05-candidate-chase.csv) supplies matched labeled-cohort aliquots at 0,2,4,6 hours: 48 rows. Times, aliquots and assay channels do not add independent cultures. Culture IDs with the same numeral in different conditions are not a paired biological design. One engineered line per condition does not measure independent-clone variation.

All values are deterministic synthetic observations, not a physical experiment. Recovery standards, assay linearity and background values are stipulated; no calibration, uncertainty distribution or workload pilot was measured. Labeling/recovery differences do not automatically mean biological synthesis changed. Restoration toward control can constrain involvement without identifying a direct molecular action.

## Baseline dictionary and RNA analysis

condition and culture identify the preparation; viable_cells_thousands is viable-cell count in thousands. rna_spike_input_eq and rna_spike_recovered_eq are added/recovered quantities of an external RNA standard in assay-equivalent units. For included, skipped, shared and precursor channels, signal_eq includes the matched background_eq. Those values are calibrated copy-equivalent signals within this exercise, not sequencing reads or literal absolute molecules in a real sample. Included and skipped are stipulated mutually exclusive, exhaustive forms of the measured mature pool; precursor is an intron-containing proxy, not a transcription-rate meter.

For each culture let recovery = recovered spike / input spike. Correct an RNA channel by subtracting its own background and dividing by this recovery. Then divide by viable_cells_thousands to express copy-equivalent signal per 1,000 viable cells. This assumes the spike and target share the relevant recovery factor; an external spike does not validate every reverse-transcription bias, isoform efficiency or biological denominator.

Skipped percent = 100 × corrected skipped / (corrected included + corrected skipped). Compute that ratio per culture before averaging. Shared signal is a separate assay and should not be substituted without checking its coverage and calibration. In this particular construction it equals the sum of the two forms, so some alternative denominators coincide numerically; correct scored values alone cannot certify the implemented method. The denominator concerns this measured mature pool, not every transcript in the cell.

An unchanged shared or precursor proxy cannot prove unchanged transcription and decay. Effective production, processing, export, stability, cell state and recovery can all influence abundance. No-RT, junction specificity and independent transcript measurements are needed for an RNA claim; no-RT observations are not supplied here, so contamination clearance is not claimed.

## Baseline protein channels

nascent_signal_au/protein_signal_au include their separately listed background_au values. Their respective reference_au channels are positive stipulated recovery/loading references with zero background already removed. Subtract target background before dividing by its matching reference. The construction gives target and reference a shared loading/recovery factor with linear channels and stable reference meaning; this is an assumption, not measured validation. Reference ratios and RNA copy-equivalent values have different scales and cannot be subtracted as though they shared units.

The short-pulse nascent ratio is a labeling proxy, not a directly calibrated synthesis rate or a measurement of initiation alone. Uptake, precursor pools, processing, elongation, target recovery and cell state remain alternatives. The standalone ratio compares two named cultures descriptively; it is not a population effect estimate. Total target-protein abundance does not identify function or a degradation route.

## Labeled-cohort chase

time_h is hours after the chase begins. labeled_target_signal_au includes its matched labeled_target_background_au; recovery_reference_au is a positive zero-background external reference for that aliquot. Its amplitude changes with loading/recovery. Calculate R_t=(signal_t−background_t)/reference_t, then f_t=R_t/R_0 for the same culture. The requested two-point first-order estimate is k=−ln(f_4)/4 h and t_half=ln(2)/k. Require 0<f_4<1, positive references and nonzero initial corrected signal; flag unavailable denominators rather than inventing values. All supplied denominators satisfy the model.

This tracks a labeled target cohort, not a synthesis-block measurement of all protein. Interpretation assumes negligible new labeled input/recycling, stable sampled population, applicable reference correction and an approximately first-order regime. Population growth, selection, tag cleavage or differential recovery can violate that interpretation. Decline alone does not identify proteasomal versus lysosomal removal. Additional 2/6-hour observations support a model-consistency check but cannot establish its biological assumptions or generality; no uncertainty or mechanism was measured.

Estimate half-life per culture before averaging the four estimates. A half-life calculated from the group's mean remaining fraction is generally different because the transformation is nonlinear. Repeated time points do not multiply culture counts. Baseline and chase scales are assay-specific; neither RNA fractions nor viability substitute for the chase recovery reference.

## Separate model and worked illustration

The composite item stipulates constant synthesis s and first-order loss k with P_ss=s/k at a true steady state. Relative synthesis and loss-rate factors enter the numerator and denominator respectively. These hypothetical factors are not inferred by treating short-pulse fluorescence as an exact synthesis rate.

For an unrelated example, included signal 38/background 8 and skipped 22/background 2 give 30 and 20 corrected units; skipped fraction is 20/(30+20)=40 percent. If a separate shared channel is 103/background 3, recovery is0.5 and viable count is20 thousand, corrected per-cell signal is(103−3)/0.5/20=10 copy-equivalents per1,000 cells. If an unrelated normalized labeled-cohort fraction is0.25 at6h, k=ln(4)/6 and the half-life is3h. None of these calculations determines a direct molecular mechanism.

## Response and discussion rules

Standalone numeric items require exactly three significant figures. Percent and half-life items require compatible units, with absolute tolerance 0.005 in percent-point/hour scales; bare shared and nascent values use their declared scale with tolerance 0.005. CSV cells are bare decimals: exact culture counts, means with tolerance 0.005 in column scales, no lexical significant-figure enforcement. Use the exact header and row IDs in the item. The nine cells carry one proposed point each. Numeric and categorical composite fields each carry one point; its percent response requires three significant figures and tolerance 0.005 percentage points. Structured fields score explicit choices only; multiple-select scoring is stated in the stem. Written methods, plots, scripts, uncertainty and causal reasoning are ungraded.

For unscored discussion, explain normalization assumptions, RNA composition versus production/stability, label-proxy alternatives, per-culture kinetics and a targeted follow-up with assay controls/independent perturbations/restoration. Draft adequate-work descriptors require naming the measurement, denominator, alternative and a matched test. These are an unscored reviewer guide, not a validated analytic rubric or a human project grade.

## Item packet

### Item 1 — 2 proposed points

For control c01, subtract included and skipped assay backgrounds and use the two measured mutually exclusive mature forms as the denominator. Report skipped-isoform percent with exactly three significant figures and a percent unit.

### Item 2 — 2 proposed points

For control c02, subtract the shared-assay background, divide by recovered/input RNA-spike fraction, then divide by viable_cells_thousands. Report exactly three significant figures as a bare shared-region copy-equivalent value per 1,000 viable cells.

### Item 3 — 2 proposed points

Compute each culture's background-corrected nascent signal divided by nascent_reference_au. Report depleted d01 divided by control c01 as a bare dimensionless ratio with exactly three significant figures. This compares two specified cultures, not a group effect estimate or an initiation rate.

### Item 4 — 2 proposed points

For control c01, correct the labeled-target chase background and divide by its matched recovery reference at each time. Normalize its 4-hour corrected ratio to its time-zero ratio. Under the stated first-order labeled-cohort loss model, report half-life in hours with exactly three significant figures.

### Item 5 — 9 proposed points

Upload exact columns condition,cultures,mean_skipped_pct,mean_half_life_h with rows control,depleted,restored. Calculate RNA fraction per culture before averaging. Calculate each culture's half-life from its normalized 0-to-4-hour chase before averaging half-lives. Repeated times/channels do not add independent cultures. Counts are exact; means have tolerance 0.005 in the declared percent or hour column scale.

### Item 6 — 2 proposed points

Use a separate hypothetical constant-rate model P_ss=s/k, not a calibration of the pulse-label assay. New synthesis is 0.50 times its original rate and the loss constant is 1.25 times its original value.

**new_abundance_pct (1 point):** Report the new steady-state abundance as a percent of the original. Report exactly 3 significant figures.

**inference (1 point):** What is needed before applying this model prediction to observed protein abundance?

1. Unchanged total mRNA alone proves the protein pool has reached its new steady state.

2. Applicable constant synthesis/loss rates, a compatible measured protein pool, and evidence the new steady state was reached; the pulse-label proxy alone does not supply all those facts.

3. The measured skipped-isoform fraction is the protein degradation constant.

### Item 7 — 4 proposed points

Select one response for each independent RNA or turnover criterion.

**rna (1 point):** What does unchanged shared-region signal with altered junction proportions support?

1. Proof that transcription and RNA decay are both unchanged.

2. A change in the measured isoform composition; production, processing and stability need separate measurements.

3. Proof that every transcript in the cell uses the skipped junction.

**rt (1 point):** Which matched control addresses genomic-DNA contamination in an RT-dependent RNA assay?

1. A no-reverse-transcriptase control with suitable junction/amplicon checks.

2. Extra wells from the same reverse-transcription sample only.

3. An unchanged protein signal without an RNA control.

**chase (1 point):** What is required to interpret normalized chase loss as first-order protein turnover?

1. Any drop in raw signal proves proteasomal degradation.

2. A stable total RNA signal replaces recovery and label-recycling controls.

3. Applicable reference/recovery, negligible new labeled input or recycling, stable sampled population and a suitable first-order regime.

**rescue (1 point):** What does movement toward control after factor restoration establish?

1. Direct binding of that factor to every target RNA and a specific initiation step.

2. Evidence consistent with factor involvement here, while indirect pathways, state shifts and assay biases remain alternatives.

3. A measured change in therapeutic function.

### Item 8 — 2 proposed points

Select all supported statements. Scoring is two points times (correct selections minus incorrect selections) divided by the number of correct options, clamped from zero to two.

1. The ribosome reads mRNA 5′ to 3′ and the polypeptide grows from its amino terminus toward its carboxyl terminus.

2. A common 5′ cap guarantees completion, correct splicing and a fixed translation rate.

3. Every eukaryotic protein-coding transcript necessarily has the same poly(A) tail and processing route.

4. Changing splice junctions or 3′ processing can alter RNA fate without proving a new functional protein was produced.

5. A fall in labeled-cohort signal uniquely identifies the proteasome as the removal route.

## Provenance and missing activation evidence

Original packet and synthetic observations: CC BY 4.0 with substantial Codex assistance. Existing original lessons supply context; no outside prose, problem, figure, dataset or identifier was imported and no new identifier-resolution pass is claimed. This is a paper/data exercise, not a wet-lab protocol or clinical result. Public DTOs bind external-key and prerequisite-reading hashes; earlier candidates retain their versions and bindings. Local artifacts and temporary protected-delivery fixtures do not establish production provisioning approval. Independent recalculation, grader-mutation/subject/assessment/manual accessibility/fairness review, measured workload and operator release decisions remain missing. All five candidates are inactive.

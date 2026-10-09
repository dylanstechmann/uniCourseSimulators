# Homework 3 candidate: lesion normalization, replication and repair evidence

**State:** inactive candidate for review, developed with substantial Codex assistance. It is not available as graded coursework and contributes no course grade. No qualified scientific, assessment or accessibility reviewer has approved it. Authored course package: 0.22.0, partial, unreviewed and formative-only.

## Preparation and purpose

Read [DNA structure and semiconservative replication](../modules/06a-dna-structure-and-replication.md) and [DNA damage and repair evidence](../modules/06b-dna-damage-and-repair-evidence.md). Open Homework 3 remains available for practice. This separate candidate uses a new dataset and new questions; existing public practice keys are not being relabeled as confidential material.

The task separates four quantities: a detector signal, a signal relative to a DNA-reference channel, a viable-cell count and a copying-model prediction. A decline in a lesion-associated signal is not itself a measured repair flux, mutation frequency or proof of error-free sequence restoration. Controls should address a named alternative and retain their own limits.

Eight proposed machine-scored items total 25 points. The allocation is a review draft, not a course-grade policy. Written discussion is unscored. No actual deadline, time limit or attempt policy is selected, and workload has not been measured. The candidate is not listed in the Practice gradebook and has no live submission route. Independent and qualified review, workload and operator release requirements remain unmet.

## Experimental construction and units of observation

The [synthetic table](homework-03-candidate-lesion-reference.csv) contains three conditions: wt, factor_depleted and factor_restored. Each has four independently cultured preparations, identified by w01–w04, d01–d04 or r01–r04. Each culture supplies matched aliquots at 0, 2 and 6 hours, for 36 rows. Aliquots, assay channels and time observations are repeated or matched measurements within a culture, not new independent cultures. A single engineered/restored line per condition does not estimate variability across independent clones.

A lesion-associated detector channel, a matched lesion-background channel and a DNA-reference channel are recorded for each aliquot. The reference represents a stipulated stable genomic-DNA measurement with zero background already removed. Loaded DNA amount and technical recovery differ across aliquots; that means raw detector amplitudes should not be compared as though DNA loading were identical. Loaded DNA is material placed in the assay, not total DNA produced by the culture and not a count of completed genome doublings.

The construction stipulates linear channels, a positive reference and a shared multiplicative loading/recovery factor for corrected lesion and reference signals. Under those assumptions their ratio removes that common factor. This is not a measured calibration or a universal correction for real assays. A lesion-specific assay and a reference assay can respond differently to extraction, DNA fragmentation or matrix changes. Those possibilities need independent controls before the same transformation is used to support real biological claims.

All signals, counts, labels and time differences are deterministic teaching values. No physical experiment, sampling distribution, technical-error model or calibration uncertainty was measured. The background is independently stated as a synthetic matched control; it must be subtracted before the ratio is calculated. The data include no measured mutation assay, excision product, direct catalytic interaction or repair-synthesis flux.

## Data dictionary

| Column | Meaning and scale |
|---|---|
| condition | wt, factor_depleted or factor_restored |
| culture | Independently cultured preparation identifier, repeated across its three time observations |
| time_h | Hours after the stipulated starting observation: 0, 2 or 6 |
| loaded_dna_ng | Nanograms of DNA loaded in that aliquot's assay; not whole-culture DNA production |
| lesion_signal_au | Lesion-associated channel in arbitrary detector units, including the listed background |
| lesion_background_au | Matched background for the lesion channel, arbitrary units |
| dna_reference_au | Positive reference channel in arbitrary units, with its background already removed |
| viable_cells_thousands | Viable-cell count for that culture in thousands; a different denominator from assay DNA loading |
| dna_synthesis_label_pct | Percentage of sampled cells positive for the stipulated DNA-synthesis label |

A synthesis-label fraction is a measured proxy. It does not specify how much of each genome was duplicated, how many complete generations elapsed or exactly how much a lesion signal was diluted by newly synthesized DNA. Similar label fractions can constrain one alternative without proving identical replication histories. Viable-cell counts likewise do not reveal the lesion burden of cells lost from the sampled population.

## Analysis contract

For a culture at time t, calculate R_t=(lesion_signal_t−lesion_background_t)/dna_reference_t. The specified remaining percentage is 100R_t/R_0 for that same culture. Require a positive reference and a nonzero time-zero corrected ratio before dividing; an unavailable denominator is a limitation, not a value to fabricate. All denominators in this synthetic file are valid under the declared model. Subtracting a background after forming a ratio has a different scale and is not the stated transformation.

At 6 hours calculate one remaining percentage per culture, then average the four culture-level percentages within each condition. Preserve culture pairing to its own time-zero reference. Do not pool raw channel sums or average all three time points before normalization. The upload also asks for the culture count and mean synthesis-label percentage at that endpoint; different channels do not multiply the culture count.

The condition contrast is a signed percentage-point difference between group means. A relative change would divide by a specified group baseline and answers a different question. No p-value, interval or population effect is requested or supplied. The viable-cell fraction item uses that culture's 6-hour count divided by its time-zero count; it is not an adjustment factor that reconstructs lesion burden in dead or detached cells.

## Separate worked illustration

These values are unrelated to the candidate table. Suppose a time-zero lesion channel is 27 a.u., background is 7 a.u. and DNA reference is 100 a.u. The corrected ratio is (27−7)/100=0.20. At a later time, lesion channel 15, background 7 and reference 80 give (15−7)/80=0.10. Relative to the matched starting ratio, 100×0.10/0.20=50 percent remains. Comparing raw lesion channels alone would mix background and reference differences. This arithmetic does not identify a repair mechanism or a mutation rate.

## Separate ideal copying model

The density-label items are not derived from the culture time course. They stipulate 64 fully heavy-labeled duplexes before a switch to exclusively light medium, three synchronized complete doublings, no molecule loss, no replacement of parental heavy strands by repair and no new heavy isotope. Under semiconservative copying each daughter duplex contains one strand from its parent and one newly synthesized light strand. Track the parental heavy strands separately from the total duplex count. Count molecules, rather than weighting band signal by an unspecified detector response.

A real density comparison needs controlled generations, appropriate heavy/light markers, recovery of each density class and adequate resolution. An intermediate class after one generation is interpreted against alternative copying models, not as a measurement of lesion repair in the other dataset. The stipulated synchronous doublings and the observed DNA-synthesis-label fraction are different kinds of information and must not be substituted for one another.

## Response rules

Remaining-signal and viable-cell numeric items require percent units and exactly three significant figures. The condition contrast requests a bare signed value in percentage points. The parental-strand count is an exact bare count, with no significant-figure rule. The composite percentage item requires percent units and exactly two significant figures. These declared numeric scales are not all the same quantity.

Upload a small UTF-8 CSV with exact columns condition,cultures,mean_remaining_pct,mean_synthesis_label_pct and one unique row per condition. Use plain values on the percentage scale without percent symbols in cells. Counts are exact; means have the stated tolerance. Formulas and code are not executed. The nine numeric cells do not assess significant figures, uncertainty, analysis scripts or written reasoning. Each structured field receives one point independently. Multiple-select scoring follows the stated correct-minus-incorrect rule; selected categorical choices do not constitute a graded written mechanism explanation.

## Item stems and proposed allocation

### Item 1 — 2 proposed points

For wt culture w01 at 6 h, subtract its measured lesion background, divide by its DNA-reference channel, then divide by the same culture's time-zero corrected lesion/reference ratio. Express remaining signal as a percent with exactly three significant figures.

### Item 2 — 2 proposed points

At 6 h normalize each culture to its own time-zero corrected lesion/reference ratio. Report mean factor_depleted percentage minus mean wt percentage as a bare signed number in percentage points, not a relative percent change.

### Item 3 — 2 proposed points

For wt w01, report viable-cell count at 6 h divided by its time-zero viable-cell count as a percent with exactly three significant figures. This is a cell-count fraction, not a correction factor for lesion burden.

### Item 4 — 2 proposed points

In a separate ideal semiconservative model, start with 64 fully heavy-labeled DNA duplexes. Complete three synchronized doublings in exclusively light medium, with no molecule loss, repair replacement or new heavy isotope. How many final duplexes contain a parental heavy strand? Report an exact bare count, not a percentage.

### Item 5 — 9 proposed points

At 6 h calculate remaining lesion/reference percent for each matched culture before averaging. Upload exact columns condition,cultures,mean_remaining_pct,mean_synthesis_label_pct with rows wt,factor_depleted,factor_restored. Counts are exact; means have tolerance 0.005 percentage points. Time points, assay channels and technical DNA loading do not add independent cultures.

### Item 6 — 2 proposed points

Use the separately stipulated 64-duplex, three-generation ideal semiconservative copying model.

**hybrid_pct (1 point):** Report the percentage of final duplexes with one heavy and one light strand. Report exactly 2 significant figures.

**inference (1 point):** What does a single intermediate-density class after only one generation distinguish?

1. It uniquely proves semiconservative copying and excludes dispersive copying.

2. It is compatible with both semiconservative and dispersive predictions; a later controlled generation and density calibration are needed.

3. It directly measures error-free lesion repair in the culture dataset.

### Item 7 — 4 proposed points

Select one response for each independent normalization, replication, selection and restoration criterion.

**reference (1 point):** What must hold for the specified normalization?

1. A positive reference and matched background with stable reference meaning and an applicable linear assay relation.

2. The largest raw lesion signal must be the denominator for all cultures.

3. The viability percentage substitutes for the DNA-reference channel.

**synthesis (1 point):** What does a similar synthesis-label fraction establish?

1. Exactly the same number of completed genome doublings.

2. A constraint on this measured label fraction, not a complete measurement of genome duplication or lesion dilution.

3. Proof that replication cannot affect lesion/reference signal.

**selection (1 point):** How can cell loss affect interpretation?

1. Every reduction in cell count proves correct repair.

2. Dividing remaining lesion percent by viable-cell fraction identifies lesion removal.

3. Loss of highly damaged cells can change the sampled population; counts alone do not reconstruct their lesion burden.

**restoration (1 point):** What does a restored condition nearer wt add?

1. Proof of direct catalytic removal by that factor in every cell type.

2. Evidence consistent with a factor-dependent contribution under these conditions; expression, independent lines and assay controls still matter.

3. A measured mutation rate for the restored line.

### Item 8 — 2 proposed points

Select all statements compatible with strand polarity and the lesson's distinctions between copying, repair and bypass. Scoring is two points times (correct selections minus incorrect selections) divided by the total number of correct options, clamped from zero to two.

1. For template 3′-G A T C C A-5′, the antiparallel complementary product is 5′-C T A G G T-3′.

2. Each lagging-strand fragment grows 3′ to 5′.

3. Translesion synthesis necessarily removes the original lesion and restores the original sequence.

4. Post-replicative mismatch repair differs from proofreading at an extending polymerase.

5. A lower lesion-associated signal is itself a measurement of mutation frequency.

## Written discussion for a future human reviewer

Explain how raw and reference-normalized signals answer different questions, naming the assumptions that allow the ratio. Discuss at least two explanations for a changing lesion-associated signal besides direct error-free removal. Use the synthesis-label, viable-cell and restored-factor information to constrain those explanations while stating what each control leaves unresolved. Propose an orthogonal lesion measurement and a separate sequence-outcome measurement, and explain which competing predictions they address. Keep the density-copying model separate from the culture time-course interpretation.

Draft discussion descriptors distinguish absent or incompatible reasoning, partly correct reasoning with a material omission, and coherent reasoning with explicit units, controls and bounded conclusions. Criteria cover matched normalization, culture-level replication, proxy versus direct measurement, survivor selection, restoration scope and a discriminating follow-up. These are unscored descriptors, not automated prose grading or released grade weights. No written response has been assessed by a human or AI grader.

## Provenance, accessibility and readiness

Instructions, stems and synthetic observations are original CC BY 4.0 work with substantial AI assistance, based on the existing original course lessons. No new outside source, paper identifier, third-party data, prose, problem or figure was introduced. All essential observations are textual with explicit units. No color discrimination, image inspection or timed interaction is required. Manual accessibility, screen-reader and fairness review remain missing; these design choices do not establish that those checks passed.

The private answer file remains outside Git, while public stems and data are independently solvable; key separation does not guarantee assessment security. Independent numerical review, qualified scientific and assessment review, measured workload and operator provisioning/release decisions remain outstanding. No physical measurement, unique repair pathway, mutation-free genome, therapeutic utility or clinical safety was established. The candidate remains inactive.

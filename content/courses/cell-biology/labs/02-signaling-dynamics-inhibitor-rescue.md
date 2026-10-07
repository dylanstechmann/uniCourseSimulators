# Virtual lab 2: signaling dynamics, inhibitor controls, and rescue

**Activity type:** synthetic-data analysis with public, ungraded formative checks  
**Course package:** Foundations of Cell and Molecular Biology, version 0.18.0. **Estimated learner time:** 2–3 hours  
**Data status:** all 120 observations are constructed for instruction; no laboratory measurements or biological samples are represented.

## Experimental question

Does a short ligand pulse produce the same ERK phosphorylation trajectory as continued ligand exposure? How does a MEK-pathway inhibitor change the measured signal, and what does a downstream active-MEK bypass rescue establish when an upstream receptor inhibitor is present?

The activity separates three questions that are often collapsed into one: what time-dependent biochemical signal was measured, what perturbation pattern is consistent with a pathway relation, and what later cell behavior would require a distinct assay. No cell-fate or therapeutic outcome is included in this dataset.

## Learning objectives

By completing the activity, learners should be able to:

1. Calculate preparation-level summaries at named times and graph the time-ordered mean signal without treating wells, cells, or time points as independent preparations.
2. Compare transient and sustained signaling and distinguish early amplitude from later duration.
3. Calculate a vehicle-adjusted inhibitor contrast and state why a compound response alone does not prove target specificity.
4. Interpret a downstream bypass rescue as bounded pathway-position evidence and identify controls for construct, target engagement, viability, and later cell-state claims.

These objectives map to the course's week-11 signaling-dynamics objectives and the four intended course outcomes on quantitative models, information flow, and experimental evidence. The interactive set returns deterministic practice feedback on fixed numeric outputs and explicit choices. It does not grade free-response prose or award course credit.

## Design and replicate structure

The linked [synthetic CSV](signaling-timecourse.csv) has six treatment conditions, five collection times (0, 2, 10, 30, and 60 minutes), and four independently prepared culture batches (P01–P04) split into matched condition wells. A destructive biochemical collection uses a separate sister well at each time point, so the same preparation label tracks a matched experimental block across conditions and time. The biological replicate count is four preparations per condition; a cell, well, assay read, or collection time is not an additional independent preparation.

The response column is a dimensionless synthetic pERK-to-total-ERK signal scaled so the vehicle signal is about 1.0. The data include a similar early increase after ligand pulse or continuous exposure, a decline toward vehicle after washout, and a sustained elevation while ligand remains present. Continuous MEK inhibitor and receptor inhibitor conditions remain near baseline in this constructed series. Active MEK under receptor inhibition restores part, not all, of the measured trajectory. The values are designed to make the comparisons reproducible; they are not measured effect sizes and do not support a statistical-significance claim.

| Condition | Perturbation schedule | 2-min mean | 60-min mean |
| --- | --- | ---: | ---: |
| Vehicle | No ligand; matched carrier | 1.00 | 1.00 |
| Ligand pulse | Ligand for 2 min, then wash | 4.80 | 1.10 |
| Continuous ligand | Ligand maintained | 4.90 | 3.20 |
| Ligand + MEK inhibitor | Continuous ligand; inhibitor pretreatment | 1.15 | 1.00 |
| Ligand + receptor inhibitor | Continuous ligand; receptor inhibitor pretreatment | 1.20 | 1.00 |
| Receptor inhibitor + active MEK | Continuous ligand; receptor block; induced active-MEK bypass | 4.20 | 2.60 |

Each table mean is calculated from four synthetic preparation-level values in the CSV. The data do not encode the true underlying variability of a cell system.

## Analysis sequence

### 1. Inspect the table before choosing a mechanism

Verify the CSV header and rows. Keep biological preparation as the independent unit. Group observations by condition and collection time; calculate the arithmetic mean only after retaining the four preparation values. Do not average all time points together. The software's upload check asks for preparation count and mean at 2 and 60 minutes for each condition; it does not ask the learner to upload code or raw data.

### 2. Plot amplitude and duration

Enter the vehicle, pulse, and continuous-ligand condition-time means on the supplied time (min) and relative-signal axes. The accessible widget previews individual points but does not connect them with lines; compare the ordered time coordinates to reason about the trajectory. A peak describes the early amplitude, while a later level describes persistence in the selected observation window. A 60-minute difference cannot tell whether the signal stayed elevated continuously between measured times.

### 3. Interpret the inhibitor contrast

At two minutes, use the formula 100 × [1 − (inhibitor − vehicle)/(ligand − vehicle)] to calculate the vehicle-adjusted reduction in the ligand-associated pERK signal. From the displayed means, ligand minus vehicle is 4.90 − 1.00 = 3.90 relative units; inhibitor minus vehicle is 1.15 − 1.00 = 0.15. The calculated descriptive suppression is about 96.2%.

This arithmetic does not supply an uncertainty interval or prove that MEK was the only affected target. A compound may alter another signaling component, ligand delivery, cell health, or assay behavior. The best next check is not simply more wells with the same compound: include target-engagement evidence and a distinct, controlled perturbation, and examine a specific rescue of a prespecified measured node.

### 4. Bound the bypass claim

The active-MEK condition rises above the receptor-inhibitor-alone condition in this synthetic pERK series. That pattern is compatible with active MEK bypassing an upstream receptor block for the measured pERK readout. The construct could also change other processes, and the dataset does not measure receptor state, every ERK branch, transcription, proliferation, differentiation, or function.

A real study would prespecify the primary signal metric and collection times; include matched inducer and empty-vector controls; verify expression and target engagement; measure total ERK, cell count, and viability; retain independently prepared batches; and use an orthogonal perturbation. If the claim concerns cell fate, a separate, later, validated cell-state or functional assay is necessary. Report each outcome at the level actually measured.

## Worked calculation

At two minutes, the continuous-ligand mean is 4.90 and the inhibitor mean is 1.15; the vehicle mean is 1.00. After subtracting vehicle, the measured ligand-associated signal is 3.90 and the inhibitor-associated signal is 0.15 relative units. Thus the constructed signal suppression is 100 × (1 − 0.15/3.90) = 96.15%, or 96.2% to three significant figures. This is a descriptive ratio on an authored relative scale, not an estimate of drug efficacy or target occupancy.

## Analytic rubric for an instructor extension

| Criterion | Full-credit evidence |
| --- | --- |
| Replicate-aware summaries | Retains four independent preparation values per condition-time group and calculates the requested means. |
| Trajectory comparison | Identifies similar early ligand responses, decline after pulse washout, and sustained signal under continuous exposure without inferring behavior between sparse samples. |
| Inhibitor calculation | Subtracts the vehicle mean from both conditions before calculating the approximate 96.2% descriptive suppression. |
| Perturbation logic | Treats a single compound response as compatible with target contribution, not proof of specificity; identifies target engagement and an orthogonal controlled test. |
| Rescue boundary | States that activated MEK restores part of the measured pERK pattern in this system, and requires separate evidence for normal physiology or cell fate. |
| Alternative controls | Includes matched construct/inducer, total ERK, cell number/viability, and prespecified readouts at relevant times. |

For instructor-led use, award 0–2 points per criterion: 0 for absent or incompatible evidence, 1 for partial evidence with a missing denominator or control, and 2 for the evidence listed above. The platform's current set does not grade this prose rubric. Its 20 ungraded practice points come from a 24-cell summary table, 15 fixed-axis coordinate pairs, one numeric contrast, and five explicit evidence choices.

## Limitations

The dataset is constructed, intentionally regular, and small. It has no raw blots, image files, assay calibration, inhibitor concentration-response, pharmacokinetics, independently estimated variance model, randomized plate map, target-engagement measurement, or measured cell outcome. The conditions are a teaching comparison, not an experimental protocol. A low pERK value can reflect more than one biological or measurement process; a bypass rescue can reflect artificial expression; and a sparse time course can miss peaks. Do not use these data to choose a treatment or infer a therapeutic effect.

The interactive graph scores coordinates on supplied axes and does not grade axis choice, uncertainty analysis, or a mechanistic explanation. The CSV checker only checks specific output cells. Structured responses are keyed choices, not an assessment of free-written reasoning. Publicly visible answer specifications make this open practice unsuitable for secure exams or a grade-bearing course assessment.

## Provenance and license

The lab narrative, question set, and synthetic CSV are original and licensed CC BY 4.0. No data, figures, or explanatory text were copied or adapted from cited material. The [MIT OpenCourseWare 7.016 calendar](https://ocw.mit.edu/courses/7-016-introductory-biology-fall-2018/pages/calendar/) is a link-only curriculum comparator for introductory cell signaling. The [NCBI Bookshelf receptor tyrosine kinase chapter](https://www.ncbi.nlm.nih.gov/books/NBK26822/) and [NCBI Bookshelf GPCR chapter](https://www.ncbi.nlm.nih.gov/books/NBK26912/) are link-only scientific references; the exact mapped entries and reuse limits are recorded in `content/sources/registry.json`. No MIT endorsement or affiliation is implied.

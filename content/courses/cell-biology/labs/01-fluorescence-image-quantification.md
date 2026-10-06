# Virtual lab 1: quantitative fluorescence image analysis

**Activity type:** data-analysis lab with public, ungraded formative checks  
**Course package:** Foundations of Cell and Molecular Biology, version 0.16.0  
**Estimated learner time:** 2–3 hours  
**Data status:** wholly synthetic teaching data; no microscopy images or biological samples are provided.

## Question

A research group asks whether a differentiation cue is associated with a change in a candidate lineage-marker fraction. The team has four independently prepared cell-culture batches. Within each batch, aliquots were assigned to vehicle or cue conditions. Each row reports a subsample of 100 viable nuclei from one independently prepared batch.

The prompt is deliberately narrow. Does the measured fraction of nuclei above one prespecified fluorescence threshold differ across these conditions? The exercise does not test developmental potency, mature function, a molecular mechanism, or clinical efficacy.

## Learning objectives

On completion, learners should be able to:

1. Calculate a marker-positive fraction using the stated viable-nucleus denominator and summarize batch-level values.
2. Distinguish cells or image fields nested within a culture from independent biological preparations.
3. Select acquisition, labeling, and analysis controls that address background, saturation, and condition-dependent thresholding.
4. Graph observed batch-level measurements and limit a biological claim to the marker and conditions measured.

These objectives practice the existing week 5 imaging objectives. The original interactive checks are listed as the virtual-lab assessment in the course assessment plan. They award practice points only; they do not contribute to a course grade.

## Synthetic data

The [CSV file](https://raw.githubusercontent.com/dylanstechmann/uniStemCourseSimulators/main/content/courses/cell-biology/labs/image-counts.csv) contains the same eight observations shown below. It is safe numeric teaching data. Each row is one independent culture preparation in the named condition; the 100 nuclei are nested observations, not 100 independent experiments.

| Condition | Batch | Viable nuclei sampled | Marker-positive nuclei | Exposure (ms) | Saturated fields |
| --- | --- | ---: | ---: | ---: | ---: |
| Vehicle | B01 | 100 | 12 | 40 | 0 |
| Vehicle | B02 | 100 | 13 | 40 | 0 |
| Vehicle | B03 | 100 | 14 | 40 | 0 |
| Vehicle | B04 | 100 | 13 | 40 | 0 |
| Cue | B01 | 100 | 20 | 40 | 0 |
| Cue | B02 | 100 | 23 | 40 | 0 |
| Cue | B03 | 100 | 22 | 40 | 0 |
| Cue | B04 | 100 | 23 | 40 | 0 |

The synthetic acquisition note says detector exposure and gain were held fixed, raw values remained below saturation, and one threshold was selected before condition labels were examined. A no-primary control and a secondary-only control showed low background; a reference-positive sample was detected. These short notes are assumed for the calculation exercise, not a complete microscope-validation record.

## Analysis workflow

1. **Define the measurement.** For each batch, compute `100 × marker-positive nuclei / viable nuclei sampled`. State that the result is a fraction of the sampled viable nuclei, not a count of all cells in the culture.
2. **Retain the replicate structure.** Keep all four batch values per condition. Calculate an arithmetic mean across the four independent batch-level fractions. Do not treat the 800 sampled nuclei as 800 biological replicates.
3. **Summarize and plot.** Upload a CSV with one summary row per condition and plot the two condition means on the supplied fixed axes. Keep the four batch values available for inspection; the plotted means alone hide their spread.
4. **Interpret within scope.** Compare the observed percentages and state the absolute difference in percentage points. The assessment does not require a significance claim. With four synthetic batches and no prespecified inferential model, a difference between means is descriptive.
5. **Name the next evidence.** A marker-associated shift does not establish cell identity, differentiation quality, or tissue function. A stronger follow-up would include an orthogonal lineage measurement, a prespecified cell-relevant functional assay, matched viability and recovery, and enough independently prepared batches for an uncertainty analysis.

The expected descriptive means are 13% for vehicle and 22% for cue, a difference of 9 percentage points. These values are calculated from the displayed batch values and are independently checked by the content validator.

## Controls and quality checks

- Hold objective, exposure, gain, illumination, processing, and segmentation settings constant across compared samples when the measurement permits.
- Use no-primary/secondary-only and single-label controls when appropriate to diagnose background, nonspecific labeling, and channel bleed-through.
- Set the marker threshold before inspecting condition labels. Preserve raw images, metadata, and the segmentation rule so the result can be reproduced.
- Exclude or separately investigate saturated measurements using a rule declared before comparing conditions. Do not silently tune each image until a preferred outcome appears.
- Report viable-cell recovery and the denominator. Lost or detached cells can change the composition of the measured sample.
- Use cultures or independent differentiation preparations as the biological replicate. Additional cells, fields, and technical wells within one preparation improve within-sample measurement but do not increase the number of independent preparations.

## Analytic rubric for an instructor extension

| Criterion | Full-credit evidence |
| --- | --- |
| Measurement and denominator | Computes marker-positive nuclei divided by sampled viable nuclei for each batch, then multiplies by 100. |
| Replication | Treats B01–B04 as four independent preparations per condition and the measured nuclei as nested observations. |
| Image controls | Recognizes fixed acquisition and a prespecified threshold, and names controls for background or label specificity. |
| Summary and graph | Reports the condition means as 13% and 22%, with a labeled percentage axis and the batch values retained. |
| Inference boundary | Calls the 9-point contrast descriptive and does not infer function, mechanism, statistical significance, or clinical relevance from these data. |

For instructor-led use, award 0–2 points per criterion: 0 for absent or incompatible evidence, 1 for a partially correct statement missing a key denominator/control/limit, and 2 for the evidence listed above. This transparent rubric is guidance; the current software does not grade free-response prose against it. The automated set scores only its numeric table cells, fixed-axis coordinates, and explicit structured choices.

## Limitations and safety

This is a data-analysis exercise, not an executable microscope simulation or wet-lab protocol. The synthetic counts have no measured image files, calibration history, biological variability beyond four constructed batches, or evidence that the candidate marker is specific to a lineage. The course does not authorize human-cell, animal, embryo, or clinical work. No clinical or therapeutic conclusion follows from this activity.

## Provenance

The activity, dataset, and assessment are original and licensed CC BY 4.0. Data are synthetic and were calculated for teaching; they do not reproduce measurements from cited sources. [MIT OCW 7.016 Lecture 29: Cell Imaging Techniques](https://ocw.mit.edu/courses/7-016-introductory-biology-fall-2018/resources/lecture-29-cell-imaging-techniques/) is a link-only curriculum comparator. Waters, “Accuracy and precision in quantitative fluorescence microscopy,” is a link-only methods reference: [PubMed record](https://pubmed.ncbi.nlm.nih.gov/19564400/). No text, question, figure, image, or dataset from these references is copied or adapted, and no MIT endorsement is implied.

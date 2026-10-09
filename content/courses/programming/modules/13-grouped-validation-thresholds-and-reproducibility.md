# Grouped validation, thresholds and reproducible reports

**Status:** original formative instruction with substantial AI assistance. All donors, labels, scores and decisions below are synthetic. This lesson connects the preserved regression reading to the classifier case. It describes evidence needed for a computational comparison, not deployment or a clinical recommendation.

## Learning objectives

1. Compute classification metrics with explicit denominators and a stated threshold rule.
2. Identify group and preprocessing leakage relative to a chosen prediction target.
3. Plan a reproducible report that distinguishes model selection from final evaluation.

## Define what a held-out unit means

A row can be a measurement while a donor is the independent unit for a generalization question. If multiple rows come from each donor, a random row split can put the same donor in training and evaluation. A flexible model may use donor-specific information that would not be available for a new donor. Such a split estimates performance for its own information setting; it does not automatically estimate performance on unseen donors.

For a target of unseen-donor prediction, keep each donor entirely in one split. For a future-time target, retain temporal order and avoid using future observations while constructing earlier features. Group separation alone does not prevent temporal leakage. Batch, device and site identities can also define dependence or a relevant shift. The target determines which separation is needed.

Data cleaning rules selected from the full dataset can leak information even when model fitting uses only training rows. Fitting a scaler on evaluation values lets the evaluation distribution influence the representation. For example, training values [0,2] have mean one; adding held-out [100,102] gives global mean 51. A transform trained on all four records is numerically reproducible, but does not follow a training-only preprocessing contract.

## Metrics are conditional counts

Define predicted positive when score≥threshold. Specify equality at the threshold, label encoding and the observation unit. True positives are positive labels predicted positive; false positives are negative labels predicted positive. False negatives are positive labels predicted negative; true negatives are negative labels predicted negative.

Sensitivity is TP/(TP+FN), while precision is TP/(TP+FP). Specificity is TN/(TN+FP), and accuracy is (TP+TN)/N. These denominators answer different questions. When a denominator is zero, report the metric as undefined under the declared rule rather than silently inventing a value. A library may offer conventions for that case, but a report must identify the convention.

A majority-negative classifier on 1000 observations with ten positive labels achieves 990/1000=99% accuracy, sensitivity zero and undefined precision because it predicts no positives. High accuracy therefore coexists with missing every positive. The preserved case asks for additional metrics and validation checks for exactly this reason. Neither a more elaborate algorithm nor another decimal place in accuracy solves the denominator problem.

## Thresholds belong to the selection process

Changing a threshold trades false positives against false negatives. Compare thresholds using training/validation information appropriate to the intended decision, then lock the selected rule before final evaluation. Selecting the best threshold on the final test set and reporting that same set as untouched overstates the independence of the estimate. Repeating this across many candidate models compounds selection effects.

Nested evaluation or a separate untouched test set can separate selection from evaluation. Cross-validation folds still need group and time rules consistent with the target. Stratification addresses label balance; it does not prevent the same donor appearing on both sides. A split can be perfectly reproducible and inappropriate for the question.

Calibration is also different from classification accuracy. It asks whether stated probabilities align with observed frequencies across relevant conditions. Ranking metrics, threshold metrics and calibration assess different aspects of prediction. A score of 0.8 is not automatically an 80% validated probability just because it is stored between zero and one.

## Worked example

Eight synthetic observations have labels [1,0,1,0,0,1,0,0] and scores [0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2]. At threshold 0.5 with equality positive, TP=2, FP=3, FN=1 and TN=2. Sensitivity is 2/3, precision is 2/5, specificity is 2/5 and accuracy is 4/8. F1, defined as 2TP/(2TP+FP+FN), is 0.5.

At threshold 0.7, TP stays two while FP falls to one, FN stays one and TN rises to four. Accuracy becomes 6/8=0.75 and precision becomes 2/3. This synthetic comparison illustrates threshold effects; it supplies no decision cost or validated threshold for a real setting. Choosing 0.7 only because this small evaluation table looks better would turn the table into selection data.

Now assign two adjacent records to each of four donors. A split placing each donor's first record in training and second in evaluation has four overlapping donors, even though row identifiers are unique. A split keeping donors one and two in training and donors three and four in evaluation has no donor overlap. It has fewer independent groups than rows, and does not establish generalization to another site or future time.

## Reproducibility is a chain of artifacts

Record immutable raw inputs, parsing and exclusion rules, split assignments, training-only transformations, code revision, dependency versions, candidate-selection procedure and final threshold. A pseudorandom seed alone does not specify the algorithm, software version or order of inputs. Preserve split identifiers directly when exact reconstruction matters. A plot should expose counts, units, threshold and grouping rather than present a single score without context.

Keep the final evaluation report separate from exploratory selection reports. If the final set is consulted to change the model, disclose that use and treat its later score accordingly. Reproducible leakage is still leakage; provenance allows it to be detected, not excused.

## Common mistakes

Equating accuracy with usefulness, treating dependent rows as independent donors, fitting preprocessing on the full file and hiding undefined precision are common failures. Another is using the final score to tune a threshold while still calling the set untouched. Report what information was available at each stage.

## Limits of this lesson

Small constructed counts do not establish clinical utility, transportability or uncertainty intervals. Choices assess selected evidence decisions, not implementation or essay quality. The official [scikit-learn grouped cross-validation guidance](https://scikit-learn.org/stable/modules/cross_validation.html) is link-only. Original counts and explanations are CC BY 4.0. The package remains partial and unreviewed; no third-party dataset or example was imported.

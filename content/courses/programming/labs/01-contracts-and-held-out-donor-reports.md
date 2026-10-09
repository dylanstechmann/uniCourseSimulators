# Virtual lab 1: contract checks and held-out donor reports

**Status:** public formative practice with public answers and unlimited retries. Points are study feedback, not course grades. All records, donors, measurements, labels and scores are synthetic. No learner code runs on the server. A local implementation is optional and remains self-assessed; the software scores selected numeric, CSV and choice responses.

## Learning objectives

1. Apply a declared input contract, preserve exclusion reasons and summarize accepted concentrations by donor.
2. Calculate threshold metrics on frozen held-out records with explicit denominators.
3. Distinguish reproducible processing, group separation and evidence for classifier usefulness.

## Data dictionary and construction

The original file [pipeline-records.csv](pipeline-records.csv) has twenty records. Columns are record_id,donor,split,mass_mg,volume,volume_unit,label,score. Record identifiers are unique. Labels are zero or one and scores are between zero and one. The label and score are independently supplied toy classifier outputs; no learner fits a classifier to the concentration column. In particular, the exercise does not claim that concentration determines the labels or explains the scores.

Training donors are d01–d04 and evaluation donors d05–d08. Each donor has two valid concentration records. For donor number i, the concentrations are i and i+2 mg/mL. Their masses are half those values in mg and volume is always 0.5 mL, expressed as either 500 uL or 0.5 mL. This mixture tests unit conversion while leaving the raw tokens unchanged. It is not a measurement-error distribution or an estimate of donor variability.

For each split, the eight valid records have scores [0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2] and labels [1,0,1,0,0,1,0,0] in record order. Training records are T01–T08 and evaluation records are E01–E08. Scores are frozen construction values, supplied without a model-fitting procedure. The study compares predefined threshold behavior, not a fitted model's external validity.

Four additional records are deliberately invalid. X01 belongs to d01 and has blank mass. X02 belongs to d02 and has zero volume. X03 belongs to d05 and has mass token nan. X04 belongs to d06 and has volume unit drop, which the contract does not recognize. The failures are distinct, one per record; no priority rule is needed for multiple failures in one row. Their labels and scores do not override their invalid concentration records.

## Declared processing contract

Preserve the raw file. Parse mass and volume as finite real values, require mass≥0 and volume>0, and accept only volume units uL or mL. Convert uL to mL by dividing by 1000 exactly once. Concentration is mass_mg/volume_ml. Quarantine an invalid record with its identifier and reason. Do not substitute zero, invent a unit or remove all other records from the same donor.

This lab's evaluation policy uses only records accepted by the complete concentration contract. That policy is stipulated for the exercise, even though the scores are supplied separately. It is not a universal requirement for classifier evaluation. In real work, exclusions could change the evaluated population or depend on outcomes. Report why the policy was chosen and examine excluded records rather than assuming that complete-case filtering is unbiased.

Group accepted concentrations by donor while retaining the frozen split assignments. Submit a summary with exactly donor,accepted_records,mean_concentration_mg_ml as its headers and d01 through d08 as row codes. Each donor has two accepted records and mean i+1 mg/mL. There are sixteen numeric CSV checks: eight counts and eight means. Counts require exact values; mean checks use the declared absolute tolerance. These checks do not inspect a learner's source code or certify its reproducibility.

## Work sequence

Open Practice gradebook and select this virtual lab as open, ungraded practice. First inspect tokens and units, then produce an accepted-record table and an exclusion log. The log is a self-assessed artifact, while the uploaded donor summary has deterministic checks. Retain the raw record identifiers in derived tables so each mean can be traced to its inputs.

Next evaluate only E01–E08 using the frozen threshold rule score≥0.5. Include the equality at 0.5. Build a confusion table before calculating sensitivity and precision. The supplied training scores do not contribute to these held-out metric denominators. Separating split membership from grouping prevents accidental pooling of sixteen valid rows into one evaluation score.

Finally compare the predefined threshold 0.7 as an exploratory calculation. If that comparison is used to select a final threshold, the evaluation records have been consulted for selection. There is no second untouched test set in this lab. Record that limitation rather than labeling the better observed score as independent validation.

## Worked example

Donor d05 has masses 2.5 and 3.5 mg with equivalent half-mL volumes. Its accepted concentrations are five and seven mg/mL, and its mean is six. The additional nan-mass record X03 is quarantined; dividing the sum twelve by three would invent a third observed concentration and lower the reported mean incorrectly.

At threshold 0.5, E01 and E03 are true positives, E02,E04,E05 are false positives, E06 is a false negative and E07,E08 are true negatives. Therefore precision is 2/5=0.4, sensitivity is 2/3, specificity is 2/5 and accuracy is 4/8=0.5. Threshold 0.7 gives TP=2,FP=1,FN=1,TN=4 and accuracy 0.75. No cost model makes either threshold a real decision recommendation.

## Common mistakes

Including nan after a successful float conversion, treating blank mass as zero, guessing a drop volume and averaging before unit conversion all violate the contract. Another mistake is calculating evaluation metrics from both splits or claiming that sixteen records represent sixteen donors. There are eight donor identifiers and only four in each accepted split. Repeated values and fixed seeds establish no independent replication.

## Limits of this lesson

The preserved classifier case remains a zero-point self-assessment checklist. This lab supplies additional metrics and donor-separation examples without grading an essay, a plot or a code implementation. It contains no fitted classifier, confidence interval, external dataset or real utility evidence. Original guide and CSV are CC BY 4.0 with substantial AI assistance. Qualified review, accessibility review and measured workload are absent. One toy data lab is not a laboratory sequence; the package stays partial, unreviewed and formative-only.

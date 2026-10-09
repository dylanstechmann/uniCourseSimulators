# Virtual lab 1: calibrated peak amounts and enantiomeric excess

**Status:** public formative practice with public answers and unlimited retries. Points are study feedback, not a course grade. This is a synthetic data exercise with no synthesis, separation or instrument-operation procedure. Prerequisites: stereochemical labels, analytical constraints and reaction-network evidence.

## Learning objectives

1. Summarize peak reports and determine supplied blank offsets and separate channel gains.
2. Convert reporting areas to amounts and calculate signed enantiomeric excess or amount ratio.
3. Distinguish response calibration, optical identity, absolute configuration and sample-purity claims.

## Construction and independent information

A hypothetical resolved enantiomeric pair is labeled A and B. Independent supplied standard identities associate A with positive and B with negative optical rotation under matching conditions. No R/S descriptors or actual molecular structure are given. Retention order and optical sign do not establish those descriptors. The model assumes no coelution, no other components and a linear response within the stated amount range.

The reporting model is area_A=3+2n_A and area_B=3+n_B, with amounts in micromoles and arbitrary area units. The unequal factors are deliberately assigned end-to-end reporting gains, which may represent peak-specific processing or recovery in this abstract model. They are not claimed intrinsic UV absorptivity differences between enantiomers in the same achiral environment. No actual detector or separation system is validated.

An independent blank contains neither enantiomer. Standard std_a contains 10.0 µmol A and no B; std_b contains 10.0 µmol B and no A. Four constructed mixtures contain A/B amounts 9/1,7/3,5/5 and 2/8 µmol. Those declared construction amounts explain the public answer examples; the learner work uses the reported table and independently supplied standard information to recover them.

Each central report has three deliberately balanced versions with offsets −0.2, zero and +0.2 area units added to both channels. Thus the two channels' demonstration offsets covary and their arithmetic means equal the central values. These repeats establish no independent sampling, Gaussian noise or real instrument precision. A blank report remains nonzero because of reporting offset, not because it contains material.

## Data dictionary

[Download the synthetic CSV](https://raw.githubusercontent.com/dylanstechmann/uniStemCourseSimulators/main/content/courses/organic-chemistry/labs/peak-reports.csv). `sample` identifies blank, pure standards or mixture groups; `replicate` identifies one of three constructed reports; `area_a` and `area_b` are raw arbitrary reporting areas, including additive offsets. No real experiment or learner record is supplied.

| Sample | Mean raw area A | Mean raw area B |
|---|---:|---:|
| blank | 3.0 | 3.0 |
| std_a | 23.0 | 3.0 |
| std_b | 3.0 | 13.0 |
| mix_1 | 21.0 | 4.0 |
| mix_2 | 17.0 | 6.0 |
| mix_3 | 13.0 | 8.0 |
| mix_4 | 7.0 | 11.0 |

## Work sequence

Open Practice gradebook and select **Virtual lab 1: calibrated peak amounts and enantiomeric excess (ungraded practice)**. Upload exact columns `sample,replicates,mean_area_a,mean_area_b` with all seven row codes. The software checks seven counts and fourteen raw means, with mean tolerance 0.005 area units. It does not automatically grade a written uncertainty, purity or method-validation argument.

First average raw reports within each group. Use the zero-amount blank to determine a separate offset for each channel. Then divide each pure-standard blank-corrected area by its independently known 10.0 µmol amount to find the corresponding gain. Apply A's factor to A and B's factor to B; transferring one factor to both channels changes the inferred composition.

Calculate each mixture amount n_A=(mean_area_A−offset_A)/gain_A and the corresponding n_B. Their total provides a consistency check with the constructed 10 µmol inventory, but it is not a newly measured total supplied by an independent real method. Signed A excess is 100(n_A−n_B)/(n_A+n_B). Its magnitude measures imbalance and its sign identifies the majority of the given pair.

## Worked calculation

Blank means are 3 and 3 area units. Pure std_a has A area 23, so A gain is (23−3)/10=2. Pure std_b has B area 13, so B gain is (13−3)/10=1. For mix_2, areas 17 and 6 give amounts (17−3)/2=7 and (6−3)/1=3 µmol. Signed A excess is 100×4/10=40%, and A's amount fraction is 70%, a different quantity.

If blank-corrected mix_2 areas 14 and 3 were treated directly as amounts, the apparent excess would be 100×11/17≈64.7059%. Offset subtraction therefore does not fix unequal gains. For mix_3, corrected areas 10 and 5 are unequal, yet calibrated amounts are both 5 and excess is zero. For mix_4, calibrated A=2 and B=8 give B/A=4 and a negative signed A excess.

## Interpretation criteria

| Criterion | Evidence to discuss |
|---|---|
| Summary | Correct grouping, counts and raw means for both channels |
| Blank | Zero-amount reference used as reporting baseline |
| Calibration | Separate gains from separate known pure standards |
| Composition | Positive calibrated amounts and pair normalization |
| Stereochemistry | Excess, major fraction and optical identity kept distinct |
| Limits | Linearity, absence of interference and identity are supplied assumptions |

All answer examples are public formative authoring material. An actual sample could contain coeluting components, nonlinear responses or differences in recovery not captured by the standards. A good numerical fit to this construction does not establish those real conditions. Equal calibrated amounts establish a racemic pair only within the supplied two-enantiomer model; zero rotation alone is not a unique identity or purity test.

## Limits and provenance

All amounts, gains, identities and reports are synthetic. One blank and one amount standard per channel determine the stipulated linear construction, rather than independently demonstrating linearity over a range. The exercise supplies no actual molecule, detector, chromatographic method, absolute stereochemical assignment or biological potency claim. The preserved amide case remains a separate self-assessment discussion. Original guide and CSV are CC BY 4.0 with substantial AI assistance; no third-party teaching text or dataset was copied. One data lab is not a laboratory sequence. The course remains partial, unreviewed and formative-only.

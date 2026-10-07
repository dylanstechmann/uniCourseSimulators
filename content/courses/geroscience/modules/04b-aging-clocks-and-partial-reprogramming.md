# Aging clocks and partial reprogramming: evaluating rejuvenation claims

"Rejuvenation" is increasingly claimed on the basis of a molecular aging clock moving backward. Some such results are real and scientifically important; others reflect measurement noise, a change in which cells were sampled, or cells losing their identity. This lesson explains how clocks are built, what can move them, and how to design a partial-reprogramming experiment whose conclusion survives those alternatives.

## Learning objectives

By the end of this lesson, you should be able to:

1. Explain how epigenetic clocks are trained and calculate age acceleration as a residual from a reference calibration.
2. Evaluate whether a change in clock age after an intervention supports rejuvenation, considering measurement error, cell-composition shifts, regression to the mean, and loss of cell identity.
3. Design measurements for a partial-reprogramming experiment that separate youthful features from dedifferentiation and tumor risk.

## How an epigenetic clock is built

DNA methylation at some CpG sites changes with age in reproducible directions. An **epigenetic clock** is a regression model, frequently a penalized linear model such as the elastic net, that predicts a target from methylation at a selected set of CpGs. A widely used pan-tissue clock (2013) combined 353 CpGs and was trained on thousands of samples from many tissues; its estimates are near zero for embryonic and induced pluripotent stem cells. Other clocks were trained in blood, on composite clinical phenotypes, on mortality risk, or on the rate of change across repeated measures.

**The training target defines what a clock means.** A clock trained to predict chronological age can be very accurate for age while tracking health only weakly. A clock trained on mortality risk carries more health information but inherits the populations and risk factors it was trained on.

**Age acceleration** is usually the residual from regressing clock age on chronological age in a reference population: AA = clock age − (a + b × chronological age). Using the raw difference (clock age − chronological age) is biased whenever the calibration slope b differs from 1, because the raw difference then changes systematically with age.

## Why a clock can move without rejuvenation

- **Technical noise.** Array batch, preprocessing, and probe reliability matter. Repeated measurement of the same DNA can differ by years for some clocks; reliability-focused constructions reduce but do not remove this noise.
- **Cell composition.** A blood clock partly reflects the proportions of cell types, such as naive and memory lymphocytes. A treatment that shifts composition can move the estimate without changing the state of any individual cell.
- **Regression to the mean.** If participants are selected because their age acceleration is high, their follow-up values will tend to be lower even without treatment. Only a randomized comparison group separates this from an effect.
- **Context mismatch.** A clock trained on human blood or tissues may not transfer to cultured cells, other species, or disease states.

## Partial reprogramming

Forced expression of **OCT4, SOX2, KLF4, and c-MYC (OSKM)** can reprogram somatic cells into induced pluripotent stem cells, erasing somatic identity. In mice, sustained in vivo OSKM expression produced teratomas in multiple organs. **Partial reprogramming** uses shorter or cyclic induction to reset some age-associated features without crossing into dedifferentiation. In a progeroid mouse model, cyclic short-term OSKM induction ameliorated cellular and physiological hallmarks of aging and extended lifespan. Expressing OSK without c-MYC in retinal ganglion cells promoted axon regeneration after optic-nerve injury and reversed vision loss in a mouse glaucoma model and in aged mice. These are model-specific results; delivery, control of expression, and long-term safety in people are unsolved.

The central risk is a threshold. Beyond some dose and duration, cells lose lineage markers, express pluripotency genes, and can form tumors. A clock may keep moving "younger" as identity is lost, because a pluripotent cell is epigenetically young. **A bigger clock change is therefore not automatically a better rejuvenation.**

## Synthetic time course

The values below are **synthetic teaching data** for adult human dermal fibroblasts with doxycycline-inducible OSKM. Cultures were induced for the stated number of days, then grown for six days without induction before measurement. Four independent preparations were averaged per condition. Clock values come from a pan-tissue model applied to cultured cells, so they are relative indicators rather than calibrated ages.

| Induction (days) | Clock estimate (years) | Fibroblast-marker-positive cells (%) | Pluripotency-marker-positive cells (%) | Collagen secretion (relative to day 0) |
| ---: | ---: | ---: | ---: | ---: |
| 0 | 52 | 96 | 0.1 | 1.00 |
| 4 | 44 | 93 | 0.3 | 1.05 |
| 8 | 37 | 71 | 2.5 | 0.80 |
| 12 | 30 | 38 | 11.0 | 0.45 |

The clock falls steadily with induction. Identity and function are retained only at day 4; by day 8 and day 12 fibroblast markers and collagen secretion fall while pluripotency-marker-positive cells rise. Only the day-4 condition is consistent with a younger-appearing profile that keeps cell identity, and even it needs durability, genome-integrity, and tumorigenicity testing before any claim.

## Worked example: compute and interpret age acceleration

In a reference cohort, a clock calibrates as clock age = 4 + 0.92 × chronological age. A 50-year-old's sample reads 55. The predicted value is 4 + 0.92 × 50 = 50, so age acceleration is 55 − 50 = +5 years. The raw difference happens to be the same here, but for an 80-year-old reading 80 the prediction is 77.6, so acceleration is +2.4 years while the raw difference is zero. If this person were enrolled *because* of high acceleration, a lower value at follow-up would be expected even without treatment, so a randomized control is required to attribute the change.

## Limits of this lesson

The time course is synthetic and is not a protocol. This lesson does not describe how to deliver reprogramming factors, does not endorse commercial biological-age tests, and does not treat a clock change as evidence of improved health, function, or lifespan.

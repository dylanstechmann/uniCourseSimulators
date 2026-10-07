# Measuring aging outcomes: survival curves, mortality hazards, and healthspan

A claim that an intervention "slows aging" is only as strong as the endpoint behind it. A longer median lifespan, a lower late-life death rate, better function at a matched age, and a shifted molecular marker are four different results. They can move together, move separately, or move in opposite directions. This lesson builds the vocabulary for keeping them apart before you evaluate any intervention.

## Learning objectives

By the end of this lesson, you should be able to:

1. Calculate an interval death probability and a Gompertz mortality-rate doubling time from cohort data, and state what each number summarizes.
2. Distinguish lifespan, healthspan, and tissue-function endpoints, including how censoring and survivor selection change what a comparison means.
3. Evaluate whether a lifespan study's design—sexes, genetic background, sites, start age, exposure, and controls—supports the generality of its claim.

## Survival curves and median lifespan

A **survival curve** S(t) gives the fraction of a cohort still alive at age t. Real studies lose some animals for reasons unrelated to the outcome: a scheduled tissue collection, an escape, or an accident judged unrelated to the treatment. Those animals are **censored**. Each one contributes follow-up time until removal and then leaves the at-risk group. Counting censored animals as deaths, or deleting them from the cohort, biases the curve; Kaplan–Meier estimation is the standard way to use their partial information.

**Median lifespan** is the age at which S(t) first reaches 0.5. It resists a few unusually long-lived animals, but it says nothing about the oldest survivors. The single longest-lived animal is a very noisy statistic, so a "maximum lifespan" claim is more defensible when it compares the fraction of each group still alive at a high percentile of the pooled survival distribution, such as the 90th. Mean lifespan requires complete follow-up; with censoring, report a restricted mean up to a stated age.

## Mortality hazard and the Gompertz description

The **hazard** μ(t) is the instantaneous death rate among animals still alive at age t. Over much of adult life in many species, hazard rises roughly exponentially:

μ(t) ≈ A · e^(G·t)

Here A sets the baseline level and G sets how quickly risk accelerates with age. The **mortality-rate doubling time** is MRDT = ln 2 / G, the age interval over which hazard doubles.

Two different intervention patterns can produce the same gain in median lifespan. Lowering A shifts the log-hazard line down at every age; lowering G makes the line shallower, so hazard rises more slowly. Some authors read a lower G as a slower "rate of aging." Be cautious: estimates of A and G are correlated, depend on the fitted age range, need large cohorts, and late-life mortality can depart from a clean exponential. Treat them as model summaries, not direct measurements of a biological aging rate. A **hazard ratio** from a proportional-hazards model compares relative risk at each age, and it is only a single-number summary if the proportionality assumption actually holds.

## Synthetic life table

The values below are **synthetic teaching data** for two groups of 60 genetically heterogeneous mice that began a treatment or a matched control diet at 18 months. No animals were censored. Each entry is the number still alive at the start of that age.

| Age (months) | Control alive | Treated alive |
| ---: | ---: | ---: |
| 18 | 60 | 60 |
| 21 | 57 | 59 |
| 24 | 50 | 55 |
| 27 | 38 | 47 |
| 30 | 24 | 35 |
| 33 | 12 | 22 |
| 36 | 4 | 10 |
| 39 | 0 | 3 |

The **interval death probability** for a band is deaths in the band divided by animals alive at its start. Between 27 and 30 months it is 14/38 ≈ 0.368 for control and 12/47 ≈ 0.255 for treated. Survival to 30 months is 24/60 = 40% versus 35/60 ≈ 58%. These descriptive numbers do not include uncertainty; a real analysis would report a survival test, confidence intervals, and the prespecified primary endpoint.

## Worked example: a doubling time from two hazards

Suppose a cohort's monthly hazard is 0.010 at 18 months and 0.040 at 30 months. Under the Gompertz form, G = ln(0.040/0.010)/(30 − 18) = ln 4/12 ≈ 0.1155 per month, and MRDT = ln 2/0.1155 ≈ 6.0 months. Now imagine a treated group whose hazard is half the control value at every age. Its G and MRDT are unchanged, yet more animals reach every age, so median lifespan increases. Doubling time and median survival answer different questions, so report both and say which one the claim is about.

## Healthspan is not one number

**Healthspan** means the part of life spent in good function, but "good function" must be defined by named measurements: grip strength, gait, endurance, motor coordination, cognitive tasks, organ physiology, a frailty index that counts accumulated deficits, disease incidence, or pathology at death. A study can extend lifespan without shortening the period of late-life disability; then more total time is spent unwell. The hoped-for pattern, a shorter disabled period relative to life length, is called **compression of morbidity**, and it must be shown rather than assumed.

Comparisons of old survivors are especially easy to misread. If a treatment keeps frailer animals alive, its surviving group can look weaker at a matched age even when every individual benefited. If a toxic treatment kills the frailest animals, its survivors can look stronger even without benefit. Prefer repeated measurements on the same animals from a common baseline age, measurements before substantial mortality, or analyses that model function and death together.

## Designing for generality

A single-sex, single-strain, single-site result is a starting point. Sex-specific responses to aging interventions are common, and an inbred strain can carry strain-specific causes of death that a treatment happens to affect. Multi-site testing with harmonized protocols in genetically heterogeneous mice addresses these problems. The U.S. National Institute on Aging's Interventions Testing Program uses this design; in its 2009 report, rapamycin started at 600 days of age extended median and maximal lifespan in both male and female mice across three independent sites.

Good designs also measure exposure (drug levels in blood or tissue), food intake, and body weight, because a compound that reduces eating can act through dietary restriction. They prespecify endpoints and analyses, keep pathology blinded, and report every death and censoring reason.

## Limits of this lesson

The life table and hazards are synthetic. This lesson does not recommend any intervention, convert mouse lifespan into human benefit, or treat a molecular marker as a substitute for survival or function. Human lifespan trials are rarely feasible, which is exactly why surrogate endpoints need validation for the claim they are used to support.

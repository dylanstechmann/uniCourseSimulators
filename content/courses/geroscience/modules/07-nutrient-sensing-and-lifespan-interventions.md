# Nutrient sensing and lifespan interventions: what the model organisms show

Cells adjust growth and maintenance to nutrient supply. Some of the most reproducible lifespan effects in the laboratory come from changing those signals, by genetic mutations, by diet, or by drugs. This lesson explains the pathways at the level needed to read the papers, shows how lifespan effects are quantified, and uses a well-known case of conflicting studies to practice judging why results differ. It does not recommend any diet or drug for people.

## Learning objectives

By the end of this lesson, you should be able to:

1. Calculate percent change in median and in late-life survival and explain why they answer different questions.
2. Explain how insulin/IGF, TOR and AMPK signaling link nutrient state to growth and maintenance programs.
3. Evaluate conflicting results from two studies of the same intervention by comparing their designs.

## Three signaling hubs

**Insulin and IGF-1 signaling.** When nutrients are plentiful, insulin and IGF-1 signal through a receptor and a kinase cascade that promotes growth and storage and restrains stress-resistance programs controlled by FOXO transcription factors. In the roundworm *C. elegans*, partial loss of function in the insulin/IGF receptor gene *daf-2* extends lifespan and requires the FOXO homolog *daf-16*. Reduced insulin/IGF signaling has been reported to extend lifespan in flies and in some mouse models, with context-dependent costs.

**TOR.** The mechanistic target of rapamycin integrates amino acids, growth factors and energy, and when active promotes protein synthesis and growth while suppressing autophagy. Rapamycin inhibits TOR complex 1. In the Interventions Testing Program, a multi-site study of genetically heterogeneous mice, rapamycin fed beginning late in life extended lifespan in both sexes.

**AMPK** senses low energy (a high AMP to ATP ratio) and shifts the cell toward catabolism and mitochondrial maintenance. Its activation is part of the response to energy restriction and exercise.

These pathways interact, and each has many targets. A lifespan effect from manipulating one therefore does not say which downstream process caused it. The same drugs and mutations also have costs: rapamycin is an approved drug for other indications with known effects on immune function and metabolism, and the doses and durations used in mice differ from clinical ones. Nothing in this lesson implies that anyone should take it.

## Dietary restriction

Reducing calories without malnutrition extends lifespan in many laboratory species, with a magnitude that depends on species, strain, sex, age at onset, diet composition and the way the control group is fed. A control group fed freely may overeat and be shortened by obesity, which can inflate the apparent benefit relative to a lean control. That is a design issue, not a flaw in either result, and it is why comparisons need the details.

## A case of conflicting studies

Two long-term studies of rhesus monkeys tested caloric restriction against controls. One, reported in 2009, found that restriction delayed disease onset and mortality. The other, reported in 2017, reached a different conclusion about all-cause survival while also reporting health benefits. The studies differed in diet composition and feeding of controls, in the origin of the animals, and in the age at which restriction began, among other points. The sensible reading is not that one study is right and the other wrong. It is that effects of restriction depend on conditions that differ between the studies, and that both are small studies of long-lived animals whose survival comparisons carry wide uncertainty.

## Quantifying survival effects

Survival studies report several summaries, and they answer different questions.

- **Median survival** is the age when half the animals have died. It measures the typical animal.
- **Late-life survival**, for example the mean age of the longest-lived 10%, is sensitive to the oldest animals and noisier because it rests on few animals.
- **Percent change** is (treated − control) / control × 100.

A treatment can raise median survival with little change at the top, which suggests it protects against early disease, or raise the top without moving the median. These patterns point to different mechanisms. The hazard-based analysis in the survival-curve lesson is preferred for testing, because it uses all deaths and handles censoring.

## Synthetic data

Values are **synthetic teaching data** from a hypothetical study with 60 animals per group.

| Group | Median survival (days) | Mean age of longest-lived 10% (days) |
|---|---:|---:|
| Control | 800 | 1000 |
| Treated | 880 | 1060 |

## Common mistakes

- Taking an effect of manipulating TOR or insulin/IGF signaling as identifying the downstream process responsible.
- Comparing dietary restriction with an overfed control, which can inflate the benefit.
- Declaring one of two conflicting studies right without comparing their designs.
- Using the median to describe the oldest survivors, or ignoring how noisy late-life survival is.
- Computing percent change relative to the treated group instead of the control.
- Reading an intervention used in mice as a recommendation for people.

## Worked example

The median changes by (880 − 800) / 800 × 100 = 10.0%. The late-life measure changes by (1060 − 1000) / 1000 × 100 = 6.0%. The median gain is larger than the gain at the top, which suggests the treatment mostly protects animals that would otherwise die earlier. Neither number is an estimate of a hazard ratio, and with 60 animals per group the late-life figure rests on only 6 animals per group.

## Limits of this lesson

The table is synthetic and the studies summarized are model-organism studies. The lesson does not claim that these interventions slow aging in people, does not give doses, and does not endorse any product. Whether any of them improves human healthspan is a question for human trials with clinical outcomes.

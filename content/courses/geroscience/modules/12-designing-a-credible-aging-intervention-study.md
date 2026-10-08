# Designing a credible aging-intervention study: endpoints, power for survival, and safeguards against fooling ourselves

The course has examined how aging is measured, which mechanisms are implicated, how to read intervention papers and why evidence from models must be weighed carefully before it says anything about people. This final lesson turns those lessons into a design exercise. It asks what a study must include for its result, positive or negative, to be believed, and it computes how large a lifespan study must be. Everything here is a planning exercise with synthetic numbers; it designs no study in people and recommends no intervention.

## Learning objectives

By the end of this lesson, you should be able to:

1. Specify a primary endpoint, comparison and analysis for an aging-intervention study in advance, and justify the choice between lifespan and healthspan endpoints.
2. Estimate the number of deaths and animals needed to detect a stated hazard ratio with a survival comparison.
3. Evaluate a study design for the safeguards that prevent false positives: randomization, blinding, both sexes, multiple sites, pre-registration and handling of censoring and survivor bias.

## Start with the question and the endpoint

A useful design states, before any data exist:

- **Population:** species, strain, sex (both, analyzed separately and together), age at start, housing.
- **Intervention and comparison:** what is given, from what age, and to what control (matched vehicle, same handling).
- **Primary endpoint:** one outcome on which the main conclusion will rest. Lifespan is unambiguous but slow and says nothing about health in late life. Healthspan measures (grip strength, gait, cognition tests, disease incidence) are closer to what people care about but are many, noisy and, when measured late, subject to survivor bias (as in the week 13 lab). A common approach is lifespan as primary, with a small number of healthspan measures pre-specified as secondary and measured at ages when nearly all animals are alive.
- **Analysis:** the survival test (for example, a log-rank test or a Cox model), how censoring is handled, how multiplicity among secondary endpoints is controlled (see the statistics lessons) and the size of difference considered meaningful.

## How many deaths are needed?

For a survival comparison, power depends on the number of **events** (deaths), not directly on the number of animals. A widely used approximation for two equal groups (Schoenfeld's formula) is

**d = 4 (z₁₋α/₂ + z₁₋β)² / (ln HR)²,**

where HR is the hazard ratio to be detected. For α = 0.05 (two-sided) and 80% power, (z₁₋α/₂ + z₁₋β)² = (1.96 + 0.8416)² = 7.85.

- To detect HR = 0.8 (a 20% lower death rate at every age): d = 4 × 7.85 / (ln 0.8)² = 631 deaths in total.
- To detect HR = 0.7: d = 247 deaths.

If about 80% of animals will die before the study ends, the number of animals needed is roughly d/0.8 = 788 for HR = 0.8, split between the two groups, before allowing for losses or analysis by sex. Many published single-site lifespan studies used far fewer animals than this; they could detect only large effects, and their positive results are more likely to be overestimates (the "winner's curse").

## Safeguards against false positives

- **Randomization** of animals to groups, and of cages to positions in the facility.
- **Blinding** of everyone who scores health measures or decides when an animal must be euthanized for welfare reasons, since those decisions define lifespan.
- **Both sexes**, because effects can differ or appear in only one.
- **Several sites** running the same protocol, because husbandry, diet and pathogens differ between facilities and can produce site-specific results.
- **Pre-registration** of the primary endpoint, analysis and stopping rules.
- **Reporting everything:** all animals, all censoring, all endpoints, including negative results.

Multi-site, pre-registered designs with these features exist in mouse aging research and have reported both positive and negative results for candidate interventions; their negative results are as informative as their positive ones.

## From animals to people

Even a well-designed animal study answers only the question it asked in that species and strain. The evidence-tier lesson describes what would be needed before any claim about human aging: mechanisms that carry across species, validated biomarkers, safety data and, eventually, trials with outcomes that matter. This course does not recommend any intervention for anyone.

## Common mistakes

- Choosing the primary endpoint after seeing the data.
- Powering a lifespan study by number of animals instead of number of deaths.
- Measuring healthspan only late, in survivors, and comparing groups directly.
- Treating one single-site result as established.

## Worked example

**Problem.** A team can afford 200 animals per group, and expects 80% to die during the study. What hazard ratio could they detect with 80% power?

**Step 1.** Expected deaths d ≈ 0.8 × 400 = 320.

**Step 2.** Solve (ln HR)² = 4 × 7.85/320 = 0.0981, so |ln HR| = 0.313 and HR = 0.73.

**Step 3.** The study can reliably detect only a reduction in death rate of about 27% or more. If the plausible effect is smaller, the design should change (more animals, more sites) or the study should be framed as exploratory.

## Limits of this lesson

All numbers are synthetic, and the event formula is an approximation for proportional hazards with equal groups. The lesson is a design exercise for animal research reasoning; it is not guidance for any study in people and not a recommendation of any intervention.

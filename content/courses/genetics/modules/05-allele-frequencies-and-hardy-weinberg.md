# Allele frequencies, Hardy–Weinberg expectations and what a departure can mean

Population genetics starts with a bookkeeping question: given a sample of genotypes, how common is each allele, and what genotype counts would we expect if alleles combined at random? The Hardy–Weinberg model answers the second part. Its value is less that real populations obey it than that departures from it are informative: they can point to genotyping error, population structure, inbreeding or selection. This lesson works through the arithmetic with a synthetic sample and then uses the same model to estimate carrier frequency for a recessive condition, stating the assumptions each step needs.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute allele frequencies and Hardy–Weinberg expected genotype counts from observed genotype counts.
2. Test and interpret a departure from Hardy–Weinberg proportions, including the heterozygote deficit summarized by F.
3. Estimate carrier frequency for a recessive trait from its incidence and state the assumptions behind the estimate.

## Counting alleles

For one locus with alleles A and a, each diploid individual carries two copies. With genotype counts n(AA), n(Aa) and n(aa) in N individuals, the frequency of A is

**p = (2 n(AA) + n(Aa)) / (2N),** and q = 1 − p.

Counting alleles needs no model; it is a description of the sample. Note that the denominator is the number of allele copies (2N), not the number of people.

## The Hardy–Weinberg expectation

If the two alleles an individual receives are drawn independently from the population's allele pool, genotype frequencies are p², 2pq and q². The assumptions behind independence are random mating with respect to this locus, no selection on it between conception and sampling, no migration or mutation large enough to matter over a generation, a large population, and a sample that represents one population. None holds exactly; the question is whether departures are large enough to see.

## A synthetic sample

**Synthetic teaching data:** 1000 individuals genotyped at one biallelic marker: AA = 420, Aa = 360, aa = 220.

p = (2 × 420 + 360) / (2 × 1000) = 0.60, q = 0.40. Expected counts are 360, 480 and 160. The sample has fewer heterozygotes and more of both homozygotes than expected.

## Testing the departure

A goodness-of-fit chi-square compares observed and expected counts: χ² = Σ (O − E)² / E. With three genotype classes and one allele frequency estimated from the data, the test has one degree of freedom. Here χ² = 10.0 + 30.0 + 22.5 = 62.5, far above 3.84, the 5% critical value for one degree of freedom. The departure is not plausibly sampling noise for this sample size.

A useful summary of a heterozygote deficit is **F = 1 − H_obs / H_exp**, where H_obs is the observed heterozygote fraction and H_exp = 2pq. Here F = 1 − 0.36/0.48 = 0.25.

## What a departure can mean

A significant chi-square says the sample does not fit random union of gametes; it does not say why. Candidate explanations predict different patterns:

- **Genotyping error**, for example heterozygotes called as homozygotes when one allele drops out, produces a heterozygote deficit at that marker only. This is why genetic association studies routinely use Hardy–Weinberg tests in control samples as a quality filter.
- **Population structure** (the Wahlund effect): pooling two groups with different allele frequencies produces a deficit of heterozygotes even when each group is in equilibrium. It affects many markers at once.
- **Inbreeding** raises homozygosity across the whole genome, not only at one locus.
- **Selection** at the locus can shift genotype frequencies in either direction, but usually needs large effects to be seen in one sample.

Distinguishing these needs more data: other markers, the sampling design, re-genotyping. One locus and one test cannot decide between them.

## Carrier frequency from incidence

For a recessive condition, affected individuals are aa. If the population is in Hardy–Weinberg proportions, q² equals the incidence, so q = √incidence and the carrier frequency is 2pq. With a synthetic incidence of 1 in 2500, q = 0.02 and 2pq = 0.0392, about 1 in 26. Most copies of a rare recessive allele are carried by heterozygotes who are unaffected.

The estimate inherits every assumption above. Consanguinity raises incidence for a given q and so inflates the estimate of q; several different alleles at the same gene (allelic heterogeneity) do not change the arithmetic but do change what "q" counts; incomplete penetrance means affected counts understate aa frequency.

## Common mistakes

- Dividing by the number of people instead of the number of allele copies (2N) when computing an allele frequency.
- Running the chi-square test on frequencies or percentages instead of counts.
- Using the wrong degrees of freedom: here one allele frequency was estimated from the data, so there is 1, not 2.
- Reading a significant departure as proof of selection, when genotyping error and population structure come first.
- Applying the square-root-of-incidence carrier estimate when consanguinity or incomplete penetrance is likely.

## Worked example

**Problem.** Two synthetic villages of 500 people each are individually in Hardy–Weinberg proportions, with allele A at frequency 0.8 in the first and 0.2 in the second. A study pools them without recording village. What heterozygote deficit does the pooled sample show?

**Step 1: each village.** Village 1 has AA/Aa/aa = 320/160/20; village 2 has 20/160/320. Each fits its own expectation exactly.

**Step 2: pool.** The pooled counts are 340/320/340 in 1000 people, so p = 0.50 and the expected heterozygote fraction is 2pq = 0.50. The observed fraction is 0.32.

**Step 3: summarize.** F = 1 − 0.32/0.50 = 0.36. Nobody inbred and no genotype was miscalled; the deficit comes entirely from mixing two populations with different allele frequencies. Every marker whose frequency differs between the villages would show a similar deficit, which is how structure is recognized and why association studies adjust for ancestry.

## Limits of this lesson

All counts are synthetic. The lesson covers a single biallelic locus in a diploid population and does not address sex-linked loci, exact tests for small samples, or linkage disequilibrium between loci.

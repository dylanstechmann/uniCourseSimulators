# Mutation rates, the fluctuation test and somatic mutation with age

New mutations are the raw material of evolution, the source of many genetic diseases and, in the body's own cells, one of the processes that accumulate with age. Measuring how often they happen is harder than it sounds, because a mutation that occurs early in a growing population is copied into many descendants. This lesson shows how mutation rates are estimated from parallel cultures, how the classic fluctuation test of Luria and Delbrück (1943) used the spread of mutant counts to show that mutations arise before selection, and how sequencing now counts the mutations that accumulate in human stem cells during life.

## Learning objectives

By the end of this lesson, you should be able to:

1. Estimate a mutation rate from the fraction of parallel cultures that contain no mutants, using the Poisson zero class.
2. Explain how the fluctuation test distinguishes mutations that arise before selection from mutations induced by it, using the variance of mutant counts across cultures.
3. Calculate somatic mutation accumulation from a per-year rate and evaluate what mutation counts in aging stem cells do and do not show.

## Rate versus frequency

The **mutation rate** is the probability of a mutation per cell per division (or per generation). The **mutant frequency** is the fraction of cells in a population that carry a mutation. They differ because each mutant divides: a mutation in the first few divisions of a culture becomes a large clone, a "jackpot", while one in the last division leaves a single mutant cell. Mutant frequency therefore depends strongly on when mutations happened and is a poor estimate of the rate.

## The zero-class (p0) method

Grow many small, independent cultures from tiny inocula, each to about N cells, so that about N cell divisions occurred in each. If mutations occur at random during growth with an average of m mutation events per culture, the number of events per culture follows a Poisson distribution, and the probability of a culture with **no** event is e^(−m). Count the cultures with no mutants at all: no mutation event means no mutants, however clonal growth spreads them.

**Synthetic experiment:** 50 parallel cultures, each grown to 2 × 10⁸ cells, are plated on a selective medium; 22 show no resistant colonies. Then p0 = 22/50 = 0.44, m = −ln 0.44 = 0.821 mutation events per culture, and the rate is m/N = 0.821/(2 × 10⁸) = 4.10 per 10⁹ cell divisions. The method works best when p0 is neither close to 0 nor close to 1.

## The fluctuation test

In 1943, bacteria that become resistant to a virus posed a question: does exposure to the virus induce resistance in a few cells, or do resistant mutants arise at random during growth, before any exposure? The two ideas make different predictions about variation.

- If exposure **induces** resistance with a small probability per cell, every culture of the same size gives a Poisson-distributed count of resistant cells: the variance should be close to the mean.
- If mutations arise **at random before exposure**, cultures in which a mutation happened early contain jackpots, so the variance across parallel cultures is far larger than the mean. Samples taken from one large culture, by contrast, all share its history and vary only by sampling, so their variance stays near their mean.

**Synthetic counts** of resistant colonies: eight independent cultures gave 0, 1, 0, 2, 0, 0, 13 and 0; eight aliquots from a single large culture gave 1, 3, 2, 0, 3, 4, 1 and 2. Both have a mean of 2.0. The variance-to-mean ratio is 10.1 for the independent cultures (sample variance 20.3) and 0.86 for the aliquots. The excess variance among independent cultures points to mutations that arose during growth, before selection, which is the conclusion of the original experiment.

## Somatic mutation in aging human cells

Body cells accumulate mutations too. Sequencing of clonal organoid cultures grown from single adult stem cells of the human small intestine, colon and liver found that mutations accumulate steadily with age, at roughly 40 new mutations per year in each tissue examined, with tissue-specific mutation spectra (Blokzijl and colleagues, 2016).

**Synthetic illustration:** a stem-cell lineage that gains 40 mutations per year, starting from zero at birth, carries about 40 × 75 = 3000 by age 75. If about 1.5% of the genome is protein-coding and mutations fall at random, about 45 of them hit coding sequence.

These counts describe accumulation. On their own they do not show that the mutations cause aging phenotypes: most fall in sequence where they have little effect, and the effect of the rest depends on which genes they hit and whether a mutant cell expands into a clone, as in clonal hematopoiesis (see the geroscience course). Testing a causal role needs experiments that change the mutation burden and measure function.

## Common mistakes

- Estimating a mutation rate from mutant frequency, which jackpots inflate.
- Applying the p0 method when nearly all or almost no cultures have mutants.
- Concluding "induced by selection" from a single culture's count; the test depends on variance across independent cultures.
- Reading a steady accumulation of somatic mutations as proof that mutations drive aging.
- Forgetting that a per-year rate starting at birth ignores mutations from development, which add an intercept.

## Worked example

**Problem.** In a second synthetic experiment, 40 cultures each reach 5 × 10⁸ cells, and 10 contain no mutants. Estimate the mutation rate.

**Step 1.** p0 = 10/40 = 0.25, so m = −ln 0.25 = 1.386 events per culture.

**Step 2.** Rate = 1.386 / (5 × 10⁸) = 2.77 per 10⁹ cell divisions.

**Step 3.** Check the conditions: p0 = 0.25 is in the useful range, the cultures were independent, and resistant mutants are assumed to grow and plate as well as non-mutants. If mutants plate less efficiently, the rate is underestimated.

## Limits of this lesson

All counts are synthetic. Modern rate estimates use maximum-likelihood fits of the full distribution of mutant counts rather than the zero class alone. The two references are link-only. The stem-cell figure comes from the paper's abstract; the 1943 paper was checked for its record and title, but its scanned text was not read for this lesson, which describes the experiment in standard textbook terms.

# Three-point mapping: gene order, map distance, interference and why distances do not simply add

Two-point crosses give a recombination fraction for a pair of loci, but they leave gene order ambiguous and they undercount crossovers between distant loci. A three-point testcross solves both problems in one experiment. This lesson works through a synthetic three-point cross from raw progeny counts to an ordered map, measures crossover interference, and shows why observed recombination between the outer loci falls short of the sum of the two intervals.

## Learning objectives

By the end of this lesson, you should be able to:

1. Determine gene order and interval recombination fractions from three-point testcross progeny counts.
2. Calculate expected double crossovers, the coefficient of coincidence and interference.
3. Evaluate why observed recombination underestimates map distance for distant loci and apply a map function to correct it.

## The cross

A fly heterozygous at three linked loci, with one chromosome carrying the wild-type alleles (+ + +) and the other carrying the mutant alleles (a b c), is crossed to a fly homozygous for all three recessive alleles. Because the tester contributes only recessive alleles, each progeny phenotype directly reveals the chromosome the heterozygous parent transmitted. That is the point of a testcross: phenotype classes are gamete classes.

**Synthetic progeny (1000 flies):**

| Class | Count | Interpretation |
|---|---|---|
| + + + | 395 | parental |
| a b c | 387 | parental |
| a + + | 52 | single crossover, region I (a–b) |
| + b c | 54 | single crossover, region I (a–b) |
| + + c | 50 | single crossover, region II (b–c) |
| a b + | 54 | single crossover, region II (b–c) |
| + b + | 4 | double crossover |
| a + c | 4 | double crossover |

## Step 1: find the parental and double-crossover classes

The two most frequent classes are the parental (non-recombinant) chromosomes: + + + and a b c. The two rarest classes are the double crossovers, because a double crossover needs two independent exchanges: + b + and a + c.

## Step 2: determine order

Compare a double-crossover class with the parental class it most resembles. + b + differs from + + + only at b; a + c differs from a b c only at b. A double crossover swaps the middle locus while leaving the outer two in their parental combination, so **b is in the middle** and the order is a–b–c. If you had assumed a different order, the rarest classes would not fit a double exchange.

## Step 3: interval distances

Recombination between a and b includes every progeny with a crossover in that interval: the region I single crossovers plus the double crossovers, which have one exchange in each interval.

- r(a–b) = (106 + 8) / 1000 = 0.114, or 11.4 cM
- r(b–c) = (104 + 8) / 1000 = 0.112, or 11.2 cM

The map distance a–c is the sum, 22.6 cM.

## Step 4: interference

If crossovers in the two intervals were independent, double crossovers would occur at r(a–b) × r(b–c) × N = 0.114 × 0.112 × 1000 = 12.8 progeny. Only 8 were observed. The **coefficient of coincidence** is observed/expected = 0.63, and **interference** I = 1 − 0.63 = 0.37: one crossover reduces the chance of another nearby. Positive interference is typical in many organisms and is one reason map distances are not perfectly additive at the level of observed fractions.

## Why distances do not simply add

Looking only at the outer loci, a and c appear recombinant in the single-crossover classes but not in the double-crossover classes, where they kept their parental combination. The observed a–c recombination fraction is (106 + 104) / 1000 = 0.210, smaller than the 0.226 obtained by summing intervals. Over long distances this undercount grows, and the observed fraction can never exceed 0.5, however far apart two loci are.

**Map functions** convert an observed fraction into an additive distance under a model of crossover distribution. Haldane's function assumes no interference: d = −½ ln(1 − 2r) Morgans. For r = 0.210, d = 27.2 cM. It overcorrects here, because Haldane assumes no interference while this cross shows substantial interference; Kosambi's function allows for some interference and gives intermediate values. The choice of function is a modeling assumption that should be stated with the map.

## Worked example

**Problem.** In a separate synthetic cross with order x–y–z, r(x–y) = 0.20 and r(y–z) = 0.15 in 2,000 progeny, and 36 double crossovers are observed. What are the expected double crossovers, the coefficient of coincidence and the interference?

**Step 1.** Expected = 0.20 × 0.15 × 2,000 = 60.

**Step 2.** Coefficient of coincidence = 36/60 = 0.60.

**Step 3.** Interference = 1 − 0.60 = 0.40. Forty percent fewer double crossovers occurred than independence predicts. A map built from these data should report interval distances, not the directly observed x–z fraction, as the additive measure.

## Limits of this lesson

All counts are synthetic. Real mapping uses many markers and likelihood methods, accounts for genotyping error and segregation distortion, and in humans relies on pedigrees or population data rather than designed testcrosses.

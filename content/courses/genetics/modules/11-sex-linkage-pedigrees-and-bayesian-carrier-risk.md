# Sex-linked inheritance, pedigrees and Bayesian carrier risk

Genes on the X chromosome are inherited differently in males and females, and that difference leaves recognizable patterns in family trees. Those patterns let geneticists estimate the chance that a relative carries a variant before any test is done, and conditional probability lets the estimate improve as more of the family is observed. This lesson covers X-linked inheritance, reads pedigrees for it, and then uses Bayes' rule to update a carrier probability, which is the reasoning behind risk estimates in genetic counselling. All families and numbers here are synthetic.

## Learning objectives

By the end of this lesson, you should be able to:

1. Recognize X-linked recessive and dominant inheritance in pedigrees and compute transmission probabilities to sons and daughters.
2. Update a carrier probability with Bayes' rule using the evidence of unaffected sons.
3. Evaluate how incomplete penetrance, new mutations and X-inactivation complicate pedigree inference.

## X-linked transmission

In mammals, females have two X chromosomes and males have one X and one Y. A male passes his X to every daughter and his Y to every son, so **X-linked traits are never transmitted from father to son** (for genes outside the small pseudoautosomal regions that X and Y share). A female passes one of her two X chromosomes, chosen at random, to each child.

For an **X-linked recessive** allele, a male with one copy is affected (he is hemizygous: no second X to compensate). A female with one copy is usually an unaffected carrier. A carrier mother and an unaffected father therefore have, for each pregnancy:

- each son: probability 1/2 affected;
- each daughter: probability 1/2 carrier, and usually unaffected.

An affected father and a non-carrier mother have no affected children, but every daughter is an obligate carrier. Typical X-linked recessive pedigrees show affected males in several generations, connected through unaffected females, with no male-to-male transmission.

For an **X-linked dominant** allele, an affected father passes the trait to all daughters and no sons, and an affected heterozygous mother passes it to half of her children of either sex. Y-linked traits pass from father to all sons. Mitochondrial DNA is transmitted through mothers.

## Prior probability from the pedigree

**Synthetic family:** a woman's brother has an X-linked recessive condition with complete penetrance, and their mother is known to be a carrier. Before considering anything about her own children, the woman inherited either her mother's normal X or the variant X, each with probability 1/2. Her **prior** probability of being a carrier is 1/2.

## Updating with Bayes' rule

She has three sons, all unaffected. If she is a carrier, each son independently had probability 1/2 of being unaffected, so three unaffected sons have probability (1/2)³ = 1/8. If she is not a carrier, three unaffected sons are certain (probability 1). Bayes' rule weighs each hypothesis by prior × likelihood:

| Hypothesis | Prior | Likelihood of 3 unaffected sons | Joint |
|---|---|---|---|
| Carrier | 1/2 | 1/8 | 1/16 |
| Not a carrier | 1/2 | 1 | 1/2 |

The **posterior** carrier probability is (1/16) / (1/16 + 1/2) = 1/9 ≈ 0.111. The unaffected sons do not rule out carrier status, but they make it much less likely. The risk that her next son is affected is 1/9 × 1/2 = 1/18 ≈ 0.056, far below the 1/4 that the prior alone would give.

## Complications

- **Incomplete penetrance.** If only 80% of hemizygous males show the condition, an unaffected son is weaker evidence: a carrier's son is unaffected with probability 1 − 1/2 × 0.8 = 0.6, not 1/2. With three unaffected sons the posterior becomes 0.178 instead of 1/9.
- **New mutations.** For conditions that greatly reduce reproduction, a substantial fraction of affected males carry a new mutation, so the mother of an isolated case is not always a carrier (although a mutation present only in part of her germline can still give her a recurrence risk). Her prior must then come from population models, not simply 1.
- **X-inactivation.** In the early cells of a female embryo one X chromosome is silenced at random, and the choice is inherited by that cell's descendants. Carriers are therefore mosaics. If, by chance, the X carrying the normal allele is silenced in most cells of a tissue (skewed X-inactivation), a carrier can show symptoms. This is one reason "carrier" does not always mean "unaffected".
- **Uncertain diagnoses** in relatives change the prior itself.

## Common mistakes

- Expecting an X-linked recessive trait to pass from father to son.
- Treating unaffected sons as proof that a woman is not a carrier, instead of as evidence that lowers the probability.
- Multiplying the prior by the likelihood but forgetting to divide by the total over both hypotheses.
- Using the prior risk (1/2 × 1/2 = 1/4 per son) after the family has supplied conditional information.
- Ignoring penetrance when it is below 100%.

## Worked example

**Problem.** In a second synthetic family the woman's prior carrier probability is also 1/2 (her mother is a carrier), and she has two unaffected sons. What is her posterior probability of being a carrier, and what is the risk for her next son?

**Step 1: likelihoods.** Carrier: (1/2)² = 1/4. Not a carrier: 1.

**Step 2: joint probabilities.** Carrier: 1/2 × 1/4 = 1/8. Not a carrier: 1/2 × 1 = 1/2.

**Step 3: normalize.** Posterior = (1/8)/(1/8 + 1/2) = 1/5 = 0.20. The next son's risk is 1/5 × 1/2 = 1/10.

**Step 4: state the assumptions.** Complete penetrance, a known carrier mother, accurate diagnoses and independent pregnancies. Any of these failing changes the numbers, which is why such estimates come with stated assumptions.

## Limits of this lesson

All families are synthetic, and the lesson is not genetic-counselling advice for any person. Real risk estimates use complete pedigrees, test results with known error rates and population data on new mutations, and they are made by qualified professionals.

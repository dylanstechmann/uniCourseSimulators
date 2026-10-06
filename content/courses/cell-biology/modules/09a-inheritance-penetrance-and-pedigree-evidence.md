# Inheritance, penetrance, and pedigree evidence

A DNA variant is transmitted through a reproductive process, but its transmission probability is not the same as the probability of a phenotype. To reason from genotype to phenotype, keep the genetic model, the observed family, the phenotype definition, and uncertainty separate. Pedigrees are evidence under assumptions; a familiar pattern is not by itself proof of a molecular mechanism.

## Learning objectives

By the end of this lesson, you should be able to:

1. Calculate allele-transmission and phenotype probabilities under an explicitly specified Mendelian model.
2. Distinguish dominance, penetrance, and expressivity and interpret a pedigree with age, ascertainment, and sample-size limits.
3. Explain how population structure, linkage, environment, and selection can complicate a genotype–phenotype association.

## Terms that answer different questions

An **allele** is one sequence form at a locus; a **genotype** describes the alleles carried by an individual at one or more loci. A **phenotype** is an observed measurement or trait, which needs an operational definition: what was measured, when, using which threshold, and by whom? “Affected” in a family diagram is not a measurement protocol.

In a diploid organism, a heterozygote carries two different alleles at a locus. **Dominance** describes how the heterozygote's phenotype compares with the two homozygous phenotypes under a stated trait model. It does not mean that one allele is more common, stronger, or molecularly dominant in every assay. A recessive phenotype can arise from loss of sufficient function when one functional copy supplies enough product; a dominant phenotype can arise through haploinsufficiency, altered dosage, dominant-negative interaction, gain of function, or another mechanism. The inheritance pattern alone does not choose among those mechanisms.

**Penetrance** is the probability of an operationally defined phenotype among people with a specified genotype under stated conditions and over a stated age range. **Expressivity** describes how strongly or in what form a phenotype appears among individuals who express it. Penetrance and expressivity can depend on age, environment, sex, other genetic variants, ascertainment, and the measurement used. The phrase “the variant is 80% penetrant” is incomplete unless the population, phenotype, age, and observation conditions are clear.

## Separate allele transmission from phenotypic expression

Suppose a parent is heterozygous `A/a` and the other parent is `a/a`. Under ordinary Mendelian segregation, no segregation distortion, and a correctly identified genotype, each conception has probability `1/2` of inheriting `A`. That is a transmission probability. If a specified phenotype has penetrance `0.80` among carriers by a given age, the simple model gives:

`P(phenotype) = P(inherit A) × P(phenotype | inherit A) = 0.50 × 0.80 = 0.40`.

This is a 40% model-based probability for the phenotype, not 40% probability of inheriting the allele. It assumes the noncarrier phenotype rate is zero, the penetrance estimate applies to the child, the phenotype is assessed by the stated age, and the genotype has no interaction with another relevant locus or exposure. A real clinical risk estimate requires evidence and may differ substantially.

For two heterozygous parents at a single autosomal locus, the simple genotype probabilities are `1/4 A/A`, `1/2 A/a`, and `1/4 a/a`. These are probabilities for each conception, not a promise that four siblings will contain exactly one, two, and one of those genotypes. Outcomes among siblings are not forced to match a Punnett-square ratio in a small family. For linked loci, inheritance is not the product of independent allele probabilities; recombination and phase matter.

## Read a pedigree as a conditional data summary

Consider an explicitly **synthetic teaching example**: a candidate heterozygous allele is confirmed in five adult relatives; four meet a predeclared clinical measurement threshold, and one carrier is age 22 while the condition is usually assessed after age 40. A first descriptive fraction is `4/5 = 0.80`, or 80% affected among these five observed carriers. It is not automatically an estimate of lifelong penetrance. The younger carrier has not reached the comparison age; the pedigree was found because one affected family member was referred; unaffected carriers might not have been tested; and a similar phenotype can have non-genetic causes.

A useful family analysis records genotypes rather than inferring them from appearance, defines how the phenotype was measured, records age and exposure, includes relatives regardless of outcome when possible, and distinguishes confirmed from inferred genotypes. Independent biological units are people, not multiple clinical measurements from the same person. Relatives also share ancestry and environment, so five relatives are not equivalent to five randomly sampled, independent population observations.

Segregation can add evidence: does the candidate genotype track with a defined phenotype across informative relatives? But small pedigrees are compatible with many models. Reduced penetrance, variable expression, a phenocopy, a second locus, age-dependent onset, incorrect diagnosis, and chance segregation can all alter the apparent pattern. A de novo variant in one affected child may strengthen a hypothesis, but parental mosaicism, technical confirmation, and phenotype specificity still matter.

## Association is not a molecular cause

In a population study, an allele may be more frequent in people with a trait without directly causing it. The allele could be inherited with a nearby causal variant through **linkage disequilibrium**. Differences in ancestry or recruitment can change both allele frequency and phenotype frequency, creating **population stratification**. Family-based comparisons, ancestry-aware design and analysis, independent replication, and functional follow-up can address different alternatives, but no single adjustment makes all confounding disappear.

An observed association is a relation between measured variables in a defined sample. A functional effect is a change in a molecular readout under an experimental condition. A causal claim about an organism-level phenotype connects these levels and requires evidence that addresses competing explanations. Keep the scope of each claim at the level actually measured.

### Worked probability example

For one `A/a` parent and one `a/a` parent, inheritance of `A` is `1/2`. If the stated penetrance among `A/a` carriers by age 40 is `0.80`, then the simple predicted probability of meeting the phenotype definition by age 40 is `0.5 × 0.8 = 0.40`. If noncarriers can also meet the phenotype definition, add that branch: `P(phenotype) = P(carrier)P(phenotype|carrier) + P(noncarrier)P(phenotype|noncarrier)`. Do not silently set the second term to zero unless the model states it.

## Check your reasoning

When a pedigree shows a 1:1 count among four siblings, does that establish a 50% population penetrance? Which probability refers to transmission, and which is conditional on carrying the allele? What information about age, ascertainment, phenotype definition, and unaffected relatives would change your interpretation?

## Provenance

This lesson and all examples are original CC BY 4.0 content. MIT OCW 7.01SC Genetics is a link-only curriculum comparator. NCBI Bookshelf sources in the registry are link-only references; no family diagram, wording, question, or dataset is copied or adapted.

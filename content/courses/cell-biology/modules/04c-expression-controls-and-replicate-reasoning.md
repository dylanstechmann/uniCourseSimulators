# Gene expression, controls and replicate-level reasoning

Original CC BY 4.0 instructional draft with substantial Codex assistance; unreviewed. This extends the preserved [compact expression reading](04-gene-expression-and-experimental-logic.md) and connects [chromatin evidence](07a-chromatin-accessibility-and-regulatory-dna.md), [RNA processing](08a-rna-processing-and-isoform-evidence.md) and [translation/turnover](08b-translation-and-protein-turnover.md). Examples are fictional teaching inputs. They are neither laboratory instructions nor clinical results.

## Information flow is a sequence of distinct measurements

In the introductory model, a DNA template supplies sequence information for an RNA transcript, and a ribosome reads a mature messenger RNA frame to synthesize a polypeptide. The template strand and synthesized RNA are antiparallel; RNA polymerization extends the new chain at its 3-prime end. Ribosomes read mRNA codons 5-prime to 3-prime, with peptide growth from amino to carboxyl end. In many eukaryotic transcripts, capping, splicing and 3-prime processing intervene between initial transcription and the mature RNA that is measured or translated.

These relationships do not mean every RNA is translated or every information-transfer process is identical. Ribosomal and transfer RNAs have roles beyond serving as protein-coding templates; reverse transcription transfers sequence information from RNA to DNA in particular systems. The simplified DNA-to-RNA-to-protein arrow is a useful starting model with a declared scope, rather than an assertion that all RNA measurements directly measure protein production.

Regulation can act at chromatin accessibility, transcription initiation, RNA processing/stability, translation, protein turnover and localization. A higher steady-state mature RNA signal could reflect greater production, slower decay, different composition, recovery or cell number. A higher protein signal might reflect synthesis, degradation, extraction, inactive material or compartment distribution. Trace the measurement chain before choosing a mechanism.

As a stipulated steady-state amount model, P=s/k when constant synthesis s balances first-order protein loss k. If s is halved and k remains constant, predicted P is halved. If k is also halved, predicted P is unchanged. Neither result demonstrates that the system has reached steady state or that the first-order model applies. Nascent-label and decay-cohort measurements can test different parts of this model; each needs its own loading, timing and detection assumptions.

## Controls address named alternatives

A positive control tests whether the assay can detect a known signal in the relevant run and range. A negative control estimates background or nonspecific signal. An input/loading measurement helps identify unequal material. A recovery reference addresses a specified loss process. A perturbation/control comparison tests an intervention-associated difference, while introduction and rescue/correction can strengthen a hypothesis under their own specificity assumptions. An orthogonal assay checks another link in the chain.

These roles overlap only when justified by the design. A bright positive control does not prove that experimental cultures contain equal protein. A no-reverse-transcriptase RNA control addresses DNA-derived amplification, not whether extraction recovery is equal. A housekeeping signal can change with condition; its name does not establish a stable denominator. Rescue may restore a phenotype through a bypass or change another factor, so restoration is supportive evidence rather than a guarantee of one native route or absence of off-target effects.

For a negative result, ask whether a positive control passed, the assay range was sufficient, the intervention engaged its target and the relevant material was recovered. Absence of detected signal is bounded by sensitivity and these conditions. It is not automatically biological absence. For a positive result, ask whether background, nonspecific signal, normalization or selection can explain it before assigning a mechanism.

## An original culture-level example

Three separately prepared cultures per condition each have a background-corrected reporter and a matched input signal. Each culture's two technical wells were averaged before reporting:

| Condition | Culture | Reporter (AU) | Input (AU) | Reporter/input ratio |
| --- | --- | --- | --- | --- |
| Reference | R1 | 40 | 20 | 2.0 |
| Reference | R2 | 60 | 20 | 3.0 |
| Reference | R3 | 80 | 40 | 2.0 |
| Perturbed | P1 | 60 | 20 | 3.0 |
| Perturbed | P2 | 90 | 30 | 3.0 |
| Perturbed | P3 | 160 | 40 | 4.0 |

The equal-culture ratio mean is `(2+3+2)/3=7/3`, about 2.33, for reference and `(3+3+4)/3=10/3`, about 3.33, for perturbed. Their descriptive difference is 1.00 ratio unit. Each group has three independent cultures, not six independent wells. Numeric suffixes do not create paired cultures across conditions; pairing would need a design such as a shared preparation split between assignments.

The pooled reference reporter/input ratio is `(40+60+80)/(20+20+40)=2.25`, which differs from the equal-culture mean. Pooling weights cultures by input and asks a different question. The requested analysis must state whether its target is an equally weighted culture response or an input-weighted bulk response. Neither calculation can be silently substituted for the other. The numerical difference also has no calibrated uncertainty or significance claim here.

Suppose the perturbed cultures also have lower viability and more reporter per recovered cell. That observation cannot establish whether reporter production rose in the original population, whether recovery changed or whether surviving cells represent a selected subset. A viable-cell denominator defines a measurement among recovered viable cells; it does not profile cells lost before measurement. This is why cell counts and fate/selection measurements matter when comparing molecular layers.

## Build a testable next step

Start with a bounded hypothesis: “The perturbation changes recovered reporter/input ratio under these conditions.” List a specific alternative such as changed RNA stability, protein turnover, input-reference regulation or survivor selection. Select a measurement that separates the proposed mechanism from that alternative: mature/precursor RNA and a production/decay assay; nascent-protein and matched decay-cohort measurements; an independent input reference; or longitudinal viable/lost-cell accounting. State the independent culture unit, matched timing, perturbation control, positive/negative controls and how the result would alter the conclusion.

The claim “this intervention raises transcription” requires stronger evidence than an endpoint reporter increase. A plasmid reporter is a sequence/context assay, not direct proof of endogenous locus necessity. Occupancy-associated evidence does not alone establish direct binding. A marker signature is separate from defined mature function. Keep these distinctions when integrating later course weeks.

## Reasoning checks with feedback

1. How many biological units per condition does the table supply? **Three independent cultures.** Technical wells improve measurement within each culture but do not create additional cultures.
2. Can the positive assay control replace the input control? **No.** They address detectability and material normalization, respectively.
3. Is the pooled ratio numerically identical to the mean of culture ratios? **No in this example.** The input values give unequal weighting.
4. Does an endpoint protein increase uniquely identify increased transcription? **No.** The information-flow chain contains multiple regulated steps and measurement alternatives.

Explain the denominator, unit, transformation, control role and inferential limit when answering. Public study feedback does not grade written design, prove retention or replace qualified course review.

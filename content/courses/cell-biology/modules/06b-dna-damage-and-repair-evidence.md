# DNA damage, repair pathways, and evidence of lesion removal

A DNA sequence difference, a replication mismatch, and a chemically damaged base are related but distinct events. Cells use overlapping pathways to preserve DNA, tolerate lesions, or join broken molecules. Choosing a repair explanation requires identifying the lesion, the replication context, the measurement, and its controls. A reduction in a lesion-associated signal is not automatically proof of error-free repair or a measured mutation rate.

## Learning objectives

By the end of this lesson, you should be able to:

1. Distinguish polymerase proofreading from post-replicative mismatch repair and match common lesion classes to plausible repair routes.
2. Compare homologous-recombination and end-joining strategies for double-strand breaks while stating cell-cycle and fidelity limits.
3. Analyze an explicitly synthetic lesion-removal time course using initial burden, perturbation, recovery, rescue, and replicate evidence.
4. State why lesion removal, DNA synthesis, cell survival, and mutation frequency are different outcomes.

## Find the error or lesion before naming a pathway

Proofreading occurs during synthesis when a replicative polymerase transfers a newly mispaired 3′ end to an exonuclease site and removes the latest incorrect nucleotide. Mismatch repair acts after an error escapes that immediate correction; it recognizes a mismatched base pair and must target the newly synthesized strand. The strand-discrimination signal differs among organisms, so one bacterial example should not be treated as a universal eukaryotic mechanism.

Damage-repair pathways recognize properties of a chemical lesion or the resulting DNA distortion. Base-excision repair commonly removes a small damaged base, such as an oxidized or deaminated base, and processes the resulting abasic site. Nucleotide-excision repair removes a short DNA segment containing many bulky, helix-distorting lesions, including common ultraviolet photoproducts. Direct reversal repairs particular chemical modifications without replacing a tract of DNA, but the available enzymes and substrates are organism-specific.

A broken chromosome end creates another problem. Homologous recombination copies information from a homologous template and is favored when a sister chromatid is available, often in S/G2 in eukaryotic cells. Nonhomologous end joining reconnects broken ends without requiring an extended homologous template; end processing can create small insertions or deletions, although the exact outcome depends on the break and pathway. Translesion synthesis is lesion bypass by specialized polymerases: it can permit replication to continue but is not synonymous with removing the original lesion or restoring the original sequence.

| Observation or lesion class | Candidate process to test | Important boundary |
| --- | --- | --- |
| Newly incorporated wrong base at an extending polymerase | Polymerase proofreading | Immediate correction at a growing 3′ end; it does not explain every later mismatch |
| Mismatch or small insertion/deletion loop remaining behind a fork | Mismatch repair | Requires discrimination of the newly synthesized strand in that organism |
| Small chemically altered base | Base-excision repair | Lesion identity and glycosylase specificity matter |
| Bulky helix-distorting UV photoproduct | Nucleotide-excision repair | A lesion signal can change for reasons other than excision; measure DNA and cell recovery |
| Double-strand break | Homologous recombination or end joining | Template availability, cell-cycle state, sequence context, and the exact product matter |

Pathway choice is not a one-to-one glossary. Replication stress, chromatin, lesion position, cell-cycle state, enzyme abundance, and experimental perturbations can change which route is used. A bypass pathway may trade immediate fork progression for increased risk of a sequence change; cells may also stop cycling or die rather than complete repair.

## Synthetic time-course: a repair factor perturbation

The table below contains **synthetic teaching data**, not observations from an experiment or published study. A lesion-specific signal is normalized per fixed amount of recovered genomic DNA after a matched UV exposure. Each value is the mean ± standard deviation from four independently cultured samples. Values at time zero are similar; the later signal remains higher after depletion of a candidate nucleotide-excision-repair factor and decreases again after a perturbation-resistant rescue is supplied.

| Condition | Immediately after UV, 0 h | After recovery, 4 h |
| --- | ---: | ---: |
| Non-targeting control | 100 ± 7 | 31 ± 6 |
| Candidate NER-factor depletion | 98 ± 8 | 79 ± 9 |
| Depletion plus matched rescue | 101 ± 6 | 34 ± 7 |

The common starting signal makes a difference in initial lesion burden less likely to explain the later contrast. The rescue strengthens the inference that the targeted factor contributes to the measured decline under these conditions. The data are **consistent with a role in removing this lesion signal**, but they do not establish that every lesion was repaired, that the repaired sequence is error-free, or that the same result occurs in every cell type.

A rigorous design also measures cell number and viability, cell-cycle distribution, genomic DNA recovery and loading, exposure matching, non-UV baseline, perturbation efficiency, and rescue expression. If DNA replicates during recovery, dilution by newly synthesized DNA may change lesion signal per genome. If damaged cells die or detach, the remaining sample may be biased. An orthogonal lesion assay and a mutation-frequency assay address different steps and should not be substituted for one another.

**Worked interpretation.** In this constructed table, the depletion condition begins near the controls at time zero but has a higher lesion-associated signal at four hours; the matched rescue moves the later signal toward the control. This supports a factor-dependent change in this assay. It does not alone prove direct catalytic action, identify every intermediate, or show that surviving DNA is mutation-free. A next experiment could measure repair synthesis or a defined sequence outcome while keeping DNA amount, viability, and cell-cycle state matched.

### Check your reasoning

Which pathway is a first candidate for a bulky UV photoproduct, and which process corrects a mismatch that escaped polymerase proofreading? In the table, what does the rescue add to the interpretation, and what additional assay would be needed to estimate mutations rather than lesion-associated signal?

## Provenance

This is original explanatory text with original synthetic data under the course’s CC BY 4.0 content license. MIT OpenCourseWare 7.28x Molecular Biology is linked as an undergraduate/graduate scope comparator. NCBI Bookshelf chapters on DNA replication and DNA repair are link-only textbook references. No source text, figure, table, or assay result is copied or adapted.

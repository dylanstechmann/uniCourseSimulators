# Transcription-factor occupancy and reporter evidence

An experiment on gene regulation often combines an association assay with a functional perturbation. Chromatin immunoprecipitation (ChIP) can enrich genomic regions cross-linked to a protein complex, while a reporter tests how a DNA fragment affects an engineered construct. Neither result alone demonstrates that a factor directly activates a particular endogenous gene. Controls and claim boundaries determine what the evidence can support.

## Learning objectives

By the end of this lesson, you should be able to:

1. Calculate a simplified percent-input value from a ChIP-qPCR input aliquot and immunoprecipitated sample, stating the amplification-efficiency assumption.
2. Select ChIP and qPCR controls that separately address input abundance, nonspecific pull-down, locus specificity, and assay contamination.
3. Interpret matched wild-type and motif-disrupted reporter constructs with promoter-only and positive controls.
4. Distinguish protein occupancy, reporter activity, endogenous regulatory causation, and direct biochemical binding as different claims.

## ChIP-qPCR measures enrichment in a prepared sample

In a typical ChIP experiment, chromatin is fixed or otherwise prepared, fragmented, incubated with an antibody, and recovered with associated DNA. qPCR primers then amplify a chosen region. Enrichment can be expressed as percent input, fold over an antibody control, or another justified normalization. These measures answer different questions and should name their denominator.

For a simplified percent-input calculation with ideal doubling efficiency, let `f` be the fraction of starting chromatin saved as the input aliquot. If that aliquot has threshold cycle `Cq_input` and the ChIP sample has `Cq_IP`, then:

`% input = 100 × f × 2^(Cq_input − Cq_IP)`

If a 1% input aliquot (`f = 0.01`) reaches threshold at cycle 25 and the ChIP sample at cycle 22, the estimate is `100 × 0.01 × 2^3 = 8% input`. This simplified comparison assumes near-100% amplification efficiency and the same well-behaved amplicon in both samples. Real analyses must document input dilution, primer efficiency, DNA recovery, and their chosen normalization; a percent-input value is not an absolute count of bound molecules or a direct measure of transcription.

Controls have distinct roles. **Input chromatin** is a pre-immunoprecipitation aliquot that helps normalize the amount and representation of starting material. A matched **IgG or mock immunoprecipitation** estimates nonspecific recovery under that pull-down procedure. A known positive locus checks whether the antibody and assay can detect an expected target; a negative locus tests locus specificity. A no-template qPCR control detects reagent contamination or primer artifacts. None substitutes for the others. Antibody validation, matched chromatin preparation, DNA fragment quality, biological replicates, and transparent reporting are also needed. Multiple PCR wells from one culture are technical replicates, not independent biological samples.

ChIP recovery means that a DNA fragment was enriched with the antibody under the assay conditions. Cross-linking can capture proteins that associate indirectly through a complex; enrichment does not necessarily show direct base-specific binding. Nor does occupancy prove that binding changes transcription, that a nearby gene is the target, or that the factor acts only at that locus.

## Reporter constructs test sequence activity in an engineered context

A reporter places a candidate regulatory sequence with a promoter and a measurable output such as luciferase. Comparing wild-type sequence with a motif-disrupted version can test whether that sequence contributes to reporter output in a chosen cell line and condition. A promoter-only construct estimates baseline; a validated positive regulatory sequence tests assay responsiveness. A co-transfected reference reporter can normalize transfection and recovery only if the reference itself is not affected by the treatment. Viability, construct identity, equal DNA amount, and biological transfections still need checking.

A plasmid has different copy number, chromatinization, genomic position, and neighboring regulatory context from the endogenous chromosome. A reporter result therefore demonstrates activity of the tested construct in that assay, not that the element regulates its predicted endogenous target. Mutating a motif may also change overlapping motifs or DNA structure. A precise edit at the native locus, multiple independent perturbations, a matched non-targeting or nearby neutral control, and rescue strengthen a causal claim. Measuring endogenous nascent or mature RNA and nearby genes helps identify what changed; orthogonal occupancy or accessibility assays can test a different link in the model.

## Synthetic occupancy and reporter data

The tables below are **synthetic teaching data**. Four independent cultures or transfections were measured per condition; values are mean ± standard deviation. ChIP values are simplified percent-input estimates under the assumptions above. Reporter values are firefly/renilla ratios normalized to the promoter-only mean. They are not published results.

| ChIP-qPCR region/control | Target-factor antibody, % input | Matched IgG, % input |
| --- | ---: | ---: |
| Candidate enhancer | 8.0 ± 1.2 | 0.5 ± 0.2 |
| Known positive locus | 10.0 ± 1.5 | 0.6 ± 0.2 |
| Unrelated negative locus | 0.7 ± 0.2 | 0.5 ± 0.2 |

| Reporter construct | Relative normalized signal |
| --- | ---: |
| Promoter only | 1.0 ± 0.2 |
| Candidate enhancer, wild type | 7.8 ± 1.1 |
| Candidate enhancer, motif disrupted | 2.4 ± 0.6 |
| Validated positive enhancer | 9.0 ± 1.4 |

The candidate region's ChIP enrichment over matched IgG and the unrelated locus is consistent with occupancy of the cross-linked factor-containing complex in this assay. The positive locus makes a complete assay failure less likely. The reporter's wild-type signal above promoter-only, and its decrease after the motif disruption, support a contribution of that sequence to the reporter construct. Because the values are synthetic and the construct is not at the endogenous chromosome, neither table proves direct binding, the identity of the regulated gene, or a change in native transcription.

### Integrated next experiment

To test whether the candidate motif contributes to the endogenous gene's transcription, introduce a precise motif edit or use a validated local repression strategy, compare independent perturbations with non-targeting and nearby neutral controls, verify edit or repression efficiency, and measure endogenous nascent RNA plus nearby genes in independent cultures. A restoration or rescue experiment can test reversibility. Monitor viability and cell-state composition so that a general state shift is not mistaken for a locus-specific effect. ChIP, reporter, RNA, and rescue each test different links; agreement strengthens a model but does not make every hidden step directly observed.

### Check your reasoning

What does input normalize that IgG does not? What does a no-template qPCR well test? If ChIP enrichment and reporter activity both rise, what additional experiment would support a causal effect at the endogenous locus?

## Provenance

This is original explanatory text with original synthetic tables under the course's CC BY 4.0 content license. MIT OpenCourseWare 7.28x Molecular Biology is a link-only curriculum comparator. Haring et al. (2007), the NCBI Bookshelf transcription-regulation chapter, and ENCODE ChIP-seq standards are linked as methods references; the lesson does not reproduce or adapt them. The Haring paper is separately identified in the source registry with its stated CC BY 2.0 license, but no article material is reused.

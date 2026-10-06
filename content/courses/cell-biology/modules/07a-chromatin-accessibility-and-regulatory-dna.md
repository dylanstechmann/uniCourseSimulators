# Chromatin accessibility and regulatory DNA

The eukaryotic genome is not a naked DNA template. DNA associates with histones and many other proteins, and cells regulate transcription partly by changing the access and local organization of that material. A useful model must connect molecular structure to a measured chromatin property while keeping association separate from causation.

## Learning objectives

By the end of this lesson, you should be able to:

1. Describe a nucleosome and explain how nucleosome occupancy, positioning, remodeling, and histone modification can alter DNA access.
2. Distinguish promoters and distal cis-regulatory elements from trans-acting regulators and explain why genomic proximity alone does not identify a functional target gene.
3. Interpret synthetic accessibility and RNA measurements across cell states, including biological replication and limits on causal claims.
4. Propose a perturbation and rescue that tests whether a candidate regulatory element contributes to endogenous transcription.

## DNA packaged into a dynamic template

Roughly 147 base pairs of DNA wrap around a histone octamer made from two copies each of H2A, H2B, H3, and H4 to form the nucleosome core particle. Linker DNA and histone H1 contribute to higher-order organization. Nucleosomes are not fixed beads spaced identically across every gene: their occupancy and position can change with DNA sequence, transcription factors, ATP-dependent remodeling complexes, histone chaperones, and transcription itself.

The term **chromatin accessibility** describes how readily a region can be contacted by a particular protein or enzyme under defined conditions. It is not one universal state. An assay may report transposase insertion, nuclease cleavage, or protein occupancy; each depends on its own chemistry, cell preparation, and analysis. A region that is more accessible on average is not automatically transcribed, and an inaccessible bulk signal can conceal a responsive subpopulation.

Histone modifications can alter charge, recruit reader proteins, or influence interactions among chromatin components. For example, acetylation of histone lysines is often associated with active promoters or enhancers, while H3K4me3 is often enriched near active promoters and H3K27me3 with Polycomb-associated repression. These are context-dependent associations, not universal switches or direct measurements of RNA output. Enzymes that write, erase, or recognize marks may affect many loci and other substrates. CpG DNA methylation can correlate with repression in some promoter contexts, but its interpretation depends on sequence, cell type, and the proteins that recognize it.

## Cis elements work in a trans environment

A **promoter** is a DNA region where the transcription machinery assembles near a transcription start site. General transcription factors and RNA polymerase II form a pre-initiation complex; sequence-specific transcription factors and co-regulators can change recruitment, initiation, or later steps. **Enhancers** and silencers are cis-acting sequences that can influence a promoter from nearby or distant positions. Their action can depend on orientation, spacing, cell state, chromatin, and combinations of motifs. A transcription factor or cofactor acting on those sequences is a trans-acting regulator.

Enhancer-promoter communication can involve chromatin contacts and protein complexes, but a measured contact alone does not show that an enhancer changes a gene's transcription. The nearest gene is a candidate, not a guaranteed target. A functional claim needs a perturbation tied to an endogenous measurement, with controls for effects on neighboring genes, cell state, and general transcription.

## Synthetic cell-state comparison

The following values are **synthetic teaching data**, not observations from a published experiment. Four independently cultured samples were measured in each cell state. Accessibility values are normalized transposase-insertion signal per million mapped fragments; transcript values are normalized RNA abundance in arbitrary units. Entries are mean ± standard deviation. The assay and units are defined here so that the measurements are not mistaken for absolute nucleosome counts.

| Region or readout | Differentiated state A, n = 4 | Progenitor-like state B, n = 4 |
| --- | ---: | ---: |
| Candidate promoter accessibility | 52 ± 8 | 12 ± 4 |
| Candidate distal enhancer accessibility | 78 ± 10 | 19 ± 5 |
| Candidate gene RNA abundance | 24 ± 5 | 5 ± 2 |
| Housekeeping promoter accessibility | 61 ± 8 | 58 ± 9 |

The candidate promoter and enhancer accessibility, and the candidate transcript, are higher in state A in this constructed example; the housekeeping promoter is similar. This pattern is consistent with a locus-specific relationship between chromatin accessibility and expression across these states. It does not establish that the enhancer causes the RNA difference: cell identity changed in many ways at once, and no regulatory element was perturbed. The independent culture is the biological replicate; additional qPCR wells or sequencing reads from one culture would not increase the biological sample size.

### Worked interpretation

Suppose a candidate enhancer is accessible in state A and the linked gene's RNA is also higher. The most defensible first statement is that these measurements co-vary across the tested states. To test enhancer contribution, perturb the endogenous element with a non-targeting control and more than one independent guide or edit; measure the target and nearby transcripts; verify perturbation and cell viability; and, where practical, rescue the sequence or regulatory activity. A reporter plasmid can add evidence about sequence function, but it does not reproduce the native locus by itself.

### Check your reasoning

Which measured quantity in the table is the accessibility proxy? Why does agreement between that quantity and RNA not prove enhancer causality? Name one perturbation, one matched control, and one endogenous readout that would improve the causal test.

## Provenance

This is original explanatory text with an original synthetic teaching table under the course's CC BY 4.0 content license. MIT OpenCourseWare 7.28x Molecular Biology is a link-only curriculum comparator. NCBI Bookshelf chapters on transcriptional regulation and genetic switches are link-only scientific references. No text, figure, table, or dataset is copied or adapted.

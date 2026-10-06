# RNA processing and isoform evidence

Eukaryotic gene expression includes a set of decisions between the first RNA copy and the mature RNA that reaches the cytoplasm. A useful experimental model must distinguish transcription, RNA processing, export, and RNA decay. An assay of total RNA abundance alone usually cannot identify which step changed.

## Learning objectives

By the end of this lesson, you should be able to:

1. Explain how capping, intron removal, alternative splicing, cleavage, and polyadenylation contribute to production and fate of many eukaryotic mRNAs.
2. Predict how a specified splice-site or splice-regulator perturbation could alter mature isoform proportions without requiring a change in total transcription.
3. Interpret RNA measurements using assay-matched controls and distinguish a change in transcript abundance from a change in isoform composition or RNA stability.

## From a primary transcript to an export-competent messenger RNA

For a typical protein-coding eukaryotic gene, RNA polymerase II makes a primary transcript that contains exons and introns. Processing is coordinated with transcription, although the timing and coupling differ among genes and cell contexts. The familiar 5′ cap, splice junctions, and 3′ end are not decorative labels: they recruit proteins that influence stability, quality control, export, translation, and localization.

### The 5′ cap

Soon after a nascent transcript emerges, a guanosine is joined to its 5′ end through an unusual 5′-to-5′ triphosphate linkage and is methylated to form the common 7-methylguanosine cap. Cap-binding factors help protect the exposed end from some exonucleases and participate in nuclear processing, export, and translation initiation. A capped RNA is not thereby guaranteed to be complete, correctly spliced, or translated at a fixed rate. Capping is one feature in a sequence of quality-control and regulatory steps.

### Spliceosome-mediated intron removal

The spliceosome is a dynamic ribonucleoprotein assembly. Small nuclear RNAs in snRNP particles base-pair with conserved regions of a pre-mRNA and help position the catalytic center. In a common major-spliceosome intron, recognition involves a 5′ splice site, a branch-point adenosine, a polypyrimidine tract, and a 3′ splice site. The reaction proceeds through two transesterification steps: the branch-point adenosine attacks the 5′ splice site to form a lariat intermediate, and the upstream exon’s new 3′ hydroxyl attacks the 3′ splice site to ligate exons. The intron is released and usually degraded.

Consensus motifs support recognition but are not an infallible barcode. Auxiliary RNA sequences, RNA-binding proteins, chromatin, transcription kinetics, and cell state can affect splice-site choice. A mutation near a splice site may cause exon skipping, intron retention, use of a cryptic site, or no detectable change. The sequence and measurements determine which conclusion is supported.

### Alternative splicing changes the mature RNA population

Alternative splicing can select different combinations of exons from the same primary-transcript region. The resulting isoforms may encode different protein sequences, change a reading frame, add a premature termination codon, alter untranslated regions, or be subject to different localization and decay. An isoform is not automatically a distinct functional protein: translation, folding, abundance, localization, and activity must be established separately.

Consider an exon included in one isoform and skipped in another. Primers crossing the inclusion-specific exon junction can estimate the included form; primers crossing the exon-to-exon junction created by skipping can estimate the skipped form. A primer pair in a shared constitutive exon estimates a shared region and may report total transcript signal, but its interpretation depends on amplification efficiency and which isoforms contain that exon. A standard end-point RT-qPCR band cannot reliably distinguish every isoform without appropriately placed primers or sequencing.

### Cleavage and the poly(A) tail

For many mRNAs, a processing complex recognizes sequence information near the 3′ end, cleaves the transcript downstream, and poly(A) polymerase adds a nontemplated tail of adenosines. Poly(A)-binding proteins interact with this tail and can influence protection, export, and translation. Alternative cleavage or polyadenylation can change the 3′ untranslated region while leaving the protein-coding sequence unchanged, thereby changing regulatory sites and RNA behavior. Some transcripts, including canonical replication-dependent histone mRNAs, are important exceptions to the common poly(A)-tail pattern.

Processing also participates in surveillance. Incompletely processed or aberrant transcripts may be retained and degraded; some premature stop-containing transcripts are recognized through nonsense-mediated decay during translation. Thus a splice change can alter mature RNA abundance through processing and subsequent surveillance, even when the initial transcription rate is unchanged.

## Abundance is a balance, not a direct transcription meter

For one RNA species, a simple bookkeeping model is

`dM/dt = r_prod − k_decay M`,

where `M` is the measured abundance, `r_prod` is its effective production rate into the measured RNA pool, and `k_decay` is an effective first-order loss constant. At steady state, `M = r_prod / k_decay`. A lower steady-state signal could therefore reflect lower transcription, less efficient processing into the measured species, faster degradation, reduced recovery, or fewer cells contributing that RNA. Conversely, unchanged total signal can hide a large shift in the mixture of isoforms.

The measured quantity and denominator must be named. Total RNA per culture, RNA per viable cell, normalized qPCR signal, and sequencing read fractions answer different questions. For an isoform claim, report the junction or read definition, the total or reference used for normalization, independent biological replicates, and how ambiguous reads are handled. Technical PCR wells improve measurement precision but do not create independent biological samples.

## Synthetic perturbation example

The following values are **synthetic teaching data**, not results from a published experiment. Four independently cultured samples were measured in each condition. Junction-specific digital counts are shown as mean counts per fixed number of viable cells; the precursor signal is a separate intron-containing assay on the same scale. The two mature isoforms are mutually exclusive in this simplified example.

| Readout | Non-targeting control, mean ± SD | Splice-regulator depletion, mean ± SD |
| --- | ---: | ---: |
| Exon-inclusion isoform, junction assay | 60 ± 5 | 30 ± 4 |
| Exon-skipping isoform, junction assay | 30 ± 4 | 60 ± 6 |
| Shared mature transcript signal | 90 ± 7 | 90 ± 8 |
| Intron-containing precursor signal | 95 ± 8 | 94 ± 9 |
| Viable-cell recovery, relative units | 1.00 ± 0.08 | 0.98 ± 0.07 |

The included and skipped counts exchange in this constructed dataset while their sum and the shared-transcript signal remain similar. This pattern is consistent with a change in isoform composition rather than a large change in the measured total precursor or mature RNA. It does not prove that the depleted protein directly recognizes this splice site. The perturbation could change another regulator or cell state, and one shared amplicon does not assay every RNA molecule.

### Worked calculation and interpretation

In the depleted group, the estimated skipped-isoform fraction among the two measured mature forms is `60 / (30 + 60) = 0.667`, or about 66.7%. In the control it is `30 / (60 + 30) = 0.333`, or about 33.3%. The estimated difference is about 33 percentage points. These are proportions of the two measured forms, not a claim that 66.7% of all transcripts in the cell use this splice pattern.

To strengthen the splice-regulator interpretation, repeat the experiment with independent perturbation reagents and biological replicates, verify depletion, and restore the factor with a perturbation-resistant construct where feasible. Use junction-specific assays or appropriately designed long-read/short-read sequencing, include no-reverse-transcriptase and assay-specific controls, measure viable-cell recovery, and test whether other transcripts or cell-state markers change. A nascent-RNA assay can help distinguish transcription from mature-RNA effects; a pulse-chase or decay assay can test altered stability. Each measurement tests a different part of the mechanism.

## Check your reasoning

If a shared-exon assay is unchanged but inclusion- and skipping-junction assays move in opposite directions, what has changed most directly: total measured transcript, isoform composition, or protein activity? What control would reveal genomic DNA contamination in a reverse-transcription assay? Which additional measurement would help distinguish altered processing from altered RNA decay?

## Provenance

This lesson, its worked calculation, and its synthetic table are original content licensed CC BY 4.0. MIT OCW 7.28x Molecular Biology is a link-only curriculum comparator. The NCBI Bookshelf chapters listed in the source registry are link-only references; no prose, figure, question, or data from them is copied or adapted.

# Translation and protein turnover

The central-dogma arrow from messenger RNA to protein compresses a multistep, energy-consuming process. A cell's protein abundance reflects both production and removal, so RNA abundance alone does not determine the amount or activity of a protein. Experiments must identify which stage was measured and avoid reading more mechanism into a result than the assay supports.

## Learning objectives

By the end of this lesson, you should be able to:

1. Trace eukaryotic translation initiation, elongation, and termination while maintaining mRNA direction, codon reading frame, and peptide-growth direction.
2. Relate synthesis and degradation to a simple protein-abundance model and calculate a first-order half-life from a decay measurement.
3. Interpret matched RNA, nascent-protein, protein-abundance, and turnover measurements and propose controls that distinguish altered translation from altered protein stability.

## Translation reads an RNA sequence in triplets

Translation occurs on ribosomes, whose rRNA and proteins form sites for the messenger RNA and transfer RNAs. Each tRNA carries an amino acid attached by an aminoacyl-tRNA synthetase and presents an anticodon that can pair with an mRNA codon. The ribosome advances along the mRNA 5′ to 3′ and extends the polypeptide from its amino terminus toward its carboxyl terminus. A coding sequence's reading frame groups bases into codons; shifting that frame changes all downstream codons until a stop is encountered.

### Initiation

In a common eukaryotic route, initiation factors help the small ribosomal subunit and initiator methionyl-tRNA associate with the 5′ end of a capped mRNA. The complex scans in the 5′-to-3′ direction and recognizes an AUG in an appropriate local sequence context. Start-site choice can vary, and a downstream AUG is not necessarily used just because it is present. The large subunit then joins to form a translating ribosome. Cap recognition, poly(A)-associated proteins, initiation factors, RNA structure, and regulatory proteins can influence initiation, but none alone predicts a fixed translation rate.

### Elongation

During each elongation cycle, a charged tRNA that matches the current codon is delivered to the ribosome's A site, subject to selection and proofreading. The growing peptide is held through the P-site tRNA; rRNA catalyzes peptide-bond formation, transferring the chain to the amino acid in the A site. The ribosome translocates by one codon, moving tRNAs through the A, P, and E sites. GTP hydrolysis helps drive delivery and movement, while ATP is used to charge tRNAs. Fidelity has an energetic cost because incorrect matches are rejected after partial progress as well as before peptide-bond formation.

### Termination and protein maturation

When a stop codon enters the A site, a release factor recognizes it and promotes hydrolysis of the linkage between the completed peptide and the P-site tRNA. The ribosome, mRNA, and tRNAs can then be recycled. Translation produces a polypeptide, not necessarily a mature active protein: folding, chaperone assistance, cleavage, chemical modification, complex assembly, and correct trafficking can all matter. A protein abundance assay does not directly measure activity or localization.

## Protein abundance reflects synthesis and loss

Let `P` be the abundance of a particular protein, `s` its synthesis rate, and `k_deg` a first-order degradation constant. A simple model is

`dP/dt = s − k_deg P`.

If the rates and conditions are constant long enough to approach steady state, then `P_ss = s / k_deg`. A protein can become less abundant because synthesis falls, degradation rises, the fraction of cells expressing it falls, or the assay recovers less protein. If synthesis suddenly stops and degradation remains first-order, the labeled protein follows `P(t) = P(0) e^(−k_deg t)` and the half-life is `t_1/2 = ln(2) / k_deg`.

For a first-order process, a corrected signal that reaches one half of its initial value at five hours implies an estimated half-life of five hours. This conclusion depends on a suitable chase, background correction, stable normalization, and a decay regime that is close enough to first-order over the measured interval. A two-point estimate is a teaching calculation, not a robust kinetic fit; real analysis should use multiple time points, replicate-level data, uncertainty, and a validated model.

The main eukaryotic routes for protein turnover include ubiquitin-directed proteasomal degradation and lysosomal degradation, including autophagic delivery. Ubiquitin is not a universal synonym for “degraded by proteasome”: ubiquitin signals can have other roles, and proteins can be degraded by multiple pathways. A fall in total protein does not identify its degradation route or establish that a specific ligase, proteasome, or lysosome caused it.

## Design measurements around the competing mechanisms

Suppose steady-state protein decreases after a perturbation. A targeted measurement plan can separate hypotheses:

| Candidate change | Useful paired readout | Key limitation to keep visible |
| --- | --- | --- |
| Less transcription or RNA processing | Nascent RNA, mature total RNA, and isoform-specific RNA | Mature RNA is influenced by processing and decay as well as transcription |
| Lower translation per mature RNA | Short-pulse nascent-protein synthesis together with matched mRNA; polysome or ribosome-footprint evidence can refine the stage | Pulse labeling and ribosome occupancy have assay-specific biases; occupancy is not always productive synthesis |
| Faster protein removal | Labeled-protein pulse-chase or carefully controlled time course | A translation inhibitor can alter stress signaling and protein turnover; one end point is not a decay curve |
| Cell number, state, or recovery changed | Viability, cell counts, reference standards, and cell-state markers | Normalization cannot remove every composition or recovery bias |

An orthogonal assay and a rescue can increase confidence in a perturbation result. Independent perturbation reagents address reagent-specific effects; a matched negative control estimates background; rescue asks whether restoring the candidate factor reverses the phenotype. Rescue supports involvement in the tested system but does not prove direct molecular action. A justified causal claim should name the perturbation, controls, measured endpoints, replicate unit, and plausible alternatives.

## Synthetic translation and turnover dataset

The following measurements are **synthetic teaching data**, not published results. Four independent cultures were measured per condition. Values are normalized to the same number of viable cells and a validated external recovery standard. The perturbation targets a candidate translation-initiation regulator; a perturbation-resistant rescue is included as a third condition.

| Readout | Non-targeting control | Regulator depletion | Depletion + rescue |
| --- | ---: | ---: | ---: |
| Mature target mRNA, relative units | 100 ± 8 | 98 ± 9 | 101 ± 7 |
| Short-pulse nascent target protein, relative units | 80 ± 7 | 41 ± 6 | 73 ± 8 |
| Steady-state target protein, relative units | 120 ± 10 | 62 ± 8 | 108 ± 11 |
| Pulse-chase half-life estimate, hours | 4.0 ± 0.4 | 4.1 ± 0.5 | 4.0 ± 0.4 |
| Viability, percent of starting cells | 94 ± 3 | 92 ± 4 | 93 ± 3 |

In this constructed pattern, target mRNA, measured protein half-life, and viability are similar, while the nascent-protein signal and steady-state protein fall under depletion and move toward control after rescue. This is consistent with reduced protein synthesis per measured mRNA in these conditions. It does not prove that the regulator directly initiates translation: rescue can restore an indirect pathway, pulse-label incorporation can change for reasons other than target-specific translation, and the half-life measurement is an estimate under one assay. A polysome profile or appropriately controlled ribosome-footprint analysis, additional independent perturbations, and other protein targets would help test specificity and locate the affected step.

### Worked mechanism check

The synthesis decrease predicts a lower steady-state abundance even if the protein's degradation constant does not change. Under the simple model, if `s` falls by about one half while `k_deg` is constant, then `P_ss = s / k_deg` also falls by about one half after a new steady state is reached. The table's nascent-protein and steady-state signals are roughly halved while the half-life remains similar, which fits that model qualitatively. The measured assays are noisy and do not establish exact proportionality or prove that the culture had fully reached a new steady state.

## Check your reasoning

If target mRNA is unchanged, nascent protein falls, and pulse-chase half-life is unchanged, which broad term in `dP/dt = s − k_deg P` is most directly supported as changed? What evidence would help distinguish reduced initiation from a downstream elongation or peptide-processing effect? Why would an inhibitor-based chase need stress and viability controls?

## Provenance

This lesson, its model, and its synthetic dataset are original content licensed CC BY 4.0. MIT OCW 7.28x Molecular Biology is a link-only curriculum comparator. NCBI Bookshelf material in the source registry is a link-only reference; no prose, figure, question, or data is copied or adapted.

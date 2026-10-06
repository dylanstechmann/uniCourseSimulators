# Protein sorting, vesicle traffic, and experimental inference

## Cargo selection and membrane traffic are separate steps

After a protein reaches a membrane-bound compartment, its next destination depends on its own sorting information, binding partners, and the transport machinery available in that cell. In the secretory pathway, newly synthesized cargo commonly moves from ER to Golgi and then to the plasma membrane, a secretory granule, or an endosomal/lysosomal route. Other proteins leave the ER only temporarily and are retrieved. These routes are dynamic cycles, not one-way conveyor belts.

Different coats and adaptors participate in common routes. COPII machinery supports export from ER exit sites; COPI supports several retrograde and intra-Golgi routes; clathrin participates in endocytosis and in selected traffic from the trans-Golgi network. Adaptors help connect cargo signals and membrane receptors to a coat. Small GTPases such as Rabs and tethering proteins help organize recognition and docking at target membranes. SNARE proteins on opposing membranes then contribute to membrane fusion. These names identify important components, not a complete or universal parts list: cells use cargo-specific adaptors, routes can overlap, and vesicle formation alone does not guarantee a particular destination.

### A route map with membrane sidedness

`ER lumen → Golgi lumen → transport vesicle lumen → extracellular space (after plasma-membrane fusion)`

`cytosol-facing cargo tail → cytosolic face of ER/Golgi/vesicle/plasma membrane`

This topology explains how a signal on the cytosolic tail can direct a transmembrane protein while its extracellular or lumenal domain remains inside the vesicle. Soluble cargo in a vesicle lumen never needs to cross the vesicle membrane during ordinary vesicle transport.

## Two sorting examples

### Lysosomal hydrolases and mannose-6-phosphate

Many soluble lysosomal hydrolases receive a mannose-6-phosphate (M6P) modification on their N-linked glycans during passage through the Golgi. M6P receptors bind cargo in the trans-Golgi network; cytosolic receptor motifs and adaptors help package the receptor–cargo complex into transport carriers headed toward endosomes. The acidic endosomal environment favors release of many hydrolase ligands, while receptor and cargo follow different later routes: receptors can recycle, and hydrolases proceed toward lysosomes. This is a common route for many soluble lysosomal enzymes, not a universal address label for every lysosomal membrane protein or every lysosomal cargo.

Primary experiments show why cargo recognition and vesicle sorting should be tested separately. Johnson and Kornfeld mutated the cytosolic tail of the cation-dependent M6P receptor in receptor-deficient mouse cells. A tail mutant retained measurable M6P-ligand binding and surface-to-Golgi recycling yet sorted newly synthesized cathepsin D less effectively. The result supports a role for the receptor's cytosolic tail after ligand binding; it does not identify every adaptor involved or establish that every cell type uses an identical quantitative route. See the linked [primary study](https://pubmed.ncbi.nlm.nih.gov/1324923/).

### Retrieval of ER-resident soluble proteins

Some ER-lumenal proteins that escape toward the Golgi carry a carboxyl-terminal retrieval signal, commonly KDEL in mammals. A cycling receptor recognizes such cargo in post-ER compartments and helps return it to the ER. “ER retention” is convenient shorthand, but it should not imply that every tagged molecule is physically trapped in the ER at every moment. Munro and Pelham's experiments showed that appending the terminal sequence to a secretory protein could alter its secretion and accumulation; later work also demonstrates that the signal's effect depends on cargo and context. Compare the [1987 primary study](https://pubmed.ncbi.nlm.nih.gov/3545499/) and a study of [retrieval beyond the cis-Golgi](https://pubmed.ncbi.nlm.nih.gov/7721936/).

## Worked data example: ligand binding versus sorting

Suppose a laboratory compares wild-type M6P receptor with a cytosolic-tail mutant. The following values are an **original synthetic exercise**, not the measurements reported in a paper. Total newly synthesized hydrolase is normalized to 100 units in each condition; independent cultures and variability would be needed before drawing a real conclusion.

| Receptor condition | Relative M6P-ligand binding | Hydrolase delivered to lysosome fraction | Hydrolase detected in medium |
| --- | ---: | ---: | ---: |
| Wild-type receptor | 100 | 68 | 24 |
| Tail-motif mutant | 96 | 42 | 49 |

Binding is similar, while the distribution of the newly made cargo shifts away from the lysosome fraction and toward the medium. This pattern is more consistent with a post-binding sorting or retention defect than with loss of ligand recognition. It is not decisive by itself: the receptor may differ in abundance or compartment access, the fractions may differ in recovery, and changes in degradation can alter measured abundance.

A stronger follow-up would confirm matched receptor abundance and localization, measure total labeled cargo at each time point, include recovery markers for the lysosome fraction, and measure cargo degradation separately from secretion. Reintroducing a wild-type receptor is a rescue test; restoring the tail motif in the mutant can more specifically test the motif. Replicates should be summarized with the individual values and uncertainty. State the conclusion at the level of the measured route and cell system rather than claiming a universal trafficking law.

## Retrieval practice and evidence checks

1. A lumenal protein with a terminal KDEL sequence appears transiently in the early Golgi and later returns to the ER. Why is “receptor-mediated retrieval” a better model than “the protein never leaves the ER”?
2. A lysosomal enzyme binds M6P receptor normally but is secreted more often after a receptor-tail mutation. Which controls separate defective sorting from altered synthesis, receptor abundance, or fraction recovery?
3. If receptor and cargo enter the same carrier, what evidence would show that they later separate rather than travel together to the lysosome?

## Sources and provenance

The teaching explanations, route map, and synthetic data are original. Primary research is linked for the M6P-receptor sorting experiment by [Johnson and Kornfeld (1992)](https://pubmed.ncbi.nlm.nih.gov/1324923/), ER retrieval by [Munro and Pelham (1987)](https://pubmed.ncbi.nlm.nih.gov/3545499/), and endosomal separation of receptor and lysosomal membrane cargo in [Geuze et al. (1988)](https://pubmed.ncbi.nlm.nih.gov/2849607/). MIT OCW [Lecture 19](https://ocw.mit.edu/courses/7-016-introductory-biology-fall-2018/resources/lecture-19-cell-trafficking-and-protein-localization/) is a topic-level comparator only. No source text, figure, problem, or dataset is copied or redistributed. See the package [source map](../source-map.json) and the repository [source registry](../../../sources/registry.json). Original content is released under CC BY 4.0.

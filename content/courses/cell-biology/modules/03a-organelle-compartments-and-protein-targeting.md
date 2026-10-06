# Organelle compartments, membrane topology, and protein targeting

## Compartments make cell chemistry conditional

A eukaryotic cell is not a well-mixed bag. The cytosol, nucleoplasm, mitochondrial matrix, endoplasmic-reticulum (ER) lumen, Golgi cisternae, endosomes, and lysosomes differ in pH, ion composition, redox conditions, enzymes, and macromolecular crowding. Membranes restrict some solutes and proteins while transporters, pores, and vesicles permit regulated exchange. A compartment's function therefore depends on both its contents and the boundary that maintains its conditions.

Examples illustrate why location changes the interpretation of a molecule. The mitochondrial inner membrane supports an electrochemical proton gradient used in ATP synthesis; the matrix contains enzymes for specific oxidative reactions. The ER lumen supports entry and early maturation of many secreted and membrane proteins. Acidic endosomes and lysosomes support sorting and degradation, but an acidic compartment is not automatically a lysosome: organelle identity also depends on enzymes, membrane proteins, and trafficking history. Peroxisomes conduct oxidative reactions with specialized enzyme and peroxide-handling systems. These descriptions are functional models, not claims that every cell has the same organelle abundance or every reaction is exclusive to one compartment.

## Destination signals are interpreted by different machinery

Many proteins reach a destination because the nascent or completed protein presents a recognizable signal. There is no single universal “organelle tag,” and a sequence prediction does not by itself demonstrate final localization.

| Destination or route | Common targeting information | A common route and an important limit |
| --- | --- | --- |
| ER lumen or secretory pathway | An exposed hydrophobic ER signal sequence, often near the amino terminus | Signal recognition particle (SRP) binds the emerging sequence and ribosome, which is delivered to an ER translocon. Many soluble secretory proteins enter while being synthesized; a cleavable signal peptide is often removed. |
| ER membrane | Signal-anchor and stop-transfer segments | Hydrophobic segments enter the membrane and determine which regions face cytosol or lumen. A membrane protein's orientation depends on sequence context and insertion machinery, not simply on one “ER address.” |
| Nucleus | Nuclear-localization sequence (NLS) on the cargo | Import receptors move cargo through nuclear pores. The NLS is commonly retained, and Ran nucleotide state contributes to directionality; nuclear entry is not ER-like translocation through a lipid bilayer. |
| Mitochondrial matrix | A common class of amino-terminal, positively charged amphipathic targeting sequences | Cytosolic chaperones and TOM/TIM translocases support import; the inner-membrane potential contributes for many matrix-directed precursors. Other mitochondrial proteins use internal or membrane-specific signals. |
| Peroxisome | A common type-1 peroxisomal targeting signal (PTS1) is near the carboxyl terminus; other cargo uses PTS2 | Receptors such as PEX5 recognize some PTS1 cargo. Peroxisomal import has features that differ from mitochondrial import; do not generalize one route to all organelles. |

Proteins without an organelle-targeting signal often remain in the cytosol, but “no signal” is not proof of a final location. Binding partners, post-translational modifications, regulated masking of signals, and cell state can change where a protein accumulates. Localization is a measurable property under stated conditions, not a guaranteed consequence of sequence inspection.

## Membrane topology follows the route

When an ER-derived transport vesicle buds and fuses with another endomembrane compartment, membrane orientation is preserved: the cytosolic face stays exposed to cytosol, and the lumen-facing surface remains lumen-facing. When a secretory vesicle fuses with the plasma membrane, its lumen becomes continuous with the extracellular space. This topological rule explains why a glycoprotein domain exposed to the ER lumen can later be extracellular, and why cytosolic sorting motifs remain on the cytosolic tails of membrane proteins.

Do not confuse vesicle transport with crossing a membrane. A vesicle moves cargo between connected lumenal spaces; a translocon moves a polypeptide across a membrane; a nuclear pore provides a gated route through a large protein assembly. These routes solve different physical problems and use different signals and machinery.

## Worked example: protease protection tests membrane enclosure

Consider a teaching experiment with a soluble protein that normally enters the ER. Cells express either the wild-type protein or a version lacking its N-terminal ER signal. After a short pulse label, ER-derived sealed microsomes are prepared. Proteinase K digests exposed protein; detergent disrupts the microsome membrane so the protease can reach the lumen. The measurements below are **synthetic** means from four independent preparations (n = 4), reported as percent of the no-protease signal for each marker.

| Protein or control | No protease | Protease, intact microsomes | Protease + detergent |
| --- | ---: | ---: | ---: |
| Wild-type test protein | 100 ± 6 | 78 ± 7 | 3 ± 1 |
| Signal-deletion test protein | 98 ± 5 | 4 ± 2 | 2 ± 1 |
| ER-lumen marker | 100 ± 8 | 86 ± 6 | 2 ± 1 |
| Cytosolic marker | 100 ± 5 | 3 ± 1 | 2 ± 1 |

The protected wild-type signal resembles the ER-lumen marker and disappears when detergent opens the membrane. The cytosolic marker is digested even without detergent, which argues that protease was active and that protection was not a general failure of the assay. The signal-deletion product is not protected. Together, the pattern supports entry of the wild-type protein into a membrane-enclosed lumen and a requirement for the deleted region under these conditions.

The result does **not** identify which step failed in the mutant. Signal recognition, ribosome targeting, translocon engagement, translocation, and rapid degradation remain possible explanations. Measure transcript and total newly synthesized protein, include a known lumenal positive control, verify microsome integrity, and use a time course. A glycosylation readout can provide an orthogonal indication of access to ER-lumenal enzymes, but glycosylation also depends on sequence and processing. Co-fractionation or microscopy with ER markers can help identify the compartment; neither alone proves direct molecular interaction.

## Check your understanding

1. A protein is protected from protease in intact microsomes but digested after detergent is added. What physical conclusion is supported, and what additional evidence would identify the compartment?
2. Why does an NLS-bearing protein not need to enter the ER before reaching the nucleus?
3. A mitochondrial matrix-targeting sequence is predicted, but the protein is mostly cytosolic in one cell type. Name two measurements that would distinguish failed import from low protein synthesis or rapid degradation.

## Sources and provenance

This explanation and its dataset are original. The dataset is synthetic and is not presented as an observation from a published study. MIT OpenCourseWare's undergraduate [Lecture 19: Cell Trafficking and Protein Localization](https://ocw.mit.edu/courses/7-016-introductory-biology-fall-2018/resources/lecture-19-cell-trafficking-and-protein-localization/) is linked as a scope comparator only. The signal-sequence history is linked to the primary research of [Blobel and Dobberstein (1975)](https://pubmed.ncbi.nlm.nih.gov/811671/); no source text, figure, or data table is reproduced. See the package [source map](../source-map.json) and the repository [source registry](../../../sources/registry.json). Original content is released under CC BY 4.0.

# Final candidate: cumulative evidence and models

**State:** inactive candidate for review, authored with substantial Codex assistance for Biology 0.29.0. The course remains partial, unreviewed and formative-only. No live submission route, course grade, deadline, time limit or attempt policy is set. Workload has not been measured. Keys and candidate-specific checks remain outside Git; no independent scientific/numerical/assessment/accessibility reviewer approved the form.

This draft has 28 multi-field cases and 150 proposed machine-scored points. It links 70 objective occurrences across 69 distinct objectives in 28 topic lessons. An objective reused by two lessons counts as two links and one unique objective. Field-level metadata makes the mapping inspectable. These checks assess the stated calculations and categorical decisions; they do not grade a learner's written explanation, design, uncertainty, script or plot. Coverage labels do not establish performance at every objective verb or a complete summative assessment.

## Assigned forms, observations and models

The [observation table](final-candidate-observations.csv) lists original synthetic case/form measurements with named scales. Contexts below supply needed assumptions, formulas and independent units. Values are deterministic teaching inputs, not physical observations or calibrated uncertainty. Forms A/B use fixed authored values and the platform's authored-variant/source/token replay contract. Both review DTO sets are public and answer-free; their keys are external. A future served field refers to the form named in its case, and the selected signed variant must be replayed when submitted. The draft does not select a production retake policy or prove immutable historical archiving exists.

Numeric fields state three significant figures where requested, a compatible unit if present and a response tolerance. Tolerances are grading rules, not uncertainty. Bare scales are explicitly named and have no unit conversion/dimension enforcement. Categorical fields score one option, not prose. Fields carry the point weights shown; partial credit is independent by field. Invalid fields receive no points or a validation error; other valid fields may earn their stated partial credit. Choices are numbered for this paper review; a future interface uses its own controls. No field needs an image or color distinction.

Experimental cases retain the named culture/preparation/clone/batch unit. Cells, repeated aliquots, fields and technical wells are not extra independent units. A mean/difference is descriptive unless an uncertainty model and justified analysis are supplied. Optical overlap is not direct binding; a molecular/cell marker is not native causality, stable identity, mature function or clinical benefit. Positive controls, backgrounds, input/loading references and loss accounting address different alternatives.

## Case packet: authored forms A and B

### cell-biology-final-candidate:case-01 — 7 proposed points

Ionizable substitution in an assembly. Authored form A. A fictional protein has a aspartate side chain on a water-exposed surface at pH 7; its measured pKa is 3.8. It is changed to alanine. Other covalent bonds remain intact; assembly has not been measured.

Ionizable substitution in an assembly. Authored form B. A fictional protein has a glutamate side chain on a water-exposed surface at pH 7; its measured pKa is 4.2. It is changed to alanine. Other covalent bonds remain intact; assembly has not been measured.

**criterion-1 (3 points):** Which description distinguishes the mutation from ordinary molecular association?

1. Association necessarily changes every peptide bond.
2. The side-chain covalent structure changes; reversible association can occur without new covalent bonds.
3. The mutation only changes noncovalent contacts, never structure.

**criterion-2 (2 points):** What bounded prediction follows at the specified pH?

1. Charge loss proves the protein cannot assemble.
2. Alanine adds an ionized carboxylate at pH 7.
3. The original side chain is predominantly negative; alanine removes that charge and may change assembly.

**criterion-3 (2 points):** Which chemical feature is directly removed by this substitution?

1. The side-chain carboxyl group, without necessarily removing the backbone amide.
2. A side-chain phosphate that neither residue contains.
3. Every backbone amide.

### cell-biology-final-candidate:case-05 — 4 proposed points

A titratable group in water. Authored form A. An isolated carboxyl group in water has pKa 6.0; the solution pH is 4.0. Use [A-]/[HA] = 10^(pH-pKa), with no coupled groups. A separate nonpolar solute aggregates in water without new covalent bonds.

A titratable group in water. Authored form B. An isolated carboxyl group in water has pKa 6.0; the solution pH is 8.0. Use [A-]/[HA] = 10^(pH-pKa), with no coupled groups. A separate nonpolar solute aggregates in water without new covalent bonds.

**criterion-1 (2 points):** Which interpretation of the nonpolar aggregate is justified?

1. Nonpolar solutes must become permanently charged.
2. Aggregation proves new peptide bonds form.
3. Water-mediated hydrophobic association is plausible; aggregation alone does not establish covalent bonding.

**criterion-2 (2 points):** Calculate the ratio of deprotonated to protonated group on a bare ratio scale. Report exactly 3 significant figures.

Response scale: `bare declared scale`; absolute tolerance 0.005; relative tolerance 0.



### cell-biology-final-candidate:case-06 — 4 proposed points

Protein quantity and function. Authored form A. A buried hydrophobic residue is replaced by a charged residue. In matched recovered protein, reference abundance is 80 and variant abundance is 20 arbitrary amount units. Total activities are 640 and 128 arbitrary rate units. Folding measurements and localization are missing.

Protein quantity and function. Authored form B. A buried hydrophobic residue is replaced by a charged residue. In matched recovered protein, reference abundance is 80 and variant abundance is 32 arbitrary amount units. Total activities are 640 and 256 arbitrary rate units. Folding measurements and localization are missing.

**criterion-1 (2 points):** Which prediction respects residue environment and missing measurements?

1. A buried charge proves loss of all activity in every context.
2. Any charged substitution necessarily increases native folding.
3. A buried charge may disrupt stability or packing, but the actual fold and localization need measurement.

**criterion-2 (2 points):** Calculate variant/reference specific activity: (variant activity/amount)/(reference activity/amount), a bare ratio. Report exactly 3 significant figures.

Response scale: `bare declared scale`; absolute tolerance 0.005; relative tolerance 0.



### cell-biology-final-candidate:case-02 — 4 proposed points

Passive potassium and transport classes. Authored form A. Only K+ is permeant in an ideal membrane. Inside K+ is 80 mM; outside is 20 mM; at 37 C use E_K = 61.5 log10(outside/inside) mV. Membrane voltage is 0 mV. A separate carrier moves a substrate uphill only when coupled to ATP hydrolysis.

Passive potassium and transport classes. Authored form B. Only K+ is permeant in an ideal membrane. Inside K+ is 160 mM; outside is 80 mM; at 37 C use E_K = 61.5 log10(outside/inside) mV. Membrane voltage is 0 mV. A separate carrier moves a substrate uphill only when coupled to ATP hydrolysis.

**criterion-1 (2 points):** Calculate E_K using the stipulated rounded coefficient. Report exactly 3 significant figures.

Response scale: `mV`; absolute tolerance 0.05; relative tolerance 0.



**criterion-2 (2 points):** Classify the ATP-dependent uphill carrier.

1. Passive transport because all carriers are passive.
2. Simple diffusion through the lipid bilayer.
3. Active transport; downhill carrier-mediated flux would be facilitated diffusion.

### cell-biology-final-candidate:case-07 — 4 proposed points

Compartment boundary evidence. Authored form A. A fictional protein with a cleavable ER-targeting peptide enters a lumen. Intact vesicles protect 85% of its immunoreactivity from added protease; detergent plus protease removes the signal. A cytosolic marker is digested without detergent. Vesicle recovery is matched. These are biochemical aliquots, not independent living cells.

Compartment boundary evidence. Authored form B. A fictional protein with a cleavable ER-targeting peptide enters a lumen. Intact vesicles protect 72% of its immunoreactivity from added protease; detergent plus protease removes the signal. A cytosolic marker is digested without detergent. Vesicle recovery is matched. These are biochemical aliquots, not independent living cells.

**criterion-1 (2 points):** What topology follows if the stated targeting and translocation succeed?

1. A cleaved ER peptide necessarily places the mature protein in the nucleus.
2. The mature soluble protein is on the luminal side and remains topologically outside the cytosol.
3. The protein must cross the bilayer at every secretory step.

**criterion-2 (2 points):** What is the bounded protease conclusion?

1. Protection proves a unique living-cell organelle and direct binding.
2. Protection is consistent with enclosed antigen; detergent sensitivity and markers address integrity, not exact native location by themselves.
3. The cytosolic digestion control is interchangeable with vesicle integrity.

### cell-biology-final-candidate:case-08 — 4 proposed points

Receptor recycling and cargo sorting. Authored form A. Pulse-labeled extracellular cargo binds equally to reference and perturbed cells at time zero. At a matched chase, receptor returns to the surface in both; cargo in a degradative compartment changes from 70% to 35%. Total recovered label and new synthesis are matched, but degradation fragments and spatial resolution are not measured.

Receptor recycling and cargo sorting. Authored form B. Pulse-labeled extracellular cargo binds equally to reference and perturbed cells at time zero. At a matched chase, receptor returns to the surface in both; cargo in a degradative compartment changes from 70% to 42%. Total recovered label and new synthesis are matched, but degradation fragments and spatial resolution are not measured.

**criterion-1 (2 points):** Which route preserves topology?

1. A surface receptor and all its cargo must always share their terminal destination.
2. Recycling requires cargo to become cytosolic by membrane inversion.
3. Endocytosed luminal cargo can remain enclosed while its receptor recycles to the surface.

**criterion-2 (2 points):** What can the matched measurements support?

1. A redistribution consistent with altered sorting; unresolved label loss and compartment assignment still need controls.
2. A late compartment percentage proves changed transcription.
3. Equal initial binding proves normal sorting and degradation.

### cell-biology-final-candidate:case-03 — 4 proposed points

Catalysis and coupling. Authored form A. Use v = Vmax*S/(Km+S), with Vmax 96 arbitrary rate units, Km 3 mM and S 9 mM. At matched conditions reaction X has deltaG +15 kJ/mol and coupled reaction Y has deltaG -27 kJ/mol; stoichiometry is 1:1.

Catalysis and coupling. Authored form B. Use v = Vmax*S/(Km+S), with Vmax 105 arbitrary rate units, Km 4 mM and S 8 mM. At matched conditions reaction X has deltaG +15 kJ/mol and coupled reaction Y has deltaG -31 kJ/mol; stoichiometry is 1:1.

**criterion-1 (2 points):** Calculate v on the declared bare rate-unit scale. Report exactly 3 significant figures.

Response scale: `bare declared scale`; absolute tolerance 0.005; relative tolerance 0.



**criterion-2 (2 points):** Calculate the net deltaG per mole of coupled events. Report exactly 3 significant figures.

Response scale: `kJ/mol`; absolute tolerance 0.005; relative tolerance 0.



### cell-biology-final-candidate:case-09 — 4 proposed points

Active enzyme and equilibrium. Authored form A. A purified catalyst changes the activation barrier without changing initial/final state free energies. In an ideal initial-rate assay active enzyme is 4 nM, kcat 9 per second, S 6 mM and Km 3 mM; v = kcat*E*S/(Km+S). No inhibition or enzyme loss occurs.

Active enzyme and equilibrium. Authored form B. A purified catalyst changes the activation barrier without changing initial/final state free energies. In an ideal initial-rate assay active enzyme is 5 nM, kcat 14 per second, S 6 mM and Km 6 mM; v = kcat*E*S/(Km+S). No inhibition or enzyme loss occurs.

**criterion-1 (2 points):** Which effect is compatible with a catalyst?

1. A catalyst makes every uphill reaction have a negative deltaG.
2. Faster forward and reverse equilibration with unchanged equilibrium constant for the same states.
3. A catalyst changes equilibrium by consuming itself irreversibly.

**criterion-2 (2 points):** Calculate initial v on a bare nM-per-second scale. Report exactly 3 significant figures.

Response scale: `bare declared scale`; absolute tolerance 0.005; relative tolerance 0.



### cell-biology-final-candidate:case-10 — 4 proposed points

Inhibitor model and optical control. Authored form A. An initial-rate fit gives Vmax 84 and apparent Km 7 mM with inhibitor; use v=Vmax*S/(Km+S) at S 7 mM. Without inhibitor Vmax is the same and Km is smaller. Blank wells show negligible optical interference; direct binding and uncertainty estimates are unavailable.

Inhibitor model and optical control. Authored form B. An initial-rate fit gives Vmax 96 and apparent Km 8 mM with inhibitor; use v=Vmax*S/(Km+S) at S 4 mM. Without inhibitor Vmax is the same and Km is smaller. Blank wells show negligible optical interference; direct binding and uncertainty estimates are unavailable.

**criterion-1 (2 points):** Calculate the fitted inhibited initial rate on the bare rate-unit scale. Report exactly 3 significant figures.

Response scale: `bare declared scale`; absolute tolerance 0.005; relative tolerance 0.



**criterion-2 (2 points):** Which statement is warranted by the parameter pattern and controls?

1. An optical blank proves a particular active-site structure.
2. The pattern proves irreversible enzyme destruction.
3. It is consistent with an ideal competitive pattern; the fit and optical blank do not prove a molecular binding route.

### cell-biology-final-candidate:case-11 — 4 proposed points

Sampling and overlap. Authored form A. For a conventional image estimate lateral resolution d=0.61*lambda/NA with lambda 540 nm and NA 1.35. Sample-plane pixel size is 80 nm. Two fluorescent channels overlap within the optical spot; single-label controls show measurable bleed-through.

Sampling and overlap. Authored form B. For a conventional image estimate lateral resolution d=0.61*lambda/NA with lambda 620 nm and NA 1.25. Sample-plane pixel size is 80 nm. Two fluorescent channels overlap within the optical spot; single-label controls show measurable bleed-through.

**criterion-1 (2 points):** Calculate nominal lateral resolution in nm. This estimate is distinct from pixel size. Report exactly 3 significant figures.

Response scale: `nm`; absolute tolerance 0.5; relative tolerance 0.



**criterion-2 (2 points):** Which follow-up and conclusion fit this image?

1. Discard single-label controls because colors differ on screen.
2. Increase magnification and declare direct binding from overlap.
3. Correct spectral cross-talk with matched controls; overlap at optical resolution does not establish direct molecular binding.

### cell-biology-final-candidate:case-12 — 4 proposed points

Recovery and enrichment. Authored form A. Input target marker activity is 160 units; the collected fraction contains 64 units. Fraction total protein is 3 mg. A second compartment marker is also detected. Only one collected fraction is supplied; missing fractions and rupture controls are absent.

Recovery and enrichment. Authored form B. Input target marker activity is 180 units; the collected fraction contains 54 units. Fraction total protein is 3 mg. A second compartment marker is also detected. Only one collected fraction is supplied; missing fractions and rupture controls are absent.

**criterion-1 (2 points):** Calculate target-marker recovery as a percentage of input. Report exactly 3 significant figures.

Response scale: `%`; absolute tolerance 0.005; relative tolerance 0.



**criterion-2 (2 points):** Which design can address the current limitations?

1. Collect all fractions and input for mass balance, multiple compartment markers and integrity controls; enrichment alone is not purity.
2. Treat the fraction protein mass as a count of independent cultures.
3. Use only the target marker and call the fraction pure.

### cell-biology-final-candidate:case-13 — 4 proposed points

Polarity and isotope generations. Authored form A. The template is 5-prime TACCG 3-prime. Polymerase extends a primer by adding to its 3-prime end. After heavy-to-light transfer, controlled isotope-density generation 1 has only hybrid-density DNA and generation 2 has hybrid plus light DNA; density resolution controls pass. In a resolved third generation, hybrid-to-light molecule classes are 1:3 under the stipulated ideal growth model.

Polarity and isotope generations. Authored form B. The template is 5-prime CGATT 3-prime. Polymerase extends a primer by adding to its 3-prime end. After heavy-to-light transfer, controlled isotope-density generation 1 has only hybrid-density DNA and generation 2 has hybrid plus light DNA; density resolution controls pass. In a resolved third generation, hybrid-to-light molecule classes are 1:3 under the stipulated ideal growth model.

**criterion-1 (2 points):** Which description correctly preserves strand polarity and synthesis?

1. Polymerase makes the leading strand by adding to its 5-prime end.
2. Both aligned strands have the same 5-prime to 3-prime direction.
3. The aligned complement runs 3-prime to 5-prime; a newly made strand grows 5-prime to 3-prime, with fragments on the lagging side.

**criterion-2 (2 points):** Which model fits the specified resolved generations?

1. Conservative replication predicts only hybrid DNA in generation 1.
2. Semiconservative replication; the second generation helps distinguish the ideal dispersive prediction.
3. All three models predict exactly the same resolved generations.

### cell-biology-final-candidate:case-14 — 4 proposed points

Lesion signal and repair. Authored form A. A bulky-adduct assay has matched input and extraction standards. At a fixed time lesion signal is 18 units in reference and 45 in a repair perturbation; rescue brings it near reference. Mutation counts, survival and independent pathway activity are unmeasured.

Lesion signal and repair. Authored form B. A bulky-adduct assay has matched input and extraction standards. At a fixed time lesion signal is 18 units in reference and 54 in a repair perturbation; rescue brings it near reference. Mutation counts, survival and independent pathway activity are unmeasured.

**criterion-1 (2 points):** Which distinction and pathway hypothesis is appropriate?

1. Proofreading and post-replicative mismatch repair are the same timed process.
2. Polymerase proofreading acts during synthesis; bulky-adduct excision is a plausible different repair pathway requiring specific tests.
3. Every bulky lesion is removed solely by polymerase proofreading.

**criterion-2 (2 points):** What does the rescue support within these measurements?

1. Rescue proves zero off-target effects or survival selection.
2. A lesion signal is directly the mutation frequency per genome.
3. Perturbation-associated lesion-signal change; mutation frequency and a unique native mechanism remain unmeasured.

### cell-biology-final-candidate:case-15 — 4 proposed points

Chromatin and independent units. Authored form A. Four independent cultures per state are each split into three technical aliquots. Accessibility rises by 35% and matched RNA by 18% between states. A histone mark also increases; no endogenous element perturbation has been done.

Chromatin and independent units. Authored form B. Four independent cultures per state are each split into three technical aliquots. Accessibility rises by 25% and matched RNA by 16% between states. A histone mark also increases; no endogenous element perturbation has been done.

**criterion-1 (2 points):** Which chromatin interpretation is bounded?

1. Any mark increase proves an irreversible transcriptional switch.
2. Accessibility and a mark can be associated with state; a mark is not by itself a transcriptional switch.
3. Nucleosomes never alter accessibility.

**criterion-2 (2 points):** Which analysis and causal follow-up fit the units?

1. Use a plasmid alone to prove endogenous element necessity.
2. Treat twelve aliquots as twelve independent cultures and infer causality from correlation.
3. Summarize aliquots within four cultures per state and perturb the endogenous element with matched controls and RNA/readout follow-up.

### cell-biology-final-candidate:case-04 — 7 proposed points

Expression and controls. Authored form A. A fictional construct is transcribed to mRNA and translated to protein. Three independent cultures have background-corrected reporter values 13, 17, 21; an untreated reference mean is 14. Positive assay control and a no-reporter negative control pass; input/loading measurements are not supplied.

Expression and controls. Authored form B. A fictional construct is transcribed to mRNA and translated to protein. Three independent cultures have background-corrected reporter values 19, 23, 27; an untreated reference mean is 18. Positive assay control and a no-reporter negative control pass; input/loading measurements are not supplied.

**criterion-1 (3 points):** Which information path fits the model?

1. RNA synthesis and peptide synthesis are the same chemical reaction.
2. Protein must first be reverse translated directly into genomic DNA.
3. DNA is transcribed to RNA; ribosomes read an mRNA frame to synthesize a polypeptide.

**criterion-2 (2 points):** Which control is missing for an abundance-normalized comparison?

1. No loading control is needed because the reporter is fluorescent.
2. A second positive control automatically replaces loading.
3. A matched input/loading measurement; positive and negative controls address different assay questions.

**criterion-3 (2 points):** Calculate the descriptive difference between the culture mean and reference on the bare reporter scale. Report exactly 3 significant figures.

Response scale: `bare declared scale`; absolute tolerance 0.005; relative tolerance 0.



### cell-biology-final-candidate:case-16 — 4 proposed points

ChIP input and cis claims. Authored form A. The measured input aliquot is fraction 0.05 of total input; Ct_input 22, Ct_IP 24. Under equal doubling efficiency use percent input=100*fraction*2^(Ct_input-Ct_IP). IgG and negative-locus controls pass. A matched plasmid deletion lowers reporter output; the endogenous locus has not been edited.

ChIP input and cis claims. Authored form B. The measured input aliquot is fraction 0.025 of total input; Ct_input 22, Ct_IP 25. Under equal doubling efficiency use percent input=100*fraction*2^(Ct_input-Ct_IP). IgG and negative-locus controls pass. A matched plasmid deletion lowers reporter output; the endogenous locus has not been edited.

**criterion-1 (2 points):** Calculate simplified ChIP percent input. Report exactly 3 significant figures.

Response scale: `%`; absolute tolerance 0.0005; relative tolerance 0.



**criterion-2 (2 points):** Which inference separates the two assays?

1. Enrichment supports occupancy-associated evidence and the plasmid tests sequence activity in that context; neither alone proves direct binding or endogenous necessity.
2. IgG controls replace input and PCR efficiency controls.
3. ChIP plus plasmid deletion proves direct binding and endogenous necessity.

### cell-biology-final-candidate:case-17 — 7 proposed points

Processing and isoform composition. Authored form A. Background-corrected mature included and skipped RNA counts are 120 and 30 in one recovered culture, with matched recovery. A common-region count measures both forms; precursor abundance is also measured. No independent transcription or decay rate is measured.

Processing and isoform composition. Authored form B. Background-corrected mature included and skipped RNA counts are 90 and 60 in one recovered culture, with matched recovery. A common-region count measures both forms; precursor abundance is also measured. No independent transcription or decay rate is measured.

**criterion-1 (3 points):** Which processing description fits many eukaryotic pre-mRNAs?

1. Capping, intron removal and 3-prime processing can produce mature RNAs; alternative splicing can change exon composition.
2. Every eukaryotic mRNA has identical processing and no exceptions.
3. The spliceosome translates introns into mature protein.

**criterion-2 (2 points):** Calculate skipped percentage among the two measured mature forms. Report exactly 3 significant figures.

Response scale: `%`; absolute tolerance 0.005; relative tolerance 0.



**criterion-3 (2 points):** Which control helps separate an RNA assay artifact?

1. A no-reverse-transcriptase control plus distinct perturbation/rescue and recovery controls; none alone identifies production versus decay.
2. A common-region amplicon proves a unique splicing mechanism.
3. A rescue automatically excludes DNA contamination.

### cell-biology-final-candidate:case-18 — 7 proposed points

Translation and labeled-cohort decay. Authored form A. A fixed protein cohort has corrected label f0=100, f4=50 after 4 h, with no new label or recycling and stable detection. Assume first-order decay f(t)/f0=exp(-k*t). A separate perturbation has unchanged RNA, lower nascent-protein signal and lower steady-state protein; loading controls pass.

Translation and labeled-cohort decay. Authored form B. A fixed protein cohort has corrected label f0=100, f4=25 after 4 h, with no new label or recycling and stable detection. Assume first-order decay f(t)/f0=exp(-k*t). A separate perturbation has unchanged RNA, lower nascent-protein signal and lower steady-state protein; loading controls pass.

**criterion-1 (3 points):** Which translation statement preserves frame and direction?

1. Ribosomes read 3-prime to 5-prime and extend peptide from carboxyl end.
2. Ribosomes read mRNA codons 5-prime to 3-prime and extend peptide from amino to carboxyl end until termination.
3. Any one-base shift leaves all downstream codons unchanged.

**criterion-2 (2 points):** Which interpretation separates synthesis and turnover?

1. Unchanged RNA proves unchanged protein synthesis and decay.
2. Lower nascent signal is consistent with reduced synthesis in this assay; matched decay measurements test turnover rather than assuming it.
3. Lower steady-state protein alone proves a proteasome route.

**criterion-3 (2 points):** Calculate the labeled-cohort half-life in h from t_half=4*ln(0.5)/ln(f4/f0). Report exactly 3 significant figures.

Response scale: `h`; absolute tolerance 0.005; relative tolerance 0.



### cell-biology-final-candidate:case-19 — 7 proposed points

A fictional inheritance model. Authored form A. For a nonclinical fictional trait, cross A/a with a/a. Exactly half offspring inherit A; at the specified age phenotype probability is 0.6 for carriers and 0.1 otherwise. A small selected pedigree and a population association are supplied without unbiased sampling or population covariates.

A fictional inheritance model. Authored form B. For a nonclinical fictional trait, cross A/a with a/a. Exactly half offspring inherit A; at the specified age phenotype probability is 0.7 for carriers and 0.1 otherwise. A small selected pedigree and a population association are supplied without unbiased sampling or population covariates.

**criterion-1 (3 points):** Calculate offspring phenotype probability as percent under this stipulated penetrance model. Report exactly 3 significant figures.

Response scale: `%`; absolute tolerance 0.005; relative tolerance 0.



**criterion-2 (2 points):** What limits a small selected pedigree?

1. Dominance means every carrier must have the same severity.
2. One selected pedigree proves complete penetrance in every age group.
3. Age, incomplete penetrance, ascertainment and sample size can alter apparent patterns; the pedigree does not establish a universal rule.

**criterion-3 (2 points):** Which association follow-up addresses alternatives?

1. Measure linkage, population structure and environmental covariates and use a controlled mechanism test; association alone does not establish causality.
2. Convert the fictional model directly into clinical risk advice.
3. Assume association excludes all linked variants and environment.

### cell-biology-final-candidate:case-20 — 7 proposed points

Isogenic cells and normalization. Authored form A. Four independently derived clones per genotype share a parent. For one clone, recovered corrected protein is 5 ug, corrected activity 40 nmol/min and viable cells 100 thousand. Recovery scales activity and protein equally. Introduction and correction were tested, but localization and native pathway function are not.

Isogenic cells and normalization. Authored form B. Four independently derived clones per genotype share a parent. For one clone, recovered corrected protein is 4 ug, corrected activity 24 nmol/min and viable cells 50 thousand. Recovery scales activity and protein equally. Introduction and correction were tested, but localization and native pathway function are not.

**criterion-1 (3 points):** Which evidence chain matches assay levels?

1. A DNA sequence measurement is a direct measurement of organism function.
2. DNA establishes the introduced sequence, RNA its measured abundance, and biochemical/cell readouts test distinct downstream hypotheses.
3. A cell phenotype proves a unique protein interaction without measurement.

**criterion-2 (2 points):** Calculate activity per recovered protein on a bare nmol-per-minute-per-ug scale. Report exactly 3 significant figures.

Response scale: `bare declared scale`; absolute tolerance 0.005; relative tolerance 0.



**criterion-3 (2 points):** Which design most strengthens a bounded mechanism claim?

1. Use correction alone to declare every editing artifact impossible.
2. Count technical wells from one clone as independent genotypes.
3. Independent introduction/correction clones with editing controls, viable-cell normalization and orthogonal localization/function follow-up.

### cell-biology-final-candidate:case-21 — 7 proposed points

Binding and downstream response. Authored form A. Ideal independent single-site binding has free ligand L=10 nM and Kd=10 nM; occupancy theta=L/(Kd+L). RTK phosphorylation and a later cell response are measured at different times. An alternate system uses a GPCR; no quantitative gain model is given.

Binding and downstream response. Authored form B. Ideal independent single-site binding has free ligand L=30 nM and Kd=10 nM; occupancy theta=L/(Kd+L). RTK phosphorylation and a later cell response are measured at different times. An alternate system uses a GPCR; no quantitative gain model is given.

**criterion-1 (3 points):** Calculate ideal receptor occupancy as percent. Report exactly 3 significant figures.

Response scale: `%`; absolute tolerance 0.005; relative tolerance 0.



**criterion-2 (2 points):** Which relay distinction is appropriate?

1. RTKs can relay through phosphorylation and GPCRs through heterotrimeric G proteins; branches and amplification depend on context.
2. Each occupied receptor must yield exactly one downstream molecule.
3. All GPCRs are receptor tyrosine kinases with the same branches.

**criterion-3 (2 points):** Which dose/time inference is bounded?

1. An occupancy percentage is automatically the same cell-response percentage.
2. Occupancy, biochemical state and later response are distinct measurements; matching one does not guarantee matching all.
3. A later response uniquely identifies receptor occupancy at every prior time.

### cell-biology-final-candidate:case-22 — 7 proposed points

Pulse, inhibitor and bypass. Authored form A. In each of four independent cultures a constant ligand exposure is verified. A signaling readout at 0,10,30 min is 0,80,20. An upstream perturbation lowers the output with verified target engagement; a downstream bypass restores it. Off-target effects and adaptation measurements remain missing. Use trapezoids on the stated bare readout-minute scale.

Pulse, inhibitor and bypass. Authored form B. In each of four independent cultures a constant ligand exposure is verified. A signaling readout at 0,10,30 min is 0,60,40. An upstream perturbation lowers the output with verified target engagement; a downstream bypass restores it. Off-target effects and adaptation measurements remain missing. Use trapezoids on the stated bare readout-minute scale.

**criterion-1 (3 points):** Calculate trapezoidal area from 0 to 30 min: 10*(y0+y10)/2 + 20*(y10+y30)/2. Report exactly 3 significant figures.

Response scale: `bare declared scale`; absolute tolerance 0.5; relative tolerance 0.



**criterion-2 (2 points):** What can bypass plus target engagement support?

1. Target engagement directly proves every downstream phenotype is on-target.
2. Bypass proves no parallel pathway or off-target effect exists.
3. Consistency with the perturbed process lying upstream of the bypassed output in this model; specificity and pathway uniqueness still need tests.

**criterion-3 (2 points):** Which measurements separate adaptation alternatives?

1. Infer feedback exclusively from a single endpoint.
2. Only add technical repeats of the late output.
3. Matched ligand availability, receptor state, feedback perturbation and orthogonal intervention/time controls in independent cultures.

### cell-biology-final-candidate:case-23 — 7 proposed points

Junctions and matrix ligands. Authored form A. Cells attach to a collagen-presenting matrix. Accessible ligand density is 2 relative units. Integrin-dependent adhesion and a cadherin-dependent neighboring-cell junction are measured separately. Filament turnover and remodeling can occur; accessible density differs between two matrices.

Junctions and matrix ligands. Authored form B. Cells attach to a collagen-presenting matrix. Accessible ligand density is 3 relative units. Integrin-dependent adhesion and a cadherin-dependent neighboring-cell junction are measured separately. Filament turnover and remodeling can occur; accessible density differs between two matrices.

**criterion-1 (3 points):** Which comparison correctly distinguishes filament roles?

1. Actin, microtubules and intermediate filaments have distinct organizations and overlapping integrated functions; all require context and turnover considerations.
2. Microtubules are the sole component of every adhesion junction.
3. All three filament systems are chemically identical and static.

**criterion-2 (2 points):** Which linkage classification fits the stated readouts?

1. Cadherin junctions are universally cell-matrix integrin adhesions.
2. Integrin/focal adhesions link cell to matrix and often actin; cadherin junctions link neighboring cells, with distinct actin or intermediate-filament connections by junction type.
3. Every cell-cell junction is a focal adhesion to collagen.

**criterion-3 (2 points):** What is needed to interpret a matrix-associated difference?

1. Match accessible ligand and consider composition/remodeling separately from mechanics.
2. Declare ligand presentation irrelevant because collagen is named in both conditions.
3. Assume nominal matrix coating guarantees identical accessible ligand.

### cell-biology-final-candidate:case-24 — 7 proposed points

Geometry, stiffness and cell readouts. Authored form A. An ideal small-strain elastic sample has area 2 mm^2, length 10 mm, extension 0.1 mm, and background-corrected force 0.0002 N. E=(force/(area*1e-6))/(extension/length). A nuclear marker rises on the stiffer matrix; traction, accessible ligand, viscoelasticity and fate are unmeasured.

Geometry, stiffness and cell readouts. Authored form B. An ideal small-strain elastic sample has area 2 mm^2, length 10 mm, extension 0.2 mm, and background-corrected force 0.0008 N. E=(force/(area*1e-6))/(extension/length). A nuclear marker rises on the stiffer matrix; traction, accessible ligand, viscoelasticity and fate are unmeasured.

**criterion-1 (3 points):** Calculate E in Pa under the stated elastic assumptions. Report exactly 3 significant figures.

Response scale: `Pa`; absolute tolerance 0.5; relative tolerance 0.



**criterion-2 (2 points):** Which interpretation of the nuclear marker is warranted?

1. It directly measures traction force and proves differentiation.
2. It is a localization-associated readout, not itself force, pathway mechanism or stable cell fate.
3. It proves identical cell states in both conditions.

**criterion-3 (2 points):** Which control set separates stiffness-related alternatives?

1. Match accessible ligand and cell state, measure material time dependence and perturb force transmission with controls.
2. Use nominal polymer concentration as proof that all biochemical variables are matched.
3. Only rename matrices as soft and stiff.

### cell-biology-final-candidate:case-25 — 6 proposed points

DNA content and a damage response. Authored form A. At 24 h a damage challenge yields 40 EdU-positive cells among 800 viable singlets. A separate all-recovered gate has 1000 cells and includes dead material. DNA 4N and p21 rise, but direct CDK activity and longitudinal recovery are unmeasured.

DNA content and a damage response. Authored form B. At 24 h a damage challenge yields 36 EdU-positive cells among 600 viable singlets. A separate all-recovered gate has 1000 cells and includes dead material. DNA 4N and p21 rise, but direct CDK activity and longitudinal recovery are unmeasured.

**criterion-1 (2 points):** Which checkpoint statement is bounded?

1. p21 abundance directly reports the activity of every CDK.
2. Checkpoint signaling can restrain cyclin-CDK transitions; the marker pattern alone is not a direct CDK assay.
3. DNA 4N means every cell is currently undergoing mitosis.

**criterion-2 (2 points):** Calculate EdU-positive percent with the specified viable-singlet denominator. Report exactly 3 significant figures.

Response scale: `%`; absolute tolerance 0.005; relative tolerance 0.



**criterion-3 (2 points):** Which follow-up tests arrest rather than cell loss?

1. Use a single 4N peak to declare permanent arrest.
2. Longitudinal viable-cell counts, re-entry after challenge removal and orthogonal phase/death readouts with controls.
3. Replace the viable denominator with all recovered material without stating the change.

### cell-biology-final-candidate:case-26 — 6 proposed points

Re-entry and apoptosis-associated evidence. Authored form A. Following withdrawal/refeeding, EdU returns to 38% in one group; in a damage group it stays low through 72 h with p21 and beta-gal-associated features. Caspase positivity is 15% among all recovered cells. Longer follow-up and joint single-cell marker identities are absent.

Re-entry and apoptosis-associated evidence. Authored form B. Following withdrawal/refeeding, EdU returns to 42% in one group; in a damage group it stays low through 72 h with p21 and beta-gal-associated features. Caspase positivity is 12% among all recovered cells. Longer follow-up and joint single-cell marker identities are absent.

**criterion-1 (2 points):** Which state inference respects the observation window?

1. Any beta-gal positivity proves permanent senescence.
2. Re-entry supports reversibility in the first group; persistent arrest with markers is senescence-associated evidence, not proof of permanent fate.
3. Failure to re-enter by 72 h proves that every cell is dead.

**criterion-2 (2 points):** Which apoptosis-route description is appropriate?

1. Extrinsic death signaling can never activate caspases.
2. Caspase positivity uniquely proves a mitochondrial initiating event.
3. Intrinsic mitochondrial and extrinsic death-receptor routes can activate caspases; this shared readout alone does not identify the initiating route.

**criterion-3 (2 points):** Which analysis separates mixed-state alternatives?

1. Add marginal marker percentages to claim a pure population.
2. Track viable loss and joint orthogonal proliferation/death markers longitudinally; separate denominators and avoid inferring marker co-occurrence from marginals.
3. Treat all recovered cells as viable singlets without gates.

### cell-biology-final-candidate:case-27 — 6 proposed points

Clonal evidence and potency. Authored form A. A fictional cell clone serially produces cells with its original phenotype and several lineages in a restricted tissue context. A marker signature reaches 80% in a culture, but a defined mature-function assay remains below its positive-control threshold. Neighboring cells, matrix and exposure duration vary between conditions.

Clonal evidence and potency. Authored form B. A fictional cell clone serially produces cells with its original phenotype and several lineages in a restricted tissue context. A marker signature reaches 75% in a culture, but a defined mature-function assay remains below its positive-control threshold. Neighboring cells, matrix and exposure duration vary between conditions.

**criterion-1 (2 points):** Which distinction fits the clonal evidence?

1. Marker positivity alone proves unlimited self-renewal and totipotency.
2. Serial maintenance tests self-renewal and lineage production tests differentiation; restricted lineages do not establish totipotency.
3. Differentiation and self-renewal are interchangeable measurements.

**criterion-2 (2 points):** Which identity claim is warranted?

1. The signature proves mature tissue function regardless of the assay.
2. Marker-associated and clonal evidence must be separated from the measured mature-function shortfall.
3. A single marker universally defines every developmental lineage.

**criterion-3 (2 points):** Which environmental interpretation fits the conditions?

1. Signals, neighboring cells, matrix and timing can each affect lineage-associated outcomes and require controlled separation.
2. Exposure duration is irrelevant if the same nominal ligand is used.
3. Only DNA sequence can affect the measured lineage outcome.

### cell-biology-final-candidate:case-28 — 6 proposed points

Factorial lineage-associated comparison. Authored form A. Four independent culture preparations are split across matrix low/high and signal off/on. Preparation-mean marker percentages are low/off=10, low/on=20, high/off=15, high/on=40. Use difference-in-differences (high/on-high/off)-(low/on-low/off) in percentage points. Matched function is near background; uncertainty and longer-term safety are absent.

Factorial lineage-associated comparison. Authored form B. Four independent culture preparations are split across matrix low/high and signal off/on. Preparation-mean marker percentages are low/off=10, low/on=25, high/off=15, high/on=45. Use difference-in-differences (high/on-high/off)-(low/on-low/off) in percentage points. Matched function is near background; uncertainty and longer-term safety are absent.

**criterion-1 (2 points):** Calculate the descriptive interaction contrast on a bare percentage-point scale. Report exactly 3 significant figures.

Response scale: `bare declared scale`; absolute tolerance 0.005; relative tolerance 0.



**criterion-2 (2 points):** Which follow-up best separates marker association and function?

1. Treat a marker as the positive-control threshold for an unrelated function assay.
2. Pool all cells across preparations to infer universal differentiation.
3. Match ligand presentation and cell state, retain preparation blocking, and assay marker and a defined function with independent controls.

**criterion-3 (2 points):** Which translation boundary is justified?

1. A positive marker makes safety and clinical oversight unnecessary.
2. The interaction alone demonstrates clinical regeneration.
3. A synthetic in-vitro association cannot establish therapeutic benefit; reproducibility, function, safety and appropriate oversight would be needed for a clinical claim.

## Unscored written reasoning and review guide

For each experimental case, explain the strongest supported claim, a specific alternative and a matched follow-up with its independent unit. For each calculation state the transformation, assumptions and denominator. Draft adequate-work descriptors require a reproducible method, compatible scale and bounded conclusion; partial descriptors require identifying the missing link, and absent/incompatible work receives no human evidence credit. These descriptors are an unscored guide: a qualified reviewer must decide the human component, weights, fairness and grading process before this can represent full objective performance. A machine score must not be presented as mastery of written explanations or design.

## Provenance and activation

Original cases, synthetic observations and explanations: CC BY 4.0 with substantial Codex assistance. Existing original course readings provide context and their hashes are bound. No public practice stem/key is relabeled as a confidential exam. No outside prose, problem,figure or dataset copied or adapted. The registered NIST SI-constant reference supports the membrane temperature correction and original coefficient recalculation; no new paper/identifier is introduced. This is a paper/data exercise, not a wet-lab protocol or clinical result.

Independent recalculation and grader review, qualified scientific/assessment review, manual accessibility/fairness review, measured workload/time accommodations, operator conduct/release/attempt decisions and immutable archive/appeal replay evidence remain required. Same-AI checks do not satisfy these gates. No exam is activated.


## Protected delivery gap

The protected assignment route currently serves a fixed source and rejects practice variant tokens. It does not select/replay these authored forms for an exam attempt. Same-AI tests separately exercise standalone signed A/B replay and temporary fixed-form-A protected delivery with randomization removed from a disposable fixture. Neither is evidence that this two-form candidate can be activated unchanged. Protected variant delivery, retake selection, source archiving and human component policies remain explicit activation gates.

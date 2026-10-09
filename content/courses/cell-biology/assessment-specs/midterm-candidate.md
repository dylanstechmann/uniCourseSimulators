# Midterm candidate: cumulative evidence and models

**State:** inactive candidate for review, authored with substantial Codex assistance for Biology 0.28.0. The course remains partial, unreviewed and formative-only. No live submission route, course grade, deadline, time limit or attempt policy is set. Workload has not been measured. Keys and candidate-specific checks remain outside Git; no independent scientific/numerical/assessment/accessibility reviewer approved the form.

This draft has 16 multi-field cases and 100 proposed machine-scored points. It links 34 objective occurrences across 33 distinct objectives in 16 topic lessons. An objective reused by two lessons counts as two links and one unique objective. Field-level metadata makes the mapping inspectable. These checks assess the stated calculations and categorical decisions; they do not grade a learner's written explanation, design, uncertainty, script or plot. Coverage labels do not establish performance at every objective verb or a complete summative assessment.

## Assigned forms, observations and models

The [observation table](midterm-candidate-observations.csv) lists original synthetic case/form measurements with named scales. Contexts below supply needed assumptions, formulas and independent units. Values are deterministic teaching inputs, not physical observations or calibrated uncertainty. Forms A/B use fixed authored values and the platform's authored-variant/source/token replay contract. Both review DTO sets are public and answer-free; their keys are external. A future served field refers to the form named in its case, and the selected signed variant must be replayed when submitted. The draft does not select a production retake policy or prove immutable historical archiving exists.

Numeric fields state three significant figures where requested, a compatible unit if present and a response tolerance. Tolerances are grading rules, not uncertainty. Bare scales are explicitly named and have no unit conversion/dimension enforcement. Categorical fields score one option, not prose. Fields carry the point weights shown; partial credit is independent by field. Invalid fields receive no points or a validation error; other valid fields may earn their stated partial credit. Choices are numbered for this paper review; a future interface uses its own controls. No field needs an image or color distinction.

Experimental cases retain the named culture/preparation/clone/batch unit. Cells, repeated aliquots, fields and technical wells are not extra independent units. A mean/difference is descriptive unless an uncertainty model and justified analysis are supplied. Optical overlap is not direct binding; a molecular/cell marker is not native causality, stable identity, mature function or clinical benefit. Positive controls, backgrounds, input/loading references and loss accounting address different alternatives.

## Case packet: authored forms A and B

### cell-biology-midterm-candidate:case-01 — 8 proposed points

Ionizable substitution in an assembly. Authored form A. A fictional protein has a aspartate side chain on a water-exposed surface at pH 7; its measured pKa is 4. It is changed to alanine. Other covalent bonds remain intact; assembly has not been measured.

Ionizable substitution in an assembly. Authored form B. A fictional protein has a glutamate side chain on a water-exposed surface at pH 7; its measured pKa is 4. It is changed to alanine. Other covalent bonds remain intact; assembly has not been measured.

**criterion-1 (3 points):** Which description distinguishes the mutation from ordinary molecular association?

1. The mutation only changes noncovalent contacts, never structure.
2. Association necessarily changes every peptide bond.
3. The side-chain covalent structure changes; reversible association can occur without new covalent bonds.

**criterion-2 (3 points):** What bounded prediction follows at the specified pH?

1. Alanine adds an ionized carboxylate at pH 7.
2. The original side chain is predominantly negative; alanine removes that charge and may change assembly.
3. Charge loss proves the protein cannot assemble.

**criterion-3 (2 points):** Which chemical feature is directly removed by this substitution?

1. Every backbone amide.
2. The side-chain carboxyl group, without necessarily removing the backbone amide.
3. A side-chain phosphate that neither residue contains.

### cell-biology-midterm-candidate:case-05 — 6 proposed points

A titratable group in water. Authored form A. An isolated carboxyl group in water has pKa 4.5; the solution pH is 3.5. Use [A-]/[HA] = 10^(pH-pKa), with no coupled groups. A separate nonpolar solute aggregates in water without new covalent bonds.

A titratable group in water. Authored form B. An isolated carboxyl group in water has pKa 4.5; the solution pH is 5.5. Use [A-]/[HA] = 10^(pH-pKa), with no coupled groups. A separate nonpolar solute aggregates in water without new covalent bonds.

**criterion-1 (3 points):** Which interpretation of the nonpolar aggregate is justified?

1. Water-mediated hydrophobic association is plausible; aggregation alone does not establish covalent bonding.
2. Nonpolar solutes must become permanently charged.
3. Aggregation proves new peptide bonds form.

**criterion-2 (3 points):** Calculate the ratio of deprotonated to protonated group on a bare ratio scale. Report exactly 3 significant figures.

Response scale: `bare declared scale`; absolute tolerance 0.005, relative tolerance 0.



### cell-biology-midterm-candidate:case-06 — 6 proposed points

Protein quantity and function. Authored form A. A buried hydrophobic residue is replaced by a charged residue. In matched recovered protein, reference abundance is 100 and variant abundance is 50 arbitrary amount units. Total activities are 800 and 400 arbitrary rate units. Folding measurements and localization are missing.

Protein quantity and function. Authored form B. A buried hydrophobic residue is replaced by a charged residue. In matched recovered protein, reference abundance is 100 and variant abundance is 40 arbitrary amount units. Total activities are 800 and 160 arbitrary rate units. Folding measurements and localization are missing.

**criterion-1 (3 points):** Which prediction respects residue environment and missing measurements?

1. Any charged substitution necessarily increases native folding.
2. A buried charge may disrupt stability or packing, but the actual fold and localization need measurement.
3. A buried charge proves loss of all activity in every context.

**criterion-2 (3 points):** Calculate variant/reference specific activity: (variant activity/amount)/(reference activity/amount), a bare ratio. Report exactly 3 significant figures.

Response scale: `bare declared scale`; absolute tolerance 0.005, relative tolerance 0.



### cell-biology-midterm-candidate:case-02 — 6 proposed points

Passive potassium and transport classes. Authored form A. Only K+ is permeant in an ideal membrane. Inside K+ is 100 mM; outside is 10 mM; at 37 C use E_K = 61.5 log10(outside/inside) mV. Membrane voltage is 0 mV. A separate carrier moves a substrate uphill only when coupled to ATP hydrolysis.

Passive potassium and transport classes. Authored form B. Only K+ is permeant in an ideal membrane. Inside K+ is 120 mM; outside is 12 mM; at 37 C use E_K = 61.5 log10(outside/inside) mV. Membrane voltage is 0 mV. A separate carrier moves a substrate uphill only when coupled to ATP hydrolysis.

**criterion-1 (3 points):** Calculate E_K using the stipulated rounded coefficient. Report exactly 3 significant figures.

Response scale: `mV`; absolute tolerance 0.05, relative tolerance 0.



**criterion-2 (3 points):** Classify the ATP-dependent uphill carrier.

1. Passive transport because all carriers are passive.
2. Simple diffusion through the lipid bilayer.
3. Active transport; downhill carrier-mediated flux would be facilitated diffusion.

### cell-biology-midterm-candidate:case-07 — 6 proposed points

Compartment boundary evidence. Authored form A. A fictional protein with a cleavable ER-targeting peptide enters a lumen. Intact vesicles protect 82% of its immunoreactivity from added protease; detergent plus protease removes the signal. A cytosolic marker is digested without detergent. Vesicle recovery is matched. These are biochemical aliquots, not independent living cells.

Compartment boundary evidence. Authored form B. A fictional protein with a cleavable ER-targeting peptide enters a lumen. Intact vesicles protect 78% of its immunoreactivity from added protease; detergent plus protease removes the signal. A cytosolic marker is digested without detergent. Vesicle recovery is matched. These are biochemical aliquots, not independent living cells.

**criterion-1 (3 points):** What topology follows if the stated targeting and translocation succeed?

1. The protein must cross the bilayer at every secretory step.
2. A cleaved ER peptide necessarily places the mature protein in the nucleus.
3. The mature soluble protein is on the luminal side and remains topologically outside the cytosol.

**criterion-2 (3 points):** What is the bounded protease conclusion?

1. Protection proves a unique living-cell organelle and direct binding.
2. Protection is consistent with enclosed antigen; detergent sensitivity and markers address integrity, not exact native location by themselves.
3. The cytosolic digestion control is interchangeable with vesicle integrity.

### cell-biology-midterm-candidate:case-08 — 6 proposed points

Receptor recycling and cargo sorting. Authored form A. Pulse-labeled extracellular cargo binds equally to reference and perturbed cells at time zero. At a matched chase, receptor returns to the surface in both; cargo in a degradative compartment changes from 60% to 20%. Total recovered label and new synthesis are matched, but degradation fragments and spatial resolution are not measured.

Receptor recycling and cargo sorting. Authored form B. Pulse-labeled extracellular cargo binds equally to reference and perturbed cells at time zero. At a matched chase, receptor returns to the surface in both; cargo in a degradative compartment changes from 60% to 30%. Total recovered label and new synthesis are matched, but degradation fragments and spatial resolution are not measured.

**criterion-1 (3 points):** Which route preserves topology?

1. A surface receptor and all its cargo must always share their terminal destination.
2. Recycling requires cargo to become cytosolic by membrane inversion.
3. Endocytosed luminal cargo can remain enclosed while its receptor recycles to the surface.

**criterion-2 (3 points):** What can the matched measurements support?

1. A late compartment percentage proves changed transcription.
2. Equal initial binding proves normal sorting and degradation.
3. A redistribution consistent with altered sorting; unresolved label loss and compartment assignment still need controls.

### cell-biology-midterm-candidate:case-03 — 6 proposed points

Catalysis and coupling. Authored form A. Use v = Vmax*S/(Km+S), with Vmax 80 arbitrary rate units, Km 2 mM and S 2 mM. At matched conditions reaction X has deltaG +12 kJ/mol and coupled reaction Y has deltaG -20 kJ/mol; stoichiometry is 1:1.

Catalysis and coupling. Authored form B. Use v = Vmax*S/(Km+S), with Vmax 90 arbitrary rate units, Km 3 mM and S 6 mM. At matched conditions reaction X has deltaG +12 kJ/mol and coupled reaction Y has deltaG -25 kJ/mol; stoichiometry is 1:1.

**criterion-1 (3 points):** Calculate v on the declared bare rate-unit scale. Report exactly 3 significant figures.

Response scale: `bare declared scale`; absolute tolerance 0.005, relative tolerance 0.



**criterion-2 (3 points):** Calculate the net deltaG per mole of coupled events. Report exactly 3 significant figures.

Response scale: `kJ/mol`; absolute tolerance 0.005, relative tolerance 0.



### cell-biology-midterm-candidate:case-09 — 6 proposed points

Active enzyme and equilibrium. Authored form A. A purified catalyst changes the activation barrier without changing initial/final state free energies. In an ideal initial-rate assay active enzyme is 2 nM, kcat 10 per second, S 4 mM and Km 4 mM; v = kcat*E*S/(Km+S). No inhibition or enzyme loss occurs.

Active enzyme and equilibrium. Authored form B. A purified catalyst changes the activation barrier without changing initial/final state free energies. In an ideal initial-rate assay active enzyme is 3 nM, kcat 12 per second, S 4 mM and Km 2 mM; v = kcat*E*S/(Km+S). No inhibition or enzyme loss occurs.

**criterion-1 (3 points):** Which effect is compatible with a catalyst?

1. A catalyst makes every uphill reaction have a negative deltaG.
2. Faster forward and reverse equilibration with unchanged equilibrium constant for the same states.
3. A catalyst changes equilibrium by consuming itself irreversibly.

**criterion-2 (3 points):** Calculate initial v on a bare nM-per-second scale. Report exactly 3 significant figures.

Response scale: `bare declared scale`; absolute tolerance 0.005, relative tolerance 0.



### cell-biology-midterm-candidate:case-10 — 6 proposed points

Inhibitor model and optical control. Authored form A. An initial-rate fit gives Vmax 100 and apparent Km 4 mM with inhibitor; use v=Vmax*S/(Km+S) at S 2 mM. Without inhibitor Vmax is the same and Km is smaller. Blank wells show negligible optical interference; direct binding and uncertainty estimates are unavailable.

Inhibitor model and optical control. Authored form B. An initial-rate fit gives Vmax 120 and apparent Km 6 mM with inhibitor; use v=Vmax*S/(Km+S) at S 3 mM. Without inhibitor Vmax is the same and Km is smaller. Blank wells show negligible optical interference; direct binding and uncertainty estimates are unavailable.

**criterion-1 (3 points):** Calculate the fitted inhibited initial rate on the bare rate-unit scale. Report exactly 3 significant figures.

Response scale: `bare declared scale`; absolute tolerance 0.005, relative tolerance 0.



**criterion-2 (3 points):** Which statement is warranted by the parameter pattern and controls?

1. It is consistent with an ideal competitive pattern; the fit and optical blank do not prove a molecular binding route.
2. An optical blank proves a particular active-site structure.
3. The pattern proves irreversible enzyme destruction.

### cell-biology-midterm-candidate:case-11 — 6 proposed points

Sampling and overlap. Authored form A. For a conventional image estimate lateral resolution d=0.61*lambda/NA with lambda 500 nm and NA 1. Sample-plane pixel size is 100 nm. Two fluorescent channels overlap within the optical spot; single-label controls show measurable bleed-through.

Sampling and overlap. Authored form B. For a conventional image estimate lateral resolution d=0.61*lambda/NA with lambda 600 nm and NA 1.2. Sample-plane pixel size is 100 nm. Two fluorescent channels overlap within the optical spot; single-label controls show measurable bleed-through.

**criterion-1 (3 points):** Calculate nominal lateral resolution in nm. This estimate is distinct from pixel size. Report exactly 3 significant figures.

Response scale: `nm`; absolute tolerance 0.5, relative tolerance 0.



**criterion-2 (3 points):** Which follow-up and conclusion fit this image?

1. Increase magnification and declare direct binding from overlap.
2. Correct spectral cross-talk with matched controls; overlap at optical resolution does not establish direct molecular binding.
3. Discard single-label controls because colors differ on screen.

### cell-biology-midterm-candidate:case-12 — 6 proposed points

Recovery and enrichment. Authored form A. Input target marker activity is 200 units; the collected fraction contains 80 units. Fraction total protein is 2 mg. A second compartment marker is also detected. Only one collected fraction is supplied; missing fractions and rupture controls are absent.

Recovery and enrichment. Authored form B. Input target marker activity is 250 units; the collected fraction contains 75 units. Fraction total protein is 2 mg. A second compartment marker is also detected. Only one collected fraction is supplied; missing fractions and rupture controls are absent.

**criterion-1 (3 points):** Calculate target-marker recovery as a percentage of input. Report exactly 3 significant figures.

Response scale: `%`; absolute tolerance 0.005, relative tolerance 0.



**criterion-2 (3 points):** Which design can address the current limitations?

1. Treat the fraction protein mass as a count of independent cultures.
2. Use only the target marker and call the fraction pure.
3. Collect all fractions and input for mass balance, multiple compartment markers and integrity controls; enrichment alone is not purity.

### cell-biology-midterm-candidate:case-13 — 6 proposed points

Polarity and isotope generations. Authored form A. The template is 5-prime GACTA 3-prime. Polymerase extends a primer by adding to its 3-prime end. After heavy-to-light transfer, controlled isotope-density generation 1 has only hybrid-density DNA and generation 2 has hybrid plus light DNA; density resolution controls pass.

Polarity and isotope generations. Authored form B. The template is 5-prime ACGTA 3-prime. Polymerase extends a primer by adding to its 3-prime end. After heavy-to-light transfer, controlled isotope-density generation 1 has only hybrid-density DNA and generation 2 has hybrid plus light DNA; density resolution controls pass.

**criterion-1 (3 points):** Which description correctly preserves strand polarity and synthesis?

1. Polymerase makes the leading strand by adding to its 5-prime end.
2. Both aligned strands have the same 5-prime to 3-prime direction.
3. The aligned complement runs 3-prime to 5-prime; a newly made strand grows 5-prime to 3-prime, with fragments on the lagging side.

**criterion-2 (3 points):** Which model fits the specified resolved generations?

1. All three models predict exactly the same resolved generations.
2. Conservative replication predicts only hybrid DNA in generation 1.
3. Semiconservative replication; the second generation helps distinguish the ideal dispersive prediction.

### cell-biology-midterm-candidate:case-14 — 6 proposed points

Lesion signal and repair. Authored form A. A bulky-adduct assay has matched input and extraction standards. At a fixed time lesion signal is 20 units in reference and 60 in a repair perturbation; rescue brings it near reference. Mutation counts, survival and independent pathway activity are unmeasured.

Lesion signal and repair. Authored form B. A bulky-adduct assay has matched input and extraction standards. At a fixed time lesion signal is 20 units in reference and 55 in a repair perturbation; rescue brings it near reference. Mutation counts, survival and independent pathway activity are unmeasured.

**criterion-1 (3 points):** Which distinction and pathway hypothesis is appropriate?

1. Polymerase proofreading acts during synthesis; bulky-adduct excision is a plausible different repair pathway requiring specific tests.
2. Every bulky lesion is removed solely by polymerase proofreading.
3. Proofreading and post-replicative mismatch repair are the same timed process.

**criterion-2 (3 points):** What does the rescue support within these measurements?

1. Perturbation-associated lesion-signal change; mutation frequency and a unique native mechanism remain unmeasured.
2. Rescue proves zero off-target effects or survival selection.
3. A lesion signal is directly the mutation frequency per genome.

### cell-biology-midterm-candidate:case-15 — 6 proposed points

Chromatin and independent units. Authored form A. Four independent cultures per state are each split into three technical aliquots. Accessibility rises by 40% and matched RNA by 25% between states. A histone mark also increases; no endogenous element perturbation has been done.

Chromatin and independent units. Authored form B. Four independent cultures per state are each split into three technical aliquots. Accessibility rises by 30% and matched RNA by 20% between states. A histone mark also increases; no endogenous element perturbation has been done.

**criterion-1 (3 points):** Which chromatin interpretation is bounded?

1. Nucleosomes never alter accessibility.
2. Any mark increase proves an irreversible transcriptional switch.
3. Accessibility and a mark can be associated with state; a mark is not by itself a transcriptional switch.

**criterion-2 (3 points):** Which analysis and causal follow-up fit the units?

1. Treat twelve aliquots as twelve independent cultures and infer causality from correlation.
2. Summarize aliquots within four cultures per state and perturb the endogenous element with matched controls and RNA/readout follow-up.
3. Use a plasmid alone to prove endogenous element necessity.

### cell-biology-midterm-candidate:case-04 — 8 proposed points

Expression and controls. Authored form A. A fictional construct is transcribed to mRNA and translated to protein. Three independent cultures have background-corrected reporter values 10, 12, 14; an untreated reference mean is 8. Positive assay control and a no-reporter negative control pass; input/loading measurements are not supplied.

Expression and controls. Authored form B. A fictional construct is transcribed to mRNA and translated to protein. Three independent cultures have background-corrected reporter values 12, 15, 18; an untreated reference mean is 9. Positive assay control and a no-reporter negative control pass; input/loading measurements are not supplied.

**criterion-1 (3 points):** Which information path fits the model?

1. RNA synthesis and peptide synthesis are the same chemical reaction.
2. Protein must first be reverse translated directly into genomic DNA.
3. DNA is transcribed to RNA; ribosomes read an mRNA frame to synthesize a polypeptide.

**criterion-2 (3 points):** Which control is missing for an abundance-normalized comparison?

1. A matched input/loading measurement; positive and negative controls address different assay questions.
2. No loading control is needed because the reporter is fluorescent.
3. A second positive control automatically replaces loading.

**criterion-3 (2 points):** Calculate the descriptive difference between the culture mean and reference on the bare reporter scale. Report exactly 3 significant figures.

Response scale: `bare declared scale`; absolute tolerance 0.005, relative tolerance 0.



### cell-biology-midterm-candidate:case-16 — 6 proposed points

ChIP input and cis claims. Authored form A. The measured input aliquot is fraction 0.01 of total input; Ct_input 20, Ct_IP 22. Under equal doubling efficiency use percent input=100*fraction*2^(Ct_input-Ct_IP). IgG and negative-locus controls pass. A matched plasmid deletion lowers reporter output; the endogenous locus has not been edited.

ChIP input and cis claims. Authored form B. The measured input aliquot is fraction 0.02 of total input; Ct_input 20, Ct_IP 23. Under equal doubling efficiency use percent input=100*fraction*2^(Ct_input-Ct_IP). IgG and negative-locus controls pass. A matched plasmid deletion lowers reporter output; the endogenous locus has not been edited.

**criterion-1 (3 points):** Calculate simplified ChIP percent input. Report exactly 3 significant figures.

Response scale: `%`; absolute tolerance 0.0005, relative tolerance 0.



**criterion-2 (3 points):** Which inference separates the two assays?

1. IgG controls replace input and PCR efficiency controls.
2. ChIP plus plasmid deletion proves direct binding and endogenous necessity.
3. Enrichment supports occupancy-associated evidence and the plasmid tests sequence activity in that context; neither alone proves direct binding or endogenous necessity.

## Unscored written reasoning and review guide

For each experimental case, explain the strongest supported claim, a specific alternative and a matched follow-up with its independent unit. For each calculation state the transformation, assumptions and denominator. Draft adequate-work descriptors require a reproducible method, compatible scale and bounded conclusion; partial descriptors require identifying the missing link, and absent/incompatible work receives no human evidence credit. These descriptors are an unscored guide: a qualified reviewer must decide the human component, weights, fairness and grading process before this can represent full objective performance. A machine score must not be presented as mastery of written explanations or design.

## Provenance and activation

Original cases, synthetic observations and explanations: CC BY 4.0 with substantial Codex assistance. Existing original course readings provide context and their hashes are bound. No public practice stem/key is relabeled as a confidential exam. No outside prose, problem,figure or dataset copied or adapted. The registered NIST SI-constant reference supports the membrane temperature correction and original coefficient recalculation; no new paper/identifier is introduced. This is a paper/data exercise, not a wet-lab protocol or clinical result.

Independent recalculation and grader review, qualified scientific/assessment review, manual accessibility/fairness review, measured workload/time accommodations, operator conduct/release/attempt decisions and immutable archive/appeal replay evidence remain required. Same-AI checks do not satisfy these gates. No exam is activated.


## Protected delivery gap

The protected assignment route currently serves a fixed source and rejects practice variant tokens. It does not select/replay these authored forms for an exam attempt. Same-AI tests separately exercise standalone signed A/B replay and temporary fixed-form-A protected delivery with randomization removed from a disposable fixture. Neither is evidence that this two-form candidate can be activated unchanged. Protected variant delivery, retake selection, source archiving and human component policies remain explicit activation gates.

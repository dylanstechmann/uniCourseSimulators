# Instructor-style feedback templates

These templates guide feedback for the current public formative material. The software's current deterministic graders do not inspect prose or reliably infer a learner's reasoning; select a template only when the saved response provides the stated evidence. A response that happens to select the correct option does not prove a sound explanation. Full explanations follow the public-practice release policy and must not be copied into a restricted assessment key.

## Layered response format

1. **Confirm or diagnose:** name the result and the part of the learner's submitted work that supports the judgment.
2. **Targeted hint:** point to the next conceptual operation without repeating the answer.
3. **Possible misconception:** attach a catalog ID only when the response provides evidence for it; otherwise say that the cause is uncertain.
4. **Next step:** ask for one concrete revision, calculation, control, or comparison.
5. **Solution release:** show a worked explanation only under the item's stated release policy; it is public for current practice items.
6. **Source link:** return the exact lesson and the relevant public comparator from the source map, without suggesting endorsement.

## Templates by evidence pattern

### Correct result with a sound reasoning chain

> Your conclusion follows from **[specific submitted evidence]** because **[chemical/model/experimental relationship]**. You also limited the claim to **[tested condition]**. Next, check whether **[one assumption or alternative explanation]** could change the interpretation.

### Correct result with weak or accidental reasoning

> The selected result is consistent with the key, but the response does not yet show why it follows. Before treating it as a reliable method, identify **[the relevant charge, gradient, control, or measurement]** and explain how it changes the prediction.

### Arithmetic error

> Your setup uses the requested quantity, but the numerical result changes at **[operation or substitution]**. Keep the equation and units visible, recompute that step, then check whether the rounded answer is consistent with the unrounded value.

### Unit or dimensional error

> The numerical magnitude may be plausible, but **[submitted unit]** does not match the requested quantity. Write the units beside every term and check whether the final dimensions reduce to **[target dimension]**.

### Misapplied equation or model

> This equation applies only when **[stated model assumptions]**. Your response includes **[observed condition]**, which may violate that assumption. State the assumptions first, then choose a model or comparison that matches the system.

### Unsupported biological claim

> The observation supports **[narrow measured result]**, but the response goes further by claiming **[broader biological conclusion]**. Add the missing evidence that connects those levels, or narrow the claim to the measured property and tested system.

### Correlation treated as causation

> These measurements vary together, but the comparison does not yet isolate which change caused the response. Identify a perturbation, matched comparison, and rescue or orthogonal measurement that would discriminate the competing explanations.

### Missing experimental control

> The readout is interpretable only if **[assay property or background]** is checked. Add **[specific positive, negative, vehicle, loading, or delivery control]** and state which failure it would reveal.

### Enzyme rate confused with thermodynamic favorability

> The response correctly identifies **[observed rate change]**, but a rate increase alone does not show that the reaction became more favorable or that its equilibrium changed. Separate the activation barrier from net ΔG, then state whether a physically coupled reaction or a new condition was measured.

### Kinetic parameter treated as a direct binding measurement

> The fitted **[Km or apparent Km]** describes the stated kinetic model and conditions. It equals a binding dissociation constant only under additional assumptions. Write the mechanism and rate constants used, check the substrate range and fit uncertainty, then limit the claim to the parameter actually estimated.

### Inhibitor pattern treated as a proven molecular mechanism

> The curve is **[consistent with the named simple model pattern]**, but rate data alone do not identify a physical binding site. Check **[vehicle, optical interference, enzyme stability, and tested concentration range]**, then propose an orthogonal binding or recovery test that distinguishes the alternatives.

### Membrane-enclosure result mistaken for a complete localization mechanism

> Your protease-protection pattern supports **[membrane-enclosed access under the tested conditions]** because **[marker and detergent controls]**. It does not yet identify **[the exact targeting/import step or compartment]**. Next, add **[an orthogonal marker, matched synthesis measurement, or time-course]** and limit the claim to what that test resolves.

### Cargo binding mistaken for successful sorting

> The binding measurement supports **[cargo recognition]**, while **[compartment distribution or secretion result]** shows that the later route may differ. Check **[receptor amount/localization and fraction recovery]**, then ask whether a rescue restores delivery. A binding result alone does not establish the final destination.

### Incomplete but promising approach

> The first step is useful: **[specific valid part]**. The missing link is **[unanswered criterion]**. Complete that link with **[a calculation, measurement, or control]**, then write a conclusion limited to the evidence you have.

### Image overlap treated as molecular interaction

> The images support **[measured signal proximity]** at approximately **[stated optical scale]** under these labeling conditions. They do not establish direct binding or causal recruitment. Check **[single-label/specificity controls]**, then choose an interaction assay or perturbation that tests the stronger claim.

### Fraction enrichment treated as purity or intact-cell localization

> The data support **[measured marker distribution or normalized enrichment]** with **[stated denominator, recovery, and contaminant markers]**. A pellet is a mixture after homogenization; it does not alone establish purity, intact-cell localization, or function. Add **[input/recovery/integrity control]** and an orthogonal intact-cell measurement.

### Strand polarity or replication-model inference

> Your sequence **[matches or reverses]** the stated template orientation. Pair the bases first, then label the new strand antiparallel to the template. For model discrimination, compare the predicted molecule classes after **[generation]**; a first-generation intermediate class alone is shared by more than one model.

### Lesion-signal change interpreted as mutation frequency

> The assay reports **[measured lesion-associated signal]** under **[tested perturbation, time, and normalization]**. Similar starting signal and a matched rescue make a factor-dependent change more plausible, but this readout does not directly count heritable mutations or establish direct catalysis. Check **[DNA recovery, viability, cell-cycle state, and an orthogonal lesion or mutation assay]** before extending the claim.

### Chromatin accessibility or histone mark treated as transcriptional causality

> The data show **[accessibility/mark]** and **[RNA measurement]** in **[cell state and condition]**. Their co-variation supports an association in these samples; it does not establish that the mark caused transcription or that the nearest gene is the target. Identify the independent culture count, then propose a defined endogenous-element perturbation, matched control, target-RNA readout, and rescue or orthogonal test.

### ChIP-qPCR or reporter result overinterpreted

> The ChIP-qPCR result estimates **[locus enrichment relative to input]** with **[antibody and controls]**; the reporter result measures **[construct activity in its assay context]**. Neither alone establishes direct motif contact or endogenous-locus causality. Check input, IgG/mock pull-down, positive and negative loci, amplification specificity, construct normalization, and independent biological replicates; next test **[native-locus perturbation or orthogonal binding evidence]**.

## Delivery and uncertainty rules

- Quote or point to the learner's own words, numbers, or selected fields; do not invent evidence about their reasoning.
- Separate the deterministic points from any interpretive feedback. A provisional language model may not silently change an automatic grade.
- State when a response is ambiguous or the rubric does not cover it; route it for human review when a graded workflow exists.
- Use the exact lesson ID and relevant source-map link. Do not cite a comparator as proof that the learner's conclusion is correct.
- Keep full solutions hidden until the item's configured release point. The current course contains public practice solutions only; it contains no secure exam material.

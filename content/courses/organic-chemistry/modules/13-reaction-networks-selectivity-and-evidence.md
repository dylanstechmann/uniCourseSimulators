# Reaction networks, selectivity and evidence

## Learning objectives

1. Calculate conversion and competing product amounts in a stipulated activated-intermediate network.
2. Distinguish branching selectivity, recovery, analytical response and stereochemical composition.
3. Evaluate product claims and the limitations of the preserved amide self-assessment case.

## Activation creates a new competition

A proposed activation step can make an acyl-transfer pathway accessible without guaranteeing the desired product. An activated intermediate may be consumed by the intended donor, water or another competing species. A balanced net equation for amide formation does not enumerate those alternatives or establish their relative rates. The intermediate's formation, consumption and any remaining starting material need separate accounting.

Use a synthetic network I→P and I→H. I is a hypothetical activated intermediate; P is the designated target and H a competing hydrolysis-equivalent product. Stipulate constant effective first-order rates a=0.040 and b=0.010 min⁻¹. Start with I₀=1.0 in arbitrary amount units and P₀=H₀=0. The labels are a paper network, not actual reagent or biological species identities.

The component balances are dI/dt=−(a+b)I, dP/dt=aI and dH/dt=bI. Their sum has zero derivative, so I+P+H remains one. The initial target-formation rate is 0.040 amount units/min and competing rate 0.010. Constant rates here summarize a supplied environment; they do not follow from the word “activated” alone.

## Conversion and branching

Remaining intermediate is I=exp(−0.050t). Its half-life is ln 2/0.050≈13.862944 min. At t=20 min, I≈0.367879, meaning conversion is approximately 0.632121. The target branch fraction among consumed intermediate is a/(a+b)=0.8, while the competing branch fraction is 0.2. Those fractions do not equal total conversion.

Integrating the product balances gives P=0.8(1−I) and H=0.2(1−I). At 20 min, P≈0.505696 and H≈0.126424. At asymptotically complete model conversion P approaches 0.8 rather than one, because competition persists. A target-selectivity statement of 80% is therefore compatible with a target amount below 80% of the initial inventory at a finite time.

If target product is recovered with a stipulated 90% efficiency after formation, the recovered target at 20 min is 0.9P≈0.455126. Recovery loss is another process, distinct from reaction branching. An analytical detector with an unknown response adds still another uncertainty. Reporting one number as conversion, product yield, recovery and purity would collapse several separate questions.

## Perturbations need a named constraint

Doubling a while holding b fixed increases target branching from 0.8 to 0.08/0.09≈0.888889 and accelerates intermediate disappearance. If a donor concentration perturbation also changes hydrolysis, ionization or observation response, however, the simple one-parameter comparison may not describe the actual system. State the fixed quantities and follow the full balance rather than claiming every stronger donor solves selectivity.

In a reversible network, products can feed back to the intermediate or other starting forms, so the irreversible branch formula can fail. A time-dependent effective rate also changes the product integrals. The current model is deliberately simple enough to examine mathematically; a successful fit within it does not establish that a real synthesis follows those exact pathways.

## Stereochemical composition is another axis

If P contains an enantiomeric pair, an enantiomeric excess is calculated from their calibrated amounts as signed excess (n_A−n_B)/(n_A+n_B). A target amount does not supply that ratio. A sample can have high conversion but low enantiomeric excess, or high excess while containing little target. Impurities can interfere with optical or chromatographic interpretation even when a net product formula is plausible.

For a supplied pair with A=7 and B=3 micromoles, signed A excess is 0.4, or 40%. The major fraction is 0.7, not 0.4. If an observation system reports gains two and one for the two separated peak channels, corrected areas 14 and 3 would instead give an uncalibrated area excess 11/17≈64.7059%. That example is a synthetic reporting model, not different intrinsic optical absorption by matched enantiomers.

The virtual lab will supply independent blanks, standards and peak identities to convert observations back into amounts. The sign of excess will refer to the supplied A/B labels and optical identities, not an inferred R/S descriptor. A calibration only establishes the stipulated linear response within this construction; it does not certify every real chromatographic method or eliminate unknown coelution.

## Return to the amide case

The preserved case asks for a plausible activation category and evidence of product identity. The network shows why such a proposal also needs competing pathways and material accounting. A new signal after activation could be intermediate, target or hydrolysis product. The assigned P/H labels in our model should not be treated as a measurement identifying those species in an actual sample.

Independent structural evidence can constrain identity, while calibrated amount observations constrain inventory. Appropriate controls can test whether activation, donor capture or background processes explain a change. These are questions for discussion rather than a wet-lab plan. The existing checklist remains self-assessment with zero course-grade points, and no independent instructor review is implied.

## Worked example

Add effective rates to obtain 0.050 min⁻¹, calculate I at 20 min and subtract from one for conversion. Normalize a by the sum for target branching and multiply that branch by converted amount for P. Recover H from the other branch and check I+P+H=1. Apply recovery only after formation if that additional assumption is supplied. Separately compare the true 7:3 enantiomer amounts with the biased 14:3 peak-channel areas.

## Common mistakes

Do not equate branching with conversion or assign an unknown signal to target merely because an activation strategy was named. Do not infer enantiomeric amounts from unequal raw reporting responses without calibration. Match every conclusion to the inventory, observation or structural evidence that supports it.

## Limits of this lesson

Network rates, recovery and peak gains are synthetic. No actual amide product, practical yield, biological effect or optimized synthesis is established. The examples provide no handling procedure or instrument method. Original instruction has substantial AI assistance. The package remains partial, unreviewed and formative-only.

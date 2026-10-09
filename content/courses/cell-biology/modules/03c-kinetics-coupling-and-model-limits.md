# Enzyme kinetics, energetic coupling and model limits

Original instructional draft, CC BY 4.0, with substantial Codex assistance. This extends the preserved [compact energetics reading](03-enzymes-and-cellular-energetics.md) and connects [catalysis](04a-enzyme-catalysis-and-free-energy.md) to [initial-rate assays](04b-initial-rates-and-enzyme-inhibition.md). No independent scientific or accessibility review has occurred. All numerical examples below are stipulated teaching models, not measured biological constants.

## What the rate model means

For an ideal single-substrate reaction, enzyme binds substrate to form a complex and the complex can release product. Under a steady-state initial-rate approximation, `v = Vmax*S/(Km+S)`. Here S is free substrate concentration, v is an initial rate, Vmax is the limiting rate under this model and Km has the same concentration unit as S. The approximation requires an appropriate enzyme/substrate regime, approximately steady complex abundance during measurement, negligible product influence over the initial window, and a stable active-enzyme pool. Multiple substrates, cooperativity, inhibition, transport limitation and enzyme inactivation can require another model.

At S=Km the expression gives half Vmax. This is an operational interpretation of the parameter, not a universal statement that Km is a binding dissociation constant. In the simple kinetic scheme, Km includes binding, dissociation and catalytic terms. Equating it to a dissociation constant requires additional limiting assumptions; a fit alone does not verify them.

With active enzyme concentration E and a compatible turnover constant kcat, Vmax=kcat*E. If kcat is 12 per second and active E is 3 nM, Vmax is 36 nM/s. At S=4 mM and Km=2 mM, the model predicts `v=36*4/(2+4)=24 nM/s`. The millimolar substrate ratio is dimensionless, while the enzyme concentration sets the rate scale. Converting E to micromolar without converting the output would introduce a factor-of-1000 error.

Doubling active E doubles Vmax and the predicted initial rate at a fixed free S under these assumptions. Doubling total immunoreactive protein need not double active E: recovery, folding, inactive material and localization may differ. A protein abundance assay and a catalytic-rate assay address separate links in the evidence chain.

## An original rate table and its limits

Consider a hypothetical stable preparation with Vmax=60 micromolar/min and Km=3 mM:

| Free S (mM) | Model initial v (micromolar/min) |
| --- | --- |
| 1 | 15 |
| 3 | 30 |
| 9 | 45 |

Each entry uses the same expression; for 9 mM, `60*9/(3+9)=45`. These are model predictions without noise, not three independent enzyme preparations. The values demonstrate saturation but cannot establish the appropriateness of the model in a living cell. A real assay would need substrate range, blanks, product calibration, an initial linear time window, active-enzyme/loading information, independently prepared units and a justified uncertainty model. A fit with many technical wells from one preparation does not supply many independent biological replicates.

The curve is approximately proportional to S when S is much smaller than Km and approaches Vmax when S is much larger. The mathematical limiting behavior is separate from an experimental decision that a range is sufficiently low or high; residuals, precision and competing models matter. A visually smooth curve is not evidence that a unique molecular mechanism has been identified.

## Rate, free energy and equilibrium answer different questions

A catalyst lowers the activation barrier for a reaction path and can speed forward and reverse equilibration. For the same initial and final chemical states at the same conditions, it does not change their free-energy difference or the equilibrium constant. A fast reaction can be uphill under a particular composition; a favorable reaction can be slow if its barrier is high. An assay of initial rate does not by itself measure equilibrium.

For a reaction with specified composition, `deltaG = deltaG_standard + R*T*ln(Q)`, with compatible energy units and dimensionless reaction quotient Q defined relative to standard states. The standard free-energy difference concerns the declared standard states. The actual value depends on composition and temperature. Writing a concentration inside a logarithm without defining its reference scale hides a dimensional assumption. This introductory relationship also does not automatically handle every nonideal intracellular activity or compartment gradient.

For an explicitly coupled 1:1 event, free-energy changes add. Suppose a step has deltaG=+9 kJ/mol and its coupled driving step has deltaG=-18 kJ/mol under the same stated conditions. The net is -9 kJ per mole of coupled events. The negative sum shows thermodynamic favorability for the stipulated combined event; it does not prove that two reactions sharing a vessel actually couple. A physical enzyme/intermediate linkage and compatible stoichiometry are needed. Changing the driving step's substrate/product composition can change its actual deltaG and the combined result.

ATP is not a generic label that guarantees any process is favorable. One must specify the coupled chemistry, composition and stoichiometry. Likewise, an ion gradient supplies free energy only through a coupled route with the relevant electrochemical conditions and direction. A cell's pathway flux depends on supply, removal, transport, regulation and capacity, beyond one isolated enzyme's Vmax.

## Reasoning checks with feedback

1. At Vmax=60 micromolar/min, Km=3 mM and S=6 mM, what does the initial-rate model predict? **40 micromolar/min**, from `60*6/9`. The denominator carries substrate concentration, not enzyme concentration.
2. Would a faster approach to the same equilibrium demonstrate a new equilibrium constant? **No.** The rate and equilibrium claims concern different quantities.
3. Does a measured Km of 3 mM prove direct binding affinity is 3 mM? **No.** Interpret Km through its model and measurement context, then use an appropriate binding experiment if affinity is the question.
4. If two favorable/uphill reactions have a negative summed deltaG, is coupling proven? **No.** The sum assesses the specified coupled event; a mechanistic linkage must still be established.

Before interpreting a rate or energy result, state the quantity, units, model assumptions, independent unit and strongest supported conclusion. Name a measurement that would test the principal alternative. These explanations are study feedback with public answers, not a protected exam or evidence of reviewed mastery.

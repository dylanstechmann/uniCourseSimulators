# Membranes, transport, and electrochemical gradients

## Membranes are selective, dynamic interfaces

Amphipathic phospholipids have polar headgroups and nonpolar acyl chains. In water, many phospholipids assemble into a bilayer that shields the hydrocarbon chains while exposing hydrated headgroups. The bilayer is not a sealed wall: small nonpolar molecules partition through it more readily than charged solutes, and cells use channels, carriers, and pumps to regulate movement. Membrane composition, temperature, and protein organization influence fluidity and permeability.

Membrane proteins do different jobs. A **channel** provides a selective pathway and supports passive flux down an electrochemical-potential gradient. A **carrier** binds a solute and changes conformation; it may mediate facilitated diffusion or, when coupled to an energy source, active transport. A **pump** uses ATP hydrolysis, light, or an existing gradient to move a solute against its own gradient. A transporter name is not enough to infer direction: the substrate gradients, membrane voltage, coupling, and transport stoichiometry matter.

## Electrochemical potential balances concentration and charge

For an ion, the chemical contribution favors movement from higher concentration to lower concentration, while the electrical contribution favors or opposes movement depending on ion charge and membrane voltage. The Nernst equation describes the voltage at which these contributions for one ion balance. At approximately 25 °C for a monovalent cation:

`E = 61.5 mV × log10([ion]outside / [ion]inside)`

This expression uses the ideal-solution approximation, a specified temperature, and a single ion. Real cellular membranes can be permeable to several ions at once; the membrane potential then depends on their relative permeabilities and concentrations, not one Nernst value alone.

### Worked calculation: potassium at equilibrium

Assume a cell has 5 mM potassium outside and 140 mM inside at 25 °C. The idealized potassium equilibrium potential is `61.5 × log10(5/140) ≈ -89 mV`. At a membrane voltage of about −89 mV (inside relative to outside), the electrical and chemical contributions for potassium balance. Concentrations remain unequal at this electrochemical equilibrium. A potassium channel does not consume ATP per ion and does not force the two concentrations to become equal.

This calculation does not predict the whole-cell voltage, because other permeant ions and transport processes contribute. It also does not tell how fast the membrane approaches equilibrium; channel number, open probability, membrane area, and transport kinetics affect flux.

## Worked experimental comparison

Suppose a fluorescent ion-sensitive dye reports a changed intracellular potassium signal after a channel inhibitor is added. The signal is consistent with altered ion handling, but it does not prove that the inhibitor acted through the candidate channel. A stronger design uses vehicle-treated cells, a second perturbation such as channel knockdown, and a rescue with a perturbation-resistant channel. Verify that the dye responds to known calibration solutions and check cell viability and membrane integrity. Measure channel abundance or localization as supporting evidence. Use replicates and report the calibration range and variability.

An inhibitor can alter another transporter or the dye itself; a knockdown can change compensatory gene expression; a rescue construct can be overexpressed. Compare predicted and observed results across these conditions. State the conclusion at the scale tested—for example, “the candidate channel contributes to the measured response in this cell line under this buffer condition”—and name the evidence needed to generalize beyond it.

## Distinguish passive flux, equilibrium, and active transport

At electrochemical equilibrium, net flux of that ion is zero even though individual ions continue to move in both directions. A channel changes the rate at which equilibrium can be approached; it does not change the equilibrium condition by itself. A pump can maintain a gradient by coupling transport to energy input. Secondary active transport couples one solute's favorable downhill movement to another solute's uphill movement. Do not use “active” as a synonym for “protein-mediated,” and do not infer ATP use simply because a membrane protein is involved.

## Check your understanding

1. A channel is opened while the membrane voltage is exactly at the ion's Nernst potential. What is the expected net ion flux in the idealized model, and why?
2. Which additional information is needed to infer whether a cotransporter can move its substrate uphill?
3. A transporter's abundance increases but flux does not. Give two explanations that do not require the abundance measurement to be wrong.

## Provenance

Original instructional text, released under CC BY 4.0. MIT OpenCourseWare 7.01SC and 7.28x are topic-level, link-only curriculum comparators; no course text, figure, question, or exam was copied or adapted. See the package [source map](../source-map.json) and the repository [source registry](../../../sources/registry.json).

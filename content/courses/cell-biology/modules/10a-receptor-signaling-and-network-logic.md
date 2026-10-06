# Receptors, signaling pathways, and network logic

Cells convert extracellular information into intracellular changes by using receptors, enzymes, small molecules, and regulated interactions. A pathway diagram is a useful model, but the cell contains connected networks: one receptor can activate several branches, different receptors can converge on a shared component, and localization or timing can change which substrates are reached.

## Learning objectives

By the end of this lesson, you should be able to:

1. Calculate idealized single-site receptor occupancy from free ligand concentration and a stated dissociation constant, and explain why occupancy is not the same as cellular response.
2. Compare the first molecular relay steps of a receptor tyrosine kinase and a G-protein-coupled receptor without treating either route as universal.
3. Interpret dose and time measurements while accounting for amplification, receptor abundance, localization, and the measured response variable.

## Begin with the measured event

A **ligand** is a molecule or physical cue that changes a cell through a receptor or another sensing mechanism. A **receptor** is a component whose interaction with a cue changes a measurable state. The first event might be ligand binding, receptor clustering, channel opening, a conformational change, or enzymatic activity. Later measurements may include phosphorylation, second-messenger concentration, transcription, metabolism, movement, survival, or cell fate. These measurements occupy different levels of a causal chain:

`input → receptor state → intracellular relay → effector → measured cell response`

Each arrow is a hypothesis. Detecting receptor phosphorylation does not by itself establish a transcriptional effect; observing transcription does not establish a later fate change. Name the measured variable before interpreting it.

## Binding occupancy is not output

For an idealized reversible interaction between one ligand and one class of independent binding sites at equilibrium, the fraction of occupied receptors can be approximated by:

`θ = [L]free / (Kd + [L]free)`

Here, `[L]free` is free ligand concentration and `Kd` is the concentration at which half of those sites are occupied under the model. If `[L]free = Kd`, then `θ = 0.5`. If `[L]free = 1 nM` and `Kd = 4 nM`, then `θ = 1/(4 + 1) = 0.20`.

This is a binding calculation, not a prediction that the cell responds at 20% of its maximum. A cell may have spare receptors, nonlinear enzyme relays, thresholds, feedback, cooperative interactions, or a response assay that saturates before receptor occupancy does. The concentration giving half of a measured functional response is often called an operational `EC50`; it need not equal a binding `Kd`. The simple equation also assumes that free ligand is known, the system is near equilibrium, and the relevant sites behave as one population. Ligand depletion, multiple receptor states, cooperative binding, and receptor internalization can violate those assumptions.

## Two receptor routes, not one universal map

| Receptor class | Example first relay | What the relay can do | Important boundary |
| --- | --- | --- | --- |
| Receptor tyrosine kinase (RTK) | Ligand binding promotes receptor association and phosphorylation; phosphotyrosines recruit proteins that can connect to Ras–RAF–MEK–ERK. | Creates multiple docking sites and can engage more than one downstream branch. | Receptor phosphorylation or ERK activation alone does not establish which branch caused a later phenotype. |
| G-protein-coupled receptor (GPCR) | Ligand-dependent receptor activity changes the nucleotide state of a heterotrimeric G protein; Gα and Gβγ can regulate effectors. | Can change cyclic AMP, phospholipase activity, calcium, ion channels, or kinase activity. | The direction depends on receptor, G-protein subtype, cell context, and effector availability. |

One common RTK route is receptor-associated adaptor recruitment, activation of the small GTPase Ras, and a kinase relay through RAF, MEK, and ERK. Each kinase can modify multiple substrate molecules, so a modest input can produce an amplified response. A GPCR coupled to Gαs can stimulate adenylyl cyclase and cyclic AMP production; cyclic AMP can regulate protein kinase A. A different GPCR may inhibit adenylyl cyclase or act through Gβγ, phospholipase C, calcium, or other effectors. These examples describe common mechanisms, not an exhaustive receptor catalog.

The network is not a single chain. **Convergence** occurs when distinct inputs influence the same component. **Cross-talk** occurs when activity in one branch changes another branch. **Scaffolds** can hold proteins near one another; membranes, endosomes, and local second-messenger degradation can restrict where a signal is effective. The total receptor count is therefore not enough to predict the response: receptor location, partner abundance, cell state, and the assay all matter.

## Dose and time are separate experimental axes

A dose–response curve asks how a measured output varies with input concentration under specified conditions. It does not automatically identify a binding affinity. Receptor number, signal amplification, ligand stability, exposure duration, and the assay's dynamic range can change the curve. A **saturating response** means additional input produces little additional measured output in that assay; it does not prove every receptor is occupied.

Time-course data ask how quickly a response begins, peaks, persists, and returns toward baseline. Two conditions can have similar peak phosphorylation yet differ in duration. A short pulse may produce a transient signal; continued input may maintain one. Transient and sustained signaling can be associated with different downstream outcomes in some systems, but a phosphorylation trace alone does not show cell division, differentiation, survival, or fate. Those outcomes need separate, prespecified measurements over an appropriate time window.

Consider four quantities that are easy to conflate:

1. Ligand concentration is an input, ideally measured or controlled as free concentration.
2. Receptor occupancy is a binding-model estimate or direct binding measurement.
3. Phosphorylation is a biochemical state measured at a specified site, time, and assay range.
4. Cell response is a separate outcome, such as a transcript, growth rate, or marker-defined state.

Agreement across levels strengthens a proposed chain. A result at one level does not substitute for measurements at the next.

## Worked example: interpreting a binding estimate

Suppose a cell-surface receptor has an estimated `Kd = 4 nM` and the free ligand is held at `1 nM`. Under the single-site equilibrium approximation, `θ = 1/(4 + 1) = 0.20`, or 20% estimated occupancy. This result supports only the modeled occupancy estimate. It does not imply a 20% ERK response, establish the receptor count, or predict cell fate. A measured response curve and appropriate time-course and specificity controls would be needed for those claims.

## What a pathway diagram leaves out

Before using a diagram as an explanation, ask:

- Which arrow was directly measured, and which arrows are inferred?
- Was the ligand dose and exposure duration controlled?
- Does the assay quantify total protein or a specific activated state?
- Is the measured response in a linear range with suitable loading, viability, and vehicle controls?
- Could receptor trafficking, feedback, cross-talk, or cell-to-cell variation account for the time course?
- Does the conclusion stop at the cell type and conditions actually tested?

These questions turn a schematic into a testable model. They also keep a common teaching map from being mistaken for a universal wiring diagram.

## Limits of this lesson

This lesson introduces receptor occupancy, common RTK and GPCR relays, amplification, and measurement boundaries. It does not survey every receptor family, derive multistate binding models, or provide a complete mathematical treatment of nonlinear networks. The next lesson uses time-course and perturbation evidence to reason about feedback and pathway position.

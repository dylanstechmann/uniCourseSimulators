# Signaling dynamics, feedback, and perturbation evidence

Signaling pathways change over time. A receptor can activate a relay within seconds or minutes, while transcription, protein abundance, and cell behavior may change later. Feedback can alter the next response, and a perturbation can affect more than its intended target. Interpreting a pathway experiment therefore requires matched controls, time-aware measurements, and a claim no broader than the evidence.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compare transient and sustained signaling in replicate time-course data without treating one phosphorylation readout as a cell-fate measurement.
2. Distinguish negative feedback, receptor adaptation, and ligand depletion as competing explanations for a declining response.
3. Interpret inhibitor, genetic perturbation, bypass, and rescue evidence while accounting for target engagement, off-target effects, and the tested cell context.

## A response is a trajectory, not one endpoint

A single measurement can hide the shape of a response. A rapid peak followed by a return toward baseline differs from a smaller response that remains elevated, even when an endpoint chosen at one time makes them look similar. **Response dynamics** include onset, peak, duration, adaptation, and recovery. These features depend on ligand exposure, receptor state, relay activity, feedback, cell state, and sampling schedule.

The table contains **synthetic teaching data**, not published measurements. One cell type received the same ligand under two exposure schedules: a two-minute pulse followed by a controlled wash, or continued ligand exposure. The phospho-ERK signal was normalized to a matched total-ERK measurement and expressed relative to time-matched vehicle (`1.0`). Values are mean ± SD across four independent culture preparations; they are not four technical wells from one culture.

| Time after ligand addition (min) | Two-minute pulse: relative phospho-ERK | Continued exposure: relative phospho-ERK |
| ---: | ---: | ---: |
| 0 | 1.0 ± 0.2 | 1.0 ± 0.2 |
| 2 | 5.8 ± 0.7 | 5.7 ± 0.8 |
| 10 | 3.6 ± 0.6 | 5.0 ± 0.7 |
| 30 | 1.7 ± 0.3 | 4.4 ± 0.6 |
| 60 | 1.1 ± 0.2 | 3.4 ± 0.5 |

The early peaks are similar in this synthetic example, while the later trajectories differ. The data support a difference in the measured phospho-ERK duration under the two exposure schedules. They do not establish a downstream transcriptional program, proliferation, differentiation, survival, or cell fate. They also do not establish that the difference is caused by a specific feedback molecule: ligand availability itself was changed by the exposure schedule.

## Feedback can shape the trajectory

**Negative feedback** occurs when a downstream response reduces an earlier step or its own continued production. A signaling response can induce a phosphatase that removes activating phosphate groups, an inhibitory protein that binds a pathway component, or a transcriptional regulator that lowers receptor or ligand availability. Feedback may act quickly through phosphorylation or localization, or more slowly through new RNA and protein synthesis.

**Adaptation** describes a reduced response during continued input. It is an observed behavior, not a unique mechanism. Receptor desensitization, internalization, a feedback phosphatase, ligand depletion, or a change in cell state can all contribute. A falling phospho-ERK trace alone cannot distinguish them. **Positive feedback** can reinforce a state or produce threshold-like behavior, but its presence also needs direct evidence and an appropriate time course.

To separate alternatives, make each one predict a measurement:

| Candidate explanation | Useful measurement or intervention | What the result can support | What it cannot establish alone |
| --- | --- | --- | --- |
| Ligand becomes unavailable | Measure or replenish ligand using matched medium-change and vehicle controls. | Whether maintained input changes the late response. | That an intracellular feedback loop is absent. |
| Receptor is removed or desensitized | Measure surface and total receptor at matched times; use a controlled recovery or recycling interval. | Whether receptor availability tracks the decline. | That every downstream branch changes for the same reason. |
| An induced phosphatase attenuates the relay | Measure candidate RNA, protein, or activity over time; perturb the candidate with a matched control and attempt a specific rescue. | Whether the candidate contributes to the measured decline in this system. | That the candidate is the only feedback mechanism or acts directly on every measured substrate. |
| Cell condition changes | Measure viability, cell number, and relevant state markers with the signaling readout. | Whether a gross cell-state change could explain the signal. | A specific molecular mechanism for the trajectory. |

A targeted perturbation is more informative when it changes the predicted node, produces the predicted downstream effect, and is supported by an independent intervention or rescue. If an intervention changes viability or receptor amount, the signaling difference may be secondary. Match the assay's exposure, wash, solvent, timing, and collection steps across conditions.

## Pathway position and the meaning of rescue

Suppose receptor inhibition lowers a downstream phospho-ERK measurement. That result is consistent with receptor input contributing to ERK activation under the conditions tested. A **target-engagement** measurement checks whether the intervention changed its intended target or the closest reliable downstream event. Vehicle controls, a no-ligand condition, a positive pathway control, and an assay-range check address different alternatives.

A bypass experiment can help order components. If constitutively active MEK restores ERK phosphorylation after receptor inhibition, the bypass is consistent with MEK being able to restore that measured downstream state in the tested cells. It does not show that receptor activity has no other roles, that MEK is the only relevant branch, or that the artificial expression level matches normal physiology. Overexpression can create nonphysiological behavior, and a restored phospho-signal is not by itself a restored cell fate.

Use different tools to reduce different uncertainties:

1. A small-molecule inhibitor asks whether a drug-sensitive activity contributes, subject to selectivity, dose, and exposure limits.
2. A genetic depletion or edit asks whether reducing a selected component changes the readout, subject to delivery, clone, and adaptation effects.
3. An orthogonal perturbation tests whether the pattern persists through a different intervention.
4. A rescue tests whether restoring the proposed component moves a prespecified readout toward the control under the same conditions.
5. A downstream outcome assay tests whether the biochemical change predicts a later cell response rather than assuming that it does.

The strongest design is not the one with the most interventions. It is the one in which each intervention, control, and time point addresses a stated alternative. Predefine the primary readout, response window, replicate unit, and analysis before inspecting the outcome.

## Worked example: bound the conclusion to the data

At 2 minutes, the pulse and continued-exposure groups have similar phospho-ERK values. At 60 minutes, the pulse group is near its vehicle-relative baseline while the continued-exposure group remains elevated. A defensible summary is: “Under these synthetic exposure conditions, the measured phospho-ERK signal is more sustained during continued ligand exposure than after a two-minute pulse.” The table does not identify why the pulse response declines. A matched ligand-replenishment experiment, receptor-availability measurements, and a time-resolved candidate-feedback perturbation would test different alternatives. A separate later cell-state assay is needed to test a differentiation or proliferation claim.

## A compact causal-evidence checklist

Before writing an instructor-style conclusion, ask:

- Did the intervention engage the intended target at the relevant time?
- Were solvent, delivery, wash, cell number, viability, and assay-range controls matched?
- Was the response measured across enough time points to distinguish peak from duration?
- Are biological preparations distinguished from technical repeats?
- Does a second, orthogonal intervention or specific rescue support the same step?
- Is a proposed intermediate directly measured, or only inferred from a familiar diagram?
- Does the claim stop at the measured biochemical state, cell type, dose, and time window?

These safeguards do not turn one experiment into universal proof. They make the evidence chain clearer and help identify the next discriminating experiment.

## Limits of this lesson

This lesson uses one synthetic ERK time course to teach experimental reasoning. The separate virtual-lab activity provides an interactive analysis of a larger constructed dataset; neither resource provides raw imaging files, a fitted dynamical model, a complete survey of GPCR or kinase signaling, or evidence for a therapeutic response. Pathway behavior varies with cell type and conditions, and external academic review is still required.

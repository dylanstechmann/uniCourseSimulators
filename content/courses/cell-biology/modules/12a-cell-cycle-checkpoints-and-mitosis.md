# Cell-cycle control, checkpoints, and mitosis

Cell division is an ordered process that duplicates genetic material and distributes it to daughter cells. The order matters: a cell should not copy damaged DNA without response or separate chromosomes that are not correctly attached to the spindle. The checkpoints that coordinate these events are control systems with measurable inputs and outcomes, not proof that every cell follows one perfectly reliable script.

## Learning objectives

By the end of this lesson, you should be able to:

1. Relate cyclin-dependent kinase activity and selected checkpoint signals to transitions through the mammalian cell cycle, while keeping a molecular model separate from direct measurement.
2. Distinguish DNA-content, nucleotide-incorporation, and mitotic-marker readouts and calculate cell fractions or relative changes from a stated denominator.
3. Evaluate a synthetic damage-response time course and propose controls that test cell-cycle arrest without confusing it with cell death or a specific signaling mechanism.

## The cycle is a sequence of states and transitions

During **G1**, a cell grows and integrates internal state with external conditions. In **S phase**, it synthesizes DNA. During **G2**, it prepares for division and can respond to incomplete replication or damage. **M phase** includes mitosis and cytokinesis. Some cells leave the cycling population for a reversible quiescent state, differentiate, or enter other context-dependent states. These states cannot be identified from a single snapshot alone.

In many mammalian cells, cyclin-dependent kinases (CDKs) are active when bound by the appropriate cyclin and can phosphorylate proteins that coordinate transition-specific events. Cyclin abundance, CDK inhibitors, activating or inhibitory phosphorylation, localization, and regulated protein destruction all contribute. A simplified overview is:

`mitogen and cell state → cyclin–CDK activity → DNA replication / mitosis → cyclin destruction and reset`

For example, G1 cyclin–CDK activity can alter retinoblastoma-family control of E2F-dependent transcription; later cyclin–CDK activities help coordinate DNA synthesis and mitotic entry. This is a compressed model of a regulated network. It does not mean that one cyclin is a universal on/off switch or that a protein abundance measurement alone gives kinase activity.

## Checkpoints ask different questions

Checkpoint pathways delay or reshape progression when an important condition has not been met. They do not repair every problem, and checkpoint activation is not identical to a particular final fate.

| Control point | Example condition being monitored | Possible response and limit |
| --- | --- | --- |
| G1/S and intra-S DNA-damage responses | DNA lesions, replication stress, cell state, and growth signals | Signaling can inhibit CDK progression and allow time for repair; persistent damage may lead to stable arrest or death. A single marker does not identify the entire pathway. |
| G2/M transition | Completion of genome replication and damage signals | Mitotic entry may be delayed while replication or repair proceeds. A G2-like DNA-content peak alone cannot name the molecular trigger. |
| Spindle-assembly checkpoint | Whether kinetochores have formed appropriate spindle attachments | Unattached kinetochores can restrain APC/C–Cdc20, delaying securin and cyclin-B destruction. This delays anaphase; it is not a scan that verifies every base in the genome. |

At mitotic exit, regulated destruction of securin releases separase to promote sister-chromatid separation; cyclin-B loss contributes to falling mitotic CDK activity. The details vary with organism and cell context. A model should predict an observable consequence before a perturbation is interpreted as confirmation.

## Follow chromosome movement without skipping the measured steps

Mitosis is commonly divided into prophase, prometaphase, metaphase, anaphase, and telophase. Chromosomes condense, the nuclear envelope breaks down in typical animal-cell mitosis, spindle microtubules interact with kinetochores, sister chromatids separate, and nuclei reform. Cytokinesis then partitions cytoplasm. These stages overlap in live cells; names organize observation rather than guarantee sharply isolated biochemical events.

DNA-content flow cytometry can distinguish a population with approximately 2N DNA from cells with intermediate DNA content and cells with approximately 4N DNA. A 4N signal does not by itself distinguish G2 from mitosis, identify chromosome attachment, or prove that cytokinesis succeeded. A short **EdU** pulse labels cells synthesizing DNA during that pulse. A phospho-histone-H3 measurement can enrich for mitotic cells, but it does not stage every chromosome or replace imaging. Gating, doublets, dying cells, pulse duration, and the time of collection affect interpretation.

## Synthetic time-course example

The table below is **synthetic teaching data**, not a published experiment. A single cultured cell type received a defined DNA-damaging treatment or matched vehicle. Four independent culture preparations per group were summarized as mean ± SD. A short EdU pulse and DNA-content measurement were made at each time; viability was assessed separately. The percentages are preparation-level summaries and may not sum exactly because of rounding.

| Condition and collection | G1-like DNA content (%) | S-range DNA content (%) | G2/M-like DNA content (%) | EdU-positive after short pulse (%) | Viable cells (%) |
| --- | ---: | ---: | ---: | ---: | ---: |
| Vehicle, matched time | 52 ± 3 | 28 ± 2 | 20 ± 2 | 27 ± 2 | 94 ± 2 |
| Damage, 4 h | 63 ± 4 | 17 ± 3 | 20 ± 3 | 15 ± 3 | 92 ± 2 |
| Damage, 24 h | 70 ± 4 | 13 ± 2 | 17 ± 3 | 11 ± 2 | 90 ± 3 |

The constructed summaries show a higher G1-like fraction and lower EdU-positive fraction at later collections, while measured viability remains broadly similar in this small example. Those observations are compatible with a reduced fraction synthesizing DNA after treatment. They do not prove that DNA damage caused a p53-dependent G1 checkpoint, that every cell arrested, or that the population became senescent. Cell-cycle distribution can also shift through altered entry, progression, detachment, or selective loss. The four culture preparations—not individual cells or image fields—are the independent replicates stated here.

## Worked example: calculate a gated fraction

Suppose a short pulse labels 60 cells out of 240 viable singlets in a stated flow-cytometry gate. The fraction positive during that pulse is:

`60 / 240 × 100% = 25%`.

This is the percent of the gated population that incorporated EdU during the pulse. It is not automatically the exact fraction of time each cell spends in S phase. Interpreting population fractions requires the pulse duration, proliferation state, gating and collection time.

From the synthetic table, the relative decrease in the EdU-positive fraction from vehicle to the 24-hour sample is `(27 − 11) / 27 × 100% ≈ 59.3%`. This relative decrease differs from a 16 percentage-point change. State the denominator whenever reporting a percent change.

## Design a discriminating follow-up

To test whether a defined damage-response pathway contributed to the pattern, measure target engagement and compare a pathway perturbation with matched vehicle and non-targeting controls. Collect a time course; measure DNA damage, DNA content, EdU incorporation, cell number, and viability with compatible denominators. Include an orthogonal perturbation or rescue where feasible. A rescue supports involvement in the tested system but does not prove a single direct molecular step.

Replicate at the independent-culture level and report the unit used for uncertainty. If doublets or apoptotic fragments alter the flow profile, show the gating logic and an orthogonal imaging or marker measurement. Do not infer stable senescence from reduced EdU alone; test recovery in a suitable mitogen condition and use a broader cell-state panel.

## Limits of this lesson

This lesson presents a simplified mammalian cell-cycle model and an explicitly synthetic summary table. It does not provide raw flow files, an instrument protocol, a complete checkpoint-network map, a chromosome-segregation assay, or evidence that a treatment is safe or effective. Phase assignments depend on the actual measurement and cell context; expert review remains necessary.

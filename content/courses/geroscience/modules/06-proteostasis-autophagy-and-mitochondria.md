# Proteostasis, autophagy and mitochondria: quality control and what changes with age

A cell is a crowded chemical system that is rebuilt all the time. Proteins are made, folded, used and removed, and organelles are replaced when they wear out. Aging research asks whether the systems that do this quality control lose capacity with age, and if so whether that loss is a cause of tissue decline or a consequence of it. This lesson focuses on a measurement problem that decides much of the argument: a marker that goes up can mean a pathway is more active or that it is blocked.

## Learning objectives

By the end of this lesson, you should be able to:

1. Calculate autophagic flux from marker levels measured with and without a lysosomal inhibitor, and interpret the result.
2. Distinguish induction of a quality-control pathway from blocked degradation when a marker rises.
3. Evaluate evidence that proteostasis or mitochondrial changes are causes rather than consequences of aging in a tissue.

## The quality-control systems

**Folding and chaperones.** Newly made proteins must fold, and stress can unfold them again. Chaperones help folding and refolding, and cells raise chaperone expression in stress responses.

**The ubiquitin–proteasome system** tags individual proteins with ubiquitin chains and degrades them in the proteasome. It handles short-lived regulatory proteins and misfolded proteins that can be unfolded and threaded through the proteasome.

**Autophagy** delivers cytoplasmic material to the lysosome. In macroautophagy a double-membrane structure, the autophagosome, forms around cargo and fuses with a lysosome, where acid hydrolases degrade it. Autophagy can take bulk cytoplasm or specific cargo such as aggregates, organelles or ribosomes. **Mitophagy** is the selective form that removes damaged mitochondria.

Together these systems clear damaged proteins and organelles. Reviews of the hallmarks of aging list loss of proteostasis and disabled macroautophagy among them and report that capacity of these systems declines with age in several tissues and organisms, while noting that the evidence differs by tissue and species and that decline is not universal.

## Measuring flux, not just level

The usual autophagy marker is **LC3-II**, a lipidated form of LC3 that sits on autophagosome membranes and is degraded along with the cargo inside the lysosome. Its steady-state amount depends on two things: how fast autophagosomes form and how fast they are degraded. A rise in LC3-II can therefore mean more autophagosome formation (induction) or slower degradation (a block), and these are opposite stories about the pathway.

The standard fix is a **flux assay**. Measure LC3-II (normalized to a loading control) with and without a lysosomal inhibitor that prevents degradation, such as bafilomycin A1 or chloroquine, for a fixed time. With the inhibitor, whatever formed during that time accumulates, so

**flux = LC3-II(with inhibitor) − LC3-II(without inhibitor).**

Flux estimates the delivery of LC3-II to the lysosome per unit time, which is closer to pathway activity than any single level. Good practice adds a second readout, such as the cargo receptor p62, which accumulates when degradation is impaired, and uses independent cultures as the replicate unit. The inhibitor must be shown to work (a control that LC3-II rises in the young cells), and one time point does not give a rate unless accumulation is roughly linear over that window.

## Mitochondria: damage, signaling and threshold effects

Mitochondria make most of a cell's ATP and produce reactive oxygen species (ROS) as by-products. The older view that ROS damage simply accumulates and causes aging is now regarded as too simple: ROS also act as signals, and supplementing antioxidants has not consistently extended lifespan in animal or human studies. What is better established is that damaged mitochondria are removed by mitophagy and replaced, and that mitochondrial DNA (mtDNA) mutations accumulate in some tissues.

Two features make mtDNA mutations hard to interpret. A cell holds many mtDNA copies, so a mutation may be present in only some of them (**heteroplasmy**). And a biochemical defect often appears only when the mutant fraction in a cell exceeds a high threshold that depends on the mutation, so a tissue can carry many mutant copies on average yet few cells that are actually defective. Averages again hide structure: what matters is the number of cells above threshold.

## Cause or consequence

An old tissue with more aggregates, more damaged mitochondria and lower autophagic flux is consistent with quality-control failure causing decline. It is equally consistent with decline from another cause (inflammation, reduced cell division, changed nutrient signaling) overloading quality control. Association with age cannot separate these. The informative experiments perturb the pathway and measure function: reduce or enhance a quality-control component in a young or old tissue and ask whether tissue function and survival change. In several model organisms, loss of autophagy-related genes has been reported to shorten lifespan or to block the benefit of other life-extending interventions, and increased autophagy-related function has been reported to extend it in some settings. Those are model-organism results with specific genetic tools; they do not show that boosting autophagy extends human life.

## Synthetic data: an autophagy flux assay

The values are **synthetic teaching data**: LC3-II normalized to a loading control and to the untreated young mean, each a mean of four independent cultures, measured after a fixed 2-hour window with or without a lysosomal inhibitor.

| Cells | Without inhibitor | With inhibitor |
|---|---:|---:|
| Young | 1.0 | 3.0 |
| Old | 1.8 | 2.4 |

## Common mistakes

- Reading a higher LC3-II level as more autophagy, when slower degradation raises it too.
- Using a lysosomal inhibitor without a control showing that it works.
- Treating one time point as a rate without checking that accumulation is roughly linear.
- Treating wells from one culture as independent replicates.
- Assuming reactive oxygen species simply accumulate and cause aging, or that antioxidants must extend lifespan.
- Averaging mitochondrial DNA mutation load over a tissue and missing that the number of cells above the threshold matters.
- Concluding from an association with age that failing quality control causes the decline.

## Worked example

Young flux = 3.0 − 1.0 = 2.0. Old flux = 2.4 − 1.8 = 0.6. The old cells have a *higher* steady-state LC3-II (1.8 against 1.0) but only 30% of the flux, which fits slower degradation of autophagosomes, not induction. In a separate set of 200 cells scored for mtDNA heteroplasmy, 34 had a mutant fraction above a pre-set 70% threshold, so 17% of cells are above threshold even if the average mutant fraction looks small.

## Limits of this lesson

The numbers are synthetic and illustrate method. The lesson does not recommend any drug, supplement or fasting regimen to alter autophagy, and the model-organism findings it summarizes do not establish an effect on human aging.

# Genome instability and repair capacity: damage, maintenance and what accumulates

DNA is the one molecule in a cell that cannot be replaced from a template once it is damaged in a way that is not repaired, which is why damage to it is a leading candidate for a driver of aging. The idea is easy to state and hard to test. This lesson separates three questions that are often run together: how much change has accumulated in the genome, what produced it, and whether it matters for how a tissue works.

## Learning objectives

By the end of this lesson, you should be able to:

1. Estimate a mutation-accumulation rate from cross-sectional counts and state the assumptions that make a rate meaningful.
2. Use the damage–maintenance balance to explain why equal burden can arise from different causes, and name measurements that separate them.
3. Evaluate what a repair-deficiency syndrome does and does not show about normal aging.

## Damage arrives constantly and repair is imperfect

Every cell sustains DNA damage continuously. Replication makes errors that proofreading and mismatch repair mostly catch. Metabolism and the environment produce chemical changes to bases, single-strand breaks and, less often, double-strand breaks. Ultraviolet light adds lesions in exposed skin. The cell-biology lesson on lesion removal described the main repair routes: base excision, nucleotide excision, mismatch repair, and homologous recombination or end joining for double-strand breaks. Repair is fast and usually accurate, but a small fraction of events become permanent: a changed base, a deletion, a rearrangement, or a lesion that stalls replication and triggers arrest or cell death instead.

Two consequences follow. A mutation is the *record* of a damage event that was repaired wrongly, copied before repair, or not recognized, so counting mutations measures the surviving errors and not the damage that came in. And the cell has a second option besides repair: it can stop dividing or die. Arrest and death keep a damaged genome from propagating, but in a tissue that renews slowly they also remove cells, which is part of why genome stability and tissue function are linked.

## What is observed to accumulate with age

Sequencing of normal tissue, clonal cell lines derived from single cells, and expanded clones has reported that somatic base substitutions accumulate with age in many human tissues, often close to linearly, at rates that differ between tissues. Rearrangements and copy-number changes, changes in mitochondrial DNA, and shifts in chromatin state also accumulate or drift. Reviews of the field, including the 2013 and 2023 hallmarks articles and a 2021 review of DNA damage in aging, treat genomic instability as one hallmark among several and note that the evidence for each hallmark differs in strength.

Three cautions apply before reading an accumulating count as a cause of decline.

- **Burden is not effect.** Most mutations fall in sequence that does not matter for the cell's function. A tissue can carry many mutations with little consequence, or a few in the wrong gene in the wrong cell with large consequence, as in cancer.
- **Averages hide structure.** Mutations are not spread evenly. Some cells carry far more than others, and a mutation that gives a growth advantage can expand into a clone, as in clonal hematopoiesis. A mean count per cell can rise because of a few cells.
- **Cross-sectional is not longitudinal.** Comparing people of different ages gives a rate only if the older and younger groups differ chiefly in age. Cohort effects and survivor selection (people with high burdens may be under-represented in the oldest group) can bend the line.

## The damage–maintenance balance

A useful frame is a balance. If damage is produced at an input rate *i* and removed or tolerated at a rate proportional to the current burden *B*, then dB/dt = i − kB, and the steady-state burden is i/k. The same burden can therefore arise from a high input with normal removal, or a normal input with weak removal. For a quantity that is not removed at all (a permanent mutation in a non-dividing cell), k is near zero and the burden grows roughly linearly with an *i* that is the net rate of new permanent change.

The frame says what to measure. To separate input from removal you need both: some readout of how much damage is produced (a lesion count right after a defined exposure, or the accumulation rate in a repair-proficient control) and a readout of how quickly it is removed (a lesion-removal time course). A higher burden in older cells is compatible with more input, less removal, or just more time, and the data have to say which.

## Repair deficiency and accelerated features

Rare human conditions caused by defects in genome-maintenance genes show some features that resemble early aging. Werner syndrome, caused by loss of a DNA helicase, and Cockayne syndrome, which affects transcription-coupled repair, are examples. They are informative: they show that failure of maintenance can accelerate some aging-like changes. They do not show that normal aging is the sum of such defects. The features are *segmental*, meaning some aging-like changes appear early and others do not, and the underlying defect is a specific lesion in a specific pathway rather than the gradual drift seen in most people. The right inference is bounded: maintenance matters for several features, and the contribution of any one pathway to normal aging needs separate evidence.

## Synthetic data: accumulation and repair

The tables are **synthetic teaching data**. Table 1 gives the mean number of base substitutions per cell in clones derived from two tissues at five ages. Table 2 gives the fraction of an induced lesion removed in four hours in cell cultures derived from young and old donors (four independent cultures each).

| Age (years) | Tissue A | Tissue B |
|---:|---:|---:|
| 20 | 410 | 150 |
| 35 | 780 | 220 |
| 50 | 1180 | 310 |
| 65 | 1560 | 380 |
| 80 | 1990 | 470 |

| Culture | Young donors: fraction removed | Old donors: fraction removed |
|---:|---:|---:|
| 1 | 0.72 | 0.55 |
| 2 | 0.7 | 0.52 |
| 3 | 0.74 | 0.57 |
| 4 | 0.71 | 0.54 |

## Common mistakes

- Reading an accumulating mutation count as proof that mutations cause decline.
- Using a mean count per cell and missing that a few cells or clones carry most of the burden.
- Estimating a rate from cross-sectional data without considering cohort effects and survivor selection.
- Assuming a higher burden means more damage input, when weaker removal or more time gives the same burden.
- Treating a repair-deficiency syndrome as proof that normal aging is a sum of such defects.
- Counting mutations as the amount of damage, when they are the errors that survived repair.

## Worked example

Between ages 20 and 80, Tissue A rises from 410 to 1990 substitutions per cell, so the average rate is (1990 − 410) / 60 = 26.33 per year. Tissue B rises from 150 to 470, a rate of 5.33 per year, so Tissue A accumulates about 4.9 times as fast. These are averages over six decades; they say nothing about whether the rate was constant, and a straight line through two points cannot show it. In Table 2 the mean fraction removed is 0.7175 for young and 0.545 for old cultures, a ratio of 0.76; that supports slower removal in the old cultures in this assay, and says nothing about whether the damage input differs.

## Limits of this lesson

The tables are synthetic and illustrate method. This lesson does not provide risk estimates for any person, does not suggest that any supplement or procedure improves DNA repair, and does not claim that mutation accumulation is the main cause of aging.

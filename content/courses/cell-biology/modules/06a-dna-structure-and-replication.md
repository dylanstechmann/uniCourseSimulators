# DNA structure, genome organization, and semiconservative replication

DNA replication copies information through complementary base pairing, but a fork is not a simple zipper. Strand polarity constrains polymerase chemistry; chromosome packaging constrains where replication begins; and the replication machinery must coordinate continuous and discontinuous synthesis while limiting errors. This lesson connects sequence orientation to fork behavior and uses a classic density-labeling design to distinguish competing models.

## Learning objectives

By the end of this lesson, you should be able to:

1. Write a complementary strand with explicit 5′ and 3′ direction and explain the chemical constraint behind 5′-to-3′ synthesis.
2. Distinguish leading- and lagging-strand synthesis and assign the major fork activities to opening, priming, extension, processivity, and joining.
3. Compare semiconservative, conservative, and dispersive replication predictions and identify what a density experiment can and cannot establish.
4. Relate replication origins to genome organization while avoiding the assumption that bacterial and eukaryotic chromosomes use identical initiation schedules.

## Sequence is directional

A DNA strand has a sugar-phosphate backbone with chemically distinct 5′ and 3′ ends. Complementary strands are antiparallel: one runs 5′ to 3′ while the other runs 3′ to 5′. A pairs with T and G pairs with C, but the complementary sequence must also be written in the opposite orientation. The strand sequence without direction is incomplete information.

DNA polymerases extend a primer's free 3′ hydroxyl using an incoming deoxynucleoside triphosphate. Bond formation releases pyrophosphate and extends the product at its 3′ end. Consequently, the new strand grows 5′ to 3′ while the polymerase reads a template 3′ to 5′. A polymerase cannot begin a new DNA chain from nothing; primase supplies a short RNA primer with a 3′ end that DNA polymerase can extend.

**Worked example.** Given template `3′-A C G T T A G C-5′`, place the matching base at each position and write the new strand antiparallel: `5′-T G C A A T C G-3′`. The written orientation matters: reading the same product from its 3′ end would reverse the displayed sequence order.

## A moving fork makes two different strands

As helicase separates the parental strands, single-strand binding proteins reduce unwanted re-pairing and secondary structure. Topoisomerases relieve torsional strain ahead of the fork. Primase lays down primers; replicative polymerases extend them; sliding clamps help keep polymerases associated with the template; primer removal, DNA synthesis, and ligase seal discontinuities. These functions are coordinated, but their molecular identities and organization vary across organisms.

At a fork moving to the right, a template oriented 3′ to 5′ in that direction supports continuous leading-strand synthesis toward the fork. The antiparallel template supports lagging-strand synthesis away from the fork in short 5′-to-3′ Okazaki fragments. The lagging strand is not synthesized 3′ to 5′; each fragment still grows 5′ to 3′ from a newly placed primer.

```text
Fork movement  →
Leading template    3′ ---------------------- 5′
New leading strand  5′ =====================> 3′
Lagging template    5′ ---------------------- 3′
New Okazaki pieces  3′ <=====5′   3′ <=====5′
                    each piece is synthesized 5′ → 3′
```

This coordination has to preserve the whole genome once per cell cycle. Many bacterial chromosomes use a prominent origin and bidirectional forks, whereas eukaryotic chromosomes use many licensed origins distributed across chromatin; only a subset fires at a given time under a regulated schedule. Nucleosomes are disassembled and reassembled as forks pass, and replication timing differs across genomic regions. An origin map therefore describes potential initiation sites, not a promise that every origin fires in every cell in every cycle.

## Copying model as an experimental question

In semiconservative replication, each daughter duplex retains one parental strand and contains one newly synthesized strand. Conservative replication would keep the two old strands together in one duplex and place both new strands together in another. Dispersive replication would distribute old and new DNA segments within both daughter strands.

The **following qualitative density patterns are predictions for a synthetic teaching comparison**, not reported measurements. Imagine first growing cells with a heavy nitrogen isotope, shifting them to light isotope medium, and separating extracted DNA by buoyant density. A density marker and samples from the heavy-grown and light-grown conditions help calibrate band positions. Cells must be allowed controlled numbers of generations; the extraction should avoid mixing generations or losing a density class.

| Model | After one generation in light medium | After two generations |
| --- | --- | --- |
| Semiconservative | One intermediate-density class | Intermediate and light classes, approximately half of each DNA molecule count in this ideal model |
| Conservative | Separate heavy and light classes | Heavy class persists as a smaller fraction; most molecules are light |
| Dispersive | One intermediate class | One class shifts toward light, rather than separate intermediate and light molecules |

One intermediate class after a single generation is compatible with both semiconservative and dispersive copying; the later appearance of separate intermediate and light classes distinguishes those predictions. A single image or band is interpretable only with gradient calibration, labeling controls, and a clear generation count. The experiment supports a copying model for the tested organism and conditions; it does not by itself explain every origin, fork protein, or genome in every cell type.

### Check your reasoning

For a template written `3′-A C G T T A G C-5′`, write the complementary strand with its orientation. Then explain why lagging-strand synthesis still proceeds 5′ to 3′, and name the additional generation result that distinguishes semiconservative from dispersive predictions.

## Provenance

This is original explanatory text and an original qualitative teaching table under the course’s CC BY 4.0 content license. MIT OpenCourseWare 7.28x Molecular Biology is linked as an undergraduate/graduate scope comparator. Meselson and Stahl’s 1958 paper and the NCBI Bookshelf chapter on replication mechanisms are link-only references. No source passage, figure, problem, or experimental dataset is copied or adapted.

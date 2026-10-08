# Cells for a scaffold: how many are needed, how much expansion that costs and whether it fits

A scaffold without cells depends on the host to supply them, and many strategies instead load the scaffold with cells grown outside the body. That raises a plain accounting question that every cell-based design must answer before any biology is considered: how many cells does the construct need, how many must be seeded to end up with that many, how many divisions does it take to grow them from a small starting sample, and does the answer fit in the volume available? Each step is arithmetic, and the answers show where a strategy is feasible, where it runs into limits of time and cell biology, and why variation between donors matters. All numbers here are synthetic. They do not describe any real tissue, cell type or procedure.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute the number of cells a construct needs and the number to seed given an attachment efficiency.
2. Compute the population doublings, expansion time and passages needed to reach that number from a starting sample.
3. Check feasibility against volume and time, and evaluate how donor variation and expansion limits affect a cell-based strategy.

## How many cells does the construct need?

The target is a cell density, which differs by orders of magnitude between tissues, times the volume to be filled. **Synthetic values:** a construct of V = 2.0 mL and a target density of 5.0 × 10⁷ cells/mL need N_target = 5.0 × 10⁷ × 2.0 = **1.0 × 10⁸ cells**. Not every seeded cell attaches and stays: with a seeding efficiency η = 60% the number to seed is N_seed = N_target/η = 1.0 × 10⁸/0.6 = **1.67 × 10⁸ cells**. A lower efficiency (for example 40%) raises the requirement to 2.50 × 10⁸.

## Expansion: doublings, time and passages

If the starting sample has N₀ = 5.0 × 10⁵ cells, the cell number must increase by a factor of 333, which takes n = log₂(N_seed/N₀) = log₂(333) = **8.38 population doublings** (so 9 whole doublings in practice). At a doubling time of 36 h this takes n × t_d = 8.38 × 36 h = 302 h = **12.6 days** if growth is exponential throughout. When cells are split 1:4 at each passage, each passage adds log₂(4) = 2 doublings, so 8.38/2 = 4.19, or **5 passages**. Real expansions take longer, because cells lag after each passage, slow down as they approach confluence, and the medium must be replaced; the exponential figure is a lower bound.

Doublings are also a cost in themselves. Primary cells can divide only a limited number of times, and the limit depends on the cell type and on the donor. Prolonged expansion can change cell behavior: for some cell types, growth on plastic in the usual way causes a loss of the specialized phenotype, so the cells put into a construct are not the cells taken from the sample. A plan with fewer doublings is therefore usually preferable to one with more, and a small starting sample is a risk, not only an inconvenience.

## Does it fit?

A cell occupies a volume of roughly 2 pL (2000 μm³). At the target density, cells occupy 5.0 × 10⁷ × 2 × 10⁻⁹ mL = 10% of the volume. Seeding the whole 1.67 × 10⁸ cells into 2.0 mL would place 8.33 × 10⁷ cells/mL there, or 16.7% of the volume, which is more than the final tissue contains and is unlikely to be achievable in pores that must also leave room for nutrients and matrix. A feasibility check therefore often shows that a design must seed fewer cells and rely on growth inside the construct, whose own limits (oxygen, nutrients, the scaffold's degradation) are the subject of other lessons.

## Donors and variability

Doubling time, yield from a sample and the ability to form tissue vary between donors. If the doubling time is 25% longer than assumed, the expansion time is 25% longer: 12.6 days becomes 15.7. A claim that an approach works needs several independent donors, since cells from one donor give n = 1 however many wells or constructs are made from them (see the statistics course's lesson on variability).

## Common mistakes

- Seeding the target number of cells and forgetting that only a fraction attach.
- Confusing doublings with passages, or ignoring the split ratio.
- Treating the exponential time as a prediction instead of a lower bound.
- Ignoring that expansion limits and phenotype change are costs of more doublings.
- Seeding at a volume fraction that the pores cannot hold.
- Treating wells or constructs from one donor as independent donors.

## Worked example

**Problem.** A synthetic construct of 0.5 mL needs 2.0 × 10⁷ cells/mL. Seeding efficiency is 50%, the starting sample has 2.0 × 10⁵ cells, the doubling time is 48 h and cells are split 1:3. Find the cells to seed, the doublings, the time and the passages.

**Step 1: target and seed.** N_target = 2.0 × 10⁷ × 0.5 = 1.0 × 10⁷; N_seed = 1.0 × 10⁷/0.5 = 2.0 × 10⁷.

**Step 2: doublings.** n = log₂(2.0 × 10⁷/2.0 × 10⁵) = log₂(100) = 6.64.

**Step 3: time and passages.** 6.64 × 48 h = 319 h = 13.3 days; each 1:3 split adds log₂(3) = 1.58 doublings, so 6.64/1.58 = 4.19, or 5 passages.

**Step 4: fit.** At the target density cells fill 4% of the volume; seeding all 2.0 × 10⁷ cells would give 8%, double that.

## Limits of this lesson

All numbers are synthetic. Growth is assumed exponential with a fixed doubling time and no cell loss, the cell volume is a round number, and the seeding efficiency and target density are placeholders. Real plans must also consider cell source, culture conditions, quality control and, for any use in people, regulation, none of which this lesson addresses. Nothing here is a protocol or a claim about any real cell type or tissue.

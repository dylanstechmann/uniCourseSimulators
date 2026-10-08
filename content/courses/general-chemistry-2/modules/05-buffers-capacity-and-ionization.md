# Buffers by design: Henderson–Hasselbalch, capacity and the ionization of weak acids and bases

Cells, culture media and nearly every biochemical assay depend on holding pH steady. A buffer does this with a weak acid and its conjugate base, which absorb added acid or base by shifting between the two forms. This lesson builds a buffer from its pKa, predicts its response to added acid, measures how much it can absorb, and applies the same equation to ask what fraction of a weak base is charged at physiological pH, a question that controls whether molecules cross membranes.

## Learning objectives

By the end of this lesson, you should be able to:

1. Use the Henderson–Hasselbalch equation to compute the base-to-acid ratio and component concentrations for a buffer at a target pH.
2. Predict the pH change of a buffer after adding strong acid and compare it with unbuffered water, using buffer capacity to explain the difference.
3. Calculate the ionized fraction of a weak acid or base at a given pH and evaluate its consequences for membrane permeation.

## The equation and its assumptions

For a weak acid HA ⇌ H⁺ + A⁻ with acid dissociation constant Ka, rearranging the equilibrium expression gives

**pH = pKa + log₁₀([A⁻]/[HA]).**

The equation assumes that the concentrations of HA and A⁻ are large compared with [H⁺] and [OH⁻], so that dissociation of the buffer itself does not change them appreciably. It uses concentrations in place of activities, which introduces errors at high ionic strength, and pKa depends on temperature and ionic strength. Treat the result as a design estimate, then measure.

## Designing a buffer

For a phosphate-type buffer with a synthetic teaching pKa of 6.86 and a target pH of 7.4, the required ratio is [A⁻]/[HA] = 10^(7.4 − 6.86) = 3.467. With total buffer 100 mM: [A⁻] = 0.1 × 3.467 / (1 + 3.467) = 77.6 mM, and [HA] = 22.4 mM.

A buffer works best within about one unit of its pKa, where both forms are present in comparable amounts. Choosing a buffer whose pKa is close to the target pH is the first design decision.

## Responding to added acid

Add 10 mmol of strong acid to 1 L of this buffer. The acid converts A⁻ to HA: A⁻ becomes 67.6 mM and HA becomes 32.4 mM, so

pH = 6.86 + log₁₀(67.6/32.4) = 7.18.

The pH falls by 0.22. The same acid added to 1 L of pure water would give pH = −log₁₀(0.01) = 2.0, a change of more than five units.

## Buffer capacity

Buffer capacity β is the amount of strong base (or acid) per liter needed to change pH by one unit, at the limit of small additions:

**β = 2.303 × C_T × Ka [H⁺] / (Ka + [H⁺])².**

For this buffer at pH 7.4, β = 40.0 mM per pH unit. Capacity is proportional to total buffer concentration and peaks when pH = pKa, where it equals 2.303 × C_T / 4. A buffer can therefore hold the right pH and still be easily overwhelmed if it is too dilute, which happens in cell culture when dense, metabolically active cells produce lactic acid.

## Ionization of weak bases and membrane crossing

The same equation tells how much of a weak base B is protonated (BH⁺) at a given pH. For a base whose conjugate acid has pKa = 9.0, the fraction un-ionized at pH 7.4 is 1 / (1 + 10^(9.0 − 7.4)) = 0.0245, about 2.5%. Charged forms cross lipid membranes poorly, so the un-ionized fraction controls passive permeation. Differences in pH between compartments, such as acidic lysosomes, can trap weak bases where pH is low, since they become more protonated there.

## Common mistakes

- Using the formula for an acid when the question is about a base (or the reverse): for a base, the un-ionized fraction rises with pH.
- Assuming that a buffer at the right pH will hold it under any load; capacity, not pH, sets how much acid it can absorb.

## Worked example

**Problem.** Culture medium is buffered at pH 7.4 by 25 mM total of a buffer with pKa 6.1, a bicarbonate-like value. What base-to-acid ratio does that require, and is the buffer near its best capacity?

**Step 1: ratio.** 10^(7.4 − 6.1) = 10^1.3 ≈ 20.0, so about 95% of the buffer is in the base form.

**Step 2: capacity.** At pH − pKa = 1.3, capacity is far below its maximum: almost all buffer is on one side, and added acid can be absorbed but added base cannot.

**Step 3: interpretation.** A closed system with this buffer would be weak. Bicarbonate is effective in the body and in incubators because CO₂ can be exchanged with the gas phase, which makes it an open system; that is why culture media need the correct CO₂ atmosphere to hold their pH.

## Limits of this lesson

pKa values are illustrative and treated as constants; activities, temperature dependence and polyprotic coupling are ignored. Nothing here is a recipe for a specific buffer or a statement about any drug.

# Coupled acid speciation and charge balance

## Learning objectives

1. Calculate diprotic species fractions at a stipulated hydrogen concentration.
2. Combine analytical mass balance with spectator charge and water equilibrium.
3. Check approximation domains and distinguish imposed pH from solved pH.

## One family, several forms

A diprotic acid family has H₂A, HA⁻ and A²⁻. Its analytical concentration C_T is their sum, not the concentration of any one form. Two dissociation steps define concentration-form teaching parameters K₁=[H⁺][HA⁻]/[H₂A] and K₂=[H⁺][A²⁻]/[HA⁻]. These dimensional parameters assume a declared ideal concentration convention; they are not silently identical to thermodynamic activity constants in every unit system.

For a synthetic family, stipulate K₁=10⁻⁵ mol/L and K₂=10⁻⁸ mol/L. At hydrogen concentration h=10⁻⁶ mol/L, the first ratio HA⁻/H₂A is 10 and the second ratio A²⁻/HA⁻ is 0.01. The second deprotonation is small here but not zero. Treating the family as two independent full-strength monoprotic acids would violate the common total amount.

## Fractions derived from ratios

Express both charged species in terms of H₂A and apply the total. The common denominator is D=h²+K₁h+K₁K₂. Species fractions are α₀=h²/D, α₁=K₁h/D and α₂=K₁K₂/D. Each is positive for positive parameters and their sum is one. This normalization provides a useful check before multiplying by an analytical concentration.

At the stipulated h, scaled denominator terms are 1, 10 and 0.1. Thus α₀=1/11.1≈0.090090, α₁=10/11.1≈0.900901 and α₂=0.1/11.1≈0.009009. For C_T=0.0100 mol/L, the concentrations are approximately 0.000901, 0.009009 and 0.0000901 mol/L. Their sum returns 0.0100. Rounding each prematurely can spoil that conservation check.

The mean negative charge per acid-family entity is α₁+2α₂≈0.918919. The doubly charged species contributes twice to electroneutrality, even though it contributes once to family mass balance. A fraction table and a charge table therefore answer different questions. Confusing the two can produce a formally normalized composition that is impossible for the stated spectator inventory.

## Imposed pH is not a solved pH

The fraction calculation assumes h is given. That might describe a mathematical comparison at an imposed pH, not a closed solution prepared with arbitrary amounts. To predict pH from analytical totals, add electroneutrality and any needed equilibrium relations. In this teaching model, let S be spectator-cation concentration minus spectator-anion concentration, measured as charge equivalents per litre. Then h+S=C_T(α₁+2α₂)+K_w,c/h.

Use the stipulated water parameter K_w,c=10⁻¹⁴ (mol/L)². For the supplied C_T=0.0100 and h=10⁻⁶ mol/L, the spectator difference required for charge balance is S≈9.18820 × 10⁻³ mol/L of charge equivalents. It is neither exactly C_T nor zero. A prescribed pH, analytical concentration and arbitrary spectator amount cannot all be imposed independently without checking their compatibility.

If S is given instead, solve the residual h+S−C_T(α₁+2α₂)−K_w,c/h=0 for positive h. Reject roots that imply negative species or violate the same total. A convenient numerical search can use logarithmic h to preserve positivity. The method still assumes the stipulated ideal chemistry and must be checked against both mass and charge balances after solving.

## Limits and dominant forms

When h is much larger than K₁, the neutral form dominates. Between well-separated K₁ and K₂, HA⁻ can dominate. When h is much smaller than K₂, A²⁻ dominates. These statements follow from comparing denominator terms, not from treating a transition boundary as a sudden all-or-none switch. Near either dissociation scale, multiple forms matter.

In the common amphiprotic approximation for a solution dominated by HA⁻, h≈√(K₁K₂), giving pH approximately 6.5 for these synthetic parameters. That shortcut requires suitable concentration, well-separated dissociation scales and negligible interfering contributions. It is not a universal pH for every mixture containing HA⁻. A full residual can test whether water or other charge contributions invalidate the approximation.

## Perturbation and interpretation

Changing analytical concentration while holding an externally imposed pH fixed scales every species concentration but leaves these ideal fractions unchanged. Changing concentration in a closed solution can instead shift pH because charge balance changes. The experiment or mathematical constraint determines which comparison is meaningful. The words “dilution changes ionization” need those conditions to be precise.

Activity coefficients, additional complexes, precipitation and temperature-dependent constants can alter actual speciation. The current fraction formulas do not calculate those effects. They remain useful as a transparent bookkeeping model whose assumptions can be examined. A disagreement with a measured pH would call for calibration and composition evidence, continuing the distinction developed in General Chemistry I.

## Worked example

At h=10⁻⁶, divide the denominator terms by h² to obtain 1,10,0.1. Normalize by 11.1 and multiply each fraction by C_T=0.0100. Compute family negative charge with one weight for HA⁻ and two for A²⁻. Add hydroxide 10⁻⁸ mol/L and subtract h to find the required spectator difference. This calculation gives both a normalized species table and the spectator inventory compatible with the imposed pH.

## Common mistakes

Do not count the doubly charged species twice in mass balance or once in charge balance. Do not use a prescribed pH as proof that arbitrary analytical amounts are consistent. State the concentration convention and check approximation assumptions.

## Limits of this lesson

Acid identities, constants and totals are synthetic; no reagent preparation or chemical handling procedure is supplied. Original instruction has substantial AI assistance, and the package remains partial, unreviewed and formative-only.

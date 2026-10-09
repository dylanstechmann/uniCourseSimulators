# Solubility, complexation and competing equilibria

## Learning objectives

1. Calculate stipulated ideal solubility and saturation quotients with correct stoichiometric powers.
2. Combine a solubility relation with a free-ligand complexation balance.
3. Distinguish a conditional threshold calculation from experimentally established selectivity.

## The solid phase matters

A solubility equilibrium relates dissolved activities while the specified solid phase is available. For hypothetical MX(s)⇌M⁺+X⁻, a concentration-form teaching parameter is K_sp,c=[M⁺][X⁻]. If pure water initially contains neither ion and all ideal assumptions apply, dissolution amount s gives both concentrations s, so s=√K_sp,c. A thermodynamic constant would instead use dimensionless activities and the relevant standard states.

Stipulate K_sp,c=10⁻⁸ (mol/L)² for invented MX. Pure-water solubility is 10⁻⁴ mol/L. This amount is not a measured solubility for an actual salt. The phase must remain present to impose the equality; if the total added solid is less than the amount required for saturation, it can dissolve fully and leave an undersaturated solution instead.

## Common-ion accounting

With a preexisting free X⁻ concentration of 0.0100 mol/L and no other process, dissolution adds s to both M and X. Solve s(0.0100+s)=10⁻⁸. The positive root is approximately 0.000001 mol/L, with the exact correction slightly below that approximation. Using K_sp,c/0.0100 is justified because s is small beside the initial common ion; the equation makes that check explicit.

For a separate hypothetical MX₂(s)⇌M²⁺+2X⁻, stipulate K_sp,c=4×10⁻¹² (mol/L)³ and no preexisting ions. Then [M]=s and [X]=2s, making the product s(2s)²=4s³. The solubility is again 10⁻⁴ mol/L. Taking a square root here would ignore both stoichiometric powers and the factor of four. Ionic strength and activity corrections are deliberately omitted.

## Quotient and onset

The current ion product Q_sp,c can be compared with K_sp,c under the same convention. If hypothetical MX has [M]=0.0010 and [X]=0.000020 mol/L, Q_sp,c/K_sp,c=2. The model is supersaturated with respect to that solid, so precipitation is thermodynamically favored. This does not determine nucleation speed or guarantee instantaneous visible precipitation.

At fixed free X=0.0100 mol/L, a metal with the stipulated MX constant reaches saturation at free M=10⁻⁶ mol/L. A second invented salt with K_sp,c=10⁻⁶ under the same one-to-one convention reaches saturation at free metal 10⁻⁴ mol/L. The hundredfold difference creates a conditional threshold interval. It does not yet establish complete separation, purity or practical recovery.

## Complexation changes free metal

Now suppose dissolved M⁺ also binds neutral L to form ML⁺, with K_f=[ML]/([M][L]) in the ideal concentration model. If free ligand l is externally held fixed, total dissolved metal is S=[M](1+K_fl). At solid saturation in pure-water MX with no initial X, free X equals total dissolved metal S because each dissolved formula unit releases one X. Therefore K_sp,c=S²/(1+K_fl).

Take the same MX constant 10⁻⁸ (mol/L)², K_f=10⁴ L/mol and stipulated free ligand l=0.0100 mol/L. Then K_fl=100 and S=√(101×10⁻⁸)≈1.00499 × 10⁻³ mol/L. Free metal is S/101≈9.95037 × 10⁻⁶ mol/L, while most dissolved metal is complexed. Increased total solubility can coexist with lower free metal concentration.

The fixed-free-ligand condition is essential. If ligand is supplied as a closed analytical total L_T, binding consumes it and l=L_T−[ML]. Then the simple fixed-l expression no longer applies without solving ligand balance. A real system may also contain several complexes, ligand protonation and competing solids. The current construction deliberately restricts the species and specifies free ligand rather than pretending ligand depletion is absent by default.

## Charge and amount checks

In this hypothetical case, M⁺ and ML⁺ each carry one positive charge. Their summed concentration S matches free X⁻ concentration S, preserving electroneutrality while neutral L supplies no additional charge. Each complex contains one metal, so metal total is [M]+[ML]. Ligand molecules do not create additional metal when they change how that total is partitioned.

Charge balance would look different for a divalent metal or a charged ligand. A net equilibrium equation can hide spectator ions but cannot remove them from full solution accounting. Changing species charges requires revisiting charge and ligand balances, rather than reusing the same equations because the variable names look similar. Conservation checks help expose a mathematically solvable but chemically incompatible setup.

## Selectivity needs more evidence

A threshold window at specified free-ion conditions provides a model hypothesis for selectivity. As one metal precipitates, free concentrations and ligand occupancy can change, potentially altering the second threshold. A target purity also depends on the amount remaining in solution, competing phases and recovery. Equilibrium onset is not a complete separation calculation.

Observed solid formation can be delayed, and a measured dissolved concentration can include complexes rather than only the free ion used in K_sp. Distinguish analytical measurement from species activity. Applying a solubility product directly to total metal in a complexing solution generally answers the wrong question. This lesson provides synthetic balances and no actual separation or handling procedure.

## Worked example

For MX in pure water, use s²=10⁻⁸. For common-ion conditions, retain s in 0.0100+s and check the small-change approximation. For MX₂, use 4s³ rather than s². In the fixed-free-ligand example, form 1+K_fl=101, solve for total S, then divide by 101 for free metal. Check the metal and charge totals before interpreting the larger dissolved amount.

## Common mistakes

Do not apply saturation equality after all solid has dissolved. Do not confuse free ions with total analytical concentrations. Match powers to stoichiometry and distinguish onset from complete selectivity.

## Limits of this lesson

All species, constants and observations are synthetic, with no reagent, purification or biological recommendation. Original instruction has substantial AI assistance. The package remains partial, unreviewed and formative-only.

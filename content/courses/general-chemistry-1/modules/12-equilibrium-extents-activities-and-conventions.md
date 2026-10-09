# Equilibrium extents, activities and conventions

## Learning objectives

1. Combine reaction stoichiometry and conservation with a stipulated equilibrium constant.
2. Compare reaction quotient and equilibrium constant for the same equation and standard-state convention.
3. Distinguish concentration approximations, thermodynamic activities and kinetic information.

## Equilibrium is dynamic balance

At chemical equilibrium, forward and reverse reaction rates balance macroscopically. Concentrations do not have to be equal, and reactions do not have to stop at the molecular scale. An equilibrium constant describes the equilibrium composition relationship for a specified reaction, temperature and standard-state convention. It does not supply the time required to reach that state.

For an idealized A⇌B reaction with dimensionless K=4, take activities as concentrations divided by c°=1 mol/L. Then K=a_B/a_A reduces to [B]/[A], because the same standard concentration cancels. If initial concentrations are A=1.0 mol/L and B=0.2 mol/L in a fixed volume, initial quotient Q=0.2, below K. Net forward change is favored by this model until the quotient reaches 4.

The stoichiometric concentration extent x changes A to 1.0−x and B to 0.2+x. Conservation fixes their sum at 1.2 mol/L. Solve (0.2+x)/(1.0−x)=4 to get x=0.76 mol/L. The equilibrium concentrations are A=0.24 and B=0.96 mol/L. Both are nonnegative and their sum remains 1.2. These checks catch an algebraic root that violates the physical amount constraints.

## Conservation and admissible roots

An equilibrium table is a compact way to represent initial values, changes and final values. It does not replace balancing the reaction. For a reaction consuming two A for each B formed, the A change would be −2x rather than −x. Every species amount and any charge balance must remain consistent with the proposed chemistry.

Nonlinear equilibrium equations can have several algebraic roots, but only roots with physically admissible concentrations and the stated conservation constraints describe the intended model. A small-change approximation is justified only after checking that the neglected change is small relative to the retained quantity. Repeating a familiar approximation without that check can fail when a reactant inventory is nearly exhausted.

In the A⇌B example, an assumed negligible x would be clearly invalid because the actual x=0.76 is large relative to initial A=1.0. The exact linear algebra is easy here, so no such approximation is needed. More complicated systems can require numerical root finding, but a solver's output still needs conservation and domain checks.

## Equation scaling changes K

Reverse A⇌B to B⇌A and its constant becomes 1/4. Double every coefficient to write 2A⇌2B and its quotient is (a_B/a_A)², so the constant becomes 16. The physical equilibrium compositions are consistent across those descriptions, while the numerical constant depends on the exact written equation. A quoted K without its reaction and convention is incomplete information.

Adding compatible reactions multiplies their equilibrium constants, just as their standard free-energy changes add. This relation needs matching temperatures and standard-state definitions. It does not permit multiplying arbitrary constants from different temperatures or differently defined empirical measurements without reconciling their conventions.

For a reaction whose stoichiometric totals differ between sides, concentration factors do not all cancel. Normalize every activity consistently before writing a thermodynamic quotient. A concentration-form constant can be convenient but may carry apparent units when written without standard-state normalization; it must not be silently treated as the same numerical quantity under a unit conversion.

## Activities and a nonideal illustration

In a concentration-based activity convention, write a_i=γ_i c_i/c°. The activity coefficient γ represents departure from the chosen ideal reference. Suppose synthetic A and B concentrations are 0.5 and 1.0 mol/L, with supplied γ_A=0.8 and γ_B=0.6. Then Q=(0.6×1.0)/(0.8×0.5)=1.5, rather than the concentration ratio 2.0. These coefficients are stipulated for the exercise, not calculated from a real solution or an ionic-strength model.

For a pure solid or liquid in its reference state, the corresponding activity is commonly taken as one in the standard expression. Its amount can still affect whether that phase is present or exhausted. Omitting a pure-solid activity term is not permission to ignore whether any solid remains. Gas activities may need fugacity rather than raw pressure when nonideality matters.

Temperature can change K. Changing composition at a fixed temperature changes Q and can move the system toward equilibrium; it does not by itself change the thermodynamic K for that same reaction and convention. Adding a catalyst can change approach rates without changing that equilibrium constant. These distinctions prevent using an equilibrium calculation as a kinetics or mechanism claim.

## Worked example

Start with A=1.0 and B=0.2 mol/L under ideal activity assumptions. Use extent x to preserve A+B=1.2, set the quotient equal to 4 and obtain x=0.76. Check final concentrations 0.24 and 0.96, their ratio 4 and their conserved sum. Reverse the equation for K=0.25 or double it for K=16. For the separate supplied nonideal composition, apply both activity coefficients and obtain Q=1.5. Mixing the ideal and nonideal conventions would compare quantities from different models.

## Common mistakes and checks

Do not equate equilibrium with equal concentrations or zero microscopic reaction rates. Do not forget stoichiometric powers or unit normalization. Reject negative-concentration roots and unverified small-change approximations. Distinguish Q, which changes with the current state, from K for the specified conditions. A catalyst does not establish a different equilibrium composition merely by accelerating the process.

## Limits of this lesson

Species, constants and activity coefficients are synthetic. The lesson does not calculate actual activity coefficients, real gas fugacities or a complete coupled speciation system. No experimental equilibrium protocol is supplied. Practice checks selected amounts and model conventions, not kinetic behavior or proof quality. Original instruction has substantial AI assistance and uses the existing chemistry scope reference without copied text. The package remains partial, unreviewed and formative-only.

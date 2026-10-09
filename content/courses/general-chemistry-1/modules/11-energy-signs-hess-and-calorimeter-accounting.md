# Energy signs, Hess' law and calorimeter accounting

## Learning objectives

1. Apply the first law with explicit system and work sign conventions.
2. Calculate reaction heat and molar enthalpy from a stipulated calorimeter model.
3. Combine state-function changes and identify omitted energy or measurement terms.

## Choose the system first

With the chemistry sign convention, ΔU=q+w, where heat entering the system is positive and work done on it is positive. For a synthetic process with q=+500 J and w=−200 J, internal-energy change is +300 J. The system gains heat but does work on its surroundings. Reversing which object is called the system changes how exchanged heat and work are labeled; it does not violate conservation.

For pressure-volume work against constant external pressure, w=−P_extΔV. Expansion has positive ΔV and negative work under this convention. With P_ext=100 kPa and expansion 1.5 L, w=−150 J because kPa·L is J. The external pressure belongs in this expression, not an arbitrary endpoint internal pressure for a nonequilibrium process. Other work forms require their own terms.

Internal energy and enthalpy are state functions. Heat and work are path-dependent transfers, so neither is an amount stored in a system as “heat content.” Different paths between the same states can exchange different q and w while giving the same ΔU. Distinguishing state change from transfer makes sign checks more reliable than memorizing that every reaction is “positive” or “negative.”

## What a calorimeter measures in a model

For a stipulated constant-pressure calorimeter with no non-pressure-volume work and negligible heat exchange with the outside, reaction heat is minus the heat gained by solution and calorimeter: q_rxn=−(mc+C_cal)ΔT. The solution term uses its mass m and specific heat c; C_cal is the separate calorimeter heat capacity. A temperature increase means these surroundings gain heat and the reaction releases it.

Use synthetic values m=100 g, c=4.00 J/(g·K), C_cal=20.0 J/K and ΔT=+3.00 K. Total heat capacity is 420 J/K and gained heat is 1260 J. Thus q_rxn=−1260 J. For stipulated reaction amount 0.0200 mol, ΔH_rxn≈−63.0 kJ per mole of reaction extent under this model. The amount must match the balanced reaction convention; “per mole” needs a specified entity or reaction extent.

Ignoring C_cal would give −1200 J and underestimate the released magnitude here. Ignoring heat loss can also change the inferred magnitude, but a discrepancy alone does not identify its cause. Specific heat can differ from a pure-solvent approximation, initial temperatures can differ, and an incomplete reaction can change the amount actually converted. The numerical example is an energy-accounting model, not a procedure for mixing actual substances.

## Enthalpy and internal energy

By definition H=U+PV. For initial and final ideal-gas states at the same temperature, ΔH=ΔU+Δn_gRT, with nongaseous pressure-volume contributions neglected in this simplified comparison. For a stipulated ΔU=−10.0 kJ and gas-amount change Δn_g=+2.0 mol at 300 K using R=8.314 J/(mol·K), the correction is +4.9884 kJ and ΔH=−5.0116 kJ.

This relation is not a general replacement for the first law along every path. It compares state functions under the given ideal-gas and temperature assumptions. Constant-volume heat equals ΔU only with the needed work restrictions; constant-pressure heat equals ΔH under corresponding restrictions. State the conditions before treating either measurement as a state-function change.

## Combining reactions

Hess' law uses the path independence of enthalpy. For constructed steps A→B with ΔH=−40 kJ and B→C with ΔH=+15 kJ, adding the equations cancels B and gives A→C with ΔH=−25 kJ. Reversing a step reverses its enthalpy sign. Multiplying all coefficients by a factor multiplies that step's enthalpy by the same factor.

These labels are hypothetical species and states, not actual tabulated reactions. In an application, the chemical equation, phases and reference states must be specified. A water liquid product and a water vapor product correspond to different enthalpy changes. Formation-enthalpy accounting requires coefficient-weighted product totals minus coefficient-weighted reactant totals, not an unweighted list of values.

Energy conservation does not ensure that a reaction is fast or that a negative enthalpy alone makes it spontaneous under every condition. Entropy and temperature matter for a full free-energy analysis, developed further in General Chemistry II. A calorimeter temperature rise therefore does not by itself establish reaction completeness, mechanism or biological suitability.

## Worked example

The synthetic calorimeter has solution heat capacity 100×4.00=400 J/K plus 20 J/K from the calorimeter. A 3 K rise gives surroundings heat +1260 J, so reaction heat is −1260 J. Divide by 0.0200 mol and convert J to kJ to obtain −63.0 kJ/mol of extent. Separately, add Hess steps −40 and +15 for −25 kJ. In the gas-state comparison, add the positive Δn_gRT correction to ΔU=−10 kJ for ΔH=−5.0116 kJ. These calculations use distinct assumptions even though each tracks energy.

## Common mistakes and checks

Do not use the same sign for reaction heat and surroundings heat in an isolated exchange. Do not omit a stated calorimeter heat capacity. Do not multiply a reaction without scaling its enthalpy. Match phases and reaction extent when interpreting molar values. Check that every term in an energy sum has the same units; a temperature alone is not an energy.

## Limits of this lesson

All process values, Hess steps and calorimeter observations are synthetic. No chemical handling protocol, material enthalpy recommendation or real apparatus validation is supplied. The model omits several real heat-flow and composition effects. Practice checks selected energy balances rather than experimental reliability or written derivations. Original content has substantial AI assistance; the package remains partial, unreviewed and formative-only.

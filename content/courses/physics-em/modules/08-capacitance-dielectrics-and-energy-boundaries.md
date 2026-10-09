# Capacitance, dielectrics and energy boundaries

## Learning objectives

1. Calculate geometry-based capacitance, charge and stored energy with consistent scales.
2. Distinguish isolated-charge and fixed-voltage dielectric changes.
3. Check source work, mechanical energy transfer and the limits of an ideal capacitor model.

## A geometry and a boundary condition

Capacitance relates conductor charge magnitude to potential difference under a specified geometry and dielectric response. For an ideal parallel-plate model with uniform gap field and negligible edge effects, C=εA/d. This relation requires the stated plate area, separation and permittivity; it is not a universal formula for every electrode shape or a direct identification of a biological membrane's molecular structure.

Stipulate a synthetic vacuum gap with ε₀=8.854×10⁻¹² F/m, area A=0.0020 m² and separation d=0.0010 m. Capacitance is 17.708 pF. A linear dielectric fully filling the gap with relative permittivity κ=4 changes this to 70.832 pF if the geometry remains fixed. These parameters are invented teaching values rather than measured properties of a named material.

The [OpenStax dielectric section](https://openstax.org/books/university-physics-volume-2/pages/8-4-capacitor-with-a-dielectric) provides a link-only reference for the distinction between fixed free charge and fixed voltage. No worked problem, image or material-property table is imported. The independent numerical construction here uses the same general physical relations with explicitly supplied values and conditions.

## Charge and energy before the change

At an initial potential difference 6.0 V, the vacuum capacitor has plate charge magnitude Q=CV=106.248 pC. Stored electrostatic energy is U=0.5CV²=318.744 pJ. Equivalent expressions Q²/(2C) and QV/2 describe the same state when Q=CV. Mixing Q from one state with V or C from another would produce an inconsistent energy calculation.

Positive and negative plates carry equal opposite charges in this ideal two-conductor construction. Q is a plate magnitude, not net charge on the combined capacitor. A field across the gap can exist even though the pair's total net charge is zero. This parallels the earlier distinction between a closed-surface flux balance and a local field value.

## Isolated free charge

First consider a mathematical change after the capacitor is isolated, with no leakage or conductive charge path. Free plate charge stays at its initial value while dielectric polarization changes capacitance. With C increased fourfold, V becomes Q/C=1.5 V and stored energy becomes 79.686 pJ. The initial-to-final energy reduction is 239.058 pJ.

That reduction does not imply energy vanished. A complete process must account for mechanical transfer, dielectric response and any losses. Under an ideal quasistatic lossless insertion interpretation, electrical energy can be transferred mechanically. The lesson specifies endpoint states rather than a real insertion mechanism or apparatus procedure. If leakage or time-dependent dielectric loss occurs, the isolated-free-charge assumption no longer suffices.

The potential difference decreases because the same free charge is associated with a larger capacitance. Dielectric polarization introduces bound charge effects, but it does not supply an extra arbitrary free-charge inventory. A material can remain electrically neutral overall while having polarized charge separation. Neither polarization nor larger capacitance proves that a dielectric is a conductor.

## Voltage held by an ideal source

Now consider a separate process in which an ideal source maintains 6.0 V during the same fourfold capacitance change. Final free charge is 424.992 pC and final stored energy 1274.976 pJ. Charge has entered from the source, so the isolated-charge formula for final voltage would describe the wrong boundary condition.

The source supplies electrical work VΔQ=6×318.744 pC=1912.464 pJ. The capacitor energy increase is 956.232 pJ. In the selected ideal quasistatic lossless interpretation, the remainder is mechanical energy transfer. This ledger explains why comparing only capacitor energy endpoints cannot determine total source work. A resistor, rapid switching or nonideal dielectric would introduce additional terms.

The signs depend on whether work is counted into the capacitor system or out of the electrical subsystem. Keep a written ledger: source work equals stored-energy increase plus mechanical transfer and any dissipation. Calling every energy term simply “work” without the system boundary can obscure an otherwise straightforward conservation check.

## Network and material limits

For independent ideal capacitors in parallel, equal voltage and additive plate charges give additive capacitance. In series without extra intermediate-node charge, equal charge magnitude and additive voltages give additive reciprocal capacitance. These connection rules follow their constraints; they should not be selected merely from a drawing's visual spacing.

Real dielectric response can depend on frequency, field, temperature and history. A measured capacitance can therefore be an effective parameter over a stated range. The present κ is linear and constant, with no breakdown, leakage or loss model. Extrapolating the example to a high-field device or tissue would require information that is not supplied by these endpoints.

## Worked example

Calculate vacuum C=17.708 pF from geometry, then initial Q=106.248 pC and U=318.744 pJ at 6 V. For the isolated process hold Q fixed, obtaining V=1.5 and U=79.686 pJ. For the separate fixed-voltage process hold V fixed, obtaining Q=424.992 pC and U=1274.976 pJ. Include source work before interpreting the energy difference.

## Common mistakes

Do not keep both free charge and voltage fixed when capacitance changes. Do not confuse the pair's net charge with one plate's charge magnitude, or stored-energy increase with all source work. State dielectric extent, geometry and the electrical boundary condition before applying a formula.

## Limits of this lesson

All geometry and parameters are synthetic. Uniform fields, ideal conductors, linear polarization and lossless endpoint balances are restricted models, not a real material specification or handling procedure. No third-party teaching asset was copied. Original instruction has substantial AI assistance. Workload, subject-matter and accessibility review remain outstanding; the course stays partial, unreviewed and formative-only.

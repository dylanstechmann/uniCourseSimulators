# RC switching, initial conditions and energy

## Learning objectives

1. Solve a first-order RC transition with a specified initial capacitor voltage.
2. Balance source work, capacitor energy and resistor dissipation.
3. Distinguish circuit time constants from biological or observation-model parameters.

## The state before the event matters

An ideal capacitor stores charge and electrostatic energy. Its current in a passive sign convention is i=C dV_C/dt. With finite current through a finite resistance, capacitor voltage cannot jump instantaneously; a jump would require an impulsive current outside that finite-current assumption. A switch can change the equation while the initial stored state remains part of its solution.

Stipulate a synthetic series network with ideal source V_s=3.0 V, resistance R=200 kΩ and capacitance C=0.50 µF. At the selected t=0 event, capacitor voltage is V₀=1.0 V. The equation is C dV_C/dt=(V_s−V_C)/R. Its time constant is RC=0.10 s and solution V_C=3−2exp(−t/0.10) V for t≥0.

The initial current is (3−1)/200000=10 µA. After one time constant, capacitor voltage is 3−2/e≈2.264241 V. The fraction 1−1/e describes the completed fraction of the transition from initial to final state, not always the fraction of final voltage. Here the capacitor starts above zero, so calling its voltage “63% of final” would be incorrect.

## A transition can go downward

If an initial voltage exceeds the newly selected source voltage, the same first-order equation predicts a downward transition and current opposite the reference charging direction. A negative current is compatible with the passive sign convention. The model must permit the ideal source to absorb returned energy when the state demands it; a real source's behavior could be more restricted.

For a separate discharge through a resistor with source replaced by the stated zero-voltage connection, V_C=V₀exp(−t/RC). The resistor's power remains nonnegative even though the current reference can be negative. Its heat equals the initial stored energy over a complete ideal discharge, provided there are no other energy-storage or transfer paths.

Changing a resistor changes the transition rate while leaving the same ideal steady voltage in the simple unloaded series circuit. Changing an additional load can change both rate and final voltage. That distinction becomes essential when an instrument input resistor sits in parallel with the capacitor: the correct resistance for the time constant is then the resistance seen by the capacitor under the specified source suppression.

## Source work is not just stored energy

For the constructed upward transition, initial capacitor energy is 0.5C×1²=0.25 µJ. Final energy at 3 V is 0.5C×3²=2.25 µJ, an increase of 2.00 µJ. Total charge supplied over the complete transition is C(3−1)=1.00 µC. The ideal constant-voltage source supplies work V_sΔQ=3.00 µJ.

The remaining 1.00 µJ is dissipated in the resistor. Integrating i²R gives 0.5C(V_s−V₀)² for this full transition. Resistance changes how quickly dissipation occurs, but this ideal endpoint expression does not depend on its value. That cancellation does not hold for every switched network, finite-time interval or nonideal energy-recovery circuit.

An instantaneous-power check is also useful: source power V_si equals the rate of capacitor-energy increase V_Ci plus resistor power i²R. This follows the loop relation V_s=V_C+iR. Integrating the three terms provides an independent numerical test of the analytic solution and catches a reversed sign or a missing stored-energy term.

## Time constant extraction

If initial and final voltages are independently known, the remaining fraction is (V_final−V(t))/(V_final−V_initial). Its logarithm is −t/τ in the ideal one-mode model. A baseline reporting offset must be handled consistently; confusing raw report values with voltage can bias a fitted time constant. A multiplicative gain cancels in a properly normalized ratio only when it is shared and constant.

A single transient's fitted τ constrains a product or equivalent combination of circuit parameters. It does not uniquely identify R and C separately. Independent resistance information or another informative perturbation can distinguish them. Likewise, observing a slower trace does not automatically prove a slower biological process when source and measurement impedances are uncharacterized.

The preserved membrane lesson describes an effective capacitance/resistance model. The present circuit examples do not identify an actual membrane's conductances or validate their constancy. A membrane can have nonlinear, voltage-dependent and multiple time-dependent processes. A clean exponential is compatible with a useful restricted model while leaving those additional possibilities unresolved.

## Worked example

Start with V₀=1 rather than a default zero state. Use τ=0.10 s and transition amplitude 2 V to evaluate V_C(0.10). Check initial current 10 µA from the resistor drop. Independently calculate initial/final capacitor energies, source charge and source work. Verify 3.00 µJ supplied equals 2.00 µJ stored plus 1.00 µJ dissipated, and compare with a numerical time integral.

## Common mistakes

Do not restart capacitor voltage at zero merely because a switch moves. Do not apply a 63% slogan to a nonzero initial state, identify τ as capacitance alone or equate source work with stored-energy increase. The resistance seen by a capacitor depends on all relevant branches and source conditions.

## Limits of this lesson

All voltages, component values and switching events are synthetic mathematical conditions. The model supplies no apparatus operation, patient connection or biological recommendation. Ideal switching, constant components and one exponential do not validate a real sensor or membrane. Original instruction has substantial AI assistance. Workload, accessibility and subject-matter review remain absent; the course stays partial, unreviewed and formative-only.

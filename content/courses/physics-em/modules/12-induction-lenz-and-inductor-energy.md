# Induction, Lenz signs and inductor energy

## Learning objectives

1. Calculate signed flux-linkage changes with an explicit contour and normal.
2. Compare stationary-loop induction with a restricted motional-emf model.
3. Balance electrical, magnetic and mechanical energy in declared resistive or RL systems.

## Choose orientation before assigning a sign

Magnetic flux through a selected surface is the integral of B dotted with its oriented area element. For a flat loop in a uniform perpendicular field, it reduces to BA with a sign fixed by the normal. A tilted loop instead needs the appropriate component. Flux linkage for N identical turns is N times each turn's flux, not merely the single-turn flux renamed.

Stipulate a stationary synthetic 20-turn loop with each turn's area 0.0030 m². Its chosen normal is +z, and positive circulation is counterclockwise when viewed from the +z side looking toward the loop. Let the uniform field be B_z=0.10+0.020t² T, with t in seconds. At t=3, each turn's flux is 0.000840 Wb and linkage is 0.01680 Wb-turn.

Faraday's law gives emf in that positive circulation as −d(NΦ)/dt. At t=3, dB/dt=0.120 T/s, so signed emf is −0.00720 V or −7.20 mV. If the contour definition reverses, its area normal must reverse too, and the reported emf sign reverses consistently. The physical opposition does not depend on arbitrarily renaming the positive direction.

## Lenz describes a change

For a closed resistive loop under these assumptions, the negative circulation corresponds to clockwise current as seen from +z. Its induced field points in −z, opposing the increasing +z flux. Lenz's rule concerns the change in flux, not a requirement that induced field always oppose the present field. A decreasing positive flux would call for a positive induced field instead.

An open loop can have an induced emf without a circulating conduction current. A resistance, inductance and complete conductive path are needed to calculate a current history. Dividing a changing emf by resistance alone assumes any inductive transient is negligible. The present signed-emf example does not claim that every real coil current follows that immediate relation.

## Motion can produce an emf

The [OpenStax motional-emf section](https://openstax.org/books/university-physics-volume-2/pages/13-3-motional-emf) is a link-only reference for magnetic force in a moving conductor. Consider a separate ideal straight conducting bar of length 0.20 m moving at speed 0.50 m/s perpendicular to a uniform 0.30 T field, with orientation arranged so v×B acts along the bar. Emf magnitude is Blv=0.030 V.

Charge separation in an open moving bar can produce an electric field balancing the magnetic force under the selected steady model. In a complete moving-boundary loop, a consistent flux-change description includes the motion of the boundary, rather than treating its area as fixed. Do not differentiate only B while ignoring an explicitly changing loop area.

For a closed bar-and-rails construction with total resistance 10 Ω and negligible inductance, current magnitude is 3.0 mA. The bar's magnetic force opposing motion has magnitude IlB=0.00018 N. Maintaining the stated speed requires matching external mechanical power Fv=0.000090 W, or 90 µW. Resistive heat I²R is the same 90 µW.

The matching powers provide an energy check beyond the emf formula. The field need not be an energy source simply because it appears in Blv; the prescribed mechanical motion supplies energy in this restricted generator model. Return-path geometry and ideal rails are part of the construction, not an apparatus design. If inductance is significant, magnetic-energy change joins the ledger.

## An inductor stores a current state

For an ideal linear inductor in a passive sign convention, voltage is L di/dt and magnetic energy is Li²/2. Finite voltage cannot make its current jump instantaneously. This is the current-state counterpart of a capacitor's finite-current voltage continuity. The inductor voltage sign changes according to whether current is increasing or decreasing, not according to one permanently assigned source polarity.

Stipulate a separate series RL network with source 2.0 V, R=20 Ω, L=0.040 H and initial current zero. Its equation is L di/dt+Ri=2.0. Time constant L/R is 0.0020 s, and final current is 0.10 A. At the final state, stored magnetic energy is 0.00020 J, or 200 µJ. The resistor continues dissipating power under a sustained source even after magnetic energy stops changing.

Thus total source work over an indefinitely driven RL interval is not bounded by the final magnetic energy. At every instant source power equals resistor heat rate plus d(Li²/2)/dt. Integrating over a stated finite interval gives a meaningful energy comparison. Switching the source to a declared passive discharge path gives another model with decreasing current; a real disconnected coil requires more boundary information than the ideal word “open.”

## Worked example

At t=3, calculate B=0.28 T and each-turn flux 840 µWb, then differentiate the specified field for emf −7.20 mV under the +z/positive-contour convention. For the separate moving bar, find 30 mV and 3 mA, and verify mechanical power equals resistor heat. For the separate RL model, find τ=2 ms, final current 100 mA and stored energy 200 µJ.

## Common mistakes

Do not omit turns, confuse flux with flux linkage, apply a magnitude as a signed emf or oppose the field rather than its change. Do not infer current from an open-loop emf, omit moving area from a flux derivative or equate all sustained-source work to final inductor energy.

## Limits of this lesson

Every field, loop, bar, component and motion is synthetic. Ideal uniform fields, rails, negligible inductance in one example and linear inductance in another are supplied assumptions. No coil switching, hardware handling or biological procedure is given. Original text uses no imported teaching asset and has substantial AI assistance. The package stays partial, unreviewed and formative-only.

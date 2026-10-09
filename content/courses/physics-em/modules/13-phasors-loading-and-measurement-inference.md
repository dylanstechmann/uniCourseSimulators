# Phasors, loading and measurement inference

## Learning objectives

1. Calculate impedance and voltage transfer with an explicit phasor convention.
2. Distinguish peak, RMS and time-averaged power in resistive and reactive elements.
3. Separate circuit loading, reporting calibration and unsupported biological inference.

## State the convention

For a sinusoidal steady state, write a real signal as the real part of a complex amplitude times exp(jωt), with j²=−1. Here complex amplitudes are peak amplitudes. Under this convention a resistor has impedance R, an ideal capacitor 1/(jωC) and an ideal inductor jωL. Changing the time convention changes some algebraic signs, so phase statements must retain their convention.

A phasor describes a steady single-frequency component rather than the entire switch-on transient. It cannot by itself supply an initial capacitor voltage or predict every response to a discontinuous event. The preceding RC and RL time-domain lessons describe those state-dependent transitions; steady phasors offer a complementary calculation under different conditions.

## A parallel input and a series source

Stipulate a synthetic source resistance R_s=100 kΩ driving an input with resistance R_in=1.0 MΩ in parallel with capacitance C_in=1.0 µF. Let the source sinusoid have peak amplitude 1.0 V at angular frequency ω=10 rad/s. Input admittance is 1/R_in+jωC_in; the series resistor's drop depends on that complete current, not on input resistance alone.

The source-to-input transfer is H=1/[1+R_s/R_in+jωR_sC_in]. At the stipulated frequency, its denominator is 1.1+j1.0. Consequently magnitude is 1/√2.21≈0.672673 and phase is −atan(1/1.1)≈−42.273689 degrees. The input peak amplitude is 0.672673 V, and it lags the source under the declared convention.

At zero frequency the transfer tends to R_in/(R_s+R_in)=10/11≈0.909091. At high frequency the capacitance lowers input impedance and increases attenuation. A large DC resistance therefore does not establish negligible loading at every frequency. The input capacitance contributes a physical filtering effect even if a voltage report is perfectly calibrated.

## A pole and a steady-state loss

The same transfer can be written H₀/(1+jωτ), with H₀=10/11 and τ=(R_s parallel R_in)C_in=0.090909 s. Its pole frequency in cycles per second is 1/(2πτ)≈1.750704 Hz. The magnitude at that frequency is H₀/√2, which is a drop relative to the already loaded low-frequency gain rather than necessarily relative to one.

The lab changes only R_in between two declared values while holding source resistance and input capacitance fixed. With R_in=100 kΩ, H₀ becomes 0.5 and τ becomes 0.050 s. Both observed amplitude and time constant change without changing the source generator. This provides a controlled mathematical counterexample to interpreting every smaller or faster trace as a change in biology.

## RMS and energy

For a zero-mean sine wave, RMS voltage is peak voltage divided by √2. The input voltage here has RMS approximately 0.475651 V. The input resistor's average power is V_rms²/R_in≈0.226244 µW. An ideal capacitor can absorb and return energy during a cycle while its average real power is zero in the steady lossless model.

The [OpenStax AC-power section](https://openstax.org/books/university-physics-volume-2/pages/15-4-power-in-an-ac-circuit) is a link-only reference for RMS and cycle-average distinctions. The circuit values and transfer example are independently constructed. No source problem, graph or figure is copied. Instantaneous power remains voltage times current; integrating it over a complete cycle checks the average rather than replacing RMS with peak values without the required factor.

For a general sinusoidal load with phase difference φ, average real power is V_rms I_rms cosφ under a compatible passive sign convention. Apparent magnitude V_rms I_rms alone does not identify heating power. A nonideal capacitor can have losses, but those require a supplied model; they do not arise simply because its impedance is complex.

## Reporting is another transformation

Suppose a separate voltage-reporting channel uses y=b+gV_node. A zero-voltage reference identifies an additive b; an independently known nonzero voltage identifies g after subtracting b. Recovering V_node from y corrects reporting, while recovering the open-circuit source still requires H or the corresponding time-domain circuit. Those corrections answer different questions.

A frequency sweep could constrain an effective transfer, but multiple circuit realizations can share that transfer over a limited range. One measured phase or amplitude cannot uniquely identify every electrode, source and input parameter. Independent reference information and a deliberately varied known load supply additional constraints. This distinction matters for the preserved high-impedance recording case.

## Worked example

Build parallel input admittance, add the series source drop and solve H=1/(1.1+j). Obtain amplitude and negative phase with the stated convention. Convert the input's peak voltage to RMS before calculating resistor power. Independently factor the transfer into H₀ and τ, then predict how changing only input resistance alters both. Keep reporting baseline/gain correction separate from this circuit transfer.

## Common mistakes

Do not treat impedance magnitudes as signed real resistances when adding branches. Do not confuse angular frequency with cycles per second, peak with RMS or reactive exchange with net dissipation. A calibrated loaded signal is still loaded; a fitted pole alone does not establish a unique biological mechanism.

## Limits of this lesson

All source, input and reporting values are synthetic. Linear steady-state and lumped-element models supply no real digitizer specification, patient connection or validated electrode transfer. Written inference and phasor drawings are not automatically graded. Original instruction has substantial AI assistance. Qualified review and measured workload remain absent; the package stays partial, unreviewed and formative-only.

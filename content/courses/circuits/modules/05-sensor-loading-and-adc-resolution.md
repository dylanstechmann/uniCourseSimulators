# Reading a sensor without fooling yourself: voltage dividers, loading error and ADC resolution

Laboratory instruments, from a culture-incubator thermistor to an electrode measuring a cell's potential, turn a physical quantity into a voltage, and an analog-to-digital converter (ADC) turns that voltage into a number. Two errors creep in at the interface: the measuring circuit draws current and changes the voltage it is trying to read (loading), and the ADC can only resolve steps of a certain size. This lesson quantifies both with a voltage-divider sensor, an electrode with a high source resistance, and a 12-bit converter.

## Learning objectives

By the end of this lesson, you should be able to:

1. Analyze a voltage divider and a source with internal resistance using a Thevenin equivalent.
2. Calculate the loading error when a measuring input of finite resistance is connected, and choose an input resistance that keeps the error below a target.
3. Compute ADC resolution and convert it into the smallest change in the measured physical quantity, and evaluate which error dominates.

## The voltage divider

Two resistors in series across a supply V_s give, at their junction, **V_out = V_s R₂ / (R₁ + R₂)**. Many sensors are resistors whose value changes with the measured quantity (thermistors with temperature, strain gauges with strain), so placing one in a divider turns resistance into voltage.

**Synthetic thermistor circuit:** V_s = 3.3 V, fixed resistor R₁ = 10 kΩ, thermistor R₂ = 12.5 kΩ at the current temperature. Then V_out = 3.3 × 12.5 / (10 + 12.5) = 1.833 V.

## Thevenin equivalents and loading

Any linear network seen from two terminals behaves like an ideal voltage source V_th in series with a resistance R_th. For the divider, V_th is the open-circuit V_out and R_th is R₁ and R₂ in parallel. When a meter or amplifier with input resistance R_in is connected, it forms a second divider with R_th:

**V_measured = V_th × R_in / (R_th + R_in).**

The relative error is R_th / (R_th + R_in): small only when R_in ≫ R_th.

For the thermistor divider, R_th = (10 × 12.5)/(10 + 12.5) = 5.56 kΩ. Connecting an input of 100 kΩ (equivalently, placing it in parallel with the thermistor) changes the reading from 1.833 V to 1.737 V, an error of 5.3%, which a temperature calibration would silently absorb or misattribute.

**Electrodes are worse.** A glass microelectrode or a pH electrode can have a source resistance of megaohms to gigaohms. With a synthetic R_s = 1 MΩ and an amplifier input of 10 MΩ, the amplifier sees 90.9% of the true voltage: a 9.1% error. With a 1 GΩ input the error falls to 0.10%. This is why electrophysiology and pH meters use amplifiers with very high input impedance (buffers or electrometer inputs).

## ADC resolution

An N-bit ADC divides its reference range into 2ᴺ steps. One least significant bit (LSB) is **V_ref / 2ᴺ**. For a 12-bit converter with a 3.3 V reference, 1 LSB = 3.3 / 4096 = 0.806 mV. If the sensor circuit produces 40 mV per °C near the operating point, the smallest resolvable temperature step is 0.806 / 40 = 0.020 °C.

Resolution is not accuracy. A reading can be resolved to 0.02 °C and still be wrong by 0.5 °C because of loading, calibration error, self-heating of the thermistor, or reference-voltage drift. Noise also matters: if electrical noise at the input is larger than one LSB, the last bits are noise, and averaging several samples is needed to use them.

## Which error dominates?

List each source with its size in the measured quantity: resolution (0.020 °C here), loading (a percent-level gain error unless the input resistance is high), calibration uncertainty of the reference, noise and drift. The largest one sets the useful precision; improving the others changes little. This is the same logic as error propagation in solution preparation.

## Common mistakes

- Ignoring the source resistance of the sensor when choosing a meter or ADC input.
- Quoting ADC resolution as measurement accuracy.
- Forgetting that the reference voltage sets the scale, so its drift appears directly in every reading.
- Using a divider whose output range covers only a small part of the ADC range, which wastes resolution.

## Worked example

**Problem.** You must read an electrode with source resistance 1 MΩ with a loading error below 0.1%. What minimum input resistance is needed?

**Step 1.** Error = R_s / (R_s + R_in) < 0.001.

**Step 2.** R_in > R_s (1 − 0.001)/0.001 ≈ 999 R_s ≈ 999 MΩ, about 1 GΩ.

**Step 3.** A general-purpose 10 MΩ input is a hundred times too low. An electrometer-grade buffer amplifier is needed, and its input bias current must also be small so that it does not drive a voltage across R_s.

## Limits of this lesson

Component values are synthetic. The analysis is for DC; at higher frequencies, cable and input capacitance add their own loading.

# Kirchhoff balances, Thevenin models and source loading

## Learning objectives

1. Apply node-current and loop-voltage balances with declared reference directions.
2. Calculate a resistive Thevenin equivalent and finite-input attenuation.
3. Distinguish delivered power, calibrated voltage and the limits of an equivalent source model.

## Currents need a reference direction

Kirchhoff's current law expresses charge conservation at a lumped node when charge accumulation is assigned consistently to modeled elements. Choose reference directions before writing currents. A negative solution means actual current is opposite the chosen arrow; it does not invalidate conservation. With ideal resistors, a branch current can be written as its reference voltage difference divided by resistance.

For a synthetic source with open-circuit voltage 3.0 V and series resistance 200 kΩ, a 1.0 MΩ input draws 2.5 µA. Its voltage is 2.5 V, while the source resistance drops 0.5 V. The input load changes the circuit state; a voltmeter with finite resistance cannot be assumed to reveal the unloaded voltage simply because it reports many digits.

The input's absorbed power is V²/R=6.25 µW. The source resistance dissipates another 1.25 µW, and the ideal 3 V source delivers 7.5 µW. This power ledger checks the current and voltage balance independently. It also distinguishes the load's power from the ideal source's total contribution rather than assigning all dissipation to the measurement input.

## A divider and a node equation

For a separate constructed network, connect a 6.0 V ideal source through R₁=200 kΩ to a node. Connect R₂=100 kΩ from that node to the reference return. Without an added load, the node voltage is 2.0 V. The original text connection map below describes topology, not physical wire placement or an equipment procedure.

```text
6 V source -- R1 -- node -- R2 -- return
                    |
                    RL
                    |
                  return
```

Description: R1 connects the ideal source's positive node to the output node. R2 connects the output node to return. An optional RL also connects output to return, in parallel with R2. Source voltage is defined relative to that same return. Line lengths are schematic; no resistor shape or spatial distance is a physical value.

With RL=100 kΩ present, current law is (6−V)/200000=V/100000+V/100000. Solving gives V=1.2 V. The extra branch changes current through R₁ and the voltage at the original R₂. Computing the original divider first and treating its output as an ideal source would miss that feedback of load current into the upstream voltage drop.

## Thevenin is a port description

For this linear resistive network, the open-circuit output voltage is V_th=2.0 V. To find output resistance with the independent ideal voltage source suppressed, replace that source by a short in the mathematical network. R₁ and R₂ then appear in parallel from the port, giving R_th=66.6667 kΩ. Their series sum would describe a different connection.

The equivalent predicts V_load=V_th R_load/(R_th+R_load). At 100 kΩ, this is 1.2 V, matching the node equation. A short-circuit current would be V_th/R_th=30 µA in this ideal model. These terminal predictions do not claim that internal currents or temperatures are identical in every physical realization of the equivalent.

Suppressing an independent source is a calculation step, not an instruction to alter real apparatus. Dependent sources require a different treatment, generally including a test source to determine port resistance. Nonlinear or time-dependent networks may need a local or frequency-dependent equivalent instead of one constant real resistance. State the domain in which the port model is valid.

## Loading can resemble a source change

The preserved course case asks why a high-impedance electrode signal shrinks when a digitizer is attached. A finite input and nonzero source impedance can explain attenuation without a change in the underlying generator. That is a candidate electrical model, not proof that every observed biological signal loss has that cause. The source itself can change, and reactive electrode behavior can require more than a DC divider.

Within the stated resistive model, increasing input resistance reduces loading. A known dummy source with controlled impedance can test a predicted attenuation independently of an actual biological generator. The forthcoming lab supplies mathematical equivalents of such independent information. It does not prescribe electrode attachment, stimulation, human measurement or a real hardware modification.

A reporting gain calibration also differs from a loading correction. An instrument can correctly report the loaded node voltage while that node is lower than the open-circuit source. Multiplying by a reporting-gain factor cannot by itself recover the source unless its impedance and input model are known. Keep the physical circuit transfer and the reporting transformation separate.

## Worked example

For the 3 V series source, use total resistance 1.2 MΩ to get 2.5 µA, then find load voltage and both resistor powers. For the separate 6 V divider, solve the open-circuit node first and calculate the port resistance after suppressing the ideal source. Add the 100 kΩ load using either KCL or the Thevenin divider and verify both yield 1.2 V.

## Common mistakes

Do not assume every voltage reading is open-circuit voltage. Do not suppress a dependent source as though it were independent, add parallel resistances directly or interpret a negative reference current as broken conservation. Calibrated reporting does not eliminate physical loading automatically.

## Limits of this lesson

All networks, voltages and resistances are synthetic and idealized. The text connection map includes a verbal description but no assistive-technology review. No human-subject procedure or device validation is supplied. Original instruction has substantial AI assistance; qualified review and measured workload remain absent. The package stays partial, unreviewed and formative-only.

# Differential signals, common mode and interface imbalance

## Learning objectives

1. Decompose two input voltages into differential and common-mode components.
2. Calculate a declared rejection ratio and selected interface-imbalance error.
3. Check input ranges and distinguish topology choice from a validated recording model.

## Two voltages contain two comparisons

Define differential voltage v_d=v_p−v_m and common-mode voltage v_c=(v_p+v_m)/2 relative to a stated circuit return. Then v_p=v_c+v_d/2 and v_m=v_c−v_d/2. Swapping the input labels reverses differential voltage while leaving common mode unchanged. A pair's difference does not describe how far either terminal lies from the amplifier's reference.

For synthetic inputs v_p=0.502 V and v_m=0.498 V, v_d=4 mV and v_c=0.500 V. A small differential signal can coexist with a much larger shared level. The preserved prototype suggests a differential front end for such a situation; the following calculation makes its required assumptions explicit rather than treating the topology name as a complete solution.

Stipulate a linear transfer V_out=b+A_dv_d+A_cv_c with b=0.020 V, A_d=100 and A_c=0.010. At these inputs the differential contribution is 0.400 V, the common-mode contribution 0.005 V and total output 0.425 V. The offset, differential signal and common-mode leakage are separate terms. Subtracting a constant offset cannot remove a common-mode term that changes with input.

## Rejection ratios need compatible quantities

For nonzero A_c, amplitude common-mode rejection ratio is |A_d/A_c|. Its decibel value uses 20log₁₀ of that amplitude ratio. The stipulated ratio is 10000, or 80 dB. The 0.5 V common-mode level therefore produces an input-referred equivalent error of A_cv_c/A_d=50 µV. Rejection is finite, and its usefulness depends on the shared signal's magnitude.

An infinite ideal rejection ratio means A_c=0 in a selected model. A real datasheet value can depend on frequency, source impedance, operating point and external resistor matching. A quoted DC ratio alone does not establish rejection of every interference component. The Texas Instruments specification reference linked in the preceding lesson separates common-mode range and rejection; they answer different questions.

## Resistor matching can create leakage

For a selected ideal four-resistor difference-amplifier model, write output as av_p−bv_m. If the inverting ratio is k₁ and the non-inverting divider ratio is k₂, coefficients can be a=(1+k₁)k₂/(1+k₂) and b=k₁ under the stated topology. Equal ratios k₁=k₂ cancel the common-mode coefficient a−b. Unequal ratios leave a residual even with an ideal active gain element.

For a separate constructed example k₁=10 and k₂=10.1, a≈10.009009 while b=10. Thus common-mode coefficient is about 0.009009 and differential coefficient is (a+b)/2≈10.004505. This example is independent of the earlier A_d=100 model. Its purpose is to show why external network mismatch can limit rejection rather than to assign a universal mismatch value to a real instrument.

Using tolerance percentages alone as a measured mismatch can also mislead. Correlated resistor tracking, absolute tolerance and temperature changes are different quantities. A worst-case bound requires a stated combination rule, while an uncertainty estimate requires a covariance model. Neither follows automatically from one nominal resistor value or the word precision.

## Bias currents interact with the interface

Consider another isolated contribution: both inputs draw 5 nA into the amplifier, with source resistances R_p=200 kΩ and R_m=100 kΩ. Their terminal shifts are −I_bR_p and −I_bR_m. Differential error is therefore −I_b(R_p−R_m)=−0.50 mV, producing −50 mV output at declared A_d=100 if the linear model remains valid.

Equal bias currents do not guarantee zero differential error when source resistances differ. Conversely, equal resistances do not guarantee cancellation if currents differ. The interface can be reactive or time dependent, so these DC resistances are restricted equivalents. A slow change in interface voltage, input current or return path can create baseline behavior that is distinct from output clipping.

The model requires a return path for input bias currents. Assuming an indefinitely floating input stays at a fixed potential despite nonzero bias current is inconsistent with charge accumulation. A capacitor-only interface can charge over time. Adding a real return path changes loading and noise as well as baseline behavior, so a full design comparison needs all those effects, not one isolated correction.

## Input and output ranges are separate gates

Suppose both input terminals must remain within −1.5 to +1.5 V, while output must remain within −1 to +1 V. The earlier 0.502/0.498 V pair and 0.425 V output fit those stipulated ranges. But two inputs near 2 V can violate the input range even with nearly zero difference and a predicted small output from the algebraic transfer.

An internal stage of a multi-amplifier front end can also saturate before the final output reaches its visible limit. The simplified transfer does not specify internal node headroom. Choosing a differential or instrumentation topology is therefore a starting analytical choice, not proof that input common mode, bias returns, bandwidth and output swing are all suitable.

## Worked example

Recover v_d=4 mV and v_c=0.5 V from the two supplied terminals, calculate the three output terms and obtain 0.425 V. Convert the amplitude rejection ratio to 80 dB. For the separate bias-current model, calculate both source drops before subtracting them. Finally check both terminal ranges and output range rather than only the differential amplitude.

## Common mistakes

Do not substitute common-mode magnitude for differential signal, use 10log for an amplitude ratio or assume equal bias currents cancel through unequal impedances. Do not confuse rejection with allowed input range. A suitable topology label does not uniquely identify or validate a real electrode interface.

## Limits of this lesson

All inputs, gains, currents, resistances and ranges are synthetic. No patient connection, electrode preparation or hardware modification is prescribed. The scalar transfer and isolated error contributions are conditional models. Original instruction has substantial AI assistance. Qualified review and measured workload remain absent; the course stays partial, unreviewed and formative-only.

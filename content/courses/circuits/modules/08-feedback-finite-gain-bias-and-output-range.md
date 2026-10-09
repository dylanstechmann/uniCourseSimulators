# Feedback, finite gain, bias and output range

## Learning objectives

1. Derive closed-loop response from a finite open-loop amplifier model.
2. Calculate selected bias-current and input-error contributions with consistent signs.
3. Check linear output and input-range assumptions before applying virtual-short reasoning.

## The virtual short is a conclusion

An ideal operational-amplifier approximation often uses nearly equal input voltages under negative feedback. That is a consequence of a sufficiently large gain and a valid linear operating state, not a physical wire connecting the two inputs. Positive feedback, output saturation or an invalid input range can defeat that approximation. Zero ideal input current and equal input voltage are separate model assumptions.

Construct a synthetic non-inverting amplifier. Its positive input receives V_in; its negative input receives a fraction β of output through R_f=90 kΩ from output and R_g=10 kΩ to return. Thus β=R_g/(R_f+R_g)=0.10 if input currents are neglected. A finite static open-loop model is V_out=A(V_in−βV_out), with A=1000.

Solving gives closed-loop gain A/(1+Aβ)=1000/101≈9.900990. The infinite-gain limit would be 1/β=10. At V_in=50 mV, finite-model output is approximately 495.049505 mV. The difference between inputs is V_out/A≈0.495050 mV, small but not zero. These numbers define a teaching model rather than a particular amplifier's measured specifications.

The [Texas Instruments specification guide](https://www.ti.com/lit/an/sloa011b/sloa011b.pdf) is a link-only reference for distinguishing input current, input range, output swing and finite gain. No manufacturer circuit drawing, table or example was imported. The following connection map and values are original, and the named document is not a component recommendation or validation.

```text
input voltage ---> positive input
output -- Rf -- negative input -- Rg -- return
```

Description: the positive input receives the supplied voltage. A divider from output through Rf to the negative input and then Rg to return supplies negative feedback. The amplifier output responds to positive minus negative input under the stated model. The text map shows connections rather than actual wiring, dimensions or device pin numbers.

## Finite feedback error

The gain error relative to the ideal value is about 0.9901% in this selected example. Increasing A reduces it if β and the linear model remain valid. A can vary with frequency, so a large DC gain does not establish the same closed-loop error or stability over an arbitrary bandwidth. Dynamic poles and phase margin would require an additional model.

Similarly, the negative input is approximately at the positive-input voltage only while feedback can generate the necessary output. The equal-input shortcut must not be applied first and then used to prove an output already beyond the allowed range. Solve the requested operating point, check the assumptions and replace the linear model if the checks fail.

## Bias current sees source resistance

Now isolate a positive-input bias contribution. Stipulate a current of 10 nA flowing into that input from a source resistance 200 kΩ, with other bias contributions temporarily excluded. The source-side drop lowers the actual positive-input voltage by I_bR_s=2 mV. Its signed input shift is −2 mV, and its finite closed-loop output contribution is approximately −19.80198 mV.

That sign follows the declared current direction. A different device can have currents of different polarity or matching behavior, so “bias current adds a positive offset” is not a universal rule. In the full circuit, negative-input bias current also interacts with the feedback-network resistance. Input offset voltage and bias-current-induced voltage are distinct contributions and should not be counted twice.

If equal currents enter both inputs and the effective resistances seen by those inputs are matched, their effects can partly cancel in an appropriate model. The feedback-side resistance here is R_f parallel R_g=9 kΩ, far below the example's 200 kΩ source resistance. Matching is a conditional analytical result, not permission to assume a high-impedance sensor already has that balance.

## Check ranges separately

Stipulate a phenomenological output limit from −0.80 to +0.80 V, while both input terminals must remain between −0.20 and +0.20 V for the selected model. With no offsets or bias errors, maximum positive input compatible with the finite linear output bound is 0.80/(1000/101)=0.0808 V, or 80.8 mV. The input-range condition also needs checking at that point.

At a larger positive input, a hard-clamp teaching model might report +0.80 V, but the original linear relation no longer describes the saturated state exactly. Real recovery, output current limits, slew behavior and supply conditions require specifications not supplied by a static clamp. A clipping plateau therefore does not establish the amplifier's unclipped gain from plateau slope.

## Worked example

Use the divider to find β=0.10, then solve the finite open-loop equation before substituting V_in. Compare finite gain with ideal gain and calculate the residual input difference. Isolate the declared positive-input bias drop with its direction, then keep it distinct from offset voltage and the other input's bias effect. Finally check output and both input ranges before relying on linear feedback.

## Common mistakes

Do not call a virtual short a conductive connection, use equal-input reasoning in saturation or assume bias-current polarity without a convention. Do not ignore source resistance, confuse input offset with current-induced error or treat a DC open-loop gain as a complete dynamic amplifier specification.

## Limits of this lesson

All gains, resistances, currents and ranges are synthetic. The original connection map has a verbal description but no assistive-technology review. No actual amplifier, patient connection or hardware procedure is supplied. Original instruction has substantial AI assistance. Qualified review and workload measurement remain absent; the course stays partial, unreviewed and formative-only.

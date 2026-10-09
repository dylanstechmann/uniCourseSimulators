# Filter loading, baseline and recovery

## Learning objectives

1. Calculate selected low-pass and high-pass responses with explicit frequency conventions.
2. Compare buffered transfer multiplication with an unbuffered passive ladder.
3. Distinguish baseline filtering, state recovery and information already lost to clipping.

## A transfer depends on the connections

The preserved first-order lesson describes an RC low-pass. Extend that idea by stating which node is observed and what load it drives. A transfer calculated for an unloaded capacitor node can change when the next stage draws current. Multiplying isolated block responses is valid only when their port assumptions remain compatible, such as an explicitly ideal buffer between them.

For a synthetic ideal low-pass H_L=1/(1+jf/f_L), use cutoff f_L=10 Hz and the exp(jωt) convention with ω=2πf. Its time constant is 1/(2πf_L)≈0.0159155 s. At f=1 Hz its amplitude gain is 1/√1.01≈0.995037 and phase is approximately −5.710593 degrees. Angular frequency and cycles per second must not be interchanged without 2π.

For a separate ideal high-pass H_H=(jf/f_H)/(1+jf/f_H), stipulate f_H=0.10 Hz. Its time constant is approximately 1.591549 s. At 1 Hz, amplitude also is approximately 0.995037 but phase is positive 5.710593 degrees. The two expressions describe different observed nodes and different low-frequency limits despite sharing the phrase first order.

## An ideal buffered band

If an ideal isolating buffer separates these blocks, cascade response is their product. At 1 Hz the gains multiply to 100/101≈0.990099 and phases add to zero for this constructed pair. Zero net phase at one frequency does not imply unit amplitude or a zero-delay waveform at every frequency. A broadband signal must be interpreted through the frequency-dependent response.

At zero frequency the high-pass removes a constant component in the steady limit. At very high frequency the low-pass attenuates rapidly varying components. The resulting selected band can be useful for a stated signal model, but neither cutoff establishes which components are biologically meaningful. An undesired baseline and a desired slow signal can occupy overlapping frequencies.

## A passive ladder gives a counterexample

Now construct two identical passive RC sections without a buffer. Each has series R=1 kΩ, and each observed node has C=10 µF to return. The first section's output drives the second resistor and capacitor directly. Let s=jω. Node-current equations give H=1/[1+3sRC+(sRC)²] for the final node under an ideal input voltage source.

To see the loading term, write node two as V₁=(1+sRC)V₂ from its current balance. The first node then gives V_s=(2+sRC)V₁−V₂. Substitution yields the stated denominator. The coefficient three comes from shared loading; treating the sections as independent would instead yield (1+sRC)² with coefficient two.

At ωRC=1, the unbuffered denominator is 3j, so final amplitude gain is 1/3. Two ideally buffered sections at that same normalized frequency give magnitude 1/2. The difference is an explicit counterexample to blindly multiplying standalone responses. Real buffers have finite bandwidth, noise and output limits, so declaring a buffer ideal is also an assumption needing review.

## Baseline steps and state recovery

For the ideal high-pass driven by a unit voltage step from an initially settled state, output is exp(−t/τ) V after the event. At one τ it is about 0.367879 V; at four τ about 0.018316 V. The final zero response does not mean the step was never present. The circuit stores an initial-condition change and then approaches a new state.

The step's initial response also differs from steady DC gain. Substituting zero frequency into a steady transfer and predicting zero voltage at every instant after a step would ignore the initial transient. A first-order model can check recovery time under stated state and linearity conditions, while saturation can create an entirely different recovery history.

## Filtering cannot undo earlier clipping

Suppose an upstream amplifier has already limited a signal to a rail. A later linear filter can smooth the plateau or change its apparent duration, but the original unclipped amplitude is no longer uniquely represented in the recorded signal. Many different inputs can produce the same clipped output. A digital high-pass cannot recover that lost information merely by making the baseline look flatter.

The preserved channel case combines clipping during movement and drifting at rest. These observations can require distinct explanations. Gain or common-mode range may cause one, while interface polarization, bias return or filter state may contribute to another. A staged synthetic control should vary one informative input or model condition at a time rather than declare every slow trace a biological change.

The new lab uses a separately stipulated exponential offset with time constant 0.50 s. That is an observation-model construction, not the same as this high-pass cutoff's 1.591549 s. Similar-looking exponentials can arise from different models. Their fitted time constants need an independently justified circuit or interface interpretation before assigning a cause.

## Worked example

Calculate both isolated first-order responses at 1 Hz and multiply only under the declared ideal-buffer condition. Derive the passive ladder from its two node equations and compare 1/3 with 1/2 at ωRC=1. For the independent high-pass step, retain the initial transient and evaluate its remaining fraction. Keep these linear calculations separate from a saturated upstream stage.

## Common mistakes

Do not confuse frequency with angular frequency, multiply loaded blocks as though isolated or use steady DC gain as an initial-step prediction. Do not treat a flatter trace as recovered clipped information, or identify a fitted exponential with a unique biological or circuit process.

## Limits of this lesson

All networks, cutoff values and steps are synthetic. Ideal buffers and linear RC models do not validate a real recording filter or recovery specification. No hardware or subject procedure is given. Original instruction has substantial AI assistance. Accessibility, qualified review and measured workload remain absent; the package stays partial, unreviewed and formative-only.

# Sampling, quantization and acquisition settling

## Learning objectives

1. Calculate a declared ideal ADC code, reconstruction and quantization error.
2. Check a sample-capacitor settling model against a specified error target.
3. Distinguish alias ambiguity, quantization assumptions and practical sampling margins.

## Declare the converter map

A bit count does not uniquely define every converter's transition conventions. Stipulate an ideal unipolar 10-bit ADC spanning 0≤V<2.0 V with 1024 equal bins. Bin width Δ=2.0/1024=1.953125 mV. For this exercise code is floor(V/Δ), and reconstructed voltage is the corresponding bin center (code+0.5)Δ. The endpoint V=2.0 is outside the declared range.

For V=0.503 V, floor(0.503/Δ)=257. Bin-center reconstruction is approximately 0.502930 V, and reconstruction minus actual input is −70.3125 µV using the exact bin-center value. The sign convention matters: defining error as input minus reconstruction would reverse it. A different rounding or endpoint rule would need a separately declared map.

The [Analog Devices ADC chapter](https://wiki.analog.com/university/courses/electronics/text/chapter-20) is a link-only reference for sampling, finite codes and nonideal converter distinctions. No source transfer drawing, table or example was imported. The present bin convention and numerical parameters are original constructions rather than a particular device's specification.

## What the half-bin bound establishes

For interior values under this exact bin-center reconstruction, quantization error magnitude is at most Δ/2, or 0.9765625 mV. That bound describes the selected quantizer, not total measurement accuracy. Reference error, gain, offset, differential nonlinearity, noise and acquisition effects can contribute additional errors. A 10-bit label alone does not remove them.

An error-variance model Δ²/12 assumes a sufficiently uniform distribution of quantization error over a bin and the needed lack of correlation for its intended use. A constant DC input can repeatedly produce the same code and the same error. A coherent periodic input can create structured error. Neither becomes independent white quantization noise merely because the converter is ideal.

More bits reduce nominal bin width at the same span, but they do not automatically improve reference stability, linearity or settling. Similarly, averaging repeated identical codes cannot reconstruct every lost sub-bin input. Additional information or a justified dither/measurement model would be needed, and the present lesson supplies no physical dither implementation.

## The acquisition interval has dynamics

Consider a separate synthetic input acquisition model: a 100 kΩ source charges a 10 pF sample capacitor through the stated effective resistance. Time constant is 1.0 µs. Ignore additional switch resistance, charge injection and source dynamics for this limited calculation. Following a full-span 2.0 V step, remaining voltage error is 2.0exp(−t/τ) V.

To reduce that error to at most half a bin of the stipulated 10-bit converter, require exp(−t/τ)≤1/2048. Thus t≥τln2048≈7.624619 µs. A short conversion period is not automatically an adequate acquisition period; the time available to settle can be a separate part of a converter cycle. The chosen target is a mathematical error budget, not a real device guarantee.

The target also depends on the prior capacitor state. A small channel-to-channel step can settle to the same absolute bound faster than a full-span step. Multiplexed inputs, source impedance changes or a nonlinear driving stage can invalidate the one-resistance/one-capacitance approximation. State the initial difference and the allowed error before quoting a required time.

## Sampling creates equivalence classes

At sampling rate f_s=1000 samples/s, a sinusoid at 1300 Hz can produce the same sampled cosine sequence as one at 300 Hz, because their phase increments differ by 2π per sample. The high-frequency input has folded into the nominal baseband. Observing a 300 Hz component in the samples alone therefore does not uniquely identify the analog source frequency.

Sine phases and folds across a negative frequency require consistent phase signs, but the ambiguity remains. A digital filter after sampling cannot uniquely undo aliasing because the competing analog inputs already have the same sequence. The analog input model and pre-sampling attenuation or other known constraints must supply distinguishing information.

## The Nyquist boundary is not a margin

An exactly half-rate sine with a suitable phase can give zero at every sample: sin(πn)=0. With another phase it gives alternating values. Arbitrary amplitude and phase are therefore not robustly recovered from this boundary case. For a general signal band extending to a nonzero highest frequency, strict separation above twice that frequency and a realizable transition band matter in practical reasoning.

The preserved prototype's 150 Hz/300 Hz question records the nominal two-times threshold. It is retained as a compact formative algebra check, not a practical alias-free design guarantee for every endpoint phase. The new counterexample and documented limitation make that boundary issue explicit. A stated sample rate also does not establish an ideal brick-wall analog filter or acquisition settling.

## Worked example

Use 1024 equal bins to obtain Δ, take floor for the stated 0.503 V input and reconstruct its bin center. Keep the error sign explicit. For the independent sample capacitor, divide the half-bin target by the full-span step and solve the exponential inequality for 7.624619 µs. Finally compare discrete phase increments for 1300 and 300 Hz and test the exactly half-rate sine.

## Common mistakes

Do not infer a code convention from bit count alone, call half-bin quantization bound total accuracy or assume repeated errors are white noise. Do not confuse conversion rate with acquisition time, treat the exact Nyquist boundary as a robust margin or expect a digital filter to recover aliased analog information uniquely.

## Limits of this lesson

All converter maps, source parameters and signals are synthetic. Ideal bins, one-pole acquisition and exact samples are restricted models, not a real data-acquisition specification. No device operation or subject measurement is supplied. Original instruction has substantial AI assistance. Qualified review and measured workload remain absent; the package stays partial, unreviewed and formative-only.

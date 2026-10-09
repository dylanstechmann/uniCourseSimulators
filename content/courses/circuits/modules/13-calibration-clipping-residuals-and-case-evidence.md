# Calibration, clipping, residuals and case evidence

## Learning objectives

1. Recover gain and offset from supplied unsaturated calibration points.
2. Check asymmetric headroom and a separate exponential baseline model.
3. Use residuals and controlled inputs to distinguish conditional circuit explanations.

## A calibration has a domain

An affine calibration V_out=b+Gv_d can describe a channel only where it remains linear. With a stated output clamp, its observation model becomes clip(b+Gv_d+A_cv_c,V_min,V_max). An endpoint plateau can be compatible with many larger input amplitudes, so the affine inverse cannot be applied to every recorded value indiscriminately.

For a synthetic high-gain channel, stipulate G=100, b=0.10 V, A_c=0.010, output limits −1 to +1 V and valid common-mode range −1.5 to +1.5 V. With v_c=0, independently known differential inputs −5,0,+5 mV produce outputs −0.40,0.10,+0.60 V. All three are unsaturated and identify gain 100 and offset 0.10 V.

Those parameters are declared constructions and public answer examples, not measurements of a particular front end. The common-mode coefficient is a separate supplied term rather than something proved absent by the zero-common-mode calibration. A known differential sweep alone cannot determine common-mode rejection or input-range validity under every operating condition.

## Headroom is not necessarily symmetric

For v_c=0, positive linear headroom reaches v_d=(1−0.10)/100=9 mV. Negative headroom reaches (−1−0.10)/100=−11 mV. The limits differ because of the nonzero offset even though the output rails are symmetric. Using ±10 mV as a symmetric input range would overlook one side's early clipping and understate the other side's available interval.

At +15 mV, the unclipped affine prediction is 1.60 V and the stipulated report is +1 V. Inverting that plateau as though linear gives (1−0.10)/100=9 mV, which does not recover the known 15 mV input. This is lost information, not a calibration precision error that can be corrected by adding more displayed digits.

For a separate low-gain condition G=20 with the same offset and clamp, the ±15 mV sweep remains unsaturated, spanning −0.20 to +0.40 V. That comparison can constrain the source input under the declared stable-source model. It also shows why an informative controlled gain change can distinguish range saturation from a changed generator, without claiming every actual movement artifact has that cause.

## Residuals expose a wrong fit domain

Suppose a linear least-squares fit includes the high-gain channel's full −15,−5,0,+5,+15 mV sweep. The corresponding outputs are −1,−0.4,0.1,0.6,+1 V. Fitting all five as linear gives slope 70 and intercept 0.06 V rather than the unsaturated slope 100 and intercept 0.10. More points have not improved the model because some points violate its domain.

Inspect residuals, declared rails and independent input values instead of reporting only one fit statistic. A straight-line fit can compromise between interior and clipped data while hiding the physical reason for deviations. Conversely, a residual pattern can also come from nonlinear source response, reference error or drift. It suggests a model check rather than uniquely identifying saturation without the accompanying evidence.

## A separate baseline construction

The lab stipulates another condition with zero differential and common-mode inputs but an offset b(t)=0.10+0.30exp(−t/0.50) V. At t=0.50 s it is approximately 0.210364 V. The excess above the final 0.10 V is a fraction exp(−1) of its initial excess. Subtracting the final baseline is necessary before fitting the logarithmic decay.

This exponential is a synthetic observation-model component, not a claim about one actual electrode polarization law. Its 0.50 s parameter is distinct from the preceding filter examples. A smooth baseline decay could arise from interface, bias-return, filter-state or other mechanisms. Independent equivalent-network or dummy-input information would be needed to connect a fitted parameter to a physical cause.

The construction assumes the baseline condition is separate from the steady calibration sweep, so their offsets should not be pooled as though taken under one unchanged state. A real drift during calibration can bias slope and intercept if timing correlates with input. Record which parameters were held fixed and which were deliberately varied when interpreting a comparison.

## Common-mode checks add a constraint

At v_d=0 and common modes −1 and +1 V, the same settled high-gain model produces 0.09 and 0.11 V. Their slope with common mode is 0.010 V/V, and combining it with differential gain 100 gives nominal CMRR 80 dB. A constant baseline cancels in the difference, but the validity of the input common-mode range remains an independent assumption.

A high nominal rejection ratio does not prevent saturation if the actual input range or an internal stage is exceeded. Nor does one common-mode test establish rejection at all frequencies. The new data deliberately isolate selected terms; they do not validate the entire front end. Parameter recovery is conditional on the declared linear and clamp model.

## Evidence for the preserved case

The preserved case asks why a biopotential channel clips during movement and drifts at rest. Keep the two observations distinct. Controlled differential/common-mode inputs, range checks and a separately declared baseline condition can support competing electrical explanations without involving a subject. This course provides mathematical synthetic controls, not a physical test protocol or an electrode-procedure change.

An adequate discussion distinguishes known reference inputs from fitted outputs, checks gain and output range, considers bias return and input common mode, and asks about filter state and recovery. The checklist remains self-assessment; automatically scored choices cannot evaluate a full written diagnosis. Actual interface and biological behavior still require qualified review and independent evidence.

## Worked example

Fit the three unsaturated points to recover G=100 and b=0.10. Compute +9 and −11 mV headroom before interpreting the ±15 mV reports. Compare the five-point compromised fit with interior calibration. For the independent drifting condition, subtract the 0.10 V final baseline and infer the exponential time scale from excess ratios. Use common-mode points to recover the separate leakage coefficient.

## Common mistakes

Do not fit clipping plateaus as linear gain, apply an affine inverse outside its domain or assume headroom is symmetric despite offset. Do not pool drifting and settled states, call a fitted exponential a unique electrode mechanism or treat one nominal rejection ratio as a complete range and bandwidth check.

## Limits of this lesson

All points, gains, clamps, ranges and baseline parameters are synthetic. No apparatus operation, subject connection or electrode protocol is supplied. Original instruction has substantial AI assistance. Accessibility, qualified subject-matter review and measured workload remain absent; the package stays partial, unreviewed and formative-only.

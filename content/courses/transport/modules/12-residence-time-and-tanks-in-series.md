# Well-mixed chambers: residence time, wash-in and washout, and tanks in series

A perfused chamber is the unit in which most culture and sensing experiments happen: a volume of medium that is fed at one flow and drained at the same flow. The first questions about it are about time. How long before a change in the feed reaches the cells? How long before the previous medium is gone? How different is the answer if the chamber is not perfectly mixed? This lesson writes the material balance of a well-mixed chamber, derives the exponential wash-in and washout and the mean residence time, adds first-order consumption by the cells, and compares one well-mixed volume with several in series, which is the standard picture of a chamber between perfect mixing and plug flow. All values are synthetic.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute the mean residence time and the wash-in and washout times of a well-mixed chamber.
2. Include first-order consumption and compute the steady concentration and the effective time constant.
3. Compare a single well-mixed volume with tanks in series and evaluate the assumption of perfect mixing.

## The balance and the residence time

For a chamber of volume V fed at a flow Q with a solute concentration C_in, and assumed perfectly mixed so that the outlet concentration equals the chamber concentration C,

**V dC/dt = Q (C_in − C).**

The ratio **τ = V/Q** is the **mean residence time**. For V = 10 mL and Q = 0.5 mL/min, τ = **20 min**. If the feed switches at t = 0 from no solute to C_in, the chamber concentration rises as

**C/C_in = 1 − e^(−t/τ)** (wash-in),

reaching 63% after one residence time, 86.5% after two and 95% after t = −τ ln 0.05 = 3.0 τ = **59.9 min**. If the feed switches back to zero, the concentration falls as **C/C₀ = e^(−t/τ)** (washout) and drops to 1% after 4.6 τ = **92.1 min**. The residence time is the natural unit of time for the chamber: a change is nearly complete after three residence times and negligible after five.

## Adding consumption

If the cells consume the solute at a rate proportional to its concentration, k C per unit volume with k = 0.05 per minute, the balance becomes V dC/dt = Q (C_in − C) − k V C. The steady concentration is

**C_ss/C_in = 1/(1 + kτ) = 1/(1 + 0.05 × 20) = 0.50,**

and the approach to it has the shorter effective time constant **τ/(1 + kτ) = 10 min**. The product kτ, the ratio of the residence time to the consumption time, says how much the cells deplete the feed. If kτ is much below 1, the chamber behaves as a pure mixing volume; if it is of order 1 or more, the cells control the concentration, and the solute level they see is a fraction of the feed.

## Tanks in series

A real chamber is not perfectly mixed. The classical model of imperfect mixing divides the volume into N equal tanks in series, each of volume V/N, so that the total mean residence time is still τ but the outflow lags more sharply. The response to a step in the feed for N tanks at time t = x τ is 1 − e^(−N x) Σ (N x)^k/k! (the sum over k from 0 to N − 1). For N = 3 at t = τ the concentration has reached **0.577** of the feed value, against 0.632 for a single tank; the time to 95% is **2.10 τ = 42.0 min**, against 3.0 τ = 59.9 min. The relative standard deviation of the residence-time distribution is 1/√N = 0.58. As N grows the response approaches that of plug flow, a pure delay of τ. A chamber with a well-stirred inlet region and a quiescent region behaves like fewer, uneven tanks and has long tails in its washout.

## Common mistakes

- Treating the residence time as the time for a change to complete.
- Applying the perfectly mixed result to a long thin channel, which is closer to plug flow.
- Forgetting consumption when estimating the concentration the cells see.
- Using the washout time of the feed for a solute that also binds the walls or the cells.
- Taking the number of tanks in series as a measured quantity without a tracer experiment.
- Assuming that the outlet concentration equals the concentration at the cells.

## Worked example

**Problem.** A synthetic chamber of 5 mL is fed at 2 mL/min, and the cells consume the solute with k = 0.2 per minute. Find the residence time, the time to wash out to 1%, the steady fraction of the feed concentration, the effective time constant and the step response of 2 equal tanks in series at t = τ.

**Step 1: residence time.** τ = 5/2 = 2.5 min.

**Step 2: washout.** t = −τ ln 0.01 = 4.6 × 2.5 = 11.5 min.

**Step 3: consumption.** kτ = 0.50; C_ss/C_in = 1/(1 + 0.50) = 0.667; the effective time constant is 2.5/1.50 = 1.67 min.

**Step 4: tanks in series.** For N = 2 at t = τ: 1 − e^(−2)(1 + 2) = 0.594.

## Limits of this lesson

All numbers are synthetic. The model assumes perfect mixing (or equal tanks), a constant flow and first-order consumption, and no dead volume, bypass or binding. Real chambers need a tracer experiment to measure the residence-time distribution. Nothing here is a design or a statement about any real chamber.

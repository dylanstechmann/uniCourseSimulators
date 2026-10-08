# Testing a scientific function: known answers, tolerances, seeds and provenance

A script that produces a number is not a result until you can say why the number is right and how someone else could get it again. Speed in research comes largely from trusting small pieces of code so that you can build on them without rechecking them every time. This lesson shows how to test a scientific function against answers you can work out by hand, how to compare floating-point numbers sensibly, how to make a random analysis repeatable, and what to record so that a figure can be traced back to its inputs.

## Learning objectives

By the end of this lesson, you should be able to:

1. Write known-answer tests for a small scientific function, computing the expected values independently.
2. Choose a tolerance and explain why floating-point numbers are compared with a tolerance.
3. Make a stochastic analysis repeatable and record the provenance needed to reproduce a figure.

## A function worth testing

```python
import math

def doubling_time_hours(n_start, n_end, hours):
    """Exponential growth: time for the population to double."""
    if n_start <= 0 or n_end <= n_start or hours <= 0:
        raise ValueError("need 0 < n_start < n_end and hours > 0")
    return hours * math.log(2) / math.log(n_end / n_start)
```

The function does one thing, takes explicit inputs, returns a value and raises an error on inputs that make no sense. That makes it testable: nothing depends on hidden state, and each behavior can be checked on its own.

## Known-answer tests

Pick inputs whose answers you can derive without running the code.

- Growth from 1 to 2 over 10 hours is one doubling, so the doubling time is 10 hours.
- Growth from 1 to 4 over 10 hours is two doublings, so it is 5 hours (the function returns 5.0).
- Inputs that break the rules, such as a population that shrinks or zero hours, must raise `ValueError`, not return a number.

Add **invariants**, properties that must hold for any valid input: a larger final count over the same time must give a shorter doubling time; multiplying both counts by a constant must not change the answer, because only the ratio matters; and the units are consistent because the result is in the units of `hours`. Invariants catch mistakes that a handful of fixed examples miss.

Compute expected values by a method that is independent of the code: by hand, with a different formula, or with a published value. A test whose expected value is produced by running the same function proves only that the code is deterministic.

## Floating-point numbers and tolerances

Computers store most real numbers approximately. In Python, `0.1 + 0.2` is `0.30000000000000004`, which differs from `0.3` by 5.55e-17. Comparing computed floats with `==` fails for reasons that have nothing to do with correctness. Compare with a tolerance, for example `math.isclose(a, b, rel_tol=1e-9)`, or `assertAlmostEqual`. Choose the tolerance from the problem: a tolerance of 1e-9 relative is about right for a closed-form formula, while a numerical integrator has a method error that you must estimate and allow for. Tolerances that are too tight make tests fail on a different machine; tolerances that are too loose let real bugs through. A test should also use **relative** tolerance for numbers that span orders of magnitude.

## Randomness and reproducibility

Many analyses use random numbers: bootstrap intervals, simulations, train-test splits. Make them repeatable by creating a generator with an explicit seed (for example `numpy.random.default_rng(12345)`), passing it into the functions that need randomness and recording the seed with the result. A test with a fixed seed can check an exact output. A separate test can check a statistical property over many seeds, for example that a 95% bootstrap interval covers the true value about 95% of the time in simulated data, which also guards against a seed that happens to work.

## Provenance: tracing a figure to its inputs

A figure that cannot be traced is hard to trust, including by its author a year later. Record with each result: a **hash** (for example SHA-256) of every input file, so a changed file is detected; the parameters and the random seed; the versions of the language and key libraries; and the code revision. Store these in a small text file next to the output. A useful final check is a clean rerun: delete the outputs, run the pipeline from the raw inputs on another machine or in a fresh environment, and confirm that the numbers match within the stated tolerance.

## Worked example

The populations and times are synthetic teaching values. `doubling_time_hours(1e5, 8e5, 30)` has three doublings in 30 hours, so the answer is 10 hours; the code returns 10.0. For the culture that grew from 2.0×10⁵ to 1.28×10⁶ cells in 24 hours the fold change is 6.4, log base 2 of 6.4 is 2.678, and the doubling time is 24 / 2.678 = 8.96 hours. A test for the second case would use `math.isclose(result, 8.9617, rel_tol=1e-4)`, with the expected value derived separately from the log-base-2 form.

## Limits of this lesson

The code is a short illustration, not a complete test suite, and the example growth model assumes exponential growth throughout. The lesson does not cover continuous integration, packaging or testing of code that reads files or the network.

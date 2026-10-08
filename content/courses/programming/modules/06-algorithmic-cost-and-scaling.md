# How long will it take? Algorithmic cost, scaling and choosing data structures for research code

Research code is usually written once and run on growing data. A script that takes a second on a pilot dataset can take hours on the full one, not because the computer is slow but because the work grows faster than the data. Thinking about cost in terms of how operations scale with input size (big-O notation) predicts this before it happens and points to the change that matters: usually a better algorithm or data structure, not a faster machine. This lesson estimates run times for common patterns with synthetic sizes and a stated assumption about speed.

## Learning objectives

By the end of this lesson, you should be able to:

1. Count the operations of simple loops and express their growth with big-O notation.
2. Estimate run time from an operation count and a stated rate, and predict how it scales when the input grows.
3. Choose data structures and algorithms (hash-based lookup, sorting with binary search, vectorized operations) that change the scaling, and decide when optimization is worth it.

## Counting operations

```python
def close_pairs(points, threshold):
    hits = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            if distance(points[i], points[j]) < threshold:
                hits.append((i, j))
    return hits
```

The inner body runs once for every pair, n(n − 1)/2 times. For n = 10,000 cells in an image, that is 49,995,000 distance computations. This is **O(n²)**: double n and the work roughly quadruples.

**Estimating time.** Assume, as a synthetic planning figure, that the loop body runs 10⁷ times per second in an interpreted language. Then the pairwise loop takes 49,995,000 / 10⁷ ≈ 5.0 s. At n = 100,000 it would take about 100 times longer, roughly 8 minutes. The constant (how fast each operation is) matters, but the exponent dominates as data grow.

## Growth rates to recognize

| Pattern | Growth | Example |
|---|---|---|
| single pass over data | O(n) | sum, mean, filter |
| sort | O(n log n) | ranking genes by p-value |
| binary search in sorted data | O(log n) | find a position in a sorted list |
| all pairs | O(n²) | pairwise distances, naive duplicate check |
| all subsets | O(2ⁿ) | exhaustive feature selection |

## Data structures change the exponent

**Membership tests.** Checking whether an item is in a Python list scans it: O(n) per query, n/2 comparisons on average. Checking 10,000 identifiers against a list of 1,000,000 costs about 10,000 × 1,000,000/2 = 5.0×10⁹ comparisons, about 8 minutes at the assumed rate. A set or dict uses hashing: each lookup is O(1) on average, so the same job is about 10,000 operations, effectively instant. Converting the list to a set once costs O(n) and pays for itself after a handful of queries.

**Sorting plus binary search.** If data are sorted once (O(n log n)), each search takes at most ⌈log₂ n⌉ steps: for 1,000,000 items, 20 steps instead of up to 1,000,000.

**Spatial structures.** For "pairs closer than a threshold", binning points into a grid with cells as large as the threshold means each point is compared only with points in neighboring cells; for evenly spread points this is close to O(n).

**Vectorization.** Libraries such as NumPy execute loops in compiled code. The operation count is the same, but the per-operation cost can drop by one to two orders of magnitude compared with a Python loop. It changes the constant, not the exponent: an O(n²) algorithm vectorized is still O(n²) and can run out of memory building an n × n array.

## When to optimize

Measure first. A profiler shows where time is actually spent, which is often not where it was expected. Optimize the part that dominates, keep the slow, obviously correct version as a test reference (see the testing lesson), and check that the fast version gives the same answers. Readable code that finishes in time is better than fast code that is wrong.

## Common mistakes

- Testing speed on a small sample and assuming linear scaling.
- Using `in` on a large list inside a loop.
- Building an n × n matrix when only nearby pairs are needed.
- Optimizing before profiling, or without a correctness check.

## Worked example

**Problem.** A pipeline deduplicates sample IDs by checking each new ID against a growing list. It takes 2 s for 5,000 IDs. Roughly how long for 50,000, and what fixes it?

**Step 1.** Each check scans the list, so the total work is about n²/2: O(n²).

**Step 2.** Ten times more IDs means about 100 times the work: roughly 200 s.

**Step 3.** Keeping seen IDs in a set makes each check O(1), so 50,000 IDs take about ten times as long as 5,000 under the new code, a fraction of a second. Confirm by timing both versions on the same input and checking that they produce the same output.

## Limits of this lesson

The operation rate is a synthetic planning number; real speed depends on language, hardware, memory access and libraries. Big-O describes growth, not exact times.

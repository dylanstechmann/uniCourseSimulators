# Rank, null space and identifiability: counting the independent information in an experiment

Before asking how well an experiment determines a set of unknowns, ask whether it can determine them at all. Three fluorophores with overlapping spectra, two sensors that read nearly the same thing, a regression with an intercept and a complete set of group indicators: in each, some combinations of the unknowns may leave every measurement unchanged, and then no amount of data separates them. Linear algebra counts this exactly. The rank of the measurement matrix is the number of independent pieces of information, and the null space is the set of changes in the unknowns that the measurements cannot see. This lesson defines both, computes them for a small example, describes all solutions of a consistent system and picks the one of smallest size. All values are synthetic.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute the rank and nullity of a matrix by elimination and relate them through the rank–nullity theorem.
2. Decide whether a system Ax = b is consistent and describe all of its solutions.
3. Identify unknowns that cannot be identified, and compute the minimum-norm solution.

## Rank, column space and null space

For an m × n matrix A, the **column space** is the set of all combinations of its columns, i.e. all b for which Ax = b has a solution. Its dimension is the **rank**. The **null space** is the set of x with Ax = 0, and its dimension is the **nullity**. The **rank–nullity theorem** says that rank + nullity = n, the number of columns. Elimination finds the rank as the number of nonzero rows (pivots) in the reduced form.

**Synthetic mixing matrix:** three channels measure combinations of three unknown amounts,

A = [[1, 2, 3], [2, 4, 6], [1, 1, 2]].

The second row is twice the first, and the third column is the sum of the first two. Elimination (subtract 2 × row 1 from row 2, and row 1 from row 3) gives rows (1, 2, 3), (0, 0, 0), (0, −1, −1): two nonzero rows, so the **rank is 2** and, with n = 3, the **nullity is 1**. A basis for the null space is n = (1, 1, −1), because A n = (1 + 2 − 3, 2 + 4 − 6, 1 + 1 − 2) = (0, 0, 0).

## Consistency and all solutions

Ax = b has a solution only if b lies in the column space. Here every column has its second entry equal to twice its first, so every combination of the columns does too, and every b in the column space has b₂ = 2b₁. For b = (6, 12, 4) the second entry is 12 = 2 × 6, and x = (1, 1, 1) works: A (1, 1, 1) = (6, 12, 4). For b = (6, 11, 4) the second entry is 11, not 2 × 6 = 12, so **no solution exists** and the equations contradict each other.

When a solution x₀ exists and the nullity is positive, there are infinitely many: every x = x₀ + t n gives the same b. With x₀ = (1, 1, 1) and n = (1, 1, −1), the solutions are (1 + t, 1 + t, 1 − t). Setting the third component to zero requires t = 1, giving x = (2, 2, 0). These solutions fit the data equally well; the data cannot say which is right. The unknowns are **not identifiable** individually, though combinations such as x₁ − x₂ and x₁ + x₃ are: they are the same for every t.

## The minimum-norm solution

If a single answer is needed, one natural choice is the solution of smallest length. It is the one orthogonal to the null space. With x₀ = (1, 1, 1) the length is √3 = 1.7321; subtracting the component along n, x = x₀ + t n with t = −(x₀·n)/(n·n) = −1/3, gives **x = (0.6667, 0.6667, 1.3333)** with length **1.6330**. This choice is a convention, not a measurement: it is shrunk toward zero, and reporting it as the amounts is wrong unless the convention is stated.

## Design matrices

The same count applies to regression. A design with an intercept column and one indicator column for each of two groups,

X = [[1, 1, 0], [1, 1, 0], [1, 0, 1], [1, 0, 1]],

has three columns but rank 2, because the intercept equals the sum of the indicators. The coefficients are not identifiable (add c to the intercept and subtract c from both group coefficients and nothing changes). The remedy is to drop one column or to impose a constraint. A fuller version of the same problem appears when two sensors read nearly the same signal: the matrix then has full rank on paper but is nearly rank deficient, which the later lessons on conditioning quantify.

## Common mistakes

- Counting the rank from the number of rows or columns instead of the number of independent ones.
- Concluding that a system has no solution because it has many, or the reverse.
- Reporting one member of a solution family as if it were the measured value.
- Forgetting that rank–nullity counts columns (unknowns), not rows (equations).
- Using the full set of dummy variables together with an intercept.
- Treating a nearly dependent column as exactly independent because the software did not complain.

## Worked example

**Problem.** For A = [[1, 2, 1], [2, 4, 2], [3, 6, 3]] find the rank and nullity, decide whether b = (2, 4, 6) is in the column space and describe the solutions.

**Step 1: rank.** Rows 2 and 3 are 2 and 3 times row 1, so there is one pivot: rank **1**, and the nullity is 3 − 1 = **2**.

**Step 2: consistency.** Every column is a multiple of (1, 2, 3), so b must be a multiple of (1, 2, 3); (2, 4, 6) = 2 × (1, 2, 3), so a solution exists, for example x = (2, 0, 0).

**Step 3: all solutions.** The null space is spanned by [−2, 1, 0] and [−1, 0, 1] (for instance (−2, 1, 0): −2 + 2 + 0 = 0 in every row of A), so the solutions are x = (2, 0, 0) + s[−2, 1, 0] + t[−1, 0, 1], a plane of solutions.

## Limits of this lesson

All numbers are synthetic. The lesson treats exact arithmetic on small matrices; with measured data, a matrix is rarely exactly rank deficient, and the practical question is how close it is, which the lessons on singular values and conditioning address.

# Cell-state transitions as a Markov chain: transition matrices, the eigenvalue 1 and how fast a population settles

Cell populations are mixtures of states, such as proliferating and quiescent, stem-like and committed, or healthy and senescent, and cells move between states. If each cell's chance of switching in the next interval depends only on its current state, the population's composition evolves by repeated multiplication by a matrix. Linear algebra then answers two questions directly: what mixture the population settles to, and how fast. This lesson builds a two-state model, finds its stationary distribution as an eigenvector and its convergence rate from the second eigenvalue.

## Learning objectives

By the end of this lesson, you should be able to:

1. Write a transition matrix for a two-state Markov chain and propagate a population distribution forward in time.
2. Compute the stationary distribution as the eigenvector for eigenvalue 1 and interpret it.
3. Use the second eigenvalue to determine how fast the population approaches the stationary distribution and evaluate the model's assumptions.

## The transition matrix

**Synthetic model:** each day, a proliferating cell (state A) becomes quiescent (state B) with probability 0.2, and a quiescent cell re-enters proliferation with probability 0.1. Write the population as a column vector p = [p_A, p_B]ᵀ of fractions. One day later, p′ = Mp with

M = [[1 − 0.2, 0.1], [0.2, 1 − 0.1]] = [[0.8, 0.1], [0.2, 0.9]].

Each column sums to one (every cell goes somewhere), and every entry is non-negative. Starting with all cells proliferating, p₀ = [1, 0]ᵀ: after one day p₁ = [0.80, 0.20]ᵀ, and after two days p₂ = M p₁ = [0.660, 0.340]ᵀ. After n days, pₙ = Mⁿ p₀.

This model ignores division and death; it tracks the fractions in each state, as if counting a constant-size mixture. Adding growth changes the matrix entries but not the method.

## The stationary distribution

A distribution that no longer changes satisfies **Mπ = π**: π is an eigenvector of M with eigenvalue 1. Because columns sum to one, 1 is always an eigenvalue of such a matrix. For two states, balance of flows gives the answer directly: at steady state, the flow A → B equals the flow B → A, so 0.2 π_A = 0.1 π_B. With π_A + π_B = 1:

π_A = 0.1 / (0.2 + 0.1) = 0.3333, π_B = 0.6667.

In the long run one third of cells proliferate, regardless of the starting mixture. Note that individual cells keep switching; only the fractions are stationary. The stationary mix depends only on the ratio of switching probabilities: halving both would give the same π but a slower approach.

## How fast: the second eigenvalue

M has two eigenvalues. One is 1. Since the trace equals the sum of eigenvalues, the other is λ₂ = trace − 1 = 0.8 + 0.9 − 1 = 0.7. Write the starting distribution as π plus a deviation along the second eigenvector; each day multiplies the deviation by λ₂. So the deviation from steady state shrinks by a factor of 0.7 per day, halves every ln 2 / (−ln 0.7) = 1.94 days, and falls below 5% of its starting size after ln 0.05 / ln 0.7 = 8.4 days.

The closer λ₂ is to 1, the slower the approach; if switching were rare in both directions, λ₂ would be close to 1 and a perturbed population would take a long time to return to its normal mix. If |λ₂| were close to zero, the population would reset almost immediately.

## Checking the model

The Markov assumption is that switching depends only on the present state, not on history. Real cells may have memory: a cell that has just become quiescent may be less likely to re-enter the cycle than one quiescent for a week. Such effects can be included by adding states (for example, "recently quiescent" and "long-term quiescent"), which enlarges the matrix. Transition probabilities are estimated from data such as lineage tracking or time-lapse imaging, and different interval lengths give different matrices, so the time step must be stated.

## Common mistakes

- Writing the matrix with rows and columns swapped and then multiplying on the wrong side; with column vectors, columns must sum to one.
- Treating the stationary distribution as the state of an individual cell rather than the population fraction.
- Assuming a population at its stationary mix is static; cells still switch.
- Using a matrix estimated from one interval length for another without converting.

## Worked example

**Problem.** A treatment (synthetic) doubles the re-entry probability to 0.2 per day while leaving exit at 0.2. What are the new stationary distribution and convergence factor?

**Step 1.** π_A = 0.2 / (0.2 + 0.2) = 0.5.

**Step 2.** λ₂ = 1 − 0.2 − 0.2 = 0.6, so deviations shrink by 0.6 per day.

**Step 3.** The population would settle to half proliferating, and faster than before (half-time ln 2 / −ln 0.6 = 1.36 days). The model predicts composition; whether the cells in each state are healthy is outside it.

## Limits of this lesson

All probabilities are synthetic. The model ignores division, death and memory, and it does not describe any specific cell type.

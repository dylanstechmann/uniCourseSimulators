# Oscillatory rheology: storage and loss moduli of a viscoelastic gel

The package's case asks for a material characterization before a cell result is interpreted: the modulus and the viscoelastic relaxation of the gel at culture conditions. The standard way to measure both is oscillatory rheology. A small sinusoidal strain is applied to a sample at a chosen frequency, and the stress that comes back is resolved into a part in phase with the strain, which measures stored elastic energy, and a part a quarter of a cycle ahead, which measures energy lost. Repeating the test across frequencies gives the relaxation behavior of the gel without a long hold, and it shows at once whether a single "stiffness" is a fair summary. This lesson defines the storage and loss moduli, computes them for the Maxwell element and the standard linear solid used in the indentation lesson, and states what must be reported for a gel's modulus to be comparable. All values are synthetic.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute the storage modulus, loss modulus, loss tangent and phase angle of a Maxwell element at a given frequency.
2. Identify the crossover frequency and relate the moduli to the relaxation time of a gel.
3. Evaluate what an oscillatory measurement shows and what must be reported with a gel modulus for a cell experiment.

## Storage and loss moduli

Apply a strain ε(t) = ε₀ sin ωt. A linear viscoelastic material returns a stress σ(t) = σ₀ sin(ωt + δ). Splitting the stress into an in-phase and an out-of-phase part defines

**G′ = (σ₀/ε₀) cos δ** (the storage modulus) and **G″ = (σ₀/ε₀) sin δ** (the loss modulus),

with the loss tangent tan δ = G″/G′ and the magnitude |G*| = √(G′² + G″²) = σ₀/ε₀. A purely elastic solid has δ = 0 and a purely viscous liquid has δ = 90°. The measurement is valid only in the linear range, with a strain small enough that the moduli do not depend on its amplitude; a strain sweep at fixed frequency checks that first.

## The Maxwell element

For a Maxwell element (a spring G in series with a dashpot, relaxation time τ = η/G), the moduli at angular frequency ω are

**G′ = G (ωτ)² / (1 + (ωτ)²), G″ = G (ωτ) / (1 + (ωτ)²).**

**Synthetic example:** G = 1000 Pa and τ = 2 s, the element of the indentation lesson.

| ω (rad/s) | ωτ | G′ (Pa) | G″ (Pa) | tan δ |
|---:|---:|---:|---:|---:|
| 0.05 | 0.1 | 9.9 | 99.0 | 10.00 |
| 0.5 | 1 | 500.0 | 500.0 | 1.00 |
| 5 | 10 | 990.1 | 99.0 | 0.10 |

At low frequency (ωτ = 0.1) the element is mostly viscous: G″ is ten times G′ and the phase angle is 84.3°. At high frequency (ωτ = 10) it is mostly elastic: G′ = 990 Pa, close to G, and tan δ = **0.10**. The two moduli cross at **ω = 1/τ = 0.5 rad/s**, where each equals G/2 = 500 Pa and δ = 45°; there |G*| = 707.1 Pa. The crossover frequency is the simplest read-out of a relaxation time. A gel that is slow to relax has its crossover at a low frequency, and a gel that relaxes quickly crosses over at a high one.

## Relating the shear modulus to Young's modulus

Rheometers report the shear modulus, while indentation and compression report Young's modulus. For an isotropic, nearly incompressible material (ν ≈ 0.5) the two are related by **E = 2(1 + ν) G = 3G**, so G = 1000 Pa corresponds to E = **3000 Pa**. A modulus quoted without saying whether it is G or E, at which frequency and strain, and at which temperature and in which medium, cannot be compared with another.

## Why a cell experiment needs more than one number

Cells apply forces over seconds to hours, so the relevant moduli are those at the frequencies and times that correspond to their activity, and a gel with the same G′ at 1 rad/s but a different loss tangent can relax stress faster, so that the cell feels less sustained resistance. The standard linear solid used for cells has G′ rising from the equilibrium modulus G₁ = 400 Pa at low frequency to G₁ + G₂ = 1200 Pa at high frequency; at ω = 0.5 rad/s it is G′ = 800 Pa with G″ = 400 Pa. A redesigned experiment that varies the crosslinker therefore has to report G′ and G″ across a range of frequencies, in the culture medium and at 37 °C, with the gel swollen to equilibrium, because stiffness measured on a dry or unswollen gel is not the stiffness the cells meet.

## Common mistakes

- Reporting G′ at one frequency as "the stiffness" without G″ or the frequency.
- Measuring outside the linear range.
- Treating G and E as the same quantity.
- Measuring a gel before it has swollen to equilibrium, or in air instead of medium.
- Reading a crossover as a measurement of stiffness instead of a time scale.
- Ignoring that different gels can match in G′ and differ in tan δ.

## Worked example

**Problem.** A synthetic gel behaves as a standard linear solid with G₁ = 400 Pa, G₂ = 800 Pa and τ = 2 s. Find G′ and G″ at ω = 0.1 and 5 rad/s, and the low- and high-frequency limits of G′.

**Step 1: ω = 0.1.** ωτ = 0.2: G′ = 400 + 800 × 0.04/1.04 = 430.8 Pa; G″ = 800 × 0.2/1.04 = 153.8 Pa.

**Step 2: ω = 5.** ωτ = 10: G′ = 1192.1 Pa; G″ = 79.2 Pa.

**Step 3: limits.** G′ tends to G₁ = 400 Pa at low frequency and to G₁ + G₂ = 1200 Pa at high frequency.

**Step 4: reading the result.** The gel appears about three times stiffer at high frequency than at low frequency, the same factor as in the indentation lesson, so a single value of "stiffness" would depend on the test.

## Limits of this lesson

All numbers are synthetic. The Maxwell element and the standard linear solid are models with one relaxation time; real hydrogels and cells show distributions of times and nonlinear behavior at larger strains. Nothing here is a measurement of any real gel or cell.

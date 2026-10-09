# Reversible and sequential kinetics

## Learning objectives

1. Calculate relaxation toward equilibrium in a closed reversible first-order system.
2. Resolve directional constants using relaxation and independent equilibrium composition.
3. Compare a sequential intermediate transient with a simple irreversible disappearance model.

## Disappearance need not reach zero

The irreversible first-order form A(t)=A₀exp(−kt) assumes the modeled A disappears into products without a reverse contribution. A closed reversible A⇌B system instead has dA/dt=−k_fA+k_rB and conserved total C=A+B. Substituting B=C−A gives dA/dt=−(k_f+k_r)(A−A_eq), with A_eq=k_rC/(k_f+k_r). The displacement from equilibrium decays exponentially even though A itself approaches a nonzero amount.

Stipulate k_f=0.048 min⁻¹, k_r=0.012 min⁻¹ and total C=1.0 mM. The relaxation constant is λ=0.060 min⁻¹ and equilibrium A is 0.20 mM. Starting with A₀=1.0 mM and B₀=0 gives A(t)=0.20+0.80exp(−0.060t), with t in minutes. At 20 min, A≈0.440955 mM and B≈0.559045 mM. Their sum remains the stipulated total.

Repeating the same reversible model from another initial composition changes the displacement amplitude while preserving the equilibrium value and relaxation constant. Starting below equilibrium makes A rise rather than fall. Thus the sign of the initial change is a useful check on the conserved-total equation, not evidence that the constants have changed.

## Which half-life?

The half-life of displacement A−A_eq is ln 2/λ≈11.552453 min. At that time, A=0.60 mM, not 0.50 mM. The time for A itself to fall to half its initial value solves 0.50=0.20+0.80exp(−0.060t), giving approximately 16.347154 min. These are different questions despite using the phrase half-life in casual discussion.

A target below A_eq is never reached in this model from above. A target equal to A_eq is approached asymptotically rather than crossed at a finite time. Always check the target against the equilibrium plateau before taking a logarithm. An invalid or negative logarithm argument is a model-domain warning, not an instruction to ignore the plateau.

## Directional information from two observations

The time dependence determines λ=k_f+k_r if the observation and plateau are known. Independent equilibrium ratio K_c=B_eq/A_eq=k_f/k_r determines how that sum is partitioned. Here K_c=4, so k_r=λ/(1+K_c)=0.012 and k_f=K_cλ/(1+K_c)=0.048 min⁻¹. Forward and reverse equilibrium fluxes both equal 0.0096 mM/min, giving zero net flux while neither microscopic direction has stopped.

The ratio equality assumes a genuinely elementary or effective first-order reversible pair with the stated concentrations and no hidden routes. An equilibrium constant alone supplies no time scale. A relaxation constant alone supplies no unique directional constants unless the equilibrium information or an equivalent constraint is available. Independent measurement matters because a fitted plateau and a signal background can otherwise trade off.

## Observation models

Suppose an instrument reports A plus a common additive background b. Its raw plateau is A_eq+b. Fitting a raw single exponential to zero treats both physical residual A and reporting background as disappearing reactant, generally biasing the inferred rate. A separate blank can constrain b, but subtracting that blank still leaves the genuine A_eq plateau. The virtual lab provides both a reference and independent equilibrium composition precisely to separate these questions.

Transforming ln(A−A_eq) gives a straight line with slope −λ only when the plateau and proportional concentration observation are correctly specified. Close to equilibrium, the displacement is small, so rounding or error becomes large relative to it. A smooth transformed line in constructed data establishes consistency with the construction rather than real noise independence or a uniquely discovered mechanism.

## A sequential alternative

For a separate irreversible chain A→I→P with k₁=0.10 and k₂=0.05 min⁻¹, initial A=1 and I=P=0 in arbitrary concentration units, A=exp(−k₁t). The intermediate is I=k₁/(k₂−k₁)×(exp(−k₁t)−exp(−k₂t)). Its sign is positive because numerator and denominator signs compensate in this ordering. Product is 1−A−I by conservation.

The intermediate reaches its maximum at t_peak=ln(k₂/k₁)/(k₂−k₁)≈13.862944 min. At that time A=0.25, I=0.50 and P=0.25. This transient is neither an equilibrium plateau nor a reporting offset. Observing only A in a sequential chain does not reveal the second constant, because A's own disappearance depends on k₁. Intermediate or product observations supply additional information.

When k₁=k₂, the displayed difference formula has a removable singularity; the limiting intermediate is k₁t exp(−k₁t). A nearly equal pair can also suffer subtractive numerical cancellation. The model equations or an appropriate limiting expression are preferable to blindly evaluating a tiny denominator. The current worked pair is deliberately separated enough to avoid that numerical problem.

## Worked example

Add the reversible constants to obtain λ=0.060 and use the reverse fraction of that sum to find A_eq=0.20. Calculate A at 20 min and recover B from conserved total. Distinguish displacement half-life from time to A=0.50. In the separate chain, differentiate the intermediate expression or set its production equal to removal, find the peak time and check the conserved amounts 0.25+0.50+0.25=1. These calculations describe two different kinetic structures.

## Common mistakes

Do not subtract the reporting background and then assume every remaining plateau is an instrument fault. Do not treat a relaxation constant as the forward constant. Check target domains and conserved totals.

## Limits of this lesson

All trajectories, species and constants here are synthetic and establish no actual reaction mechanism or storage recommendation. Original explanation has substantial AI assistance. The package remains partial, unreviewed and formative-only.

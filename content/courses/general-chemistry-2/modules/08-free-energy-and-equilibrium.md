# Free energy, equilibrium and reaction direction

## Learning objectives

1. Calculate reaction free energy with matching energy units and stated temperature assumptions.
2. Connect a dimensionless equilibrium constant to standard free energy and a current reaction quotient.
3. Distinguish thermodynamic direction, attainable work and kinetic information.

## The state and the question

An enthalpy change alone does not determine reaction direction at fixed temperature and pressure. Entropy also enters the Gibbs state function G=H−TS. Under a common constant-temperature comparison, ΔG=ΔH−TΔS. Identify the system, reaction equation and state conditions before assigning signs. A negative reaction free energy means forward reaction is thermodynamically favored at the current composition under the model; it does not specify how quickly that reaction proceeds.

The [OpenStax free-energy section](https://openstax.org/books/chemistry-2e/pages/16-4-free-energy) provides a link-only reference for the standard relations. The worked values here are independently constructed paper examples, with no copied problem or measured material property. We will use R=8.314 J/(mol·K), a rounded teaching value. Energies are expressed per mole of reaction extent for the exact equation being discussed.

For a hypothetical conversion, stipulate ΔH°=+12.0 kJ/mol and ΔS°=+50.0 J/(mol·K). At 300 K the entropy term is +15.0 kJ/mol, making ΔG°=−3.0 kJ/mol. The enthalpy is positive while the standard free energy is negative. Using 50 directly beside 12 without converting joules to kilojoules would produce a meaningless subtraction despite an apparently clear sign.

## A temperature comparison with limits

If the stipulated enthalpy and entropy are held constant over a teaching interval, their free-energy sign changes at T=ΔH°/ΔS°=240 K. Above that boundary the positive entropy term outweighs the positive enthalpy. Below it, the opposite is true. This is an illustrative constant-parameter comparison, not a measured transition temperature for an actual substance.

Real thermodynamic quantities can change with temperature and phase. A wide-range extrapolation needs heat-capacity and phase information, and the simple crossing can lie outside the stable states assumed by the model. Even when ΔG° becomes negative, the current composition matters. A standard-state calculation is a reference comparison rather than a guarantee about every initial mixture.

## Reference free energy and K

For the same reaction and temperature, ΔG°=−RT ln K, where K is the dimensionless activity-based equilibrium constant. At 300 K, the constructed ΔG°=−3000 J/mol gives K=exp(3000/(8.314×300)), approximately 3.329395. The natural logarithm belongs in this formula. A base-ten logarithm needs the corresponding conversion factor; switching logarithm bases silently changes the answer.

K greater than one favors products in the standard activity comparison, but it does not mean complete conversion. The actual equilibrium amounts also depend on total inventories and reaction stoichiometry. For ideal A⇌B with total concentration 1.0 mol/L, K=[B]/[A]. Therefore equilibrium B concentration is K/(1+K), approximately 0.76902 mol/L, and A supplies the remainder. A positive finite K gives both species positive concentrations in this stipulated closed system.

## Current composition changes direction

Away from equilibrium, reaction free energy is ΔG=ΔG°+RT ln Q=RT ln(Q/K). With the same standard free energy and Q=10, it is approximately +2.743108 kJ/mol. Forward reaction is now disfavored despite negative ΔG°. The mixture is product-rich relative to its equilibrium ratio, so reverse change lowers the modeled free energy. At Q=K the reaction free energy is zero, while microscopic forward and reverse events can continue.

Q uses activities for the written equation. For an ideal concentration approximation, normalize concentration by the chosen standard concentration before constructing activities. Stoichiometric powers follow the balanced equation. Reversing the equation changes ΔG° sign and replaces K by its reciprocal. Multiplying every coefficient by two doubles ΔG° and squares K. Cell potentials, introduced later, do not scale the same way because electron count also changes.

## Work and coupling

In a reversible fixed-temperature, fixed-pressure comparison, negative ΔG bounds the useful non-expansion work the system can deliver. A real operating process can deliver less because of dissipation and other constraints. A favorable free-energy difference does not supply a reaction rate, a device design or a safe operating condition. Thermodynamic favorability and practical attainability require different evidence.

Combining compatible reactions adds their free-energy changes and multiplies their equilibrium constants. Stipulate two linked steps with constants 4 and 0.5 under matching conditions; their net constant is 2. An unfavorable individual step can be included in a favorable overall coupled change, but a mere equation sum does not establish an actual coupling mechanism. Shared intermediates, conservation and conditions still need to be specified.

## Worked example

Convert 50.0 J/(mol·K) to 0.0500 kJ/(mol·K), then calculate 12.0−300×0.0500=−3.0 kJ/mol. Convert back to joules for K=exp(3000/(8.314×300)). For Q=10, add RT ln 10 to the standard free energy and obtain positive current ΔG. For the separate ideal A/B inventory with total 1.0 mol/L, combine K with conservation instead of claiming complete conversion. Finally, combine compatible constants 4 and 0.5 to obtain net K=2.

## Common mistakes

Do not infer reaction speed from a free-energy sign. Do not confuse ΔG° with ΔG at the current mixture. Match logarithm bases, energy units, temperature and reaction coefficients.

## Limits of this lesson

All parameters here are synthetic and constant-parameter extrapolation is deliberately limited. No experiment, energy device, biological intervention or real material recommendation is supplied. Original instruction has substantial AI assistance. The package remains partial, unreviewed and formative-only.

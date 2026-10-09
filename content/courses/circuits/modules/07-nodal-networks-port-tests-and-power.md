# Nodal networks, port tests and power

## Learning objectives

1. Solve a two-node resistive network using consistent current references.
2. Determine a port equivalent with a test-source calculation.
3. Check power conservation and distinguish power matching from voltage measurement.

## Write the topology before the arithmetic

A node equation describes connections, not the visual placement of components on a page. Select one return node as zero potential and assign each other node a voltage. For a resistor between nodes a and b, reference current from a to b is (V_a−V_b)/R. A negative result means current flows opposite that reference; it does not break charge conservation.

Construct a synthetic network: an ideal 6 V source feeds a 1 kΩ resistor into node a. A 2 kΩ resistor connects a to return. A second 1 kΩ connects a to node b, and a third 1 kΩ connects b to return. No additional external load is present initially. All resistances are ideal, constant and positive; the source voltage is defined relative to the same return.

At node b, current law gives (V_a−V_b)/1000=V_b/1000, hence V_b=V_a/2. At a, (6−V_a)/1000=V_a/2000+(V_a−V_b)/1000. Substitution gives V_a=3 V and V_b=1.5 V. Solving the simultaneous equations avoids calling the first resistor and one downstream resistor a simple divider while ignoring the remaining branch.

The [OpenStax Kirchhoff section](https://openstax.org/books/university-physics-volume-2/pages/10-3-kirchhoffs-rules) is a link-only reference for node and loop balances. The network, values and examples here are original constructions. No source problem, diagram or worked solution was copied. Current references can be chosen freely, provided the equations use their signs consistently.

## Power checks reveal missing branches

Source current is (6−3)/1000=3 mA, so the ideal source delivers 18 mW. The first resistor dissipates 9 mW. The a-to-return branch dissipates 3²/2000=4.5 mW, while each resistor in the a-to-b-to-return branch dissipates 1.5²/1000=2.25 mW. Their sum is 18 mW, matching the source contribution.

This ledger is an independent consistency check on the nodal solution. If resistor powers exceeded delivered source power in the declared passive network, investigate omitted sources, units or signs. The passive convention assigns positive absorbed power when current enters an element's positive-voltage terminal. An ideal source delivering power then has negative absorbed power in that same convention.

## A port is a boundary

Treat node b and return as an output port where an extra external load may be attached. Open-circuit port voltage is 1.5 V even though the internal 1 kΩ b-to-return resistor remains present. “Open circuit” means the external port branch is absent, not that every resistor touching b is removed. Changing that internal branch changes the network being characterized.

To find the resistance seen at the port, mathematically suppress the independent ideal voltage source by replacing it with a short. Then a reaches return through 1 kΩ in parallel with 2 kΩ, giving 666.667 Ω. From b, the other route to return has 1 kΩ plus that 666.667 Ω, in parallel with the internal b-to-return 1 kΩ. The result is 625 Ω.

A test voltage of 1 V at b provides another route to this value. With the independent source suppressed, solve a's node equation to obtain V_a=0.4 V. Test current is 1/1000+(1−0.4)/1000=1.6 mA. Port resistance is test voltage divided by current, 625 Ω. This checks the equivalent using actual branch currents rather than relying only on reduction rules.

## Load and source respond together

An added 1 kΩ external load receives V=1.5×1000/(625+1000)=12/13≈0.923077 V. The loaded network's a voltage also changes. The Thevenin model preserves selected terminal voltage/current behavior; it does not claim every internal current equals the equivalent source's current. A direct loaded nodal solution can check the port prediction separately.

For a positive real source resistance and variable positive resistive load, maximum transferred load power occurs at matched resistance. Here that condition gives load voltage 0.75 V and power 0.90 mW. But a voltage-measurement objective usually seeks small loading, with input resistance large relative to source resistance. Maximum-power matching and accurate unloaded-voltage observation are different objectives.

## Dependent sources need a test

Suppress only independent sources when finding an equivalent resistance by the usual method. A dependent source expresses a circuit relation and must remain active in the mathematical port test. Removing it would erase the response being measured. Some active networks can produce negative incremental resistance or require frequency-dependent equivalents, so passive matching assumptions cannot be transferred automatically.

A useful check is to state the port, source type, operating point and linear domain together. A constant Thevenin pair can be valid for this fixed resistive construction while failing for a nonlinear sensor over a wide range. The equivalent's utility comes from its declared boundary and conditions rather than proving one unique physical realization.

## Worked example

Solve b in terms of a, substitute into a's current balance and recover 3 and 1.5 V. Use branch powers to verify 18 mW source delivery. Suppress only the independent source, apply a mathematical 1 V port test and calculate 1.6 mA for 625 Ω. Predict the added 1 kΩ load voltage and distinguish that measurement-loading calculation from maximum-power matching.

## Common mistakes

Do not remove an internal resistor when declaring an external port open, ignore a branch in a divider or suppress dependent sources arbitrarily. Do not treat maximum delivered power as minimum voltage-loading error. Keep current references, power conventions and the chosen port explicit.

## Limits of this lesson

All networks and values are synthetic. Ideal sources and constant resistances establish no real sensor or equipment operating condition. No apparatus procedure is provided. Original instruction has substantial AI assistance. Qualified review, accessibility review and measured workload remain absent; the package stays partial, unreviewed and formative-only.

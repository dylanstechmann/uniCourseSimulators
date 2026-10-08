# Magnetic forces and induction at the bench: flow meters, induced voltages and keeping currents within limits

Magnetic fields act on moving charges, and changing magnetic fields create voltages. Both effects turn up in the laboratory: an electromagnetic flow meter measures how fast a conducting liquid moves by the voltage it generates, a switched magnetic field can induce unwanted voltages in nearby loops of wire, and any instrument that connects to cells or tissue needs its currents kept below a design limit. This lesson works through each with synthetic values.

## Learning objectives

By the end of this lesson, you should be able to:

1. Calculate the magnetic force on a moving charge and the voltage across a conducting fluid flowing through a magnetic field.
2. Apply Faraday's law to compute the voltage induced in a coil by a changing magnetic field, and use Lenz's law to give its direction.
3. Use circuit measurements to design a current limit and to estimate a leakage current, relating both to a stated safety limit.

## The magnetic force on moving charge

A charge q moving with velocity v through a magnetic field B feels the **Lorentz force** F = qv × B, with magnitude qvB when v is perpendicular to B. The force is perpendicular to both, so it changes direction of motion without doing work. A monovalent ion moving at 0.5 m/s across a 1.5 T field feels 1.2×10⁻¹⁹ N, tiny compared with collisions in solution, which is why magnetic fields at these strengths do not appreciably steer ions in water.

## Electromagnetic flow measurement

In a conducting liquid flowing at mean velocity v across a pipe of diameter d in a perpendicular field B, positive and negative ions are pushed toward opposite walls until the resulting electric field balances the magnetic force. The voltage between electrodes on opposite walls is

**ε = B d v.**

**Synthetic flow meter:** B = 0.1 T, d = 10 mm, v = 0.3 m/s gives ε = 0.1 × 0.01 × 0.3 = 0.30 mV. The voltage is proportional to velocity and independent of the liquid's conductivity (as long as it conducts at all), which makes these meters useful for culture medium and other saline solutions. The signal is small, so the amplifier must have high input impedance to avoid loading it (see the sensor-loading lesson in circuits).

## Faraday's law and Lenz's law

The voltage induced in a coil of N turns equals the rate of change of magnetic flux through it:

**ε = −N dΦ/dt,** with Φ = B A for a uniform field perpendicular to a flat loop of area A.

The minus sign is **Lenz's law**: the induced current flows in the direction that opposes the change in flux. A coil of 50 turns and 2 cm² in a field changing at 20 T/s develops ε = 50 × 2×10⁻⁴ × 20 = 0.20 V. Rapidly switched fields, as in some imaging systems, can induce voltages in any conducting loop in their path, including sensor cables; that is why leads in such environments are kept short and routed without loops.

## Keeping currents within a limit

Any circuit that makes electrical contact with cells, tissue or a person carries a risk if current exceeds a level appropriate for that application. Medical device standards set such limits for specific situations; this lesson uses a synthetic design limit of 10 μA to show the arithmetic, not to state what is safe for any use.

**Current limiting.** If a stimulus circuit can apply at most 5 V, a series resistance of at least R = V/I = 5 / 10⁻⁵ = 500 kΩ keeps current below the limit even if every other resistance in the path fell to zero. A design that relies on the tissue's own resistance to limit current fails when that resistance changes, so the limit should be enforced by the circuit.

**Measuring leakage.** A leakage current can be estimated by placing a known resistor in the path and measuring the voltage across it. If 0.35 V appears across 100 kΩ, I = 0.35/10⁵ = 3.5 μA, below the 10 μA limit with a margin of 2.9×. The measuring instrument's own input resistance is in parallel with the sense resistor, so it must be much larger for the reading to be accurate.

## Common mistakes

- Using total pipe area instead of diameter in ε = Bdv.
- Forgetting the number of turns in Faraday's law.
- Relying on an uncontrolled load resistance to limit current.
- Reading a sense voltage with a meter whose input resistance is comparable to the sense resistor.

## Worked example

**Problem.** The flow meter above must resolve a velocity change of 1 mm/s. What voltage change is that, and what does it imply for the amplifier?

**Step 1.** Δε = B d Δv = 0.1 × 0.01 × 0.001 = 1.0 μV.

**Step 2.** The amplifier's noise and drift must be well below 1 μV over the measurement time.

**Step 3.** Electrode offsets and electrochemical drift easily exceed this, which is why practical meters alternate the field direction and measure the difference: the flow signal reverses with the field, while electrode offsets do not.

## Limits of this lesson

All values, including the current limit, are synthetic. The lesson is not guidance on electrical safety for any medical, laboratory or personal use; real limits come from the standards and risk analysis that apply to a specific device.

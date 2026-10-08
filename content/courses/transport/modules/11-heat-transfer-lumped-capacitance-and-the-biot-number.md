# Heat transfer: lumped capacitance, the Biot number and thermal time scales

Cultures, media and samples are warmed and cooled all the time: a flask taken from a refrigerator, a vial moved into a bath, a chamber exposed to room air when a door opens. How long this takes sets how long cells sit at the wrong temperature, and the same arithmetic describes thermal gradients inside a construct. This lesson treats the simplest case, a body that stays at one temperature throughout (lumped capacitance), derives its exponential time course and time constant, introduces the Biot number that says when the assumption holds, and compares the result with the time for conduction inside the body. The numbers are synthetic and the lesson is arithmetic about heat transfer, not a procedure for handling any sample.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute the time constant of a body cooling or warming by convection and the time to reach a target temperature.
2. Compute the Biot number and decide whether the lumped assumption holds.
3. Compare external and internal thermal time scales and evaluate when a gradient inside the body controls the time course.

## Lumped capacitance

If the temperature inside a body is uniform, an energy balance gives ρ c_p V dT/dt = −h A (T − T_∞), where h is the heat-transfer coefficient, A the surface area and T_∞ the temperature of the surroundings. The solution is exponential,

**T(t) = T_∞ + (T₀ − T_∞) e^(−t/τ), with τ = ρ c_p V/(h A).**

For a sphere V/A = D/6. **Synthetic example:** a water-like sphere (10 mm in diameter, ρ = 1000 kg/m³, c_p = 4180 J/(kg·K), k = 0.6 W/(m·K)) cooling in still air with h = 10 W/(m²·K) has V/A = 1.667 mm and **τ = 1000 × 4180 × 0.001667/10 = 697 s** (11.6 min). Moved from 37 °C into surroundings at 4 °C, it reaches 10 °C after t = τ ln((T₀ − T_∞)/(T − T_∞)) = 697 × ln(33/6) = **1188 s**, or 19.8 min. The time constant is long because a body with a large heat capacity and a small surface changes temperature slowly; it is proportional to the size of the body and inversely proportional to h.

## The Biot number

The lumped model assumes that conduction inside the body is fast enough to keep it uniform. The **Biot number**

**Bi = h (V/A) / k**

compares the resistance to conduction inside the body with the resistance to convection at its surface. For the sphere in air Bi = 10 × 0.001667/0.6 = **0.0278**, far below the usual rule-of-thumb limit of 0.1, so the lumped model is accurate. In a stirred bath with h = 500 W/(m²·K), the time constant would fall to τ = 13.9 s, but Bi = 1.39 exceeds 0.1, so the body is no longer uniform and the lumped result cannot be trusted.

## Internal conduction sets a floor

Conduction inside the body has its own time scale, of order R²/α with the thermal diffusivity α = k/(ρ c_p) = 1.4 × 10⁻⁷ m²/s: for R = 5 mm, **R²/α = 179 s**, and the slowest decay of a sphere whose surface is held at the bath temperature has the time constant R²/(π² α) = 18.1 s. If the external time constant (13.9 s in the bath) is shorter than the internal one, the interior controls the cooling: raising h further no longer helps, and the centre lags behind the surface. For the sphere in air the external time constant (697 s) is much longer than the internal one, so the whole body follows a single exponential. The same comparison applies to constructs, vials and flasks: a thin vessel in air is lumped, whereas a thick sample in a bath is limited by conduction.

## Common mistakes

- Using the lumped model without checking the Biot number.
- Using the time constant as the time to reach the final temperature.
- Expecting a fiftyfold higher h to give a fiftyfold shorter time when conduction inside the body takes over.
- Using the diameter, instead of V/A, as the length in the Biot number.
- Forgetting that an exponential approach never reaches the surrounding temperature in finite time.
- Applying the model to a body with internal heat generation or phase change.

## Worked example

**Problem.** A synthetic water-like sphere of 6 mm diameter is warmed in surroundings at 37 °C with h = 25 W/(m²·K), starting at 22 °C. Find the time constant, the Biot number and the time to reach 35 °C.

**Step 1: time constant.** V/A = 1.0 mm, so τ = 1000 × 4180 × 0.0010/25 = 167 s.

**Step 2: Biot number.** Bi = 25 × 0.0010/0.6 = 0.042, below 0.1, so the lumped model holds.

**Step 3: time to 35 °C.** t = τ ln((37 − 22)/(37 − 35)) = 167 × ln(15/2) = 337 s.

**Step 4: reading the result.** The body takes 2.0 time constants to come within 2 °C of its surroundings.

## Limits of this lesson

All numbers are synthetic, with water-like properties. The model assumes uniform temperature, a constant h, no phase change and no internal heat generation. Real samples have containers, air gaps and liquid layers, and h depends on the flow and the geometry. Nothing here is a protocol for warming, cooling, freezing or thawing any sample.

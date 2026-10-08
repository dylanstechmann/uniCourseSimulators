# Respiratory mechanics and gas exchange: ventilation, dead space, compliance and the alveolar gas equation

Breathing moves air in and out of the lungs, and gas exchange moves oxygen and carbon dioxide across the thin barrier between alveoli and blood. Two numbers organize most of the quantitative reasoning: the ventilation that actually reaches gas-exchanging alveoli, and the pressure each gas reaches there. Mechanics (how stiff the lungs and chest wall are, and how much the airways resist flow) decides what that ventilation costs to produce. This lesson computes alveolar ventilation, alveolar gas pressures, compliance and shunt with synthetic numbers and connects them to the oxygen-delivery lesson.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute minute and alveolar ventilation from tidal volume, breathing rate and dead space, and explain why shallow rapid breathing is less effective.
2. Apply the alveolar gas equation and the relation between alveolar CO₂, CO₂ production and alveolar ventilation.
3. Calculate lung–chest wall compliance and a shunt fraction, and predict the effects of stiff lungs and of shunt on gas exchange.

## Ventilation and dead space

Minute ventilation is tidal volume times breathing rate, V̇_E = V_T × f. Not all inspired air reaches alveoli: the conducting airways hold a **dead-space** volume V_D (about 150 mL in adults) that is filled with fresh air at the end of each inspiration and then exhaled unchanged. Alveolar ventilation is

**V̇_A = (V_T − V_D) × f.**

For V_T = 500 mL and f = 12 per minute with V_D = 150 mL, V̇_E = 6.0 L/min and V̇_A = 350 × 12 = 4.2 L/min. Now breathe more shallowly and faster: V_T = 250 mL and f = 24. Minute ventilation is unchanged at 6.0 L/min, but alveolar ventilation falls to (250 − 150) × 24 = 2.4 L/min, because the same dead space is refilled twice as often.

## Carbon dioxide and alveolar ventilation

Carbon dioxide is produced by metabolism at V̇_CO₂ and removed only by alveolar ventilation, so the alveolar (and, closely, arterial) CO₂ pressure is set by their ratio:

**P_ACO₂ ≈ 0.863 × V̇_CO₂ / V̇_A,**

with V̇_CO₂ in mL/min, V̇_A in L/min and the result in mmHg (the constant converts between gas conditions). With V̇_CO₂ = 200 mL/min and V̇_A = 4.2 L/min, P_ACO₂ = 0.863 × 200/4.2 = 41.1 mmHg. Halving alveolar ventilation doubles it to 82.2 mmHg. Because CO₂ pressure scales inversely with V̇_A, it is the most direct readout of whether alveolar ventilation matches the metabolic load.

## The alveolar gas equation

The oxygen pressure in the alveoli is set by the inspired pressure, minus the carbon dioxide that replaces some of it:

**P_AO₂ = F_IO₂ (P_B − P_H₂O) − P_aCO₂ / R,**

where P_B is barometric pressure, P_H₂O = 47 mmHg the water vapor pressure at body temperature, and R the respiratory exchange ratio (CO₂ produced per O₂ consumed, about 0.8). For room air at sea level (760 mmHg, F_IO₂ = 0.21) and P_aCO₂ = 40 mmHg, P_AO₂ = 0.21 × (760 − 47) − 40/0.8 = 99.7 mmHg. If alveolar ventilation falls so that P_aCO₂ rises to 80 mmHg, P_AO₂ falls to 49.7 mmHg: hypoventilation lowers oxygen as well as raising carbon dioxide. With F_IO₂ = 0.5 and normal CO₂, it rises to 306 mmHg.

The **alveolar–arterial difference**, P_AO₂ − P_aO₂, measures how well oxygen crosses from alveolus to blood. With a measured arterial P_aO₂ of 90 mmHg, the gradient is 99.7 − 90 = 9.7 mmHg. Hypoventilation alone lowers both P_AO₂ and P_aO₂ and leaves the gradient normal, whereas impaired diffusion, ventilation–perfusion mismatch or shunt widen it.

## Mechanics: compliance and resistance

Lung **compliance** is the volume change per unit pressure change, C = ΔV/ΔP. The lungs and chest wall act in series, so their compliances combine like springs in series: **1/C_total = 1/C_lung + 1/C_wall**. With both at 200 mL/cmH₂O, C_total = 100 mL/cmH₂O. If the lungs stiffen to 50 mL/cmH₂O, C_total falls to 40: the same breath now needs 2.5 times the pressure change. Because the total is dominated by the stiffer element, a stiff lung makes the whole system stiff.

Airflow obeys ΔP = R × flow, with airway resistance rising steeply as radius falls (the fourth-power relation from the hemodynamics lesson applies roughly to laminar flow in a narrowed airway). Both extra stiffness and extra resistance raise the work of breathing, and the body responds by changing the pattern of breathing, usually shallower and faster when the lung is stiff and slower and deeper when the airways are obstructed.

## Shunt

Blood that passes the lung without contacting ventilated alveoli (a **shunt**) arrives in the arteries with the oxygen content of mixed venous blood. The shunt fraction follows from oxygen contents:

**Q̇_s / Q̇_t = (C_cO₂ − C_aO₂) / (C_cO₂ − C_vO₂),**

where C_cO₂ is the content of blood leaving ventilated alveoli (end-capillary). With contents 20.1 (end-capillary), 19.0 (arterial) and 15.2 (mixed venous) mL/dL, the shunt fraction is (20.1 − 19.0)/(20.1 − 15.2) = 0.22. A large shunt is only partly corrected by breathing more oxygen, because shunted blood never contacts the extra oxygen; mismatch between ventilation and perfusion responds much better to it.

## Common mistakes

- Equating minute ventilation with the ventilation that reaches the alveoli.
- Forgetting that halving alveolar ventilation doubles alveolar CO₂ pressure.
- Using P_B instead of P_B − P_H₂O in the alveolar gas equation.
- Assuming a normal alveolar–arterial gradient means normal gas exchange when ventilation is low.
- Adding series compliances as if they were parallel.
- Expecting oxygen therapy to cure a large shunt.

## Worked example

**Problem.** A synthetic person breathes with V_T = 400 mL at f = 15 per minute (V_D = 150 mL) and produces 250 mL/min of CO₂. Estimate alveolar ventilation, alveolar CO₂ and alveolar oxygen in room air.

**Step 1: ventilation.** V̇_A = (400 − 150) × 15 = 3750 mL/min = 3.75 L/min.

**Step 2: carbon dioxide.** P_ACO₂ = 0.863 × 250/3.75 = 57.5 mmHg, above the 40 mmHg of the earlier example.

**Step 3: oxygen.** P_AO₂ = 0.21 × 713 − 57.5/0.8 = 77.8 mmHg.

**Step 4: reading the result.** The raised CO₂ and lowered O₂ together point to inadequate alveolar ventilation for this metabolic rate, not to a barrier problem, which a normal alveolar–arterial gradient would confirm.

## Limits of this lesson

All values are synthetic and round. The alveolar gas equation uses a single average alveolus, the CO₂ relation assumes steady state and inspired air free of CO₂, and compliance is not constant across the lung volume range. The lesson explains reasoning about gas exchange and gives no medical advice.

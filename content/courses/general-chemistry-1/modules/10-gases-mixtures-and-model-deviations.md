# Gases, mixtures and model deviations

## Learning objectives

1. Calculate ideal-gas pressure with consistent absolute-temperature and volume units.
2. Relate mixture amounts to mole fractions and partial pressures.
3. Compare kinetic-model speed and compressibility while identifying limits of the ideal model.

## A state model with units

The ideal-gas equation PV=nRT links pressure, volume, amount and absolute temperature. It neglects intermolecular interactions and molecular excluded volume. Use kelvin rather than Celsius in its temperature factor. Use a gas constant whose pressure-volume units match the other quantities. For the new calculations here, take the rounded value R=8.314 J/(mol·K), equivalent to Pa·m³/(mol·K). Its scale follows from the [NIST defining constants](https://www.nist.gov/pml/special-publication-330/sp-330-section-2), with R=N_Ak before rounding.

For a synthetic gas sample n=0.25 mol, T=300 K and V=5.00 L=0.00500 m³, the model gives P=0.25×8.314×300/0.005=124710 Pa, or 124.71 kPa. Using 5.00 as though it were cubic metres would lower the result by a factor of one thousand. Using a Celsius number without adding the reference offset would describe neither the intended absolute temperature nor the same state.

The equation predicts relationships under stated constraints. At fixed amount and volume, doubling absolute temperature doubles pressure, giving 249.42 kPa at 600 K in this construction. At fixed amount and temperature, doubling volume halves pressure. The conditions are essential: allowing gas to escape or react changes amount, while a temperature change can also affect phase or chemistry.

## Mixture composition

For an ideal mixture of nonreacting gases, each component has partial pressure p_i=n_iRT/V. Total pressure is the sum, and p_i=y_iP with mole fraction y_i=n_i/n_total. Amount fractions sum to one. Mass fractions differ when molar masses differ; a component contributing 40% of the moles need not contribute 40% of the mass.

Suppose the 0.25 mol sample contains 0.10 mol A and 0.15 mol B. Then y_A=0.4 and y_B=0.6. At the stated temperature and volume, p_A=49.884 kPa and p_B=74.826 kPa, summing to 124.71 kPa. The component names are hypothetical and their amounts are stipulated. Neither partial pressure is the pressure that would result from inserting each gas into a different container volume.

For a reacting gas mixture, update the species amounts before computing composition. For a gas collected in contact with a liquid, the measured total pressure may include vapor. Removing that contribution needs a justified vapor-pressure value at the relevant temperature. The simple mixture equation does not establish that a real collection is dry, leak-free or at uniform temperature.

## Molecular motion and temperature

The elementary kinetic model relates temperature to translational kinetic energy. Root-mean-square speed is u_rms=√(3RT/M) for molar mass M in kg/mol when R is in J/(mol·K). For a stipulated M=0.028 kg/mol and T=300 K, it is approximately 516.93 m/s. Substituting 28 without converting grams to kilograms would produce a speed too small by √1000.

Root-mean-square speed is not the velocity of every molecule, the mean signed velocity or the bulk flow speed. A stationary sample can have zero mean directed velocity while its molecules have large individual speeds. Different speed averages have different formulas. The model assumes an equilibrium thermal distribution; a temperature value alone does not justify applying it to every nonequilibrium flow.

At the same temperature, the RMS-speed ratio of two species is the square root of the inverse molar-mass ratio. A lighter species therefore has greater RMS speed under the same model. This relation does not mean heavier molecules have a lower average translational energy at that common temperature; mass and squared speed compensate in the energy relation.

## A deviation diagnostic

Define compressibility factor Z=PV/(nRT). The ideal model gives Z=1. If the same synthetic state has a supplied pressure reading 135.0 kPa rather than 124.71 kPa, then Z=135.0/124.71≈1.082512. This expresses a departure from the ideal equation using those supplied inputs. It does not by itself identify a unique intermolecular mechanism or distinguish a real-gas effect from an amount, volume, temperature or pressure error.

Real-gas deviations become important in some high-density or low-temperature regimes, but no universal cutoff is specified here. A correction model must be justified for the actual substance and state. A value of Z near one also does not prove that every ideal-mixture or kinetic assumption is satisfied. Agreement with one equation can coexist with other modeling errors.

## Worked example

Convert 5 L to 0.005 m³, evaluate PV=nRT and obtain 124.71 kPa. Divide the specified A amount 0.10 mol by total 0.25 mol to obtain mole fraction 0.4, then multiply by total pressure for 49.884 kPa. Independently compare the supplied 135.0 kPa reading to ideal pressure and obtain Z≈1.082512. Finally use M=0.028 kg/mol in the RMS formula for approximately 516.93 m/s. Pressure, composition, deviation and molecular speed are related quantities but answer different questions.

## Common mistakes and checks

Do not use Celsius as an absolute-temperature factor. Match litres or cubic metres to the gas constant. Distinguish mole fraction from mass fraction, partial pressure from total pressure and RMS speed from bulk flow. A sum of partial pressures should reproduce the ideal total under the specified mixture assumptions. A positive amount, temperature and volume should give a positive model pressure.

## Limits of this lesson

Gas amounts, species and pressure observations are synthetic. The lesson supplies no pressure-vessel setting, gas-handling procedure or measured material property. It develops introductory state and kinetic models rather than a complete real-gas equation of state. Practice checks selected calculations and conditions. Original content has substantial AI assistance; the package remains partial, unreviewed and formative-only.

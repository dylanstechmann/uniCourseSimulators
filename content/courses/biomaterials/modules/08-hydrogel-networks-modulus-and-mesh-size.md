# Hydrogel networks: stiffness, crosslink density and mesh size

A hydrogel is a polymer network swollen with water, and three of its properties are linked by the same few numbers: how stiff it is, how tightly it is crosslinked, and how large the gaps in the network are. The links matter for design. Cells feel stiffness, cargo molecules feel the gaps, and degradation changes both at once. This lesson uses the theory of an ideal rubbery network to turn a measured modulus into a crosslink density, a molar mass between crosslinks and a mesh size, compares the mesh with the size of a cargo, and states where the ideal picture fails. All values are synthetic and illustrative; the formulas are textbook-level estimates, not predictions for a real gel.

## Learning objectives

By the end of this lesson, you should be able to:

1. Relate a gel's shear modulus to the density of elastically active chains and the molar mass between crosslinks using ideal rubber elasticity.
2. Estimate the mesh size from the modulus and how it changes when crosslinks are lost.
3. Compare the size of a cargo with the mesh size to judge diffusion hindrance, and evaluate the limits of the ideal-network picture.

## Modulus and the density of chains

In an ideal affine network, each elastically active chain stores thermal energy, and the shear modulus is proportional to how many chains there are per volume:

**G = ν R T,**

where ν is the amount of elastically active chains per volume (mol/m³), R = 8.314 J/(mol·K) and T the temperature in kelvin. A gel that is nearly incompressible has Young's modulus **E ≈ 3 G**. **Synthetic values:** G = 12 kPa at T = 310 K (37 °C). Then ν = 12000 / (8.314 × 310) = **4.66 mol/m³** and E = **36 kPa**.

If the polymer concentration is c = 100 kg/m³ (10% w/v), the molar mass of polymer per elastically active chain is Mc = c/ν = 100 / 4.66 = **21.5 kg/mol** (21.5 kDa). A gel made from longer chains between crosslinks is softer. The polymer concentration follows from the swelling: a gel that swells to Q = 10 times its dry volume has a polymer volume fraction φ = 1/Q = 0.1, which for a polymer density of 1000 kg/m³ gives c = φ ρ = 100 kg/m³.

Real networks contain loops, dangling ends and entanglements, so not every nominal crosslink is elastically active and the effective ν is smaller than the amount of crosslinker added. The ideal formula is a way of reading a measured modulus, not of predicting it from the recipe.

## Mesh size

Each elastically active chain occupies a volume of roughly ξ³, so the spacing between crosslinks is about

**ξ ≈ (k_B T / G)^(1/3),**

which is the same as the cube root of the volume per chain, since G = n k_B T with n chains per m³. With k_B = 1.381 × 10⁻²³ J/K, ξ = ((1.381 × 10⁻²³ × 310) / 12000)^(1/3) = **7.1 nm**. Because ξ depends on the cube root, large changes in stiffness give small changes in mesh size: doubling the crosslink density doubles G and shrinks ξ only by 2^(−1/3) = 0.79, to 5.6 nm, and a gel ten times stiffer has a mesh only 2.15 times smaller. This is why stiffness and mesh size cannot be tuned independently by changing the crosslinker alone, and why a stiffer gel releases a cargo more slowly while also resisting cell spreading.

## Cargo size against mesh size

A cargo's size is expressed by its hydrodynamic radius r_h. In water at 310 K and viscosity η = 0.69 mPa·s, the Stokes–Einstein relation D₀ = k_B T / (6π η r_h) gives, for r_h = 3.5 nm, **D₀ = 94 μm²/s**, so free diffusion over 1 mm would take about L²/D₀ = 2.95 h (compare the release estimates in the lesson on hydrogel degradation). Inside the gel the cargo moves more slowly, and the ratio r_h/ξ is the first thing to look at: 3.5 nm against 7.1 nm gives 0.49, whereas a larger cargo with r_h = 6 nm gives 0.85, close to the point at which it is trapped and moves only when the network fluctuates or breaks down. Several models (obstruction, hydrodynamic and free-volume) turn this ratio into a diffusion coefficient, each with fitted parameters; none is derived here.

## What degradation does to the network

When crosslinks are cleaved, ν falls. If 40% of the elastically active chains are lost, G falls to 0.6 × 12 = 7.2 kPa and the mesh grows to ξ = 7.1 × (1/0.6)^(1/3) = **8.4 nm**. The larger cargo's ratio falls from 0.85 to 0.71, so it is released more readily as the gel weakens, even though most of the mass is still present. The ideal formula changes linearly with the loss of chains; real gels lose stiffness faster near the point where the network stops being connected, so the formula understates the loss of stiffness late in degradation.

## Common mistakes

- Using the Young's modulus where the shear modulus is needed, or the reverse.
- Entering the temperature in degrees Celsius instead of kelvin.
- Equating the amount of crosslinker added with the density of elastically active chains.
- Treating the mesh size as an exact pore diameter.
- Expecting to change the stiffness of a gel without changing its mesh.
- Applying ideal-network formulas to gels with strong entanglement, charge or heterogeneity without checking.

## Worked example

**Problem.** A synthetic gel has G = 30 kPa at 310 K and a polymer concentration of 150 kg/m³. Find ν, Mc, the mesh size and E, and compare it with a cargo of r_h = 3.5 nm.

**Step 1: chains.** ν = 30000 / (8.314 × 310) = 11.64 mol/m³.

**Step 2: molar mass.** Mc = 150 / 11.64 = 12.9 kg/mol.

**Step 3: mesh and modulus.** ξ = (k_B T / G)^(1/3) = 5.23 nm and E ≈ 3 G = 90 kPa.

**Step 4: the cargo.** r_h/ξ = 3.5/5.23 = 0.67: this gel is stiffer and has a tighter mesh than the one above, and the same cargo is considerably more hindered.

## Limits of this lesson

All numbers are synthetic. Ideal rubber elasticity assumes Gaussian chains, affine deformation and no entanglements, and the mesh-size formula is a scaling estimate with an unknown prefactor. Real gels are heterogeneous, may be charged, and show viscoelastic relaxation that a single modulus ignores. Nothing here is a prediction for a real hydrogel or evidence about any cell.

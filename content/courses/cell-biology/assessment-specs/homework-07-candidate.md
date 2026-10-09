# Homework 7 candidate: matched matrix inputs and localization evidence

**State:** inactive candidate for review, authored with substantial Codex assistance for Biology 0.26.0. The course remains partial, unreviewed and formative-only. This proposed 25-point packet has no live submission route, contributes no course grade and is absent from the Practice gradebook. Keys/tests remain outside Git. Independent review is missing and workload has not been measured. No actual deadline, time limit, attempt or release policy is set.

Prerequisites: [11a-cytoskeleton-adhesion-and-extracellular-matrix](../modules/11a-cytoskeleton-adhesion-and-extracellular-matrix.md), [11b-matrix-mechanics-and-mechanotransduction](../modules/11b-matrix-mechanics-and-mechanotransduction.md). Open homework remains public practice; this candidate uses new observations/stems rather than relabeling its answers as confidential.


## Design and dictionary

The [matrix table](homework-07-candidate-matrix.csv) contains four independent parent culture preparations b01–b04. Each supplies matched randomized splits to six conditions:soft/stiff by low/high accessible ligand, plus block/rescue at stiff-high. The24 rows are matched constructs, not24 independent preparations. Equal preparation weight defines the summaries. These deterministic synthetic values contain no physical test, calibration/uncertainty model or independently verified target engagement. Condition names denote the stipulated intervention, not proof of specificity.

original_area_mm2 and initial_length_mm describe initial specimen geometry; extension_mm is extension in the stipulated small-strain test. force_signal_n includes force_background_n. accessible_ligand_au is the stated accessible surface ligand proxy, not solution concentration. seeded_cells is the same input count across condition splits within a preparation; viable_attached_cells is a different recovered population. nuclear_marker_positive_cells refers to a predefined localization threshold in those viable attached cells. summed_cell_area_um2 sums their areas. An image field/cell is not a new biological preparation.

## Analysis and assumptions

Subtract the stated force baseline before stress calculation. One mm² is10⁻⁶m². Engineering stress is corrected force/original area and strain is extension/initial length. E=stress/strain is a corrected secant; it equals the Young slope only under the stipulated uniform linear-elastic-through-origin model. A real specimen needs an appropriate curve, force/geometry calibration, hydration, direction, rate and range evidence. A single E cannot summarize viscoelasticity, anisotropy, remodeling or cellular activity. The dataset supplies positive geometry/strain denominators; unavailable denominators must be flagged, not fabricated.

Calculate mean area and nuclear-marker percent among viable attached cells within each preparation/condition. Compute factorial differences within each preparation before averaging. Differences are percentage points; dividing by a baseline would answer a relative-change question. Matched splits retain the biological block, but this balanced construction lets some unpaired arithmetic coincide on the same descriptive number. Correct scored output cannot certify the analysis method or uncertainty. No confidence interval, p-value or molecular interaction is established.

Ligand differences and attached-cell counts are deliberately visible. soft_high versus stiff_high matches the stated ligand level; soft_low versus stiff_high changes two inputs. Block/rescue also change attachment, so a changed percentage among attached cells can include selection/composition effects. Count cells per seeded input if that is the claim, and collect missing-cell/state information. Nuclear localization is not a force calibration, universal stiffness sensor, lineage outcome or mature function measurement. Restoration narrows involvement only with appropriate specificity/engagement controls.

## Separate worked illustration and response scales

Unrelated example:corrected force0.00012N over3mm² gives40Pa. Extension0.20mm over10mm gives strain0.02, so the linear model yields2000Pa. A region with20 positive among80 attached cells has 25 percent positivity; if100 were seeded, the positive-per-seeded fraction is20 percent. Those denominators answer different questions.

The four numeric items use the declared Pa,µm²,percent and bare percentage-point scales. Modulus tolerance 0.5Pa,area0.05µm²,percent0.005points and contrast0.005points are response tolerances, not experimental uncertainty. The first three enforce three significant figures and compatible units/dimensions; the contrast is bare without a significant-figure rule. CSV cells are bare decimals with exact counts and tolerance 0.005 on stated scales, without lexical precision checks. Composite percent uses three significant figures/tolerance 0.005points and a separate one-point categorical field. Choices are not prose grading; multiple-select scoring appears in its stem.


## Item packet

### Item 1 — 2 proposed points

For stiff_high preparation b01, subtract force background, convert the original area from mm² to m², calculate engineering strain and infer E under the stated linear-elastic-through-origin model. Report modulus in Pa with exactly three significant figures.

### Item 2 — 2 proposed points

For stiff_high b01, divide summed_cell_area_um2 by viable_attached_cells. Report mean area in µm² with exactly three significant figures; seeded cells are a different denominator.

### Item 3 — 2 proposed points

For stiff_high b01, report nuclear_marker_positive_cells/viable_attached_cells as a percent with exactly three significant figures.

### Item 4 — 2 proposed points

For each independent preparation compute (stiff_high−stiff_low)−(soft_high−soft_low) using nuclear-marker percentages among viable attached cells, then average the four preparation contrasts. Report a bare signed percentage-point difference, not a relative percent or significance test.

### Item 5 — 9 proposed points

Upload exact columns condition,preparations,mean_area_um2,mean_marker_pct with rows soft_high,stiff_high,stiff_high_block. Derive area and marker fraction within each preparation before averaging with equal preparation weight. Counts are exact; means have tolerance0.005 on their µm² or percent column scales. Matched condition splits are repeated observations of the same independent preparation.

### Item 6 — 2 proposed points

Using equal-preparation mean nuclear-marker percentages, compute the fraction of the stiff_high-versus-block difference recovered by the rescue condition.

**gap_recovered_pct (1 point):** Report100×(rescue−block)/(stiff_high−block) as a percent. Report exactly 3 significant figures.

**inference (1 point):** What does this recovery support?

1. The intervention uniquely proves a single direct force pathway and mature tissue function.

2. It supports restoration of this localization readout under the tested conditions; attachment/selection, target engagement and alternative pathways still need tests.

3. The nuclear-marker fraction measures Young modulus directly.

### Item 7 — 4 proposed points

Select one response for each distinct matrix or inference criterion.

**ligand (1 point):** Which comparison holds the stated accessible ligand level fixed while changing measured modulus?

1. soft_low versus stiff_high

2. soft_high versus stiff_high, with other stated conditions and measurement limits retained

3. Any two conditions because the coating solution was prepared once

**selection (1 point):** Why retain seeded and viable-attached cell counts?

1. Perturbations can alter attachment/recovery and the sampled population; percentages among attached cells do not describe lost cells.

2. A higher marker fraction always means more positive cells per seeded culture.

3. Viable-cell counts prove the exact molecular route.

**mechanics (1 point):** What limits the single corrected stress/strain modulus?

1. One secant value identifies all relaxation and anisotropy.

2. Force divided by area is already a modulus.

3. It equals the linear model slope only under the stated assumptions; hydration, geometry, rate, relaxation and nonlinear response need measurements.

**route (1 point):** Which follow-up strengthens a proposed integrin/actomyosin route?

1. A nuclear-marker image alone gives adhesion force and cell fate.

2. Matched target/pathway perturbations, target engagement, attachment/state controls and orthogonal force or function readouts.

3. Ignore ligand and viability because a rescue was present.

### Item 8 — 2 proposed points

Select all supported statements. Scoring is two points times (correct selections minus incorrect selections) divided by the number of correct options, clamped from zero to two.

1. Actin, microtubules and intermediate filaments have interchangeable assembly and motor roles.

2. Integrin-associated focal adhesions can connect matrix to actin-associated structures; a cadherin cell–cell junction asks a different connection question.

3. A nuclear localization readout alone establishes stable differentiation and tissue function.

4. Matching one instantaneous modulus proves all matrices have identical ligand accessibility and relaxation.

5. Intermediate-filament-linked junctions and microtubule-based transport illustrate distinct network roles; context and direct measurements remain necessary.

## Discussion and activation requirements

Written methods, explanations, uncertainty, plots, scripts and study design are ungraded. For unscored discussion, identify the measurement, denominator, independent unit, assumptions, alternative and a matched follow-up. Draft adequate-work descriptors require those elements; they are an unscored review guide, not a qualified rubric or human grade. Numeric/CSV/choice cells cover a limited subset of the instruction. Independent numerical, grader-mutation, scientific, assessment, manual accessibility/fairness review, measured workload and operator provisioning/release remain absent. Automated same-AI checks do not satisfy these gates.

Original packet and synthetic data: CC BY 4.0 with substantial Codex assistance. Existing original lessons provide context; no outside source, prose,problem,figure,dataset or identifier imported; no new identifier-resolution pass claimed. This is a paper/data exercise, not a wet-lab protocol, clinical result or proof of therapeutic benefit. Public metadata binds external-key and prerequisite hashes. Local artifacts and temporary protected delivery fixtures do not approve deployment. Earlier candidates preserve their authored files, versions and bindings. No candidate is activated.

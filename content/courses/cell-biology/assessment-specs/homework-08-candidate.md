# Homework 8 candidate: time-resolved cell-state denominators

**State:** inactive candidate for review, authored with substantial Codex assistance for Biology 0.27.0. The course remains partial, unreviewed and formative-only. This proposed 25-point packet has no live submission route, contributes no course grade and is absent from the Practice gradebook. Keys/tests remain outside Git. Independent review is missing and workload has not been measured. No actual deadline, time limit, attempt or release policy is set.

Prerequisites: [12a-cell-cycle-checkpoints-and-mitosis](../modules/12a-cell-cycle-checkpoints-and-mitosis.md), [12b-senescence-apoptosis-and-cell-fate](../modules/12b-senescence-apoptosis-and-cell-fate.md). Open homework remains public practice; this candidate uses new observations/stems rather than relabeling its answers as confidential.


## Construction and dictionary

The [cell-state table](homework-08-candidate-fate.csv) contains three conditions, four independent cultures per condition and matched observations0,24,72hours after a stipulated cue-removal/challenge point. The36 rows are repeated aliquots, not36 independent cultures. Numerals across condition IDs do not establish biological pairing. The conditions vehicle,withdrawal_refeed and damage_challenge specify the construction, not measured proof of a pathway or pure fate.

seeded_cells is the starting input, all_recovered_cells includes recovered viable/nonviable cells and viable_singlets is the declared live-singlet analysis gate. DNA2N,S-range,4N counts partition the viable-singlet pool under this simplified diploid gating model. Their assignment does not resolveG2 fromM or all abnormal ploidy/doublets. edu_positive_viable,p21_high_viable,beta_gal_high_viable and mitotic_marker_positive_viable each use viable_singlets. caspase_positive_all_recovered uses all_recovered_cells. Marker channels can overlap; no joint-overlap data exist, so these are not exhaustive mutually exclusive fates. The recovered counts give no marker profile of cells lost from the sampled population.

All observations are deterministic synthetic teaching counts. Large cell counts do not replace four independent cultures or create realistic uncertainty. No raw flow/image files, instrument/gate validation, marker specificity, challenge efficacy, error distribution or workload pilot was measured. The counts and thresholds are assumptions of this exercise, not a lab protocol or diagnostic assay.

## Analysis and inference

Calculate each marker fraction using its declared gate within a culture/time point. Average culture-level percentages with equal culture weight at72h. Count cultures once despite three times and many channels. A pooled cell fraction weights cultures by cell number and answers a different question. Recovery relative to seeded input is a count ratio, not an independently established survival probability; proliferation, selection, detachment and gating can affect it. Missing cells cannot be reconstructed by renormalizing recovered markers.

The requested relative EdU decrease divides a group-mean difference by vehicle mean; a percentage-point difference has no such denominator. The reentry ratio compares observed group means and is not a causal effect size or population risk. No interval,p-value or unique mechanism is supplied. DNA-content, pulse incorporation and a mitotic marker measure different proxies; a4N peak alone cannot name a checkpoint or separateG2 fromM.

Low post-challenge incorporation with multiple senescence-associated features can support a bounded persistent-arrest interpretation in this window. It does not show every cell is identical or permanently arrested. Validate challenge conditions and follow a longer suitable recovery window with orthogonal markers/state and cell counts. Effector caspase positivity is downstream evidence, not proof of mitochondrial versus receptor initiation; loss alone can have many causes. The data do not establish tissue function, organismal aging or therapeutic benefit.

## Separate worked example and responses

Unrelated example:40EdU-positive among200viable singlets gives20percent. If250total cells were recovered and 25were caspase-positive in that broader gate, its fraction is10percent, not25/200. If160viable singlets were recovered from200seeded cells, the count ratio is80percent, but it does not identify why40cells are missing or what markers they had.

Four standalone percentages require compatible units and exactly three significant figures, with tolerance 0.005percentage points. The composite bare ratio requires three significant figures/tolerance 0.005 on its declared dimensionless scale; its categorical field carries one separate point. CSV cells are bare percentages, exact culture counts and tolerance 0.005points without lexical precision enforcement. Structured fields score explicit choices only; multiple-select scoring appears in its stem. The25proposed points are an inactive review allocation, not a course grade.


## Item packet

### Item 1 — 2 proposed points

For damage_challenge culture g01 at72h, report edu_positive_viable/viable_singlets as a percent with exactly three significant figures. Other recovered cells and seeded cells are different denominators.

### Item 2 — 2 proposed points

For damage_challenge g01 at72h, report viable_singlets/seeded_cells as a percent with exactly three significant figures. This is recovered viable count relative to seeded input, not proof of a unique death mechanism.

### Item 3 — 2 proposed points

For vehicle c01 at72h, report mitotic_marker_positive_viable/viable_singlets as a percent with exactly three significant figures. The DNA4N bin is not the denominator requested here.

### Item 4 — 2 proposed points

At72h first calculate EdU percent among viable singlets within each culture, then equal-culture group means. Report100×(vehicle_mean−damage_challenge_mean)/vehicle_mean as a percent with exactly three significant figures, not a percentage-point difference.

### Item 5 — 9 proposed points

Upload exact columns condition,cultures,mean_edu_pct_viable,mean_caspase_pct_all_recovered with rows vehicle,withdrawal_refeed,damage_challenge. Use72h values, calculate percentages with their distinct stated gates per culture, then average equally. Counts are exact; percentage means have tolerance0.005points. Times and counted cells do not add independent cultures.

### Item 6 — 2 proposed points

Compare equal-culture mean EdU-positive fractions at72h after the stipulated cue removal/challenge.

**reentry_ratio (1 point):** Report withdrawal_refeed mean divided by damage_challenge mean as a bare ratio. Report exactly 3 significant figures.

**inference (1 point):** Which inference fits that descriptive ratio and the time course?

1. The ratio proves that every damaged cell is permanently senescent.

2. It proves that caspase activity initiated the lower EdU fraction.

3. It indicates more measured pulse incorporation after refeed than after the damage challenge in this window; pure cell identities, long-term persistence and causal pathways need further evidence.

### Item 7 — 4 proposed points

Select one response for each longitudinal or pathway criterion.

**persistence (1 point):** How should low post-challenge EdU with p21/beta-gal features be described?

1. A unique diagnosis from one marker in every sampled cell.

2. Proof of irreversible arrest for all future conditions.

3. A pattern compatible with a persistent senescence-associated arrest in the tested window; repeated/orthogonal recovery, state and viability evidence is still needed.

**gates (1 point):** Why are caspase and EdU percentages not interchangeable?

1. Both use exactly the seeded population.

2. Caspase uses all recovered cells; EdU uses viable singlets, and neither measures marker states in lost cells.

3. They are exhaustive mutually exclusive cell-state categories.

**apoptosis (1 point):** Which statement distinguishes the instructional routes without overreading the assay?

1. Intrinsic mitochondrial signaling can involve BAX/BAK, cytochrome-c/APAF-1 and caspase9; death-receptor signaling can involve caspase8, while an effector-caspase marker alone does not identify the initiating route.

2. Effector-caspase positivity uniquely proves the mitochondrial trigger.

3. All loss of viable cells is necessarily apoptosis.

**checkpoint (1 point):** What would strengthen a claim about a named checkpoint pathway?

1. A4N DNA peak alone measures every spindle attachment and DNA base.

2. Cyclin abundance alone is kinase activity.

3. Time-resolved pathway/target-engagement evidence, matched perturbation and orthogonal DNA-content/incorporation/mitotic imaging with gate and viability controls.

### Item 8 — 2 proposed points

Select all supported statements. Scoring is two points times (correct selections minus incorrect selections) divided by the number of correct options, clamped from zero to two.

1. A4N DNA signal uniquely distinguishes mitosis fromG2.

2. A short EdU pulse reports incorporation within its stated collection/gate; it does not directly measure each cell's lifetimeS-phase duration.

3. Beta-gal activity alone identifies a universal permanent senescence state.

4. Caspase-positive, p21-high and beta-gal-high counts can be added to obtain exhaustive nonoverlapping fates.

5. A snapshot phase-like fraction and a stable cell-state claim require different longitudinal and orthogonal evidence.

## Discussion and activation requirements

Written methods, explanations, uncertainty, plots, scripts and study design are ungraded. For unscored discussion, identify the measurement, denominator, independent unit, assumptions, alternative and a matched follow-up. Draft adequate-work descriptors require those elements; they are an unscored review guide, not a qualified rubric or human grade. Numeric/CSV/choice cells cover a limited subset of the instruction. Independent numerical, grader-mutation, scientific, assessment, manual accessibility/fairness review, measured workload and operator provisioning/release remain absent. Automated same-AI checks do not satisfy these gates.

Original packet and synthetic data: CC BY 4.0 with substantial Codex assistance. Existing original lessons provide context; no outside source, prose,problem,figure,dataset or identifier imported; no new identifier-resolution pass claimed. This is a paper/data exercise, not a wet-lab protocol, clinical result or proof of therapeutic benefit. Public metadata binds external-key and prerequisite hashes. Local artifacts and temporary protected delivery fixtures do not approve deployment. Earlier candidates preserve their authored files, versions and bindings. No candidate is activated.

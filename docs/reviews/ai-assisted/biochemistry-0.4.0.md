# AI-assisted check: Biochemistry I: Proteins, Enzymes & Metabolism 0.4.0

**This is not a human review.** It was run on 2026-10-08 by an AI coding assistant (Claude Sonnet 5.5 in
Claude Code) on material that the same kind of system had just written, so it is not independent and may
share that material's blind spots. It changes no maturity or review label. The package remains `partial`,
unreviewed and formative-only.

- **Version checked:** the working tree that became 0.4.0.
- **Scope:** lessons 8 to 13 (amino acids, charge and pH; protein folding and stability; glycolysis, energy
  charge and the AMP signal; mitochondrial bioenergetics; flux control and the layers of regulation; reading a
  metabolic perturbation), the enzyme-kinetics lab (reading, dataset and seven items), the schedule, the
  learner-facing limitations and the syllabus. It also covers the numerical keys of the earlier lessons 1, 2,
  3, 5, 6 and 7. All 49 new items were checked.
- **Not checked:** teaching depth and sequencing, Bloom labels, accessibility, and the textbook-level values
  listed below, which cite no source.

## Method

1. Every numerical key in the package (all 63 numeric items, old and new) was recomputed independently from the
   numbers in its prompt, with constants written out. The calculations are kept as tests in
   `tests/content/test_ai_assisted_checks.py`, which also asserts that every numeric item is covered. The
   check found one older numeric item (`biochemistry-1:check`) that the first list had missed, and it agrees too.
2. The lab keys were recomputed from the lab CSV with separate code: the replicate means, the least-squares
   double-reciprocal fits, the apparent Km and the inhibition constant. The fit recovers the parameters the
   data were built from (Vmax 100, Km 5, apparent Km 15, K_I 2) to within 0.5%.
3. All 49 new items were graded with the real grader using a correct response: 49 of 49 earned full credit
   after one fix (see the table).
4. Each lesson was read twice, once after drafting and once as rendered, for accuracy, internal consistency and
   overclaiming.

## Results

No answer key in the package was wrong, including the 15 older numeric keys. Six problems were found in the
drafts and fixed before the version was committed:

| # | Where | Severity | Finding | Status |
|---|---|---|---|---|
| 1 | Lesson 13, baseline | error | The text said most glucose carbon is oxidized at baseline, but its own numbers send 64% of the glucose to lactate even though 90% of the ATP is oxidative. | Corrected, and turned into a teaching point: a high baseline lactate-to-glucose ratio is not by itself a sign of a mitochondrial problem |
| 2 | Lab item `control-fit` | error | Vmax = 100 asked "to 3 significant figures" reads as one significant figure, so a correct answer lost credit under the real grader. | Asks for 4 significant figures |
| 3 | Lesson 8 | misleading | Isoelectric points were printed as 6.01 and 3.23 where the exact values are 6.015 and 3.225, which would confuse a student checking the arithmetic. | Printed at full precision |
| 4 | Lesson 11 | misleading | "The same small pool is therefore made and used about once or twice a minute" does not follow from 30 g/min against a pool of tens of grams. | Now "remade every minute or two (estimates vary)" |
| 5 | Lesson 12 | error | One answer option was left half-edited. | Fixed |
| 6 | Lesson 13 | unclear | An outdated name for the glyceraldehyde-3-phosphate dehydrogenase step, and an unconditional claim that an electron acceptor "would not rescue" a glycolytic defect. | Renamed, and softened to "would be expected to do little" |

## Statements without a cited source

The package cites no papers. These values and statements are at textbook level and a reviewer should confirm
that each is acceptable as stated: typical pKa values of amino-acid groups and that they shift in proteins
(lesson 8); typical globular-protein stabilities of a few tens of kJ/mol and the dependence of the m-value on
exposed surface (lesson 9); the net glycolysis reaction, the adenylate kinase equilibrium constant near 1 and
the effectors of phosphofructokinase-1 (lesson 10); protons pumped per NADH and FADH₂, protons per ATP, the
range of 30 to 32 ATP per glucose, and an ATP pool of tens of grams (lesson 11); the time scales of the layers
of regulation (lesson 12); and, in lesson 13, that lactate/pyruvate tracks cytosolic NADH/NAD⁺ and that an
added electron acceptor such as pyruvate can partly relieve the redox block of a chain inhibitor.

## For a human reviewer

- Lesson 13 models the course case (a respiratory-chain inhibitor lowers ATP and raises lactate) with complete
  inhibition and fixed ATP yields. A biochemist should judge whether the discriminating readouts it names
  (oxygen consumption, lactate/pyruvate, a glucose tracer, an electron-acceptor rescue) are the right ones.
- The lab teaches the double-reciprocal fit mainly to show its weakness. Its means are rounded to two
  decimals and so look cleaner than real data. Check that the pedagogy is acceptable.
- Lesson 11 uses a single set of stoichiometries; sources differ, and the lesson says so.
- Prototype units 1 to 4 are still 60 to 80 words each, and their eight objectives are linked to no course
  outcome.

# Validation report

2026-10-05. Synthetic local data only. No instructor review, accreditation, semester equivalence, security or deployment certification is asserted.

## Baseline

Started unmodified reader in workspace dev container at port 4173. Browser checked first cell-biology item, saved a synthetic note and reloaded; result/note persisted and no browser errors appeared. Audit documents findings before code edits.

## Milestone 1

Commands run through the shared workspace development service (repository mounted at `/workspace/lattice-biomed-academy`):

```sh
python3 -m venv /tmp/courselab-check
/tmp/courselab-check/bin/pip install -r requirements-dev.txt
/tmp/courselab-check/bin/python tools/validate_content.py
/tmp/courselab-check/bin/python -m pytest tests/content -q
npm run test:legacy
node --check src/app.js
node --check src/state.js
node --check src/data/courses.js
```

Content authoring checks passed: 25 partial packages, 100 readings, 100 questions, 200 cards and 25 cases; zero errors. The 125 warnings are intentionally retained: 100 legacy-depth and 25 objective-coverage limitations. Integrated content adversity tests passed 34 tests in 70.06 seconds. State migration tests passed 4 tests. JavaScript syntax checks passed. The first intermediate validator run caught a robotics hint shorter than the schema minimum; the hint was expanded with provenance. An initial pytest invocation from the workspace directory failed to import `tools`; corrected commands run from the repository root.

Browser regression on the existing synthetic `localhost:4173` state confirmed the CourseLab identity, retained practice result and note, practice-only progress wording, and labelled navigation. No console warnings/errors appeared. Browser module caching required versioned asset URLs. No full accessibility certification is claimed.

Official-reference research opened the 22 preserved MIT comparators plus JHU/policy references. Automated live-link probing is separate from offline validation and its result will be recorded; no institutional material was imported.

## Outstanding definition-of-done checks

Complete Compose startup, enrollment/submission/feedback/grade/persistence, private-solution/bundle checks and full tests await milestone 2. Full-course gates, advanced grading, safe code runner, 14-week biology and actual human review are pending; roadmap lists remaining work.

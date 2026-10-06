# Current state audit

Audit date: 2026-10-05. Baseline: local commit `2669929`; remote previously populated through the GitHub contents API. This audit was written before application changes.

## Observed behavior

The unchanged site was started using the shared workspace development container:

```sh
# Historical command; replace <checkout> with the actual folder name.
docker compose run --rm -d -p 127.0.0.1:4173:4173 --name courselab-baseline dev python3 -m http.server 4173 --bind 0.0.0.0 --directory /workspace/<checkout>
```

Browser review showed 25 catalog entries, 100 short lessons, four suggested paths, 200 cards, and six equation calculators. Opening the first cell-biology lesson and selecting its correct option immediately changed progress to 1/4 and displayed the solution. A validation-only note and result persisted after reload on the separate `localhost:4173` test origin. No console warnings or errors appeared in that flow. There is no enrollment, login, server, gradebook, attempt timeline, or formal exam mode. The “Case studio” is saved prose with a learner checklist, not an autograded exam.

## Existing strengths

- Original explanatory notes, worked examples, targeted hints, cards, and integrative cases are useful teaching seeds.
- A consistent visual vocabulary, searchable domain catalog, pathways, and lesson navigation make disciplines approachable.
- Notes, bookmarks, card review dates, and practice results survive reload. Calculators expose formulas, units, and model assumptions.
- HTML text escaping protects current notes and text rendering against direct markup injection. Course links are explicit and the README already admits compact scope.

## Architecture limitations

`src/app.js` renders the whole application with string templates and delegated events. Educational prose, answer keys, references, and course metadata are combined in one JavaScript module. There are no schemas, content versions, migrations, dependency graph, server authorization, or automated checks. Client localStorage is the only persistence mechanism. Replacing the root DOM on navigation and grading loses focus. Historical local and remote Git histories differ; preserve both rather than force-pushing an unrelated root.

## Assessment limitations

One multiple-choice or numeric question per lesson is insufficient evidence of mastery. Correct answers and full solutions are shipped in `courses.js`; browser state and scores can be edited. A wrong first attempt exposes the solution. Numeric grading allows omitted units, compares supplied unit strings rather than dimensions/conversions, uses a default tolerance floor, and has no significant-figure rule. Only the latest response per item is retained, so “recent accuracy” is not an attempt-history metric. Cases are self-assessed. No partial credit, policy-controlled solution release, randomized variants, appeals, overrides, or server grade records exist. Never execute learner code inside this web process during migration.

## Content-depth limitations

All 25 packages contain four compact units and four formative items. These are **partial** course seeds. No package has a 14-week teaching sequence, substantive weekly homework, laboratory/data activities, a midterm, cumulative final, or independently reviewed course version. Displayed credit estimates and invented 20–35 minute lesson times do not substantiate course workload or transferable credit. Broad course names merge distinct engineering subjects that eventually require their own packages. No course qualifies as complete or externally reviewed. Existing text must be preserved while claims and labels are corrected.

The 100 notes total about 6,565 words (median 66 words per lesson); cell-biology has 292 words of explanatory notes plus 102 words of worked examples. Identified defects include a geometric-series tail calculation (correct tail 0.01), an E2 geometry option (typical anti-periplanar requirement), and ambiguous scaffold fractional-loss wording. Migration corrects these with history rather than inventing depth.

## Accessibility and security concerns

- At narrow widths, CSS hides navigation text while icons are `aria-hidden`, leaving primary buttons without accessible names.
- Tab semantics lack linked panels and keyboard behavior; the whole root is an `aria-live` region, and focus is discarded on rerender.
- Small 8–11 pixel teaching/interface text, muted contrast, missing skip link and reduced-motion rules need improvement and automated auditing.
- Local guest notes have no export/reset tools and storage is only shallowly validated. A malformed stored shape can break rendering.
- No backend currently exists, so server authentication/CSRF/password handling cannot be assessed. Future Markdown must be sanitized; assessment learner DTOs must exclude private specifications. Public repository answer specifications are open-source authoring resources, not secure secrets. A production operator needs separate private assessment storage.

## Migration risks and decisions

Retain course/module identifiers and preserve source teaching text. Introduce validated manifests and Markdown packages before replacing the reader. Label all migrated material partial and keep an explicit limitations list. Copy valid old guest state to a versioned uniStemCourseSimulators key with a retained local backup; imported client scores remain formative. Keep legacy assets outside the production frontend root after React migration. Validate source registry entries and separate software/content licenses before adapting third-party assets. Keep guest/auth data and answer specifications server-side, apply ownership checks, and use migrations for durable records. A code-runner interface may be disabled until a separately isolated worker meets the requested resource and network constraints.

## Validation boundary

This is a source and browser audit, not a qualified instructor review, accessibility certification, or a security penetration test. Future milestone results belong in `docs/VALIDATION_REPORT.md`. No reviewers, institutional approval, or semester equivalency are asserted.

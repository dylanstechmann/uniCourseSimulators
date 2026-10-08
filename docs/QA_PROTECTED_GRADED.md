# Browser QA of protected graded assignments

Written by an AI coding assistant on 2026-10-08, at the owner's request to test the protected, graded
mode automatically instead of by hand. This is functional QA in one browser on synthetic data. It is
not a security audit, a load test or a review of any course.

## What is tested

Every committed package is formative-only, so the normal stack has no protected graded work to test.
`tools/qa/build_protected_fixture.py` builds a throwaway deployment outside the repository: a copy of
`content/` in which genetics uses a `graded-course` policy with `assessment_protection: protected`,
plus three graded QA assignments whose questions and keys exist only in a private store
(`private://`). One assignment is open, one is past its deadline and one is not yet released. The
items are labelled QA fixtures, and every private solution contains a sentinel string,
`QA_PRIVATE_KEY_SENTINEL`, so a test can prove that no key reaches the learner.

`frontend/e2e/protected-graded.spec.ts` (Playwright, Chromium) then drives the real frontend and API:

1. A guest enrolls and opens the course's assessment plan, which states that answers are protected.
   The past-deadline and unreleased assignments cannot be opened.
2. The open assignment passes an automated accessibility scan (axe, WCAG 2.1 A and AA rules).
3. An incomplete submission is stopped in the browser and does not use an attempt.
4. Attempt 1 (wrong control, a number without its unit, an overclaim) scores 0 of 6 with the expected
   diagnoses ("incorrect result", "unit mistake", "incorrect selection").
5. Attempt 2 scores 6 of 6. The counter shows 2 of 2, the form closes, and the server refuses a third
   attempt (HTTP 409).
6. The course grade follows the stated policy: the never-submitted, past-deadline assignment counts as
   zero, so homework is (6 + 0) / 12 = 50%.
7. A human-review request on attempt 1 is saved and shown as open. Everything persists after a reload.
8. Submissions to the past-deadline and unreleased assignments, and questions for the unreleased one,
   are refused. The learner data export contains the graded attempts but no keys.
9. Throughout, no API response and no page text contains the sentinel, `solution_spec` or `private://`.

In the default CI run (Docker Compose), the spec is skipped, because it needs the QA fixture.

## How to run it

```bash
# Build only the fixture (writes nothing inside the repository)
python tools/qa/build_protected_fixture.py /tmp/courselab-qa

# Fixture, SQLite database, API, Vite dev server and the browser test in one go
PYTHON=/path/to/venv/bin/python FRONTEND_DIR=frontend tools/qa/run_protected_e2e.sh /tmp/courselab-qa
```

Prerequisites: a Python environment with `backend/requirements.txt`, `npm ci` in the frontend
directory, and Playwright's Chromium (`npx playwright install chromium`). Chromium also needs some
system libraries (`npx playwright install-deps chromium` installs them where you are allowed to
install packages). In the development container used on 2026-10-08, no system packages were
installed. The libraries were unpacked from Ubuntu packages into `~/.cache/chromium-libs` and passed
with `LD_LIBRARY_PATH`.

## Results on 2026-10-08 (this container, Python 3.12.3, Chromium headless shell 153)

The first run found three defects. All are fixed, and each fix has a regression test that fails
without it:

| Defect | Effect | Fix and test |
|---|---|---|
| The grade calculation re-checked protection without the pinned source paths | Every protected graded course answered 409 on its gradebook, which also hid the assessment plan and the assignment from learners | `backend/courselab/main.py` passes each pinned `source_path`; `test_protected_course_gradebook_counts_private_graded_work` |
| Graded submissions accepted only `[a-z0-9_-]` question ids, while content ids may contain `:` and `.` | An assignment written with the usual `lesson:slug` ids could never be submitted (HTTP 422) | `backend/courselab/schemas.py` uses the content-id grammar; `test_graded_assignment_accepts_authored_colon_and_dot_question_ids` |
| The assignment view did not count a just-saved attempt | The counter stayed at 0, and the form stayed open after the last allowed attempt until a reload (the server still refused the extra attempt) | `GradedAssessment.tsx` updates the count from the saved attempt; `GradedAssessment.test.tsx` |

After the fixes, both protected tests pass.

The existing browser suite (`learning-flow.spec.ts`) was also run locally against the committed
content through the Vite dev server: 19 passed, 2 skipped (the protected spec), 1 failed. The failure
is the check that the web server answers 404 for `/content`, `/legacy` and `/.env`. The nginx front
end in Docker Compose has those rules and the Vite dev server does not, so this is a difference
between test setups, not a product defect. CI runs that check against nginx.

## Observations for the owner (behavior left unchanged)

- Under the strict-deadline policy, a learner who enrolls after an assignment's deadline gets zero for
  it. That caused the 50% above. Excusing late enrollees, or setting deadlines per enrollment, would be
  a policy decision.
- After a graded attempt, learners see each item's hint and diagnosis. The solution text is never
  sent. If hints should stay hidden until the deadline, that would be a new setting.

## Not covered

- The Docker Compose and nginx production stack with a protected course (CI cannot provide the
  private store without a workflow change).
- An instructor resolving a graded review request in the browser. Backend tests cover that API,
  including auditing and the block on reviewing one's own submission.
- Other browsers, phone layouts, many concurrent learners, and security testing beyond the leak
  checks above.

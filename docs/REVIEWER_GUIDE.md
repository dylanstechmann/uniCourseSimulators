# Reviewing a course package

This repository is a personal hobby and learning project. Most of its teaching text, practice items
and code were written with substantial help from AI coding assistants. Every course package is
labelled `partial` and unreviewed. All data in the newer lessons is synthetic (made up for teaching).
Nothing here confers credit. This guide explains how someone can help check it, and what each kind of
check can and cannot change.

## Three kinds of review

| Kind | Who can do it | What it checks | What it can change |
|---|---|---|---|
| Reader feedback | Anyone: friends, relatives, students, curious readers | Confusing explanations, missing steps, typos, items that seem wrong, pages or buttons that misbehave | The reported problems get fixed. Labels stay as they are. |
| AI-assisted check | AI tools run by the owner or a coding agent | Recomputes every numerical answer from the data stated in the item; checks units, rounding and internal consistency; finds stale or contradictory text; runs the wording scan | A dated record under [reviews/ai-assisted](reviews/ai-assisted/), plus fixes. It never counts as human review and changes no label. |
| Subject-matter review | Someone qualified in the subject: for example, a university instructor, a graduate student or researcher in the field, or a freelancer with a relevant degree and teaching experience | Scientific correctness, reasoning and causal claims, controls and uncertainty, whether items test what the objectives say, whether keys and tolerances are fair, prerequisites and scope | A named review record for the exact version reviewed. Together with every other gate in the [content quality standard](CONTENT_QUALITY_STANDARD.md), it is needed before a package can move past `partial`. |

AI-assisted checks catch arithmetic, consistency and staleness problems cheaply, so it is worth
running one before asking a person for their time. They are not independent: the same kind of system
wrote most of the content, and it can share the same blind spots. The repository's standard therefore
requires actual human review for `complete` and named, qualified, independent review for
`externally reviewed`.

## Reader feedback (about 10 minutes)

Open a lesson in the app or on GitHub, read it, try its practice items, and write down anything that
confused you, with the course, lesson title and a sentence or two. Send it to the owner, or open an
issue on GitHub with the "Course feedback" form. You do not need to be an expert. "I could not follow
step 2" is useful.

## Subject-matter review of one lesson (about 30 to 60 minutes)

1. Note the package version from the syllabus (for example, "Genetics & Genomics, version 0.4.1").
2. Read the lesson once straight through.
3. Answer its practice items yourself before looking at the keys (they are in the package's
   `question-banks/practice.json`). Then compare.
4. Check the worked example step by step.
5. For each problem you find, record where it is (lesson, section or item id), what is wrong, and how
   serious it is:
   - **error**: a wrong fact, number, key or conclusion;
   - **misleading**: true but likely to give a wrong impression, or overclaimed;
   - **unclear**: hard to follow, or missing a step;
   - **suggestion**: a better example, source or order.
6. Say what you did not check (for example, "did not check the references" or "items 4 to 6 only").

A copyable form is in [review-templates/lesson-review.md](review-templates/lesson-review.md).

## How a subject-matter review is recorded

- The reviewer's notes go in the package as `reviews/<date>-<reviewer>.md`. They state the reviewer's
  name (or an agreed public identifier), the qualification as the reviewer describes it, the version
  and lessons reviewed, the method, the findings, anything left unresolved, and any conflict of
  interest. Reviewers decide whether their name may be public. Nothing is recorded without their
  agreement.
- The owner adds the reviewer to the package's `course.json` under `review.reviewers` and sets
  `review.reviewed_version`. Use status `internal` for someone involved in the project (including the
  owner) and `external` only for a qualified reviewer independent of it. The validator rejects
  reviewers on an unreviewed package and requires the evidence file.
- Unresolved errors block any maturity change. A later content change means the review covers the old
  version only, so the version number matters.

## Practical notes for paid or university reviewers

- Agree on a fixed scope (for example, "lessons 5 to 9 of genetics, version 0.4.1") and a written
  report as the deliverable.
- A content review needs only the public repository. It needs no account, password or private
  assessment key. If a protected graded assignment ever needs review, its key file is shared
  privately and never committed or pasted into an issue.
- The lessons include synthetic data on purpose. A reviewer should judge whether a synthetic example
  is plausible and labelled, not look for its source.

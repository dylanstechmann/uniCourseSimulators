#!/usr/bin/env python3
"""Build a throwaway graded, protected copy of one course package for end-to-end QA.

Copies ``content/`` to ``<out>/content``, switches one package (default: genetics) to a
``graded-course`` policy with ``assessment_protection: protected`` and adds three graded QA
assignments whose questions and keys exist only in ``<out>/private`` (the ``private://`` store):
one open, one past its deadline and one not yet released. The items are synthetic QA fixtures,
not course assessments; every private solution contains ``QA_PRIVATE_KEY_SENTINEL`` so a browser
test can prove the key never reaches the learner. Nothing is written inside the repository, and
the committed packages stay formative-only.

    python tools/qa/build_protected_fixture.py /tmp/courselab-qa
    # then run the API with CONTENT_ROOT=/tmp/courselab-qa/content and
    # PRIVATE_ASSESSMENTS_ROOT=/tmp/courselab-qa/private (see docs/QA_PROTECTED_GRADED.md)
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SENTINEL = "QA_PRIVATE_KEY_SENTINEL"
GRADING_POLICY = {
    "mode": "graded-course",
    "assessment_protection": "protected",
    "categories": [{"id": "homework", "title": "Homework", "weight": 1.0}],
    "category_aggregation": "points",
    "late_submission_policy": "strict-deadline",
    "attempt_policy": "QA fixture: two attempts per assignment; the highest score counts.",
    "solution_release": "QA fixture: solutions are never released.",
    "late_policy": "QA fixture: no late work is accepted after the deadline.",
    "appeals": "QA fixture: one human review request per saved attempt.",
}


def qa_questions(lesson: str, prefix: str) -> list[dict]:
    def item(slug, objective, body):
        return {
            "id": f"{prefix}:{slug}",
            "points": 2,
            "objective_ids": [f"{lesson}-objective-{objective}"],
            "visibility": "restricted-server-assessment",
            "provenance": {"kind": "original", "modifications": []},
            **body,
        }

    return [
        item("control-choice", 1, {
            "type": "single_choice",
            "prompt": f"QA fixture item for {prefix}. A knockdown experiment compares cells given a targeting guide with untreated "
                      "cells. Which added comparison best isolates the effect of losing the targeted gene?",
            "options": [
                "A second untreated culture grown on another day.",
                "Cells given a non-targeting guide delivered the same way.",
                "Cells given twice the amount of the targeting guide.",
                "No added comparison is needed when the effect is large.",
            ],
            "solution_spec": {"answer": 1},
            "feedback": {
                "hint": "Which comparison keeps delivery identical but removes the specific target?",
                "solution": f"{SENTINEL}: the non-targeting guide controls for delivery and handling.",
                "lesson_ids": [lesson], "misconception_ids": [],
            },
        }),
        item("knockdown-percent", 2, {
            "type": "numeric",
            "prompt": f"QA fixture item for {prefix}. In a synthetic qPCR run the target's ΔCt (target minus reference) is 3.0 in "
                      "control cells and 5.0 in knockdown cells. Assuming perfect amplification efficiency, by what "
                      "percentage is the target's expression reduced? Enter a value with the unit %.",
            "solution_spec": {
                "answer": 75, "unit": "%", "tolerance": 0.5, "unit_required": True,
                "significant_figures": None, "dimensions": None,
            },
            "feedback": {
                "hint": "Compute ΔΔCt, convert it to a fold change with 2 to the power of minus ΔΔCt, then to a reduction.",
                "solution": f"{SENTINEL}: ΔΔCt = 2.0, fold change 0.25, so expression is reduced by 75 %.",
                "lesson_ids": [lesson], "misconception_ids": [],
            },
        }),
        item("supported-claims", 1, {
            "type": "multiple_select",
            "prompt": f"QA fixture item for {prefix}. In synthetic data a knockdown lowers the target transcript by 80% and slows "
                      "wound closure, and a rescue construct restores closure. Which conclusions are supported? "
                      "Select all that apply.",
            "options": [
                "The closure phenotype depends on loss of the target in this cell system.",
                "The rescue argues against an off-target explanation.",
                "The gene causes slow wound healing in people.",
                "The knockdown removed all of the target protein.",
            ],
            "solution_spec": {"answer": [0, 1], "partial_credit": "correct-minus-incorrect-clamped-v1"},
            "feedback": {
                "hint": "Separate what the cell experiment shows from claims about people or about protein levels.",
                "solution": f"{SENTINEL}: options 1 and 2 are supported; the others go beyond the data.",
                "lesson_ids": [lesson], "misconception_ids": [],
            },
        }),
    ]


def build(out: Path, course_id: str, lesson: str) -> dict:
    out = out.resolve()
    if out == ROOT or ROOT in out.parents:
        raise SystemExit("The QA fixture must be written outside the repository.")
    if out.exists():
        shutil.rmtree(out)
    shutil.copytree(ROOT / "content", out / "content")
    manifest_path = out / "content" / "courses" / course_id / "course.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    links = {item["id"]: item.get("course_outcome_ids", []) for item in manifest["lesson_objectives"]}
    schedules = {
        "qa-protected-open": ("QA protected homework (open)", "2020-01-01T00:00:00Z", "2099-01-01T00:00:00Z"),
        "qa-protected-closed": ("QA protected homework (past deadline)", "2020-01-01T00:00:00Z", "2020-06-01T00:00:00Z"),
        "qa-protected-scheduled": ("QA protected homework (not yet released)", "2099-01-01T00:00:00Z", "2099-06-01T00:00:00Z"),
    }
    for assessment_id, (title, release_at, due_at) in schedules.items():
        questions = qa_questions(lesson, assessment_id)
        objectives = list(dict.fromkeys(oid for question in questions for oid in question["objective_ids"]))
        outcomes = [item["id"] for item in manifest["outcomes"] if any(item["id"] in links[o] for o in objectives)]
        key_file = out / "private" / "courses" / course_id / "assignments" / f"{assessment_id}.json"
        key_file.parent.mkdir(parents=True, exist_ok=True)
        key_file.write_text(json.dumps({
            "schema_version": "1.0", "course_id": course_id,
            "license": "QA fixture only; never serve to learners",
            "questions": questions,
        }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        manifest["assessments"].append({
            "id": assessment_id, "type": "homework", "mode": "graded", "title": title,
            "path": f"private://assignments/{assessment_id}.json",
            "objective_ids": objectives + outcomes,
            "question_ids": [question["id"] for question in questions],
            "points": sum(question["points"] for question in questions),
            "category_id": "homework", "week": 1,
            "release_at": release_at, "due_at": due_at,
            "attempt_limit": 2, "attempt_scoring": "highest",
        })
    manifest["grading_policy"] = GRADING_POLICY
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return {"content_root": str(out / "content"), "private_root": str(out / "private"), "course_id": course_id,
            "assessments": list(schedules), "sentinel": SENTINEL}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("out", type=Path, help="directory outside the repository; replaced if it exists")
    parser.add_argument("--course", default="genetics")
    parser.add_argument("--lesson", default="genetics-8", help="lesson whose objectives the QA items are tagged to")
    args = parser.parse_args(argv)
    json.dump(build(args.out, args.course, args.lesson), sys.stdout, indent=2)
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Verify deployed learner DTOs and supported practice specs without publishing keys.

This is an integration check, not an independent mathematical recalculation or
a complete-course content quality gate. The root content validator owns those.
"""

import argparse
from pathlib import Path

from .content import ContentRepository
from .grading import grade
from .schemas import AttemptRequest
from .variants import resolve_variant, variant_ids


def learner_keys(value):
    if isinstance(value, dict):
        assert not {"solution_spec", "answer", "solution"}.intersection(value)
        for item in value.values():
            learner_keys(item)
    elif isinstance(value, list):
        for item in value:
            learner_keys(item)


def check(root: Path) -> tuple[int, int]:
    repo = ContentRepository(root)
    count = 0
    catalog = repo.catalog()
    for summary in catalog:
        detail = repo.course(summary.id)
        learner_keys(detail.model_dump())
        for module in detail.modules:
            for lesson in module.lessons:
                learner_keys(repo.lesson(summary.id, lesson.id).model_dump())
        for question in repo.questions(summary.id):
            for variant_id in variant_ids(question) or [None]:
                resolved = resolve_variant(question, variant_id)
                spec = resolved["solution_spec"]
                result = grade(resolved, AttemptRequest(response=spec["answer"], unit=spec.get("unit")))
                assert result.correct, (
                    f"Practice specification not gradeable: {summary.id}/{question['id']}/{variant_id}"
                )
                learner_keys(result.model_dump())
                count += 1
    return len(catalog), count


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path)
    args = parser.parse_args()
    packages, questions = check(args.root)
    print(f"Learner integration check passed: {packages} course packages and {questions} supported practice specifications.")

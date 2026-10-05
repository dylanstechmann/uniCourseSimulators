"""Read authoring packages on the server, publish only explicit learner DTOs.

The legacy practice specifications are intentionally open authoring resources.
They are not restricted production examinations. They still never ship as a
frontend static asset or through a learner content response.
"""

import json
import re
from collections.abc import Callable
from pathlib import Path

from .schemas import (
    CourseSummary,
    LessonSummary,
    ModuleSummary,
    Objective,
    Prerequisites,
    PublicCourse,
    PublicLesson,
    PublicQuestion,
)


class ContentMissing(LookupError):
    pass


class ContentInvalid(ValueError):
    pass


class ContentRepository:
    def __init__(self, root: Path):
        self.root = root.resolve()

    def _file(self, course_id: str, relative: str) -> Path:
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", course_id):
            raise ContentMissing("Course not found")
        directory = (self.root / "courses" / course_id).resolve()
        course_root = (self.root / "courses").resolve()
        if not directory.is_relative_to(course_root):
            raise ContentInvalid("Unsafe content directory")
        candidate = (directory / relative).resolve()
        if not candidate.is_relative_to(directory):
            raise ContentInvalid("Unsafe content reference")
        if not candidate.is_file():
            raise ContentMissing("Content not found")
        return candidate

    def manifest(self, course_id: str) -> dict:
        item = json.loads(self._file(course_id, "course.json").read_text(encoding="utf-8"))
        if item.get("id") != course_id:
            raise ContentInvalid("Manifest ID mismatch")
        return item

    def _read(self, course_id: str, relative: str) -> str:
        return self._file(course_id, relative).read_text(encoding="utf-8")

    def _summary(self, manifest: dict) -> CourseSummary:
        return CourseSummary(
            **{name: manifest[name] for name in (
                "id", "title", "description", "domain", "level", "maturity", "version", "limitations"
            )},
            lesson_count=sum(len(module["lessons"]) for module in manifest["modules"]),
        )

    def catalog(self) -> list[CourseSummary]:
        items = []
        for path in sorted((self.root / "courses").glob("*/course.json")):
            items.append(self._summary(self.manifest(path.parent.name)))
        return items

    def sources(self) -> list[dict]:
        registry = self.root / "sources" / "registry.json"
        if not registry.is_file():
            return []
        data = json.loads(registry.read_text(encoding="utf-8"))
        entries = data if isinstance(data, list) else data.get("sources", [])
        return [{key: entry.get(key) for key in ("id", "title", "url", "institution", "license")}
                for entry in entries]

    def course(self, course_id: str) -> PublicCourse:
        manifest = self.manifest(course_id)
        modules = [ModuleSummary(
            id=module["id"], title=module["title"], source_ids=module.get("source_ids", []),
            lessons=[LessonSummary(id=lesson["id"], title=lesson["title"],
                                   learning_objective_ids=lesson.get("objectives", []))
                     for lesson in module["lessons"]],
        ) for module in manifest["modules"]]
        return PublicCourse(
            **self._summary(manifest).model_dump(),
            prerequisites=Prerequisites.model_validate(manifest["prerequisites"]),
            outcomes=[Objective.model_validate(item) for item in manifest["outcomes"]],
            lesson_objectives=[Objective.model_validate(item) for item in manifest.get("lesson_objectives", [])],
            modules=modules, syllabus_markdown=self._read(course_id, manifest["syllabus"]),
            license=manifest["license"], review_status=manifest["review"]["status"],
        )

    def lesson_record(self, course_id: str, lesson_id: str) -> tuple[dict, dict]:
        for module in self.manifest(course_id)["modules"]:
            for lesson in module["lessons"]:
                if lesson["id"] == lesson_id:
                    return module, lesson
        raise ContentMissing("Lesson not found")

    def questions(self, course_id: str) -> list[dict]:
        package = json.loads(self._read(course_id, "question-banks/practice.json"))
        if package.get("course_id") != course_id:
            raise ContentInvalid("Question-bank course mismatch")
        # Fail closed: the unrestricted retry route only serves the explicitly
        # public seed practice bank. Restricted/untagged records are not gradeable
        # or readable through this repository interface.
        return [question for question in package["questions"]
                if question.get("visibility") == "public-practice-authoring"]

    def question(self, course_id: str, question_id: str) -> dict:
        for item in self.questions(course_id):
            if item["id"] == question_id:
                return item
        raise ContentMissing("Question not found")

    def public_question(
        self, question: dict, variant_id: str | None = None, variant_token: str | None = None
    ) -> PublicQuestion:
        """Build a whitelisted learner DTO; never return the authored grader spec."""
        return PublicQuestion(
            id=question["id"], type=question["type"], prompt=question["prompt"],
            options=question.get("options", []), unit=question.get("solution_spec", {}).get("unit"),
            significant_figures=question.get("solution_spec", {}).get("significant_figures"),
            points=question.get("points", 1), learning_objective_ids=question.get("objective_ids", []),
            selection="multiple" if question["type"] == "multiple_select" else "single",
            partial_credit_policy=(question.get("solution_spec", {}).get("partial_credit")
                                   if question["type"] == "multiple_select" else None),
            variant_id=variant_id, variant_token=variant_token,
        )

    def lesson(
        self, course_id: str, lesson_id: str,
        public_question_factory: Callable[[dict], PublicQuestion] | None = None,
    ) -> PublicLesson:
        module, lesson = self.lesson_record(course_id, lesson_id)
        available = {question["id"]: question for question in self.questions(course_id)}
        questions = [available[question_id] for question_id in lesson.get("question_ids", [])
                     if question_id in available]
        return PublicLesson(
            id=lesson["id"], title=lesson["title"], markdown=self._read(course_id, lesson["reading"]),
            learning_objective_ids=lesson.get("objectives", []), worked_example=lesson.get("worked_example"),
            source_ids=module.get("source_ids", []),
            questions=[public_question_factory(question) if public_question_factory else
                       self.public_question(question, "base" if question.get("randomization") else None)
                       for question in questions],
        )

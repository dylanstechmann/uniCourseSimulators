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
    PublicCurriculum,
    PublicLesson,
    PublicQuestion,
    PublicRetrievalCard,
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

    def assessment_source_file(self, course_id: str, relative: str) -> Path:
        """Resolve a manifest assessment source under its course package."""
        return self._file(course_id, relative)

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

    def curriculum(self) -> PublicCurriculum:
        """Return a prerequisite/pathway map with explicit course maturity."""
        map_path = self.root / "curriculum-map.json"
        if not map_path.is_file():
            raise ContentInvalid("Curriculum map is unavailable")
        source = json.loads(map_path.read_text(encoding="utf-8"))
        nodes = []
        for path in sorted((self.root / "courses").glob("*/course.json")):
            manifest = self.manifest(path.parent.name)
            nodes.append({
                "id": manifest["id"], "title": manifest["title"],
                "domain": manifest["domain"], "level": manifest["level"],
                "maturity": manifest["maturity"], "description": manifest["description"],
                "prerequisites": manifest["prerequisites"], "package_id": manifest["id"],
                "related_package_ids": [], "relation_note": None,
            })
        for item in source["catalog_only"]:
            nodes.append({
                **item, "package_id": None,
            })
        return PublicCurriculum(
            schema_version=source["schema_version"], description=source["description"],
            nodes=nodes, pathways=source["pathways"], alignment_maps=source["alignment_maps"],
        )

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

    def retrieval_cards(self, course_id: str, lesson_id: str) -> list[PublicRetrievalCard]:
        """Publish only the learner-facing fields for cards assigned to this lesson."""
        manifest = self.manifest(course_id)
        package = json.loads(self._read(course_id, manifest["retrieval_cards"]))
        if package.get("course_id") != course_id:
            raise ContentInvalid("Retrieval-card course mismatch")
        _, lesson = self.lesson_record(course_id, lesson_id)
        cards_by_id = {}
        for card in package["cards"]:
            if card["id"] in cards_by_id:
                raise ContentInvalid("Retrieval-card IDs must be unique")
            cards_by_id[card["id"]] = card
        selected = []
        for card_id in lesson.get("card_ids", []):
            card = cards_by_id.get(card_id)
            if card is None or card.get("lesson_id") != lesson_id:
                raise ContentInvalid("Lesson retrieval-card reference is invalid")
            selected.append(PublicRetrievalCard(
                id=card["id"], front=card["front"], back=card["back"],
                learning_objective_ids=card.get("objective_ids", []),
            ))
        return selected

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
            response_fields=[
                {
                    "id": field["id"], "type": field["type"], "prompt": field["prompt"],
                    "options": field.get("options", []), "unit": field.get("unit"),
                    "points": field["points"],
                }
                for field in question.get("response_fields", [])
            ],
            graph_spec=(
                {
                    "x_axis": {
                        "label": question["graph_spec"]["x_axis"]["label"],
                        "minimum": question["graph_spec"]["x_axis"]["minimum"],
                        "maximum": question["graph_spec"]["x_axis"]["maximum"],
                    },
                    "y_axis": {
                        "label": question["graph_spec"]["y_axis"]["label"],
                        "minimum": question["graph_spec"]["y_axis"]["minimum"],
                        "maximum": question["graph_spec"]["y_axis"]["maximum"],
                    },
                    "points": [
                        {"id": point["id"], "label": point["label"]}
                        for point in question["graph_spec"]["points"]
                    ],
                    "observations": [
                        {
                            "id": observation["id"],
                            "x": observation["x"],
                            "values": observation["values"],
                        }
                        for observation in question["graph_spec"]["observations"]
                    ],
                }
                if question["type"] == "graph" else None
            ),
            accepted_media_types=(
                question.get("solution_spec", {}).get("accepted_media_types", [])
                if question["type"] == "file_upload" else []
            ),
            max_upload_bytes=(
                question.get("solution_spec", {}).get("max_bytes")
                if question["type"] == "file_upload" else None
            ),
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
            retrieval_cards=self.retrieval_cards(course_id, lesson["id"]),
            questions=[public_question_factory(question) if public_question_factory else
                       self.public_question(question, "base" if question.get("randomization") else None)
                       for question in questions],
        )

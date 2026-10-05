import { render, screen, within } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import type { Attempt, Course, Gradebook } from "../types";
import { GradebookView } from "./GradebookView";

describe("practice gradebook API contract", () => {
  it("renders a scalar limitations notice and persisted attempt evidence", () => {
    const gradebook: Gradebook = {
      course_id: "cell-biology",
      assessment_role: "formative",
      aggregation: "best practice result per question",
      score: 1,
      max_score: 4,
      attempt_count: 1,
      objective_evidence_policy: {
        version: "practice-evidence-v1",
        minimum_distinct_items: 3,
        minimum_item_coverage: 0.8,
        minimum_performance: 0.8,
      },
      objective_evidence: {
        "cell-biology-lo-1": {
          attempts: 1,
          correct_results: 1,
          attempted_items: 1,
          item_count: 3,
          best_score: 1,
          best_possible_score: 1,
          performance: 1,
          status: "insufficient_evidence",
        },
      },
      limitations:
        "Practice results do not establish reasoning, mastery, or course completion.",
    };
    const course: Course = {
      id: "cell-biology",
      title: "Foundations of Cell and Molecular Biology",
      description: "Reason about cell experiments.",
      domain: "Life sciences",
      level: "Year 1",
      maturity: "partial",
      version: "0.1",
      lesson_count: 4,
      limitations: ["This partial package is not a semester course."],
      prerequisites: {
        course_ids: [],
        recommended_course_ids: [],
        concurrent_course_ids: [],
        knowledge: [],
        statement: "Review basic molecular structure.",
      },
      outcomes: [
        {
          id: "cell-biology-lo-1",
          description: "Relate macromolecular structure to function.",
          bloom: "analyze",
        },
      ],
      lesson_objectives: [],
      modules: [],
      syllabus_markdown: "Original partial syllabus.",
      license: "CC-BY-4.0",
      review_status: {},
      assessment_policy: {},
    };
    const attempt: Attempt = {
      id: "attempt-1",
      course_id: "cell-biology",
      question_id: "cell-biology-q-1",
      content_version: "0.1",
      response: { response: 0, variant_id: "surface-residue-substitution" },
      score: 1,
      max_score: 1,
      result: {
        score: 1,
        max_score: 1,
        correct: true,
        assessment_role: "formative",
        grading_policy_version: "practice-v1",
        feedback: {
          diagnosis: "correct_result_reasoning_not_assessed",
          hint: "Identify the interaction that changes.",
          misconception: null,
          next_step: "Explain the mechanism using the lesson.",
          lesson_id: "cell-biology-1",
          reasoning_assessed: false,
          provisional: false,
        },
      },
      objective_ids: ["cell-biology-lo-1"],
      created_at: "2026-10-05T12:00:00Z",
    };
    render(
      <GradebookView
        gradebook={gradebook}
        course={course}
        attempts={[attempt]}
      />,
    );
    expect(screen.getByText(gradebook.limitations)).toBeInTheDocument();
    expect(screen.getByText("1 / 4 practice points")).toBeInTheDocument();
    const evidenceTable = screen.getAllByRole("table")[0];
    expect(
      within(evidenceTable).getByRole("rowheader", {
        name: "Relate macromolecular structure to function.",
      }),
    ).toBeInTheDocument();
    expect(within(evidenceTable).getByText("1 / 3")).toBeInTheDocument();
    expect(
      within(evidenceTable).getByText("insufficient evidence"),
    ).toBeInTheDocument();
    expect(screen.getByText(/at least 3 distinct items/)).toBeInTheDocument();
    const attemptsTable = screen.getAllByRole("table")[1];
    expect(within(attemptsTable).getAllByRole("row")).toHaveLength(2);
    expect(
      within(attemptsTable).getByRole("rowheader", {
        name: /Variant: surface-residue-substitution/,
      }),
    ).toBeInTheDocument();
    expect(
      within(attemptsTable).getByText("Feedback details"),
    ).toBeInTheDocument();
    expect(
      within(attemptsTable).getByRole("link", {
        name: "Review lesson and feedback",
      }),
    ).toHaveAttribute("href", "#/course/cell-biology/lesson/cell-biology-1");
    expect(
      screen.getByText(/not a course grade, mastery certification/),
    ).toBeInTheDocument();
  });
});

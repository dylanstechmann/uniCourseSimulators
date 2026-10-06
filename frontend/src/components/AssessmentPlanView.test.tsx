import { render, screen, within } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import type { AssessmentPlan } from "../types";
import { AssessmentPlanView } from "./AssessmentPlanView";

describe("versioned assessment plan", () => {
  it("keeps formative practice separate from a course grade", () => {
    const plan: AssessmentPlan = {
      course_id: "cell-biology",
      content_version: "0.3.2",
      grading_mode: "formative-only",
      course_grade_status: "not_configured",
      categories: [],
      category_aggregation: "points",
      attempt_policy: "Practice retries are unlimited.",
      solution_release: "After an attempt.",
      late_policy: "There are no course deadlines.",
      appeals: "Request human review of a saved practice attempt.",
      assessments: [
        {
          id: "week-one-practice",
          title: "Molecular structure practice",
          type: "practice",
          mode: "practice",
          category_id: null,
          week: 1,
          points: 4,
          item_count: 2,
          objective_count: 1,
          release_at: null,
          due_at: null,
          attempt_limit: null,
          attempt_scoring: "highest",
          schedule_status: "practice",
        },
      ],
    };
    render(<AssessmentPlanView plan={plan} />);
    expect(
      screen.getByRole("heading", { name: "Course assessment plan" }),
    ).toBeTruthy();
    expect(screen.getByText(/No course grade is configured/)).toBeTruthy();
    expect(screen.getByText("Molecular structure practice")).toBeTruthy();
    const table = screen.getByRole("table");
    expect(
      within(table).getByRole("columnheader", { name: "Due" }),
    ).toBeTruthy();
    expect(
      within(table).getAllByRole("cell", { name: "practice" }),
    ).toHaveLength(2);
  });
});

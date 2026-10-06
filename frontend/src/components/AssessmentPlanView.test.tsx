import { fireEvent, render, screen, within } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
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
    const onOpenPractice = vi.fn();
    render(<AssessmentPlanView plan={plan} onOpenPractice={onOpenPractice} />);
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
    fireEvent.click(screen.getByRole("button", { name: "Open practice set" }));
    expect(onOpenPractice).toHaveBeenCalledWith("week-one-practice");
  });

  it("opens an available graded activity from its versioned schedule", () => {
    const plan: AssessmentPlan = {
      course_id: "fixture-course",
      content_version: "0.2.0",
      grading_mode: "graded-course",
      course_grade_status: "configured_no_submissions",
      categories: [{ id: "homework", title: "Homework", weight: 1 }],
      category_aggregation: "points",
      attempt_policy: "Two attempts; highest score counts.",
      solution_release: "After the due time.",
      late_policy: "No late work.",
      appeals: "Request manual review.",
      assessments: [
        {
          id: "homework-1",
          title: "Control analysis",
          type: "homework",
          mode: "graded",
          category_id: "homework",
          week: 1,
          points: 2,
          item_count: 1,
          objective_count: 1,
          release_at: null,
          due_at: null,
          attempt_limit: 2,
          attempt_scoring: "highest",
          schedule_status: "open",
        },
      ],
    };
    const onOpen = vi.fn();
    render(<AssessmentPlanView plan={plan} onOpenAssessment={onOpen} />);
    fireEvent.click(screen.getByRole("button", { name: "Open assignment" }));
    expect(onOpen).toHaveBeenCalledWith("homework-1");
    expect(
      screen.getByText(/no graded submissions are saved yet/i),
    ).toBeInTheDocument();
  });
});

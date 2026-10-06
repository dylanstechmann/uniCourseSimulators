import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { beforeEach, describe, expect, it, vi } from "vitest";
import { api } from "../api";
import type { Attempt, PracticeAssessment } from "../types";
import { PracticeAssessmentView } from "./PracticeAssessmentView";

vi.mock("../api", () => ({
  api: { practiceAssessment: vi.fn() },
  errorMessage: (error: unknown) =>
    error instanceof Error ? error.message : "Request failed",
}));

const practiceSet: PracticeAssessment = {
  course_id: "cell-biology",
  assessment_id: "week-8-review",
  title: "Week 8 cumulative review practice (ungraded; not a midterm)",
  content_version: "0.9.1",
  points: 1,
  questions: [
    {
      id: "control-check",
      type: "single_choice",
      prompt: "Which comparison is the matched vehicle control?",
      options: ["Vehicle", "Active compound"],
      points: 1,
      learning_objective_ids: ["controls"],
      assessment_role: "formative",
    },
  ],
};

const attempt: Attempt = {
  id: "attempt-1",
  course_id: "cell-biology",
  question_id: "control-check",
  content_version: "0.9.1",
  response: { response: 0 },
  score: 1,
  effective_score: 1,
  max_score: 1,
  appeal: null,
  result: {
    score: 1,
    max_score: 1,
    correct: true,
    assessment_role: "formative",
    grading_policy_version: "practice-v1",
    feedback: {
      diagnosis: "correct_result_reasoning_not_assessed",
      next_step: "Explain which conditions the vehicle controls.",
      lesson_id: "cell-biology-4",
      reasoning_assessed: false,
      misconception: null,
      provisional: false,
    },
  },
  objective_ids: ["controls"],
  created_at: "2026-10-06T12:00:00Z",
};

describe("public cumulative practice set", () => {
  beforeEach(() => {
    vi.mocked(api.practiceAssessment).mockResolvedValue(practiceSet);
  });

  it("loads answer-free questions and saves a formative attempt with feedback", async () => {
    const onSubmit = vi.fn().mockResolvedValue(attempt);
    render(
      <PracticeAssessmentView
        courseId="cell-biology"
        assessmentId="week-8-review"
        enabled
        attempts={[]}
        onSubmit={onSubmit}
        onAppeal={vi.fn()}
        onClose={vi.fn()}
      />,
    );
    const user = userEvent.setup();
    expect(
      await screen.findByRole("heading", {
        name: "Week 8 cumulative review practice (ungraded; not a midterm)",
      }),
    ).toBeTruthy();
    expect(
      screen.getByText(/not a midterm or other summative exam/i),
    ).toBeTruthy();
    await user.click(screen.getByRole("radio", { name: "Vehicle" }));
    await user.click(
      screen.getByRole("button", { name: "Submit practice response" }),
    );
    expect(onSubmit).toHaveBeenCalledWith(
      "control-check",
      0,
      undefined,
      undefined,
    );
    expect(
      await screen.findByText(
        "Correct result. Reasoning has not been assessed.",
      ),
    ).toBeTruthy();
  });
});

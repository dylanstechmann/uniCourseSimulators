import { render, screen, waitFor } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { beforeEach, describe, expect, it, vi } from "vitest";
import { api } from "../api";
import type {
  GradedAssessment as GradedAssessmentData,
  GradedSubmission,
} from "../types";
import { GradedAssessment } from "./GradedAssessment";

vi.mock("../api", () => ({
  api: {
    gradedAssessment: vi.fn(),
    submitGradedAssessment: vi.fn(),
  },
  errorMessage: (error: unknown) =>
    error instanceof Error ? error.message : "Request failed",
}));

const assessment: GradedAssessmentData = {
  course_id: "fixture-course",
  assessment_id: "homework-1",
  title: "Control analysis",
  content_version: "0.1.0",
  points: 2,
  attempts_used: 0,
  attempt_limit: 2,
  schedule_status: "open",
  questions: [
    {
      id: "choice",
      type: "single_choice",
      prompt: "Select the matched control.",
      options: ["Vehicle", "Active drug"],
      points: 2,
      learning_objective_ids: ["objective"],
      assessment_role: "graded",
    },
  ],
};

const submission: GradedSubmission = {
  id: "submission-1",
  course_id: "fixture-course",
  assessment_id: "homework-1",
  content_version: "0.1.0",
  attempt_number: 1,
  responses: { choice: { response: 0 } },
  results: [
    {
      question_id: "choice",
      score: 2,
      max_score: 2,
      feedback: {
        diagnosis: "correct_result_reasoning_not_assessed",
        hint: "Match the delivery conditions.",
        misconception: null,
        next_step: "Review the matched-control example.",
        lesson_id: "lesson-one",
        reasoning_assessed: false,
        provisional: false,
      },
    },
  ],
  score: 2,
  max_score: 2,
  score_percent: 100,
  submitted_at: "2026-10-06T12:00:00Z",
};

describe("graded assignment submission", () => {
  beforeEach(() => vi.clearAllMocks());

  it("loads safe questions and shows persisted deterministic feedback", async () => {
    vi.mocked(api.gradedAssessment).mockResolvedValue(assessment);
    vi.mocked(api.submitGradedAssessment).mockResolvedValue(submission);
    const onSubmitted = vi.fn(async () => undefined);
    const user = userEvent.setup();
    render(
      <GradedAssessment
        courseId="fixture-course"
        assessmentId="homework-1"
        enabled
        history={[]}
        onSubmitted={onSubmitted}
      />,
    );

    await screen.findByText("Select the matched control.");
    await user.click(screen.getByRole("radio", { name: "Vehicle" }));
    await user.click(screen.getByRole("button", { name: "Submit assignment" }));

    await waitFor(() =>
      expect(api.submitGradedAssessment).toHaveBeenCalledWith(
        "fixture-course",
        "homework-1",
        { choice: { response: 0 } },
      ),
    );
    expect(onSubmitted).toHaveBeenCalledWith(submission);
    expect(
      await screen.findByRole("heading", { name: /Attempt 1/ }),
    ).toBeInTheDocument();
    expect(
      screen.getByText(/correct result reasoning not assessed/),
    ).toBeInTheDocument();
  });
});

import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { afterEach, describe, expect, it, vi } from "vitest";
import { api } from "../api";
import type { InstructorAppeal } from "../types";
import { InstructorReview } from "./InstructorReview";

afterEach(() => vi.restoreAllMocks());

const appeal: InstructorAppeal = {
  id: "appeal-1",
  attempt_id: "attempt-1",
  course_id: "cell-biology",
  question_id: "cell-biology-1:check",
  reason: "Please reconsider whether my selected control is supported.",
  status: "open",
  decision: null,
  review_note: null,
  original_score: 0,
  effective_score: 0,
  max_score: 1,
  created_at: "2026-10-06T12:00:00Z",
  reviewed_at: null,
  learner: "learner@example.org",
  content_is_current: true,
  review_question: {
    id: "cell-biology-1:check",
    type: "single_choice",
    prompt: "Which condition controls for delivery-reagent effects?",
    options: ["Vehicle only", "Active treatment"],
    points: 1,
    learning_objective_ids: ["cell-biology-lo-1"],
    variant_id: "alternate-control",
    assessment_role: "formative",
  },
  question_prompt: "Which condition controls for delivery-reagent effects?",
  question_options: ["Vehicle only", "Active treatment"],
  response: { response: 1, variant_id: "alternate-control" },
  automatic_feedback: {
    score: 0,
    max_score: 1,
    correct: false,
    assessment_role: "formative",
    grading_policy_version: "practice-v10",
    feedback: {
      diagnosis: "incorrect_selection",
      hint: "Match the delivery process while omitting the active treatment.",
      misconception: "A vehicle control does not contain the active treatment.",
      next_step: "Compare the treatment and control conditions.",
      lesson_id: "cell-biology-1",
      reasoning_assessed: false,
      provisional: false,
    },
  },
  specification_pinned: true,
};

describe("instructor appeal review", () => {
  it("shows the pinned variant's prompt, options, and answer before recording a decision", async () => {
    const list = vi.spyOn(api, "instructorAppeals").mockResolvedValue([appeal]);
    const review = vi.spyOn(api, "reviewAppeal").mockResolvedValue(appeal);
    const user = userEvent.setup();
    render(<InstructorReview />);

    expect(
      await screen.findByText(appeal.review_question!.prompt),
    ).toBeInTheDocument();
    expect(
      screen.getByRole("list", { name: "Question options" }),
    ).toHaveTextContent("Vehicle onlyActive treatment");
    expect(
      screen.getByText("Active treatment", { selector: ".submitted-response" }),
    ).toBeInTheDocument();

    await user.click(
      screen.getByRole("radio", { name: "Adjust practice score" }),
    );
    await user.clear(screen.getByLabelText(/Reviewed practice score/));
    await user.type(screen.getByLabelText(/Reviewed practice score/), "1");
    await user.type(
      screen.getByLabelText("Review note (visible to the learner)"),
      "The alternate response matches the question's stated control condition.",
    );
    await user.click(
      screen.getByRole("button", { name: "Record review decision" }),
    );

    expect(review).toHaveBeenCalledWith(
      "appeal-1",
      "adjusted",
      "The alternate response matches the question's stated control condition.",
      1,
    );
    expect(list).toHaveBeenCalledTimes(2);
  });

  it("allows only a decline when the pinned question is unavailable", async () => {
    vi.spyOn(api, "instructorAppeals").mockResolvedValue([
      {
        ...appeal,
        content_is_current: false,
        review_question: null,
        question_prompt: null,
        question_options: null,
      },
    ]);
    render(<InstructorReview />);

    expect(
      await screen.findByText(/unavailable or has changed/),
    ).toBeInTheDocument();
    expect(
      screen.getByRole("radio", { name: "Adjust practice score" }),
    ).toBeDisabled();
    expect(
      screen.getByRole("radio", { name: "Uphold automatic score" }),
    ).toBeDisabled();
    expect(
      screen.getByRole("radio", { name: "Decline request" }),
    ).toBeEnabled();
  });
});

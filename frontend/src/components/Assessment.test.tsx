import { render, screen, fireEvent } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { describe, expect, it, vi } from "vitest";
import { Assessment } from "./Assessment";
import type { Attempt, Question } from "../types";

const numericQuestion: Question = {
  id: "kinetics-rate",
  type: "numeric",
  prompt: "Predict the initial enzyme rate.",
  options: [],
  unit: "µmol/min",
  points: 1,
  learning_objective_ids: ["rate"],
  assessment_role: "formative",
};
const attempt: Attempt = {
  id: "attempt-1",
  course_id: "cell-biology",
  question_id: "kinetics-rate",
  content_version: "0.1",
  response: { response: "80", unit: "µmol/min" },
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
      next_step: "Explain the assumptions of your model.",
      lesson_id: "cell-biology-3",
      reasoning_assessed: false,
      misconception: null,
      provisional: false,
    },
  },
  objective_ids: ["rate"],
  created_at: "2026-10-05T12:00:00Z",
};

describe("formative assessment submission", () => {
  it("requires an explicit unit and rejects nonfinite values before making a request", async () => {
    const submit = vi.fn();
    const { container } = render(
      <Assessment question={numericQuestion} enabled onSubmit={submit} />,
    );
    await userEvent.type(screen.getByLabelText("Numerical value"), "80");
    fireEvent.submit(container.querySelector("form")!);
    expect(screen.getByRole("alert")).toHaveTextContent("Enter the unit");
    expect(submit).not.toHaveBeenCalled();
    await userEvent.type(screen.getByLabelText("Unit"), "µmol/min");
    await userEvent.clear(screen.getByLabelText("Numerical value"));
    await userEvent.type(screen.getByLabelText("Numerical value"), "Infinity");
    fireEvent.submit(container.querySelector("form")!);
    expect(screen.getByRole("alert")).toHaveTextContent(
      "finite numerical value",
    );
    expect(submit).not.toHaveBeenCalled();
  });
  it("sends value and unit separately and does not equate a correct result with sound reasoning", async () => {
    const submit = vi.fn().mockResolvedValue(attempt);
    render(<Assessment question={numericQuestion} enabled onSubmit={submit} />);
    await userEvent.type(screen.getByLabelText("Numerical value"), "80");
    await userEvent.type(screen.getByLabelText("Unit"), "µmol/min");
    await userEvent.click(
      screen.getByRole("button", { name: "Submit practice response" }),
    );
    expect(submit).toHaveBeenCalledWith("80", "µmol/min");
    expect(
      await screen.findByText(
        "Correct result. Reasoning has not been assessed.",
      ),
    ).toBeInTheDocument();
    expect(
      screen.getByText(
        /does not establish sound reasoning or learning mastery/,
      ),
    ).toBeInTheDocument();
    expect(
      screen.queryByText(/sound reasoning confirmed/i),
    ).not.toBeInTheDocument();
  });
  it("prevents submission when not enrolled", () => {
    const submit = vi.fn();
    render(
      <Assessment
        question={numericQuestion}
        enabled={false}
        onSubmit={submit}
      />,
    );
    expect(
      screen.getByRole("button", { name: "Submit practice response" }),
    ).toBeDisabled();
    expect(screen.getByLabelText("Numerical value")).toBeDisabled();
  });
});

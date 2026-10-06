import { render, screen, fireEvent, within } from "@testing-library/react";
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
const symbolicQuestion: Question = {
  id: "quotient-derivative",
  type: "symbolic",
  prompt:
    "Differentiate the rational function and enter a simplified expression.",
  options: [],
  points: 1,
  learning_objective_ids: ["quotient-rule"],
  assessment_role: "formative",
};
const dataInterpretationQuestion: Question = {
  id: "group-summary",
  type: "data_interpretation",
  prompt: "Compare the reported means and interpret the evidence.",
  options: [],
  points: 2,
  learning_objective_ids: ["causal-limits"],
  assessment_role: "formative",
  response_fields: [
    {
      id: "difference",
      type: "numeric",
      prompt: "Calculate treatment minus control and include its unit.",
      options: [],
      unit: "μM",
      points: 1,
    },
    {
      id: "conclusion",
      type: "single_choice",
      prompt: "Select the strongest supported conclusion.",
      options: [
        "Descriptive difference only",
        "Treatment caused every increase",
      ],
      points: 1,
    },
  ],
};
const structuredQuestion: Question = {
  id: "experimental-logic",
  type: "structured",
  prompt: "Construct a controlled experimental inference.",
  options: [],
  points: 2,
  learning_objective_ids: ["controls"],
  assessment_role: "formative",
  response_fields: [
    {
      id: "control",
      type: "single_choice",
      prompt: "Control fidelity · Select the matched control.",
      options: ["Matched non-targeting control", "Untreated cells"],
      points: 1,
    },
    {
      id: "claim",
      type: "single_choice",
      prompt: "Inference boundary · Select the supported claim.",
      options: ["Tested system only", "Universal causal claim"],
      points: 1,
    },
  ],
};
const fileUploadQuestion: Question = {
  id: "csv-summary",
  type: "file_upload",
  prompt: "Upload a UTF-8 CSV with unique condition rows and numeric results.",
  options: [],
  points: 4,
  accepted_media_types: ["text/csv"],
  max_upload_bytes: 32768,
  learning_objective_ids: ["summarize-data"],
  assessment_role: "formative",
};
const graphQuestion: Question = {
  id: "concentration-graph",
  type: "graph",
  prompt: "Calculate sample means and plot each group on the supplied axes.",
  options: [],
  points: 2,
  learning_objective_ids: ["summarize-data"],
  assessment_role: "formative",
  graph_spec: {
    x_axis: { label: "Dose (μM)", minimum: 0, maximum: 1 },
    y_axis: { label: "Mean response (units)", minimum: 0, maximum: 10 },
    points: [
      { id: "vehicle", label: "Vehicle" },
      { id: "treatment", label: "Treatment" },
    ],
    observations: [
      { id: "vehicle", x: 0, values: [4, 5, 6] },
      { id: "treatment", x: 1, values: [8, 9, 10] },
    ],
  },
};
const multipleQuestion: Question = {
  id: "membrane-assembly",
  type: "multiple_select",
  prompt:
    "Which statements explain bilayer assembly in water? Select all that apply.",
  options: [
    "Hydrophobic tails are shielded.",
    "Polar headgroups remain hydrated.",
    "Covalent bonds are required.",
  ],
  selection: "multiple",
  partial_credit_policy: "correct-minus-incorrect-clamped-v1",
  points: 3,
  learning_objective_ids: ["membrane"],
  assessment_role: "formative",
};
const variantQuestion: Question = {
  id: "variant-control",
  type: "single_choice",
  prompt: "Which comparison preserves the delivery procedure?",
  options: ["Non-targeting sequence", "Untreated cells"],
  points: 1,
  learning_objective_ids: ["controls"],
  assessment_role: "formative",
  variant_id: "non-targeting-control",
  variant_token: "signed-variant-token",
};
const attempt: Attempt = {
  id: "attempt-1",
  course_id: "cell-biology",
  question_id: "kinetics-rate",
  content_version: "0.1",
  response: { response: "80", unit: "µmol/min" },
  score: 1,
  effective_score: 1,
  appeal: null,
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
  it("collects an algebraic expression and sends it to the deterministic grader", async () => {
    const submit = vi.fn().mockResolvedValue(attempt);
    render(
      <Assessment question={symbolicQuestion} enabled onSubmit={submit} />,
    );
    await userEvent.type(
      screen.getByLabelText("Algebraic expression"),
      "(x^2 + 2*x - 1)/(x + 1)^2",
    );
    await userEvent.click(
      screen.getByRole("button", { name: "Submit practice response" }),
    );
    expect(submit).toHaveBeenCalledWith("(x^2 + 2*x - 1)/(x + 1)^2", undefined);
  });
  it("submits structured data fields and shows independent field-level scoring", async () => {
    const submit = vi.fn().mockResolvedValue({
      ...attempt,
      question_id: dataInterpretationQuestion.id,
      response: { response: { difference: "4.0 μM", conclusion: "1" } },
      score: 1,
      max_score: 2,
      result: {
        ...attempt.result,
        correct: false,
        score: 1,
        max_score: 2,
        feedback: {
          ...attempt.result.feedback,
          diagnosis: "data_interpretation_partial",
          components: [
            {
              field_id: "difference",
              label: "Calculate treatment minus control and include its unit.",
              score: 1,
              max_score: 1,
              diagnosis: "correct_result_reasoning_not_assessed",
            },
            {
              field_id: "conclusion",
              label: "Select the strongest supported conclusion.",
              score: 0,
              max_score: 1,
              diagnosis: "incorrect_result",
            },
          ],
        },
      },
    });
    const { container } = render(
      <Assessment
        question={dataInterpretationQuestion}
        enabled
        onSubmit={submit}
      />,
    );
    fireEvent.submit(container.querySelector("form")!);
    expect(screen.getByRole("alert")).toHaveTextContent("at least one field");
    await userEvent.type(
      screen.getByLabelText(/Calculate treatment minus control/),
      "4.0 μM",
    );
    await userEvent.selectOptions(
      screen.getByLabelText(/Select the strongest supported conclusion/),
      "1",
    );
    await userEvent.click(
      screen.getByRole("button", { name: "Submit practice response" }),
    );
    expect(submit).toHaveBeenCalledWith(
      { difference: "4.0 μM", conclusion: "1" },
      undefined,
    );
    expect(
      await screen.findByText(/Some fields are correct/),
    ).toBeInTheDocument();
    expect(screen.getByLabelText("Field-level scoring")).toHaveTextContent(
      "1 / 1 point",
    );
    expect(screen.getByLabelText("Field-level scoring")).toHaveTextContent(
      "0 / 1 point",
    );
  });
  it("submits analytic rubric fields separately and identifies prose as ungraded", async () => {
    const submit = vi.fn().mockResolvedValue({
      ...attempt,
      question_id: structuredQuestion.id,
      score: 2,
      max_score: 2,
      result: {
        ...attempt.result,
        correct: true,
        score: 2,
        max_score: 2,
        feedback: {
          ...attempt.result.feedback,
          diagnosis: "structured_rubric_complete",
          next_step:
            "Each structured analytic criterion met its deterministic check. Free-form reasoning was not assessed.",
          components: [
            {
              field_id: "control",
              label: "Control fidelity",
              score: 1,
              max_score: 1,
              diagnosis: "correct_result_reasoning_not_assessed",
            },
            {
              field_id: "claim",
              label: "Inference boundary",
              score: 1,
              max_score: 1,
              diagnosis: "correct_result_reasoning_not_assessed",
            },
          ],
        },
      },
    });
    render(
      <Assessment question={structuredQuestion} enabled onSubmit={submit} />,
    );
    expect(
      screen.getByText(/Each analytic criterion is scored separately/),
    ).toBeInTheDocument();
    await userEvent.selectOptions(
      screen.getByLabelText(/Control fidelity/),
      "0",
    );
    await userEvent.selectOptions(
      screen.getByLabelText(/Inference boundary/),
      "0",
    );
    await userEvent.click(
      screen.getByRole("button", { name: "Submit practice response" }),
    );
    expect(submit).toHaveBeenCalledWith(
      { control: "0", claim: "0" },
      undefined,
    );
    expect(
      await screen.findByText(
        "All structured analytic criteria met their deterministic checks.",
      ),
    ).toBeInTheDocument();
    expect(screen.getByLabelText("Field-level scoring")).toHaveTextContent(
      "Control fidelity",
    );
    expect(
      screen.getByText(/Free-form reasoning was not assessed/),
    ).toBeInTheDocument();
  });
  it("encodes a size-bounded CSV file as data for the server grader", async () => {
    const submit = vi.fn().mockResolvedValue(attempt);
    render(
      <Assessment question={fileUploadQuestion} enabled onSubmit={submit} />,
    );
    const input = screen.getByLabelText("CSV file upload");
    const csv = "condition,mean_signal\nvehicle,5\n";
    await userEvent.upload(
      input,
      new File([csv], "summary.csv", { type: "text/csv" }),
      { applyAccept: false },
    );
    expect(input).toHaveProperty("files.length", 1);
    await userEvent.click(
      screen.getByRole("button", { name: "Submit practice response" }),
    );
    const bytes = new TextEncoder().encode(csv);
    const expectedBase64 = btoa(
      Array.from(bytes, (byte) => String.fromCharCode(byte)).join(""),
    );
    expect(submit).toHaveBeenCalledWith(
      { content_base64: expectedBase64 },
      undefined,
    );
    expect(
      screen.getByText(/parsed as data; uploaded content is never executed/),
    ).toBeInTheDocument();
  });
  it("plots learner coordinates accessibly and submits coordinate-level responses", async () => {
    const submit = vi.fn().mockResolvedValue({
      ...attempt,
      question_id: graphQuestion.id,
      score: 1.5,
      effective_score: 1.5,
      max_score: 2,
      result: {
        ...attempt.result,
        correct: false,
        score: 1.5,
        max_score: 2,
        feedback: {
          ...attempt.result.feedback,
          diagnosis: "graph_coordinates_partial",
          next_step:
            "Each x and y coordinate is scored separately. Check the source pairs, point labels, and axis units.",
          components: [
            {
              field_id: "vehicle_x",
              label: "Vehicle dose coordinate",
              score: 0.5,
              max_score: 0.5,
              diagnosis: "correct_result_reasoning_not_assessed",
            },
            {
              field_id: "vehicle_y",
              label: "Vehicle mean coordinate",
              score: 0,
              max_score: 0.5,
              diagnosis: "numerical_mismatch",
            },
          ],
        },
      },
    });
    render(<Assessment question={graphQuestion} enabled onSubmit={submit} />);
    expect(
      screen.getByRole("table", {
        name: "Replicate measurements supplied for this graph",
      }),
    ).toHaveTextContent("4, 5, 6");
    const preview = screen.getByRole("img", { name: /Graph preview/ });
    expect(preview).toHaveAttribute(
      "aria-label",
      expect.stringContaining("not plotted"),
    );

    const vehicle = within(screen.getByRole("group", { name: "Vehicle" }));
    await userEvent.type(vehicle.getByLabelText("Dose (μM) coordinate"), "0");
    await userEvent.type(
      vehicle.getByLabelText("Mean response (units) coordinate"),
      "4.5",
    );
    const treatment = within(screen.getByRole("group", { name: "Treatment" }));
    await userEvent.type(treatment.getByLabelText("Dose (μM) coordinate"), "1");
    await userEvent.type(
      treatment.getByLabelText("Mean response (units) coordinate"),
      "9",
    );
    expect(preview).toHaveAttribute(
      "aria-label",
      expect.stringContaining("Vehicle: x 0, y 4.5"),
    );
    await userEvent.click(
      screen.getByRole("button", { name: "Submit practice response" }),
    );
    expect(submit).toHaveBeenCalledWith(
      {
        vehicle_x: "0",
        vehicle_y: "4.5",
        treatment_x: "1",
        treatment_y: "9",
      },
      undefined,
    );
    expect(
      await screen.findByText(
        "Some plotted coordinates met their deterministic checks. Each x and y coordinate receives separate credit.",
      ),
    ).toBeInTheDocument();
    expect(screen.getByLabelText("Field-level scoring")).toHaveTextContent(
      "Vehicle mean coordinate",
    );
  });
  it("rejects an over-size CSV before sending it", async () => {
    const submit = vi.fn();
    render(
      <Assessment
        question={{ ...fileUploadQuestion, max_upload_bytes: 4 }}
        enabled
        onSubmit={submit}
      />,
    );
    await userEvent.upload(
      screen.getByLabelText("CSV file upload"),
      new File(["12345"], "large.csv", { type: "text/csv" }),
      { applyAccept: false },
    );
    await userEvent.click(
      screen.getByRole("button", { name: "Submit practice response" }),
    );
    expect(screen.getByRole("alert")).toHaveTextContent("larger than 4 bytes");
    expect(submit).not.toHaveBeenCalled();
  });
  it("shows the significant-figure requirement before numeric practice", () => {
    render(
      <Assessment
        question={{ ...numericQuestion, significant_figures: 3 }}
        enabled
        onSubmit={vi.fn()}
      />,
    );
    expect(
      screen.getByText(/Report exactly 3 significant figures/),
    ).toBeInTheDocument();
  });
  it("explains when an in-tolerance result uses the wrong precision", async () => {
    const submit = vi.fn().mockResolvedValue({
      ...attempt,
      score: 0,
      result: {
        ...attempt.result,
        score: 0,
        correct: false,
        feedback: {
          ...attempt.result.feedback,
          diagnosis: "significant_figures_mistake",
          next_step: "Report exactly 2 significant figures.",
        },
      },
    });
    render(
      <Assessment
        question={{ ...numericQuestion, significant_figures: 2 }}
        enabled
        onSubmit={submit}
      />,
    );
    await userEvent.type(screen.getByLabelText("Numerical value"), "82.0");
    await userEvent.type(screen.getByLabelText("Unit"), "µmol/min");
    await userEvent.click(
      screen.getByRole("button", { name: "Submit practice response" }),
    );
    expect(
      await screen.findByText(
        /within tolerance, but its written precision does not match/,
      ),
    ).toBeInTheDocument();
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
  it("requires a selection and submits multiple choices with transparent partial credit", async () => {
    const submit = vi.fn().mockResolvedValue({
      ...attempt,
      question_id: multipleQuestion.id,
      response: { response: [0, 1] },
      score: 2,
      effective_score: 2,
      max_score: 3,
      result: {
        ...attempt.result,
        score: 2,
        max_score: 3,
        correct: false,
        feedback: {
          ...attempt.result.feedback,
          diagnosis: "partially_correct_selection",
        },
      },
    });
    const { container } = render(
      <Assessment question={multipleQuestion} enabled onSubmit={submit} />,
    );
    fireEvent.submit(container.querySelector("form")!);
    expect(screen.getByRole("alert")).toHaveTextContent("Select at least one");
    expect(submit).not.toHaveBeenCalled();
    expect(
      screen.getByText(/each incorrect selection subtracts one equal share/),
    ).toBeInTheDocument();
    await userEvent.click(screen.getByLabelText(multipleQuestion.options[0]));
    await userEvent.click(screen.getByLabelText(multipleQuestion.options[1]));
    await userEvent.click(
      screen.getByRole("button", { name: "Submit practice response" }),
    );
    expect(submit).toHaveBeenCalledWith([0, 1], undefined);
    expect(
      await screen.findByText("2 / 3 practice points"),
    ).toBeInTheDocument();
  });
  it("submits the signed token for the displayed authored variant", async () => {
    const submit = vi.fn().mockResolvedValue({
      ...attempt,
      question_id: variantQuestion.id,
      response: { response: 0, variant_id: variantQuestion.variant_id },
    });
    render(<Assessment question={variantQuestion} enabled onSubmit={submit} />);
    await userEvent.click(screen.getByLabelText("Non-targeting sequence"));
    await userEvent.click(
      screen.getByRole("button", { name: "Submit practice response" }),
    );
    expect(submit).toHaveBeenCalledWith(0, undefined, "signed-variant-token");
  });

  it("sends a reasoned human-review request without changing the automatic attempt", async () => {
    const failedAttempt: Attempt = {
      ...attempt,
      score: 0,
      effective_score: 0,
      result: {
        ...attempt.result,
        score: 0,
        correct: false,
        feedback: {
          ...attempt.result.feedback,
          diagnosis: "numerical_mismatch",
        },
      },
    };
    const appeal = {
      id: "appeal-1",
      attempt_id: failedAttempt.id,
      course_id: failedAttempt.course_id,
      question_id: failedAttempt.question_id,
      reason: "The alternate value is supported by the stated model.",
      status: "open" as const,
      decision: null,
      review_note: null,
      original_score: 0,
      effective_score: 0,
      max_score: 1,
      created_at: "2026-10-05T12:05:00Z",
      reviewed_at: null,
    };
    const submit = vi.fn().mockResolvedValue(failedAttempt);
    const requestReview = vi.fn().mockResolvedValue(appeal);
    render(
      <Assessment
        question={numericQuestion}
        enabled
        onSubmit={submit}
        onAppeal={requestReview}
      />,
    );
    await userEvent.type(screen.getByLabelText("Numerical value"), "79");
    await userEvent.type(screen.getByLabelText("Unit"), "µmol/min");
    await userEvent.click(
      screen.getByRole("button", { name: "Submit practice response" }),
    );
    await userEvent.type(
      screen.getByLabelText("Reason for review"),
      appeal.reason,
    );
    await userEvent.click(
      screen.getByRole("button", { name: "Send for human review" }),
    );
    expect(requestReview).toHaveBeenCalledWith(failedAttempt.id, appeal.reason);
    expect(
      await screen.findByRole("heading", { name: "Human review · open" }),
    ).toBeInTheDocument();
    expect(
      screen.getByRole("heading", { name: "0 / 1 practice points" }),
    ).toBeInTheDocument();
  });
});

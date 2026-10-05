import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { describe, expect, it } from "vitest";
import type { CourseSummary } from "../types";
import { CourseCatalog } from "./CourseCatalog";

const courses: CourseSummary[] = [
  {
    id: "cell-biology",
    title: "Foundations of Cell and Molecular Biology",
    description: "Reason about cells and molecular experiments.",
    domain: "Life sciences",
    level: "Year 1",
    maturity: "partial",
    version: "0.1",
    lesson_count: 4,
    limitations: ["Full course development remains."],
  },
  {
    id: "circuits",
    title: "Circuits I",
    description: "Analyze circuit models.",
    domain: "Engineering",
    level: "Year 2",
    maturity: "catalog-only",
    version: "0.1",
    lesson_count: 0,
    limitations: ["No lessons yet."],
  },
];

describe("catalog maturity and filtering", () => {
  it("reports partial and catalog-only maturity with honest course-depth limits", async () => {
    render(<CourseCatalog courses={courses} enrollments={[]} bookmarks={[]} />);
    expect(screen.getByText("partial")).toBeInTheDocument();
    expect(screen.getByText("catalog-only")).toBeInTheDocument();
    expect(
      screen.getByText(
        /Four short lessons do not constitute a semester course/,
      ),
    ).toBeInTheDocument();
    await userEvent.selectOptions(
      screen.getByLabelText("Domain"),
      "Engineering",
    );
    expect(
      screen.getByRole("link", { name: "Circuits I" }),
    ).toBeInTheDocument();
    expect(
      screen.queryByRole("link", {
        name: "Foundations of Cell and Molecular Biology",
      }),
    ).not.toBeInTheDocument();
  });
});

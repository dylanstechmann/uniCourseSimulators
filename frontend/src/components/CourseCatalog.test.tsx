import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { describe, expect, it } from "vitest";
import type { CourseSummary, CurriculumMap } from "../types";
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
      screen.getByText(/prototype material with uneven depth/),
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

  it("shows prerequisite-linked study steps and keeps planned topics distinct", async () => {
    const curriculum: CurriculumMap = {
      schema_version: "1.0",
      description:
        "Project-authored planning map with no university-equivalency claim.",
      nodes: [
        {
          id: "cell-biology",
          title: "Foundations of Cell and Molecular Biology",
          domain: "Life sciences",
          level: "Year 1",
          maturity: "partial",
          description: "Study cells and experimental logic.",
          prerequisites: {
            course_ids: [],
            recommended_course_ids: [],
            concurrent_course_ids: [],
            knowledge: [],
            statement: "High-school biology.",
          },
          package_id: "cell-biology",
          related_package_ids: [],
          relation_note: null,
        },
        {
          id: "molecular-biology",
          title: "Molecular Biology",
          domain: "Life sciences",
          level: "Year 2",
          maturity: "catalog-only",
          description: "Planned independent molecular biology study area.",
          prerequisites: {
            course_ids: ["cell-biology"],
            recommended_course_ids: [],
            concurrent_course_ids: [],
            knowledge: [],
            statement: "Prior cell-biology study is recommended.",
          },
          package_id: null,
          related_package_ids: [],
          relation_note: null,
        },
      ],
      pathways: [
        {
          id: "jhu-regenerative-stem-cell-prerequisites",
          title:
            "Johns Hopkins regenerative/stem-cell prerequisite knowledge map",
          description: "A planning map to public program topics.",
          course_ids: ["cell-biology", "molecular-biology"],
          source_ids: [],
          sequence_note:
            "Project planning sequence only; university requirements may differ.",
        },
      ],
      alignment_maps: [],
    };
    render(
      <CourseCatalog
        courses={courses}
        enrollments={[]}
        bookmarks={[]}
        curriculum={curriculum}
      />,
    );
    expect(
      screen.getByRole("heading", { name: "Curriculum pathways" }),
    ).toBeInTheDocument();
    await userEvent.click(
      screen.getByText(
        "Johns Hopkins regenerative/stem-cell prerequisite knowledge map",
      ),
    );
    expect(
      screen.getByText("Molecular Biology", { selector: "h3" }),
    ).toBeInTheDocument();
    expect(screen.getAllByText("catalog-only")).toHaveLength(2);
    expect(
      screen.getByText(
        /Prerequisites: Foundations of Cell and Molecular Biology/,
      ),
    ).toBeInTheDocument();
    expect(
      screen.getByText(
        /Original lessons and assessments have not been authored/,
      ),
    ).toBeInTheDocument();
    expect(
      screen.getByRole("link", {
        name: /Open available partial package: Foundations of Cell and Molecular Biology/,
      }),
    ).toHaveAttribute("href", "#/course/cell-biology");
  });
});

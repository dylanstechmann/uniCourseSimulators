import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { afterEach, describe, expect, it, vi } from "vitest";
import App from "./App";
import { api } from "./api";
import type { Course } from "./types";

afterEach(() => {
  window.location.hash = "";
});

describe("reader keyboard navigation", () => {
  it("moves the skip-link focus to main without replacing the course route", async () => {
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
        knowledge: ["High-school biology and chemistry"],
        statement: "Review basic molecular structure before beginning.",
      },
      outcomes: [],
      lesson_objectives: [],
      modules: [],
      syllabus_markdown: "Original partial syllabus.",
      license: "CC-BY-4.0",
      review_status: {},
      assessment_policy: {},
    };
    vi.spyOn(api, "session").mockResolvedValue({
      user: null,
      csrf_token: null,
    });
    vi.spyOn(api, "courses").mockResolvedValue([course]);
    vi.spyOn(api, "sources").mockResolvedValue([]);
    vi.spyOn(api, "course").mockResolvedValue(course);
    const scroll = vi.fn();
    Object.defineProperty(Element.prototype, "scrollIntoView", {
      configurable: true,
      value: scroll,
    });
    window.location.hash = "/course/cell-biology";
    render(<App />);
    await screen.findByRole("heading", {
      name: course.title,
      level: 1,
    });
    const originalRoute = window.location.hash;
    await userEvent.click(
      screen.getByRole("link", { name: "Skip to main content" }),
    );
    expect(window.location.hash).toBe(originalRoute);
    expect(screen.getByRole("main")).toHaveFocus();
    expect(scroll).toHaveBeenCalledOnce();
    expect(
      screen.getByRole("heading", { name: course.title, level: 1 }),
    ).toBeInTheDocument();
  });
});

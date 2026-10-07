import { render, screen, within } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { describe, expect, it, vi } from "vitest";
import type { CardSchedule, ReviewQueue, ReviewQueueCard } from "../types";
import { describeSchedule } from "./CardRatingControls";
import { ReviewQueueView } from "./ReviewQueueView";

const schedule = (overrides: Partial<CardSchedule> = {}): CardSchedule => ({
  policy_version: "retrieval-schedule-v1",
  last_rating: "good",
  review_count: 1,
  repetitions: 1,
  ease: 2.5,
  interval_days: 1,
  due_at: "2026-10-08T12:00:00.000000Z",
  reviewed_at: "2026-10-07T12:00:00.000000Z",
  due: false,
  ...overrides,
});

const card = (
  id: string,
  overrides: Partial<ReviewQueueCard> = {},
): ReviewQueueCard => ({
  card_id: id,
  lesson_id: "cell-biology-1",
  lesson_title: "What counts as evidence",
  front: `Front of ${id}`,
  back: `Back of ${id}`,
  learning_objective_ids: [],
  schedule: null,
  content_changed_since_last_review: false,
  ...overrides,
});

const queue = (overrides: Partial<ReviewQueue> = {}): ReviewQueue => ({
  course_id: "cell-biology",
  content_version: "0.18.0",
  policy_version: "retrieval-schedule-v1",
  policy: "Self-rated retrieval schedule (retrieval-schedule-v1).",
  generated_at: "2026-10-09T12:00:00.000000Z",
  counts: { due: 1, new: 1, upcoming: 1 },
  due: [card("due-card", { schedule: schedule({ due: true }) })],
  new: [card("new-card", { content_changed_since_last_review: true })],
  upcoming: [
    card("later-card", {
      schedule: schedule({ interval_days: 6, last_rating: "easy" }),
    }),
  ],
  limitations:
    "Ratings are your own self-assessment after revealing an answer. The schedule is not a practice score.",
  ...overrides,
});

describe("spaced retrieval review queue", () => {
  it("separates due, new and scheduled cards and keeps the self-assessment notice", () => {
    render(
      <ReviewQueueView
        courseId="cell-biology"
        queue={queue()}
        enabled
        onRate={vi.fn()}
      />,
    );
    expect(
      screen.getByText("1 due now · 1 not yet reviewed · 1 scheduled later"),
    ).toBeInTheDocument();
    expect(screen.getByText(/not a practice score/)).toBeInTheDocument();
    const due = screen.getByRole("list", { name: "Cards due now" });
    expect(within(due).getByText("Front of due-card")).toBeInTheDocument();
    const fresh = screen.getByRole("list", { name: "Cards not yet reviewed" });
    expect(
      within(fresh).getByText(/card text changed since your last review/),
    ).toBeInTheDocument();
    const table = screen.getByRole("table");
    expect(
      within(table).getByRole("rowheader", { name: "Front of later-card" }),
    ).toBeInTheDocument();
    expect(within(table).getByText("easy")).toBeInTheDocument();
    expect(
      within(due).getByRole("link", { name: "What counts as evidence" }),
    ).toHaveAttribute("href", "#/course/cell-biology/lesson/cell-biology-1");
  });

  it("saves a self-rating for a revealed card and reports the next interval", async () => {
    const onRate = vi.fn().mockResolvedValue({
      card_id: "due-card",
      lesson_id: "cell-biology-1",
      rating: "good",
      schedule: schedule({ interval_days: 6, review_count: 2 }),
    });
    render(
      <ReviewQueueView
        courseId="cell-biology"
        queue={queue({
          counts: { due: 1, new: 0, upcoming: 0 },
          new: [],
          upcoming: [],
        })}
        enabled
        onRate={onRate}
      />,
    );
    await userEvent.click(screen.getByText("Reveal answer"));
    const controls = screen.getByRole("group", {
      name: "Rate your recall for card due-card",
    });
    await userEvent.click(
      within(controls).getByRole("button", { name: /^Good:/ }),
    );
    expect(onRate).toHaveBeenCalledWith("due-card", "good");
    expect(await screen.findByRole("status")).toHaveTextContent(
      /Saved “good”\. Next review in 6 days/,
    );
  });

  it("disables ratings when the enrollment cannot save work", async () => {
    render(
      <ReviewQueueView
        courseId="cell-biology"
        queue={queue({
          counts: { due: 1, new: 0, upcoming: 0 },
          new: [],
          upcoming: [],
        })}
        enabled={false}
        onRate={vi.fn()}
      />,
    );
    await userEvent.click(screen.getByText("Reveal answer"));
    for (const button of within(
      screen.getByRole("group", { name: "Rate your recall for card due-card" }),
    ).getAllByRole("button")) {
      expect(button).toBeDisabled();
    }
  });

  it("describes relearning, scheduled and due states", () => {
    const now = Date.parse("2026-10-07T12:00:00Z");
    expect(
      describeSchedule(
        schedule({
          interval_days: 0,
          due_at: "2026-10-07T12:10:00.000000Z",
        }),
        now,
      ),
    ).toBe("Shown again in about 10 minutes.");
    expect(describeSchedule(schedule({ interval_days: 1 }), now)).toMatch(
      /^Next review in 1 day \(/,
    );
    expect(describeSchedule(schedule({ due: true }), now)).toBe(
      "Due for review now.",
    );
  });
});

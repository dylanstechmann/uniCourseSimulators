import { describe, expect, it, vi } from "vitest";
import { api, ApiError } from "./api";

describe("API session and ownership boundaries", () => {
  it("uses cookie credentials and CSRF token for a saved learner mutation", async () => {
    const fetchMock = vi
      .fn()
      .mockResolvedValueOnce(
        new Response(
          JSON.stringify({
            user: { id: "guest", email: null, is_guest: true },
            csrf_token: "test-csrf-value",
          }),
          { status: 200 },
        ),
      )
      .mockResolvedValueOnce(
        new Response(
          JSON.stringify({
            course_id: "cell-biology",
            content_version: "0.1",
            created_at: "2026-10-05",
          }),
          { status: 201 },
        ),
      );
    vi.stubGlobal("fetch", fetchMock);
    await api.session();
    await api.enroll("cell-biology");
    expect(fetchMock).toHaveBeenLastCalledWith(
      "/api/v1/enrollments",
      expect.objectContaining({
        method: "POST",
        credentials: "include",
        headers: expect.objectContaining({ "X-CSRF-Token": "test-csrf-value" }),
        body: '{"course_id":"cell-biology"}',
      }),
    );
    vi.unstubAllGlobals();
  });
  it("keeps malformed server error bodies out of learner-facing errors", async () => {
    vi.stubGlobal(
      "fetch",
      vi
        .fn()
        .mockResolvedValue(
          new Response("<html>unavailable</html>", { status: 503 }),
        ),
    );
    await expect(api.courses()).rejects.toBeInstanceOf(ApiError);
    await expect(api.courses()).rejects.toThrow("Request failed (503)");
    vi.unstubAllGlobals();
  });
  it("updates a selected enrollment version without using the new-course enroll route", async () => {
    const fetchMock = vi
      .fn()
      .mockResolvedValueOnce(
        new Response(
          JSON.stringify({
            user: { id: "guest", email: null, is_guest: true },
            csrf_token: "migration-csrf",
          }),
          { status: 200 },
        ),
      )
      .mockResolvedValueOnce(
        new Response(
          JSON.stringify({
            course_id: "cell-biology",
            content_version: "0.2.0",
            created_at: "2026-10-05",
          }),
          { status: 200 },
        ),
      );
    vi.stubGlobal("fetch", fetchMock);
    await api.session();
    await api.upgradeEnrollment("cell-biology");
    expect(fetchMock).toHaveBeenLastCalledWith(
      "/api/v1/enrollments/cell-biology/version",
      expect.objectContaining({
        method: "PUT",
        credentials: "include",
        headers: expect.objectContaining({ "X-CSRF-Token": "migration-csrf" }),
        body: "{}",
      }),
    );
    vi.unstubAllGlobals();
  });
});

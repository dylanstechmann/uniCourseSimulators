import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import { MarkdownReader } from "./MarkdownReader";

describe("MarkdownReader content boundary", () => {
  it("renders instructional Markdown without executing raw HTML or unsafe links", () => {
    const { container } = render(
      <MarkdownReader>
        {
          '## Experimental controls\n\nUse a [reference](https://example.edu).\n\n<script>window.stolen = true</script>\n\n<img src=x onerror="alert(1)">\n\n[unsafe](javascript:alert(1))'
        }
      </MarkdownReader>,
    );
    expect(
      screen.getByRole("heading", { name: "Experimental controls" }),
    ).toBeInTheDocument();
    expect(screen.getByRole("link", { name: "reference" })).toHaveAttribute(
      "href",
      "https://example.edu",
    );
    expect(container.querySelector("script")).toBeNull();
    expect(container.querySelector("[onerror]")).toBeNull();
    expect(container.querySelector('a[href^="javascript:"]')).toBeNull();
  });
});

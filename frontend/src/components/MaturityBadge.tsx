import type { Maturity } from "../types";

export function MaturityBadge({ maturity }: { maturity: Maturity }) {
  return (
    <span className={`badge maturity-${maturity.replaceAll(" ", "-")}`}>
      {maturity}
    </span>
  );
}

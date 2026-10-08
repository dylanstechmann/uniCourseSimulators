"""Recalculations kept from AI-assisted checks (docs/reviews/ai-assisted/).

Each expected value is computed here from the data stated in the item or lesson, not read from the stored
key. A pass means the stored keys and the stated numbers agree with this arithmetic. It is not a review
of the teaching, and an AI-assisted check is not a human review.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSES = ROOT / "content" / "courses"
Z80 = 1.96 + 0.8416  # two-sided alpha 0.05 and 80% power, as stated in the genetics items

GENETICS_NUMERIC = {
    "genetics-2:check": 72 / 400 * 100,
    "genetics-1:genotype-vs-phenotype-frequency": 2 * 0.8 * 0.2,
    "genetics-2:map-distance": 12 / 200 * 100,
    "genetics-5:allele-frequency": (2 * 420 + 360) / 2000,
    "genetics-5:expected-heterozygotes": 2 * 0.6 * 0.4 * 1000,
    "genetics-5:chi-square": (420 - 360) ** 2 / 360 + (360 - 480) ** 2 / 480 + (220 - 160) ** 2 / 160,
    "genetics-5:inbreeding-f": 1 - 0.36 / 0.48,
    "genetics-5:carrier-frequency": 2 * (1 - math.sqrt(1 / 2500)) * math.sqrt(1 / 2500),
    "genetics-6:falconer-h2": 2 * (0.5 - 0.3),
    "genetics-6:unique-environment": 1 - 0.5,
    "genetics-6:polygenic-score": sum(b * g for b, g in zip([0.1, -0.05, 0.2, 0.04], [2, 1, 0, 2])),
    "genetics-6:variance-to-correlation": math.sqrt(0.08),
    "genetics-7:rf-ab": (106 + 8) / 1000,
    "genetics-7:expected-dco": 0.114 * 0.112 * 1000,
    "genetics-7:interference": 1 - 8 / (0.114 * 0.112 * 1000),
    "genetics-7:haldane": -0.5 * math.log(1 - 2 * 0.21) * 100,
    "genetics-8:ddct-expression": 2 ** -((26.5 - 18.2) - (24.0 - 18.0)),
    "genetics-8:percent-knockdown": (1 - 0.203) * 100,
    "genetics-8:sample-size": 2 * Z80**2 * 0.5**2 / 1.0**2,
    "genetics-9:wald-ratio": 0.05 / 0.1,
    "genetics-9:odds-ratio": math.exp(0.5),
    "genetics-9:wald-se": 0.01 / 0.1,
    "genetics-9:f-statistic": (0.02 / 0.01) ** 2,
}


def bank(course: str) -> dict[str, dict]:
    path = COURSES / course / "question-banks" / "practice.json"
    return {item["id"]: item for item in json.loads(path.read_text(encoding="utf-8"))["questions"]}


def reading(course: str, lesson_id: str) -> str:
    manifest = json.loads((COURSES / course / "course.json").read_text(encoding="utf-8"))
    lesson = next(item for module in manifest["modules"] for item in module["lessons"] if item["id"] == lesson_id)
    return (COURSES / course / lesson["reading"]).read_text(encoding="utf-8")


def _phi(x: float) -> float:
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def _over_chi2(df: int, integrand, steps: int = 4000) -> float:
    """Simpson's rule for E[integrand(V)] with V ~ chi-square(df)."""
    upper = df + 60 * math.sqrt(2 * df)
    h = upper / steps
    log_norm = (df / 2) * math.log(2) + math.lgamma(df / 2)

    def weight(v: float) -> float:
        return 0.0 if v <= 0 else math.exp((df / 2 - 1) * math.log(v) - v / 2 - log_norm) * integrand(v)

    total = weight(0) + weight(upper)
    total += sum((4 if i % 2 else 2) * weight(i * h) for i in range(1, steps))
    return total * h / 3


def two_sample_t_power(n: int, sd: float, delta: float, alpha: float = 0.05) -> float:
    """Exact power of a two-sided, two-sample t-test with n per group (noncentral t by integration)."""
    df, ncp = 2 * n - 2, delta / (sd * math.sqrt(2 / n))

    def central_cdf(t: float) -> float:
        return _over_chi2(df, lambda v: _phi(t * math.sqrt(v / df)))

    low, high = 0.0, 20.0
    for _ in range(60):
        mid = (low + high) / 2
        low, high = (mid, high) if central_cdf(mid) < 1 - alpha / 2 else (low, mid)
    critical = (low + high) / 2
    return _over_chi2(
        df, lambda v: _phi(ncp - critical * math.sqrt(v / df)) + _phi(-ncp - critical * math.sqrt(v / df))
    )


@pytest.mark.parametrize("question_id,expected", sorted(GENETICS_NUMERIC.items()))
def test_genetics_numeric_key_matches_independent_recalculation(question_id, expected):
    spec = bank("genetics")[question_id]["solution_spec"]
    assert abs(spec["answer"] - expected) <= spec["tolerance"], (question_id, spec["answer"], expected)


def test_every_genetics_numeric_item_is_recalculated():
    numeric = {qid for qid, item in bank("genetics").items() if item["type"] == "numeric"}
    assert numeric == set(GENETICS_NUMERIC)


def test_replicate_advice_matches_exact_t_test_power():
    # The normal approximation gives n = 3.92 -> 4 per group, but the exact two-sample t-test needs more.
    assert two_sample_t_power(4, 0.5, 1.0) == pytest.approx(0.657, abs=0.005)
    assert two_sample_t_power(5, 0.5, 1.0) < 0.80 < two_sample_t_power(6, 0.5, 1.0)
    assert two_sample_t_power(11, 0.8, 1.0) < 0.80 < two_sample_t_power(12, 0.8, 1.0)
    text = reading("genetics", "genetics-8")
    assert "4 per group gives only about 66% power, and 6 per group are needed for 80%" in text
    assert "11 per group (12 by the exact t-test calculation)" in text
    assert "at least 6 times per condition" in text


def test_kosambi_distance_stated_in_the_mapping_lesson():
    r = 0.21
    kosambi_cm = 25 * math.log((1 + 2 * r) / (1 - 2 * r))
    assert round(kosambi_cm, 1) == 22.4
    assert "gives 22.4 cM, close to the 22.6 cM" in reading("genetics", "genetics-7")

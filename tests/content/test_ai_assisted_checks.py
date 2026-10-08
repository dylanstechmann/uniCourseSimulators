"""Recalculations kept from AI-assisted checks (docs/reviews/ai-assisted/).

Each expected value is computed here from the data stated in the item or lesson, not read from the stored
key. A pass means the stored keys and the stated numbers agree with this arithmetic. It is not a review
of the teaching, and an AI-assisted check is not a human review.
"""

from __future__ import annotations

import functools
import itertools
import json
import math
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSES = ROOT / "content" / "courses"
Z80 = 1.96 + 0.8416  # two-sided alpha 0.05 and 80% power, as stated in the genetics items


def benjamini_hochberg_count(pvalues: list[float], q: float) -> int:
    """Largest rank k with p(k) <= (k/m) q, found by scanning from the largest rank down (step-up)."""
    ranked, m = sorted(pvalues), len(pvalues)
    return next((k for k in range(m, 0, -1) if ranked[k - 1] <= k / m * q + 1e-12), 0)


def credible_set_size(bayes_factors: list[float], level: float) -> int:
    probabilities = sorted((b / sum(bayes_factors) for b in bayes_factors), reverse=True)
    total = 0.0
    for size, probability in enumerate(probabilities, 1):
        total += probability
        if total >= level - 1e-12:
            return size
    return len(probabilities)


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
    # genetics 0.5.0: lessons 10 to 15 and the association lab, recomputed from the numbers in each prompt
    "genetics-10:expected-971": 9 / 16 * 160,
    "genetics-10:chi-3-1": (96 - 120) ** 2 / 120 + (64 - 40) ** 2 / 40,
    "genetics-10:chi-9-7": (96 - 90) ** 2 / 90 + (64 - 70) ** 2 / 70,
    "genetics-11:posterior-three-sons": (0.5 * 0.5**3) / (0.5 * 0.5**3 + 0.5 * 1),
    "genetics-11:next-son-risk": (0.5 * 0.5**3) / (0.5 * 0.5**3 + 0.5 * 1) * 0.5,
    "genetics-11:penetrance-likelihood": 1 - 0.5 * 0.8,
    "genetics-11:posterior-two-sons": (0.5 * 0.5**2) / (0.5 * 0.5**2 + 0.5 * 1),
    "genetics-12:mi-disomic": 0.04 * 2 / 4,
    "genetics-12:mii-disomic": 0.04 * 1 / 4,
    "genetics-12:relative-risk": (12 / 1000) / (6 / 4000),
    "genetics-12:risk-difference": (12 / 1000 - 6 / 4000) * 1000,
    "genetics-13:events-per-culture": -math.log(22 / 50),
    "genetics-13:rate-per-1e9": -math.log(22 / 50) / 2e8 * 1e9,
    "genetics-13:variance-to-mean": (sum((x - 2.0) ** 2 for x in [0, 1, 0, 2, 0, 0, 13, 0]) / 7) / 2.0,
    "genetics-13:coding-mutations": 40 * 75 * 0.015,
    "genetics-14:cpm": 450 / 25_000_000 * 1e6,
    "genetics-14:log2-fold-change": math.log2((450 / 25_000_000) / (300 / 15_000_000)),
    "genetics-14:false-positives": 20_000 * 0.05,
    "genetics-14:bh-discoveries": benjamini_hochberg_count([0.001, 0.008, 0.020, 0.021, 0.024, 0.2, 0.35, 0.6, 0.8, 0.9], 0.05),
    "genetics-15:top-pip": 600 / (600 + 300 + 60 + 30 + 10),
    "genetics-15:credible-set-size": credible_set_size([600, 300, 60, 30, 10], 0.95),
    "genetics-15:ase-z": (140 - 100) / math.sqrt(200 * 0.25),
    "genetics-lab1:chi-square-syn1": (52 - 40) ** 2 / 40 + (48 - 60) ** 2 / 60 + (28 - 40) ** 2 / 40 + (72 - 60) ** 2 / 60,
    "genetics-lab1:bonferroni": 0.05 / 3,
}


def _nernst_mv(out: float, inside: float) -> float:
    return 8.314 * 310.15 / 96485 * 1000 * math.log(out / inside)


def _ghk_mv(k_out: float) -> float:
    return 8.314 * 310.15 / 96485 * 1000 * math.log((1.0 * k_out + 0.04 * 145) / (1.0 * 140 + 0.04 * 12))


def _parallel(*resistances: float) -> float:
    return 1 / sum(1 / r for r in resistances)


_B_BEDS = (40, 90, 240)
_B_CHALLENGE = (40, 45, 240)
_Q_B = (100 - 4) / _parallel(*_B_BEDS)
_HILL_B, _HILL_A, _HILL_F0 = 0.1, 0.25 * 500, 500.0          # m/s, N, N
_F_STAR = (math.sqrt(0.25 * 1.25) - 0.25) * _HILL_F0
_P_STAR = _F_STAR * _HILL_B * (_HILL_F0 - _F_STAR) / (_F_STAR + _HILL_A)

PHYSIOLOGY_NUMERIC = {
    # items written before 2026-10-08, recomputed from the numbers in their prompts
    "physiology-1:check": 12 / (0.3 * 2),
    "physiology-2:check": 4 * (-50 - 50),
    "physiology-4:check": 24 * 1.5 / 3,
    "physiology-2:ionic-current": 10 * (-40 - (-90)) / 1000,
    "physiology-5:arterial-content": 1.34 * 15 * 0.98 + 0.003 * 100,
    "physiology-5:fick-output": 250 / ((20.00 - 15.20) * 10),
    "physiology-5:extraction-ratio": 250 / (5.21 * 200),
    "physiology-5:anemia-extraction": 250 / (5.21 * 134.3),
    "physiology-6:inulin-gfr": 30 * 1.0 / 0.25,
    "physiology-6:filtration-fraction": 120 / 600,
    "physiology-6:glucose-excretion": 120 * 4.0 - 375,
    "physiology-6:drug-clearance": 2.4 * 1.0 / 0.04,
    "physiology-7:arterial-net": (35 - 0) - 0.9 * (25 - 5),
    "physiology-7:venous-net": (15 - 0) - 0.9 * (25 - 5),
    "physiology-7:filtration-rate": 0.5 * 7,
    "physiology-7:low-albumin": (35 - 0) - 0.9 * (15 - 5),
    # physiology 0.4.0
    "physiology-8:time-constant": 14 / 7,
    "physiology-8:new-steady-state": 35 / 3.5,
    "physiology-8:time-to-90": (14 / 3.5) * math.log(10),
    "physiology-8:temperature-rise": (1.5 * 20 - 0.2 * 1.5 * 20 - 0.25 * 20) / (70 * 3.5),
    "physiology-8:closed-loop-deviation": 10 / (1 + 4),
    "physiology-8:gain-estimate": 12 / 3 - 1,
    "physiology-9:nernst-k": _nernst_mv(5, 140),
    "physiology-9:nernst-na": _nernst_mv(145, 12),
    "physiology-9:ghk-rest": _ghk_mv(5),
    "physiology-9:ghk-high-k": _ghk_mv(8),
    "physiology-9:chord-conductance": (1.0 * _nernst_mv(5, 140) + 0.15 * _nernst_mv(145, 12)) / 1.15,
    "physiology-10:cardiac-output": 80 * 60 / 1000,
    "physiology-10:tpr": (100 - 4) / 4.8,
    "physiology-10:parallel-resistance": _parallel(40, 60, 120),
    "physiology-10:bed-flow": (100 - 4) / 60,
    "physiology-10:radius-halved": 2**4,
    "physiology-10:pulse-pressure": 60 / 1.2,
    "physiology-11:alveolar-ventilation": (250 - 150) * 24 / 1000,
    "physiology-11:halved-va": 0.863 * 200 / (4.2 / 2),
    "physiology-11:pao2-room-air": 0.21 * (760 - 47) - 40 / 0.8,
    "physiology-11:pao2-hypoventilation": 0.21 * (760 - 47) - 80 / 0.8,
    "physiology-11:stiff-lung-compliance": 1 / (1 / 50 + 1 / 200),
    "physiology-11:shunt-fraction": (20.1 - 19.0) / (20.1 - 15.2),
    "physiology-12:isometric-force": 25 * 20,
    "physiology-12:length-tension": (3.6 - 3.0) / (3.6 - 2.2),
    "physiology-12:half-load-velocity": 100 * _HILL_B * (_HILL_F0 - 250) / (250 + _HILL_A),
    "physiology-12:half-load-power": 250 * _HILL_B * (_HILL_F0 - 250) / (250 + _HILL_A),
    "physiology-12:peak-power": _P_STAR,
    "physiology-12:smaller-muscle": 0.7 * _P_STAR,
    "physiology-13:closure-time": 500 / (2 * 25),
    "physiology-13:percent-closed": 2 * 25 * 6 / 500 * 100,
    "physiology-13:slowed-closure": 500 / (2 * 25 * 0.6),
    "physiology-13:edge-speed": 0.40 * 400 / 2 / 8,
    "physiology-13:half-time": math.log(2) / 0.1,
    "physiology-14:co-b": _Q_B,
    "physiology-14:renal-flow-b": (100 - 4) / 240,
    "physiology-14:extraction-b": 250 / (_Q_B * 200),
    "physiology-14:reserve-b": 4.5 - _Q_B,
    "physiology-14:challenge-co-needed": (100 - 4) / _parallel(*_B_CHALLENGE),
    "physiology-14:map-b-challenge": 4.5 * _parallel(*_B_CHALLENGE) + 4,
    "physiology-lab1:relative-closure": (100 - 74) / (100 - 47),
    "physiology-lab1:edge-speed": (100 - 47) / 100 * 400 / 2 / 12,
    "physiology-lab1:division-block": (100 - 7) / (100 - 4),
}


def _least_squares_lb(condition: str) -> tuple[float, float]:
    """Vmax and Km from an ordinary least-squares fit of 1/mean rate on 1/[S], read from the lab CSV."""
    import csv
    rows = list(csv.DictReader((COURSES / "biochemistry/labs/enzyme-kinetics-rates.csv").open(encoding="utf-8")))
    substrates = sorted({float(r["substrate_um"]) for r in rows})
    means = [
        sum(float(r["rate_um_per_min"]) for r in rows if r["condition"] == condition and float(r["substrate_um"]) == s)
        / sum(1 for r in rows if r["condition"] == condition and float(r["substrate_um"]) == s)
        for s in substrates
    ]
    x, y = [1 / s for s in substrates], [1 / v for v in means]
    mx, my = sum(x) / len(x), sum(y) / len(y)
    slope = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    intercept = my - slope * mx
    return 1 / intercept, slope / intercept


_KM_CTRL = _least_squares_lb("control")[1]
_KM_INH = _least_squares_lb("inhibitor")[1]
_RT25 = 8.314 * 298.15 / 1000
_AK_AMP = 0.3**2 / 3.0
_PROT = lambda ph, pka: 1 / (1 + 10 ** (ph - pka))       # noqa: E731  protonated fraction of a base
_DEPROT = lambda ph, pka: 1 / (1 + 10 ** (pka - ph))     # noqa: E731  deprotonated fraction of an acid

BIOCHEMISTRY_NUMERIC = {
    # items written before 2026-10-08, recomputed from the numbers in their prompts
    "biochemistry-1:check": 12 / (4 + 12),
    "biochemistry-3:check": 5 * 2,
    "biochemistry-2:catalytic-efficiency": 500 / 25e-6,
    "biochemistry-5:rate-at-20": 100 * 20 / (5 + 20),
    "biochemistry-5:kcat": 100 / 0.01 / 60,
    "biochemistry-5:competitive-km": 5 * (1 + 4 / 2),
    "biochemistry-5:noncompetitive-rate": (100 / 3) * 20 / (5 + 20),
    "biochemistry-6:atp-actual-dg": -30.5 + 2.577 * math.log((0.3e-3 * 3.0e-3) / 3.0e-3),
    "biochemistry-6:coupled-dg0": 13.8 + (-30.5),
    "biochemistry-6:equilibrium-constant": math.exp(-13.8 / 2.577),
    "biochemistry-6:nadh-oxygen": -2 * 96.485 * (0.815 - (-0.320)),
    "biochemistry-7:occupancy": 30 / (10 + 30),
    "biochemistry-7:depletion": (110 - math.sqrt(110**2 - 4 * 50 * 50)) / 2,
    "biochemistry-7:hill-40": 100 * 40**2.8 / (26**2.8 + 40**2.8),
    "biochemistry-7:unloading": (97.8 - 77.0) - 3.8,
    # biochemistry 0.4.0
    "biochemistry-8:lys-protonated": _PROT(7.4, 10.5),
    "biochemistry-8:his-protonated": _PROT(7.4, 6.0),
    "biochemistry-8:pi-alanine": (2.34 + 9.69) / 2,
    "biochemistry-8:pi-glutamate": (2.2 + 4.25) / 2,
    "biochemistry-8:lysine-charge": _PROT(7.4, 8.95) + _PROT(7.4, 10.53) - _DEPROT(7.4, 2.18),
    "biochemistry-9:k-unfold": math.exp(-10 / _RT25),
    "biochemistry-9:fraction-folded": 1 / (1 + 0.0177),
    "biochemistry-9:midpoint": 25 / 10,
    "biochemistry-9:dg-at-2m": 25 - 10 * 2.0,
    "biochemistry-9:mutation-fold": math.exp(8 / _RT25),
    "biochemistry-10:amp-from-ak": _AK_AMP,
    "biochemistry-10:energy-charge": (3.0 + 0.5 * 0.3) / (3.0 + 0.3 + _AK_AMP),
    "biochemistry-10:amp-fold": (0.527**2 / 2.7) / _AK_AMP,
    "biochemistry-10:glucose-for-atp": 6.0 / 2,
    "biochemistry-10:pfk-fold": (1 / (1 + (0.5 / 1.0) ** 2.5)) / (1 / (1 + (2.0 / 1.0) ** 2.5)),
    "biochemistry-11:pmf": 150 + 61.5 * 0.75,
    "biochemistry-11:energy-per-proton": 96.485 * 0.1961,
    "biochemistry-11:min-protons": 51.4 / 18.9,
    "biochemistry-11:atp-per-glucose": 4 + 10 * (10 / 4) + 2 * (6 / 4),
    "biochemistry-11:leak-yield": 4 + (10 * 2.5 + 2 * 1.5) * 0.75,
    "biochemistry-11:atp-rate": 0.25 / 22.4 * 1000 * 5.3,
    "biochemistry-12:pool-k1-doubled": (2 * 2.0) / 0.5,
    "biochemistry-12:flux-k2-halved": 2.0,
    "biochemistry-12:missing-coefficient": 1 - (0.50 + 0.25 + 0.15),
    "biochemistry-12:flux-increase-e1": 0.50 * 20,
    "biochemistry-12:turnover-time": math.log(10) / (math.log(2) / 2.0),
    "biochemistry-13:baseline-glucose": 0.9 * 6.4 / 32 + 0.1 * 6.4 / 2,
    "biochemistry-13:glucose-after-block": 6.4 / 2,
    "biochemistry-13:lactate-fold": 6.4 / (0.1 * 6.4 / 2 * 2),
    "biochemistry-13:nadh-fold": 40 / 10,
    "biochemistry-13:tracer-fraction": 0.48 / 0.5,
    "biochemistry-lab1:km-control": _KM_CTRL,
    "biochemistry-lab1:km-apparent": _KM_INH,
    "biochemistry-lab1:inhibition-constant": 4 / (_KM_INH / _KM_CTRL - 1),
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
    allowed = spec["tolerance"] + (spec.get("relative_tolerance") or 0) * abs(spec["answer"])
    assert abs(spec["answer"] - expected) <= allowed, (question_id, spec["answer"], expected)


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


@pytest.mark.parametrize("question_id,expected", sorted(PHYSIOLOGY_NUMERIC.items()))
def test_physiology_numeric_key_matches_independent_recalculation(question_id, expected):
    spec = bank("physiology")[question_id]["solution_spec"]
    allowed = spec["tolerance"] + (spec.get("relative_tolerance") or 0) * abs(spec["answer"])
    assert abs(spec["answer"] - expected) <= allowed, (question_id, spec["answer"], expected)


def test_every_physiology_numeric_item_is_recalculated():
    numeric = {qid for qid, item in bank("physiology").items() if item["type"] == "numeric"}
    assert numeric == set(PHYSIOLOGY_NUMERIC)


def test_physiology_hemodynamic_and_compensation_statements_in_the_lessons():
    text = reading("physiology", "physiology-14")
    parallel = _parallel(*_B_BEDS)
    assert f"R_total = {parallel:.1f}" in text
    assert f"{_Q_B:.2f} L/min" in text
    assert f"{_parallel(*_B_CHALLENGE):.1f}" in text
    f_max_a, f_max_b = 1 - 80 / 150, 1 - 100 / 150
    assert f"{f_max_a:.2f}" in text and f"{f_max_b:.2f}" in text


def test_hill_peak_power_is_at_the_load_the_lesson_states():
    f0, a, b = 500.0, 125.0, 0.1                      # N, N, m/s (muscle lesson)

    def power(force: float) -> float:
        return force * b * (f0 - force) / (force + a)

    best_force = max((x / 10 for x in range(1, 5000)), key=power)
    analytic = (math.sqrt(0.25 * 1.25) - 0.25) * f0
    assert abs(best_force - analytic) < 0.2
    assert abs(power(best_force) - power(analytic)) < 1e-3
    text = reading("physiology", "physiology-12")
    assert f"F* = {analytic / f0:.3f} F₀ = {analytic:.1f} N" in text


@pytest.mark.parametrize("question_id,expected", sorted(BIOCHEMISTRY_NUMERIC.items()))
def test_biochemistry_numeric_key_matches_independent_recalculation(question_id, expected):
    spec = bank("biochemistry")[question_id]["solution_spec"]
    allowed = spec["tolerance"] + (spec.get("relative_tolerance") or 0) * abs(spec["answer"])
    assert abs(spec["answer"] - expected) <= allowed, (question_id, spec["answer"], expected)


def test_every_biochemistry_numeric_item_is_recalculated():
    numeric = {qid for qid, item in bank("biochemistry").items() if item["type"] == "numeric"}
    assert numeric == set(BIOCHEMISTRY_NUMERIC)


def test_biochemistry_lab_fit_recovers_the_parameters_the_data_were_built_from():
    vmax, km = _least_squares_lb("control")
    assert abs(vmax - 100.0) < 0.5 and abs(km - 5.0) < 0.05
    assert abs(_KM_INH - 15.0) < 0.2 and abs(4 / (_KM_INH / _KM_CTRL - 1) - 2.0) < 0.1
    field = bank("biochemistry")["biochemistry-lab1:control-fit"]["solution_spec"]["field_specs"][0]
    assert abs(field["answer"] - vmax) < 0.05


# ---- statistics 0.4.0 ----------------------------------------------------------------------------------------
# Student's t is evaluated by integrating over the chi-square mixing distribution above, which does not share code
# with the scipy functions that produced the stored keys.


@functools.lru_cache(maxsize=None)
def _t_cdf(t: float, df: float) -> float:
    return _over_chi2(df, lambda v: _phi(t * math.sqrt(v / df)))


def _two_sided_p(t: float, df: float) -> float:
    return 2 * (1 - _t_cdf(abs(t), df))


@functools.lru_cache(maxsize=None)
def _t_quantile(p: float, df: float) -> float:
    low, high = 0.0, 40.0
    for _ in range(50):
        mid = (low + high) / 2
        low, high = (mid, high) if _t_cdf(mid, df) < p else (low, mid)
    return (low + high) / 2


def _z_quantile(p: float) -> float:
    low, high = 0.0, 10.0
    for _ in range(60):
        mid = (low + high) / 2
        low, high = (mid, high) if _phi(mid) < p else (low, mid)
    return (low + high) / 2


def _ols(xs: list[float], ys: list[float]) -> tuple[float, float, float, float]:
    """Slope, intercept, R squared and standard error of the slope for ordinary least squares."""
    n, mx, my = len(xs), sum(xs) / len(xs), sum(ys) / len(ys)
    sxx = sum((x - mx) ** 2 for x in xs)
    slope = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sxx
    intercept = my - slope * mx
    sse = sum((y - intercept - slope * x) ** 2 for x, y in zip(xs, ys))
    sst = sum((y - my) ** 2 for y in ys)
    return slope, intercept, 1 - sse / sst, math.sqrt(sse / (n - 2)) / math.sqrt(sxx)


_KM_TIMES = [2, 3, 4, 5, 6, 8, 9, 10, 12, 12]
_KM_EVENTS = [1, 1, 0, 1, 0, 1, 0, 1, 0, 0]


def _km_survival(at: float) -> float:
    survival = 1.0
    for t in sorted({t for t, e in zip(_KM_TIMES, _KM_EVENTS) if e and t <= at}):
        at_risk = sum(1 for u in _KM_TIMES if u >= t)
        deaths = sum(1 for u, e in zip(_KM_TIMES, _KM_EVENTS) if e and u == t)
        survival *= 1 - deaths / at_risk
    return survival


_P10 = [0.001, 0.004, 0.012, 0.02, 0.031, 0.04, 0.18, 0.33, 0.52, 0.81]
_CAL_X, _CAL_Y = [0, 2, 4, 6, 8, 10], [6.0, 24.0, 47.5, 62.0, 88.5, 101.0]
_SLOPE, _INTERCEPT, _R2, _SE_SLOPE = _ols(_CAL_X, _CAL_Y)
_CONTROL, _TREATED = [12, 15, 14, 16], [18, 20, 17, 21]
_RANK = {v: i + 1 for i, v in enumerate(sorted(_CONTROL + _TREATED))}
_ARRANGEMENT_SUMS = [sum(c) for c in itertools.combinations(range(1, 9), 4)]
_T10 = _t_quantile(0.975, 10)
_SE_6 = 2.2 * math.sqrt(2 / 6)
_SE_WELCH = math.sqrt(2.0 ** 2 / 6 + 2.4 ** 2 / 6)
_DF_WELCH = (2.0 ** 2 / 6 + 2.4 ** 2 / 6) ** 2 / ((2.0 ** 2 / 6) ** 2 / 5 + (2.4 ** 2 / 6) ** 2 / 5)
_SB, _ST = 8.5, 5.0                                   # statistics-15: between-animal and technical SD


def _animals_needed(readings: int, z_alpha: float = 1.96, delta: float = 5.0) -> float:
    return 2 * (z_alpha + 0.8416) ** 2 * (_SB ** 2 + _ST ** 2 / readings) / delta ** 2


def _ppv(power: float, prior: float, alpha: float = 0.05) -> float:
    true_positive, false_positive = 1_000_000 * prior * power, 1_000_000 * (1 - prior) * alpha
    return true_positive / (true_positive + false_positive)


def _lab_statistics() -> dict[str, float]:
    import csv
    rows = list(csv.DictReader((COURSES / "statistics/labs/nested-biomarker-readings.csv").open(encoding="utf-8")))
    animals = {a: [float(r["value_au"]) for r in rows if r["animal_id"] == a] for a in dict.fromkeys(r["animal_id"] for r in rows)}
    group_of = {r["animal_id"]: r["group"] for r in rows}
    means = {a: sum(v) / len(v) for a, v in animals.items()}
    ss_within = sum((x - means[a]) ** 2 for a, v in animals.items() for x in v)
    ms_within = ss_within / sum(len(v) - 1 for v in animals.values())

    def pooled_variance(samples: list[list[float]]) -> float:
        total = df = 0.0
        for sample in samples:
            m = sum(sample) / len(sample)
            total += sum((x - m) ** 2 for x in sample)
            df += len(sample) - 1
        return total / df

    groups = sorted(set(group_of.values()))
    animal_means = [[means[a] for a in animals if group_of[a] == g] for g in groups]
    reading_groups = [[float(r["value_au"]) for r in rows if r["group"] == g] for g in groups]
    ms_animals = 3 * pooled_variance(animal_means)
    sigma_b2 = (ms_animals - ms_within) / 3
    diff = sum(animal_means[1]) / len(animal_means[1]) - sum(animal_means[0]) / len(animal_means[0])
    t_reading = diff / math.sqrt(pooled_variance(reading_groups) * 2 / len(reading_groups[0]))
    t_animal = diff / math.sqrt(pooled_variance(animal_means) * 2 / len(animal_means[0]))
    grand = sum(sum(g) for g in reading_groups) / sum(len(g) for g in reading_groups)
    ms_group = len(reading_groups[0]) * sum((sum(g) / len(g) - grand) ** 2 for g in reading_groups) / (len(groups) - 1)
    return {"ms_group": ms_group, "ms_animals": ms_animals, "sd_t": math.sqrt(ms_within), "icc": sigma_b2 / (sigma_b2 + ms_within), "t_reading": t_reading, "t_animal": t_animal,
            "df_reading": 2 * len(reading_groups[0]) - 2, "df_animal": 2 * len(animal_means[0]) - 2, "diff": diff, "n_rows": len(rows)}


_LAB = _lab_statistics()

STATISTICS_NUMERIC = {
    # items written before 2026-10-08, recomputed from the numbers in their prompts
    "statistics-1:check": 10 / math.sqrt(25),
    "statistics-1:standard-error": 12 / math.sqrt(36),
    "statistics-3:check": 100 * (1 - 0.95 ** 10),
    "statistics-3:bonferroni": 0.05 / 20,
    "statistics-6:km-at-5": _km_survival(5),
    "statistics-6:km-at-8": _km_survival(8),
    "statistics-6:median-survival": min(t for t, e in zip(_KM_TIMES, _KM_EVENTS) if e and _km_survival(t) <= 0.5),
    "statistics-6:rate-ratio": (12 / 480) / (20 / 400),
    "statistics-7:fwer": 1 - 0.95 ** 20,
    "statistics-7:expected-fp": 1000 * 0.05,
    "statistics-7:bonferroni-count": sum(p <= 0.05 / len(_P10) for p in _P10),
    "statistics-7:bh-count": benjamini_hochberg_count(_P10, 0.05),
    "statistics-8:standard-error": 3.0 * math.sqrt(2 / 20),
    "statistics-8:ci-upper": 1.5 + _t_quantile(0.975, 38) * 3.0 * math.sqrt(2 / 20),
    "statistics-8:cohens-d": 1.5 / 3.0,
    "statistics-8:larger-n-se": 3.0 * math.sqrt(2 / 80),
    "statistics-8:regression-to-mean": 100 + 0.7 * (130 - 100),
    # statistics-9: variability
    "statistics-9:technical-sd": 7.07 / math.sqrt(2),
    "statistics-9:naive-se": math.sqrt(10 ** 2 + 5 ** 2) / math.sqrt(12),
    "statistics-9:correct-se": math.sqrt(10 ** 2 / 4 + 5 ** 2 / 12),
    "statistics-9:icc": 10 ** 2 / (10 ** 2 + 5 ** 2),
    "statistics-9:effective-n": 12 / (1 + (3 - 1) * 0.8),
    # statistics-10: comparing two groups
    "statistics-10:se-difference": _SE_WELCH,
    "statistics-10:t-statistic": (13.0 - 10.2) / _SE_WELCH,
    "statistics-10:welch-df": _DF_WELCH,
    "statistics-10:cohens-d": 2.8 / math.sqrt((2.0 ** 2 + 2.4 ** 2) / 2),
    "statistics-10:paired-t": 2.8 / (1.5 / math.sqrt(6)),
    # statistics-11: power and sample size
    "statistics-11:signal-to-noise": 2.8 / _SE_6,
    "statistics-11:n-80": 2 * Z80 ** 2 * 2.2 ** 2 / 2.8 ** 2,
    "statistics-11:n-half-effect": 2 * Z80 ** 2 * 2.2 ** 2 / 1.4 ** 2,
    "statistics-11:min-significant": _T10 * _SE_6,
    "statistics-11:exaggeration": _T10 * _SE_6 / 1.4,
    # statistics-12: regression and calibration
    "statistics-12:slope": _SLOPE,
    "statistics-12:intercept": _INTERCEPT,
    "statistics-12:r-squared": _R2,
    "statistics-12:se-slope": _SE_SLOPE,
    "statistics-12:inverse-prediction": (55 - _INTERCEPT) / _SLOPE,
    # statistics-13: resampling
    "statistics-13:n-arrangements": math.comb(8, 4),
    "statistics-13:exact-p": sum(1 for total in _ARRANGEMENT_SUMS if total <= 10 or total >= 26) / math.comb(8, 4),
    "statistics-13:bootstrap-inclusion": 1 - (1 - 1 / 10) ** 10,
    "statistics-13:rank-sum": sum(_RANK[v] for v in _TREATED),
    "statistics-13:u-statistic": sum(1 for c in _CONTROL for t in _TREATED if c > t),
    # statistics-14: base rates
    "statistics-14:ppv-test": (10_000 * 0.02 * 0.90) / (10_000 * 0.02 * 0.90 + 10_000 * 0.98 * 0.05),
    "statistics-14:lr-positive": 0.90 / (1 - 0.95),
    "statistics-14:ppv-study": _ppv(0.5, 0.10),
    "statistics-14:ppv-high-power": _ppv(0.8, 0.10),
    "statistics-14:ppv-rare": _ppv(0.8, 0.01),
    "statistics-14:replication-probability": _ppv(0.5, 0.10) * 0.5 + (1 - _ppv(0.5, 0.10)) * 0.05,
    # statistics-15: planning a confirmatory study (the sample-size keys are the rounded-up values)
    "statistics-15:any-false-positive": 1 - 0.95 ** 18,
    "statistics-15:bonferroni-threshold": 0.05 / 18,
    "statistics-15:animal-t": 7.0 / (math.sqrt(_SB ** 2 + _ST ** 2 / 3) * math.sqrt(2 / 6)),
    "statistics-15:n-triplicate": _animals_needed(3),
    "statistics-15:n-single-reading": _animals_needed(1),
    "statistics-15:n-all-eighteen": _animals_needed(3, z_alpha=2.99),
    "statistics-15:optimal-readings": math.sqrt(_ST ** 2 * 20 / (_SB ** 2 * 1)),
    # virtual lab 1, recomputed from the CSV
    "statistics-lab1:technical-sd": _LAB["sd_t"],
    "statistics-lab1:intraclass-correlation": _LAB["icc"],
}


@pytest.mark.parametrize("question_id,expected", sorted(STATISTICS_NUMERIC.items()))
def test_statistics_numeric_key_matches_independent_recalculation(question_id, expected):
    spec = bank("statistics")[question_id]["solution_spec"]
    allowed = spec["tolerance"] + (spec.get("relative_tolerance") or 0) * abs(spec["answer"])
    assert abs(spec["answer"] - expected) <= allowed, (question_id, spec["answer"], expected)


def test_every_statistics_numeric_item_is_recalculated():
    numeric = {qid for qid, item in bank("statistics").items() if item["type"] == "numeric"}
    assert numeric == set(STATISTICS_NUMERIC)


def test_statistics_quoted_p_values_match_an_independent_t_distribution():
    comparing = reading("statistics", "statistics-10")
    t_welch = 2.8 / _SE_WELCH
    assert f"{_two_sided_p(t_welch, _DF_WELCH):.3f}" == "0.054" and "0.054" in comparing
    assert f"{_two_sided_p(2.8 / (1.5 / math.sqrt(6)), 5):.3f}" == "0.006" and "p ≈ 0.006" in comparing
    se_worked = math.sqrt(5.0 ** 2 / 8 + 7.0 ** 2 / 8)
    df_worked = (5.0 ** 2 / 8 + 7.0 ** 2 / 8) ** 2 / ((5.0 ** 2 / 8) ** 2 / 7 + (7.0 ** 2 / 8) ** 2 / 7)
    assert f"{df_worked:.2f}" == "12.67" and f"{_two_sided_p(6.0 / se_worked, df_worked):.3f}" == "0.071"
    assert "Welch df = 12.67, p ≈ 0.071" in comparing
    planning = reading("statistics", "statistics-15")
    sd_reading, sd_animal = math.sqrt(_SB ** 2 + _ST ** 2), math.sqrt(_SB ** 2 + _ST ** 2 / 3)
    t_naive, t_animal = 7.0 / (sd_reading * math.sqrt(2 / 18)), 7.0 / (sd_animal * math.sqrt(2 / 6))
    assert f"p = {_two_sided_p(t_naive, 34):.3f}" == "p = 0.041" and "p = 0.041" in planning
    assert f"p = **{_two_sided_p(t_animal, 10):.2f}**" in planning
    assert f"**{_T10 * sd_animal * math.sqrt(2 / 6):.1f}** units" in planning


def test_statistics_power_statements_match_the_exact_t_test():
    power = reading("statistics", "statistics-11")
    assert two_sample_t_power(6, 2.2, 2.8) == pytest.approx(0.5126, abs=0.002) and "power 0.51" in power
    assert f"{two_sample_t_power(6, 2.2, 1.4):.2f}" == "0.17" and "0.17 for a true δ of 1.4" in power
    assert two_sample_t_power(10, 2.2, 2.8) < 0.80 <= two_sample_t_power(11, 2.2, 2.8)
    assert "the exact t calculation asks for 11" in power
    assert two_sample_t_power(38, 2.2, 1.4) < 0.80 and "about 39 or more with the exact test" in power
    planning = reading("statistics", "statistics-15")
    sd = math.sqrt(_SB ** 2 + _ST ** 2 / 3)
    assert two_sample_t_power(51, sd, 5.0) < 0.80 <= two_sample_t_power(52, sd, 5.0)
    assert "needs 52 animals per group for m = 3" in planning
    assert f"{two_sample_t_power(6, sd, 5.0):.2f}" == "0.14" and "would have been only 0.14" in planning


def test_statistics_planning_table_and_critical_value_in_the_capstone():
    planning = reading("statistics", "statistics-15")
    assert [math.ceil(_animals_needed(m)) for m in (1, 3, 6)] == [62, 51, 48]
    assert math.ceil(_animals_needed(3, z_alpha=2.99)) == 95 and math.ceil(_animals_needed(3) * 1.25 ** 2) == 80
    assert abs(_z_quantile(1 - 0.05 / 36) - 2.99) < 0.005
    for row in ("| 1 | 97.25 | 62 |", "| 3 | 80.58 | 51 |", "| 6 | 76.42 | 48 |"):
        assert row in planning
    assert "is m = √" in planning and "= **2.63**" in planning


def test_statistics_lab_interpretation_keys_and_nested_f_test_match_the_dataset():
    fields = {q: bank("statistics")[q]["solution_spec"]["field_specs"][0] for q in ("statistics-lab1:reading-level-test", "statistics-lab1:animal-level-test")}
    assert abs(fields["statistics-lab1:reading-level-test"]["answer"] - _LAB["t_reading"]) <= fields["statistics-lab1:reading-level-test"]["tolerance"]
    assert abs(fields["statistics-lab1:animal-level-test"]["answer"] - _LAB["t_animal"]) <= fields["statistics-lab1:animal-level-test"]["tolerance"]
    assert all(f["significant_figures"] == 3 for f in fields.values())
    assert _LAB["n_rows"] == 24 and _LAB["diff"] == pytest.approx(8.0)
    lab = (COURSES / "statistics/labs/01-pseudoreplication-and-nested-designs.md").read_text(encoding="utf-8")
    assert f"p = {_two_sided_p(_LAB['t_reading'], _LAB['df_reading']):.4f}" in lab
    assert f"p = {_two_sided_p(_LAB['t_animal'], _LAB['df_animal']):.3f}" in lab
    # balanced nested analysis of variance: F for groups equals the square of the animal-level t statistic
    f_nested = _LAB["ms_group"] / _LAB["ms_animals"]
    assert f_nested == pytest.approx(_LAB["t_animal"] ** 2, rel=1e-9)
    assert f"{_LAB['ms_group']:.0f}/{_LAB['ms_animals']:.0f} = {f_nested:.2f}" in lab


def test_statistics_base_rate_lesson_states_the_natural_frequencies():
    text = reading("statistics", "statistics-14")
    true_positive, false_positive = 10_000 * 0.02 * 0.90, 10_000 * 0.98 * 0.05
    assert f"**{true_positive:.0f} true positives**" in text and f"**{false_positive:.0f} false positives**" in text
    assert f"Of the {true_positive + false_positive:.0f} positive tests, {true_positive:.0f} are true" in text
    assert f"{true_positive / (true_positive + false_positive):.3f}" in text
    assert f"{_ppv(0.5, 0.10):.3f}" in text and f"{_ppv(0.8, 0.01):.2f}" in text


def test_statistics_worked_examples_and_lesson_statements_agree_with_the_arithmetic():
    # lesson 9: variability
    text = reading("statistics", "statistics-9")
    correct = math.sqrt(6 ** 2 / 5 + 6 ** 2 / (5 * 2))
    naive = math.sqrt(6 ** 2 + 6 ** 2) / math.sqrt(10)
    deff = 1 + (2 - 1) * 0.5
    for fragment in (f"{correct:.2f}", f"{naive:.2f}", f"{correct / naive:.2f} times too small", f"DEFF = 1 + (2 − 1) × 0.50 = {deff:.2f}", f"n_eff = 10/{deff:.2f} = {10 / deff:.1f}"):
        assert fragment in text, fragment
    assert f"{math.sqrt(10 ** 2 / 4 + 5 ** 2 / 4):.2f}" in text and f"{math.sqrt(10 ** 2 / 12 + 5 ** 2 / 12):.2f}" in text
    assert f"{(100 + 25 / 3) / 9:.2f}" not in text and "n = (100 + 25/3)/9 = 12 animals" in text
    assert f"{10 ** 2 / (10 ** 2 + 5 ** 2 / 3):.0%}" == "92%" and "92%" in text
    # lesson 11: worked example
    text = reading("statistics", "statistics-11")
    assert f"{2 * Z80 ** 2 * 3 ** 2 / 2 ** 2:.1f}" == "35.3" and "35.3, so at least 36 per group" in text
    se = 3 * math.sqrt(2 / 6)
    assert f"{_phi(2 / se - 1.96):.2f}" == "0.21" and "Φ(−0.81) = 0.21" in text and f"{2 / se - 1.96:.2f}" == "-0.81"
    assert f"{Z80 * se:.2f}" == "4.85" and f"{_phi(2.8 / _SE_6 - 1.96):.2f}" == "0.60"
    # lesson 12: regression
    text = reading("statistics", "statistics-12")
    s = _SE_SLOPE * math.sqrt(70)
    x_hat = (55 - _INTERCEPT) / _SLOPE
    se_x = s / abs(_SLOPE) * math.sqrt(1 + 1 / 6 + (x_hat - 5) ** 2 / 70)
    t4 = _t_quantile(0.975, 4)
    assert f"= {se_x:.3f}" in text and f"±{t4 * se_x:.2f} μM" in text
    assert f"({_SLOPE - t4 * _SE_SLOPE:.2f}, {_SLOPE + t4 * _SE_SLOPE:.2f})" in text and f"{s:.3f}" in text
    assert f"{_INTERCEPT + _SLOPE * 20:.0f}" == "201" and "gives 201" in text
    b, a, r2_saturating, _ = _ols(_CAL_X, [0, 18, 33, 44, 52, 57])
    residuals = [y - (a + b * x) for x, y in zip(_CAL_X, [0, 18, 33, 44, 52, 57])]
    assert f"R² = {r2_saturating:.3f}" in text
    assert "(" + ", ".join(f"{r:+.1f}".replace("-", "−") for r in residuals) + ")" in text
    assert [(r > 0) for r in residuals] == [False, True, True, True, True, False]
    wb, wa, wr2, wse = _ols([1, 2, 3, 4, 5], [3.1, 4.9, 7.2, 8.8, 11.1])
    assert (round(wb, 2), round(wa, 2), f"{wr2:.4f}", f"{wse:.3f}") == (1.99, 1.05, "0.9973", "0.060")
    assert "R² = 1 − 0.107/39.708 = 0.9973" in text and "SE(b) = 0.189/√10 = 0.060" in text
    # lesson 13: resampling
    text = reading("statistics", "statistics-13")
    values = [11, 14, 13, 18, 15, 17, 16, 19]
    treated_mean = (15 + 17 + 16 + 19) / 4
    control_mean = (11 + 14 + 13 + 18) / 4
    observed = treated_mean - control_mean
    as_extreme = sum(
        1 for chosen in itertools.combinations(range(8), 4)
        if abs(sum(values[i] for i in chosen) / 4 - sum(values[i] for i in range(8) if i not in chosen) / 4) >= observed - 1e-12
    )
    assert (observed, as_extreme) == (2.75, 14) and "14 give a difference of at least 2.75" in text and "p = 14/70 = 0.20" in text
    ranks = {v: i + 1 for i, v in enumerate(sorted(values))}
    assert sorted(ranks[v] for v in (15, 17, 16, 19)) == [4, 5, 6, 8] and sum(ranks[v] for v in (11, 14, 13, 18)) == 13
    assert 4 ** 4 == 256 and [f"{1 - (1 - 1 / n) ** n:.3f}" for n in (4, 10)] == ["0.684", "0.651"]
    assert f"{1 - math.exp(-1):.3f}" == "0.632" and "0.684 for n = 4, 0.651 for n = 10" in text


def test_statistics_older_data_interpretation_key_matches_its_prompt():
    item = bank("statistics")["statistics-5:group-summary"]
    field = next(f for f in item["solution_spec"]["field_specs"] if f["id"] == "mean_difference")
    assert "vehicle n=8, mean 10.0 μM, and compound n=8, mean 14.0 μM" in item["prompt"]
    assert field["answer"] == pytest.approx(14.0 - 10.0)


# ---- biomaterials 0.3.0 --------------------------------------------------------------------------------------
_MMHG = 133.322
_R_GAS, _T_BODY, _K_B = 8.314, 310.0, 1.381e-23
_NA = 6.022e23


def _protein_capacity_mg_m2(kda: float, footprint_nm2: float) -> float:
    return kda / (_NA * footprint_nm2 * 1e-18) * 1e6


def _diffusion_arrival_time_s(gamma_mg_m2: float, d_um2_s: float, c_mg_ml: float) -> float:
    return math.pi * (gamma_mg_m2 * 1e-6 / (2 * c_mg_ml)) ** 2 / (d_um2_s * 1e-12)


def _bonds_cleaved(t: float, k: float) -> float:
    return 1 - math.exp(-k * t)


def _mn_scission(t: float, mn0: float, repeat: float, k: float) -> float:
    return 1 / (1 / mn0 + _bonds_cleaved(t, k) / repeat)


def _buckling_pa(e_pa: float, h: float, r: float, nu: float = 0.3) -> float:
    return e_pa / (4 * (1 - nu ** 2)) * (h / r) ** 3


def _wall_shear_pa(mu: float, q: float, r: float) -> float:
    return 4 * mu * q / (math.pi * r ** 3)


def _biomaterials_lab_rows() -> list[dict[str, str]]:
    import csv
    return list(csv.DictReader((COURSES / "biomaterials/labs/scaffold-degradation-time-course.csv").open(encoding="utf-8")))


def _lab_mean(rows: list[dict[str, str]], day: int, column: str) -> float:
    values = [float(r[column]) for r in rows if int(r["day"]) == day]
    return sum(values) / len(values)


_BM_ROWS = _biomaterials_lab_rows()
_BM_P28 = 72.0 * (1 / (_lab_mean(_BM_ROWS, 28, "mn_kda") * 1000) - 1 / (_lab_mean(_BM_ROWS, 0, "mn_kda") * 1000))
_BM_KE = math.log(_lab_mean(_BM_ROWS, 0, "modulus_mpa") / _lab_mean(_BM_ROWS, 56, "modulus_mpa")) / 56
_BM_CRIT_P = 72.0 * (1 / 5000.0 - 1 / 100000.0)
_BM_TC = -math.log(1 - _BM_CRIT_P) / 0.0002
_BM_A = [90, 98, 82, 105, 88, 95]
_BM_B = [78, 86, 70, 92, 74, 82]


def _pooled_sd(a: list[float], b: list[float]) -> float:
    def var(x: list[float]) -> float:
        m = sum(x) / len(x)
        return sum((v - m) ** 2 for v in x) / (len(x) - 1)
    return math.sqrt((var(a) + var(b)) / 2)


_BM_SE = _pooled_sd(_BM_A, _BM_B) * math.sqrt(2 / 6)
_BM_NEED = 5.0e7 * 2.0
_BM_SEED = _BM_NEED / 0.6
_BM_PH = 7.2 + math.log10((10 / (1 + 10 ** (7.2 - 7.4)) - 2) / (10 - 10 / (1 + 10 ** (7.2 - 7.4)) + 2))

BIOMATERIALS_NUMERIC = {
    # items written before 2026-10-08, recomputed from the numbers in their prompts
    "biomaterials-2:check": 100 * (1 - 0.15),
    "biomaterials-2:degradation-modulus": 2.0 * math.exp(-0.05 * 14),
    "biomaterials-5:half-life": math.log(2) / 0.05 * 24,
    "biomaterials-5:remaining-mass": 100 * math.exp(-0.05 * 30),
    "biomaterials-5:diffusion-time": (1e-3) ** 2 / 1e-10 / 3600,
    "biomaterials-5:thinner-slab": (0.5e-3) ** 2 / 1e-10 / 3600,
    "biomaterials-6:porosity": 100 * (1 - 0.10),
    "biomaterials-6:gibson-ashby": 1000 * 0.1 ** 2,
    "biomaterials-6:double-density": 1000 * 0.2 ** 2,
    "biomaterials-6:darcy-flow": 1e-10 * 1e-4 * 10 / (1e-3 * 5e-3) * 1e6 * 60,
    # biomaterials-7: protein adsorption
    "biomaterials-7:work-of-adhesion": 72 * (1 + math.cos(math.radians(65))),
    "biomaterials-7:contact-angle": math.degrees(math.acos((35 - 10) / 72)),
    "biomaterials-7:coverage": 0.2 / (0.05 + 0.2),
    "biomaterials-7:concentration-for-90": 0.9 * 0.05 / 0.1,
    "biomaterials-7:monolayer-capacity": _protein_capacity_mg_m2(66, 50),
    "biomaterials-7:arrival-time": _diffusion_arrival_time_s(1.5, 60, 0.2),
    "biomaterials-7:arrival-ratio": (40 * math.sqrt(61)) / (3 * math.sqrt(20)),
    # biomaterials-8: hydrogel networks
    "biomaterials-8:youngs-modulus": 3 * 12.0,
    "biomaterials-8:chain-density": 12000 / (_R_GAS * _T_BODY),
    "biomaterials-8:molar-mass-between-crosslinks": 100 / (12000 / (_R_GAS * _T_BODY)),
    "biomaterials-8:mesh-size": (_K_B * _T_BODY / 12000) ** (1 / 3) * 1e9,
    "biomaterials-8:mesh-after-doubling": (_K_B * _T_BODY / 24000) ** (1 / 3) * 1e9,
    "biomaterials-8:mesh-after-loss": (_K_B * _T_BODY / (0.6 * 12000)) ** (1 / 3) * 1e9,
    "biomaterials-8:free-diffusion": _K_B * _T_BODY / (6 * math.pi * 0.69e-3 * 3.5e-9) * 1e12,
    # biomaterials-9: chain scission
    "biomaterials-9:bonds-cleaved": 100 * _bonds_cleaved(28, 0.0002),
    "biomaterials-9:molar-mass": _mn_scission(28, 100000, 72, 0.0002),
    "biomaterials-9:onset-time": _BM_TC,
    "biomaterials-9:cleaved-at-onset": 100 * _BM_CRIT_P,
    "biomaterials-9:mass-at-100": 100 * math.exp(-0.02 * (100 - _BM_TC)),
    "biomaterials-9:critical-thickness": math.sqrt(0.0090 / 0.0002),
    # biomaterials-10: vascular scaffold mechanics
    "biomaterials-10:hoop-stress": 120 * _MMHG * 2.0 / 0.40 / 1000,
    "biomaterials-10:pulse-strain": 100 * 40 * _MMHG * 2.0 / (0.40 * 2.0e6),
    "biomaterials-10:buckling-pressure": _buckling_pa(2.0e6, 0.40e-3, 2.0e-3) / _MMHG,
    "biomaterials-10:thin-wall-buckling": _buckling_pa(2.0e6, 0.20e-3, 2.0e-3) / _MMHG,
    "biomaterials-10:time-to-threshold": math.log(2.0e6 / (10 * _MMHG * 4 * (1 - 0.3 ** 2) / (0.4 / 2.0) ** 3)) / 0.02,
    "biomaterials-10:relative-flow": 0.8 ** 4,
    "biomaterials-10:wall-shear-after": _wall_shear_pa(3.5e-3, 4e-6, 1.6e-3),
    # biomaterials-11: biocompatibility evidence
    "biomaterials-11:relative-viability": 100 * 0.96 / 1.20,
    "biomaterials-11:independent-units": 3,
    "biomaterials-11:capsule-difference": sum(_BM_A) / 6 - sum(_BM_B) / 6,
    "biomaterials-11:animal-level-t": (sum(_BM_A) / 6 - sum(_BM_B) / 6) / _BM_SE,
    "biomaterials-11:capsule-permeability": 300 / 100,
    "biomaterials-11:flux-ratio": 100 / 20,
    # biomaterials-12: cells for a scaffold
    "biomaterials-12:cells-needed": _BM_NEED / 1e8,
    "biomaterials-12:cells-to-seed": _BM_SEED / 1e8,
    "biomaterials-12:doublings": math.log2(_BM_SEED / 5.0e5),
    "biomaterials-12:expansion-days": math.log2(_BM_SEED / 5.0e5) * 36 / 24,
    "biomaterials-12:passages": math.ceil(math.log2(_BM_SEED / 5.0e5) / math.log2(4)),
    "biomaterials-12:volume-fraction": 5.0e7 * 2.0e-9,
    "biomaterials-12:extra-days": (math.log2(_BM_NEED / 0.4 / 5.0e5) - math.log2(_BM_SEED / 5.0e5)) * 36 / 24,
    # biomaterials-13: failure analysis
    "biomaterials-13:lumen-area-loss": 100 * (1 - (1.4 / 1.8) ** 2),
    "biomaterials-13:flow-fraction": (1.4 / 1.8) ** 4,
    "biomaterials-13:shear-factor": (1.8 / 1.4) ** 3,
    "biomaterials-13:buckling-day-60": _buckling_pa(2.0e6 * math.exp(-0.02 * 60), 0.40e-3, 2.0e-3) / _MMHG,
    "biomaterials-13:local-ph": _BM_PH,
    # virtual lab 1, recomputed from the CSV
    "biomaterials-lab1:fraction-cleaved": 100 * _BM_P28,
    "biomaterials-lab1:scission-rate-constant": -math.log(1 - _BM_P28) / 28,
    "biomaterials-lab1:support-threshold": math.log(_lab_mean(_BM_ROWS, 0, "modulus_mpa") / 0.8) / _BM_KE,
    "biomaterials-lab1:first-mass-loss": next(
        d for d in sorted({int(r["day"]) for r in _BM_ROWS}) if _lab_mean(_BM_ROWS, d, "mass_pct") < 0.95 * _lab_mean(_BM_ROWS, 0, "mass_pct")
    ),
}


@pytest.mark.parametrize("question_id,expected", sorted(BIOMATERIALS_NUMERIC.items()))
def test_biomaterials_numeric_key_matches_independent_recalculation(question_id, expected):
    spec = bank("biomaterials")[question_id]["solution_spec"]
    allowed = spec["tolerance"] + (spec.get("relative_tolerance") or 0) * abs(spec["answer"])
    assert abs(spec["answer"] - expected) <= allowed, (question_id, spec["answer"], expected)


def test_every_biomaterials_numeric_item_is_recalculated():
    numeric = {qid for qid, item in bank("biomaterials").items() if item["type"] == "numeric"}
    assert numeric == set(BIOMATERIALS_NUMERIC)


def _fragments_in(text: str, fragments: list[str]) -> None:
    missing = [f for f in fragments if f not in text]
    assert not missing, missing


def test_biomaterials_protein_and_network_lessons_state_the_computed_numbers():
    theta = math.degrees(math.acos(25 / 72))
    capacity_side, capacity_end = _protein_capacity_mg_m2(66, 50), _protein_capacity_mg_m2(66, 20)
    gamma_1s = 2 * 0.2 * math.sqrt(60e-12 / math.pi) * 1e6
    capacity2 = _protein_capacity_mg_m2(45, 30)
    gamma2 = capacity2 * 0.3 / (0.1 + 0.3)
    _fragments_in(reading("biomaterials", "biomaterials-7"), [
        f"θ = **{theta:.1f}°**", f"**{72 * (1 + math.cos(math.radians(65))):.1f} mN/m**", f"{72 * (1 + math.cos(math.radians(110))):.1f} mN/m",
        "Γ = 2.4 mg/m²", "**0.45 mg/mL**", f"**{capacity_side:.2f} mg/m²**", f"{capacity_end:.2f} mg/m²",
        f"Γ(1 s) = **{gamma_1s:.2f} mg/m²**", f"{gamma_1s / 3.0:.0%} of the capacity", f"**{_diffusion_arrival_time_s(1.5, 60, 0.2):.2f} s**",
        f"**{40 * math.sqrt(61) / (3 * math.sqrt(20)):.1f} times**", f"{capacity2:.2f} mg/m²", f"{gamma2:.2f} mg/m²",
        f"= {_diffusion_arrival_time_s(gamma2, 80, 0.3):.2f} s",
    ])
    nu = 12000 / (_R_GAS * _T_BODY)
    xi = lambda g: (_K_B * _T_BODY / g) ** (1 / 3) * 1e9               # noqa: E731  nm
    d0 = _K_B * _T_BODY / (6 * math.pi * 0.69e-3 * 3.5e-9) * 1e12
    ratio_small, ratio_large = 3.5 / xi(12000), 6.0 / xi(12000)
    nu2 = 30000 / (_R_GAS * _T_BODY)
    _fragments_in(reading("biomaterials", "biomaterials-8"), [
        f"**{nu:.2f} mol/m³**", "**36 kPa**", f"**{100 / nu:.1f} kg/mol**", f"**{xi(12000):.1f} nm**", f"{2 ** (-1 / 3):.2f}, to {xi(24000):.1f} nm",
        f"only {10 ** (1 / 3):.2f} times smaller", f"**D₀ = {d0:.0f} μm²/s**", f"{1e-6 / (d0 * 1e-12) / 3600:.2f} h",
        f"gives {ratio_small:.2f}", f"gives {ratio_large:.2f}", f"**{xi(0.6 * 12000):.1f} nm**", f"from {ratio_large:.2f} to {6.0 / xi(0.6 * 12000):.2f}",
        f"{nu2:.2f} mol/m³", f"{150 / nu2:.1f} kg/mol", f"{xi(30000):.2f} nm", "E ≈ 3 G = 90 kPa", f"{3.5 / xi(30000):.2f}",
    ])


def test_biomaterials_degradation_and_mechanics_lessons_state_the_computed_numbers():
    k, mn0, mu = 0.0002, 100000.0, 72.0
    text = reading("biomaterials", "biomaterials-9")
    _fragments_in(text, [
        f"p = **{_bonds_cleaved(28, k):.2%}**", f"**{_mn_scission(28, mn0, mu, k) / 1000:.1f} kDa**", f"p = {_bonds_cleaved(56, k):.2%}",
        f"{_mn_scission(56, mn0, mu, k) / 1000:.1f} kDa", f"one bond in {1 / _bonds_cleaved(28, k):.0f}", f"{1 - _mn_scission(28, mn0, mu, k) / mn0:.0%}",
        f"**{_BM_TC:.1f} days**", f"{math.exp(-0.02 * (100 - _BM_TC)):.1%} remains at day 100", f"{_BM_TC + math.log(2) / 0.02:.1f} days",
        f"{mn0 / _mn_scission(60, mn0, mu, k):.0f} times shorter", f"**{math.sqrt(0.009 / k):.1f} mm**", f"τ_D = {1 / 0.009:.0f} days against 1/k = {1 / k:,.0f} days",
        f"τ_D k = {1 / 0.009 * k:.2f}", f"τ_D = {100 / 0.009:,.0f} days (τ_D k = {100 / 0.009 * k:.1f})",
    ])
    pb = 58.0 * (1 / 4000.0 - 1 / 60000.0)
    mn30b = _mn_scission(30, 60000.0, 58.0, 0.0004)
    _fragments_in(text, [f"{_bonds_cleaved(30, 0.0004):.2%}", f"{mn30b:.0f} g/mol ({mn30b / 1000:.1f} kDa)", f"{1 - mn30b / 60000.0:.0%}",
                         f"{pb:.4f}", f"{-math.log(1 - pb) / 0.0004:.1f} days"])
    text = reading("biomaterials", "biomaterials-10")
    sigma = 120 * _MMHG * 2.0 / 0.40
    _fragments_in(text, [
        f"**{sigma / 1000:.1f} kPa**", f"{sigma / 2.0e6:.3f}", f"**{100 * 40 * _MMHG * 2.0 / (0.40 * 2.0e6):.2f}%**",
        f"{100 * 40 * _MMHG * 2.0 / (0.40 * 2.0e6) * 100 / 40:.1f}% per 100 mmHg", f"**{_buckling_pa(2.0e6, 0.4e-3, 2.0e-3) / _MMHG:.1f} mmHg**",
        f"{_buckling_pa(2.0e6, 0.2e-3, 2.0e-3) / _MMHG:.1f} mmHg", "**59.7 days**" if abs(BIOMATERIALS_NUMERIC["biomaterials-10:time-to-threshold"] - 59.65) < 0.01 else "?",
        f"{10 * _MMHG * 4 * (1 - 0.3 ** 2) / (0.4 / 2.0) ** 3 / 1e6:.3f} MPa", f"**{_wall_shear_pa(3.5e-3, 4e-6, 2.0e-3):.2f} Pa**",
        f"**{0.8 ** 4:.2f}**", f"{_wall_shear_pa(3.5e-3, 4e-6, 1.6e-3):.2f} Pa", f"{(1 / 0.8) ** 3:.2f}",
    ])
    sig_w = 100 * _MMHG * 1.5 / 0.30
    _fragments_in(text, [
        f"{sig_w / 1000:.1f} kPa", f"{sig_w / 1.5e6:.3f}", f"{_buckling_pa(1.5e6, 0.3e-3, 1.5e-3) / _MMHG:.1f} mmHg", f"{(1.2 / 1.5) ** 4:.2f}",
        f"from {_wall_shear_pa(3.5e-3, 3e-6, 1.5e-3):.2f} Pa to {_wall_shear_pa(3.5e-3, 3e-6, 1.2e-3):.2f} Pa",
    ])


def test_biomaterials_evidence_cells_and_failure_lessons_state_the_computed_numbers():
    diff = sum(_BM_A) / 6 - sum(_BM_B) / 6
    t10 = _t_quantile(0.975, 10)
    text = reading("biomaterials", "biomaterials-11")
    _fragments_in(text, [
        "= 80.0%**", f"**{diff:.2f} μm**", f"**{diff / _BM_SE:.2f}** on 10 degrees of freedom", f"p = {_two_sided_p(diff / _BM_SE, 10):.3f}",
        f"{diff - t10 * _BM_SE:.1f} to {diff + t10 * _BM_SE:.1f} μm", "**3.0 μm/s**", "15.0 μm/s", "48 sections", "46 degrees of freedom",
    ])
    c_animals, r_animals = [60, 72, 55, 80, 66], [58, 70, 52, 77, 63]
    se2 = _pooled_sd(c_animals, r_animals) * math.sqrt(2 / 5)
    _fragments_in(text, [f"{100 * 0.57 / 0.85:.1f}%", f"t = {(66.6 - 64.0) / se2:.2f} on 8 degrees of freedom"])
    seed = 1.0e8 / 0.6
    doublings = math.log2(seed / 5.0e5)
    text = reading("biomaterials", "biomaterials-12")
    _fragments_in(text, [
        "**1.0 × 10⁸ cells**", f"**{seed / 1e8:.2f} × 10⁸ cells**", f"**{doublings:.2f} population doublings**", f"**{doublings * 36 / 24:.1f} days**",
        f"**{math.ceil(doublings / 2)} passages**", "= 10% of the volume", f"{seed / 2.0 * 2.0e-9:.1%} of the volume", f"{doublings * 36 / 24:.1f} days becomes {doublings * 36 / 24 * 1.25:.1f}",
    ])
    doublings2 = math.log2(2.0e7 / 2.0e5)
    _fragments_in(text, [f"= {doublings2:.2f}", f"{doublings2 * 48 / 24:.1f} days", f"{doublings2 / math.log2(3):.2f}", "cells fill 4% of the volume", "would give 8%"])
    text = reading("biomaterials", "biomaterials-13")
    shear = _wall_shear_pa(3.5e-3, 4e-6, 1.4e-3) / _wall_shear_pa(3.5e-3, 4e-6, 1.8e-3)
    _fragments_in(text, [
        f"{1 - 1.4 / 1.8:.1%}", f"{1 - (1.4 / 1.8) ** 2:.1%}", f"**{(1.4 / 1.8) ** 4:.3f}**", f"{_wall_shear_pa(3.5e-3, 4e-6, 1.8e-3):.2f} Pa to **{_wall_shear_pa(3.5e-3, 4e-6, 1.4e-3):.2f} Pa**",
        f"a factor of {shear:.2f}", f"{_buckling_pa(2.0e6, 0.4e-3, 2.0e-3) / _MMHG:.1f} mmHg", f"{BIOMATERIALS_NUMERIC['biomaterials-13:buckling-day-60']:.1f} mmHg",
        f"e^(1.2) = {math.exp(1.2):.2f}", f"**{_BM_PH:.2f}**", "6.13 mM", "3.87 mM",
    ])
    r2 = 1.6 / 1.8
    _fragments_in(text, [f"({r2:.3f})² = {r2 ** 2:.3f}", f"({r2:.3f})⁴ = {r2 ** 4:.3f}"])


def test_biomaterials_lab_text_and_keys_agree_with_the_dataset():
    assert len(_BM_ROWS) == 21 and sorted({int(r["day"]) for r in _BM_ROWS}) == [0, 14, 28, 42, 56, 70, 84]
    text = (COURSES / "biomaterials/labs/01-degradation-time-course-of-a-synthetic-scaffold.md").read_text(encoding="utf-8")
    k_fit = -math.log(1 - _BM_P28) / 28
    half_time = math.log(2) / _BM_KE
    t_threshold = math.log(_lab_mean(_BM_ROWS, 0, "modulus_mpa") / 0.8) / _BM_KE
    _fragments_in(text, [
        f"{_lab_mean(_BM_ROWS, 28, 'mn_kda'):.2f} kDa at day 28", f"p = 72 × (1/{_lab_mean(_BM_ROWS, 28, 'mn_kda') * 1000:.0f}", f"= {_BM_P28:.5f}",
        f"{100 * _BM_P28:.2f}% of bonds", f"{k_fit:.5f} per day", f"the half-time is {half_time:.1f} days", f"{t_threshold:.1f} days",
        f"{_lab_mean(_BM_ROWS, 84, 'mass_pct'):.1f}%", "first falls below 95% of its starting value at day 84",
    ])
    spec = bank("biomaterials")["biomaterials-lab1:modulus-half-time"]["solution_spec"]["field_specs"][0]
    assert abs(spec["answer"] - half_time) <= spec["tolerance"] and spec["significant_figures"] == 3
    checks = {(c["row_id"], c["column"]): c["answer"] for c in bank("biomaterials")["biomaterials-lab1:time-course-summary"]["solution_spec"]["validation_spec"]["checks"]}
    assert len(checks) == 20
    for day in (0, 14, 28, 56, 84):
        assert checks[(f"d{day}", "replicates")] == 3
        for column in ("mn_kda", "mass_pct", "modulus_mpa"):
            assert abs(checks[(f"d{day}", column)] - _lab_mean(_BM_ROWS, day, column)) < 1e-3, (day, column)
    # the data were built from a random-scission model: the fitted rate recovers the construction value
    assert abs(k_fit - 0.0002) < 0.00001 and abs(_BM_KE - 0.02) < 0.0005

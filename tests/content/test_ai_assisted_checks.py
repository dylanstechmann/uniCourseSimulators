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


# ---- bioreactors 0.4.0 --------------------------------------------------------------------------------------
def _monod(s: float, mumax: float, ks: float) -> float:
    return mumax * s / (ks + s)


def _chemostat_nutrient(d: float, mumax: float, ks: float) -> float:
    return d * ks / (mumax - d)


def _stirred_power_w(n_rev_s: float, d_m: float, power_number: float = 1.5, rho: float = 1000.0) -> float:
    return power_number * rho * n_rev_s ** 3 * d_m ** 5


def _kolmogorov_um(eps: float, nu: float = 0.70e-6) -> float:
    return (nu ** 3 / eps) ** 0.25 * 1e6


def _factorial_effect(runs: dict[tuple[int, int, int], float], sign) -> float:
    high = [v for k, v in runs.items() if sign(k) > 0]
    low = [v for k, v in runs.items() if sign(k) < 0]
    return sum(high) / len(high) - sum(low) / len(low)


def _bioreactors_lab_rows() -> list[dict[str, str]]:
    import csv
    return list(csv.DictReader((COURSES / "bioreactors/labs/gassing-out-do-curves.csv").open(encoding="utf-8")))


def _gassing_mean(rows: list[dict[str, str]], rpm: int, minutes: int) -> float:
    values = [float(r["do_pct"]) for r in rows if int(r["rpm"]) == rpm and int(r["time_min"]) == minutes]
    return sum(values) / len(values)


def _kla_per_hour(rows: list[dict[str, str]], rpm: int, minutes: int) -> float:
    return -math.log(1 - _gassing_mean(rows, rpm, minutes) / 100) / (minutes / 60)


_BR_ROWS = _bioreactors_lab_rows()
_BR_K200, _BR_K400 = _kla_per_hour(_BR_ROWS, 200, 30), _kla_per_hour(_BR_ROWS, 400, 10)
_FACT = {(-1, -1, -1): 3.1, (1, -1, -1): 3.9, (-1, 1, -1): 3.3, (1, 1, -1): 4.1, (-1, -1, 1): 3.4, (1, -1, 1): 4.6, (-1, 1, 1): 3.5, (1, 1, 1): 5.0}
_CENTER = [4.2, 4.0, 4.1]
_CENTER_SD = math.sqrt(sum((c - sum(_CENTER) / 3) ** 2 for c in _CENTER) / 2)
_T_CRIT_2DF = 0.95 * math.sqrt(2 / (1 - 0.95 ** 2))              # exact two-sided 5 % critical value for 2 degrees of freedom
_D_OPT = 0.04 * (1 - math.sqrt(0.5 / 20.5))
_OUR_LARGE_S = 2.0e-10 * 1.0e7 * 1e3 / 3600                   # mmol/(L s)
_YIELD = 1.5e5                                                 # cells/mL per mM
_N2_CONST_PV = 200 / 60 * 10 ** (-2 / 3)
_EPS = 21.6 / 1000

BIOREACTORS_NUMERIC = {
    # items written before 2026-10-08, recomputed from the numbers in their prompts
    "bioreactors-1:check": math.log(2) / 30,
    "bioreactors-2:check": 2e9 * 1e-16 * 3600 * 1000,
    "bioreactors-1:doubling-time": 24 / math.log2(1.28e6 / 2.0e5),
    "bioreactors-2:oxygen-supply-vs-demand": 10 * (0.20 - 0.10) - 1.5e10 * 1.0e-10,
    "bioreactors-5:max-otr": 5.0 * (0.2 - 0.05),
    "bioreactors-5:max-cell-density": 5.0 * (0.2 - 0.05) / 2.0e-10 / 1e3,
    "bioreactors-5:oxygen-enriched-gas": 5.0 * (0.5 - 0.05),
    "bioreactors-5:max-medium-depth": 3e-9 * 0.15 / (2e9 * 2.0e-10 * 1e-3 / 3600) * 1000,
    "bioreactors-6:glucose-used": 2.0e-10 * 5.0e5 * (math.exp(0.03 * 48) - 1) / 0.03 * 1000,
    "bioreactors-6:lactate": 1.6 * 10.736,
    "bioreactors-6:exhaustion": math.log(1 + 25 * 0.03 / (2.0e-10 * 5.0e5 * 1000)) / 0.03,
    "bioreactors-6:min-perfusion": 2.0e-10 * 5.0e6 * 1000 / 25,
    # bioreactors-7: Monod growth and yield
    "bioreactors-7:growth-rate": _monod(5.0, 0.04, 0.5),
    "bioreactors-7:nutrient-for-90": 0.9 * 0.5 / 0.1,
    "bioreactors-7:doubling-time": math.log(2) / _monod(5.0, 0.04, 0.5),
    "bioreactors-7:max-cell-density": (2.0e5 + _YIELD * (20 - 1)) / 1e6,
    "bioreactors-7:minimum-time": math.log((2.0e5 + _YIELD * 19) / 2.0e5) / 0.04,
    "bioreactors-7:doubled-glucose": (2.0e5 + _YIELD * (40 - 1)) / 1e6,
    "bioreactors-7:specific-uptake": 0.04 / (_YIELD * 1e3) / 1e-10,
    # bioreactors-8: chemostat and perfusion
    "bioreactors-8:washout-rate": 0.04 * 20 / (0.5 + 20),
    "bioreactors-8:steady-nutrient": _chemostat_nutrient(0.02, 0.04, 0.5),
    "bioreactors-8:steady-cells": _YIELD * (20 - _chemostat_nutrient(0.02, 0.04, 0.5)) / 1e6,
    "bioreactors-8:output": 0.03 * _YIELD * (20 - _chemostat_nutrient(0.03, 0.04, 0.5)) / 1e4,
    "bioreactors-8:optimal-dilution": _D_OPT,
    "bioreactors-8:perfusion-rate": 0.04 * 24 / 5.0e6 * 1e9,
    "bioreactors-8:minimum-perfusion": 2.0e-10 / ((25 - 5) * 1e-3) * 24 * 1e9,
    # bioreactors-9: mixing and scale-up
    "bioreactors-9:power-input": _stirred_power_w(200 / 60, 0.060),
    "bioreactors-9:power-per-volume": _stirred_power_w(200 / 60, 0.060) / 2.0e-3,
    "bioreactors-9:reynolds-number": 1000 * (200 / 60) * 0.060 ** 2 / 0.70e-3,
    "bioreactors-9:speed-at-constant-pv": 200 * 10 ** (-2 / 3),
    "bioreactors-9:tip-speed-at-scale": math.pi * _N2_CONST_PV * 0.60,
    "bioreactors-9:mixing-time-at-scale": 20 / _N2_CONST_PV,
    "bioreactors-9:pv-at-constant-speed": (_stirred_power_w(200 / 60, 0.60) / 2.0) / (_stirred_power_w(200 / 60, 0.060) / 2.0e-3),
    # bioreactors-10: shear and eddies
    "bioreactors-10:dissipation": _EPS,
    "bioreactors-10:kolmogorov-scale": _kolmogorov_um(_EPS),
    "bioreactors-10:local-scale": _kolmogorov_um(100 * _EPS),
    "bioreactors-10:kolmogorov-stress": 0.70e-3 * math.sqrt(100 * _EPS / 0.70e-6),
    "bioreactors-10:ratio-to-carrier": _kolmogorov_um(100 * _EPS) / 150,
    "bioreactors-10:allowed-power": (0.70e-6) ** 3 / (50e-6) ** 4 * 1000 / 100,
    "bioreactors-10:scale-shrinks": 100 ** -0.25,
    # bioreactors-11: dissolved-oxygen control
    "bioreactors-11:our-start": 2.0e-10 * 5.0e5 * 1e3,
    "bioreactors-11:kla-required": 2.0e-10 * 5.0e5 * 1e3 / (0.20 - 0.10),
    "bioreactors-11:time-to-limit": math.log(5.0 / 1.0) / 0.03,
    "bioreactors-11:density-at-limit": 5.0e5 * 5.0 / 1e6,
    "bioreactors-11:enriched-capacity": 5.0 * (0.50 - 0.10) / 2.0e-10 / 1e3 / 1e6,
    "bioreactors-11:time-enriched": math.log(5.0 * 0.40 / 0.1) / 0.03,
    "bioreactors-11:oxygen-time-constant": 60 / 5.0,
    # bioreactors-12: factorial design
    "bioreactors-12:effect-temperature": _factorial_effect(_FACT, lambda k: k[0]),
    "bioreactors-12:effect-oxygen": _factorial_effect(_FACT, lambda k: k[2]),
    "bioreactors-12:interaction-ac": _factorial_effect(_FACT, lambda k: k[0] * k[2]),
    "bioreactors-12:effect-standard-error": 2 * _CENTER_SD / math.sqrt(8),
    "bioreactors-12:curvature": sum(_CENTER) / 3 - sum(_FACT.values()) / 8,
    "bioreactors-12:runs-needed": 2 ** 4,
    "bioreactors-12:ofat-precision": math.sqrt(1 / 2 + 1 / 2) / math.sqrt(1 / 4 + 1 / 4),
    # bioreactors-13: scale-down experiment
    "bioreactors-13:oxygen-fall": _OUR_LARGE_S * 120,
    "bioreactors-13:time-to-critical": (0.10 - 0.03) / _OUR_LARGE_S,
    "bioreactors-13:time-to-anoxia": 0.10 / _OUR_LARGE_S,
    "bioreactors-13:oxygen-consumed-fraction": _OUR_LARGE_S * 120 / 0.10,
    "bioreactors-13:loop-effect": ((88 - 95) + (78 - 94)) / 2,
    "bioreactors-13:interaction": ((78 - 94) - (88 - 95)) / 2,
    "bioreactors-13:cultures-per-group": math.ceil(2 * (1.96 + 0.8416) ** 2 * 3.0 ** 2 / 6.0 ** 2),
    # virtual lab 1, recomputed from the CSV
    "bioreactors-lab1:kla-200": _BR_K200,
    "bioreactors-lab1:kla-400": _BR_K400,
    "bioreactors-lab1:supportable-density": 5.66 * (0.20 - 0.05) / 2.0e-10 / 1e3 / 1e6,
    "bioreactors-lab1:probe-lag": 5.66 * 20 / 3600,
}


@pytest.mark.parametrize("question_id,expected", sorted(BIOREACTORS_NUMERIC.items()))
def test_bioreactors_numeric_key_matches_independent_recalculation(question_id, expected):
    spec = bank("bioreactors")[question_id]["solution_spec"]
    allowed = spec["tolerance"] + (spec.get("relative_tolerance") or 0) * abs(spec["answer"])
    assert abs(spec["answer"] - expected) <= allowed, (question_id, spec["answer"], expected)


def test_every_bioreactors_numeric_item_is_recalculated():
    numeric = {qid for qid, item in bank("bioreactors").items() if item["type"] == "numeric"}
    assert numeric == set(BIOREACTORS_NUMERIC)


def test_bioreactors_growth_and_culture_lessons_state_the_computed_numbers():
    mu5 = _monod(5.0, 0.04, 0.5)
    xmax = 2.0e5 + _YIELD * 19
    _fragments_in(reading("bioreactors", "bioreactors-7"), [
        f"**{mu5:.4f} per hour**", f"{mu5 / 0.04:.0%} of the maximum", f"the doubling time is {math.log(2) / mu5:.1f} h", f"{math.log(2) / 0.04:.1f} h",
        "**4.5 mM**", f"**{xmax / 1e6:.2f} × 10⁶ cells/mL**", f"a {xmax / 2.0e5:.2f}-fold increase", f"**{math.log(xmax / 2.0e5) / 0.04:.1f} h**",
        f"{(2.0e5 + _YIELD * 39) / 1e6:.2f} × 10⁶ cells/mL, about double",
        f"μ = 0.05 × 2/(1.0 + 2) = {_monod(2.0, 0.05, 1.0):.4f} per hour", "S = 0.8 K_s/0.2 = 4 K_s = 4.0 mM",
        f"{(3.0e5 + 1.0e5 * 9.5) / 1e6:.2f} × 10⁶ cells/mL", f"{math.log((3.0e5 + 1.0e5 * 9.5) / 3.0e5) / 0.05:.1f} h at the maximum rate",
    ])
    s1, s2 = _chemostat_nutrient(0.02, 0.04, 0.5), _chemostat_nutrient(0.03, 0.04, 0.5)
    p1, p2 = 0.02 * _YIELD * (20 - s1), 0.03 * _YIELD * (20 - s2)
    p_opt = _D_OPT * _YIELD * (20 - _chemostat_nutrient(_D_OPT, 0.04, 0.5))
    ss2 = _chemostat_nutrient(0.03, 0.05, 1.0)
    xs2 = 1.0e5 * (10 - ss2)
    text = reading("bioreactors", "bioreactors-8")
    _fragments_in(text, [
        f"**{s1:.2f} mM**", f"**{_YIELD * (20 - s1) / 1e6:.3f} × 10⁶ cells/mL**", f"{s2:.2f} mM", f"{_YIELD * (20 - s2) / 1e6:.3f} × 10⁶ cells/mL",
        f"= {0.04 * 20 / 20.5:.4f} per hour", f"= {_D_OPT:.4f} per hour", f"{p1 / 1e4:.2f} × 10⁴", f"{p2 / 1e4:.2f} × 10⁴", f"{p_opt / 1e4:.2f} × 10⁴",
        f"**{0.04 * 24 / 5.0e6 * 1e9:.0f} pL/(cell·day)**", f"**{2.0e-10 / (20 * 1e-3) * 24 * 1e9:.0f} pL/(cell·day)**",
        f"= {0.05 * 10 / 11:.4f} per hour", f"{ss2:.2f} mM", f"{xs2 / 1e6:.3f} × 10⁶ cells/mL", f"{1 / 0.03:.1f} h",
    ])


def test_bioreactors_oxygen_control_and_scale_up_lessons_state_the_computed_numbers():
    our0 = 2.0e-10 * 5.0e5 * 1e3
    fold = 5.0 / (our0 / 0.10)
    _fragments_in(reading("bioreactors", "bioreactors-11"), [
        f"**{our0:.3f} mmol/(L·h)**", "**1.0 per hour**", f"**{math.log(fold) / 0.03:.1f} h**", f"**{5.0e5 * fold / 1e6:.1f} × 10⁶ cells/mL**",
        f"**{5.0 * 0.40 / 2.0e-10 / 1e3 / 1e6:.1f} × 10⁶ cells/mL**", f"**{math.log(5.0 * 0.40 / our0) / 0.03:.1f} h**", f"{5.0 * 0.15 / 2.0e-10 / 1e3 / 1e6:.2f} × 10⁶ cells/mL",
        "**12 min**", f"**{5.0 * 30 / 3600:.3f}**", f"{0.20 - 0.60 / 5:.2f} mmol/L",
    ])
    our02 = 1.5e-10 * 4.0e5 * 1e3
    kr02 = our02 / (0.20 - 0.12)
    fold2 = 4.0 / kr02
    _fragments_in(reading("bioreactors", "bioreactors-11"), [f"{our02:.3f} mmol/(L·h)", f"{kr02:.2f} per hour", f"{math.log(fold2) / 0.025:.1f} h", f"{4.0e5 * fold2 / 1e6:.2f} × 10⁶ cells/mL", "= 15 min"])
    p1 = _stirred_power_w(200 / 60, 0.060)
    n2 = 200 / 60 * 10 ** (-2 / 3)
    text = reading("bioreactors", "bioreactors-9")
    _fragments_in(text, [
        f"**{p1:.4f} W**", f"**{p1 / 2.0e-3:.1f} W/m³**", f"**{1000 * (200 / 60) * 0.06 ** 2 / 0.70e-3:,.0f}**", f"{math.pi * (200 / 60) * 0.06:.2f} m/s",
        f"{20 / (200 / 60):.1f} s", "| Constant P/V | 0.215 | 1 | 2.15 | 21.5 | 4.64 |", "| Constant tip speed | 0.100 | 0.10 | 1 | 10 | 10 |",
        "| Constant speed (mixing time) | 1 | 100 | 10 | 100 | 1 |", f"N = {n2 * 60:.1f} rpm", f"**{math.pi * n2 * 0.60:.2f} m/s**", f"**{20 / n2:.1f} s**",
        f"{_stirred_power_w(200 / 60 / 10, 0.60) / 2.0:.2f} W/m³", "2,160 W/m³", f"{math.pi * 200 / 60 * 0.60:.2f} m/s",
    ])
    pv1w = _stirred_power_w(4.0, 0.05) / 1.0e-3
    n2w = 4.0 * 5 ** (-2 / 3)
    _fragments_in(text, [f"{pv1w:.1f} W/m³", f"{n2w * 60:.1f} rpm", f"a factor of {math.pi * n2w * 0.25 / (math.pi * 4.0 * 0.05):.2f}", f"a factor of {(20 / n2w) / (20 / 4.0):.2f}"])
    text = reading("bioreactors", "bioreactors-10")
    eta = _kolmogorov_um(_EPS)
    eta_l = _kolmogorov_um(100 * _EPS)
    _fragments_in(text, [
        f"**{_EPS:.4f} W/kg**", f"**{eta:.1f} μm**", f"**{0.70e-3 * math.sqrt(_EPS / 0.70e-6):.3f} Pa**", f"**{100 * _EPS:.2f} W/kg**", f"**{eta_l:.1f} μm**",
        f"{0.70e-3 * math.sqrt(100 * _EPS / 0.70e-6):.2f} Pa", f"{eta / 150:.2f} (average) to **{eta_l / 150:.2f}**", f"{(0.70e-6) ** 3 / (50e-6) ** 4:.4f} W/kg",
        f"**{(0.70e-6) ** 3 / (50e-6) ** 4 * 1000 / 100:.2f} W/m³**",
    ])
    e2 = 50.0 / 1000
    _fragments_in(text, [f"{e2:.3f} W/kg", f"{_kolmogorov_um(e2):.1f} μm", f"{_kolmogorov_um(50 * e2):.1f} μm", f"{0.70e-3 * math.sqrt(50 * e2 / 0.70e-6):.2f} Pa"])


def test_bioreactors_design_of_experiments_and_scale_down_lessons_state_the_computed_numbers():
    text = reading("bioreactors", "bioreactors-12")
    ea, eb, ec = (_factorial_effect(_FACT, lambda k, i=i: k[i]) for i in range(3))
    eac = _factorial_effect(_FACT, lambda k: k[0] * k[2])
    hi_a = sum(v for k, v in _FACT.items() if k[0] > 0) / 4
    lo_a = sum(v for k, v in _FACT.items() if k[0] < 0) / 4
    fm = sum(_FACT.values()) / 8
    curv = sum(_CENTER) / 3 - fm
    se_curv = _CENTER_SD * math.sqrt(1 / 8 + 1 / 3)
    _fragments_in(text, [
        f"average {hi_a:.3f}", f"average {lo_a:.3f}", f"**A = {ea:.3f}**", f"B = {eb:.3f}", f"**C = {ec:.3f}**", f"**AC** is half the difference: (1.35 − 0.80)/2 = **{eac:.3f}**",
        f"s = **{_CENTER_SD:.2f}**", f"**{2 * _CENTER_SD / math.sqrt(8):.4f}**", f"about {_T_CRIT_2DF * 2 * _CENTER_SD / math.sqrt(8):.2f}", f"is **{curv:.4f}**",
        f"about {curv / se_curv:.1f} standard errors", f"{math.sqrt(2):.3f} times larger",
    ])
    runs = {(-1, -1): 2.0, (1, -1): 3.0, (-1, 1): 2.6, (1, 1): 4.2}
    wa = (runs[(1, -1)] - runs[(-1, -1)] + runs[(1, 1)] - runs[(-1, 1)]) / 2
    wb = (runs[(-1, 1)] - runs[(-1, -1)] + runs[(1, 1)] - runs[(1, -1)]) / 2
    wab = ((runs[(1, 1)] - runs[(-1, 1)]) - (runs[(1, -1)] - runs[(-1, -1)])) / 2
    _fragments_in(text, [f"= {wa:.2f} g/L", f"= {wb:.2f} g/L", f"= {wab:.2f} g/L", "2⁵ = 32", "2⁴ = 16"])
    text = reading("bioreactors", "bioreactors-13")
    sd, delta = 3.0, 6.0
    n_exact = next(n for n in range(2, 100) if two_sample_t_power(n, sd, delta) >= 0.80)
    _fragments_in(text, [
        f"= {2.0e-10 * 1.0e7 * 1e3:.1f} mmol/(L·h)", f"**{_OUR_LARGE_S * 120:.4f} mmol/L**", f"{0.10 - _OUR_LARGE_S * 120:.4f} mmol/L", f"**{(0.10 - 0.03) / _OUR_LARGE_S:.0f} s**",
        f"**{0.10 / _OUR_LARGE_S:.0f} s**", f"{_OUR_LARGE_S * 15:.4f} mmol/L", f"is {_OUR_LARGE_S * 120 / 0.10:.2f} in the large vessel and {_OUR_LARGE_S * 15 / 0.10:.2f}",
        "**(-7 + (-16))/2 = -11.5**".replace("-", "−"), f"{2 * (1.96 + 0.8416) ** 2 * sd ** 2 / delta ** 2:.2f}", f"a power of {two_sample_t_power(4, sd, delta):.2f} at 4",
        f"{two_sample_t_power(5, sd, delta):.2f} at 5", f"{two_sample_t_power(n_exact, sd, delta):.2f} at {n_exact}", f"**{n_exact} per group**", f"**{sd / math.sqrt(3):.2f}** points",
    ])
    our2 = 2.0e-10 * 6.0e6 * 1e3 / 3600
    _fragments_in(text, [f"{our2 * 1e4:.2f} × 10⁻⁴ mmol/(L·s)", f"{our2 * 90:.3f} mmol/L", f"{(0.08 - 0.03) / our2:.0f} s", f"Da = {our2 * 90 / 0.08:.2f}"])
    assert n_exact == 6


def test_bioreactors_lab_text_and_keys_agree_with_the_dataset():
    assert len(_BR_ROWS) == 63 and sorted({int(r["rpm"]) for r in _BR_ROWS}) == [200, 300, 400]
    text = (COURSES / "bioreactors/labs/01-measuring-kla-by-dynamic-gassing-out.md").read_text(encoding="utf-8")
    k300 = _kla_per_hour(_BR_ROWS, 300, 20)
    exponent = math.log(_BR_K400 / _BR_K200) / math.log(2)
    _fragments_in(text, [
        f"kLa(200) = −ln(1 − {_gassing_mean(_BR_ROWS, 200, 30) / 100:.4f})/0.5 = {_BR_K200:.2f} per hour", f"kLa(400) = −ln(1 − {_gassing_mean(_BR_ROWS, 400, 10) / 100:.4f})/(10/60) = {_BR_K400:.2f} per hour",
        f"gives {k300:.2f} per hour", f"a = ln({_BR_K400:.2f}/{_BR_K200:.2f})/ln 2 = {exponent:.2f}", f"{5.66 * 0.15:.3f} mmol/(L·h)", f"supports {5.66 * 0.15 / 2.0e-10 / 1e9:.3f} × 10⁶ cells/mL",
        f"{5.66 * 20 / 3600:.3f}",
    ])
    spec = bank("bioreactors")["bioreactors-lab1:speed-exponent"]["solution_spec"]["field_specs"][0]
    assert abs(spec["answer"] - exponent) <= spec["tolerance"] and spec["significant_figures"] == 3
    checks = {(c["row_id"], c["column"]): c["answer"] for c in bank("bioreactors")["bioreactors-lab1:curve-summary"]["solution_spec"]["validation_spec"]["checks"]}
    assert len(checks) == 9
    for rpm in (200, 300, 400):
        assert checks[(f"rpm{rpm}", "runs")] == 3
        for minutes in (10, 30):
            assert abs(checks[(f"rpm{rpm}", f"do_{minutes}")] - _gassing_mean(_BR_ROWS, rpm, minutes)) < 1e-3
    # the curves were built from kLa = 2.0 (N/200)^1.5 per hour; the fits recover it
    assert abs(_BR_K200 - 2.0) < 0.06 and abs(_BR_K400 - 2.0 * 2 ** 1.5) < 0.15 and abs(exponent - 1.5) < 0.06
    assert all(0 <= float(r["do_pct"]) <= 100 for r in _BR_ROWS)


# ---- transport 0.4.0 ----------------------------------------------------------------------------------------
_TD, _TC0, _TQ = 2.0e-9, 0.2, 0.02                            # the oxygen-limit lesson's diffusion coefficient, surface value and uptake
_T_KB, _T_T = 1.381e-23, 310.0


def _bisect(f, low: float, high: float, steps: int = 200) -> float:
    for _ in range(steps):
        mid = (low + high) / 2
        low, high = (mid, high) if f(low) * f(mid) > 0 else (low, mid)
    return (low + high) / 2


def _erfc_inverse(p: float) -> float:
    return _bisect(lambda x: math.erfc(x) - p, 0.0, 6.0)


def _sphere_core_radius(radius: float) -> float:
    if _TC0 - _TQ * radius ** 2 / (6 * _TD) >= 0:
        return 0.0
    return _bisect(lambda rn: _TQ / (6 * _TD) * (radius ** 2 - 3 * rn ** 2 + 2 * rn ** 3 / radius) - _TC0, 1e-9, radius * 0.999999)


def _mm_slab_minimum(length: float, vmax: float = 0.02, km: float = 0.005, c0: float = 0.2, d: float = 2.0e-9, steps: int = 800) -> float:
    """Lowest concentration (sealed face) of a one-sided slab with Michaelis-Menten uptake, by RK4 shooting and bisection."""
    def rate(c: float) -> float:
        c = max(c, 0.0)
        return vmax * c / (km + c) / d

    def end_state(slope: float) -> tuple[float, float]:
        c, g, h = c0, slope, length / steps
        for _ in range(steps):
            k1c, k1g = g, rate(c)
            k2c, k2g = g + h / 2 * k1g, rate(c + h / 2 * k1c)
            k3c, k3g = g + h / 2 * k2g, rate(c + h / 2 * k2c)
            k4c, k4g = g + h * k3g, rate(c + h * k3c)
            c += h / 6 * (k1c + 2 * k2c + 2 * k3c + k4c)
            g += h / 6 * (k1g + 2 * k2g + 2 * k3g + k4g)
        return g, c

    slope = _bisect(lambda s: end_state(s)[0], -5e3, 0.0, steps=70)
    return end_state(slope)[1]


def _krogh_radial_drop(rt: float, rc: float, q: float, d: float) -> float:
    return q / (4 * d) * (2 * rt ** 2 * math.log(rt / rc) - (rt ** 2 - rc ** 2))


def _tanks_in_series(x: float, n: int) -> float:
    return 1 - math.exp(-n * x) * sum((n * x) ** k / math.factorial(k) for k in range(n))


def _transport_lab_rows() -> list[dict[str, str]]:
    import csv
    return list(csv.DictReader((COURSES / "transport/labs/oxygen-depth-profiles.csv").open(encoding="utf-8")))


def _profile_mean(rows: list[dict[str, str]], thickness: int, depth: int) -> float:
    values = [float(r["o2_mol_m3"]) for r in rows if int(r["thickness_um"]) == thickness and int(r["depth_um"]) == depth]
    return sum(values) / len(values)


_TR_ROWS = _transport_lab_rows()
_TR_Q = round(2 * _TD * (_TC0 - _profile_mean(_TR_ROWS, 100, 100)) / (100e-6) ** 2, 3)
_TR_LC = math.sqrt(2 * _TD * _TC0 / _TR_Q) * 1e6
_TR_ZERO = next(z for z in range(0, 301, 25) if _profile_mean(_TR_ROWS, 300, z) == 0)
_TR_PIPE_Q = 2.0e-6 / 60
_ETA_T = 200e-6 / (2 * math.sqrt(_TD * 60))
_CH_RC, _CH_RT, _CH_L, _CH_Q = 100e-6, 200e-6, 10e-3, 10e-9 / 60
_CH_UPTAKE = math.pi * (_CH_RT ** 2 - _CH_RC ** 2) * _CH_L * _TQ
_CH_DR = _krogh_radial_drop(_CH_RT, _CH_RC, _TQ, _TD)
_CH_DAX = _CH_UPTAKE / _CH_Q
_CH_QREQ = _CH_UPTAKE / (_TC0 - _CH_DR - 0.05)
_LC_SPHERE = math.sqrt(6 * _TD * _TC0 / _TQ)
_LUMPED_TAU = 1000 * 4180 * (10e-3 / 6) / 10
_SH_KC = 3.66 * _TD / 1e-3
_AREAL_FLUX = 2.0e5 * 1e4 * 2.0e-10 * 1e-3 / 3600

TRANSPORT_NUMERIC = {
    # items written before 2026-10-08, recomputed from the numbers in their prompts
    "transport-1:check": 5.0,
    "transport-2:check": (100e-6) ** 2 / 1e-9,
    "transport-3:check": 1000 * 0.02 * 0.5e-3 / 0.001,
    "transport-4:check": 0.02 / (0.5 * 0.10),
    "transport-1:accumulation-rate": 2.0 - 1.5,
    "transport-2:diffusion-time": (100e-6) ** 2 / 1.0e-9,
    "transport-3:poiseuille-flow": math.pi * (0.5e-3) ** 4 * 100 / (8 * 1.0e-3 * 0.10),
    "transport-4:series-thermal-resistance": 50 / (0.20 + 0.30),
    "transport-5:critical-thickness": math.sqrt(2 * _TD * _TC0 / _TQ) * 1e6,
    "transport-5:minimum-concentration": _TC0 - _TQ * (150e-6) ** 2 / (2 * _TD),
    "transport-5:doubled-surface-oxygen": math.sqrt(2 * _TD * 0.4 / _TQ) * 1e6,
    "transport-5:thiele-modulus": _TQ * (100e-6) ** 2 / (_TD * _TC0),
    "transport-6:heater-power": 1000 * _TR_PIPE_Q * 4180 * (37 - 22),
    "transport-6:reynolds": 4 * 1000 * _TR_PIPE_Q / (math.pi * 7.80e-4 * 1.0e-3),
    "transport-6:pressure-drop": 128 * 7.80e-4 * 0.5 * _TR_PIPE_Q / (math.pi * (1.0e-3) ** 4),
    "transport-6:half-diameter": 2 ** 4,
    "transport-6:wall-shear": 32 * 7.80e-4 * _TR_PIPE_Q / (math.pi * (1.0e-3) ** 3),
    # transport-7: transient diffusion
    "transport-7:diffusion-time-1mm": (1e-3) ** 2 / _TD,
    "transport-7:diffusion-time-5mm": (5e-3) ** 2 / _TD / 3600,
    "transport-7:similarity-variable": _ETA_T,
    "transport-7:concentration-at-depth": _TC0 * 0.683,
    "transport-7:half-time": (500e-6 / (2 * _erfc_inverse(0.5))) ** 2 / _TD,
    "transport-7:time-scaling": (1000 / 500) ** 2,
    "transport-7:valid-time": (1e-3) ** 2 / (16 * _TD),
    # transport-8: advection and diffusion
    "transport-8:advection-time": 1e-3 / 2.0e-4,
    "transport-8:peclet-number": 2.0e-4 * 1e-3 / _TD,
    "transport-8:slow-flow-peclet": 2.0e-6 * 1e-3 / _TD,
    "transport-8:mass-transfer-coefficient": _SH_KC * 1e6,
    "transport-8:concentration-difference": _AREAL_FLUX / _SH_KC,
    "transport-8:schmidt-number": 0.70e-6 / _TD,
    "transport-8:boundary-layer-ratio": (0.70e-6 / _TD) ** (-1 / 3),
    # transport-9: spheroid
    "transport-9:critical-radius": _LC_SPHERE * 1e6,
    "transport-9:central-concentration": _TC0 - _TQ * (300e-6) ** 2 / (6 * _TD),
    "transport-9:radius-ratio": math.sqrt(2),
    "transport-9:core-volume-share": (_sphere_core_radius(400e-6) / 400e-6) ** 3,
    "transport-9:rim-thickness": (500e-6 - _sphere_core_radius(500e-6)) * 1e6,
    "transport-9:growth-time": 3 * 24 * math.log2(_LC_SPHERE / 100e-6),
    # transport-10: Michaelis-Menten uptake
    "transport-10:fraction-at-km": 0.005 / (0.005 + 0.005),
    "transport-10:concentration-for-90": 0.9 * 0.005 / (1 - 0.9),
    "transport-10:uptake-at-low-oxygen": 0.02 * 0.02 / (0.005 + 0.02),
    "transport-10:zero-order-overestimate": 0.02 / (0.02 * 0.02 / (0.005 + 0.02)),
    "transport-10:first-order-constant": 0.02 / 0.005,
    "transport-10:km-to-surface": 0.005 / 0.2,
    # transport-11: lumped heat transfer
    "transport-11:volume-to-area": 10 / 6,
    "transport-11:time-constant": _LUMPED_TAU,
    "transport-11:biot-number-air": 10 * (10e-3 / 6) / 0.6,
    "transport-11:cooling-time": _LUMPED_TAU * math.log((37 - 4) / (10 - 4)) / 60,
    "transport-11:biot-number-bath": 500 * (10e-3 / 6) / 0.6,
    "transport-11:bath-time-constant": 1000 * 4180 * (10e-3 / 6) / 500,
    "transport-11:conduction-time": (5e-3) ** 2 / 1.4e-7,
    # transport-12: residence time
    "transport-12:residence-time": 10.0 / 0.5,
    "transport-12:washin-two-tau": 1 - math.exp(-2),
    "transport-12:time-to-95": -20 * math.log(0.05),
    "transport-12:washout-to-one-percent": -20 * math.log(0.01),
    "transport-12:steady-fraction-with-uptake": 1 / (1 + 0.05 * 20),
    "transport-12:effective-time-constant": 20 / (1 + 0.05 * 20),
    "transport-12:series-response": _tanks_in_series(1.0, 3),
    # transport-13: perfused construct
    "transport-13:radial-drop": _CH_DR,
    "transport-13:axial-drop": _CH_DAX,
    "transport-13:outlet-concentration": _TC0 - _CH_DAX,
    "transport-13:lowest-concentration": _TC0 - _CH_DAX - _CH_DR,
    "transport-13:required-flow": _CH_QREQ * 60 * 1e9,
    "transport-13:shear-at-required-flow": 4 * 0.78e-3 * _CH_QREQ / (math.pi * (100e-6) ** 3),
    # virtual lab 1, recomputed from the CSV
    "transport-lab1:consumption-rate": _TR_Q,
    "transport-lab1:critical-thickness": _TR_LC,
    "transport-lab1:zero-depth": _TR_ZERO,
    "transport-lab1:anoxic-thickness": 300 - round(_TR_LC),
}


@pytest.mark.parametrize("question_id,expected", sorted(TRANSPORT_NUMERIC.items()))
def test_transport_numeric_key_matches_independent_recalculation(question_id, expected):
    spec = bank("transport")[question_id]["solution_spec"]
    allowed = spec["tolerance"] + (spec.get("relative_tolerance") or 0) * abs(spec["answer"])
    assert abs(spec["answer"] - expected) <= allowed, (question_id, spec["answer"], expected)


def test_every_transport_numeric_item_is_recalculated():
    numeric = {qid for qid, item in bank("transport").items() if item["type"] == "numeric"}
    assert numeric == set(TRANSPORT_NUMERIC)


def test_transport_diffusion_and_advection_lessons_state_the_computed_numbers():
    eta = _ETA_T
    eta_half = _erfc_inverse(0.5)
    eta_01 = _erfc_inverse(0.01)
    coef = 1 / (4 * eta_half ** 2)
    rows = ["| 0 | 1.0000 |"] + [f"| {e:g} | {math.erfc(e):.4f} |" for e in (0.25, 0.5, 1.0, 1.5, 2.0)]
    _fragments_in(reading("transport", "transport-7"), rows + [
        f"takes {(100e-6) ** 2 / _TD:.0f} s", f"**{(1e-3) ** 2 / _TD:.0f} s**", f"{(5e-3) ** 2 / _TD:,.0f} s, or **{(5e-3) ** 2 / _TD / 3600:.2f} h**", f"**{eta:.4f}**",
        f"erfc({eta:.3f}) = {math.erfc(eta):.3f}", f"**{_TC0 * math.erfc(eta):.4f} mol/m³**", f"{math.erfc(eta):.0%} of the surface value", f"by only {math.sqrt(2) - 1:.0%}",
        f"η = {eta_half:.4f}", f"{coef:.3f} x²/D", f"**{coef * (500e-6) ** 2 / _TD:.0f} s**", f"η = {eta_01:.3f}", f"{2 * eta_01 * math.sqrt(_TD * 600) * 1000:.1f} mm",
        f"For L = 1 mm this is {(1e-3) ** 2 / (16 * _TD):.0f} s", f"{_TC0}/{_TQ} = {_TC0 / _TQ:.0f} s", f"is {(100e-6) ** 2 / _TD / (_TC0 / _TQ):.1f} times the consumption time",
    ])
    eta_w = 300e-6 / (2 * math.sqrt(1.0e-9 * 120))
    _fragments_in(reading("transport", "transport-7"), [
        f"= {eta_w:.4f}", f"erfc({eta_w:.3f}) = {math.erfc(eta_w):.3f}", f"= {math.erfc(eta_w):.3f} mol/m³", f"= {coef * (300e-6) ** 2 / 1.0e-9:.0f} s", f"x²/D = {(300e-6) ** 2 / 1.0e-9:.0f} s",
    ])
    kc = 3.66 * _TD / 1e-3
    pe_w = 1.0e-3 * 0.5e-3 / 3.0e-9
    kc_w = 3.66 * 3.0e-9 / 0.5e-3
    _fragments_in(reading("transport", "transport-8"), [
        f"t_adv = {1e-3 / 2.0e-4:.0f} s and t_diff = {(1e-3) ** 2 / _TD:.0f} s", f"**Pe = {2.0e-4 * 1e-3 / _TD:.0f}**", f"Pe = {2.0e-6 * 1e-3 / _TD:.0f}", f"**{kc * 1e6:.2f} μm/s**",
        f"**{_AREAL_FLUX / 1e-7 :.2f} × 10⁻⁷ mol/(m²·s)**", f"**{_AREAL_FLUX / kc:.4f} mol/m³**", f"{_AREAL_FLUX / kc / _TC0:.1%}", f"Sc = **{0.70e-6 / _TD:.0f}**", f"{(0.70e-6 / _TD) ** (-1 / 3):.2f}",
        f"Pe = {(0.5e-3) ** 2 / 3.0e-9:.0f}/{0.5e-3 / 1.0e-3:.1f} = {pe_w:.0f}", f"{kc_w * 1e6:.2f} μm/s", f"ΔC = 2.0 × 10⁻⁷/(2.20 × 10⁻⁵) = {2.0e-7 / kc_w:.4f} mol/m³",
    ])


def test_transport_oxygen_lessons_state_the_computed_numbers():
    lc_sphere = math.sqrt(6 * _TD * _TC0 / _TQ)
    rn_400, rn_500, rn_600 = (_sphere_core_radius(r * 1e-6) for r in (400, 500, 600))
    _fragments_in(reading("transport", "transport-9"), [
        f"**{lc_sphere * 1e6:.1f} μm**", f"**{_TC0 - _TQ * (300e-6) ** 2 / (6 * _TD):.3f} mol/m³**",
        "| 200 | 0.133 | — | 0% |", "| 300 | 0.050 | — | 0% |", f"| 400 | 0 (anoxic core) | {rn_400 * 1e6:.1f} | {(rn_400 / 400e-6) ** 3:.1%} |",
        f"| 500 | 0 (anoxic core) | {rn_500 * 1e6:.1f} | {(rn_500 / 500e-6) ** 3:.1%} |", f"| 600 | 0 (anoxic core) | {rn_600 * 1e6:.1f} | {(rn_600 / 600e-6) ** 3:.1%} |",
        f"core of radius {rn_400 * 1e6:.1f} μm, only **{(rn_400 / 400e-6) ** 3:.1%}**", f"**{(rn_500 / 500e-6) ** 3:.1%}** of the volume", f"{(500e-6 - rn_500) * 1e6:.1f} μm thick",
        f"({(600e-6 - rn_600) * 1e6:.1f} μm at a radius of 600 μm)", f"**{3 * 24 * math.log2(lc_sphere / 100e-6):.0f} h**", f"{3 * 24 * math.log2(lc_sphere / 100e-6) / 24:.1f} days", f"**{math.sqrt(2):.3f}**",
    ])
    # the cubic that fixes the core radius is satisfied at the stated values
    for radius, rn in ((400e-6, rn_400), (500e-6, rn_500), (600e-6, rn_600)):
        assert _TQ / (6 * _TD) * (radius ** 2 - 3 * rn ** 2 + 2 * rn ** 3 / radius) == pytest.approx(_TC0, abs=1e-9)
    d2, c2, q2 = 1.5e-9, 0.15, 0.03
    rc2 = math.sqrt(6 * d2 * c2 / q2)
    _fragments_in(reading("transport", "transport-9"), [f"{rc2 * 1e6:.1f} μm", f"{c2 - q2 * (180e-6) ** 2 / (6 * d2):.3f} mol/m³", f"{3 * 30 * math.log2(rc2 / 80e-6):.0f} h", f"{180e-6 / rc2:.0%} of the critical radius"])
    text = reading("transport", "transport-10")
    zero = {um: _TC0 - _TQ * (um * 1e-6) ** 2 / (2 * _TD) for um in (150, 180, 200)}
    mm = {um: _mm_slab_minimum(um * 1e-6) for um in (150, 180, 200, 220, 250)}
    _fragments_in(text, [
        "v(K_m) = **0.5 V_max**", "**0.045 mol/m³**", f"**{0.02 * 0.02 / 0.025:.3f} mol/(m³·s)**", f"**{0.02 / (0.02 * 0.02 / 0.025):.2f}**", f"**{0.02 / 0.005:.1f} per second**", f"{0.005 / 0.2:.3f}",
        f"| 150 | {zero[150]:.3f} | {mm[150]:.4f} |", f"| 180 | {zero[180]:.3f} | {mm[180]:.4f} |", f"| 200 | 0.000 | {mm[200]:.4f} |", f"| 220 | no valid solution | {mm[220]:.4f} |",
        f"| 250 | no valid solution | {mm[250]:.4f} |", f"**{mm[200]:.4f} mol/m³**", f"{mm[200] / _TC0:.0%} of the surface value", f"{mm[250]:.4f} mol/m³ at 250 μm",
    ])
    assert abs(zero[200]) < 1e-12 and 0.005 <= mm[150] - zero[150] <= 0.012 and 0.005 <= mm[180] - zero[180] <= 0.012
    v2 = 0.03 * 0.03 / (0.01 + 0.03)
    _fragments_in(text, [f"{v2:.4f} mol/(m³·s)", f"{v2 / 0.03:.0%}", f"{19 * 0.01:.2f} mol/m³", f"{0.03 / 0.01:.1f} per second", f"{0.03 / v2:.2f}"])


def test_transport_heat_chamber_and_capstone_lessons_state_the_computed_numbers():
    lc = 10e-3 / 6
    tau = 1000 * 4180 * lc / 10
    text = reading("transport", "transport-11")
    _fragments_in(text, [
        f"has V/A = {lc * 1000:.3f} mm", f"**τ = 1000 × 4180 × {lc:.6f}/10 = {tau:.0f} s**", f"**{tau * math.log(33 / 6):.0f} s**", f"{tau * math.log(33 / 6) / 60:.1f} min",
        f"**{10 * lc / 0.6:.4f}**", f"τ = {1000 * 4180 * lc / 500:.1f} s", f"Bi = {500 * lc / 0.6:.2f}", f"**R²/α = {(5e-3) ** 2 / 1.4e-7:.0f} s**", f"{(5e-3) ** 2 / (math.pi ** 2 * 1.4e-7):.1f} s",
        f"({tau:.0f} s) is much longer",
    ])
    lw = 6e-3 / 6
    tau_w = 1000 * 4180 * lw / 25
    _fragments_in(text, [f"τ = 1000 × 4180 × {lw:.4f}/25 = {tau_w:.0f} s", f"Bi = 25 × {lw:.4f}/0.6 = {25 * lw / 0.6:.3f}", f"= {tau_w * math.log((37 - 22) / (37 - 35)):.0f} s"])
    f_2 = 1 - math.exp(-2)
    t95 = -20 * math.log(0.05)
    x95 = _bisect(lambda x: _tanks_in_series(x, 3) - 0.95, 0.1, 6.0)
    _fragments_in(reading("transport", "transport-12"), [
        f"τ = **{10.0 / 0.5:.0f} min**", f"{f_2:.1%} after two", f"**{t95:.1f} min**", f"**{-20 * math.log(0.01):.1f} min**", f"{1 / (1 + 0.05 * 20):.2f},", f"= {20 / (1 + 0.05 * 20):.0f} min**",
        f"**{_tanks_in_series(1.0, 3):.3f}**", f"**{x95:.2f} τ = {x95 * 20:.1f} min**", f"1/√N = {1 / math.sqrt(3):.2f}",
    ])
    tau2 = 5.0 / 2.0
    _fragments_in(reading("transport", "transport-12"), [f"{tau2:.1f} min", f"{-tau2 * math.log(0.01):.1f} min", f"{1 / (1 + 0.2 * tau2):.3f}", f"{tau2 / (1 + 0.2 * tau2):.2f} min", f"{_tanks_in_series(1.0, 2):.3f}"])
    text = reading("transport", "transport-13")
    dr, dax = _CH_DR, _CH_DAX
    bracket = 2 * _CH_RT ** 2 * math.log(_CH_RT / _CH_RC) - (_CH_RT ** 2 - _CH_RC ** 2)
    shear = 4 * 0.78e-3 * _CH_Q / (math.pi * _CH_RC ** 3)
    dp = 8 * 0.78e-3 * _CH_Q * _CH_L / (math.pi * _CH_RC ** 4)
    dr2 = _krogh_radial_drop(150e-6, _CH_RC, _TQ, _TD)
    dax2 = math.pi * (150e-6 ** 2 - _CH_RC ** 2) * _CH_L * _TQ / _CH_Q
    _fragments_in(text, [
        f"bracket is {bracket * 1e8:.3f} × 10⁻⁸ m²", f"**{dr:.4f} mol/m³**", f"{dr / _TC0:.0%} of the inlet value", f"tissue minimum is {_TC0 - dr:.4f} mol/m³", f"= {dax:.4f} mol/m³**",
        f"**{_TC0 - dax:.4f} mol/m³**", f"**{_TC0 - dax - dr:.4f} mol/m³**", f"**{shear:.3f} Pa**", f"{dp:.0f} Pa", f"**{_CH_QREQ * 60 * 1e9:.1f} μL/min**",
        f"{_CH_UPTAKE * 1e11:.3f} × 10⁻¹¹ mol/s", f"{dr2:.4f} mol/m³ (a factor of {dr / dr2:.1f})", f"**{_TC0 - dax2 - dr2:.4f} mol/m³**",
    ])
    rc3, rt3, l3, q3 = 75e-6, 150e-6, 8e-3, 0.015
    dr3 = _krogh_radial_drop(rt3, rc3, q3, _TD)
    dax3 = math.pi * (rt3 ** 2 - rc3 ** 2) * l3 * q3 / (4.0e-9 / 60)
    _fragments_in(text, [f"= {dr3:.4f} mol/m³", f"{dax3:.4f} mol/m³", f"{_TC0 - dax3:.4f} mol/m³", f"{_TC0 - dax3 - dr3:.4f} mol/m³"])
    # the radial formula is the solution of the Krogh-cylinder equation: check it by direct integration of the profile
    steps, r, c = 4000, _CH_RC, 0.0
    h = (_CH_RT - _CH_RC) / steps
    def gradient(radius: float) -> float:
        return _TQ / (2 * _TD) * (radius - _CH_RT ** 2 / radius)

    for _ in range(steps):
        c += h * gradient(r + h / 2)
        r += h
    assert c == pytest.approx(-dr, rel=1e-4)


def test_transport_lab_text_and_keys_agree_with_the_dataset():
    assert len(_TR_ROWS) == 81 and sorted({int(r["thickness_um"]) for r in _TR_ROWS}) == [100, 200, 300]
    text = (COURSES / "transport/labs/01-oxygen-depth-profiles-in-cell-laden-slabs.md").read_text(encoding="utf-8")
    _fragments_in(text, [
        f"is {_profile_mean(_TR_ROWS, 100, 100):.3f} mol/m³, so q", f"= {2 * _TD * (_TC0 - _profile_mean(_TR_ROWS, 100, 100)) / (100e-6) ** 2:.4f} mol/(m³·s)", f"is √(2 × 2.0 × 10⁻⁹ × {_TC0}/{_TR_Q}) = {_TR_LC:.0f} μm",
        f"reaches zero at {_TR_ZERO} μm", f"anoxic over the remaining {300 - round(_TR_LC)} μm",
    ])
    checks = {(c["row_id"], c["column"]): c["answer"] for c in bank("transport")["transport-lab1:profile-summary"]["solution_spec"]["validation_spec"]["checks"]}
    assert len(checks) == 12
    for thickness in (100, 200, 300):
        assert checks[(f"l{thickness}", "profiles")] == 3
        for column, depth in (("c_surface", 0), ("c_100", 100), ("c_end", thickness)):
            assert abs(checks[(f"l{thickness}", column)] - _profile_mean(_TR_ROWS, thickness, depth)) < 1e-3, (thickness, column)
    # the profiles follow C = C0 - (q/2D) z (2 Lm - z) with Lm = min(L, critical thickness)
    for r in _TR_ROWS:
        lm = min(int(r["thickness_um"]) * 1e-6, math.sqrt(2 * _TD * _TC0 / _TQ))
        z = int(r["depth_um"]) * 1e-6
        model = 0.0 if (z >= lm - 1e-12 and int(r["thickness_um"]) * 1e-6 > lm) else _TC0 - _TQ / (2 * _TD) * z * (2 * lm - z)
        assert abs(float(r["o2_mol_m3"]) - model) <= 0.0045, r


# ---- cellular biomechanics 0.3.0 ----------------------------------------------------------------------------
def _maxwell_moduli(w: float, g: float = 1000.0, tau: float = 2.0) -> tuple[float, float]:
    x = w * tau
    return g * x ** 2 / (1 + x ** 2), g * x / (1 + x ** 2)


def _pillar_k(e: float, d: float, length: float) -> float:
    return 3 * math.pi * e * d ** 4 / (64 * length ** 3)


def _hill(e: float, ymax: float = 80.0, ec50: float = 10.0, n: float = 2.0) -> float:
    return ymax * e ** n / (ec50 ** n + e ** n)


def _cb_lab_rows() -> list[dict[str, str]]:
    import csv
    return list(csv.DictReader((COURSES / "cellular-biomechanics/labs/stiffness-ligand-marker-expression.csv").open(encoding="utf-8")))


def _sd(values: list[float]) -> float:
    m = sum(values) / len(values)
    return math.sqrt(sum((v - m) ** 2 for v in values) / (len(values) - 1))


_CB_ROWS = _cb_lab_rows()
_CB_CONDITIONS = ["s1_low", "s1_high", "s10_low", "s10_high", "s100_low", "s100_high"]


def _cb_gel_means(condition: str) -> list[float]:
    out = []
    for gel in (1, 2, 3):
        cells = [float(r["marker_au"]) for r in _CB_ROWS if r["condition"] == condition and int(r["gel"]) == gel]
        out.append(sum(cells) / len(cells))
    return out


_CB_COND = {c: sum(_cb_gel_means(c)) / 3 for c in _CB_CONDITIONS}
_CB_LIG_100 = _CB_COND["s100_high"] - _CB_COND["s100_low"]
_CB_LIG_1 = _CB_COND["s1_high"] - _CB_COND["s1_low"]
_CB_SD_GEL = math.sqrt((_sd(_cb_gel_means("s100_low")) ** 2 + _sd(_cb_gel_means("s100_high")) ** 2) / 2)
_CB_SD_CELL = math.sqrt((_sd([float(r["marker_au"]) for r in _CB_ROWS if r["condition"] == "s100_low"]) ** 2
                         + _sd([float(r["marker_au"]) for r in _CB_ROWS if r["condition"] == "s100_high"]) ** 2) / 2)
_KT_PN_NM = 1.381e-23 * 310 * 1e21
_BELL = math.exp(-10 * 0.5 / _KT_PN_NM)
_CB_TENSION = 100 / (2 * (1 / 4e-6 - 1 / 8e-6))
_VIF = 1 / (1 - 0.95 ** 2)
_SD_GEL_MEAN = math.sqrt(6.0 ** 2 + 15.0 ** 2 / 20)

CELLULAR_BIOMECHANICS_NUMERIC = {
    # items written before 2026-10-08, recomputed from the numbers in their prompts
    "cellular-biomechanics-5:hertz-modulus": 3 * 0.3e-9 * (1 - 0.5 ** 2) / (4 * math.sqrt(2.5e-6) * (0.5e-6) ** 1.5),
    "cellular-biomechanics-5:hertz-scaling": 0.3 * (1.0 / 0.5) ** 1.5,
    "cellular-biomechanics-5:maxwell-tau": 2e3 / 1e3,
    "cellular-biomechanics-5:maxwell-stress": 100 * math.exp(-5 / 2.0),
    "cellular-biomechanics-5:sls-instantaneous": 400 + 800,
    "cellular-biomechanics-6:stiffness-effect": (1400 + 2600) / 2 - (900 + 1300) / 2,
    "cellular-biomechanics-6:interaction": ((2600 - 1400) - (1300 - 900)) / 2,
    "cellular-biomechanics-6:ligand-density": 1e-12 * 6.022e23 / 1e8,
    "cellular-biomechanics-6:traction-force": 300 * 1000e-12 * 1e9,
    # cellular-biomechanics-7: oscillatory rheology
    "cellular-biomechanics-7:storage-modulus": _maxwell_moduli(0.5)[0],
    "cellular-biomechanics-7:loss-modulus": _maxwell_moduli(5.0)[1],
    "cellular-biomechanics-7:loss-tangent": _maxwell_moduli(5.0)[1] / _maxwell_moduli(5.0)[0],
    "cellular-biomechanics-7:crossover-frequency": 1 / 2.0,
    "cellular-biomechanics-7:complex-modulus": math.hypot(*_maxwell_moduli(0.5)),
    "cellular-biomechanics-7:phase-angle": math.degrees(math.atan2(_maxwell_moduli(0.05)[1], _maxwell_moduli(0.05)[0])),
    "cellular-biomechanics-7:young-from-shear": 2 * (1 + 0.5) * 1000,
    # cellular-biomechanics-8: micropillars
    "cellular-biomechanics-8:pillar-stiffness": _pillar_k(2.0e6, 2.0e-6, 6.0e-6) * 1e3,
    "cellular-biomechanics-8:force-from-deflection": _pillar_k(2.0e6, 2.0e-6, 6.0e-6) * 0.2e-6 * 1e9,
    "cellular-biomechanics-8:traction-stress": _pillar_k(2.0e6, 2.0e-6, 6.0e-6) * 0.2e-6 / (math.pi * (1.0e-6) ** 2),
    "cellular-biomechanics-8:total-force": 40 * _pillar_k(2.0e6, 2.0e-6, 6.0e-6) * 0.1e-6 * 1e9,
    "cellular-biomechanics-8:diameter-scaling": _pillar_k(2.0e6, 4.0e-6, 6.0e-6) / _pillar_k(2.0e6, 2.0e-6, 6.0e-6),
    "cellular-biomechanics-8:height-scaling": _pillar_k(2.0e6, 2.0e-6, 3.0e-6) / _pillar_k(2.0e6, 2.0e-6, 6.0e-6),
    "cellular-biomechanics-8:force-resolution": _pillar_k(2.0e6, 2.0e-6, 6.0e-6) * 1e3 * 0.02,
    # cellular-biomechanics-9: bonds under force
    "cellular-biomechanics-9:thermal-energy": _KT_PN_NM,
    "cellular-biomechanics-9:lifetime-factor": _BELL,
    "cellular-biomechanics-9:lifetime-at-force": 1.0 * _BELL,
    "cellular-biomechanics-9:half-life-force": _KT_PN_NM * math.log(2) / 0.5,
    "cellular-biomechanics-9:loading-time-stiff": 10 / (1.0 * 100),
    "cellular-biomechanics-9:loading-time-soft": 10 / (0.1 * 100),
    "cellular-biomechanics-9:critical-stiffness": 10 / (100 * _BELL),
    # cellular-biomechanics-10: micropipette aspiration
    "cellular-biomechanics-10:cortical-tension": _CB_TENSION * 1e3,
    "cellular-biomechanics-10:double-tension-pressure": 2 * (2 * _CB_TENSION) * (1 / 4e-6 - 1 / 8e-6),
    "cellular-biomechanics-10:wider-pipette": 2 * _CB_TENSION * (1 / 6e-6 - 1 / 8e-6),
    "cellular-biomechanics-10:smaller-cell": 2 * _CB_TENSION * (1 / 4e-6 - 1 / 6e-6),
    "cellular-biomechanics-10:circumference-force": _CB_TENSION * 2 * math.pi * 4e-6 * 1e9,
    "cellular-biomechanics-10:stress-scale": _CB_TENSION / 0.2e-6,
    # cellular-biomechanics-11: Hill dose-response
    "cellular-biomechanics-11:response-at-5kpa": _hill(5),
    "cellular-biomechanics-11:response-at-ec50": _hill(10),
    "cellular-biomechanics-11:response-at-40kpa": _hill(40),
    "cellular-biomechanics-11:stiffness-for-response": _bisect(lambda e: _hill(e) - 64.0, 0.1, 100.0),
    "cellular-biomechanics-11:slope-at-midpoint": (_hill(10.0 + 1e-4) - _hill(10.0 - 1e-4)) / 2e-4,
    "cellular-biomechanics-11:increase-5-to-20": _hill(20) - _hill(5),
    "cellular-biomechanics-11:linear-levels-range": _hill(100) - _hill(20),
    # cellular-biomechanics-12: applying strain
    "cellular-biomechanics-12:engineering-strain": 2e-3 / 20e-3,
    "cellular-biomechanics-12:true-strain": math.log(1.10),
    "cellular-biomechanics-12:transverse-strain": -0.5 * 0.10,
    "cellular-biomechanics-12:area-strain": 1.10 * 0.95 - 1,
    "cellular-biomechanics-12:membrane-stress": 1.5e6 * 0.10 / 1000,
    "cellular-biomechanics-12:membrane-force": 1.5e6 * 0.10 * 10e-3 * 0.5e-3,
    "cellular-biomechanics-12:peak-strain-rate": 2 * math.pi * 1.0 * 0.05,
    # cellular-biomechanics-13: redesign
    "cellular-biomechanics-13:variance-inflation": _VIF,
    "cellular-biomechanics-13:se-inflation": math.sqrt(_VIF),
    "cellular-biomechanics-13:frap-diffusion": 0.224 * 5.0 ** 2 / 12.0,
    "cellular-biomechanics-13:mobility-ratio": 30.0 / 12.0,
    "cellular-biomechanics-13:gel-mean-sd": _SD_GEL_MEAN,
    "cellular-biomechanics-13:gel-level-se": _SD_GEL_MEAN * math.sqrt(2 / 9),
    "cellular-biomechanics-13:naive-cell-level-se": math.sqrt(6.0 ** 2 + 15.0 ** 2) * math.sqrt(2 / 180),
    # virtual lab 1, recomputed from the CSV
    "cellular-biomechanics-lab1:stiffness-effect": (_CB_COND["s100_low"] + _CB_COND["s100_high"]) / 2 - (_CB_COND["s1_low"] + _CB_COND["s1_high"]) / 2,
    "cellular-biomechanics-lab1:ligand-effect-100": _CB_LIG_100,
    "cellular-biomechanics-lab1:interaction": (_CB_LIG_100 - _CB_LIG_1) / 2,
    "cellular-biomechanics-lab1:naive-se": _CB_SD_CELL * math.sqrt(2 / 30),
}


@pytest.mark.parametrize("question_id,expected", sorted(CELLULAR_BIOMECHANICS_NUMERIC.items()))
def test_cellular_biomechanics_numeric_key_matches_independent_recalculation(question_id, expected):
    spec = bank("cellular-biomechanics")[question_id]["solution_spec"]
    allowed = spec["tolerance"] + (spec.get("relative_tolerance") or 0) * abs(spec["answer"])
    assert abs(spec["answer"] - expected) <= allowed, (question_id, spec["answer"], expected)


def test_every_cellular_biomechanics_numeric_item_is_recalculated():
    numeric = {qid for qid, item in bank("cellular-biomechanics").items() if item["type"] == "numeric"}
    assert numeric == set(CELLULAR_BIOMECHANICS_NUMERIC)


def test_cellular_biomechanics_rheology_pillar_and_clutch_lessons_state_the_computed_numbers():
    gp = lambda w: _maxwell_moduli(w)[0]                                     # noqa: E731
    gpp = lambda w: _maxwell_moduli(w)[1]                                    # noqa: E731
    rows = [f"| {w:g} | {w * 2:g} | {gp(w):.1f} | {gpp(w):.1f} | {gpp(w) / gp(w):.2f} |" for w in (0.05, 0.5, 5.0)]
    delta_low = math.degrees(math.atan2(gpp(0.05), gp(0.05)))
    text = reading("cellular-biomechanics", "cellular-biomechanics-7")
    _fragments_in(text, rows + [
        f"the phase angle is {delta_low:.1f}°", f"G′ = {gp(5.0):.0f} Pa", f"tan δ = **{gpp(5.0) / gp(5.0):.2f}**", "**ω = 1/τ = 0.5 rad/s**", f"each equals G/2 = {gp(0.5):.0f} Pa",
        f"|G*| = {math.hypot(gp(0.5), gpp(0.5)):.1f} Pa", "E = **3000 Pa**",
    ])

    def sls(w: float) -> tuple[float, float]:
        x = w * 2.0
        return 400 + 800 * x ** 2 / (1 + x ** 2), 800 * x / (1 + x ** 2)

    _fragments_in(text, [f"G′ = {sls(0.5)[0]:.0f} Pa with G″ = {sls(0.5)[1]:.0f} Pa", f"{sls(0.1)[0]:.1f} Pa; G″", f"{sls(5)[0]:.1f} Pa; G″ = {sls(5)[1]:.1f} Pa"])
    k = _pillar_k(2.0e6, 2.0e-6, 6.0e-6)
    k_soft = _pillar_k(2.0e6, 1.5e-6, 8.0e-6)
    _fragments_in(reading("cellular-biomechanics", "cellular-biomechanics-8"), [
        f"**{k:.4f} N/m = {k * 1e3:.1f} nN/μm**", f"**{k * 1e3 * 0.2:.2f} nN**", f"{math.pi * 1.0 ** 2:.2f} μm²", f"stress of {k * 0.2e-6 / (math.pi * 1e-12):.0f} Pa", f"**{40 * k * 1e3 * 0.1:.0f} nN**",
        "**16 times**", "**8 times**", f"k = {k_soft * 1e3:.2f} nN/μm", f"about {k / k_soft:.0f} times softer", f"{k * 1e3 * 0.02:.2f} nN",
    ])
    k2 = _pillar_k(1.5e6, 1.0e-6, 4.0e-6)
    _fragments_in(reading("cellular-biomechanics", "cellular-biomechanics-8"), [f"{k2:.4f} N/m = {k2 * 1e3:.2f} nN/μm", f"= {k2 * 1e3 * 0.05:.2f} nN", f"{k2 * 0.05e-6 / (math.pi * (0.5e-6) ** 2):.0f} Pa", f"{25 * k2 * 1e3 * 0.05:.0f} nN"])
    text = reading("cellular-biomechanics", "cellular-biomechanics-9")
    _fragments_in(text, [
        f"{_KT_PN_NM:.2f} pN·nm", f"**{_BELL:.3f}**", f"**{_BELL:.3f} s**", f"**{_KT_PN_NM * math.log(2) / 0.5:.2f} pN**", "**0.10 s**", "**1.0 s**",
        f"= {10 / (100 * _BELL):.3f} pN/nm", f"({_BELL:.3f} s)",
    ])
    bell2 = math.exp(-8 * 0.8 / _KT_PN_NM)
    _fragments_in(text, [f"{2 * bell2:.3f} s", f"{_KT_PN_NM * math.log(2) / 0.8:.2f} pN", f"{8 / (80 * 2 * bell2):.3f} pN/nm"])


def test_cellular_biomechanics_aspiration_dose_response_strain_and_redesign_lessons_state_the_computed_numbers():
    t = _CB_TENSION
    text = reading("cellular-biomechanics", "cellular-biomechanics-10")
    _fragments_in(text, [
        "**4.0 × 10⁻⁴ N/m**", f"{t * 1e3:.2f} mN/m", f"{t * 2 * math.pi * 4e-6 * 1e9:.1f} nN", f"needs {2 * t * 2 * (1 / 4e-6 - 1 / 8e-6):.0f} Pa instead of {2 * t * (1 / 4e-6 - 1 / 8e-6):.0f} Pa",
        f"needs only {2 * t * (1 / 6e-6 - 1 / 8e-6):.1f} Pa", f"needs only {2 * t * (1 / 4e-6 - 1 / 6e-6):.1f} Pa", f"{t / 0.2e-6:.0f} Pa",
    ])
    t2 = 60 / (2 * (1 / 3e-6 - 1 / 6e-6))
    _fragments_in(text, [f"{t2 * 1e3:.2f} mN/m", f"{2 * 1.5e-4 * (1 / 3e-6 - 1 / 6e-6):.0f} Pa"])
    text = reading("cellular-biomechanics", "cellular-biomechanics-11")
    _fragments_in(text, [
        f"| 1 | {_hill(1):.1f} |", f"| 3 | {_hill(3):.1f} |", f"| 10 | {_hill(10):.1f} |", f"| 30 | {_hill(30):.1f} |", f"| 100 | {_hill(100):.1f} |",
        f"At 5 kPa the response is {_hill(5):.0f}%", f"at 20 kPa {_hill(20):.0f}%", f"by {_hill(20) - _hill(5):.0f} points", f"**{_hill(10):.0f}%**", f"at 40 kPa it is {_hill(40):.1f}%",
        "**20 kPa**", "**4 percentage points per kPa**", "(responses " + ", ".join(f"{_hill(e):.0f}" for e in (1, 3, 10, 30, 100)) + "%)", "(responses " + ", ".join(f"{_hill(e):.0f}" for e in (20, 40, 60, 80, 100)) + "%)",
    ])
    hill2 = lambda e: 60.0 * e ** 3 / (4.0 ** 3 + e ** 3)                    # noqa: E731
    _fragments_in(text, [f"y(2) = 60 × 2³/(4³ + 2³) = {hill2(2):.1f}%", f"y(8) = 60 × 8³/(4³ + 8³) = {hill2(8):.1f}%", f"E = 4 × (45/15)^(1/3) = {4 * (45 / 15) ** (1 / 3):.2f} kPa"])
    text = reading("cellular-biomechanics", "cellular-biomechanics-12")
    ar = 1.10 * 0.95 - 1
    _fragments_in(text, [
        "**0.10** (10%)", f"**{math.log(1.10):.4f}** (9.53%)", "**-0.050**".replace("-", "−"), f"**{ar:.3f}** (4.5%)", "**0.21**", "σ = 150 kPa**", "**0.75 N**", f"**{2 * math.pi * 0.05:.3f} per second**",
    ])
    e2 = 1.5e-3 / 30e-3
    ar2 = (1 + e2) * (1 - 0.5 * e2) - 1
    _fragments_in(text, [f"{e2:.3f}", f"{ar2:.4f}", f"{1.0e6 * e2 / 1000:.0f} kPa", f"{1.0e6 * e2 * 12e-3 * 0.4e-3:.3f} N", f"{2 * math.pi * 0.5 * 0.04:.3f} per second"])
    text = reading("cellular-biomechanics", "cellular-biomechanics-13")
    sd_gel = math.sqrt(6.0 ** 2 + 15.0 ** 2 / 20)
    _fragments_in(text, [
        f"{_VIF:.2f},", f"**{math.sqrt(_VIF):.2f} times**", f"**{0.224 * 25 / 12:.3f} μm²/s**", f"{0.224 * 25 / 30:.3f} μm²/s", "**2.5**", f"= **{sd_gel:.2f}**",
        f"= **{sd_gel * math.sqrt(2 / 9):.2f}** points", f"= **{math.sqrt(6.0 ** 2 + 15.0 ** 2) * math.sqrt(2 / 180):.2f}** points", f"{sd_gel * math.sqrt(2 / 9) / (math.sqrt(6.0 ** 2 + 15.0 ** 2) * math.sqrt(2 / 180)):.2f} times too small",
    ])
    sd2 = math.sqrt(5.0 ** 2 + 12.0 ** 2 / 15)
    _fragments_in(text, [f"{1 / (1 - 0.9 ** 2):.2f}.", f"{sd2:.2f}", f"{sd2 * math.sqrt(2 / 6):.2f}", f"{math.sqrt(5.0 ** 2 + 12.0 ** 2) * math.sqrt(2 / 90):.2f}", f"{0.224 * 16 / 20:.3f} μm²/s"])


def test_cellular_biomechanics_lab_text_and_keys_agree_with_the_dataset():
    assert len(_CB_ROWS) == 180 and {int(r["cell"]) for r in _CB_ROWS} == set(range(1, 11))
    text = (COURSES / "cellular-biomechanics/labs/01-stiffness-ligand-density-and-the-unit-of-analysis.md").read_text(encoding="utf-8")
    interaction = (_CB_LIG_100 - _CB_LIG_1) / 2
    se_gel = _CB_SD_GEL * math.sqrt(2 / 3)
    se_naive = _CB_SD_CELL * math.sqrt(2 / 30)
    _fragments_in(text, [
        f"The main effect of stiffness is ({_CB_COND['s100_low']:.0f} + {_CB_COND['s100_high']:.0f})/2 − ({_CB_COND['s1_low']:.0f} + {_CB_COND['s1_high']:.0f})/2 = 30",
        f"The ligand effect is {_CB_LIG_100:.0f} at 100 kPa and {_CB_LIG_1:.0f} at 1 kPa", f"({_CB_LIG_100:.0f} − {_CB_LIG_1:.0f})/2 = {interaction:.0f}",
        f"pooled SD of the gel means is {_CB_SD_GEL:.1f}", f"{_CB_SD_GEL:.1f} × √(2/3) = {se_gel:.2f}", f"t = {_CB_LIG_100 / se_gel:.1f} on 4 degrees of freedom",
        f"a pooled cell-level SD of {_CB_SD_CELL:.1f}", f"would give {se_naive:.2f}", f"about {se_gel / se_naive:.1f} times smaller",
    ])
    spec = bank("cellular-biomechanics")["cellular-biomechanics-lab1:gel-level-se"]["solution_spec"]["field_specs"][0]
    assert abs(spec["answer"] - se_gel) <= spec["tolerance"] and spec["significant_figures"] == 3
    checks = {(c["row_id"], c["column"]): c["answer"] for c in bank("cellular-biomechanics")["cellular-biomechanics-lab1:condition-summary"]["solution_spec"]["validation_spec"]["checks"]}
    assert len(checks) == 18
    for condition in _CB_CONDITIONS:
        assert checks[(condition, "gels")] == 3 and checks[(condition, "cells")] == 30
        assert abs(checks[(condition, "mean_of_gels")] - _CB_COND[condition]) < 1e-3
    # the gel means were built from the stated condition means with a between-gel spread of -6, 0 and +6
    assert [round(_CB_COND[c]) for c in _CB_CONDITIONS] == [22, 28, 36, 50, 42, 68]
    assert all(sorted(round(v - _CB_COND[c]) for v in _cb_gel_means(c)) == [-6, 0, 6] for c in _CB_CONDITIONS)


# ---- statics and mechanics of materials 0.4.0 ---------------------------------------------------------------
def _basquin_life(sa: float, sf: float, b: float) -> float:
    return 0.5 * (sa / sf) ** (1 / b)


def _euler_load(e: float, d: float, length: float, k: float = 1.0) -> float:
    return math.pi ** 2 * e * (math.pi * d ** 4 / 64) / (k * length) ** 2


def _weibull_pf(s: float, s0: float, m: float, v: float = 1.0) -> float:
    return 1 - math.exp(-v * (s / s0) ** m)


def _sm_lab_rows() -> list[dict[str, str]]:
    import csv
    return list(csv.DictReader((COURSES / "statics-materials/labs/fatigue-lives-by-stress-amplitude.csv").open(encoding="utf-8")))


_SM_ROWS = _sm_lab_rows()
_SM_LEVELS = [("s300", 300), ("s260", 260), ("s230", 230), ("s200", 200)]


def _sm_logs(level: str, failed_only: bool = True) -> list[float]:
    return [math.log10(float(r["cycles"])) for r in _SM_ROWS if r["level"] == level and (r["status"] == "failed" or not failed_only)]


def _sm_fit() -> tuple[float, float, float]:
    xs = [math.log10(s) for lv, s in _SM_LEVELS[:3]]
    ys = [sum(_sm_logs(lv)) / len(_sm_logs(lv)) for lv, _ in _SM_LEVELS[:3]]
    mx, my = sum(xs) / 3, sum(ys) / 3
    slope = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    return slope, mx, my


_SM_SLOPE, _SM_MX, _SM_MY = _sm_fit()
_SM_I_STRUT = math.pi * 0.5 ** 4 / 64
_SM_A_STRUT = math.pi * 0.5 ** 2 / 4
_SM_D_DESIGN = _bisect(lambda d: _euler_load(2000.0, d, 5.0) - 5.0, 0.1, 2.0)
_SM_VM = math.sqrt(80 ** 2 - 80 * 20 + 20 ** 2 + 3 * 30 ** 2)
_SM_I_STRIP = 5 * 1 ** 3 / 12
_SM_ENERGY = math.pi * 0.2e6 * (0.2 / 5.0) * 0.1                      # J/m^3 per cycle: pi sigma_a eps_a sin(delta)
_SM_RATE_10 = _SM_ENERGY * 10 / 4.0e6                                  # K/s
_SM_BOLD_MOHR = (math.hypot((80 - 20) / 2, 30), 50 + math.hypot(30, 30), 50 - math.hypot(30, 30))
_SM_WEIBULL_M = (math.log(-math.log(1 - 0.60)) - math.log(-math.log(1 - 0.10))) / (math.log(90) - math.log(70))

STATICS_MATERIALS_NUMERIC = {
    # items written before 2026-10-08, recomputed from the numbers in their prompts
    "statics-materials-1:check": 600 / 2,
    "statics-materials-2:check": 500 / 50,
    "statics-materials-4:check": 120 / 40,
    "statics-materials-1:reaction-force": 200 * 1.0 / 4.0,
    "statics-materials-2:stress-units": 1200 / 30,
    "statics-materials-3:bending-stress": 500 * 0.05 / (0.05 * 0.1 ** 3 / 12) / 1e6,
    "statics-materials-4:factor-of-safety": 250 / 100,
    "statics-materials-5:second-moment": math.pi / 4 * (13 ** 4 - 7 ** 4),
    "statics-materials-5:bending-stress": 100e3 * 13 / 20546,
    "statics-materials-5:combined-stress": 100e3 * 13 / (math.pi / 4 * (13 ** 4 - 7 ** 4)) + 2000 / (math.pi * (13 ** 2 - 7 ** 2)),
    "statics-materials-5:safety-factor": 150 / (100e3 * 13 / (math.pi / 4 * (13 ** 4 - 7 ** 4)) + 2000 / (math.pi * (13 ** 2 - 7 ** 2))),
    "statics-materials-5:solid-equivalent": 100e3 * math.sqrt(120.0) / (math.pi * math.sqrt(120.0) ** 4 / 4),
    "statics-materials-6:muscle-force": (15 * 15 + 50 * 35) / 4,
    "statics-materials-6:joint-reaction": (15 * 15 + 50 * 35) / 4 - 15 - 50,
    "statics-materials-6:angled-muscle": 493.75 / math.sin(math.radians(80)),
    "statics-materials-6:compression": 501.4 * math.cos(math.radians(80)),
    "statics-materials-6:mechanical-advantage": 4 / 35,
    # statics-materials-7: stress concentrations
    "statics-materials-7:hole-local-stress": 3 * 50,
    "statics-materials-7:first-yield-stress": 120 / 3,
    "statics-materials-7:ellipse-kt": 1 + 2 * 2 / 0.5,
    "statics-materials-7:ellipse-local-stress": 9 * 50,
    "statics-materials-7:notch-kt": 1 + 2 * math.sqrt(1 / 0.1),
    "statics-materials-7:smaller-root-radius": 1 + 2 * math.sqrt(1 / 0.05),
    "statics-materials-7:fatigue-notch-factor": 1 + 0.8 * (3 - 1),
    # statics-materials-8: fatigue
    "statics-materials-8:stress-amplitude": (200 - 20) / 2,
    "statics-materials-8:mean-stress": (200 + 20) / 2,
    "statics-materials-8:stress-ratio": 20 / 200,
    "statics-materials-8:life-at-300": _basquin_life(300, 900, -0.1) / 1000,
    "statics-materials-8:life-ratio": _basquin_life(0.9 * 300, 900, -0.1) / _basquin_life(300, 900, -0.1),
    "statics-materials-8:miner-sum": 10_000 / 29_525 + 500_000 / 1_702_531,
    "statics-materials-8:goodman-amplitude": 150 * (1 - 200 / 600),
    # statics-materials-9: buckling
    "statics-materials-9:radius-of-gyration": math.sqrt(_SM_I_STRUT / _SM_A_STRUT),
    "statics-materials-9:slenderness": 5.0 / math.sqrt(_SM_I_STRUT / _SM_A_STRUT),
    "statics-materials-9:critical-load": _euler_load(2000.0, 0.5, 5.0),
    "statics-materials-9:critical-stress": _euler_load(2000.0, 0.5, 5.0) / _SM_A_STRUT,
    "statics-materials-9:length-doubled": _euler_load(2000.0, 0.5, 10.0),
    "statics-materials-9:fixed-fixed": _euler_load(2000.0, 0.5, 5.0, k=0.5),
    "statics-materials-9:transition-slenderness": math.pi * math.sqrt(2000 / 40),
    "statics-materials-9:design-diameter": _SM_D_DESIGN,
    # statics-materials-10: combined stress
    "statics-materials-10:mohr-radius": _SM_BOLD_MOHR[0],
    "statics-materials-10:principal-max": _SM_BOLD_MOHR[1],
    "statics-materials-10:principal-min": _SM_BOLD_MOHR[2],
    "statics-materials-10:principal-angle": math.degrees(math.atan2(2 * 30, 80 - 20) / 2),
    "statics-materials-10:inclined-plane": 50 + 30 * math.cos(math.radians(60)) + 30 * math.sin(math.radians(60)),
    "statics-materials-10:von-mises": _SM_VM,
    "statics-materials-10:safety-factor": 120 / _SM_VM,
    "statics-materials-10:shear-yield": 120 / math.sqrt(3),
    # statics-materials-11: beam deflection
    "statics-materials-11:second-moment": _SM_I_STRIP,
    "statics-materials-11:central-deflection": 2 * 20 ** 3 / (48 * 3000 * _SM_I_STRIP),
    "statics-materials-11:bending-stiffness": 48 * 3000 * _SM_I_STRIP / 20 ** 3,
    "statics-materials-11:centre-stress": (2 * 20 / 4) * 0.5 / _SM_I_STRIP,
    "statics-materials-11:thickness-halved": (5 * 0.5 ** 3 / 12) / (5 * 1.0 ** 3 / 12),
    "statics-materials-11:cantilever-tip": 0.05 * 20 ** 3 / (3 * 3000 * _SM_I_STRIP),
    "statics-materials-11:uniform-load": 5 * 0.02 * 20 ** 4 / (384 * 3000 * _SM_I_STRIP),
    "statics-materials-11:flexural-modulus": 11.2 * 24 ** 3 / (48 * (6 * 1.2 ** 3 / 12)),
    # statics-materials-12: Weibull strength
    "statics-materials-12:failure-probability": _weibull_pf(80, 100, 10),
    "statics-materials-12:characteristic-fraction": 1 - math.exp(-1),
    "statics-materials-12:stress-for-one-percent": _bisect(lambda s: _weibull_pf(s, 100, 10) - 0.01, 1.0, 100.0),
    "statics-materials-12:size-factor": 8 ** (-1 / 10),
    "statics-materials-12:large-part-stress": _bisect(lambda s: _weibull_pf(s, 100, 10, v=8) - 0.01, 1.0, 100.0),
    "statics-materials-12:lower-modulus": _weibull_pf(80, 100, 5),
    "statics-materials-12:modulus-two-points": _SM_WEIBULL_M,
    # statics-materials-13: cyclic perfusion failure analysis
    "statics-materials-13:static-factor": 1.9 / 0.4,
    "statics-materials-13:service-cycles": 30 * 24 * 3600 * 1.0 / 1e6,
    "statics-materials-13:strut-amplitude": 40 * 0.2,
    "statics-materials-13:strut-life": _basquin_life(8.0, 30.0, -0.08) / 1e6,
    "statics-materials-13:life-after-degradation": _basquin_life(8.0, 30.0, -0.08) / _basquin_life(8.0, 30.0 * 0.85, -0.08),
    "statics-materials-13:buckling-modulus": 0.86 / 2.0,
    "statics-materials-13:heating-rate": _SM_RATE_10 * 1000,
    "statics-materials-13:time-to-2k": 2.0 / _SM_RATE_10,
    # virtual lab 1, recomputed from the CSV
    "statics-materials-lab1:scatter-260": _sd(_sm_logs("s260")),
    "statics-materials-lab1:fitted-slope": _SM_SLOPE,
    "statics-materials-lab1:basquin-exponent": 1 / _SM_SLOPE,
    "statics-materials-lab1:extrapolated-life": _SM_MY + _SM_SLOPE * (math.log10(160) - _SM_MX),
}


@pytest.mark.parametrize("question_id,expected", sorted(STATICS_MATERIALS_NUMERIC.items()))
def test_statics_materials_numeric_key_matches_independent_recalculation(question_id, expected):
    spec = bank("statics-materials")[question_id]["solution_spec"]
    allowed = spec["tolerance"] + (spec.get("relative_tolerance") or 0) * abs(spec["answer"])
    assert abs(spec["answer"] - expected) <= allowed, (question_id, spec["answer"], expected)


def test_every_statics_materials_numeric_item_is_recalculated():
    numeric = {qid for qid, item in bank("statics-materials").items() if item["type"] == "numeric"}
    assert numeric == set(STATICS_MATERIALS_NUMERIC)


def test_statics_materials_concentration_fatigue_and_buckling_lessons_state_the_computed_numbers():
    text = reading("statics-materials", "statics-materials-7")
    kt_notch = 1 + 2 * math.sqrt(1 / 0.1)
    kt_2 = 1 + 2 * math.sqrt(0.8 / 0.2)
    _fragments_in(text, [
        f"3 × 50 = **{3 * 50:.0f} MPa**", f"120/3 = **{120 / 3:.0f} MPa**", f"K_t = 1 + 2 × 2/0.5 = **{1 + 2 * 2 / 0.5:.0f}**", f"local stress of **{9 * 50:.0f} MPa**",
        f"= **{kt_notch:.2f}**", f"raises it to {1 + 2 * math.sqrt(1 / 0.05):.2f}", f"K_f = 1 + 0.8 × 2 = **{1 + 0.8 * 2:.1f}**",
        f"12000/(30 × 2) = {12000 / (30 * 2):.0f} MPa", f"12000/(24 × 2) = **{12000 / (24 * 2):.0f} MPa**",
        f"σ_max = 2.5 × 90 = {2.5 * 90:.0f} MPa; first yield at 200/2.5 = {200 / 2.5:.0f} MPa", f"K_t = 1 + 2 × 1.5/0.75 = {1 + 2 * 1.5 / 0.75:.0f}",
        f"K_t = 1 + 2√(0.8/0.2) = {kt_2:.2f}; K_f = 1 + 0.6 × ({kt_2:.2f} − 1) = {1 + 0.6 * (kt_2 - 1):.2f}",
    ])
    miner = 10_000 / _basquin_life(300, 900, -0.1) + 500_000 / _basquin_life(200, 900, -0.1)
    text = reading("statics-materials", "statics-materials-8")
    _fragments_in(text, [
        "σ_a = **90 MPa**, σ_m = **110 MPa** and R = **0.1**", f"= **{_basquin_life(300, 900, -0.1):,.0f} cycles**", f"N_f = **{_basquin_life(200, 900, -0.1):,.0f} cycles**",
        f"0.9^(−10) = **{0.9 ** -10:.2f}**", f"150 × (1 − 200/600) = **{150 * (1 - 200 / 600):.0f} MPa**",
        f"= {10_000 / _basquin_life(300, 900, -0.1):.3f} + {500_000 / _basquin_life(200, 900, -0.1):.3f} = **{miner:.3f}**", f"About {1 - miner:.0%} of the life remains",
    ])
    n_250, n_200 = _basquin_life(250, 800, -0.12), _basquin_life(200, 800, -0.12)
    d2 = 2_000 / n_250 + 15_000 / n_200
    _fragments_in(text, [
        f"= {n_250:,.0f}; N_f(200) = {n_200:,.0f} cycles", f"D = 2,000/{n_250:,.0f} + 15,000/{n_200:,.0f} = {2_000 / n_250:.3f} + {15_000 / n_200:.3f} = {d2:.3f}",
        f"R = {30 / 150:.2f}", f"use {d2:.0%} of the life, so the remaining life is {1 - d2:.0%}",
    ])
    text = reading("statics-materials", "statics-materials-9")
    d_design = _SM_D_DESIGN
    i_2 = math.pi * 0.8 ** 4 / 64
    a_2 = math.pi * 0.8 ** 2 / 4
    p_2 = _euler_load(1500.0, 0.8, 6.0, k=0.7)
    _fragments_in(text, [
        f"**{_SM_I_STRUT * 1e-12 / 1e-15:.3f} × 10⁻¹⁵ m⁴** ({_SM_I_STRUT:.6f} mm⁴)", f"A = {_SM_A_STRUT:.5f} mm²", "r = 0.125 mm", f"= **{_euler_load(2000.0, 0.5, 5.0):.3f} N**",
        f"gives {_euler_load(2000.0, 0.5, 10.0):.4f} N, one quarter", f"gives {_euler_load(2000.0, 0.5, 5.0, k=0.5):.3f} N, four times", "by 16.", "λ = 5/0.125 = **40**",
        f"= **{_euler_load(2000.0, 0.5, 5.0) / _SM_A_STRUT:.2f} MPa**", f"λ* = **{math.pi * math.sqrt(2000 / 40):.2f}**", f"**d = {d_design:.3f} mm**", f"slenderness of {5 / (d_design / 4):.1f}",
        f"I = π × 0.8⁴/64 = {i_2:.5f} mm⁴, A = {a_2:.4f} mm² and r = d/4 = 0.20 mm", f"/(0.7 × 6)² = {p_2:.2f} N, which corresponds to σ_cr = {p_2 / a_2:.2f} MPa",
        f"λ = 0.7 × 6/0.20 = {0.7 * 6 / 0.2:.0f}", f"λ* = π √(1500/30) = {math.pi * math.sqrt(1500 / 30):.2f}", f"σ_y A = 30 × {a_2:.4f} = {30 * a_2:.2f} N, below the Euler value of {p_2:.2f} N",
        f"overestimated the capacity by {p_2 / (30 * a_2) - 1:.0%}",
    ])


def test_statics_materials_stress_beam_brittle_and_capstone_lessons_state_the_computed_numbers():
    s1, s2 = _SM_BOLD_MOHR[1], _SM_BOLD_MOHR[2]
    text = reading("statics-materials", "statics-materials-10")
    sig_30 = 50 + 30 * math.cos(math.radians(60)) + 30 * math.sin(math.radians(60))
    tau_30 = -30 * math.sin(math.radians(60)) + 30 * math.cos(math.radians(60))
    _fragments_in(text, [
        f"= **{sig_30:.2f} MPa** and τθ = −{abs(tau_30):.2f} MPa", f"R = √(30² + 30²) = **{_SM_BOLD_MOHR[0]:.2f} MPa**", f"σ1 = **{s1:.2f} MPa** and σ2 = **{s2:.2f} MPa**",
        f"θp = ½ atan(2 × 30/60) = **{math.degrees(math.atan2(60, 60)) / 2:.1f}°**", f"σ1/2 = {s1 / 2:.2f} MPa", f"σ_vm = **{_SM_VM:.2f} MPa**", f"the Tresca value is {s1:.2f} MPa",
        f"**{120 / _SM_VM:.3f}** by von Mises and {120 / s1:.3f} by Tresca", f"σ_y/√3 = **{120 / math.sqrt(3):.2f} MPa**",
    ])
    r_2 = math.hypot(40, 35)
    p1, p2 = 20 + r_2, 20 - r_2
    vm_2 = math.sqrt(60 ** 2 - 60 * (-20) + (-20) ** 2 + 3 * 35 ** 2)
    _fragments_in(text, [
        f"R = √(40² + 35²) = {r_2:.2f} MPa", f"σ1 = 20 + {r_2:.2f} = {p1:.2f} MPa and σ2 = 20 − {r_2:.2f} = −{abs(p2):.2f} MPa", f"at θp = ½ atan(2 × 35/80) = {math.degrees(math.atan2(70, 80)) / 2:.2f}°",
        f"= {vm_2:.2f} MPa, so n = 150/{vm_2:.2f} = {150 / vm_2:.3f}", f"σ1 − σ2 = {p1 - p2:.2f} MPa", f"n = 150/{p1 - p2:.2f} = {150 / (p1 - p2):.3f}",
    ])
    text = reading("statics-materials", "statics-materials-11")
    ei = 3000 * _SM_I_STRIP
    k_2 = 48 * 2400 * (4 * 0.8 ** 3 / 12) / 16 ** 3
    h_req = (10 * 16 ** 3 / (4 * 2400 * 4)) ** (1 / 3)
    _fragments_in(text, [
        f"I = 5 × 1³/12 = **{_SM_I_STRIP:.4f} mm⁴**, EI = {ei:.0f} N·mm²", f"= 2 × 20³/(48 × {ei:.0f}) = **{2 * 20 ** 3 / (48 * ei):.4f} mm**", f"= **{48 * ei / 20 ** 3:.1f} N/mm**",
        f"σ = 3PL/(2bh²) = **{3 * 2 * 20 / (2 * 5 * 1 ** 2):.1f} MPa**", f"{2 * 20 ** 3 / (48 * ei) / 20:.1%} of the span", "multiplies the stiffness by 0.125, one eighth",
        f"= 0.05 × 20³/(3 × {ei:.0f}) = **{0.05 * 20 ** 3 / (3 * ei):.5f} mm**", f"δ = 5wL⁴/(384EI) = **{5 * 0.02 * 20 ** 4 / (384 * ei):.5f} mm**", f"= **{11.2 * 24 ** 3 / (4 * 6 * 1.2 ** 3):.0f} MPa**",
        f"I = 4 × 0.8³/12 = {4 * 0.8 ** 3 / 12:.5f} mm⁴", f"= {1.3 * 16 ** 3 / (48 * 2400 * 4 * 0.8 ** 3 / 12):.4f} mm", f"k = 48EI/L³ = {k_2:.2f} N/mm and σ = 3PL/(2bh²) = {3 * 1.3 * 16 / (2 * 4 * 0.8 ** 2):.2f} MPa",
        f"= {h_req ** 3:.4f} mm³, so h = {h_req:.3f} mm", f"factor of {10 / k_2:.2f}", f"ratio of {16 / h_req:.1f}",
    ])
    text = reading("statics-materials", "statics-materials-12")
    strengths = [62.0, 71.0, 77.0, 83.0, 88.0, 96.0]
    xs = [math.log(s) for s in strengths]
    ys = [math.log(-math.log(1 - (i + 0.5) / 6)) for i in range(6)]
    mx, my = sum(xs) / 6, sum(ys) / 6
    m_fit = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    s0_fit = math.exp(mx - my / m_fit)
    s_1pct = _bisect(lambda s: _weibull_pf(s, 100, 10) - 0.01, 1.0, 100.0)
    s_1pct_big = _bisect(lambda s: _weibull_pf(s, 100, 10, v=8) - 0.01, 1.0, 100.0)
    k_ic_stress = lambda a: 1.0 / (1.12 * math.sqrt(math.pi * a))             # noqa: E731
    _fragments_in(text, [
        f"σ_f = **{k_ic_stress(50e-6):.1f} MPa** for a 50 μm flaw and **{k_ic_stress(20e-6):.1f} MPa** for a 20 μm flaw", f"1 − 1/e = **{1 - math.exp(-1):.3f}**",
        f"P_f(80 MPa) = 1 − exp(−0.8^10) = **{_weibull_pf(80, 100, 10):.4f}** and P_f(60 MPa) = {_weibull_pf(60, 100, 10):.4f}", f"factor of about {_weibull_pf(80, 100, 10) / _weibull_pf(60, 100, 10):.0f}",
        f"σ = **{s_1pct:.2f} MPa**, about {s_1pct / 100:.0%} of σ₀", f"m = **{_SM_WEIBULL_M:.2f}**", f"m = {m_fit:.1f} and σ₀ = {s0_fit:.1f} MPa",
        f"8^(−1/10) = **{8 ** (-1 / 10):.4f}**", f"from {s_1pct:.2f} MPa to **{s_1pct_big:.2f} MPa**", f"factor of {8 ** (-1 / 5):.3f}", f"rises from {_weibull_pf(80, 100, 10):.3f} to **{_weibull_pf(80, 100, 5):.4f}**",
        f"1 − exp(−(0.75)^8) = 1 − exp(−{0.75 ** 8:.4f}) = {_weibull_pf(90, 120, 8):.4f}",
        f"σ = 120 × [−ln(0.995)]^(1/8) = 120 × {(-math.log(0.995)) ** (1 / 8):.4f} = {120 * (-math.log(0.995)) ** (1 / 8):.1f} MPa", f"27^(−1/8) = {27 ** (-1 / 8):.4f}",
        f"{120 * (-math.log(0.995)) ** (1 / 8):.1f} × {27 ** (-1 / 8):.4f} = {120 * (-math.log(0.995)) ** (1 / 8) * 27 ** (-1 / 8):.1f} MPa", f"about {27 ** (-1 / 8):.0%} of the stress",
    ])
    text = reading("statics-materials", "statics-materials-13")
    n_strut = _basquin_life(8.0, 30.0, -0.08)
    n_deg = _basquin_life(8.0, 25.5, -0.08)
    w_cycle = _SM_ENERGY
    _fragments_in(text, [
        f"1.9/0.4 = **{1.9 / 0.4:.2f}**", "40 × 0.2 = **8.0 MPa**", f"30 × 86,400 = **{30 * 86400:,.0f} cycles**", f"= **{n_strut / 1e6:.2f} million cycles**, about {n_strut / (30 * 86400):.1f} times",
        "to 25.5 MPa", f"The life becomes {n_deg / 1e6:.2f} million cycles, shorter by the factor 0.85^(−12.5) = **{n_strut / n_deg:.2f}**, which is {n_deg / 86400:.1f} days",
        f"0.86/2.0 = **{0.86 / 2.0:.2f}**", f"take {30 * 86400 / 10 / 86400:.1f} days at 10 Hz", "the strain amplitude is 0.040", f"**{w_cycle / 1000:.3f} kJ/m³**", f"At 10 Hz this is {w_cycle * 10:,.0f} W/m³",
        f"**{_SM_RATE_10 * 1000:.2f} mK/s**", f"at least **{2 / _SM_RATE_10:.0f} s**", f"At 1 Hz the rate is {_SM_RATE_10 * 100:.3f} mK/s and the same rise takes {2 / (_SM_RATE_10 / 10):,.0f} s",
        f"divides the life by {1.25 ** 12.5:.1f}", "This plan uses 50 specimens (20 + 5 + 15 + 5 + 5)",
    ])
    ss_2 = 35 * 0.15
    n_2, n_2d = _basquin_life(ss_2, 28.0, -0.09), _basquin_life(ss_2, 28.0 * 0.85, -0.09)
    w_2 = math.pi * 0.15e6 * (0.15 / 4.0) * 0.08
    _fragments_in(text, [
        f"35 × 0.15 = {ss_2:.2f} MPa", f"= {n_2 / 1e6:.1f} million cycles, a margin of {n_2 / (30 * 86400):.1f} over 2,592,000", f"σ_f′ = {28 * 0.85:.1f} MPa, N_f = {n_2d / 1e6:.2f} million cycles, a margin of {n_2d / (30 * 86400):.1f}",
        f"{w_2:,.0f} J/m³ per cycle", f"{w_2 * 10:,.0f}/4,000,000 = {w_2 * 10 / 4e6 * 1000:.2f} mK/s", f"takes at least {2 / (w_2 * 10 / 4e6):.0f} s",
    ])


def test_statics_materials_lab_text_and_keys_agree_with_the_dataset():
    assert len(_SM_ROWS) == 20 and {r["level"] for r in _SM_ROWS} == {lv for lv, _ in _SM_LEVELS}
    runouts = [r for r in _SM_ROWS if r["status"] == "runout"]
    assert [r["level"] for r in runouts] == ["s200", "s200"] and all(int(r["cycles"]) == 2_000_000 for r in runouts)
    assert all(int(r["cycles"]) < 2_000_000 for r in _SM_ROWS if r["status"] == "failed")
    assert all(int(r["amplitude_mpa"]) == dict(_SM_LEVELS)[r["level"]] for r in _SM_ROWS)
    # the lives were built from Basquin's law (sigma_f' = 900 MPa, b = -0.10) with spread in log10 life
    for level, amplitude in _SM_LEVELS[:3]:
        line = math.log10(0.5) - 10 * math.log10(amplitude / 900)
        logs = _sm_logs(level)
        assert abs(sum(logs) / len(logs) - line) < 0.05, level
        assert 0.1 < _sd(logs) < 0.25, level
    text = (COURSES / "statics-materials/labs/01-fatigue-lives-scatter-and-run-outs.md").read_text(encoding="utf-8")
    means = [sum(_sm_logs(lv)) / len(_sm_logs(lv)) for lv, _ in _SM_LEVELS]
    mean_all_200 = sum(_sm_logs("s200", failed_only=False)) / 5
    sd_260 = _sd(_sm_logs("s260"))
    ratio_260 = max(float(r["cycles"]) for r in _SM_ROWS if r["level"] == "s260") / min(float(r["cycles"]) for r in _SM_ROWS if r["level"] == "s260")
    log_160 = _SM_MY + _SM_SLOPE * (math.log10(160) - _SM_MX)
    _fragments_in(text, [
        "are " + ", ".join(f"{m:.3f}" for m in means) + ", in the order of the table", f"at 260 MPa is {sd_260:.3f}, a factor of {10 ** sd_260:.2f} in cycles", f"the longest life is {ratio_260:.1f} times the shortest",
        f"slope −{abs(_SM_SLOPE):.2f}, so b = 1/−{abs(_SM_SLOPE):.2f} = −{abs(1 / _SM_SLOPE):.3f}", f"the three failures is {means[3]:.3f}", f"counted at the cutoff is {mean_all_200:.3f}",
        f"median log10 life of {log_160:.2f}, about {10 ** log_160 / 1e6:.0f} million cycles", "nothing here is evidence about any device",
    ])
    field = bank("statics-materials")["statics-materials-lab1:runout-bias"]["solution_spec"]["field_specs"][0]
    assert abs(field["answer"] - mean_all_200) <= field["tolerance"] and field["significant_figures"] == 3
    checks = {(c["row_id"], c["column"]): c["answer"] for c in bank("statics-materials")["statics-materials-lab1:level-summary"]["solution_spec"]["validation_spec"]["checks"]}
    assert len(checks) == 12
    for level, _ in _SM_LEVELS:
        failed = len(_sm_logs(level))
        assert checks[(level, "specimens")] == 5 and checks[(level, "failures")] == failed
        assert abs(checks[(level, "mean_log10_failed")] - sum(_sm_logs(level)) / failed) < 1e-3


# ---- signals and control 0.4.0 -------------------------------------------------------------------------------
import cmath  # noqa: E402


def _sc_rk4(f, x0: list[float], t_end: float, dt: float) -> list[tuple[float, list[float]]]:
    """Fourth-order Runge-Kutta; returns (t, state) at every step."""
    t, x, out = 0.0, list(x0), [(0.0, list(x0))]
    n = int(round(t_end / dt))
    for _ in range(n):
        k1 = f(t, x)
        k2 = f(t + dt / 2, [a + dt / 2 * b for a, b in zip(x, k1)])
        k3 = f(t + dt / 2, [a + dt / 2 * b for a, b in zip(x, k2)])
        k4 = f(t + dt, [a + dt * b for a, b in zip(x, k3)])
        x = [a + dt / 6 * (b + 2 * c + 2 * d + e) for a, b, c, d, e in zip(x, k1, k2, k3, k4)]
        t += dt
        out.append((t, list(x)))
    return out


def _sc_step_second_order(a1: float, a0: float, b0: float, t_end: float, dt: float = 1e-3, zero: float = 0.0) -> list[tuple[float, float]]:
    """Unit-step response of (b0 - zero*s)/(s^2 + a1 s + a0) in controllable canonical form: y = b0 x1 - zero x2."""
    traj = _sc_rk4(lambda t, x: [x[1], -a0 * x[0] - a1 * x[1] + 1.0], [0.0, 0.0], t_end, dt)
    return [(t, b0 * x[0] - zero * x[1]) for t, x in traj]


def _sc_last_exit(traj: list[tuple[float, float]], final: float, band: float = 0.02) -> float:
    last = 0.0
    for t, y in traj:
        if abs(y - final) > band * abs(final):
            last = t
    return last


def _sc_G(w: float, k: float = 0.5, tau: float = 10.0, theta: float = 1.0) -> complex:
    return k * cmath.exp(-1j * w * theta) / (1 + 1j * w * tau)


def _sc_pm(loop, lo: float = 1e-3, hi: float = 50.0) -> tuple[float, float]:
    w = _bisect(lambda x: abs(loop(x)) - 1, lo, hi)
    return 180 + math.degrees(cmath.phase(loop(w))), w


def _sc_phase_crossover(loop, lo: float = 1.0, hi: float = 2.5) -> float:
    return _bisect(lambda x: loop(x).imag, lo, hi)


_SC_LOOP20 = lambda w: 20.0 * _sc_G(w)                                   # noqa: E731
_SC_PM20, _SC_WGC20 = _sc_pm(_SC_LOOP20)
_SC_WPC = _sc_phase_crossover(_SC_LOOP20)
_SC_GM = 1 / abs(_SC_LOOP20(_SC_WPC))


def _sc_pi_loop(kp: float, ti: float, k: float = 0.5, tau: float = 10.0, theta: float = 1.0, tf: float = 0.0):
    return lambda w: kp * (1 + 1 / (1j * w * ti)) * _sc_G(w, k, tau, theta) / (1 + 1j * w * tf)


def _sc_kp_for_pm(target: float, tf: float) -> float:
    def pm_of(kp: float) -> float:
        return _sc_pm(_sc_pi_loop(kp, 10.0, tf=tf))[0] - target
    return _bisect(pm_of, 1.0, 13.0)


def _sc_lab_rows() -> list[dict[str, str]]:
    import csv
    return list(csv.DictReader((COURSES / "signals-control/labs/incubator-step-tests.csv").open(encoding="utf-8")))


_SC_ROWS = _sc_lab_rows()


def _sc_final(test: str) -> float:
    vals = [float(r["rise_c"]) for r in _SC_ROWS if r["test"] == test and int(r["time_min"]) >= 56]
    return sum(vals) / len(vals)


def _sc_curve(test: str) -> list[float]:
    return [sum(float(r["rise_c"]) for r in _SC_ROWS if r["test"] == test and int(r["time_min"]) == t) / 2 for t in range(61)]


def _sc_t63(test: str) -> tuple[float, int]:
    curve, final = _sc_curve(test), _sc_final(test)
    delay = max(t for t in range(4) if curve[t] <= 0.02 * final)
    i = next(i for i in range(1, 61) if curve[i] >= 0.632 * final)
    return i - 1 + (0.632 * final - curve[i - 1]) / (curve[i] - curve[i - 1]), delay


_SC_T63, _SC_DELAY = _sc_t63("test_20w")
_SC_STEP_Y2 = dict(_sc_step_second_order(8.0, 12.0, 18.0, 1.0001))
_SC_ALIAS_DFT_N = 80


def _sc_alias(f: float, fs: float = 80.0) -> float:
    """Apparent frequency of a sampled cosine, found as the DFT peak of one second of samples."""
    n = int(fs)
    xs = [math.cos(2 * math.pi * f * k / fs) for k in range(n)]
    mags = [abs(sum(x * cmath.exp(-2j * math.pi * b * k / n) for k, x in enumerate(xs))) for b in range(n // 2 + 1)]
    return float(max(range(len(mags)), key=lambda b: mags[b]))


def _sc_closed_loop_amplitude(kp: float, t_end: float = 400.0, dt: float = 0.005) -> float:
    """Proportional loop around 0.5 exp(-s)/(10 s + 1) with a one-minute delay; returns the peak |y| over the last 40 minutes."""
    delay_steps = int(round(1.0 / dt))
    u_hist = [0.0] * delay_steps
    y, ys = 0.0, []
    for k in range(int(t_end / dt)):
        u_delayed = u_hist[k % delay_steps]
        y += dt * (-y + 0.5 * u_delayed) / 10.0
        u_hist[k % delay_steps] = kp * (1.0 - y)                       # unit setpoint step
        ys.append(y)
    tail = ys[-int(40 / dt):]
    return max(tail) - min(tail)


def _sc_second_order_peak(zeta: float, wn: float) -> tuple[float, float]:
    traj = _sc_step_second_order(2 * zeta * wn, wn ** 2, wn ** 2, 0.06, dt=1e-6)
    peak_t, peak_y = max(traj, key=lambda p: p[1])
    return peak_t * 1000, 100 * (peak_y - 1)


_SC_PEAK_T, _SC_OVERSHOOT = _sc_second_order_peak(0.25, 2 * math.pi * 20)
_SC_ZETA10 = _bisect(lambda z: math.exp(-math.pi * z / math.sqrt(1 - z ** 2)) - 0.10, 0.05, 0.95)
_SC_KP_ZN = 0.45 * 20 * _SC_GM
_SC_PU = 2 * math.pi / _SC_WPC
_SC_PM_PI, _SC_W_PI = _sc_pm(_sc_pi_loop(20 / 3, 10.0))
_SC_PM0, _SC_W0 = _sc_pm(_sc_pi_loop(40 / 3, 10.0))
_SC_PM1, _SC_W1 = _sc_pm(_sc_pi_loop(40 / 3, 10.0, tf=1.0))
_SC_PM_FAST, _ = _sc_pm(_sc_pi_loop(40 / 3, 10.0, tf=0.25))
_SC_KP45 = _sc_kp_for_pm(45.0, 1.0)

SIGNALS_CONTROL_NUMERIC = {
    # items written before 2026-10-08, recomputed from the numbers in their prompts
    "signals-control-2:check": 1 / (2 * math.pi * 0.05),
    "signals-control-1:dc-gain": 6 / 2,
    "signals-control-2:aliased-frequency": _sc_alias(120.0, 200.0),
    "signals-control-3:gain-margin": 1 / 0.4,
    "signals-control-5:steady-power": 15 / 0.5,
    "signals-control-5:p-error": 15 / (1 + 0.5 * 20),
    "signals-control-5:closed-loop-tau": 600 / (1 + 10),
    "signals-control-5:high-gain-error": 15 / (1 + 0.5 * 100),
    "signals-control-6:conv-sample": sum(h * x for h, x in zip([0.5, 0.3, 0.2], [1, 1, 1])),
    "signals-control-6:conv-length": 7 + 3 - 1,
    "signals-control-6:step-2tau": 100 * (1 - math.exp(-4 / 2)),
    "signals-control-6:impulse-value": math.exp(-1) / 2,
    "signals-control-6:ramp-error": 0.5 * 2,
    # signals-control-7: poles, zeros and the final value
    "signals-control-7:dc-gain": 18 / 12,
    "signals-control-7:slow-time-constant": 1 / abs(_bisect(lambda s: (s + 2) * (s + 6), -3.0, -1.0)),
    "signals-control-7:residue": 18 / ((-2) * (-2 + 6)),
    "signals-control-7:step-at-one-second": _SC_STEP_Y2[min(_SC_STEP_Y2, key=lambda t: abs(t - 1.0))],
    "signals-control-7:quadratic-slow-pole": 1 / abs((-8 + math.sqrt(64 - 60)) / 2),
    "signals-control-7:final-value": 5 * 4 / 10,
    "signals-control-7:wrong-way-start": dict(_sc_step_second_order(2.0, 1.0, 1.0, 0.5001, zero=0.5))[min(dict(_sc_step_second_order(2.0, 1.0, 1.0, 0.5001, zero=0.5)), key=lambda t: abs(t - 0.5))],
    # signals-control-8: second-order systems
    "signals-control-8:overshoot": _SC_OVERSHOOT,
    "signals-control-8:peak-time": _SC_PEAK_T,
    "signals-control-8:settling-time": 4 / (0.25 * 2 * math.pi * 20) * 1000,
    "signals-control-8:damped-frequency": 2 * math.pi * 20 * math.sqrt(1 - 0.25 ** 2),
    "signals-control-8:damping-from-coefficients": 12 / (2 * math.sqrt(100)),
    "signals-control-8:damping-for-overshoot": _SC_ZETA10,
    "signals-control-8:resonance-gain": abs(1 / ((1j) ** 2 + 2 * 0.25 * 1j + 1)),
    "signals-control-8:amplitude-at-12-hz": abs(1 / ((1j * 0.6) ** 2 + 2 * 0.25 * (1j * 0.6) + 1)),
    # signals-control-9: Bode plots
    "signals-control-9:dc-gain-db": 20 * math.log10(0.5),
    "signals-control-9:corner-frequency": _bisect(lambda w: abs(_sc_G(w, theta=0.0)) - 0.5 / math.sqrt(2), 1e-3, 5.0),
    "signals-control-9:magnitude-in-db": 20 * math.log10(abs(_sc_G(0.5))),
    "signals-control-9:lag-phase": math.degrees(cmath.phase(1 / (1 + 5j))),
    "signals-control-9:delay-phase": math.degrees(0.5 * 1.0),
    "signals-control-9:total-phase": math.degrees(cmath.phase(_sc_G(0.5))),
    "signals-control-9:cascade-magnitude": 20 * math.log10(abs(_sc_G(0.5) / (1 + 2j * 0.5))),
    "signals-control-9:time-lag": -cmath.phase(_sc_G(0.5)) / 0.5,
    # signals-control-10: stability margins
    "signals-control-10:gain-crossover": _SC_WGC20,
    "signals-control-10:phase-at-crossover": math.degrees(cmath.phase(_SC_LOOP20(_SC_WGC20))),
    "signals-control-10:phase-margin": _SC_PM20,
    "signals-control-10:phase-crossover": _SC_WPC,
    "signals-control-10:gain-margin": _SC_GM,
    "signals-control-10:largest-gain": 20 * _SC_GM,
    "signals-control-10:delay-margin": math.radians(_SC_PM20) / _SC_WGC20,
    "signals-control-10:gain-for-45": _bisect(lambda kp: _sc_pm(lambda w: kp * _sc_G(w))[0] - 45.0, 5.0, 25.0),
    # signals-control-11: PI control
    "signals-control-11:imc-kp": 10 / (0.5 * (2 + 1)),
    "signals-control-11:integral-gain": (10 / (0.5 * 3)) / 10,
    "signals-control-11:crossover-pi": _SC_W_PI,
    "signals-control-11:pi-phase-margin": _SC_PM_PI,
    "signals-control-11:ultimate-period": _SC_PU,
    "signals-control-11:zn-kp": _SC_KP_ZN,
    "signals-control-11:zn-ti": _SC_PU / 1.2,
    "signals-control-11:windup-stored": (10 / (0.5 * 3) / 10) * 1.8 * 7,
    # signals-control-12: sampling
    "signals-control-12:alias-50": _sc_alias(50.0),
    "signals-control-12:alias-140": _sc_alias(140.0),
    "signals-control-12:antialias-attenuation": abs(1 / (1 + 1j * 50 / 20)),
    "signals-control-12:hold-phase-loss": math.degrees((1 / 3) * (0.5 / 2)),
    "signals-control-12:longest-period": (1 / (1 / 3)) / 10,
    "signals-control-12:pi-update": 22.0 + (20 / 3) * (0.9 - 1.2) + (20 / 3) * (0.25 / 10) * 0.9,
    "signals-control-12:plant-pole": math.exp(-0.25 / 10),
    "signals-control-12:step-after-40": functools.reduce(lambda y, _: math.exp(-0.025) * y + 0.5 * (1 - math.exp(-0.025)) * 20, range(40), 0.0),
    # signals-control-13: a sensor filter that makes a loop oscillate
    "signals-control-13:margin-before": _SC_PM0,
    "signals-control-13:filter-lag": math.degrees(cmath.phase(1 / (1 + 1j * _SC_W0 * 1.0))) * -1,
    "signals-control-13:crossover-after": _SC_W1,
    "signals-control-13:margin-after": _SC_PM1,
    "signals-control-13:overshoot-estimate": 100 * math.exp(-math.pi * (_SC_PM1 / 100) / math.sqrt(1 - (_SC_PM1 / 100) ** 2)),
    "signals-control-13:gain-for-45": _SC_KP45,
    "signals-control-13:gain-reduction": 100 * (40 / 3 - _SC_KP45) / (40 / 3),
    "signals-control-13:margin-fast-filter": _SC_PM_FAST,
    # virtual lab 1, recomputed from the CSV
    "signals-control-lab1:gain-20": _sc_final("test_20w") / 20,
    "signals-control-lab1:delay": float(_SC_DELAY),
    "signals-control-lab1:t63": _SC_T63,
    "signals-control-lab1:time-constant": _SC_T63 - _SC_DELAY,
    "signals-control-lab1:pi-gain": 10 / (0.49 * (2 + 1)),
}


@pytest.mark.parametrize("question_id,expected", sorted(SIGNALS_CONTROL_NUMERIC.items()))
def test_signals_control_numeric_key_matches_independent_recalculation(question_id, expected):
    spec = bank("signals-control")[question_id]["solution_spec"]
    allowed = spec["tolerance"] + (spec.get("relative_tolerance") or 0) * abs(spec["answer"])
    assert abs(spec["answer"] - expected) <= allowed, (question_id, spec["answer"], expected)


def test_every_signals_control_numeric_item_is_recalculated():
    numeric = {qid for qid, item in bank("signals-control").items() if item["type"] == "numeric"}
    assert numeric == set(SIGNALS_CONTROL_NUMERIC)


def test_signals_control_closed_loop_simulation_agrees_with_the_margins():
    """A delay-differential simulation of the proportional loop rings down below the ultimate gain and grows above it."""
    ku = 20 * _SC_GM
    assert _sc_closed_loop_amplitude(0.9 * ku) < 0.05
    assert _sc_closed_loop_amplitude(1.1 * ku) > 1.0
    # the sustained oscillation near the ultimate gain has the period 2 pi / w_pc found from the phase condition
    dt = 0.005
    delay_steps = int(round(1.0 / dt))
    u_hist, y, ys = [0.0] * delay_steps, 0.0, []
    for k in range(int(500 / dt)):
        y += dt * (-y + 0.5 * u_hist[k % delay_steps]) / 10.0
        u_hist[k % delay_steps] = ku * (1.0 - y)
        ys.append(y)
    tail = ys[-int(100 / dt):]
    crossings = [i for i in range(1, len(tail)) if tail[i - 1] < 0.0 + sum(tail) / len(tail) <= tail[i]]
    periods = [(b - a) * dt for a, b in zip(crossings, crossings[1:])]
    assert periods and abs(sum(periods) / len(periods) - _SC_PU) < 0.1


def test_signals_control_poles_second_order_and_bode_lessons_state_the_computed_numbers():
    text = reading("signals-control", "signals-control-7")
    y1 = dict(_sc_step_second_order(12.0, 20.0, 20.0, 0.5001))
    t_s1 = _sc_last_exit(_sc_step_second_order(12.0, 20.0, 20.0, 6.0), 1.0)
    yw = dict(_sc_step_second_order(5.0, 4.0, 12.0, 2.0001))
    t_sw = _sc_last_exit(_sc_step_second_order(5.0, 4.0, 12.0, 10.0), 3.0)
    y_rhp = dict(_sc_step_second_order(2.0, 1.0, 1.0, 0.5001, zero=0.5))
    _fragments_in(text, [
        "B = 20/((−2)(−2 + 10)) = **−1.25** and C = 20/((−10)(−10 + 2)) = **0.25**", f"= **{y1[min(y1, key=lambda t: abs(t - 0.5))]:.4f}**", f"(the exact value for this response is {t_s1:.2f} s)",
        "y(∞) = 5 × 4/10 = **2.0**", f"which at t = 0.5 is **−{abs(y_rhp[min(y_rhp, key=lambda t: abs(t - 0.5))]):.4f}**",
        "G(0) = 12/(1 × 4) = **3**", f"y(2) = 3 − 4 × {math.exp(-2):.4f} + {math.exp(-8):.4f} = **{yw[min(yw, key=lambda t: abs(t - 2.0))]:.3f}**", f"the exact 2% time is {t_sw:.2f} s",
    ])
    text = reading("signals-control", "signals-control-8")
    wn, wd = 2 * math.pi * 20, 2 * math.pi * 20 * math.sqrt(1 - 0.0625)
    z_c = _bisect(lambda z: math.exp(-math.pi * z / math.sqrt(1 - z ** 2)) - 0.10, 0.05, 0.95)
    mp_c = dict(_sc_step_second_order(12.0, 100.0, 100.0, 1.0, dt=1e-4))
    mp_c = 100 * (max(mp_c.values()) - 1)
    _fragments_in(text, [
        f"ωn = 2π × 20 = {wn:.1f} rad/s", f"The poles are −{0.25 * wn:.1f} ± j{wd:.1f}", f"ωd = **{wd:.2f} rad/s**", f"the overshoot is **{_SC_OVERSHOOT:.2f}%**",
        f"the peak time is **{_SC_PEAK_T:.2f} ms**", f"the settling time is **{4 / (0.25 * wn) * 1000:.1f} ms**", f"ζ = **{z_c:.4f}**", f"the overshoot is {mp_c:.2f}%",
        "which is **2.0** for ζ = 0.25", f"the amplitude ratio is {abs(1 / ((1j * 0.6) ** 2 + 2 * 0.25 * 1j * 0.6 + 1)):.3f}", f"for ζ = 0.64 it is {abs(1 / ((1j * 0.6) ** 2 + 2 * 0.64 * 1j * 0.6 + 1)):.4f}",
    ])
    wn2 = 2 * math.pi * 10
    wd2 = wn2 * math.sqrt(1 - 0.4 ** 2)
    t2, os2 = _sc_second_order_peak(0.4, wn2)
    _fragments_in(text, [
        f"ωn = 2π × 10 = {wn2:.2f} rad/s and ωd = {wn2:.2f} × √(1 − 0.4²) = {wd2:.2f} rad/s", f"= {os2:.2f}%", f"t_p = π/{wd2:.2f} = {math.pi / wd2:.4f} s = {t2:.2f} ms",
        f"t_s = 4/(0.4 × {wn2:.2f}) = {4 / (0.4 * wn2):.4f} s = {4 / (0.4 * wn2) * 1000:.1f} ms", f"= **{abs(1 / ((1j * 0.6) ** 2 + 2 * 0.4 * 1j * 0.6 + 1)):.3f}**",
    ])
    text = reading("signals-control", "signals-control-9")
    g05 = _sc_G(0.5)
    ph_total = -math.degrees(cmath.phase(g05))
    f2 = 1 / (1 + 1j)
    _fragments_in(text, [
        f"0.5 = **{20 * math.log10(0.5):.2f} dB**".replace("-", "−"), "1/τ = **0.1 rad/min**", f"the magnitude is {0.5 / math.sqrt(2):.4f}, which is {20 * math.log10(0.5 / math.sqrt(2)):.2f} dB".replace("-", "−"),
        f"= {abs(0.5 / (1 + 5j)):.5f}, which is **−{abs(20 * math.log10(abs(g05))):.2f} dB**", f"−atan(5) = −{math.degrees(math.atan(5)):.2f}°", f"−0.5 × 1 rad = −{math.degrees(0.5):.2f}°",
        f"the total phase is **−{ph_total:.2f}°**", f"time lag of {math.radians(ph_total):.4f} rad/0.5 = **{math.radians(ph_total) / 0.5:.3f} min**",
        f"= {abs(f2):.4f} ({20 * math.log10(abs(f2)):.2f} dB) and adds −45°".replace("-", "−"), f"**−{abs(20 * math.log10(abs(g05 * f2))):.2f} dB**", f"**−{ph_total + 45:.2f}°**",
    ])
    g2 = _sc_G(0.5, 2.0, 4.0, 0.5)
    _fragments_in(text, [
        f"= {abs(g2):.4f}, which is **{20 * math.log10(abs(g2)):.2f} dB**".replace("-", "−"), f"a total of **−{-math.degrees(cmath.phase(g2)):.2f}°**", f"= **{-cmath.phase(g2) / 0.5:.3f} min**",
    ])


def test_signals_control_margin_pi_sampling_and_capstone_lessons_state_the_computed_numbers():
    text = reading("signals-control", "signals-control-10")
    pm10, w10 = _sc_pm(lambda w: 10.0 * _sc_G(w))
    pm30, w30 = _sc_pm(lambda w: 30.0 * _sc_G(w))
    kp45 = _bisect(lambda kp: _sc_pm(lambda w: kp * _sc_G(w))[0] - 45.0, 5.0, 25.0)
    w45 = _sc_pm(lambda w: kp45 * _sc_G(w))[1]
    zeta = _SC_PM20 / 100
    mp = 100 * math.exp(-math.pi * zeta / math.sqrt(1 - zeta ** 2))
    _fragments_in(text, [
        f"ω_gc = √99/10 = **{_SC_WGC20:.3f} rad/min**", f"= −{-math.degrees(cmath.phase(_SC_LOOP20(_SC_WGC20))):.2f}°, so the **phase margin is {_SC_PM20:.1f}°**",
        f"ω_pc = **{_SC_WPC:.3f} rad/min**", f"The **gain margin is {_SC_GM:.3f}**", f"= **{20 * _SC_GM:.1f} W/°C**", f"{2 * math.pi / _SC_WPC:.2f} min",
        f"= **{math.radians(_SC_PM20) / _SC_WGC20:.3f} min**", f"| 10 | 5 | {w10:.3f} | {pm10:.1f}° |", f"| 20 | 10 | {_SC_WGC20:.3f} | {_SC_PM20:.1f}° |", f"| 30 | 15 | {w30:.3f} | {pm30:.1f}° |",
        f"ζ ≈ {zeta:.2f} and an overshoot of about {mp:.0f}%", f"gives ω_gc = {w45:.3f} rad/min", f"**K_p = {kp45:.2f} W/°C**",
    ])
    k2 = _sc_G(1.0, 1.2, 5.0, 2.0)
    loop2 = lambda w: 2.0 * _sc_G(w, 1.2, 5.0, 2.0)                           # noqa: E731
    pm2, w2 = _sc_pm(loop2)
    wpc2 = _sc_phase_crossover(loop2, 0.5, 1.2)
    gm2 = 1 / abs(loop2(wpc2))
    _fragments_in(text, [
        f"ω_gc = {w2:.4f} rad/min", f"so the phase margin is **{pm2:.1f}°**", f"ω_pc = {wpc2:.4f} rad/min", f"so the gain margin is **{gm2:.3f}**", f"= **{math.radians(pm2) / w2:.3f} min**",
    ])
    assert k2 != 0
    text = reading("signals-control", "signals-control-11")
    pm_c, w_c = _sc_pm(_sc_pi_loop(20 / 3, 10.0))
    table = []
    for lam in (4.0, 2.0, 1.0, 0.5):
        kp = 10 / (0.5 * (lam + 1))
        pm, w = _sc_pm(_sc_pi_loop(kp, 10.0))
        table.append(f"| {lam:g} | {kp:.3f} | {w:.4f} | {pm:.1f}° |")
    pm_zn, w_zn = _sc_pm(_sc_pi_loop(_SC_KP_ZN, _SC_PU / 1.2))
    _fragments_in(text, table + [
        f"K_p = 10/(0.5 × (2 + 1)) = **{20 / 3:.3f} W/°C**", f"K_i = {20 / 3:.3f}/10 = **{20 / 30:.3f} W/(°C·min)**", f"ω_gc = {20 / 3:.3f} × 0.5/10 = **{w_c:.4f} rad/min**", f"PM = 90° − {math.degrees(w_c):.2f}° = **{pm_c:.1f}°**",
        f"K_u = {20 * _SC_GM:.1f} W/°C and P_u = 2π/{_SC_WPC:.3f} = {_SC_PU:.2f} min", f"K_p = 0.45 K_u = **{_SC_KP_ZN:.2f} W/°C**", f"T_i = P_u/1.2 = **{_SC_PU / 1.2:.2f} min**",
        f"a crossover at {w_zn:.3f} rad/min and a phase margin of only {pm_zn:.1f}°", f"{20 / 30:.3f} × 1.8 × 7 = **{20 / 30 * 1.8 * 7:.1f} W**",
    ])
    kp3 = 5 / (1.2 * (3 + 2))
    pm3, w3 = _sc_pm(_sc_pi_loop(kp3, 5.0, k=1.2, tau=5.0, theta=2.0))
    _fragments_in(text, [f"= **{kp3:.3f}**", f"ω_gc = {kp3:.3f} × 1.2/5 = {w3:.3f} rad/min", f"= **{pm3:.1f}°**"])
    text = reading("signals-control", "signals-control-12")
    zoh_deg = math.degrees((1 / 3) * 0.25)
    pm_s = _sc_pm(_sc_pi_loop(20 / 3, 10.0))[0] - zoh_deg
    _fragments_in(text, [
        f"appears at |50 − 80| = **{_sc_alias(50.0):.0f} Hz**", f"appears at |140 − 2 × 80| = **{_sc_alias(140.0):.0f} Hz**", f"| 50 | {_sc_alias(50.0):.0f} |", f"| 100 | {_sc_alias(100.0):.0f} |",
        f"is **{abs(1 / (1 + 2.5j)):.4f}** ({20 * math.log10(abs(1 / (1 + 2.5j))):.1f} dB)".replace("-", "−"), f"= {(1 / 3) * 0.25:.4f} rad = **{zoh_deg:.2f}°**, reducing the margin to {pm_s:.1f}°", "should not exceed **0.3 min**",
        f"the new command is 22.0 + {20 / 3:.3f} × (0.9 − 1.2) + {20 / 3:.3f} × (0.25/10) × 0.9 = **{22.0 + 20 / 3 * -0.3 + 20 / 3 * 0.025 * 0.9:.2f} W**", f"a = **{math.exp(-0.025):.5f}**", f"gives {10 * (1 - math.exp(-1)):.4f} °C".replace(f"{10 * (1 - math.exp(-1)):.4f}", f"{functools.reduce(lambda y, _: math.exp(-0.025) * y + 0.5 * (1 - math.exp(-0.025)) * 20, range(40), 0.0):.4f}"),
        f"|60 − 100| = **{_sc_alias(60.0, 100.0):.0f} Hz**", f"= **{abs(1 / (1 + 4j)):.4f}**", "= **0.5 min**", "= **2.7083**",
    ])
    text = reading("signals-control", "signals-control-13")
    pm0, w0 = _SC_PM0, _SC_W0
    pm1, w1 = _SC_PM1, _SC_W1
    rows = []
    for tf in (0.0, 0.25, 0.5, 1.0, 2.0):
        pm, w = _sc_pm(_sc_pi_loop(40 / 3, 10.0, tf=tf))
        rows.append(f"| {tf:g} | {w:.3f} | {pm:.1f}° | {abs(1 / (1 + 6j * tf)):.3f} |")
    zeta1 = pm1 / 100
    os1 = 100 * math.exp(-math.pi * zeta1 / math.sqrt(1 - zeta1 ** 2))
    w45 = _sc_pm(lambda w: _sc_pi_loop(_SC_KP45, 10.0, tf=1.0)(w))[1]
    _fragments_in(text, rows + [
        f"**ω_gc = {w0:.4f} rad/min**", f"= **{pm0:.1f}°**", f"**−{math.degrees(math.atan(w0)):.2f}°**", f"**ω_gc = {w1:.4f} rad/min**", f"**phase margin falls from {pm0:.1f}° to {pm1:.1f}°**",
        f"overshoot of about {os1:.0f}%", f"The delay margin is {math.radians(pm1):.4f}/{w1:.4f} = {math.radians(pm1) / w1:.2f} min", f"**ω_gc = {w45:.4f} rad/min**", f"= **{_SC_KP45:.2f} W/°C**",
        f"a reduction of **{100 * (40 / 3 - _SC_KP45) / (40 / 3):.0f}%**",
    ])
    kp2 = 5 / (1.2 * (2 + 2))
    pm2_0, _ = _sc_pm(_sc_pi_loop(kp2, 5.0, k=1.2, tau=5.0, theta=2.0))
    pm2_1, w2_1 = _sc_pm(_sc_pi_loop(kp2, 5.0, k=1.2, tau=5.0, theta=2.0, tf=1.5))
    _fragments_in(text, [f"= **{pm2_0:.1f}°**", f"ω_gc = {w2_1:.4f} rad/min, and the phase margin is **{pm2_1:.1f}°**, a loss of {pm2_0 - pm2_1:.1f}°"])


def test_signals_control_lab_text_and_keys_agree_with_the_dataset():
    assert len(_SC_ROWS) == 366 and {r["test"] for r in _SC_ROWS} == {"test_10w", "test_20w", "test_30w"}
    assert {int(r["run"]) for r in _SC_ROWS} == {1, 2} and {int(r["time_min"]) for r in _SC_ROWS} == set(range(61))
    # the readings follow a first-order-plus-delay response with gains 0.500, 0.485 and 0.460 degC/W plus noise below 0.06 degC
    for r in _SC_ROWS:
        u, t = float(r["power_w"]), int(r["time_min"])
        gain = {10: 0.500, 20: 0.485, 30: 0.460}[int(u)]
        model = 0.0 if t < 1 else gain * u * (1 - math.exp(-(t - 1) / 10))
        assert abs(float(r["rise_c"]) - model) <= 0.06, r
    gains = {t: _sc_final(t) / int(t.split("_")[1][:-1]) for t in ("test_10w", "test_20w", "test_30w")}
    text = (COURSES / "signals-control/labs/01-identifying-an-incubator-from-step-tests.md").read_text(encoding="utf-8")
    final20 = _sc_final("test_20w")
    _fragments_in(text, [
        "are " + ", ".join(f"{_sc_final(t):.2f}" for t in gains) + " °C for 10, 20 and 30 W", "so the gains are " + ", ".join(f"{g:.3f}" for g in gains.values()) + " °C/W",
        f"within 2% of the settled value ({0.02 * final20:.2f} °C) up to minute {_SC_DELAY}", f"reaches 63.2% of {final20:.2f} °C, which is {0.632 * final20:.2f} °C, at {_SC_T63:.2f} min by linear interpolation",
        f"The time constant is {_SC_T63:.2f} − {_SC_DELAY} = {_SC_T63 - _SC_DELAY:.2f} min", "the proportional gain is 10/(0.49 × 3) = 6.803 W/°C",
        f"The gain at 30 W is {gains['test_30w'] / gains['test_10w']:.3f} times the gain at 10 W", "nothing here is evidence about any device",
    ])
    field = bank("signals-control")["signals-control-lab1:linearity"]["solution_spec"]["field_specs"][0]
    assert abs(field["answer"] - gains["test_30w"] / gains["test_10w"]) <= field["tolerance"] and field["significant_figures"] == 3
    checks = {(c["row_id"], c["column"]): c["answer"] for c in bank("signals-control")["signals-control-lab1:step-summary"]["solution_spec"]["validation_spec"]["checks"]}
    assert len(checks) == 9
    for test in gains:
        assert checks[(test, "runs")] == 2 and checks[(test, "samples")] == 61
        assert abs(checks[(test, "mean_final_rise")] - _sc_final(test)) < 1e-3


# ---- differential equations 0.3.0 ----------------------------------------------------------------------------
def _de_integrate(f, x0: list[float], t_end: float, dt: float) -> list[tuple[float, list[float]]]:
    return _sc_rk4(f, x0, t_end, dt)


def _de_at(traj: list[tuple[float, list[float]]], t: float, index: int = 0) -> float:
    return min(traj, key=lambda p: abs(p[0] - t))[1][index]


def _de_chamber(c_in, tau: float = 40.0, t_end: float = 400.0, dt: float = 0.02):
    return _de_integrate(lambda t, x: [(c_in(t) - x[0]) / tau], [0.0], t_end, dt)


def _de_sine_fit(traj, omega: float, t_start: float) -> tuple[float, float]:
    """Amplitude and phase lag (rad) of a steady sinusoid, by projecting the last whole period on sin and cos."""
    period = 2 * math.pi / omega
    pts = [(t, x[0]) for t, x in traj if t >= t_start and t <= t_start + period]
    n = len(pts)
    a = 2 * sum(y * math.sin(omega * t) for t, y in pts) / n
    b = 2 * sum(y * math.cos(omega * t) for t, y in pts) / n
    return math.hypot(a, b), math.atan2(-b, a)


def _de_forced_amplitude(r: float, zeta: float = 0.15, wn: float = 20.0, m: float = 0.2, force: float = 0.5) -> float:
    c, k = 2 * zeta * wn * m, wn ** 2 * m
    w = r * wn
    traj = _de_integrate(lambda t, x: [x[1], (force * math.cos(w * t) - c * x[1] - k * x[0]) / m], [0.0, 0.0], 8.0, 5e-4)
    return 1000 * max(abs(x[0]) for t, x in traj if t > 6.0)


def _de_free_pan():
    m, c, k = 0.2, 1.2, 80.0
    traj = _de_integrate(lambda t, x: [x[1], -(c * x[1] + k * x[0]) / m], [1.0, 0.0], 2.5, 1e-4)
    peaks = [(t, x[0]) for (t0, x0), (t, x), (t2, x2) in zip(traj, traj[1:], traj[2:]) if x[0] > x0[0] and x[0] >= x2[0] and x[0] > 0.0]
    return peaks


_DE_PEAKS = _de_free_pan()


def _de_linear_flow(matrix, x0, t_end):
    (a, b), (c, d) = matrix
    return _de_integrate(lambda t, x: [a * x[0] + b * x[1], c * x[0] + d * x[1]], list(x0), t_end, 1e-3)


def _de_logistic(n0: float = 0.2, k: float = 8.0, r: float = 0.05, t_end: float = 130.0):
    return _de_integrate(lambda t, x: [r * x[0] * (1 - x[0] / k)], [n0], t_end, 0.01)


_DE_LOGISTIC = _de_logistic()


def _de_first_crossing(traj, level: float) -> float:
    return next(t for t, x in traj if x[0] >= level)


def _de_toggle_flow(x0, a: float = 3.0, t_end: float = 60.0):
    return _de_integrate(lambda t, x: [a / (1 + x[1] ** 2) - x[0], a / (1 + x[0] ** 2) - x[1]], list(x0), t_end, 0.01)


def _de_jacobian_eigs(a: float, point: tuple[float, float]):
    h = 1e-6
    def f(x, y): return (a / (1 + y ** 2) - x, a / (1 + x ** 2) - y)
    x, y = point
    j = [[(f(x + h, y)[i] - f(x - h, y)[i]) / (2 * h), (f(x, y + h)[i] - f(x, y - h)[i]) / (2 * h)] for i in range(2)]
    tr, det = j[0][0] + j[1][1], j[0][0] * j[1][1] - j[0][1] * j[1][0]
    disc = tr ** 2 - 4 * det
    return j, det, ((tr + math.sqrt(disc)) / 2, (tr - math.sqrt(disc)) / 2) if disc >= 0 else None


def _de_symmetric(a: float) -> float:
    return _bisect(lambda s: a / (1 + s ** 2) - s, 0.0, 10.0)


def _de_euler_threshold(rate: float, predicate) -> float:
    return _bisect(lambda h: 1.0 if predicate(1 - rate * h) else -1.0, 1e-6, 500.0)


def _de_fit_line(xs, ys):
    xb, yb = sum(xs) / len(xs), sum(ys) / len(ys)
    slope = sum((x - xb) * (y - yb) for x, y in zip(xs, ys)) / sum((x - xb) ** 2 for x in xs)
    return slope, yb - slope * xb


_DE_T = [0, 6, 12, 18, 24]
_DE_DATA = [round(100.0 * math.exp(-0.04 * t), 1) for t in _DE_T]
_DE_SL, _DE_IC = _de_fit_line(_DE_T, _DE_DATA)
_DE_HOLD_SL, _DE_HOLD_IC = _de_fit_line(_DE_T[:3], _DE_DATA[:3])
_DE_K_FIT = -_de_fit_line(_DE_T, [math.log(v) for v in _DE_DATA])[0]
_DE_N24 = _DE_DATA[-1]


def _de_lab_rows() -> list[dict[str, str]]:
    import csv
    return list(csv.DictReader((COURSES / "differential-equations/labs/cell-counts-after-growth-factor-removal.csv").open(encoding="utf-8")))


_DE_ROWS = _de_lab_rows()
_DE_MEAN = {t: sum(float(r["count_k"]) for r in _DE_ROWS if int(r["hours"]) == t) / 3 for t in (0, 6, 12, 18, 24, 36, 48)}
_DE_LAB_SL, _DE_LAB_IC = _de_fit_line([0, 6, 12, 18, 24], [_DE_MEAN[t] for t in (0, 6, 12, 18, 24)])
_DE_LAB_K = -_de_fit_line([0, 6, 12, 18, 24], [math.log(_DE_MEAN[t]) for t in (0, 6, 12, 18, 24)])[0]
_DE_LAB_N0 = math.exp(_de_fit_line([0, 6, 12, 18, 24], [math.log(_DE_MEAN[t]) for t in (0, 6, 12, 18, 24)])[1])
_DE_LAB_EXP48 = _DE_LAB_N0 * math.exp(-_DE_LAB_K * 48)

_DE_STEP60 = _de_at(_de_chamber(lambda t: 1.0), 60.0)
_DE_SINE = _de_chamber(lambda t: math.sin(2 * math.pi / 120 * t), t_end=1500.0)
_DE_SINE_AMP, _DE_SINE_PHASE = _de_sine_fit(_DE_SINE, 2 * math.pi / 120, 1200.0)
def _de_pulse(t_eval: float, width: float = 30.0, tau: float = 40.0) -> float:
    """Pulse response integrated in two stages, switching the input exactly at the edge of the pulse."""
    first = _de_integrate(lambda t, x: [(1.0 - x[0]) / tau], [0.0], min(t_eval, width), 0.005)
    if t_eval <= width:
        return first[-1][1][0]
    second = _de_integrate(lambda t, x: [(0.0 - x[0]) / tau], first[-1][1], t_eval - width, 0.005)
    return second[-1][1][0]


_DE_DECAY = _de_chamber(lambda t: math.exp(-t / 100.0), t_end=200.0)
_DE_RAMP = _de_chamber(lambda t: 0.02 * t, t_end=600.0)
_DE_PEAK_T, _DE_PEAK_Y = max(((t, x[0]) for t, x in _DE_DECAY), key=lambda p: p[1])
_DE_NODE1 = _de_linear_flow(((-2, 1), (1, -2)), (3.0, 1.0), 1.0)
_DE_SADDLE2 = _de_linear_flow(((1, 2), (2, 1)), (1.1, -1.0), 2.0)
_DE_SPIRAL = _de_linear_flow(((-0.5, 2), (-2, -0.5)), (1.0, 0.0), 8.0)
_DE_TOGGLE_END = _de_toggle_flow((1.3, 1.1))[-1][1]


def _de_spiral_turn() -> tuple[float, float]:
    """Time and distance ratio at the first return of the spiral to the positive x axis, found by linear interpolation of the simulated flow."""
    for (t0, a), (t1, b) in zip(_DE_SPIRAL, _DE_SPIRAL[1:]):
        if t0 > 1.0 and a[1] > 0 >= b[1] and b[0] > 0:
            f = a[1] / (a[1] - b[1])
            x = a[0] + f * (b[0] - a[0])
            return t0 + f * (t1 - t0), x
    raise AssertionError('no return to the axis')


_DE_TURN_T, _DE_TURN_R = _de_spiral_turn()
_DE_MM = _de_integrate(lambda t, x: [-2.0 * x[0] / (0.5 + x[0])], [5.0], 3.5, 1e-4)

DIFFERENTIAL_EQUATIONS_NUMERIC = {
    # items written before 2026-10-08, recomputed from the numbers in their prompts
    "differential-equations-1:check": 8 * math.exp(-0.25 * 4),
    "differential-equations-2:check": math.sqrt(50 / 2),
    "differential-equations-4:check": 3 + 0.25 * 2,
    "differential-equations-1:characteristic-time": 1 / 0.5,
    "differential-equations-4:euler-stability-limit": _de_euler_threshold(50.0, lambda f: abs(f) < 1),
    "differential-equations-5:steady-state": 0.05 * 10 / (0.05 + 0.02),
    "differential-equations-5:time-constant": 1 / (0.05 + 0.02),
    "differential-equations-5:time-to-90": math.log(10) / 0.07,
    "differential-equations-5:euler-step": 0.0 + 10 * (0.05 * 10 - 0.07 * 0.0),
    "differential-equations-5:stability-limit": _de_euler_threshold(0.07, lambda f: abs(f) < 1),
    "differential-equations-6:equilibrium": 1e6 * (1 - 0.01 / 0.03),
    "differential-equations-6:recovery-tau": 1 / (0.03 - 0.01),
    "differential-equations-6:msy": max(h * 1e6 * (1 - h / 0.03) for h in [i * 1e-5 for i in range(1, 3000)]),
    "differential-equations-6:slow-eigenvalue": (-0.6 + math.sqrt(0.36 - 4 * 0.02)) / 2,
    # differential-equations-7: forced first-order systems
    "differential-equations-7:chamber-tau": 20 / 0.5,
    "differential-equations-7:step-fraction": _DE_STEP60,
    "differential-equations-7:time-to-95": _de_first_crossing(_de_chamber(lambda t: 1.0, t_end=200.0), 0.95),
    "differential-equations-7:ramp-lag": 0.02 * 580.0 - _de_at(_DE_RAMP, 580.0),
    "differential-equations-7:amplitude-ratio": _DE_SINE_AMP,
    "differential-equations-7:time-lag": _DE_SINE_PHASE / (2 * math.pi / 120),
    "differential-equations-7:pulse-response": _de_pulse(60.0),
    "differential-equations-7:peak-time": _DE_PEAK_T,
    # differential-equations-8: resonance and damping
    "differential-equations-8:natural-frequency": math.sqrt(80 / 0.2),
    "differential-equations-8:damping-ratio": 1.2 / (2 * math.sqrt(80 * 0.2)),
    "differential-equations-8:damped-period": _DE_PEAKS[1][0] - _DE_PEAKS[0][0],
    "differential-equations-8:log-decrement": math.log(_DE_PEAKS[0][1] / _DE_PEAKS[1][1]),
    "differential-equations-8:after-three-cycles": _DE_PEAKS[3][1] / _DE_PEAKS[0][1],
    "differential-equations-8:resonant-amplitude": _de_forced_amplitude(1.0),
    "differential-equations-8:half-frequency-amplitude": _de_forced_amplitude(0.5),
    "differential-equations-8:half-power-bandwidth": 2 * 0.15 * 20.0,
    # differential-equations-9: phase portraits
    "differential-equations-9:determinant": (-2) * (-2) - 1 * 1,
    "differential-equations-9:slow-eigenvalue": (-4 + math.sqrt(16 - 12)) / 2,
    "differential-equations-9:initial-coefficient": (3.0 + 1.0) / 2,
    "differential-equations-9:state-at-one": _de_at(_DE_NODE1, 1.0, 0),
    "differential-equations-9:spiral-period": _DE_TURN_T,
    "differential-equations-9:spiral-shrink": _DE_TURN_R,
    "differential-equations-9:unstable-eigenvalue": (2 + math.sqrt(4 + 12)) / 2,
    "differential-equations-9:saddle-state": _de_at(_DE_SADDLE2, 2.0, 0),
    # differential-equations-10: logistic growth
    "differential-equations-10:half-capacity-time": _de_first_crossing(_DE_LOGISTIC, 4.0),
    "differential-equations-10:count-at-24h": _de_at(_DE_LOGISTIC, 24.0),
    "differential-equations-10:fraction-at-48h": _de_at(_DE_LOGISTIC, 48.0) / 8.0,
    "differential-equations-10:doubling-time": math.log(2) / 0.05,
    "differential-equations-10:maximum-growth-rate": max(0.05 * x[0] * (1 - x[0] / 8.0) for t, x in _DE_LOGISTIC),
    "differential-equations-10:time-to-90": _de_first_crossing(_DE_LOGISTIC, 7.2),
    "differential-equations-10:logit-slope": (math.log(_de_at(_DE_LOGISTIC, 24.0) / (8.0 - _de_at(_DE_LOGISTIC, 24.0))) - math.log(0.2 / 7.8)) / 24,
    "differential-equations-10:extrapolation-error": 0.2 * math.exp(0.05 * 72) - _de_at(_DE_LOGISTIC, 72.0),
    # differential-equations-11: toggle switch
    "differential-equations-11:symmetric-state": _de_symmetric(3.0),
    "differential-equations-11:coupling": -_de_jacobian_eigs(3.0, (_de_symmetric(3.0),) * 2)[0][0][1],
    "differential-equations-11:unstable-eigenvalue": _de_jacobian_eigs(3.0, (_de_symmetric(3.0),) * 2)[2][0],
    "differential-equations-11:high-state": _DE_TOGGLE_END[0],
    "differential-equations-11:low-state": _DE_TOGGLE_END[1],
    "differential-equations-11:relaxation-time": 1 / abs(_de_jacobian_eigs(3.0, tuple(_DE_TOGGLE_END))[2][0]),
    "differential-equations-11:threshold": _bisect(lambda a: _de_jacobian_eigs(a, (_de_symmetric(a),) * 2)[2][0], 1.2, 3.0),
    "differential-equations-11:coupling-below-threshold": -_de_jacobian_eigs(1.5, (_de_symmetric(1.5),) * 2)[0][0][1],
    # differential-equations-12: stiff equations
    "differential-equations-12:stability-limit": _de_euler_threshold(50.0, lambda f: abs(f) < 1),
    "differential-equations-12:positivity-limit": _de_euler_threshold(50.0, lambda f: f >= 0),
    "differential-equations-12:explicit-factor": abs(1 - 50 * 0.05),
    "differential-equations-12:implicit-factor": 1 / (1 + 50 * 0.05),
    "differential-equations-12:stiffness-ratio": abs((-50.1 - math.sqrt(50.1 ** 2 - 4 * 2.5)) / (-50.1 + math.sqrt(50.1 ** 2 - 4 * 2.5))),
    "differential-equations-12:depletion-time": next(t for t, x in _DE_MM if x[0] <= 0.5),
    "differential-equations-12:initial-rate": 2.0 * 5.0 / (0.5 + 5.0),
    "differential-equations-12:mm-positivity-step": _bisect(lambda h: 1.0 if 1e-6 - h * 2.0 * 1e-6 / (0.5 + 1e-6) >= 0 else -1.0, 1e-3, 5.0),
    # differential-equations-13: negative predicted counts
    "differential-equations-13:line-slope": _DE_SL,
    "differential-equations-13:zero-crossing": _DE_IC / -_DE_SL,
    "differential-equations-13:line-prediction": _DE_IC + _DE_SL * 48,
    "differential-equations-13:first-order-rate": _DE_K_FIT,
    "differential-equations-13:positivity-limit": _de_euler_threshold(0.04, lambda f: f >= 0),
    "differential-equations-13:single-step": functools.reduce(lambda n, _: n * (1 - 0.04 * 48), range(1), _DE_N24),
    "differential-equations-13:four-steps": functools.reduce(lambda n, _: n * (1 - 0.04 * 12), range(4), _DE_N24),
    "differential-equations-13:holdout-error": _DE_N24 - (_DE_HOLD_IC + _DE_HOLD_SL * 24),
    # virtual lab 1, recomputed from the CSV
    "differential-equations-lab1:early-rate": _DE_LAB_K,
    "differential-equations-lab1:line-zero": _DE_LAB_IC / -_DE_LAB_SL,
    "differential-equations-lab1:line-at-48": _DE_LAB_IC + _DE_LAB_SL * 48,
    "differential-equations-lab1:exponential-at-48": _DE_LAB_EXP48,
}


@pytest.mark.parametrize("question_id,expected", sorted(DIFFERENTIAL_EQUATIONS_NUMERIC.items()))
def test_differential_equations_numeric_key_matches_independent_recalculation(question_id, expected):
    spec = bank("differential-equations")[question_id]["solution_spec"]
    allowed = spec["tolerance"] + (spec.get("relative_tolerance") or 0) * abs(spec["answer"])
    assert abs(spec["answer"] - expected) <= allowed, (question_id, spec["answer"], expected)


def test_every_differential_equations_numeric_item_is_recalculated():
    numeric = {qid for qid, item in bank("differential-equations").items() if item["type"] == "numeric"}
    assert numeric == set(DIFFERENTIAL_EQUATIONS_NUMERIC)


def _mn(x: float, nd: int = 2) -> str:
    """Format with a typographic minus sign, as the lessons do."""
    return f"{x:.{nd}f}".replace("-", "−")


def test_differential_equations_chamber_resonance_and_phase_portrait_lessons_state_the_computed_numbers():
    text = reading("differential-equations", "differential-equations-7")
    t95 = _de_first_crossing(_de_chamber(lambda t: 1.0, t_end=200.0), 0.95)
    peak_y = _DE_PEAK_Y
    pulse30 = _de_pulse(30.0)
    _fragments_in(text, [
        "so τ = **40 min**", f"= **{_DE_STEP60:.4f}** of the new concentration", f"= **{t95:.1f} min**", f"the offset is 0.02 × 40 = **{0.02 * 580.0 - _de_at(_DE_RAMP, 580.0):.1f} mM**",
        f"ω = 2π/120 = {2 * math.pi / 120:.5f} rad/min and ωτ = {2 * math.pi / 120 * 40:.3f}", f"the amplitude is multiplied by **{_DE_SINE_AMP:.4f}**", f"the phase lag is {math.degrees(_DE_SINE_PHASE):.1f}°",
        f"the time lag is φ/ω = **{_DE_SINE_PHASE / (2 * math.pi / 120):.1f} min**", f"attenuated to {1 / math.sqrt(1 + (2 * math.pi / 10 * 40) ** 2):.3f} of its amplitude",
        f"= **{_DE_PEAK_T:.1f} min** at {peak_y:.4f} c₀", f"the chamber has reached {pulse30:.4f} c₀", f"= **{_de_pulse(60.0):.4f} c₀**",
    ])
    tau2 = 15 / 0.4
    w2 = 2 * math.pi / 90
    traj2 = _de_chamber(lambda t: 1.0, tau=tau2, t_end=100.0)
    sine2 = _de_chamber(lambda t: math.sin(w2 * t), tau=tau2, t_end=1200.0)
    amp2, ph2 = _de_sine_fit(sine2, w2, 900.0)
    _fragments_in(text, [
        f"τ = 15/0.4 = **{tau2:.1f} min**", f"= **{_de_at(traj2, 50.0):.4f}**", f"ω = 2π/90 = {w2:.5f} rad/min, ωτ = {w2 * tau2:.3f}", f"= **{amp2:.4f}**",
        f"φ = atan({w2 * tau2:.3f}) = {math.degrees(ph2):.1f}° and the time lag is φ/ω = **{ph2 / w2:.1f} min**",
    ])
    text = reading("differential-equations", "differential-equations-8")
    wn, zeta = 20.0, 0.15
    wd = wn * math.sqrt(1 - zeta ** 2)
    delta = math.log(_DE_PEAKS[0][1] / _DE_PEAKS[1][1])
    r_peak = math.sqrt(1 - 2 * zeta ** 2)
    _fragments_in(text, [
        f"ωn = √(80/0.2) = **{wn:.0f} rad/s** ({wn / (2 * math.pi):.2f} Hz)", f"ζ = 1.2/8 = **{zeta}**", f"ωd = {wd:.3f} rad/s, and the damped period is 2π/ωd = **{2 * math.pi / wd:.4f} s**",
        f"= **{delta:.4f}**", f"e^(−3δ) = **{_DE_PEAKS[3][1] / _DE_PEAKS[0][1]:.4f}** of its starting value", f"after ten cycles it is {100 * _DE_PEAKS[0][1] ** 0 * math.exp(-10 * delta):.3f}% of it",
        f"(F/k)/(2ζ) = **{_de_forced_amplitude(1.0):.2f} mm**", f"at r = √(1 − 2ζ²) = {r_peak:.4f}, where X = {_de_forced_amplitude(r_peak):.2f} mm", f"X = **{_de_forced_amplitude(0.5):.2f} mm**", "approximately 2ζωn = **6.0 rad/s**",
    ])
    # the half-power width of the exact amplitude curve is within 3% of the approximation 2*zeta*wn
    amp = lambda w: 1 / math.sqrt((1 - (w / wn) ** 2) ** 2 + (2 * zeta * w / wn) ** 2)          # noqa: E731
    pk = amp(wn * r_peak)
    w_lo = _bisect(lambda w: amp(w) - pk / math.sqrt(2), 0.5 * wn, wn * r_peak)
    w_hi = _bisect(lambda w: amp(w) - pk / math.sqrt(2), wn * r_peak, 1.5 * wn)
    assert abs((w_hi - w_lo) - 6.0) / 6.0 < 0.03
    w2n = math.sqrt(20 / 0.05)
    wd2 = w2n * math.sqrt(1 - 0.2 ** 2)
    _fragments_in(text, [
        f"ωn = √(20/0.05) = **{w2n:.0f} rad/s**", f"ζ = 0.4/(2√(20 × 0.05)) = **0.2**, so ωd = {w2n:.0f} × √(1 − 0.2²) = {wd2:.3f} rad/s", f"= **{2 * math.pi * 0.2 / math.sqrt(1 - 0.04):.4f}**",
        f"X = {1000 * 0.2 / 20:.1f}/(2 × 0.2) = **{_de_forced_amplitude(1.0, zeta=0.2, wn=w2n, m=0.05, force=0.2):.1f} mm**",
    ])
    text = reading("differential-equations", "differential-equations-9")
    spiral_turn_t, spiral_turn_r = _DE_TURN_T, _DE_TURN_R
    wflow = _de_linear_flow(((-3, 2), (1, -2)), (1.0, 2.0), 0.5)
    _fragments_in(text, [
        "has trace −4 and determinant **3**", "λ₁ = **−1** and λ₂ = −3", "gives c₁ = **2** and c₂ = 1", f"(**{_de_at(_DE_NODE1, 1.0, 0):.4f}**, {_de_at(_DE_NODE1, 1.0, 1):.4f})",
        f"a period of 2π/2 = **{spiral_turn_t:.4f}**", f"e^(−0.5 × {spiral_turn_t:.4f}) = **{spiral_turn_r:.4f}**", "The eigenvalues are **3** and −1",
        f"the state is ({_de_at(_DE_SADDLE2, 2.0, 0):.1f}, {_de_at(_DE_SADDLE2, 2.0, 1):.1f})", "T = −5 and D = **4**", f"x(0.5) = (**{_de_at(wflow, 0.5, 0):.4f}**, {_de_at(wflow, 0.5, 1):.4f})",
    ])


def test_differential_equations_logistic_switch_stiffness_and_capstone_lessons_state_the_computed_numbers():
    text = reading("differential-equations", "differential-equations-10")
    n24, n48 = _de_at(_DE_LOGISTIC, 24.0), _de_at(_DE_LOGISTIC, 48.0)
    t_half = _de_first_crossing(_DE_LOGISTIC, 4.0)
    t90 = _de_first_crossing(_DE_LOGISTIC, 7.2)
    logit = lambda n: math.log(n / (8.0 - n))                                      # noqa: E731
    exp72, log72 = 0.2 * math.exp(0.05 * 72), _de_at(_DE_LOGISTIC, 72.0)
    _fragments_in(text, [
        "(K − N₀)/N₀ = **39**", f"= **{n24:.4f} million**", f"N(48 h) is **{n48 / 8:.4f}** of capacity ({n48:.3f} million)", f"ln(39)/0.05 = **{t_half:.1f} h**", f"= ln(351)/0.05 = {t90:.1f} h",
        f"ln 2/r = **{math.log(2) / 0.05:.2f} h**", f"rK/4 = **{max(0.05 * x[0] * (1 - x[0] / 8.0) for t, x in _DE_LOGISTIC):.2f} million cells per hour**",
        f"logit(N₀) = ln(0.2/7.8) = {_mn(logit(0.2), 3)} and logit(N) = {_mn(logit(n24), 3)}", f"so the slope is **{(logit(n24) - logit(0.2)) / 24:.4f} h⁻¹**",
        f"by {100 * (0.2 * math.exp(1.2) / n24 - 1):.1f}% ({0.2 * math.exp(1.2):.3f} against {n24:.3f} million)", f"the exponential gives {exp72:.2f} million cells, and the logistic gives {log72:.3f} million",
        f"too high by **{exp72 - log72:.2f} million cells**, about {100 * (exp72 - log72) / log72:.0f}%", f"by 96 h it gives {0.2 * math.exp(0.05 * 96):.1f} million cells",
    ])
    traj2 = _de_logistic(0.1, 5.0, 0.08, 120.0)
    _fragments_in(text, [
        f"t₁/₂ = ln(49)/0.08 = **{_de_first_crossing(traj2, 2.5):.1f} h**", f"= **{_de_at(traj2, 36.0):.3f} million**", f"ln 2/0.08 = {math.log(2) / 0.08:.2f} h",
        f"0.1 e^(5.76) = {0.1 * math.exp(0.08 * 72):.1f} million", f"the logistic gives {_de_at(traj2, 72.0):.2f} million",
    ])
    text = reading("differential-equations", "differential-equations-11")
    s = _de_symmetric(3.0)
    j, det, eigs = _de_jacobian_eigs(3.0, (s, s))
    m = -j[0][1]
    j_hi, det_hi, eigs_hi = _de_jacobian_eigs(3.0, tuple(_DE_TOGGLE_END))
    s15 = _de_symmetric(1.5)
    m15 = -_de_jacobian_eigs(1.5, (s15, s15))[0][0][1]
    end_b = _de_toggle_flow((1.1, 1.3))[-1][1]
    _fragments_in(text, [
        f"gives **s = {s:.4f}**", f"x = (3 + √5)/2 = **{_DE_TOGGLE_END[0]:.4f}** with y = (3 − √5)/2 = {_DE_TOGGLE_END[1]:.4f}", f"= **{m:.4f}**", f"−1 − m = {_mn(eigs[1], 4)}", f"**−1 + m = {eigs[0]:.4f}**",
        f"1 − m² = {_mn(det, 3)} < 0", f"c_y = {-j_hi[0][1]:.4f} and c_x = {-j_hi[1][0]:.4f}", f"that is **{_mn(eigs_hi[0], 4)}** and {_mn(eigs_hi[1], 4)}", f"1/{abs(eigs_hi[0]):.4f} = **{1 / abs(eigs_hi[0]):.1f}**",
        f"m = {m15:.4f} < 1", f"the system settles at ({_DE_TOGGLE_END[0]:.3f}, {_DE_TOGGLE_END[1]:.3f})", f"mirror image ({end_b[0]:.3f}, {end_b[1]:.3f})",
    ])
    s4 = _de_symmetric(4.0)
    j4, _, _ = _de_jacobian_eigs(4.0, (s4, s4))
    m4 = -j4[0][1]
    hi4 = _bisect(lambda x: x - 4.0 / (1 + (4.0 / (1 + x ** 2)) ** 2), s4 + 0.05, 8.0)
    lo4 = 4.0 / (1 + hi4 ** 2)
    eig4 = _de_jacobian_eigs(4.0, (hi4, lo4))[2]
    _fragments_in(text, [f"gives **s = {s4:.4f}**", f"= **{m4:.4f}**", f"= **{m4 - 1:.4f}** is positive", f"x = {hi4:.4f} and y = {lo4:.4f}", f"= {_mn(eig4[0], 4)} and {_mn(eig4[1], 4)}"])
    text = reading("differential-equations", "differential-equations-12")
    disc = math.sqrt(50.1 ** 2 - 4 * 2.5)
    l_slow, l_fast = (-50.1 + disc) / 2, (-50.1 - disc) / 2
    # Use the strict stability inequality before rounding to an integer step count.
    min_steps = math.floor(10 * abs(l_fast) / 2) + 1
    assert abs(1 + l_fast * (10 / min_steps)) < 1
    assert abs(1 + l_fast * (10 / (min_steps - 1))) > 1
    mm = _de_integrate(lambda t, x: [-2.0 * x[0] / (0.5 + x[0])], [5.0], 3.5, 1e-4)
    seq = [(1 - 50 * 0.05) ** k for k in range(4)]
    _fragments_in(text, [
        f"h < 2/50 = **{_de_euler_threshold(50.0, lambda f: abs(f) < 1):.2f} h**", f"h ≤ **{_de_euler_threshold(50.0, lambda f: f >= 0):.2f} h**", f"= {_mn(1 - 50 * 0.05)}, with magnitude **1.5**", ", ".join(f"{v:.3g}" for v in seq).replace("-", "−"),
        f"= **{1 / (1 + 50 * 0.05):.4f}**", f"e^(−2.5) = {math.exp(-2.5):.4f}", f"the eigenvalues are **{_mn(l_slow, 5)}** and {_mn(l_fast, 3)} h⁻¹", f"The ratio is |{_mn(l_fast, 3)}/{_mn(l_slow, 5)}| = **{abs(l_fast / l_slow):.0f}**",
        f"= {2 / abs(l_fast):.4f} h throughout: at least {math.floor(10 / (2 / abs(l_fast))) + 1} equal steps", f"= **{2.0 * 5.0 / 5.5:.3f} mM/h**", f"= **{next(t for t, x in mm if x[0] <= 0.5):.3f} h**", "**h ≤ K_m/V_max = 0.25 h**", "= −2.5 mM",
    ])
    mm3 = _de_integrate(lambda t, x: [-1.5 * x[0] / (0.8 + x[0])], [4.0], 4.5, 1e-4)
    _fragments_in(text, ["= **0.10 h**", f"= **{_mn(1 - 20 * 0.08, 1)}**", f"= **{1 / (1 + 20 * 0.08):.4f}**", f"e^(−1.6) = {math.exp(-1.6):.4f}", f"= **{next(t for t, x in mm3 if x[0] <= 0.4):.3f} h**"])
    text = reading("differential-equations", "differential-equations-13")
    b_data = [round(80.0 * math.exp(-0.05 * t), 1) for t in _DE_T]
    sl_b, ic_b = _de_fit_line(_DE_T, b_data)
    hold_sl, hold_ic = _de_fit_line(_DE_T[:3], b_data[:3])
    resid = [y - (_DE_IC + _DE_SL * t) for t, y in zip(_DE_T, _DE_DATA)]
    _fragments_in(text, [
        "**" + ", ".join(f"{v:.1f}" for v in _DE_DATA) + "**", f"slope **{_mn(_DE_SL, 4)}** per hour and intercept {_DE_IC:.2f}", f"The largest residual is {max(abs(r) for r in resid):.1f}", f"= **{_DE_IC / -_DE_SL:.1f} h**",
        f"it predicts **{_mn(_DE_IC + _DE_SL * 48, 1)}**", f"k = **{_DE_K_FIT:.4f} h⁻¹**", f"the prediction at 48 h is {100 * math.exp(-0.04 * 48):.1f}", "h ≤ 1/k = **25 h**", "h < 2/k = 50 h", f"the exact answer is {_DE_N24 * math.exp(-0.04 * 48):.2f}",
        f"38.3 × (1 − 1.92) = **{_mn(_DE_N24 * (1 - 0.04 * 48), 1)}**", f"give **{_DE_N24 * (1 - 0.04 * 12) ** 4:.2f}**", f"3 h steps give {_DE_N24 * (1 - 0.04 * 3) ** 16:.2f}", f"0.75 h steps give {_DE_N24 * (1 - 0.04 * 0.75) ** 64:.2f}",
        f"predicts {_DE_HOLD_IC + _DE_HOLD_SL * 24:.2f} at 24 h, against an observed 38.3: an error of {_DE_N24 - (_DE_HOLD_IC + _DE_HOLD_SL * 24):.2f}, or {100 * (_DE_N24 - (_DE_HOLD_IC + _DE_HOLD_SL * 24)) / _DE_N24:.0f}% of the observed value",
    ])
    _fragments_in(text, [
        ", ".join(f"{v:.1f}" for v in b_data), f"slope is {_mn(sl_b, 3)} per hour with intercept {ic_b:.2f}", f"**{ic_b / -sl_b:.1f} h**", f"= **{_mn(ic_b + sl_b * 48, 1)}**, impossible", "= **20 h**",
        f"= **{_mn(b_data[-1] * (1 - 0.05 * 48), 1)}**, while the exact value is {b_data[-1] * math.exp(-0.05 * 48):.2f}", f"gives {hold_ic + hold_sl * 24:.1f} against an observed {b_data[-1]:.1f}",
    ])


def test_differential_equations_lab_text_and_keys_agree_with_the_dataset():
    assert len(_DE_ROWS) == 21 and {r["time"] for r in _DE_ROWS} == {f"t{t:02d}h" for t in (0, 6, 12, 18, 24, 36, 48)}
    assert {int(r["well"]) for r in _DE_ROWS} == {1, 2, 3}
    # the mean counts follow N = 100 (0.94 exp(-0.08 t) + 0.06) within 0.1, and each well is within 4.2% of its mean
    for t, mean_count in _DE_MEAN.items():
        assert abs(mean_count - 100.0 * (0.94 * math.exp(-0.08 * t) + 0.06)) < 0.1, t
    text = (COURSES / "differential-equations/labs/01-fitting-decay-models-and-testing-them-beyond-the-window.md").read_text(encoding="utf-8")
    ratio = _DE_MEAN[48] / _DE_LAB_EXP48
    _fragments_in(text, [
        "The means are " + ", ".join(f"{_DE_MEAN[t]:.1f}" for t in (0, 6, 12, 18, 24, 36, 48)), f"has slope −{_DE_LAB_K:.4f}, so k = {_DE_LAB_K:.4f} h⁻¹, and N₀ = {_DE_LAB_N0:.1f}",
        f"The straight line is {_DE_LAB_IC:.2f} + ({_mn(_DE_LAB_SL, 3)})t, which reaches zero at {_DE_LAB_IC / -_DE_LAB_SL:.1f} h and predicts {_mn(_DE_LAB_IC + _DE_LAB_SL * 48, 1)} at 48 h",
        f"{_DE_LAB_N0:.1f} × e^(−{_DE_LAB_K:.4f} × 48) = {_DE_LAB_EXP48:.2f}", f"while the observed mean is {_DE_MEAN[48]:.1f}, a ratio of {ratio:.2f}", "nothing here is evidence about any culture",
    ])
    field = bank("differential-equations")["differential-equations-lab1:beyond-the-window"]["solution_spec"]["field_specs"][0]
    assert abs(field["answer"] - ratio) <= field["tolerance"] and field["significant_figures"] == 3
    checks = {(c["row_id"], c["column"]): c["answer"] for c in bank("differential-equations")["differential-equations-lab1:time-summary"]["solution_spec"]["validation_spec"]["checks"]}
    assert len(checks) == 14
    for t in (0, 6, 12, 18, 24, 36, 48):
        assert checks[(f"t{t:02d}h", "wells")] == 3 and abs(checks[(f"t{t:02d}h", "mean_count")] - _DE_MEAN[t]) < 1e-3

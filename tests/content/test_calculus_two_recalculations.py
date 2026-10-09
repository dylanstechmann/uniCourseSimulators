"""Separate calculations for public practice keys, not human mathematical review.

Uses numerical quadrature, finite sums, transformed improper integrals and
committed observations. It does not import authoring scripts or their constants.
"""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/calculus-2"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


BANK = {q["id"]: q for q in load(COURSE / "question-banks/practice.json")["questions"]}


def integral(f, a, b, panels=1000):
    h = (b - a) / panels
    return (
        h
        / 3
        * math.fsum(
            (1 if i in (0, panels) else 4 if i % 2 else 2) * f(a + i * h)
            for i in range(panels + 1)
        )
    )


def interpolate(nodes, values, x):
    result = 0
    for j, value in enumerate(values):
        factor = 1
        for k, node in enumerate(nodes):
            if k != j:
                factor *= (x - node) / (nodes[j] - node)
        result += value * factor
    return result


def sampled_integral(nodes, values, degree):
    # Integrate the line/parabola interpolants instead of repeating rule weights.
    return math.fsum(
        integral(
            lambda x: interpolate(
                nodes[j : j + degree + 1], values[j : j + degree + 1], x
            ),
            nodes[j],
            nodes[j + degree],
            panels=20,
        )
        for j in range(0, len(nodes) - 1, degree)
    )


def first_certificate(bound, target, initial=0):
    for n in range(initial, 10000):
        if bound(n) <= target:
            return n
    raise AssertionError("No certificate in search range")


def lab_data():
    with (COURSE / "labs/force-samples.csv").open(
        encoding="utf-8", newline=""
    ) as stream:
        rows = list(csv.DictReader(stream))
    groups = {}
    for row in rows:
        groups.setdefault(row["position"], []).append(float(row["force_N"]))
    means = {key: math.fsum(values) / len(values) for key, values in groups.items()}
    nodes = [
        float(next(row["metres"] for row in rows if row["position"] == key))
        for key in groups
    ]
    corrected = [means[key] - 1 for key in groups]
    return rows, groups, means, nodes, corrected


def geometric_tail(final_index, ratio=0.4):
    return math.fsum(ratio**k for k in range(final_index + 1, final_index + 101))


def expected_answers():
    answers = {}

    def add(lesson, **values):
        answers.update(
            {
                f"calculus-2-{lesson}:{key.replace('_', '-')}": value
                for key, value in values.items()
            }
        )

    # Preserved keys checked without changing the authoring objects.
    add(1, check=integral(lambda t: 4 * math.exp(-2 * t), 0, 20))
    add(2, taylor_remainder=1.6487 * 0.5**3 / math.factorial(3))
    work = integral(lambda x: 4 * x, 0, 3)
    add(3, check=work, variable_force_work=work)
    add(
        4,
        check=math.fsum(0.2**k / math.factorial(k) for k in range(3)),
        alternating_series_error=1 / 25,
    )
    old_nodes = [0, 12, 24, 36, 48]
    old_rates = [0.5, 0.7167, 1.0272, 1.4723, 2.1103]
    add(
        5,
        exact_total=integral(lambda t: 0.5 * math.exp(0.03 * t), 0, 48),
        trapezoid=sampled_integral(old_nodes, old_rates, 1),
        simpson=sampled_integral(old_nodes, old_rates, 2),
        error_bound=48 * 12**2 / 12 * 0.5 * 0.03**2 * math.exp(1.44),
        improper_total=integral(lambda t: 2 * math.exp(-0.1 * t), 0, 300, panels=10000),
    )
    angle = math.radians(10)
    lost = -math.expm1(-0.05)
    add(
        6,
        p2_value=math.fsum((-0.2) ** k / math.factorial(k) for k in range(3)),
        remainder_bound=0.2**3 / math.factorial(3),
        decay_linear_error=100 * (0.05 - lost) / lost,
        small_angle=100 * (angle - math.sin(angle)) / math.sin(angle),
        tolerance_kt=math.sqrt(0.02),
    )

    add(
        7,
        substitution=integral(lambda t: 2 * t / (1 + t * t), 0, 2),
        parts_product=integral(lambda x: x * math.exp(x), 0, 1),
        parts_log=integral(math.log, 1, math.e),
        partial_fractions=integral(lambda x: 1 / ((x + 1) * (x + 2)), 0, 1),
        trig_substitution=integral(
            lambda t: math.sin(t) ** 3 * math.cos(t), 0, math.pi / 2
        ),
        arctangent=integral(lambda x: 1 / (1 + x * x), 0, 1),
    )
    # Substitutions remove improper endpoints: u=1/x, x=u²,
    # u=1/(1+t), and u=1/x for the arctangent tail.
    add(
        8,
        power_tail_total=integral(lambda u: 1, 0, 1),
        endpoint_root=integral(lambda u: 2, 0, 1),
        shifted_total=integral(lambda u: 6, 0, 1),
        shifted_tail=integral(lambda u: 6, 0, 0.25),
        cutoff_tail=integral(lambda u: 1, 0, 0.01),
        comparison_exact=integral(lambda u: 1 / (1 + u * u), 0, 1),
    )
    add(
        9,
        geometric_sum=math.fsum(0.4**k for k in range(100)),
        geometric_partial=math.fsum(0.4**k for k in range(4)),
        geometric_tail=geometric_tail(3),
        geometric_index=first_certificate(geometric_tail, 0.001),
        p_tail_bound=integral(lambda u: 1, 0, 0.01),
        telescoping=math.fsum(1 / (n * n + n) for n in range(1, 10)),
    )
    add(
        10,
        log_partial=math.fsum((-1) ** (n + 1) * 0.5**n / n for n in range(1, 5)),
        log_bound=0.5**5 / 5,
        log_term_count=first_certificate(
            lambda n: 0.5 ** (n + 1) / (n + 1), 0.0001, initial=1
        ),
        arctan_partial=math.fsum(
            (-1) ** n * 0.5 ** (2 * n + 1) / (2 * n + 1) for n in range(3)
        ),
        arctan_bound=0.5**7 / 7,
        endpoint_count=first_certificate(lambda n: 1 / (n + 1), 0.01, initial=1),
    )
    ratio_index = 10**10
    add(
        11,
        radius=3 * (ratio_index + 1) / ratio_index,
        interior_value=math.fsum((1 / 6) ** n / n for n in range(1, 100)),
        geometric_polynomial=math.fsum(0.25**n for n in range(3)),
        geometric_error=geometric_tail(2, 0.25),
        derivative_series=math.fsum(n * 0.5 ** (n - 1) for n in range(1, 100)),
        integrated_series=math.fsum(0.5 ** (n + 1) / (n + 1) for n in range(100)),
    )
    add(
        12,
        decay_cubic=math.fsum((-0.4) ** n / math.factorial(n) for n in range(4)),
        decay_bound=0.4**4 / math.factorial(4),
        growth_bound=max(math.exp(i / 2000) for i in range(1001))
        * 0.5**4
        / math.factorial(4),
        sine_polynomial=math.fsum(
            (-1) ** n * 0.6 ** (2 * n + 1) / math.factorial(2 * n + 1) for n in range(3)
        ),
        integrated_bound=integral(lambda x: x**4 / math.factorial(4), 0, 0.4),
        degree_choice=first_certificate(
            lambda n: 0.8 ** (n + 1) / math.factorial(n + 1), 0.0001
        ),
    )
    radial = integral(lambda r: 6 * (1 - r * r / 4) * 2 * math.pi * r, 0, 2)
    disk_area = integral(lambda r: 2 * math.pi * r, 0, 2)
    add(
        13,
        strip_area=integral(lambda x: x - x * x, 0, 1),
        disk_volume=integral(lambda x: math.pi * (x * x) ** 2, 0, 1),
        parametric_length=integral(lambda t: math.hypot(3, 4), 0, 2),
        polar_area=integral(lambda theta: 0.5 * 2**2, 0, math.pi / 2),
        radial_total=radial,
        radial_average=radial / disk_area,
    )
    _, _, _, nodes, force = lab_data()
    add(
        "lab-01",
        trapezoid=sampled_integral(nodes, force, 1),
        simpson=sampled_integral(nodes, force, 2),
        series_work=integral(
            lambda x: 10 * x * math.fsum((0.2 * x) ** n for n in range(4)), 0, 2
        ),
        tail_bound=integral(lambda x: 10 * x * (0.2 * x) ** 4 / 0.6, 0, 2),
    )
    return answers


EXPECTED = expected_answers()


@pytest.mark.parametrize("question_id", sorted(EXPECTED))
def test_all_numeric_keys_with_separate_calculations(question_id):
    spec = BANK[question_id]["solution_spec"]
    assert spec["answer"] == pytest.approx(
        EXPECTED[question_id], abs=max(spec["tolerance"], 1e-8), rel=2e-6
    )


def test_numeric_calculation_inventory_is_exhaustive():
    assert set(EXPECTED) == {key for key, q in BANK.items() if q["type"] == "numeric"}
    assert len(EXPECTED) == 62


CSV_CHECKS = BANK["calculus-2-lab-01:summary"]["solution_spec"]["validation_spec"][
    "checks"
]


@pytest.mark.parametrize("check", CSV_CHECKS, ids=lambda check: check["id"])
def test_upload_keys_recompute_committed_observations(check):
    _, groups, means, _, _ = lab_data()
    values = groups[check["row_id"]]
    expected = (
        len(values) if check["column"] == "replicates" else means[check["row_id"]]
    )
    assert check["answer"] == pytest.approx(expected, abs=check["tolerance"])
    assert check["calculation"]["values"] == values


def correct_option(key):
    question = BANK[key]
    return question["options"][question["solution_spec"]["answer"]]


def test_method_primitives_and_internal_singularity():
    for x in (0.1, 0.7, 1.4):
        h = 1e-5

        def primitive(u):
            return (u - 1) * math.exp(u)

        assert (primitive(x + h) - primitive(x - h)) / (2 * h) == pytest.approx(
            x * math.exp(x), rel=1e-8
        )
    assert correct_option("calculus-2-7:parts-sign") == "(x−1)eˣ+C."
    assert "internal singularity" in correct_option("calculus-2-7:pole")
    # One-sided log magnitudes grow instead of approaching finite limits.
    assert abs(math.log(1e-8)) > abs(math.log(1e-4))
    assert "ordinary improper integral diverges" in correct_option(
        "calculus-2-8:principal-value"
    )


def test_power_criteria_and_zero_term_limit():
    assert "p>1" in correct_option("calculus-2-8:endpoint-rule")
    assert "p<1" in correct_option("calculus-2-8:endpoint-rule")
    # Each dyadic harmonic block adds at least one half despite shrinking terms.
    for k in range(1, 9):
        assert math.fsum(1 / n for n in range(2 ** (k - 1) + 1, 2**k + 1)) >= 0.5
    assert "harmonic series diverges" in correct_option("calculus-2-9:zero-limit")
    assert "inconclusive" in correct_option("calculus-2-9:ratio-one")


def test_truncation_certificates_are_first_sufficient():
    cases = [
        (geometric_tail, 8, 0.001),
        (lambda n: 0.5 ** (n + 1) / (n + 1), 9, 0.0001),
        (lambda n: 1 / (n + 1), 99, 0.01),
        (lambda n: 0.8 ** (n + 1) / math.factorial(n + 1), 6, 0.0001),
    ]
    for bound, index, tolerance in cases:
        assert bound(index) <= tolerance < bound(index - 1)


def test_alternating_actual_errors_and_signs():
    log_error = math.log1p(0.5) - EXPECTED["calculus-2-10:log-partial"]
    assert 0 < log_error < EXPECTED["calculus-2-10:log-bound"]
    atan_error = math.atan(0.5) - EXPECTED["calculus-2-10:arctan-partial"]
    assert -EXPECTED["calculus-2-10:arctan-bound"] < atan_error < 0
    assert "Conditionally" in correct_option("calculus-2-10:conditional")
    assert "decreasing to zero" in correct_option("calculus-2-10:decrease")


def test_power_series_endpoints_and_operation_domains():
    assert correct_option("calculus-2-11:endpoints").startswith("[−1,5)")
    assert "Inside the radius" in correct_option("calculus-2-11:operation")
    assert "function is finite but this series diverges" in correct_option(
        "calculus-2-11:outside"
    )
    # At x=3 the geometric terms grow, despite the rational value being finite.
    assert (3 / 2) ** 20 > (3 / 2) ** 10
    assert 1 / (1 - 3 / 2) == -2
    # Differentiation changes the integrated logarithm's left endpoint behavior.
    assert abs((-1) ** 1000) == 1
    assert 1 / 1000 < 1 / 100


def test_taylor_bounds_include_actual_and_accumulated_errors():
    assert (
        abs(math.exp(-0.4) - EXPECTED["calculus-2-12:decay-cubic"])
        < EXPECTED["calculus-2-12:decay-bound"]
    )
    growth_cubic = math.fsum(0.5**n / math.factorial(n) for n in range(4))
    assert abs(math.exp(0.5) - growth_cubic) < EXPECTED["calculus-2-12:growth-bound"]
    polynomial_integral = integral(
        lambda x: math.fsum((-x) ** n / math.factorial(n) for n in range(4)), 0, 0.4
    )
    actual_integral = integral(lambda x: math.exp(-x), 0, 0.4)
    assert (
        0
        < actual_integral - polynomial_integral
        < EXPECTED["calculus-2-12:integrated-bound"]
    )
    assert "actual error might still be smaller" in correct_option(
        "calculus-2-12:certificate"
    )


def test_radial_case_and_parameter_multiplicity():
    # A different substitution s=r²/R² gives the same radial half factor.
    transformed = 6 * math.pi * 4 * integral(lambda s: 1 - s, 0, 1)
    assert transformed == pytest.approx(EXPECTED["calculus-2-13:radial-total"])
    assert 6 * math.pi * 4 == pytest.approx(2 * transformed)
    assert integral(lambda t: 2, 0, 4 * math.pi) == pytest.approx(8 * math.pi)
    assert "Two traversals" in correct_option("calculus-2-13:traversal")
    assert "Amount per length" in correct_option("calculus-2-13:density-units")
    assert integral(lambda t: t * 2 * t, 0, 1) == pytest.approx(2 / 3)


def test_lab_data_construction_offset_and_error_separation():
    rows, groups, means, nodes, corrected = lab_data()
    assert len(rows) == 15 and all(len(values) == 3 for values in groups.values())
    for row in rows:
        x = float(row["metres"])
        center = round(10 * x / (1 - 0.2 * x) + 1, 4)
        delta = (int(row["replicate"]) - 2) * 0.05
        assert float(row["force_N"]) == pytest.approx(center + delta, abs=1e-10)
        assert float(row["offset_N"]) == 1
    raw = [means[key] for key in groups]
    for degree in (1, 2):
        assert sampled_integral(nodes, raw, degree) - sampled_integral(
            nodes, corrected, degree
        ) == pytest.approx(2)
    exact = integral(lambda x: 10 * x / (1 - 0.2 * x), 0, 2)
    tail = integral(lambda x: 10 * x * (0.2 * x) ** 4 / (1 - 0.2 * x), 0, 2)
    assert exact - EXPECTED["calculus-2-lab-01:series-work"] == pytest.approx(tail)
    assert 0 < tail < EXPECTED["calculus-2-lab-01:tail-bound"]
    assert EXPECTED["calculus-2-lab-01:trapezoid"] > exact
    assert abs(EXPECTED["calculus-2-lab-01:simpson"] - exact) < 0.006


def test_schedule_and_partial_status():
    manifest = load(COURSE / "course.json")
    assert manifest["version"] == "0.4.0"
    assert (
        manifest["maturity"] == "partial"
        and manifest["review"]["status"] == "unreviewed"
    )
    assert manifest["grading_policy"]["mode"] == "formative-only"
    lessons = {
        lesson["id"] for module in manifest["modules"] for lesson in module["lessons"]
    }
    weeks = manifest["duration"]["weeks"]
    assert [week["week"] for week in weeks] == list(range(1, 15))
    assert {lesson for week in weeks for lesson in week["lesson_ids"]} == lessons
    assert weeks[-1]["assessment_ids"] == [
        "calculus-2-week14-force-lab",
        "calculus-2-case",
    ]
    assert len(lessons) == 14 and len(BANK) == 91
    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    assert "14 readings, 91 practice items and 48 retrieval cards" in syllabus
    assert "Weeks 1, 4, 7 and 10 retain compact prototype readings" in syllabus

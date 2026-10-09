"""Separate geometry/dynamics checks; same AI, not qualified human review."""

from __future__ import annotations

import csv
import json
import math
from fractions import Fraction
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/robotics"
BANK = {
    q["id"]: q
    for q in json.loads((COURSE / "question-banks/practice.json").read_text())[
        "questions"
    ]
}
MANIFEST = json.loads((COURSE / "course.json").read_text())


def position(q1, q2, l1=0.3, l2=0.2):
    return [
        l1 * math.cos(q1) + l2 * math.cos(q1 + q2),
        l1 * math.sin(q1) + l2 * math.sin(q1 + q2),
    ]


def jacobian(q1, q2):
    return [
        [-0.3 * math.sin(q1) - 0.2 * math.sin(q1 + q2), -0.2 * math.sin(q1 + q2)],
        [0.3 * math.cos(q1) + 0.2 * math.cos(q1 + q2), 0.2 * math.cos(q1 + q2)],
    ]


def product(matrix, vector):
    return [math.fsum(a * b for a, b in zip(row, vector)) for row in matrix]


def solve(matrix, rhs):
    a, b = matrix[0]
    c, d = matrix[1]
    det = a * d - b * c
    assert abs(det) > 1e-12
    return [(d * rhs[0] - b * rhs[1]) / det, (-c * rhs[0] + a * rhs[1]) / det]


def motion(angle, task):
    matrix = jacobian(0, math.radians(angle))
    desired = [-0.01, 0] if task == "inward" else [0, 0.01]
    rates = solve(matrix, desired)
    scale = min(1, 0.5 / max(map(abs, rates)))
    command = [scale * rate for rate in rates]
    return rates, scale, command, product(matrix, command)


def expected_answers():
    q1, q2 = math.radians(30), math.radians(45)
    x, y = position(q1, q2)
    elbow = math.acos((0.35**2 + 0.15**2 - 0.3**2 - 0.2**2) / (0.12))
    shoulder = math.atan2(0.15, 0.35) - math.atan2(
        0.2 * math.sin(elbow), 0.3 + 0.2 * math.cos(elbow)
    )
    result = {
        "robotics-1:check": math.sin(math.pi / 2),
        "robotics-2:check": 0.5 + 0.5,
        "robotics-3:check": 0.8 * 3,
        "robotics-1:end-effector-position": 1 + 0.5,
        "robotics-3:gear-ratio-torque": 0.1 * 20 * 0.8,
        "robotics-4:combined-sensor-uncertainty": math.hypot(3, 3),
        "robotics-5:forward-x": x,
        "robotics-5:forward-y": y,
        "robotics-5:elbow-angle": math.degrees(elbow),
        "robotics-5:shoulder-angle": math.degrees(shoulder),
        "robotics-5:tool-error": 0.4635 * math.pi / 180 * 1000,
        "robotics-6:output-torque": 0.05 * 50 * 0.8,
        "robotics-6:output-speed": 3000 / 50,
        "robotics-6:gravity-torque": 0.2 * 9.81 * 0.3,
        "robotics-6:margin": 2 / 0.589,
        "robotics-6:tool-resolution": 0.3 * 2 * math.pi / (1024 * 50) * 1000,
    }
    values = {
        7: {
            "base-x": 0.3 - 0.02,
            "base-y": 0.1 + 0.04,
            "inverse-x": 0.14 - 0.1,
            "orientation-mm": 0.1 * 0.002 * 1000,
            "standard-mm": math.sqrt(0.3**2 + 0.2**2),
            "bounded-mm": 0.3 + 0.2,
        },
        8: {
            "determinant": 0.3 * 0.2,
            "elbow-rate": 0.01 / 0.2,
            "force-torque-1": -0.2 * 5,
            "force-torque-2": -0.2 * 5,
            "power": 5 * (-0.06) + 2 * 0.03,
            "damped-rate": 0.01 * 0.1 / (0.01**2 + 0.05**2),
        },
        9: {
            "elbow-cosine": (0.25**2 + 0.25**2 - 2 * 0.25**2) / (2 * 0.25**2),
            "positive-elbow": math.degrees(math.acos(0)),
            "allowed-branches": 1,
            "outer-reach": 2 * 0.25,
            "clearance": 0.1 - 0.05,
            "joint-midpoint-x": 0.5 * math.cos(math.pi / 4),
        },
        10: {
            "kinetic-energy": (0.155 + 2 * 0.02 * 1 * 2 + 0.02 * 2**2) / 2,
            "matrix-determinant": 0.155 * 0.02 - 0.02**2,
            "gravity-shoulder": 1.5 * 9.81 * 0.3,
            "accelerating-shoulder": 1.5 * 9.81 * 0.3 + 0.155,
            "potential-rise": 0.5 * 9.81 * 0.2,
            "straight-mass-determinant": 0.215 * 0.02 - 0.05**2,
        },
        11: {
            "voltage-current": (12 - 0.1 * 100) / 2,
            "motor-torque": 0.1 * 1,
            "low-speed-output": 0.8 * 50 * 0.1 * 2,
            "reflected-inertia": 0.0001 * 50**2,
            "pd-frequency": math.sqrt(2 / 0.02),
            "pd-damping": (0.01 + 0.39) / (2 * math.sqrt(0.02 * 2)),
        },
        12: {
            "cubic-midpoint": 0.4 * (3 * 0.5**2 - 2 * 0.5**3),
            "cubic-peak-speed": 1.5 * 0.4 / 2,
            "cubic-peak-acceleration": 6 * 0.4 / 2**2,
            "duration-speed": float(Fraction(3, 2) * Fraction(2, 5) / Fraction(1, 5)),
            "stop-allowance": 0.2 * 0.05 + 0.2**2 / (2 * 1) + 0.003,
            "clearance-reserve": 0.04 - (0.2 * 0.05 + 0.2**2 / 2 + 0.003),
        },
        13: {
            "following-error": 0.2 - 0.12,
            "jump-speed": 0.1 / 0.01,
            "bounded-change": 2 * 0.01,
            "transmission-gap": 0.01 * 0.3 * 1000,
            "combined-mm": math.sqrt(0.5**2 + 0.8**2),
            "fiducial-bias": sum([2, 2]) / 2,
        },
    }
    result.update(
        {
            f"robotics-{n}:{key}": value
            for n, items in values.items()
            for key, value in items.items()
        }
    )
    rates, scale, _, velocity = motion(2, "inward")
    result.update(
        {
            "robotics-lab-01:in02-demand": rates[1],
            "robotics-lab-01:uniform-scale": scale,
            "robotics-lab-01:achieved-inward": -velocity[0] * 1000,
            "robotics-lab-01:straight-radial-torque": 0,
        }
    )
    return result


EXPECTED = expected_answers()


def test_every_numeric_item_has_separate_calculation():
    assert set(EXPECTED) == {key for key, q in BANK.items() if q["type"] == "numeric"}
    assert len(EXPECTED) == 62


@pytest.mark.parametrize("key", sorted(EXPECTED))
def test_numeric_keys_against_declared_tolerances(key):
    spec = BANK[key]["solution_spec"]
    allowed = max(
        spec["tolerance"], spec.get("relative_tolerance", 0) * abs(EXPECTED[key])
    )
    assert abs(spec["answer"] - EXPECTED[key]) <= allowed


def test_frame_roundtrip_composition_direction_and_uncertainty():
    def rotate(point):
        return [-point[1], point[0]]

    for point in [[0.04, 0.02], [0, 0], [-0.1, 0.3]]:
        rotated = rotate(point)
        base = [rotated[0] + 0.3, rotated[1] + 0.1]
        shifted = [base[0] - 0.3, base[1] - 0.1]
        recovered = [shifted[1], -shifted[0]]
        assert recovered == pytest.approx(point)
    before = rotate([1 + 0.3, 0 + 0.1])
    after = [rotate([1, 0])[0] + 0.3, rotate([1, 0])[1] + 0.1]
    assert before != after
    angle = 0.002
    chord = 2 * 0.1 * math.sin(angle / 2) * 1000
    assert chord == pytest.approx(0.2, rel=1e-6)
    assert math.hypot(0.3, 0.2) < 0.3 + 0.2


@pytest.mark.parametrize(
    "q1,q2", [(0, math.pi / 2), (0.4, 0.3), (-0.2, math.radians(2))]
)
def test_jacobian_finite_differences_determinant_and_power(q1, q2):
    matrix = jacobian(q1, q2)
    step = 1e-6
    for axis in range(2):
        plus = [q1, q2]
        minus = [q1, q2]
        plus[axis] += step
        minus[axis] -= step
        derivative = [
            (a - b) / (2 * step) for a, b in zip(position(*plus), position(*minus))
        ]
        assert derivative == pytest.approx([row[axis] for row in matrix], abs=1e-10)
    assert matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0] == pytest.approx(
        0.06 * math.sin(q2)
    )
    rates, force = [0.1, 0.2], [5, 2]
    velocity = product(matrix, rates)
    torque = product(list(zip(*matrix)), force)
    assert sum(a * b for a, b in zip(velocity, force)) == pytest.approx(
        sum(a * b for a, b in zip(torque, rates))
    )


def test_singular_direction_force_map_and_damped_residual():
    matrix = jacobian(0, 0)
    assert matrix == [[0, 0], [0.5, 0.2]]
    assert product(matrix, [1, -2.5]) == pytest.approx([0, 0])
    assert product(list(zip(*matrix)), [5, 0]) == [0, 0]
    with pytest.raises(AssertionError):
        solve(matrix, [-0.01, 0])
    rate = 0.01 * 0.1 / (0.01**2 + 0.05**2)
    assert 0.01 * rate < 0.1
    assert rate < 10


def test_inverse_branches_limits_and_distinct_joint_path_midpoint():
    candidates = []
    for elbow in [math.pi / 2, -math.pi / 2]:
        shoulder = math.pi / 4 - math.atan2(
            0.25 * math.sin(elbow), 0.25 + 0.25 * math.cos(elbow)
        )
        assert position(shoulder, elbow, 0.25, 0.25) == pytest.approx([0.25, 0.25])
        candidates.append((math.degrees(shoulder), math.degrees(elbow)))
    assert sum(-30 <= a <= 60 and -120 <= b <= 120 for a, b in candidates) == 1
    midpoint = position(math.pi / 4, 0, 0.25, 0.25)
    assert midpoint == pytest.approx([0.5 / math.sqrt(2)] * 2)
    assert midpoint != [0.25, 0.25]
    assert (0.6**2 - 0.25**2 - 0.25**2) / (2 * 0.25**2) > 1


def clearance(start, end, center, radius):
    vector = [b - a for a, b in zip(start, end)]
    norm = sum(v * v for v in vector)
    fraction = (
        0
        if norm == 0
        else max(
            0, min(1, sum((c - a) * v for c, a, v in zip(center, start, vector)) / norm)
        )
    )
    nearest = [a + fraction * v for a, v in zip(start, vector)]
    return math.hypot(*(c - p for c, p in zip(center, nearest))) - radius


@pytest.mark.parametrize(
    "end,center,answer",
    [([1, 0], [0.5, 0.1], 0.05), ([1, 0], [2, 0], 0.95), ([0, 0], [0, 0.1], 0.05)],
)
def test_segment_projection_endpoint_and_degenerate_clearance(end, center, answer):
    assert clearance([0, 0], end, center, 0.05) == pytest.approx(answer)


def mass(q1, q2):
    matrix = jacobian(q1, q2)
    a = 0.09 + 0.5 * sum(row[0] ** 2 for row in matrix)
    b = 0.5 * sum(row[0] * row[1] for row in matrix)
    d = 0.5 * sum(row[1] ** 2 for row in matrix)
    return [[a, b], [b, d]]


def energy(q, rates):
    tool_velocity = product(jacobian(*q), rates)
    kinetic = 0.5 * (0.3 * rates[0]) ** 2 + 0.5 * 0.5 * sum(
        v * v for v in tool_velocity
    )
    potential = 1.5 * 9.81 * 0.3 * math.sin(q[0]) + 0.5 * 9.81 * 0.2 * math.sin(sum(q))
    return kinetic + potential


@pytest.mark.parametrize("q", [[0, 0], [0, math.pi / 2], [0.3, 0.4]])
def test_point_mass_inertia_positive_and_nonzero_rate_energy_balance(q):
    matrix = mass(*q)
    assert matrix[0][0] > 0 and matrix[0][0] * matrix[1][1] - matrix[0][1] ** 2 > 0
    rates, acc = [0.7, -0.4], [0.2, 0.3]
    h = [
        -0.5 * 0.3 * 0.2 * math.sin(q[1]) * (2 * rates[0] * rates[1] + rates[1] ** 2),
        0.5 * 0.3 * 0.2 * math.sin(q[1]) * rates[0] ** 2,
    ]
    gravity = [
        1.5 * 9.81 * 0.3 * math.cos(q[0]) + 0.5 * 9.81 * 0.2 * math.cos(sum(q)),
        0.5 * 9.81 * 0.2 * math.cos(sum(q)),
    ]
    torque = [a + b + c for a, b, c in zip(product(matrix, acc), h, gravity)]
    dt = 1e-6
    plus_q = [a + dt * b for a, b in zip(q, rates)]
    minus_q = [a - dt * b for a, b in zip(q, rates)]
    plus_rate = [a + dt * b for a, b in zip(rates, acc)]
    minus_rate = [a - dt * b for a, b in zip(rates, acc)]
    derivative = (energy(plus_q, plus_rate) - energy(minus_q, minus_rate)) / (2 * dt)
    assert derivative == pytest.approx(
        sum(a * b for a, b in zip(torque, rates)), abs=1e-8
    )


def test_motor_same_point_power_envelope_and_pd_parameters():
    for speed, current in [(20, 2), (100, 1)]:
        voltage = 2 * current + 0.1 * speed
        assert voltage <= 12
        torque = 0.1 * current
        assert (0.8 * 50 * torque) * (speed / 50) == pytest.approx(0.8 * torque * speed)
    assert 8 * 2 > 0.8 * (0.1 * 1) * 100
    assert 2 * 0.5 > 0.3
    assert math.sqrt(2 / 0.02) == 10 and (0.01 + 0.39) / (2 * math.sqrt(0.02 * 2)) == 1


def test_cubic_extrema_bounds_quintic_endpoints_and_stopping_allowance():
    velocities = [
        0.4 / 2 * (6 * s - 6 * s * s) for s in [i / 2000 for i in range(2001)]
    ]
    assert max(velocities) == pytest.approx(0.3)
    assert 6 * 0.4 / 2**2 == pytest.approx(0.6)
    displacement, speed_limit = Fraction(2, 5), Fraction(1, 5)
    duration = max(Fraction(3, 2) * displacement / speed_limit, math.sqrt(6))
    assert duration == 3
    assert Fraction(3, 2) * displacement / duration <= speed_limit
    assert 6 * displacement / duration**2 <= Fraction(2, 5)
    for s in [0, 1]:
        assert 30 * s * s - 60 * s**3 + 30 * s**4 == 0
        assert 60 * s - 180 * s * s + 120 * s**3 == 0
    assert 0.2 * 0.05 + 0.2**2 / 2 + 0.003 == pytest.approx(0.033)
    assert clearance([0, 0], [1, 0], [0.5, 0], 0.01) < 0
    assert (
        math.hypot(0.5, 0) - 0.01 > 0
    )  # Safe endpoints do not rule out an interior overlap.


def reports():
    with (COURSE / "labs/near-extension-reports.csv").open(newline="") as stream:
        return list(csv.DictReader(stream))


CHECKS = BANK["robotics-lab-01:summary"]["solution_spec"]["validation_spec"]["checks"]


@pytest.mark.parametrize("check", CHECKS, ids=lambda c: c["id"])
def test_csv_cells_recalculated_from_reported_components(check):
    selected = [r for r in reports() if r["sample"] == check["row_id"]]
    value = (
        len(selected)
        if check["column"] == "reports"
        else math.fsum(
            float(
                r[
                    "reported_vx_mm_s"
                    if check["column"] == "mean_vx_mm_s"
                    else "reported_vy_mm_s"
                ]
            )
            for r in selected
        )
        / len(selected)
    )
    assert abs(check["answer"] - value) <= check["tolerance"]


@pytest.mark.parametrize("task", ["inward", "tangent"])
def test_lab_commands_and_report_variants_have_declared_origin(task):
    rows = reports()
    assert len(rows) == 24 and len(CHECKS) == 24
    for row in rows:
        if row["task"] != task:
            continue
        _, scale, command, velocity = motion(float(row["q2_deg"]), task)
        assert float(row["command_q1_rad_s"]) == pytest.approx(command[0], abs=5.1e-10)
        assert float(row["command_q2_rad_s"]) == pytest.approx(command[1], abs=5.1e-10)
        assert max(map(abs, command)) <= 0.5 + 1e-15
        index = int(row["replicate"]) - 2
        assert float(row["reported_vx_mm_s"]) == pytest.approx(
            1000 * velocity[0] + index * 0.02, abs=5.1e-7
        )
        assert float(row["reported_vy_mm_s"]) == pytest.approx(
            1000 * velocity[1] - index * 0.01, abs=5.1e-7
        )
        if task == "tangent":
            assert scale == 1 and command == pytest.approx([1 / 30, -1 / 30])


def test_uniform_limiter_preserves_direction_while_independent_clipping_changes_it():
    rates, scale, command, velocity = motion(2, "inward")
    assert scale < 1 and command[1] == pytest.approx(0.5)
    assert velocity == pytest.approx([-0.01 * scale, 0], abs=1e-16)
    clipped = [max(-0.5, min(0.5, r)) for r in rates]
    assert product(jacobian(0, math.radians(2)), clipped) == pytest.approx([0, -0.15])


def test_sensing_bound_and_case_qualifications_are_explicit():
    assert 0.1 / 0.01 > 2 and 0.1 > 2 * 0.01
    assert 0.01 * 0.3 * 1000 == 3
    assert math.hypot(0.5, 0.8) < 0.5 + 0.8
    lesson = next(
        lesson
        for module in MANIFEST["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "robotics-13"
    )
    text = (COURSE / lesson["reading"]).read_text()
    assert "finite endpoint force mapping alone does not universally diverge" in text
    assert "lacks continuous redundancy" in text


def test_schedule_once_formative_labels_and_all_package_schedules():
    weeks = MANIFEST["duration"]["weeks"]
    assert [w["week"] for w in weeks] == list(range(1, 15))
    lessons = [
        lesson["id"] for module in MANIFEST["modules"] for lesson in module["lessons"]
    ]
    assert sorted(item for week in weeks for item in week["lesson_ids"]) == sorted(
        lessons
    )
    assessment_ids = {a["id"] for a in MANIFEST["assessments"]}
    assert all(a in assessment_ids for week in weeks for a in week["assessment_ids"])
    assert (
        MANIFEST["maturity"] == "partial"
        and MANIFEST["review"]["status"] == "unreviewed"
    )
    assert MANIFEST["grading_policy"]["mode"] == "formative-only"
    assert all(a["mode"] != "graded" for a in MANIFEST["assessments"])
    courses = [
        json.loads(p.read_text())
        for p in (ROOT / "content/courses").glob("*/course.json")
    ]
    assert len(courses) == 25 and all(c["duration"]["weeks"] for c in courses)

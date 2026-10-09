"""Separate model calculations; same-AI checks, not qualified human review.

No authoring imports. Recompute numeric and CSV keys from committed data,
and cross-check force, energy, angular and constitutive balances.
"""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/physics-mechanics"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


BANK = {q["id"]: q for q in load(COURSE / "question-banks/practice.json")["questions"]}


def bisect(function, low, high):
    sign = function(low)
    assert sign * function(high) <= 0
    for _ in range(90):
        middle = (low + high) / 2
        value = function(middle)
        if sign * value <= 0:
            high = middle
        else:
            low, sign = middle, value
    return (low + high) / 2


def integrate(function, initial, duration, steps=2000):
    state = list(initial)
    dt = duration / steps
    for _ in range(steps):
        a = function(state)
        b = function([v + dt * k / 2 for v, k in zip(state, a)])
        c = function([v + dt * k / 2 for v, k in zip(state, b)])
        d = function([v + dt * k for v, k in zip(state, c)])
        state = [
            v + dt * (ka + 2 * kb + 2 * kc + kd) / 6
            for v, ka, kb, kc, kd in zip(state, a, b, c, d)
        ]
    return state


def trapezoid(function, lower, upper, steps=2000):
    dt = (upper - lower) / steps
    return dt * (
        (function(lower) + function(upper)) / 2
        + math.fsum(function(lower + i * dt) for i in range(1, steps))
    )


def lab_data():
    with (COURSE / "labs/compliance-reports.csv").open(
        encoding="utf-8", newline=""
    ) as stream:
        rows = list(csv.DictReader(stream))
    groups = {}
    for row in rows:
        groups.setdefault(row["sample"], []).append(
            float(row["reported_displacement_mm"])
        )
    means = {key: math.fsum(values) / len(values) for key, values in groups.items()}
    return rows, groups, means


def regression(force, displacement):
    """Unweighted OLS with an intercept, rather than endpoint division."""
    x_bar = math.fsum(force) / len(force)
    y_bar = math.fsum(displacement) / len(displacement)
    slope = math.fsum(
        (x - x_bar) * (y - y_bar) for x, y in zip(force, displacement)
    ) / math.fsum((x - x_bar) ** 2 for x in force)
    return y_bar - slope * x_bar, slope


def lab_fit(kind):
    rows, _, _ = lab_data()
    selected = [row for row in rows if row["orientation"] == kind]
    return regression(
        [float(row["force_n"]) for row in selected],
        [float(row["reported_displacement_mm"]) for row in selected],
    )


def expected_answers():
    answers = {}

    def add(lesson, **values):
        answers.update(
            {
                f"physics-mechanics-{lesson}:{key.replace('_', '-')}": value
                for key, value in values.items()
            }
        )

    g = 9.81
    add(1, check=12 / 3, incline_acceleration=g * math.sin(math.pi / 6))
    add(2, check=2 * 3**2 / 2, dissipated_energy=2 * g * 5 - 2 * 8**2 / 2)
    add(
        3,
        check=(0.1 * 5) / (0.1 + 0.4),
        impulse_area=trapezoid(lambda t: 10000 * t, 0, 0.02),
    )
    add(4, check=30 * 0.2, strain_from_stress=5_000_000 / 2_000_000_000)
    add(
        5,
        impact_speed=bisect(lambda v: 70 * v * v / 2 - 70 * g * 0.5, 0, 5),
        impulse_force=70 * 3.13 / 0.01,
        padded_force=219.2 / 0.05,
        work_energy_force=343.4 / 0.02,
    )
    omega = 3000 * 2 * math.pi / 60
    add(
        6,
        rcf=0.1 * omega**2 / g,
        rpm_target=bisect(
            lambda rpm: 0.1 * (rpm * 2 * math.pi / 60) ** 2 / g - 500, 0, 4000
        ),
        kinetic_energy=(2 * 0.12**2 / 2) * omega**2 / 2,
        spin_up_torque=0.0144 * 314.2 / 20,
        imbalance_force=0.001 * 0.1 * omega**2,
    )
    landing = bisect(lambda t: 1 + 3 * t - g * t * t / 2, 0, 2)
    add(
        7,
        x_position=1 + 2 * 2 + 2**2,
        y_position=3 - 2 + 2**2 / 2,
        speed=math.hypot(6, 1),
        x_acceleration=2,
        landing_time=landing,
        range=2 * landing,
    )
    normal = 2 * g
    add(
        8,
        normal=normal,
        static_friction=6,
        static_limit=0.4 * normal,
        kinetic_friction=0.2 * normal,
        sliding_acceleration=(8 - 0.2 * normal) / 2,
        incline_acceleration=(
            2 * g * math.sin(math.pi / 6) - 0.2 * 2 * g * math.cos(math.pi / 6)
        )
        / 2,
    )
    velocity = (0.2 * 3 + 0.3 * (-1)) / 0.5
    work = trapezoid(lambda x: 4 + 2 * x, 0, 3)
    add(
        9,
        collision_velocity=velocity,
        collision_energy_loss=(0.2 * 3**2 + 0.3 * (-1) ** 2) / 2
        - 0.5 * velocity**2 / 2,
        net_average_force=2 * (0 - (-5)) / 0.1,
        contact_average_force=(2 * (0 - (-5)) + 2 * g * 0.1) / 0.1,
        variable_force_work=work,
        work_speed=bisect(lambda v: 2 * v * v / 2 - work, 0, 10),
    )
    inertia = 2 * 0.1**2 / 2
    add(
        10,
        torque=0.2 * 30 - 0.1 * 10,
        disk_inertia=inertia,
        angular_acceleration=5 / inertia,
        rotational_energy=inertia * 20**2 / 2,
        angular_momentum=inertia * 20,
        rolling_speed=bisect(
            lambda v: 2 * v * v / 2
            + (2 * 0.1**2 / 2) * (v / 0.1) ** 2 / 2
            - 2 * g * 0.5,
            0,
            5,
        ),
    )
    damped = bisect(lambda w: 0.5 * (w * w + (0.8 / (2 * 0.5)) ** 2) - 50, 0, 20)
    add(
        11,
        natural_frequency=bisect(lambda w: 0.5 * w * w - 50, 0, 20),
        damped_frequency=damped,
        damped_period=2 * math.pi / damped,
        critical_damping=bisect(lambda c: c * c - 4 * 0.5 * 50, 0, 20),
        initial_energy=50 * 0.02**2 / 2,
        envelope_half=bisect(lambda t: math.exp(-0.8 * t) - 0.5, 0, 2),
    )
    add(
        12,
        stress=10 / 0.000002 / 1_000_000,
        strain=0.00020 / 0.020,
        secant_modulus=(10 / 0.000002) / (0.00020 / 0.020) / 1_000_000,
        spring_dashpot_stress=100_000 * 0.02 + 50_000 * 0.01,
        creep_time=50_000 / 100_000,
        creep_limit=3000 / 100_000,
    )
    add(
        13,
        reported_displacement=(0.002 + 0.001 * 0.3 + 0.3 / 1000) * 1000,
        apparent_stiffness=1 / (0.001 + 1 / 1000),
        machine_compliance=0.001 * 1000,
        gauge_extension=(0.0026 - 0.002 - 0.001 * 0.3) * 1000,
        corrected_modulus=1000 * 0.02 / 0.000001 / 1_000_000,
        apparent_modulus=500 * 0.02 / 0.000001 / 1_000_000,
    )
    intercept, machine = lab_fit("ref")
    add(
        "lab-01",
        offset=intercept,
        machine_compliance=machine,
        a_stiffness=1000 / (lab_fit("a")[1] - machine),
        b_stiffness=1000 / (lab_fit("b")[1] - machine),
    )
    return answers


EXPECTED = expected_answers()


@pytest.mark.parametrize("item_id,expected", EXPECTED.items(), ids=list(EXPECTED))
def test_numeric_key_matches_separate_calculation(item_id, expected):
    spec = BANK[item_id]["solution_spec"]
    assert abs(spec["answer"] - expected) <= spec["tolerance"] + 1e-10


def test_all_numeric_keys_are_recalculated():
    numeric = {q["id"] for q in BANK.values() if q["type"] == "numeric"}
    assert set(EXPECTED) == numeric and len(numeric) == 63


CHECKS = BANK["physics-mechanics-lab-01:summary"]["solution_spec"]["validation_spec"][
    "checks"
]


@pytest.mark.parametrize("check", CHECKS, ids=[check["id"] for check in CHECKS])
def test_csv_checks_recompute_from_committed_reports(check):
    _, groups, means = lab_data()
    value = (
        len(groups[check["row_id"]])
        if check["column"] == "replicates"
        else means[check["row_id"]]
    )
    assert check["answer"] == pytest.approx(value, abs=check["tolerance"])


def test_position_derivatives_average_and_constant_velocity_frame():
    def position(t):
        return (1 + 2 * t + t * t, 3 - t + t * t / 2)

    dt = 0.001
    center, before, after = position(2), position(2 - dt), position(2 + dt)
    velocity = [(a - b) / (2 * dt) for a, b in zip(after, before)]
    acceleration = [(a - 2 * c + b) / dt**2 for a, c, b in zip(after, center, before)]
    assert velocity == pytest.approx([6, 1])
    assert acceleration == pytest.approx([2, 1], abs=1e-8)
    assert [(a - b) / 2 for a, b in zip(position(2), position(0))] == [4, 0]
    transformed = [position(t)[0] - t for t in (2 - dt, 2, 2 + dt)]
    assert (transformed[2] - transformed[0]) / (2 * dt) == pytest.approx(5)
    assert (
        transformed[2] - 2 * transformed[1] + transformed[0]
    ) / dt**2 == pytest.approx(2)


def test_projectile_event_apex_and_energy_conservation():
    t = EXPECTED["physics-mechanics-7:landing-time"]
    assert t > 3 / 9.81 > 0
    assert 1 + 3 * t - 9.81 * t * t / 2 == pytest.approx(0, abs=1e-12)
    initial = (2**2 + 3**2) / 2 + 9.81
    final = (2**2 + (3 - 9.81 * t) ** 2) / 2
    assert final == pytest.approx(initial)
    assert math.hypot(2, 0) > 0  # Vertical velocity zero is not zero speed.


def test_static_friction_feasibility_contact_and_net_force():
    normal = 2 * 9.81
    assert 6 < 0.4 * normal < 8
    assert normal * math.sin(math.pi / 6) > 0.4 * normal * math.cos(math.pi / 6)
    assert 21.62 - 2 * 9.81 == pytest.approx(2 * 1)
    # A pulling contact cannot replace a lost unilateral normal force.
    required_normal = 2 * 9.81 - 25
    assert required_normal < 0


def test_collision_and_contact_impulse_ledgers():
    final = EXPECTED["physics-mechanics-9:collision-velocity"]
    assert 0.5 * final == pytest.approx(0.2 * 3 - 0.3)
    assert 0.5 * final**2 / 2 < (0.2 * 3**2 + 0.3) / 2
    contact = EXPECTED["physics-mechanics-9:contact-average-force"]
    assert contact * 0.1 - 2 * 9.81 * 0.1 == pytest.approx(2 * 5)
    assert contact > EXPECTED["physics-mechanics-9:net-average-force"]


def test_torque_cross_product_inertia_quadrature_and_rolling_balance():
    radius, mass = 0.1, 2
    density = mass / (math.pi * radius**2)
    integrated_inertia = trapezoid(
        lambda r: r * r * density * 2 * math.pi * r, 0, radius
    )
    assert integrated_inertia == pytest.approx(
        EXPECTED["physics-mechanics-10:disk-inertia"], rel=1e-6
    )
    assert 0.2 * 30 - 0.1 * 10 == EXPECTED["physics-mechanics-10:torque"]
    speed = EXPECTED["physics-mechanics-10:rolling-speed"]
    rotation = integrated_inertia * (speed / radius) ** 2 / 2
    translation = mass * speed**2 / 2
    assert rotation + translation == pytest.approx(mass * 9.81 * 0.5, rel=1e-6)
    assert rotation / (rotation + translation) == pytest.approx(1 / 3, rel=1e-6)
    # At 30 degrees solid-cylinder rolling needs μ_s≥tan(theta)/3.
    required = math.tan(math.pi / 6) / 3
    assert 0.1 < required < 0.2


@pytest.mark.parametrize("duration", [0.1, 0.5, 1.0])
def test_oscillator_component_ode_initial_conditions_and_dissipation(duration):
    mass, stiffness, damping, initial = 0.5, 50, 0.8, 0.02

    def derivative(state):
        x, v, _ = state
        return [v, (-stiffness * x - damping * v) / mass, damping * v * v]

    x, v, loss = integrate(derivative, [initial, 0, 0], duration)
    delta = damping / (2 * mass)
    omega = EXPECTED["physics-mechanics-11:damped-frequency"]
    analytic = (
        initial
        * math.exp(-delta * duration)
        * (math.cos(omega * duration) + delta / omega * math.sin(omega * duration))
    )
    assert x == pytest.approx(analytic, abs=1e-11)
    energy = mass * v * v / 2 + stiffness * x * x / 2
    assert energy + loss == pytest.approx(stiffness * initial**2 / 2, abs=1e-11)
    assert loss > 0
    pure_envelope_energy = stiffness * initial**2 / 2 * math.exp(-2 * delta * duration)
    assert abs(energy - pure_envelope_energy) > 1e-5


def test_parallel_constitutive_creep_ode_and_slope_definition():
    strain = integrate(lambda state: [(3000 - 100000 * state[0]) / 50000], [0], 0.5)[0]
    assert strain == pytest.approx(0.03 * (1 - math.exp(-1)), abs=1e-12)
    assert 0 < strain < EXPECTED["physics-mechanics-12:creep-limit"]
    stress_elastic, stress_viscous = 100000 * 0.02, 50000 * 0.01
    assert (
        stress_elastic + stress_viscous
        == EXPECTED["physics-mechanics-12:spring-dashpot-stress"]
    )
    # Nonlinear σ=Eε+qε² separates secant from tangent modulus.
    secant = 100000 + 200000 * 0.02
    tangent = 100000 + 2 * 200000 * 0.02
    assert tangent > secant


@pytest.mark.parametrize(
    "kind,slope,stiffness", [("a", 1, 2000), ("b", 1.5, 1000), ("ref", 0.5, None)]
)
def test_lab_regression_balanced_reports_and_series_reconstruction(
    kind, slope, stiffness
):
    rows, groups, means = lab_data()
    assert len(rows) == 27 and len(groups) == 9 and len(CHECKS) == 18
    intercept, fitted = lab_fit(kind)
    assert intercept == pytest.approx(1)
    assert fitted == pytest.approx(slope)
    for row in rows:
        if row["orientation"] != kind:
            continue
        key = row["sample"]
        assert len(groups[key]) == 3
        assert means[key] == pytest.approx(1 + slope * float(row["force_n"]))
        offsets = [value - means[key] for value in groups[key]]
        assert offsets == pytest.approx([-0.01, 0, 0.01])
    if stiffness:
        corrected = 1000 / (fitted - lab_fit("ref")[1])
        assert corrected == pytest.approx(stiffness)
        strain = 0.4 / corrected / 0.020
        assert strain <= 0.020 + 1e-12
        assert corrected * 0.020 / 0.000001 / 1e6 == pytest.approx(
            40 if kind == "a" else 20
        )


def test_series_bias_finite_reference_and_passive_limiting_cases():
    machine = lab_fit("ref")[1]
    ca, cb = lab_fit("a")[1], lab_fit("b")[1]
    assert cb / ca == pytest.approx(1.5)
    assert (cb - machine) / (ca - machine) == pytest.approx(2)
    # A finite reference slope contains reference and machine contributions.
    ref_compliance = 0.2
    observed = machine + ref_compliance
    assert observed - ref_compliance == pytest.approx(machine)
    assert 1 / (1 / 2000 + 0) == 2000
    assert 1 / (1 / 1e15 + 0.0005) == pytest.approx(1 / 0.0005)
    assert 0.4 - machine < 0  # Incompatible total compliance cannot yield passive k>0.

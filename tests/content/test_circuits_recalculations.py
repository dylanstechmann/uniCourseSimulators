"""Separate circuit/model calculations; same-AI checks, not human review.

No authoring imports. Recalculate numeric/CSV keys and cross-check nodal,
feedback, filter-energy, covariance, quantizer and calibration domains.
"""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/circuits"


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


def quadrature(function, low, high, steps=2000):
    dt = (high - low) / steps
    return dt * (
        (function(low) + function(high)) / 2
        + math.fsum(function(low + i * dt) for i in range(1, steps))
    )


def nodal(external_conductance=0):
    aa, ab, ba, bb = 0.0025, -0.001, -0.001, 0.002 + external_conductance
    rhs = 0.006
    determinant = aa * bb - ab * ba
    return rhs * bb / determinant, -ba * rhs / determinant


def lab_data():
    with (COURSE / "labs/channel-reports.csv").open(
        encoding="utf-8", newline=""
    ) as stream:
        rows = list(csv.DictReader(stream))
    groups = {}
    for row in rows:
        groups.setdefault(row["sample"], []).append(float(row["reported_output_v"]))
    means = {key: math.fsum(values) / len(values) for key, values in groups.items()}
    return rows, groups, means


def fit(x, y):
    mx, my = math.fsum(x) / len(x), math.fsum(y) / len(y)
    slope = math.fsum((a - mx) * (b - my) for a, b in zip(x, y)) / math.fsum(
        (a - mx) ** 2 for a in x
    )
    return my - slope * mx, slope


def expected_answers():
    result = {}

    def add(lesson, **values):
        result.update(
            {
                f"circuits-{lesson}:{key.replace('_', '-')}": value
                for key, value in values.items()
            }
        )

    add(1, check=12 / 6000 * 1000, thevenin_resistance=1 / (1 / 4 + 1 / 12))
    add(2, check=1 + 40000 / 10000)
    add(3, check=1 / (2 * math.pi * 1000 * 10e-6), nyquist_rate=2 * 150)
    add(
        4,
        check=(2.10 - 0.10) / 0.5,
        uncertainty_propagation=math.hypot(10 * 0.02, 2 * 0.1),
    )
    add(
        5,
        divider=3.3 * 12500 / 22500,
        thevenin_r=1 / (1 / 10000 + 1 / 12500),
        loading_error=100 * (1 - 10e6 / 11e6),
        lsb=3.3 / 4096 * 1000,
        temperature_resolution=0.806 / 40,
    )
    add(
        6,
        cutoff=1 / (2 * math.pi * 10000 * 10e-9),
        noise_gain=1 / math.sqrt(1 + (10000 / 1591.5) ** 2),
        decibels=20 * math.log10(0.1572),
        phase=-math.degrees(math.atan(100 / 1591.5)),
        alias_gain=1 / math.sqrt(1 + (1000 / 1591.5) ** 2),
    )
    va, vb = nodal()
    test_va = 1 * 0.001 / 0.0025
    test_current = 1 / 1000 + (1 - test_va) / 1000
    add(
        7,
        node_a=va,
        node_b=vb,
        source_current=(6 - va) / 1000 * 1000,
        source_power=6 * (6 - va) / 1000 * 1000,
        port_resistance=1 / test_current,
        loaded_port=nodal(0.001)[1],
    )
    out = bisect(lambda v: 1000 * (0.05 - 0.1 * v) - v, 0, 1)
    gain = out / 0.05
    add(
        8,
        ideal_gain=1 + 90000 / 10000,
        finite_gain=gain,
        finite_output=out * 1000,
        input_difference=(0.05 - 0.1 * out) * 1000,
        bias_shift=-10e-9 * 200000 * 1000,
        positive_limit=0.8 / gain * 1000,
    )
    add(
        9,
        differential=(0.502 - 0.498) * 1000,
        common_mode=(0.502 + 0.498) / 2,
        total_output=0.02 + 100 * (0.502 - 0.498) + 0.01 * (0.502 + 0.498) / 2,
        common_contribution=0.01 * 0.5 * 1000,
        rejection_db=20 * math.log10(100 / 0.01),
        imbalance_output=100 * (-5e-9 * 200000 + 5e-9 * 100000) * 1000,
    )
    add(
        10,
        lowpass_time=1 / (2 * math.pi * 10),
        lowpass_amplitude=abs(1 / (1 + 1j * 0.1)),
        highpass_time=1 / (2 * math.pi * 0.1),
        step_remainder=integrate(lambda s: [-s[0]], [1], 1)[0],
        buffered_cascade=abs(1 / (1 + 1j) ** 2),
        passive_ladder=abs(1 / (1 + 3j + 1j**2)),
    )
    # Transform f=100 tan(theta) to integrate the complete one-pole tail.
    band = quadrature(
        lambda theta: 100 / (1 + math.tan(theta) ** 2) / math.cos(theta) ** 2,
        0,
        math.pi / 2 - 1e-9,
    )
    add(
        11,
        noise_bandwidth=band,
        input_rms=6 * math.sqrt(band),
        output_rms=20 * 6 * math.sqrt(band) / 1000,
        independent_sum=math.hypot(3, 4),
        correlated_sum=math.sqrt(9 + 16 + 2 * 0.5 * 3 * 4),
        calibration_uncertainty=math.sqrt(
            (0.02 / 0.5) ** 2 + (0.01 / 0.5) ** 2 + ((2.1 - 0.1) * 0.005 / 0.5**2) ** 2
        ),
    )
    width = 2 / 1024
    code = math.floor(0.503 / width)
    center = (code + 0.5) * width
    settling = bisect(lambda t: 2 * math.exp(-t) - width / 2, 0, 20)
    add(
        12,
        bin_width=width * 1000,
        adc_code=code,
        reconstruction=center * 1000,
        signed_error=(center - 0.503) * 1e6,
        acquisition_time=settling,
        aliased_frequency=abs(1300 - round(1300 / 1000) * 1000),
    )
    add(
        13,
        interior_gain=(0.6 - (-0.4)) / (0.005 - (-0.005)),
        interior_offset=0.1,
        positive_headroom=(1 - 0.1) / 100 * 1000,
        negative_headroom=(-1 - 0.1) / 100 * 1000,
        clipped_output=min(1, max(-1, 0.1 + 100 * 0.015)),
        drift_half_second=0.1 + 0.3 * math.exp(-1),
    )
    _, _, means = lab_data()
    low = fit([-0.005, 0, 0.005], [means[k] for k in ["low_m5", "low_0", "low_p5"]])[1]
    high = fit(
        [-0.005, 0, 0.005], [means[k] for k in ["high_m5", "high_0", "high_p5"]]
    )[1]
    common = (means["cm_p1"] - means["cm_m1"]) / 2
    tau = -0.5 / math.log((means["drift_05"] - 0.1) / (means["drift_0"] - 0.1))
    add(
        "lab-01",
        low_gain=low,
        high_gain=high,
        rejection=20 * math.log10(high / common),
        drift_time=tau,
    )
    return result


EXPECTED = expected_answers()


@pytest.mark.parametrize("item_id,expected", EXPECTED.items(), ids=list(EXPECTED))
def test_numeric_key_matches_separate_calculation(item_id, expected):
    spec = BANK[item_id]["solution_spec"]
    allowance = spec["tolerance"] + spec.get("relative_tolerance", 0) * abs(
        spec["answer"]
    )
    assert abs(spec["answer"] - expected) <= allowance + 1e-10


def test_all_numeric_keys_are_recalculated():
    numeric = {q["id"] for q in BANK.values() if q["type"] == "numeric"}
    assert set(EXPECTED) == numeric and len(numeric) == 63


CHECKS = BANK["circuits-lab-01:summary"]["solution_spec"]["validation_spec"]["checks"]


@pytest.mark.parametrize("check", CHECKS, ids=[check["id"] for check in CHECKS])
def test_csv_cells_recompute_from_committed_reports(check):
    _, groups, means = lab_data()
    actual = (
        len(groups[check["row_id"]])
        if check["column"] == "replicates"
        else means[check["row_id"]]
    )
    assert check["answer"] == pytest.approx(actual, abs=check["tolerance"])


def test_node_power_port_prediction_and_matching_objective():
    va, vb = nodal()
    heat = (6 - va) ** 2 / 1000 + va**2 / 2000 + (va - vb) ** 2 / 1000 + vb**2 / 1000
    assert heat == pytest.approx(6 * (6 - va) / 1000)
    rth = EXPECTED["circuits-7:port-resistance"]
    assert nodal(0.001)[1] == pytest.approx(vb * 1000 / (rth + 1000))
    matched_voltage = vb * rth / (rth + rth)
    assert matched_voltage**2 / rth == pytest.approx(0.0009)
    near_open_voltage = vb * 1e9 / (rth + 1e9)
    assert near_open_voltage > matched_voltage
    assert near_open_voltage**2 / 1e9 < matched_voltage**2 / rth


def test_finite_feedback_bias_and_saturation_domain():
    output = EXPECTED["circuits-8:finite-output"] / 1000
    assert 1000 * (0.05 - 0.1 * output) == pytest.approx(output)
    assert 0 < 0.05 - 0.1 * output < 0.001
    assert -10e-9 * 200000 == -0.002
    demand = 0.1 * EXPECTED["circuits-8:finite-gain"]
    assert demand > 0.8
    saturated = 0.8
    assert 1000 * (0.1 - 0.1 * saturated) != pytest.approx(saturated)


def test_common_mode_ratio_mismatch_bias_and_input_range():
    k1, k2 = 10, 10.1
    noninv = (1 + k1) * k2 / (1 + k2)
    inv = k1
    common = noninv - inv
    assert common == pytest.approx(0.009009009)
    # Independently solve the ideal difference-amplifier node relations for Vp=Vm=1.
    vminus = k2 / (1 + k2)
    output = (1 + k1) * vminus - k1
    assert output == pytest.approx(common)
    vp, vm = 2, 2
    assert vp - vm == 0 and 0.02 + 0.01 * (vp + vm) / 2 < 1
    assert (
        max(vp, vm) > 1.5
    )  # Small computed output does not certify valid input range.


@pytest.mark.parametrize("duration", [0.01, 0.05, 0.2])
def test_passive_ladder_state_ode_and_power_ledger(duration):
    resistance, cap, source = 1000, 10e-6, 1

    def derivative(state):
        v1, v2, _, _ = state
        first = (source - v1) / resistance
        second = (v1 - v2) / resistance
        return [
            (first - second) / cap,
            second / cap,
            source * first,
            ((source - v1) ** 2 + (v1 - v2) ** 2) / resistance,
        ]

    v1, v2, work, heat = integrate(derivative, [0, 0, 0, 0], duration)
    assert 0 < v2 < v1 < 1
    assert work == pytest.approx(heat + 0.5 * cap * (v1 * v1 + v2 * v2), abs=1e-13)


def test_loaded_ladder_phasors_and_buffered_band():
    s = 1j
    v2 = 1 / (1 + 3 * s + s * s)
    v1 = (1 + s) * v2
    assert 1 - v1 == pytest.approx(s * v1 + v1 - v2)
    assert v1 - v2 == pytest.approx(s * v2)
    assert abs(v2) == pytest.approx(1 / 3)
    assert abs(1 / (1 + s) ** 2) == pytest.approx(0.5)
    cascade = (1 / (1 + 0.1j)) * (10j / (1 + 10j))
    assert cascade.real == pytest.approx(100 / 101) and cascade.imag == pytest.approx(0)


@pytest.mark.parametrize("rho", [-1, 0, 0.5, 1])
def test_constructed_orthogonal_components_check_covariance_sum_and_difference(rho):
    u, v = [1, -1, 1, -1], [1, 1, -1, -1]
    first = [3 * a for a in u]
    second = [4 * (rho * a + math.sqrt(1 - rho * rho) * b) for a, b in zip(u, v)]
    summed = math.fsum((a + b) ** 2 for a, b in zip(first, second)) / 4
    difference = math.fsum((a - b) ** 2 for a, b in zip(first, second)) / 4
    assert summed == pytest.approx(25 + 24 * rho)
    assert difference == pytest.approx(25 - 24 * rho)
    assert summed >= 0 and difference >= 0


def test_calibration_sensitivities_covariance_and_standard_uncertainty():
    def invert(voltage, offset, gain):
        return (voltage - offset) / gain

    values = [2.1, 0.1, 0.5]
    step = 1e-6
    gradient = []
    for axis in range(3):
        plus, minus = list(values), list(values)
        plus[axis] += step
        minus[axis] -= step
        gradient.append((invert(*plus) - invert(*minus)) / (2 * step))
    assert gradient == pytest.approx([2, -2, -8], rel=1e-8)
    uncertainty = math.sqrt(
        math.fsum((a * b) ** 2 for a, b in zip(gradient, [0.02, 0.01, 0.005]))
    )
    assert uncertainty == pytest.approx(EXPECTED["circuits-11:calibration-uncertainty"])
    correlated_variance = uncertainty**2 + 2 * gradient[1] * gradient[2] * (
        0.5 * 0.01 * 0.005
    )
    assert correlated_variance > uncertainty**2
    assert uncertainty < 0.04 + 0.02 + 0.04


def test_quantizer_bins_bounds_dc_counterexample_and_acquisition_ode():
    width = 2 / 1024
    for code in range(1024):
        center = (code + 0.5) * width
        assert math.floor(center / width) == code
    for index in range(1000):
        voltage = 2 * index / 1000
        reconstruction = (math.floor(voltage / width) + 0.5) * width
        assert abs(reconstruction - voltage) <= width / 2 + 1e-15
    repeated = [(math.floor(0.503 / width) + 0.5) * width - 0.503] * 10
    assert len(set(repeated)) == 1 and repeated[0] != 0
    required = EXPECTED["circuits-12:acquisition-time"] * 1e-6
    remaining = integrate(lambda state: [-state[0] / 1e-6], [2], required)[0]
    assert remaining == pytest.approx(width / 2, abs=1e-12)
    assert 2 * math.exp(-required / (2 * 1e-6)) > width / 2


def test_alias_equivalence_and_exact_nyquist_phase_ambiguity():
    for sample in range(30):
        assert math.cos(2 * math.pi * 1300 * sample / 1000) == pytest.approx(
            math.cos(2 * math.pi * 300 * sample / 1000), abs=1e-12
        )
        assert math.sin(math.pi * sample) == pytest.approx(0, abs=1e-13)
        assert math.sin(math.pi * sample + math.pi / 2) == pytest.approx(
            (-1) ** sample, abs=1e-13
        )


@pytest.mark.parametrize("condition", ["low", "high", "common", "drift"])
def test_lab_known_inputs_clamp_before_variants_and_rounding(condition):
    rows, groups, means = lab_data()
    assert len(rows) == 48 and len(groups) == 16 and len(CHECKS) == 32
    selected = [r for r in rows if r["condition"] == condition]
    for row in selected:
        diff = float(row["input_diff_mv"]) / 1000
        common = float(row["input_common_v"])
        if condition == "drift":
            internal = 0.1 + 0.3 * math.exp(-float(row["time_s"]) / 0.5)
        else:
            gain = 20 if condition == "low" else 100
            internal = 0.1 + gain * diff + 0.01 * common
            assert row["time_s"] == ""
        perturbation = (int(row["replicate"]) - 2) * 0.001
        output = max(-1, min(1, internal + perturbation))
        assert float(row["reported_output_v"]) == pytest.approx(output, abs=0.00000051)
        assert len(groups[row["sample"]]) == 3
    if condition == "high":
        assert groups["high_m15"] == [-1] * 3 and groups["high_p15"] == [1] * 3
    assert means["high_0"] == pytest.approx(0.1)


def test_interior_vs_all_point_calibration_and_lost_clipped_amplitude():
    _, _, means = lab_data()
    interior = fit(
        [-0.005, 0, 0.005], [means[k] for k in ["high_m5", "high_0", "high_p5"]]
    )
    whole = fit(
        [-0.015, -0.005, 0, 0.005, 0.015],
        [means[k] for k in ["high_m15", "high_m5", "high_0", "high_p5", "high_p15"]],
    )
    assert interior == pytest.approx([0.1, 100])
    assert whole == pytest.approx([0.06, 70])
    assert (means["high_p15"] - 0.1) / 100 == pytest.approx(0.009)
    assert (means["high_p15"] - 0.1) / 100 != 0.015
    assert -1 <= 0.1 + 20 * 0.015 <= 1


@pytest.mark.parametrize(
    "key,time", [("drift_05", 0.5), ("drift_1", 1), ("drift_2", 2)]
)
def test_baseline_excess_time_estimates_allow_declared_rounding(key, time):
    _, _, means = lab_data()
    inferred = -time / math.log((means[key] - 0.1) / (means["drift_0"] - 0.1))
    assert inferred == pytest.approx(0.5, rel=3e-5)
    wrong = -time / math.log(means[key] / means["drift_0"])
    assert abs(wrong - 0.5) > 0.1

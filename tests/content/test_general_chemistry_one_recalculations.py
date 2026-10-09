"""Separate calculations for synthetic chemistry; not independent human review.

No authoring imports. Uses conservation, Decimal unit calculations, direct
concentration polynomial roots and the committed observations.
"""

from __future__ import annotations

import csv
import json
import math
from decimal import Decimal, localcontext
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/general-chemistry-1"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


BANK = {q["id"]: q for q in load(COURSE / "question-banks/practice.json")["questions"]}


def bisect(function, low, high):
    assert function(low) * function(high) <= 0
    for _ in range(100):
        middle = (low + high) / 2
        if function(middle) > 0:
            high = middle
        else:
            low = middle
    return (low + high) / 2


def hydrogen_root(total, spectator, ka=10 ** (-4.8), kw=1e-14):
    # Multiply the charge residual by h(ka+h), then solve the resulting
    # cubic directly in concentration. Author solved charge in log space.
    def polynomial(h):
        return (
            h**3
            + (ka + spectator) * h * h
            + (spectator * ka - total * ka - kw) * h
            - kw * ka
        )

    return bisect(polynomial, 0, 1)


def inventory_ph(acid, base, pka=4.8):
    # Recover hydrogen from Ka=H*A/HA before taking its logarithm.
    assert acid > 0 and base > 0
    return -math.log10(10 ** (-pka) * acid / base)


def lab_data():
    with (COURSE / "labs/buffer-reports.csv").open(
        encoding="utf-8", newline=""
    ) as stream:
        rows = list(csv.DictReader(stream))
    groups = {}
    for row in rows:
        groups.setdefault(row["sample"], []).append(float(row["reported_pH"]))
    means = {key: math.fsum(values) / len(values) for key, values in groups.items()}
    return rows, groups, means


def partition_water(amount, water_volume, other_volume, coefficient):
    # Solve simultaneous amount conservation and concentration ratio.
    water_concentration = bisect(
        lambda c: c * water_volume + coefficient * c * other_volume - amount,
        0,
        amount / water_volume,
    )
    return water_concentration * water_volume / amount


def expected_answers():
    answers = {}

    def add(lesson, **values):
        answers.update(
            {
                f"general-chemistry-1-{lesson}:{key.replace('_', '-')}": value
                for key, value in values.items()
            }
        )

    add(
        2,
        check=bisect(lambda volume: 1.5 * volume / 1000 - 0.10 * 0.300, 0, 300),
        limiting_reagent=min(4 / 2.016 / 2, 32 / 32) * 2 * 18.02,
    )
    add(3, check=-620 - (-410), reaction_enthalpy=(-393.5 + 2 * (-285.8)) - (-74.8))
    amount = 0.150 * 0.500
    add(
        5,
        mass_needed=amount * 58.44,
        purity_correction=bisect(lambda mass: mass * 0.98 - amount * 58.44, 0, 10),
        mgml_to_mm=4.5 / 180.16 * 1000,
        stock_volume=bisect(lambda volume: 5 * volume / 1000 - 0.150 * 0.200, 0, 200),
        serial_dilution=2 * 1000 * (0.1) ** 4,
    )
    heat = (100 + 5.35) * 4.18 * (-3.3)
    add(
        6,
        fraction_water_equal=partition_water(1, 1, 1, 100),
        fraction_water_unequal=partition_water(1, 0.100, 0.010, 100),
        q_solution=heat,
        delta_h=1453 / 0.1 / 1000,
    )
    with localcontext() as context:
        context.prec = 40
        h = Decimal("6.62607015e-34")
        c = Decimal("299792458")
        na = Decimal("6.02214076e23")
        energy = h * c / Decimal("500e-9")
        scaled_energy = float(energy / Decimal("1e-19"))
        molar_energy = float(energy * na / 1000)
        count = float(Decimal(".02500") * na / Decimal("1e22"))
    add(
        7,
        ion_electrons=12 - 2,
        shell_capacity=2 + 6,
        isotope_average=math.fsum([35] * 3 + [37]) / 4,
        entity_count=count,
        photon_energy=scaled_energy,
        photon_molar_energy=molar_energy,
    )
    angle = bisect(
        lambda degrees: math.cos(math.radians(180 - degrees)) - 1 / 3, 90, 180
    )
    # Use components and the law of cosines instead of the author's half-angle formula.
    theta = math.radians(104.5)
    resultant = math.hypot(1 + math.cos(theta), math.sin(theta))
    add(
        8,
        co2_valence=4 + 6 + 6,
        ammonium_valence=5 + 4 - 1,
        nitrogen_formal_charge=5 - 4,
        water_lone_pairs=(6 + 2 - 2 * 2) / 2,
        tetrahedral_angle=angle,
        bent_dipole=resultant,
    )
    extent = min(0.8, 1.8 / 3)
    consumed_mass = extent * 28 + 3 * extent * 2
    precipitate = min(0.100 * 0.020, 0.150 * 0.010)
    leftover = 0.100 * 0.020 - precipitate
    add(
        9,
        ammonia_amount=2 * extent,
        nitrogen_left=0.8 - extent,
        product_mass=consumed_mass,
        percent_yield=100 * 15.3 / consumed_mass,
        precipitate_amount=precipitate,
        remaining_ion=leftover / 0.250 * 1000,
    )
    pressure = 0.2500 * 8.314 * 300 / 0.005
    partial_a = 0.10 * 8.314 * 300 / 0.005 / 1000
    rms = bisect(lambda speed: 0.028 * speed * speed / 2 - 1.5 * 8.314 * 300, 0, 1000)
    add(
        10,
        gas_pressure=pressure,
        mole_fraction=0.1 / (0.1 + 0.15),
        partial_pressure=partial_a,
        temperature_ratio=600 / 300,
        rms_speed=rms,
        compressibility=135000 / pressure,
    )
    surroundings = (100 * 4 + 20) * 3
    add(
        11,
        internal_energy=500 - 200,
        expansion_work=-100000 * 0.0015,
        reaction_heat=-surroundings,
        molar_enthalpy=-surroundings / 0.0200 / 1000,
        hess_total=-40 + 15,
        enthalpy_correction=-10 + (2 * 8.314 * 300) / 1000,
    )
    extent = bisect(lambda x: (0.2 + x) / (1 - x) - 4, 0, 0.999)
    a, b = 1 - extent, 0.2 + extent
    add(
        12,
        equilibrium_a=a,
        equilibrium_b=b,
        extent=extent,
        reverse_constant=a / b,
        doubled_constant=(b / a) ** 2,
        activity_quotient=(0.6 * 1) / (0.8 * 0.5),
    )
    add(
        13,
        activity_ph=-math.log10(0.7 * 1e-5),
        initial_buffer=inventory_ph(0.05, 0.03),
        after_ten=inventory_ph(0.06, 0.02),
        after_twenty=inventory_ph(0.07, 0.01),
        base_inventory=0.03,
        exhausted_ph=-math.log10(hydrogen_root(0.16, 0, kw=0)),
    )
    _, _, means = lab_data()
    offset = means["reference"] - 4
    add(
        "lab-01",
        reference_offset=offset,
        corrected_ten=means["q10"] - offset,
        nominal_ten=inventory_ph(0.05 + 0.01, 0.03 - 0.01),
        full_thirty=-math.log10(hydrogen_root(0.16, (0.024 - 0.030) / 0.5)),
    )
    return answers


EXPECTED = expected_answers()


@pytest.mark.parametrize("question_id", sorted(EXPECTED))
def test_numeric_keys_with_separate_calculations(question_id):
    spec = BANK[question_id]["solution_spec"]
    assert spec["answer"] == pytest.approx(
        EXPECTED[question_id], abs=max(spec["tolerance"], 1e-8), rel=2e-6
    )


def test_numeric_inventory_is_exhaustive():
    assert set(EXPECTED) == {key for key, q in BANK.items() if q["type"] == "numeric"}
    assert len(EXPECTED) == 59


CHECKS = BANK["general-chemistry-1-lab-01:summary"]["solution_spec"]["validation_spec"][
    "checks"
]


@pytest.mark.parametrize("check", CHECKS, ids=lambda check: check["id"])
def test_csv_summary_keys_match_committed_rows(check):
    _, groups, means = lab_data()
    values = groups[check["row_id"]]
    expected = (
        len(values) if check["column"] == "replicates" else means[check["row_id"]]
    )
    assert check["answer"] == pytest.approx(expected, abs=check["tolerance"])
    assert check["calculation"]["values"] == values


def correct_option(key):
    q = BANK[key]
    return q["options"][q["solution_spec"]["answer"]]


def test_amount_scales_and_precision_prompts():
    assert 35 < EXPECTED["general-chemistry-1-7:isotope-average"] < 37
    specs = [
        q
        for q in BANK.values()
        if q["type"] == "numeric" and q["solution_spec"]["significant_figures"]
    ]
    assert len(specs) == 6
    assert all(
        "exactly" in q["prompt"] and "significant figures" in q["prompt"] for q in specs
    )
    assert "Electron count decreases by two" in correct_option(
        "general-chemistry-1-7:identity"
    )
    assert "sample/wavelength uncertainty remains" in correct_option(
        "general-chemistry-1-7:exactness"
    )


def test_lewis_geometry_and_dipole_limits():
    assert 5 - 4 == 1 and 4 * (1 - 1) == 0
    assert math.hypot(1 + math.cos(math.pi), math.sin(math.pi)) == pytest.approx(
        0, abs=1e-15
    )
    assert "bent molecular shape" in correct_option("general-chemistry-1-8:shape")
    assert "equal opposing bond vectors can cancel" in correct_option(
        "general-chemistry-1-8:polarity"
    )


def test_reaction_mass_charge_and_leftover_balance():
    extent = 0.6
    assert (0.8 - extent) >= 0 and (1.8 - 3 * extent) == pytest.approx(0)
    assert 0.8 * 28 + 1.8 * 2 == pytest.approx(1.2 * 17 + 0.2 * 28)
    precipitate = EXPECTED["general-chemistry-1-9:precipitate-amount"]
    assert precipitate + 0.0005 == pytest.approx(0.002)
    assert 2 + (-2) == 0
    assert "completion assumption" in correct_option(
        "general-chemistry-1-9:precipitation"
    )


def test_gas_pressure_sums_and_state_conditions():
    pa = EXPECTED["general-chemistry-1-10:partial-pressure"]
    pb = 0.15 * 8.314 * 300 / 0.005 / 1000
    assert (pa + pb) * 1000 == pytest.approx(EXPECTED["general-chemistry-1-10:gas-pressure"])
    assert "Absolute temperature in kelvin" in correct_option(
        "general-chemistry-1-10:temperature"
    )
    assert "distinct from directed bulk velocity" in correct_option(
        "general-chemistry-1-10:rms"
    )
    assert "state-input errors" in correct_option("general-chemistry-1-10:z-inference")


def test_energy_signs_capacities_and_equation_scaling():
    q = EXPECTED["general-chemistry-1-11:reaction-heat"]
    assert q + (100 * 4 + 20) * 3 == 0
    assert abs(q) > 100 * 4 * 3
    assert -(-40) + (-15) == 25
    assert 2 * (-40 + 15) == -50
    assert "Reaction heat is negative" in correct_option(
        "general-chemistry-1-11:calorimeter"
    )
    assert "different states" in correct_option("general-chemistry-1-11:phase")


def test_equilibrium_conservation_activity_and_direction():
    a, b = (
        EXPECTED["general-chemistry-1-12:equilibrium-a"],
        EXPECTED["general-chemistry-1-12:equilibrium-b"],
    )
    assert a + b == pytest.approx(1.2) and b / a == pytest.approx(4)
    assert a > 0 and b > 0
    assert 0.2 / 1 < 4
    assert EXPECTED["general-chemistry-1-12:activity-quotient"] != 1 / 0.5
    assert "Net forward change" in correct_option("general-chemistry-1-12:q-k")
    assert "Rates of approach" in correct_option("general-chemistry-1-12:catalyst")


def test_full_buffer_roots_mass_charge_and_approximation_boundary():
    ka = 10 ** (-4.8)
    for load in (0, 0.005, 0.01, 0.02, 0.025, 0.03):
        spectator = (0.024 - load) / 0.5
        h = hydrogen_root(0.16, spectator)
        anion = 0.16 * ka / (ka + h)
        acid = 0.16 - anion
        hydroxide = 1e-14 / h
        assert 0 < anion < 0.16 and acid > 0
        assert acid + anion == pytest.approx(0.16)
        assert h + spectator == pytest.approx(anion + hydroxide, abs=1e-12)
        assert h * anion / acid == pytest.approx(ka)
    assert 0.024 - 0.030 < 0
    assert "Replace the failed inventory-ratio logarithm" in correct_option(
        "general-chemistry-1-13:zero-base"
    )


def test_lab_construction_reference_and_independent_composition():
    rows, groups, means = lab_data()
    assert len(rows) == 21 and all(len(values) == 3 for values in groups.values())
    for row in rows:
        if row["sample"] == "reference":
            assert row["acid_equivalents_mol"] == ""
            true_ph = 4
        else:
            load = float(row["acid_equivalents_mol"])
            true_ph = -math.log10(hydrogen_root(0.16, (0.024 - load) / 0.5))
        central = round(true_ph + 0.08, 4)
        offset = (int(row["replicate"]) - 2) * 0.01
        assert float(row["reported_pH"]) == pytest.approx(central + offset, abs=1e-10)
    calibration = means["reference"] - 4
    assert calibration == pytest.approx(0.08)
    actual_initial = means["q00"] - calibration
    actual_ten = means["q10"] - calibration
    nominal_initial = inventory_ph(0.05, 0.03)
    nominal_ten = inventory_ph(0.06, 0.02)
    assert actual_ten < nominal_ten
    assert actual_initial - actual_ten > nominal_initial - nominal_ten
    assert 0.024 + 0.056 == 0.030 + 0.050


def test_logarithmic_averaging_and_nonunique_discrepancy():
    _, groups, _ = lab_data()
    readings = groups["q10"]
    mean_ph = math.fsum(readings) / len(readings)
    log_of_mean = -math.log10(
        math.fsum(10 ** (-value) for value in readings) / len(readings)
    )
    assert log_of_mean < mean_ph
    assert "Calibration, composition and nonideal explanations" in correct_option(
        "general-chemistry-1-13:cause"
    )


def test_link_only_references_and_disclosed_access():
    registry = {
        s["id"]: s for s in load(ROOT / "content/sources/registry.json")["sources"]
    }
    for name in ["nist-si-defining-constants", "iupac-goldbook-ph-definition"]:
        source = registry[name]
        assert (
            source["accessed_at"] == "2026-10-09"
            and source["reuse_mode"] == "link-only-reference"
        )
        assert source["permissions"] == {
            "linking": True,
            "quotation": False,
            "adaptation": False,
            "redistribution": False,
        }
        assert source["imported_assets"] == []
    assert "403" in registry["iupac-goldbook-ph-definition"]["version"]


def test_schedule_and_conservative_labels():
    manifest = load(COURSE / "course.json")
    assert manifest["version"] == "0.4.0" and manifest["maturity"] == "partial"
    assert (
        manifest["review"]["status"] == "unreviewed"
        and manifest["grading_policy"]["mode"] == "formative-only"
    )
    lessons = {
        lesson["id"] for module in manifest["modules"] for lesson in module["lessons"]
    }
    weeks = manifest["duration"]["weeks"]
    assert [week["week"] for week in weeks] == list(range(1, 15))
    assert {lid for week in weeks for lid in week["lesson_ids"]} == lessons
    assert weeks[-1]["assessment_ids"] == [
        "general-chemistry-1-week14-buffer-lab",
        "general-chemistry-1-case",
    ]
    assert len(lessons) == 14 and len(BANK) == 91
    text = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    assert "14 readings, 91 public practice items and 48 retrieval cards" in text
    assert "Weeks 1, 4, 8 and 11 retain compact prototype readings" in text

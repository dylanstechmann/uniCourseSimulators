"""Separate chemical/model calculations; same-AI checks, not human review.

No authoring imports. Tests committed numeric/CSV keys, atom/charge ledgers,
spatial orientation, spin enumeration and component differential equations.
"""

from __future__ import annotations

import csv
import itertools
import json
import math
from collections import Counter
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/organic-chemistry"


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


def integrate(function, initial, duration, steps=1000):
    """Component RK4 independent of author's exponential item formulas."""
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


def parallel(initial, time, a, b):
    def derivative(state):
        return [-(a + b) * state[0], a * state[0], b * state[0]]

    return integrate(derivative, [initial, 0, 0], time)


def dbe(carbon, hydrogen, nitrogen=0, halogen=0):
    return (2 * carbon + 2 + nitrogen - hydrogen - halogen) / 2


def splitting(neighbors):
    # Enumerate neighboring spin configurations; no n+1 expression used.
    return Counter(sum(spins) for spins in itertools.product([-1, 1], repeat=neighbors))


def lab_data():
    with (COURSE / "labs/peak-reports.csv").open(
        encoding="utf-8", newline=""
    ) as stream:
        rows = list(csv.DictReader(stream))
    groups = {}
    for row in rows:
        groups.setdefault(row["sample"], []).append(
            [float(row["area_a"]), float(row["area_b"])]
        )
    means = {
        key: [
            math.fsum(pair[column] for pair in values) / len(values)
            for column in (0, 1)
        ]
        for key, values in groups.items()
    }
    return rows, groups, means


def calibrated(means, sample):
    gains = [
        (means["std_a"][0] - means["blank"][0]) / 10,
        (means["std_b"][1] - means["blank"][1]) / 10,
    ]
    return [(means[sample][i] - means["blank"][i]) / gains[i] for i in (0, 1)]


def expected_answers():
    answers = {}

    def add(lesson, **values):
        answers.update(
            {
                f"organic-chemistry-{lesson}:{key.replace('_', '-')}": value
                for key, value in values.items()
            }
        )

    long_fraction = bisect(
        lambda fraction: 0.01 * (1 - fraction) - math.log(2) / 10 * fraction, 0, 1
    )
    short_fraction = bisect(
        lambda fraction: 0.01 * (1 - fraction) - math.log(2) * 365 / 2 * fraction, 0, 1
    )
    add(
        5,
        histidine_fraction=100 / (1 + 10 ** (7.4 - 6)),
        lysine_unprotonated=100 / (1 + 10 ** (10.5 - 7.4)),
        steady_state_long_lived=long_fraction,
        steady_state_short_lived=short_fraction,
    )
    add(
        6,
        sn2_rate=0.002 * 0.1 * 0.4,
        stereoisomers=len(list(itertools.product([0, 1], repeat=3))),
        enantiomeric_excess=100 * (-9.2) / (-11.5),
        major_fraction=100
        * bisect(lambda fraction: fraction - (1 - fraction) - 0.8, 0, 1),
    )
    add(
        7,
        electron_budget=5 * 4 + 9 + 5 + 6,
        unsaturation=dbe(5, 9, 1),
        proton_transfer=10 ** (9 - 5),
        base_fraction=bisect(lambda fraction: fraction / (1 - fraction) - 10, 0, 0.99),
    )
    weight = bisect(lambda w: 8.314 * 300 * math.log(w) + 5000, 0.01, 1)
    pair = list(itertools.product([0, 1], repeat=2))
    symmetric = {tuple(sorted(bits)) for bits in pair}
    add(
        8,
        conformer_weight=weight,
        degenerate_population=(weight + weight) / math.fsum([1, weight, weight]),
        no_symmetry_count=len(pair),
        meso_count=len(symmetric),
    )
    a, b = 0.02 * 0.1, 0.01 * 0.2
    add(
        9,
        substitution_rate=a * 0.05,
        elimination_rate=b * 0.05,
        substitution_branch=a / (a + b),
        substrate_half=bisect(
            lambda time: 0.05 * math.exp(-(a + b) * time) - 0.025, 0, 400
        ),
    )
    adduct = bisect(lambda product: product / ((0.1 - product) * 0.2) - 10, 0, 0.099)

    def hydrolysis(state):
        return [-0.03 * state[0], 0.03 * state[0]]

    remaining, product = integrate(hydrolysis, [0.1, 0], 30)
    add(
        10,
        adduct_amount=adduct,
        free_carbonyl=0.1 - adduct,
        hydrolysis_remaining=remaining,
        hydrolysis_product=product,
    )
    add(
        11,
        alpha_hydrogens=3,
        proton_transfer=10 ** (22 - 20),
        aldol_carbons=2 + 2,
        dehydrated_unsaturation=dbe(4, 8 - 2),
    )
    add(
        12,
        formula_unsaturation=dbe(4, 8),
        integral_fraction=3 / sum([3, 2, 3]),
        methylene_lines=len(splitting(3)),
        methyl_lines=len(splitting(2)),
    )
    intermediate, target, _ = parallel(1, 20, 0.04, 0.01)
    add(
        13,
        target_branch=0.04 / (0.04 + 0.01),
        intermediate_half=bisect(lambda time: math.exp(-0.05 * time) - 0.5, 0, 30),
        intermediate_twenty=intermediate,
        target_twenty=target,
    )
    _, _, means = lab_data()
    mix_two = calibrated(means, "mix_2")
    mix_four = calibrated(means, "mix_4")
    add(
        "lab-01",
        blank_offset=means["blank"][0],
        a_gain=(means["std_a"][0] - means["blank"][0]) / 10,
        mix_two_excess=100 * (mix_two[0] - mix_two[1]) / sum(mix_two),
        mix_four_ratio=mix_four[1] / mix_four[0],
    )
    return answers


EXPECTED = expected_answers()


@pytest.mark.parametrize("item_id,expected", EXPECTED.items(), ids=list(EXPECTED))
def test_numeric_key_matches_separate_calculation(item_id, expected):
    spec = BANK[item_id]["solution_spec"]
    allowed = spec["tolerance"] + abs(expected) * spec.get("relative_tolerance", 0)
    assert abs(spec["answer"] - expected) <= allowed + 1e-12


def test_every_numeric_item_is_covered_and_enforcement_is_disclosed():
    numeric = {key for key, q in BANK.items() if q["type"] == "numeric"}
    assert set(EXPECTED) == numeric and len(numeric) == 40
    assert (
        sum(q["solution_spec"].get("unit_required", False) for q in BANK.values()) == 4
    )
    assert not any(q["solution_spec"].get("significant_figures") for q in BANK.values())


CSV_CHECKS = BANK["organic-chemistry-lab-01:summary"]["solution_spec"][
    "validation_spec"
]["checks"]


@pytest.mark.parametrize("check", CSV_CHECKS, ids=[c["id"] for c in CSV_CHECKS])
def test_csv_checks_recompute_from_committed_reports(check):
    _, groups, means = lab_data()
    index = 1 if check["column"] == "mean_area_b" else 0
    values = [pair[index] for pair in groups[check["row_id"]]]
    assert check["calculation"]["values"] == pytest.approx(values)
    expected = (
        len(values)
        if check["column"] == "replicates"
        else round(means[check["row_id"]][index], 4)
    )
    assert check["answer"] == pytest.approx(expected, abs=1e-12)


def determinant(rows):
    a, b, c = rows
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def chirality(top, right, bottom, left):
    positions = [(0, 1, -1), (1, 0, 1), (0, -1, -1), (-1, 0, 1)]
    ranked = dict(zip([top, right, bottom, left], positions))
    differences = [
        [ranked[i][axis] - ranked[4][axis] for axis in range(3)] for i in (1, 2, 3)
    ]
    # Negative determinant matches clockwise priorities with fourth away.
    return "R" if determinant(differences) < 0 else "S"


def test_fischer_orientation_swap_rotation_and_priority_order():
    assert chirality(2, 4, 3, 1) == "S"
    assert chirality(2, 1, 3, 4) == "R"
    assert chirality(3, 1, 2, 4) == "S"  # 180-degree page rotation
    assert chirality(1, 2, 4, 3) == "R"  # 90-degree reinterpretation
    carboxyl_next, methyl_next = [8, 8, 8], [1, 1, 1]
    assert carboxyl_next > methyl_next
    assert BANK["organic-chemistry-8:fischer"]["options"][
        BANK["organic-chemistry-8:fischer"]["solution_spec"]["answer"]
    ].startswith("S,")
    text = (
        COURSE / "modules/08-conformations-fischer-maps-and-stereochemical-labels.md"
    ).read_text()
    assert "Description: COOH is above" in text and "CH3" in text


def test_carboxylate_two_pair_flow_preserves_valence_and_charge():
    original_orders, exchanged_orders = [1, 2, 1], [2, 1, 1]
    invalid_one_pair = [2, 2, 1]
    assert sum(original_orders) == sum(exchanged_orders) == 4
    assert sum(invalid_one_pair) == 5
    single_oxygen_charge = 6 - 6 - 2 / 2
    double_oxygen_charge = 6 - 4 - 4 / 2
    assert single_oxygen_charge + double_oxygen_charge == -1


def test_carbonyl_addition_and_collapse_charge_ledgers():
    before_orders = [2, 1, 1]
    tetrahedral_orders = [1, 1, 1, 1]
    assert sum(before_orders) == sum(tetrahedral_orders) == 4
    neutral_nh3_charge = 5 - 2 - 6 / 2
    attached_nh3_charge = 5 - 0 - 8 / 2
    alkoxide_charge = 6 - 6 - 2 / 2
    assert neutral_nh3_charge == 0 and attached_nh3_charge + alkoxide_charge == 0
    restored_orders = [2, 1, 1]
    assert sum(restored_orders) == 4


def test_aldol_atom_mapping_hydrogen_valence_and_dehydration():
    # Heavy-atom ledger: donor C1/C2/O1, acceptor C3/C4/O3.
    edges = [(1, 2, 1), (1, "o1", 2), (2, 3, 1), (3, 4, 1), (3, "o3", 1)]
    order_sum = Counter()
    for first, second, order in edges:
        order_sum[first] += order
        order_sum[second] += order
    hydrogens = {
        node: (4 if isinstance(node, int) else 2) - total
        for node, total in order_sum.items()
    }
    assert hydrogens == {1: 1, 2: 2, 3: 1, 4: 3, "o1": 0, "o3": 1}
    assert sum(hydrogens.values()) == 8 and len(order_sum) == 6
    assert (2, 3, 1) in edges
    assert dbe(4, 8) == 1 and dbe(4, 6) == 2
    assert Counter(C=4, H=8, O=2) - Counter(H=2, O=1) == Counter(C=4, H=6, O=1)


@pytest.mark.parametrize("neighbors,counts", [(2, [1, 2, 1]), (3, [1, 3, 3, 1])])
def test_splitting_spin_enumeration_and_proton_inventory(neighbors, counts):
    distribution = splitting(neighbors)
    assert [distribution[key] for key in sorted(distribution)] == counts
    assert sum(distribution.values()) == 2**neighbors
    assert 3 + 2 + 3 == 8


@pytest.mark.parametrize("time", [0, 10, 20, 40, 100])
def test_parallel_route_ode_conservation_and_finite_conversion(time):
    intermediate, target, hydrolysis = parallel(1, time, 0.04, 0.01)
    assert all(value >= 0 for value in [intermediate, target, hydrolysis])
    assert intermediate + target + hydrolysis == pytest.approx(1, abs=1e-12)
    assert target == pytest.approx(0.8 * (1 - intermediate), abs=1e-12)
    assert hydrolysis == pytest.approx(0.2 * (1 - intermediate), abs=1e-12)
    if time > 0:
        assert target / hydrolysis == pytest.approx(4)
        assert target < 0.8


def test_adduct_inventory_free_donor_and_conformer_degeneracy():
    bound = EXPECTED["organic-chemistry-10:adduct-amount"]
    free = EXPECTED["organic-chemistry-10:free-carbonyl"]
    assert bound + free == pytest.approx(0.1)
    assert bound / (free * 0.2) == pytest.approx(10)
    weight = EXPECTED["organic-chemistry-8:conformer-weight"]
    fraction = EXPECTED["organic-chemistry-8:degenerate-population"]
    assert fraction > weight / (1 + weight)
    assert 0 < weight < 1 and 0 < fraction < 1


@pytest.mark.parametrize(
    "sample,amounts",
    [
        ("blank", [0, 0]),
        ("std_a", [10, 0]),
        ("std_b", [0, 10]),
        ("mix_1", [9, 1]),
        ("mix_2", [7, 3]),
        ("mix_3", [5, 5]),
        ("mix_4", [2, 8]),
    ],
)
def test_lab_model_reconstruction_covarying_repeats_and_amounts(sample, amounts):
    rows, groups, means = lab_data()
    assert len(rows) == 21
    assert calibrated(means, sample) == pytest.approx(amounts)
    expected = [3 + 2 * amounts[0], 3 + amounts[1]]
    assert means[sample] == pytest.approx(expected)
    assert len(groups[sample]) == 3
    for index, delta in enumerate([-0.2, 0, 0.2]):
        assert groups[sample][index] == pytest.approx(
            [expected[0] + delta, expected[1] + delta]
        )


def test_blank_only_area_ratio_is_biased_and_optical_labels_do_not_assign_rs():
    _, _, means = lab_data()
    corrected = [means["mix_2"][i] - means["blank"][i] for i in (0, 1)]
    naive = 100 * (corrected[0] - corrected[1]) / sum(corrected)
    assert naive == pytest.approx(1100 / 17)
    assert naive > EXPECTED["organic-chemistry-lab-01:mix-two-excess"]
    racemic = calibrated(means, "mix_3")
    assert racemic[0] == pytest.approx(racemic[1])
    assert means["mix_3"][0] != means["mix_3"][1]
    text = (COURSE / "labs/01-calibrated-peak-amounts-and-excess.md").read_text()
    assert "not claimed intrinsic UV absorptivity differences" in text
    assert "No R/S descriptors" in text


@pytest.mark.parametrize(
    "number,reference_count", [(7, 1), (8, 1), (9, 1), (11, 1), (12, 2)]
)
def test_primary_reference_rights_remain_link_only(number, reference_count):
    manifest = load(COURSE / "course.json")
    module = next(
        m
        for m in manifest["modules"]
        if m["id"] == f"organic-chemistry-module-{number}"
    )
    sources = {
        s["id"]: s for s in load(ROOT / "content/sources/registry.json")["sources"]
    }
    records = [
        sources[sid]
        for sid in module["source_ids"]
        if sid.startswith("openstax-organic-")
    ]
    assert len(records) == reference_count
    for source in records:
        assert source["permissions"] == dict(
            linking=True, quotation=False, adaptation=False, redistribution=False
        )
        assert source["imported_assets"] == [] and source["accessed_at"] == "2026-10-09"


def test_schedule_partial_labels_and_preserved_case():
    manifest = load(COURSE / "course.json")
    lessons = {
        lesson["id"] for module in manifest["modules"] for lesson in module["lessons"]
    }
    weeks = manifest["duration"]["weeks"]
    assert len(weeks) == 14 and len(lessons) == 14
    assert sorted(lid for week in weeks for lid in week["lesson_ids"]) == sorted(
        lessons
    )
    assert manifest["version"] == "0.4.0" and manifest["maturity"] == "partial"
    assert manifest["review"]["status"] == "unreviewed"
    assert (
        len(BANK) == 91
        and len(load(COURSE / "question-banks/retrieval-cards.json")["cards"]) == 48
    )
    assert all(
        a["mode"] in ("practice", "self-assessment") for a in manifest["assessments"]
    )
    assert len([q for q in BANK.values() if q["type"] == "single_choice"]) >= 35
    case = next(a for a in manifest["assessments"] if a["type"] == "case")
    assert case["points"] == 0 and case["question_ids"] == []

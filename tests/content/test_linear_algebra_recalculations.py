"""AI-assisted recalculation using independent matrix operations, not authoring scripts.

These checks establish arithmetic/structural consistency, not human content review.
"""

from __future__ import annotations

import csv
import json
import math
from fractions import Fraction
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/linear-algebra"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


BANK = {q["id"]: q for q in load(COURSE / "question-banks/practice.json")["questions"]}


def dot(a, b):
    return math.fsum(x * y for x, y in zip(a, b))


def norm(v):
    return math.sqrt(dot(v, v))


def mv(a, v):
    return [dot(row, v) for row in a]


def solve(a, b):
    """Partial-pivot Gauss-Jordan, independent of the author's spectral ridge formula."""
    rows = [[float(v) for v in row] + [float(rhs)] for row, rhs in zip(a, b)]
    n = len(rows)
    for j in range(n):
        pivot = max(range(j, n), key=lambda i: abs(rows[i][j]))
        rows[j], rows[pivot] = rows[pivot], rows[j]
        scale = rows[j][j]
        assert abs(scale) > 1e-12
        rows[j] = [v / scale for v in rows[j]]
        for i in range(n):
            if i != j:
                factor = rows[i][j]
                rows[i] = [x - factor * y for x, y in zip(rows[i], rows[j])]
    return [row[-1] for row in rows]


def rank(a):
    """Exact rational elimination, including rectangular and dependent matrices."""
    rows = [[Fraction(v) for v in row] for row in a]
    r = 0
    for j in range(len(rows[0])):
        pivot = next((i for i in range(r, len(rows)) if rows[i][j]), None)
        if pivot is None:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        scale = rows[r][j]
        rows[r] = [v / scale for v in rows[r]]
        for i in range(r + 1, len(rows)):
            factor = rows[i][j]
            rows[i] = [x - factor * y for x, y in zip(rows[i], rows[r])]
        r += 1
        if r == len(rows):
            break
    return r


def gram(a):
    cols = list(zip(*a))
    return [[dot(x, y) for y in cols] for x in cols]


def spectrum2(a):
    """Power iteration for dominant positive eigenvalue, determinant for the other.

    All callers use positive definite matrices. Avoids the author's quadratic roots.
    """
    q = [1.0, 0.4]
    for _ in range(500):
        v = mv(a, q)
        q = [x / norm(v) for x in v]
    largest = dot(q, mv(a, q))
    smallest = (a[0][0] * a[1][1] - a[0][1] * a[1][0]) / largest
    return largest, smallest, q


def singular_values(a):
    high, low, _ = spectrum2(gram(a))
    return math.sqrt(high), math.sqrt(low)


def fit(x, y):
    xm, ym = sum(x) / len(x), sum(y) / len(y)
    slope = dot([v - xm for v in x], [v - ym for v in y]) / dot(
        [v - xm for v in x], [v - xm for v in x]
    )
    return ym - slope * xm, slope


def sensor_rows():
    with (COURSE / "labs/sensor-pairs.csv").open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    estimates = {}
    for row in rows:
        a = [[float(row[f"a{i}{j}"]) for j in (1, 2)] for i in (1, 2)]
        b = [float(row["b1"]), float(row["b2"])]
        x = solve(a, b)
        assert mv(a, x) == pytest.approx(b, abs=1e-12)
        estimates.setdefault(row["geometry"], []).append(x)
    return rows, estimates


def expected_answers():
    values = {}

    def add(n, **answers):
        values.update(
            {
                f"linear-algebra-{n}:{slug.replace('_', '-')}": v
                for slug, v in answers.items()
            }
        )

    add(
        1,
        check=solve([[1, 1], [1, -1]], [7, 1])[0],
        rank_from_pivots=rank([[1, 2, 3], [2, 4, 6], [1, 0, 1]]),
    )
    add(
        2,
        check=mv([[0, -1], [1, 0]], [3, 0])[1],
        vector_vs_coordinates=mv([[1, 1], [0, 1]], [3, 1])[0],
    )
    component = 1.0
    for _ in range(3):
        component *= 0.8
    add(3, mode_by_mode_decay=component)
    add(4, check=fit([0, 2], [2, 6])[1])
    xs, ys = [0, 1, 2, 3, 4], [0.1, 2.1, 3.9, 6.2, 7.9]
    intercept, slope = fit(xs, ys)
    residuals = [y - intercept - slope * x for x, y in zip(xs, ys)]
    total = sum((v - sum(ys) / len(ys)) ** 2 for v in ys)
    add(
        5,
        slope=slope,
        intercept=intercept,
        r_squared=1 - dot(residuals, residuals) / total,
        read_unknown=(5 - intercept) / slope,
    )
    transition = [[0.8, 0.1], [0.2, 0.9]]
    stationary = [1.0, 0.0]
    for _ in range(200):
        stationary = mv(transition, stationary)
    add(
        6,
        two_steps=mv(transition, mv(transition, [1, 0]))[0],
        stationary=stationary[0],
        second_eigenvalue=sum(transition[i][i] for i in (0, 1)) - 1,
        half_time=24 * math.log(0.5) / math.log(0.7),
    )
    a = [[1, 2, 3], [2, 4, 6], [1, 1, 2]]
    null = [1, 1, -1]
    assert mv(a, null) == [0, 0, 0]
    # KKT system independently minimizes ||x||² under two independent constraints.
    minimum = solve(
        [
            [1, 0, 0, 1, 1],
            [0, 1, 0, 2, 1],
            [0, 0, 1, 3, 2],
            [1, 2, 3, 0, 0],
            [1, 1, 2, 0, 0],
        ],
        [0, 0, 0, 6, 4],
    )[:3]
    add(
        7,
        rank=rank(a),
        nullity=3 - rank(a),
        nullity_4_by_6=6 - 3,
        consistent_entry=mv(a, [1, 1, 1])[1],
        solution_parameter=1,
        min_norm_third=minimum[2],
        min_norm_length=norm(minimum),
        design_rank=rank([[1, 1, 0], [1, 1, 0], [1, 0, 1], [1, 0, 1]]),
    )
    direction, b = [1, 2, 2], [4, 1, 2]
    coefficient = dot(direction, b) / dot(direction, direction)
    residual = [y - coefficient * x for x, y in zip(direction, b)]
    intercept, slope = fit([1, 2, 3], [1, 2, 2])
    fit_residual = [y - intercept - slope * x for x, y in zip([1, 2, 3], [1, 2, 2])]
    add(
        8,
        projection_coefficient=coefficient,
        residual_length=norm(residual),
        r11=norm([1, 1, 1]),
        r12=dot([1 / math.sqrt(3)] * 3, [1, 2, 3]),
        r22=norm([-1, 0, 1]),
        slope_by_qr=slope,
        intercept_by_qr=intercept,
        residual_norm=norm(fit_residual),
    )
    symmetric = [[4, 1], [1, 3]]
    high, low, q = spectrum2(symmetric)
    w = [1 / math.sqrt(2)] * 2
    add(
        9,
        determinant=4 * 3 - 1,
        largest_eigenvalue=high,
        smallest_eigenvalue=low,
        eigenvector_angle=math.degrees(math.atan2(q[1], q[0])),
        variance_diagonal=dot(w, mv(symmetric, w)),
        variance_fraction=high / 7,
        negative_eigenvalue=-1,
        quadratic_form_negative=dot([1, -1], mv([[1, 2], [2, 1]], [1, -1])),
    )
    a = [[3, 1], [2, 2], [1, 3]]
    s1, s2 = singular_values(a)
    frobenius = norm([v for row in a for v in row])
    error = norm([v - 2 for row in a for v in row])
    add(
        10,
        first_singular_value=s1,
        second_singular_value=s2,
        frobenius_norm=frobenius,
        energy_fraction=s1 * s1 / (frobenius * frobenius),
        rank_one_error=error,
        relative_error=error / frobenius,
        storage_rank_3=3 * (1000 + 50 + 1),
        compression=50000 / (3 * 1051),
    )
    poor, improved = [[1, 0.99], [0.99, 1]], [[1, 0.2], [0.2, 1]]
    # Symmetric positive definite matrices: eigenvalues equal singular values.
    high, low, _ = spectrum2(poor)
    better_high, better_low, _ = spectrum2(improved)
    at_a = gram(poor)
    ridge_matrix = [
        [at_a[i][j] + (0.01 if i == j else 0) for j in (0, 1)] for i in (0, 1)
    ]
    rhs = mv(poor, [4.97, 4.98])
    add(
        11,
        condition_number=high / low,
        gram_condition=(high / low) ** 2,
        relative_bound=(high / low) * 0.001,
        error_first=solve(poor, [0.01, -0.01])[0],
        ridge_first=solve(ridge_matrix, rhs)[0],
        improved_condition=better_high / better_low,
    )
    rows = [[8, 19], [12, 21], [10, 19], [10, 21]]
    means = [sum(col) / 4 for col in zip(*rows)]
    centered = [[v - m for v, m in zip(row, means)] for row in rows]
    covariance = [[v / 3 for v in row] for row in gram(centered)]
    high, low, q = spectrum2(covariance)
    reconstructed_errors = [
        [v - dot(z, q) * axis for v, axis in zip(z, q)] for z in centered
    ]
    correlation = covariance[0][1] / math.sqrt(covariance[0][0] * covariance[1][1])
    chigh, clow, _ = spectrum2([[1, correlation], [correlation, 1]])
    add(
        12,
        mean_first=means[0],
        covariance=covariance[0][1],
        leading_eigenvalue=high,
        explained_fraction=high / sum(covariance[i][i] for i in (0, 1)),
        second_score=dot(centered[1], q),
        rank_one_error=norm([v for row in reconstructed_errors for v in row]),
        standardized_fraction=chigh / (chigh + clow),
    )
    inverse_poor_columns = [solve(poor, [1, 0]), solve(poor, [0, 1])]
    inverse_better_columns = [solve(improved, [1, 0]), solve(improved, [0, 1])]
    coordinate_sd = 0.01 * norm([col[0] for col in inverse_poor_columns])
    better_sd = 0.01 * norm([col[0] for col in inverse_better_columns])
    noisy = solve(poor, [4.98, 4.97])
    add(
        13,
        noisy_first=noisy[0],
        parameter_error=norm([noisy[0] - 2, noisy[1] - 3]),
        coordinate_sd=coordinate_sd,
        repeat_sd=1 / math.sqrt(25),
        offset_bias=solve(poor, [0, 0.01])[0],
        better_sd=better_sd,
    )
    _, estimates = sensor_rows()
    rmse = {
        g: math.sqrt(
            sum(dot([x[0] - 2, x[1] - 3], [x[0] - 2, x[1] - 3]) for x in vs) / len(vs)
        )
        for g, vs in estimates.items()
    }
    add(
        "lab-01",
        poor_rmse=rmse["poor"],
        improved_rmse=rmse["improved"],
        rmse_ratio=rmse["poor"] / rmse["improved"],
        predicted_weak_sd=0.01 / spectrum2(poor)[1],
    )
    return values


EXPECTED = expected_answers()


def test_every_package_numeric_key_is_recalculated():
    assert set(EXPECTED) == {qid for qid, q in BANK.items() if q["type"] == "numeric"}
    assert len(EXPECTED) == 69


@pytest.mark.parametrize("qid,value", sorted(EXPECTED.items()))
def test_numeric_key(qid, value):
    spec = BANK[qid]["solution_spec"]
    tolerance = spec["tolerance"] + spec.get("relative_tolerance", 0) * abs(
        spec["answer"]
    )
    assert abs(value - spec["answer"]) <= tolerance


def test_csv_summary_keys_recalculated_from_committed_signals():
    rows, estimates = sensor_rows()
    assert len(rows) == 10 and set(estimates) == {"poor", "improved"}
    checks = BANK["linear-algebra-lab-01:summary"]["solution_spec"]["validation_spec"][
        "checks"
    ]
    assert len(checks) == 4
    for check in checks:
        index = {"mean_x1": 0, "mean_x2": 1}[check["column"]]
        actual = [v[index] for v in estimates[check["row_id"]]]
        assert check["calculation"]["values"] == pytest.approx(actual, abs=1e-11)
        assert check["answer"] == pytest.approx(
            sum(actual) / len(actual), abs=check["tolerance"]
        )


def lesson_text(lid):
    manifest = load(COURSE / "course.json")
    lesson = next(
        record
        for m in manifest["modules"]
        for record in m["lessons"]
        if record["id"] == lid
    )
    return (COURSE / lesson["reading"]).read_text(encoding="utf-8")


def test_rank_solution_family_and_worked_example():
    a = [[1, 2, 3], [2, 4, 6], [1, 1, 2]]
    for t in [-4, -1 / 3, 0, 1, 7]:
        assert mv(a, [1 + t, 1 + t, 1 - t]) == pytest.approx([6, 12, 4])
    worked = [[1, 2, 1], [2, 4, 2], [3, 6, 3]]
    assert rank(worked) == 1
    for null in [[-2, 1, 0], [-1, 0, 1]]:
        assert mv(worked, null) == [0, 0, 0]
    assert rank([row + [rhs] for row, rhs in zip(a, [6, 11, 4])]) > rank(a)
    feedback = BANK["linear-algebra-7:rank-statements"]["feedback"]["solution"]
    assert "less likely" not in feedback and "column space" in feedback


def test_projection_and_triangular_worked_example():
    a, b = [2, 1, 2], [1, 4, 1]
    c = dot(a, b) / dot(a, a)
    residual = [v - c * u for u, v in zip(a, b)]
    assert dot(a, residual) == pytest.approx(0, abs=1e-12)
    text = lesson_text("linear-algebra-8")
    assert f"{c:.4f}" in text and f"{norm(residual):.4f}" in text
    assert solve([[3, 1], [0, 2]], [6, 4]) == pytest.approx([4 / 3, 2])
    assert "leaving measurement sensitivity unchanged" in text
    prompt = BANK["linear-algebra-8:intercept-by-qr"]["prompt"]
    assert "R = [[1.7321, 3.4641], [0, 1.4142]]" in prompt
    assert "Qᵀb = (2.8868, 0.7071)" in prompt


def test_spectral_quadrant_repeated_eigenvalues_and_worked_example():
    c = [[5, 2], [2, 2]]
    high, low, q = spectrum2(c)
    assert [high, low] == pytest.approx([6, 1])
    assert mv(c, q) == pytest.approx([high * v for v in q])
    text = lesson_text("linear-algebra-9")
    assert f"{math.degrees(math.atan2(q[1], q[0])):.2f}" in text
    assert "atan2" in text and "repeat" in text and "at 90°" in text
    theta = 0.5 * math.atan2(0, 1 - 3)
    axis = [math.cos(theta), math.sin(theta)]
    assert dot(axis, mv([[1, 0], [0, 3]], axis)) == pytest.approx(3)
    assert dot([0.6, 0.8], mv([[2, 0], [0, 2]], [0.6, 0.8])) == pytest.approx(2)


def test_svd_reconstruction_rectangular_zeros_and_storage():
    a = [[3, 1], [2, 2], [1, 3]]
    u = [[1 / math.sqrt(3)] * 3, [1 / math.sqrt(2), 0, -1 / math.sqrt(2)]]
    v = [[1 / math.sqrt(2)] * 2, [1 / math.sqrt(2), -1 / math.sqrt(2)]]
    sigmas = singular_values(a)
    for i in range(3):
        for j in range(2):
            assert sum(sigmas[k] * u[k][i] * v[k][j] for k in (0, 1)) == pytest.approx(
                a[i][j]
            )
    # AAᵀ has an additional zero mode, absent from the positive definite AᵀA.
    left_null = [1, -2, 1]
    assert mv(list(zip(*a)), left_null) == [0, 0]
    assert rank(a) == 2 and rank(gram(a)) == 2
    worked = [[1, 1], [1, -1], [2, 0]]
    assert singular_values(worked) == pytest.approx([math.sqrt(6), math.sqrt(2)])
    tiny = [[2, 2], [1, 1], [3, 3.1]]
    high, low = singular_values(tiny)
    text = lesson_text("linear-algebra-10")
    assert f"{high:.4f}" in text and f"{low:.4f}" in text
    assert "zero eigenvalue multiplicities can differ" in text
    assert "rectangular diagonal" in text and "reflections" in text
    assert 1 * (3 + 2 + 1) == 3 * 2
    assert "k(m + n + 1) < mn" in text


def test_conditioning_covariance_bias_and_validation_numbers():
    a, g = [[1, 0.99], [0.99, 1]], [[1, 0.2], [0.2, 1]]
    assert solve(a, [0.01, -0.01]) == pytest.approx([1, -1])
    assert solve(g, [0.01, -0.01]) == pytest.approx([0.0125, -0.0125])
    for matrix, expected in [(a, 0.014142), (g, 1.131371)]:
        separation = norm(
            [x - y for x, y in zip(mv(matrix, [2, 3]), mv(matrix, [3, 2]))]
        )
        assert separation == pytest.approx(expected, abs=1e-6)
        assert f"{expected:.6f}" in lesson_text("linear-algebra-13")
    bias = solve(a, [0, 0.01])
    assert mv(a, bias) == pytest.approx([0, 0.01])
    assert f"{bias[1]:.6f}" in lesson_text("linear-algebra-13")
    assert "deterministic error bounds, not confidence intervals" in lesson_text(
        "linear-algebra-11"
    )


def test_pca_centering_reconstruction_scaling_and_leakage():
    text = lesson_text("linear-algebra-12")
    for fragment in [
        "3.236068",
        "1.527864",
        "0.853553",
        "training samples only",
        "batch and treatment are confounded",
    ]:
        assert fragment in text
    # Unscaled diagonal covariance has a unique leading axis; correlation does not.
    assert spectrum2([[9, 0], [0, 1]])[0] == pytest.approx(9)
    assert gram([[1, 0], [0, 1]]) == [[1, 0], [0, 1]]
    assert "no unique leading axis" in text


def test_schedule_syllabus_and_partial_labels():
    c = load(COURSE / "course.json")
    weeks = c["duration"]["weeks"]
    lessons = {record["id"] for m in c["modules"] for record in m["lessons"]}
    assessment_ids = {a["id"] for a in c["assessments"]}
    scheduled = [lid for w in weeks for lid in w["lesson_ids"]]
    assert len(weeks) == 14 and len(scheduled) == len(set(scheduled)) == 14
    assert set(scheduled) == lessons
    assert {aid for w in weeks for aid in w["assessment_ids"]} <= assessment_ids
    assert weeks[12]["lesson_ids"] == ["linear-algebra-lab-01"]
    assert "linear-algebra-case" in weeks[13]["assessment_ids"]
    assert c["maturity"] == "partial" and c["review"]["status"] == "unreviewed"
    assert c["grading_policy"]["mode"] == "formative-only" and c["version"] == "0.3.0"
    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    assert all(o["description"] in syllabus for o in c["outcomes"])
    assert "Version: 0.3.0" in syllabus and "no instructor review" in lesson_text(
        "linear-algebra-13"
    )

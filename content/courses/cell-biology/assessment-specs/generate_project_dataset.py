"""Original deterministic synthetic project observations; no grading keys.

Run with Python 3: python generate_project_dataset.py --output DIRECTORY
Writes two fixed teaching forms, each 24 independent cultures x two times.
No random sampling, empirical calibration or biological mechanism is claimed.
"""

import argparse
import csv
from pathlib import Path

CONDITIONS = ("control", "signal_low", "signal_high", "matrix_high", "both", "rescue")
COLUMNS = (
    "form", "condition", "culture", "time_h", "seeded_cells", "viable_cells",
    "rna_signal_eq", "rna_background_eq", "spike_input_eq", "spike_recovered_eq",
    "protein_signal_ug", "protein_background_ug", "protein_recovery_fraction",
    "marker_positive_viable", "functional_events_viable", "perk_0_au", "perk_10_au",
    "perk_30_au", "matrix_modulus_pa", "accessible_ligand_relative",
)


def observations(form):
    """Each condition has four separately prepared cultures, measured twice."""
    offset = 2 if form == "B" else 0
    for ci, condition in enumerate(CONDITIONS):
        for i in range(1, 5):
            seeded = i * 10000
            culture = f"{form}-{condition}-{i:02}"
            for time in (0, 48):
                viable_fraction = (95 if time == 0 else (90, 85, 75, 80, 65, 85)[ci]) / 100
                viable = int(seeded * viable_fraction)
                rna_per_thousand = (100 if time == 0 else (100, 115, 140, 105, 155, 130)[ci]) + i * 3 + offset
                recovery = (70 + i * 5) / 100
                spike = 100 * recovery
                rna = rna_per_thousand * viable / 1000 * recovery + 20
                protein_per_thousand = (0.10 if time == 0 else (.10, .11, .13, .09, .12, .11)[ci]) + i * .002
                protein = protein_per_thousand * viable / 1000 * recovery + .005
                marker_pct = (10 if time == 0 else (12, 20, 38, 24, 55, 43)[ci]) + i + offset
                function_pct = (3 if time == 0 else (4, 5, 6, 4, 6, 5)[ci]) + i
                peak = (60, 70, 110, 65, 115, 100)[ci] + i * 2 + offset
                late = (20, 30, 60, 25, 70, 50)[ci] + i + offset
                yield (form, condition, culture, time, seeded, viable, round(rna, 6), 20,
                       100, spike, round(protein, 8), .005, recovery,
                       int(viable * marker_pct / 100), int(viable * function_pct / 100),
                       0, peak, late, 20000 if ci in (3, 4) else 5000,
                       3 if ci in (3, 4) else 2)


def write(output):
    output.mkdir(parents=True, exist_ok=True)
    path = output / "integrative-project-candidate-cultures.csv"
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(COLUMNS)
        for form in ("A", "B"):
            writer.writerows(observations(form))
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    print(write(parser.parse_args().output))

"""A synthetic, offline example of values and quality states. Standard library only."""

import argparse
import csv
import json
import math
from collections import Counter
from dataclasses import dataclass
from html import escape
from pathlib import Path


@dataclass(frozen=True)
class Sample:
    sample_id: str
    value: float | None
    status: str


def read_samples(path: Path) -> list[Sample]:
    """Reject ambiguous rows before producing any output."""
    samples = []
    seen_ids = set()
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != ["sample_id", "value", "status", "synthetic"]:
            raise ValueError("Expected columns: sample_id,value,status,synthetic")
        for line_number, row in enumerate(reader, start=2):
            if None in row or any(value is None for value in row.values()):
                raise ValueError(f"Line {line_number}: incomplete or extra columns")
            sample_id = row["sample_id"].strip()
            status = row["status"].strip()
            raw_value = row["value"].strip()
            if not sample_id or sample_id in seen_ids:
                raise ValueError(f"Line {line_number}: sample_id must be nonempty and unique")
            if row["synthetic"].strip() != "true":
                raise ValueError(f"Line {line_number}: this example accepts synthetic=true only")
            if status not in {"valid", "missing", "invalid"}:
                raise ValueError(f"Line {line_number}: unknown status {status!r}")
            if status == "missing" and raw_value:
                raise ValueError(f"Line {line_number}: a missing observation must have an empty value")
            if status == "valid" and not raw_value:
                raise ValueError(f"Line {line_number}: a valid observation needs a value")
            value = float(raw_value) if raw_value else None
            if value is not None and not math.isfinite(value):
                raise ValueError(f"Line {line_number}: numeric values must be finite")
            # Invalid values may be retained as evidence, but never enter the mean or plot.
            samples.append(Sample(sample_id, value, status))
            seen_ids.add(sample_id)
    if not samples or not any(sample.status == "valid" for sample in samples):
        raise ValueError("At least one valid synthetic observation is required")
    return samples


def summarise(samples: list[Sample]) -> dict:
    valid_values = [sample.value for sample in samples if sample.status == "valid"]
    counts = Counter(sample.status for sample in samples)
    valid_sum = sum(valid_values)
    return {
        "synthetic": True,
        "unit": "arbitrary demonstration units",
        "sample_count": len(samples),
        "status_counts": {status: counts[status] for status in ("valid", "missing", "invalid")},
        "valid_zero_count": sum(value == 0 for value in valid_values),
        "valid_only": {"count": len(valid_values), "sum": valid_sum, "mean": valid_sum / len(valid_values)},
        "deliberately_incorrect_zero_fill": {
            "description": "Force every non-valid row to zero, then divide by all rows; not a recommended treatment.",
            "count": len(samples),
            "sum": valid_sum,
            "mean": valid_sum / len(samples),
        },
        "samples": [
            {"sample_id": sample.sample_id, "retained_value": sample.value,
             "status": sample.status, "included_in_valid_mean": sample.status == "valid"}
            for sample in samples
        ],
        "limitation": "Synthetic arithmetic and display demonstration; no sensor or operational-system validation.",
    }


def make_figure(samples: list[Sample]) -> str:
    """Plot valid values only; use a separate rail for every sample's quality state."""
    width, height = 960, 460
    left, right, top, bottom = 100, 915, 100, 290
    values = [sample.value for sample in samples if sample.status == "valid"]
    low, high = min(0, min(values)), max(0, max(values))
    if low == high:
        high = low + 1
    x_step = (right - left) / max(1, len(samples) - 1)
    x_at = lambda index: left + index * x_step
    y_at = lambda value: bottom - (value - low) / (high - low) * (bottom - top)
    colors = {"valid": "#166534", "missing": "#1d4ed8", "invalid": "#b45309"}
    elements = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        '<title id="title">Synthetic values: valid zero, missing and invalid</title>',
        '<desc id="desc">Only valid observations appear on the value axis. Missing and invalid observations leave gaps. A separate status rail preserves all sample positions.</desc>',
        '<rect width="960" height="460" fill="#ffffff"/>',
        '<g font-family="Arial, sans-serif" font-size="14" fill="#172033">',
        '<text x="36" y="35" font-size="24" font-weight="bold">A value and its quality state answer different questions</text>',
        '<text x="36" y="62">All inputs are synthetic. No device readings or experimental results are shown.</text>',
        '<text x="28" y="200" transform="rotate(-90 28 200)">Value (arbitrary units)</text>',
    ]
    for tick_index in range(5):
        value = low + (high - low) * tick_index / 4
        y = y_at(value)
        elements.append(f'<line x1="{left}" y1="{y:.2f}" x2="{right}" y2="{y:.2f}" stroke="#e2e8f0"/>')
        elements.append(f'<text x="85" y="{y + 5:.2f}" text-anchor="end">{value:g}</text>')
    elements.append(f'<path d="M {left} {top} V {bottom} H {right}" fill="none" stroke="#64748b"/>')
    previous = None
    for index, sample in enumerate(samples):
        x = x_at(index)
        label = escape(sample.sample_id)
        elements.append(f'<text x="{x:.2f}" y="320" text-anchor="middle">{label}</text>')
        if sample.status == "valid":
            y = y_at(sample.value)
            if previous is not None:
                elements.append(f'<line x1="{previous[0]:.2f}" y1="{previous[1]:.2f}" x2="{x:.2f}" y2="{y:.2f}" stroke="#166534" stroke-width="2"/>')
            elements.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="6" fill="#166534"/>')
            previous = (x, y)
        else:
            # Break the line at a non-valid row instead of inventing a zero observation.
            previous = None
        color = colors[sample.status]
        elements.append(f'<rect x="{x - 6:.2f}" y="357" width="12" height="12" rx="2" fill="{color}"/>')
        elements.append(f'<text x="{x:.2f}" y="391" text-anchor="middle" fill="{color}">{sample.status.title()}</text>')
    elements.extend([
        '<text x="36" y="345" font-weight="bold">Quality state</text>',
        '<text x="36" y="434">Only adjacent valid samples are joined. Gaps are not plotted as zero.</text>',
        '</g></svg>',
    ])
    return "\n".join(elements) + "\n"


def main() -> None:
    example_dir = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=example_dir / "inputs.csv")
    parser.add_argument("--output", type=Path, default=example_dir / "generated")
    args = parser.parse_args()
    input_path, output_dir = args.input.resolve(), args.output.resolve()
    try:
        if output_dir == input_path.parent or output_dir == example_dir:
            raise ValueError("Choose an output subdirectory separate from the input and script directories")
        samples = read_samples(input_path)
        summary, figure = summarise(samples), make_figure(samples)
        output_dir.mkdir(parents=True, exist_ok=True)
        (output_dir / "summary.json").write_text(json.dumps(summary, indent=2, allow_nan=False) + "\n", encoding="utf-8")
        (output_dir / "validity-demo.svg").write_text(figure, encoding="utf-8")
    except (OSError, ValueError) as error:
        parser.error(str(error))
    print("Synthetic example complete: summary.json and validity-demo.svg")


if __name__ == "__main__":
    main()

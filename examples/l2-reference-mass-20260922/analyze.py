"""Reproduce descriptive calculations from a small transcribed laboratory record.

This script reads a local JSON file and writes a summary and figure. It has no
device, database, credential, or network integration.
"""

import argparse
import hashlib
import json
import math
import platform
from pathlib import Path
from statistics import mean, stdev

import matplotlib

matplotlib.use("Agg")  # Save figures without opening an interactive window.
import matplotlib.pyplot as plt


def load_groups(data_path):
    """Keep the two channels separate and reject ambiguous input rows."""
    raw_bytes = data_path.read_bytes()
    document = json.loads(raw_bytes)
    groups = {}
    seen = set()
    for row in document["readings"]:
        channel = row["channel"]
        index = row["reading_index"]
        if channel not in {"plant", "drainage"} or type(index) is not int or index < 1:
            raise ValueError("Expected a known channel and a positive reading index")
        if (channel, index) in seen:
            raise ValueError("Repeated channel/reading index")
        seen.add((channel, index))
        for field in ("nominal_g", "reported_g"):
            if type(row[field]) not in (int, float) or not math.isfinite(row[field]):
                raise ValueError("Mass fields must contain finite numbers")
        if row["nominal_g"] <= 0:
            raise ValueError("Nominal mass must be positive")
        groups.setdefault(channel, []).append(row)
    if set(groups) != {"plant", "drainage"}:
        raise ValueError("Both channels are required")
    for rows in groups.values():
        rows.sort(key=lambda row: row["reading_index"])
        if len(rows) < 2 or len({row["nominal_g"] for row in rows}) != 1:
            raise ValueError("Each group needs two readings at one nominal mass")
    return document, groups, hashlib.sha256(raw_bytes).hexdigest()


def summarize(groups):
    """Describe the listed values; do not infer uncertainty or pass/fail."""
    results = []
    for channel in ("plant", "drainage"):
        rows = groups[channel]
        nominal = rows[0]["nominal_g"]
        values = [row["reported_g"] for row in rows]
        average = mean(values)
        difference = average - nominal
        results.append({
            "channel": channel, "n": len(values), "nominal_g": nominal,
            "mean_g": average, "mean_minus_nominal_g": difference,
            "relative_mean_difference_percent": 100 * difference / nominal,
            "sample_sd_g": stdev(values),  # Uses the n - 1 denominator.
            "range_g": max(values) - min(values),
        })
    return results


def save_figure(groups, results, destination):
    """Plot individual differences on the same vertical scale, without a time axis."""
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.8), sharey=True)
    for ax, result in zip(axes, results):
        rows = groups[result["channel"]]
        x = [row["reading_index"] for row in rows]
        differences = [row["reported_g"] - row["nominal_g"] for row in rows]
        ax.axhline(0, color="#667085", linewidth=1)
        ax.axhline(result["mean_minus_nominal_g"], color="#b54708", linestyle="--",
                   label=f"Mean difference: {result['mean_minus_nominal_g']:+.3f} g")
        ax.scatter(x, differences, color="#175cd3", s=55, zorder=3)
        for index, difference in zip(x, differences):
            ax.annotate(f"{difference:+.3f}", (index, difference), xytext=(0, 9),
                        textcoords="offset points", ha="center", fontsize=9)
        ax.set(title=f"{result['channel'].title()} | nominal {result['nominal_g']:g} g",
               xticks=x, xlim=(0.5, max(x) + 0.5), ylim=(-4, 1))
        ax.set_xlabel("Recorded reading (listed order)")
        ax.grid(axis="y", alpha=0.2)
        ax.legend(loc="lower right", fontsize=8, frameon=False)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].set_ylabel("Reported mass - nominal mass (g)")
    fig.suptitle("L2 reference-mass record | 22 September 2026", fontsize=13)
    fig.text(0.5, 0.025, "Three transcribed readings per channel; independence and reference uncertainty not established.",
             ha="center", fontsize=8)
    fig.tight_layout(rect=(0, 0.07, 1, 0.94))
    fig.savefig(destination, dpi=180, metadata={"Software": "Matplotlib"})
    plt.close(fig)


def main():
    case_dir = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=case_dir / "reproduced")
    args = parser.parse_args()
    document, groups, data_hash = load_groups(case_dir / "readings.json")
    results = summarize(groups)
    args.output.mkdir(parents=True, exist_ok=True)
    summary = {"record_date": document["record_date"], "data_kind": document["data_kind"],
               "data_sha256": data_hash, "runtime": {"python": platform.python_version(),
               "matplotlib": matplotlib.__version__}, "results": results}
    (args.output / "summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    save_figure(groups, results, args.output / "deviations.png")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()

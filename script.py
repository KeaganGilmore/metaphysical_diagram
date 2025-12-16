# python
import json
import textwrap
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# --- helpers ---
def wrap(text, width):
    if not text:
        return ""
    return textwrap.fill(text, width=width, replace_whitespace=False)

def abbreviate(text, max_len):
    if not text:
        return ""
    text = text.strip()
    return (text[: max_len - 1] + "…") if len(text) > max_len else text

def build_axis_colors(axes_def):
    palette = [
        "#1f77b4", "#2ca02c", "#d62728", "#9467bd", "#8c564b",
        "#17becf", "#e377c2", "#bcbd22", "#7f7f7f", "#ff7f0e"
    ]
    mapping = {}
    for i, a in enumerate(axes_def or []):
        axis_name = a.get("axis", f"Axis {i+1}")
        mapping[axis_name] = palette[i % len(palette)]
    return mapping

# --- main ---
def generate_timeline_compact(json_path):
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: {json_path} not found.")
        return

    phases = data.get("time_phases", [])
    if not phases:
        print("No time phases found in data.")
        return

    axes_def = data.get("axes_definition", [])
    axis_colors = build_axis_colors(axes_def)

    # Compact layout sizing
    n = len(phases)
    fig_width = max(10, n * 2.6)
    fig_height = 4.6
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))
    ax.axis("off")

    # Timeline baseline
    left, right = 0.5, n - 0.5
    ax.plot([left, right], [0, 0], color="#444444", linewidth=2)

    # Layout constants
    card_y = 0.35
    y_limits = 0.9
    card_box = dict(boxstyle="round,pad=0.5,rounding_size=0.5",
                    fc="#ffffff", ec="#cfd8dc", linewidth=1.2, alpha=0.99)

    # Draw each phase as a concise card
    for i, phase in enumerate(phases):
        x = i + 0.5
        title = phase.get("phase", "Unknown")
        date_range = phase.get("date_range", "")

        # Pick top 2 values (labels only), abbreviated
        values = phase.get("dominant_values", []) or []
        top_values = []
        for v in values[:2]:
            label = abbreviate((v.get("value") or "").strip(), 24)
            if label:
                top_values.append((label, (v.get("axis") or "").strip()))
        # Fallback if no values present
        if not top_values:
            top_values = [("N/A", "")]

        # Minimal text body
        header = wrap(title, 22)
        dates = f"({date_range})" if date_range else ""
        vals_line = "; ".join([t[0] for t in top_values])

        full_text = f"{header}\n{dates}\n{wrap(vals_line, 26)}"

        # Marker color uses first value's axis color for a subtle cue
        first_axis = top_values[0][1] if top_values else ""
        marker_color = axis_colors.get(first_axis, "#2c3e50")

        # Timeline marker and short connector
        ax.scatter(x, 0, s=120, color=marker_color, zorder=3, edgecolors="white", linewidth=1.0)
        ax.plot([x, x], [0.04, card_y * 0.78], color="#90a4ae", linestyle="-", linewidth=1)

        # Card
        ax.text(
            x, card_y, full_text,
            ha="center", va="bottom",
            fontsize=9.5, family="sans-serif", linespacing=1.1,
            bbox=card_box, zorder=4
        )

    # Limits and title
    ax.set_xlim(0, n)
    ax.set_ylim(-y_limits, y_limits)

    model_name = data.get("model_name", "Timeline")
    fig.suptitle(model_name, fontsize=14, weight="bold", color="#263238", y=0.98)

    # Tight layout, small margins
    plt.tight_layout(rect=[0.02, 0.02, 0.98, 0.94])

    out = "timeline_compact.png"
    plt.savefig(out, dpi=300, bbox_inches="tight")
    print(f"Successfully generated diagram: {out}")

if __name__ == "__main__":
    # Reads `data.json` and outputs `timeline_compact.png`
    generate_timeline_compact("data.json")
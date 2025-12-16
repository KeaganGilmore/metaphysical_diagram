# Metaphysical Diagram

An experimental visualization tool for exploring complex timelines and value shifts across multiple conceptual axes.

> **Utilization notice**  
> The underlying research and model structure are the work of the author. For reuse, extensions, or other forms of utilization beyond personal/local experimentation, please contact **keagangilmore@gmail.com**.

This project provides two complementary ways to visualize your data from a single `data.json` file:

- **Interactive web timeline** (`index.html`) – rich, scrolling, multi-axis diagram rendered in the browser.
- **Static compact diagram** (`timeline_compact.png`) – generated via `script.py` using Matplotlib.

---

## Project Structure

- `index.html` – Interactive timeline visualization powered by HTML/CSS/JavaScript. It renders phases and axes defined in `data.json` and draws connections between them on a canvas.
- `data.json` – Your data model. Defines axes, time phases, dominant values, and related metadata.
- `script.py` – Python script that reads `data.json` and generates a compact PNG timeline (`timeline_compact.png`).
- `timeline_compact.png` – Output image produced by `script.py`.
- `DONATIONS.md` – Information on how to support the project author.
- `package.json` – Minimal Node metadata (not required for running the visualizations).

---

## Data Format (`data.json`)

`data.json` is expected to have the following high-level structure:

```jsonc
{
  "model_name": "My Timeline Model",
  "axes_definition": [
    {
      "axis": "Example Axis",
      "description": "What this axis represents",
      "disciplines": ["philosophy", "history"]
    }
  ],
  "time_phases": [
    {
      "phase": "Phase name",
      "date_range": "2000–2024",
      "dominant_conditions": ["optional list of conditions"],
      "dominant_values": [
        {
          "axis": "Example Axis",
          "value": "Value / state in this phase",
          "description": "Short explanation of the value in this phase"
        }
      ],
      "value_shift_summary": "Optional textual summary of how values change here",
      "evidence": ["citations or sources"],
      "notes_on_limitations": ["caveats and uncertainties"]
    }
  ]
}
```

The **axes** listed in `axes_definition` are used as rows in the visualizations, and each **time phase** becomes a column on the timeline.

If `data.json` cannot be loaded in the browser, `index.html` will fall back to a minimal built-in sample model so that the page still renders.

---

## Running the Interactive Timeline (Browser)

1. Ensure `index.html` and `data.json` are in the same directory.
2. Open `index.html` directly in a modern browser (Chrome, Edge, Firefox).
   - On some browsers, loading local JSON via `fetch` is blocked by default. If you see errors about `data.json` not loading, you have two options:
     - Serve the folder with a simple local web server (recommended), or
     - Rely on the built-in sample data.

### Option A: Run with a simple local server (recommended)

From the project directory:

- **Using Python 3**:
  - `python -m http.server 8000`
  - Visit `http://localhost:8000/index.html` in your browser.

Now the page will fetch `data.json` correctly and render your full model.

---

## Generating the Compact Diagram (Python)

`script.py` reads `data.json` and generates `timeline_compact.png`.

### Requirements

- Python 3.8+
- `matplotlib`

Install dependencies (for example):

```bash
pip install matplotlib
```

### Usage

From the project directory:

```bash
python script.py
```

This will:

1. Read `data.json` in the current directory.
2. Render a compact horizontal timeline where each phase is a card positioned along a central line.
3. Save the image as `timeline_compact.png`.

If `data.json` is missing or malformed, the script will print an error and exit.

---

## Customizing the Visualizations

### In the browser (`index.html`)

- **Styling**: All appearance (colors, spacing, typography, animations) is defined in the `<style>` block near the top. You can tweak gradients, card layouts, and axis colors there.
- **Legend & axes**: The legend is auto-generated from `axes_definition` and shows one color per axis.
- **Interactivity**: The JS currently generates cards from `data.json` and draws connective lines on a canvas. You can extend it with tooltips, filters, or additional metadata.

### In Python (`script.py`)

You can adjust:

- Figure size, margins, and DPI for `timeline_compact.png`.
- Number of dominant values displayed per phase (default: top 2).
- Text wrapping and maximum label length.
- Color palette mapped to axes in `build_axis_colors`.

---

## Contributions & Support

Issues, suggestions, and improvements are welcome.

If you find this project useful and want to support ongoing development, see `DONATIONS.md` for donation links and contact details.

For utilization of the research model, academic or commercial reuse, or collaboration inquiries, contact: **keagangilmore@gmail.com**.

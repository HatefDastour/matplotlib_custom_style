"""
mizzou_example.py
-----------------
Demonstration of the Mizzou Matplotlib style and colormaps.

Run this script to see all three Mizzou colormap types in action together
with the mizzou.mplstyle visual identity.

Usage
-----
    python examples/mizzou_example.py
"""

import sys
import os

import numpy as np
import matplotlib.pyplot as plt

# Allow running from repo root or from the examples/ directory
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from mizzou_colormaps import mu_categorical, mu_sequential, mu_diverging, register_mizzou_colormaps

# Register colormaps so they can be referenced by name
register_mizzou_colormaps()

# Apply the Mizzou mplstyle (load from the repo root)
style_path = os.path.join(os.path.dirname(__file__), "..", "mizzou.mplstyle")
plt.style.use(os.path.abspath(style_path))

rng = np.random.default_rng(42)

# ---------------------------------------------------------------------------
# Sample data
# ---------------------------------------------------------------------------
heatmap_data = rng.random((10, 10))
diverging_data = heatmap_data - 0.5          # centered on zero

categories = ["A", "B", "C", "D", "E"]
values = [10, 24, 15, 18, 5]

x = np.linspace(0, 10, 200)
line_data = {
    "sin(x)":   np.sin(x),
    "cos(x)":   np.cos(x),
    "sin(2x)":  np.sin(2 * x),
    "cos(2x)":  np.cos(2 * x),
    "sin(x/2)": np.sin(x / 2),
}

# ---------------------------------------------------------------------------
# Figure layout: 2 rows × 3 columns
# ---------------------------------------------------------------------------
fig, axs = plt.subplots(2, 3, figsize=(15, 9))
fig.suptitle(
    "University of Missouri — Data Visualization Palette Demo",
    fontsize=16,
    fontweight="bold",
)

# ── Row 1: colormaps ──────────────────────────────────────────────────────

# Sequential heatmap
im0 = axs[0, 0].imshow(heatmap_data, cmap=mu_sequential, aspect="auto")
axs[0, 0].set_title("Sequential (Limestone → Gold)")
fig.colorbar(im0, ax=axs[0, 0])

# Diverging heatmap
im1 = axs[0, 1].imshow(diverging_data, cmap=mu_diverging, aspect="auto")
axs[0, 1].set_title("Diverging (Botanic ↔ Sunrise)")
fig.colorbar(im1, ax=axs[0, 1])

# Categorical bar chart
bars = axs[0, 2].bar(categories, values, color=mu_categorical.colors)
axs[0, 2].set_title("Categorical (5-color safe palette)")
axs[0, 2].set_xlabel("Category")
axs[0, 2].set_ylabel("Value")

# ── Row 2: line chart, colorbar swatches, accessibility note ─────────────

# Line chart — uses the same categorical colors via the prop_cycle in mizzou.mplstyle
for label, y in line_data.items():
    axs[1, 0].plot(x, y, label=label)
axs[1, 0].set_title("Line Chart (prop_cycle from mizzou.mplstyle)")
axs[1, 0].set_xlabel("x")
axs[1, 0].set_ylabel("y")
axs[1, 0].legend()

# Color swatch strip (categorical palette)
swatch_ax = axs[1, 1]
swatch_ax.set_xlim(0, len(mu_categorical.colors))
swatch_ax.set_ylim(0, 1)
swatch_ax.set_title("Categorical Palette Swatches")
swatch_ax.axis("off")
color_names = [
    "Mizzou Gold\n#FDB719",
    "Tiger Paw Black\n#000000",
    "Botanic Tint\n#99CECF",
    "Slate\n#4A596E",
    "Sunrise Shade\n#993429",
]
for i, (color, name) in enumerate(zip(mu_categorical.colors, color_names)):
    swatch_ax.add_patch(plt.Rectangle((i, 0), 1, 1, color=color))
    text_color = "white" if color in ("#000000", "#4A596E", "#993429") else "black"
    swatch_ax.text(
        i + 0.5, 0.5, name,
        ha="center", va="center",
        fontsize=8, color=text_color,
    )

# Accessibility notes
note_ax = axs[1, 2]
note_ax.axis("off")
note_ax.set_title("Accessibility Notes")
notes = (
    "Text Contrast:\n"
    "  • Black text on light backgrounds\n"
    "    (Limestone, Gold, White)\n"
    "  • White text on dark backgrounds\n"
    "    (Black, Slate, Botanic Shade)\n\n"
    "Color-Blind Safety:\n"
    "  • First 4 categorical colors are SAFE\n"
    "    for protanopia, deuteranopia,\n"
    "    and tritanopia\n\n"
    "Avoid Pairing:\n"
    "  • Mizzou Gold + Sunrise Shade\n"
    "    (POOR contrast in categorical charts)"
)
note_ax.text(
    0.05, 0.95, notes,
    transform=note_ax.transAxes,
    va="top", ha="left",
    fontsize=9,
    family="monospace",
)

plt.tight_layout()
plt.savefig(
    os.path.join(os.path.dirname(__file__), "mizzou_example.pdf"),
    bbox_inches="tight",
)
plt.show()

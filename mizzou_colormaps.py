"""
mizzou_colormaps.py
-------------------
Matplotlib colormaps derived from the University of Missouri (Mizzou)
Data Visualization Brand Guidelines.

Reference: https://udair.missouri.edu/data-visualization-style-guidelines/

Three colormap types are provided:

* **Categorical** – for distinct, unordered groups (up to 5 color-blind-safe colors).
* **Sequential** – for data ranging from low to high, built around Mizzou Gold.
* **Diverging**  – for data that deviates from a meaningful midpoint, using
                   Botanic Shade (cool) → Limestone (neutral) → Sunrise Shade (warm).

Quick start
-----------
    from mizzou_colormaps import register_mizzou_colormaps
    register_mizzou_colormaps()

    import matplotlib.pyplot as plt
    import numpy as np

    data = np.random.rand(10, 10)
    plt.imshow(data, cmap="MizzouSequential")
    plt.colorbar()
    plt.show()

Or import the colormap objects directly:

    from mizzou_colormaps import mu_categorical, mu_sequential, mu_diverging
"""

from matplotlib.colors import LinearSegmentedColormap, ListedColormap
import matplotlib as mpl

# ---------------------------------------------------------------------------
# MU brand colors
# ---------------------------------------------------------------------------
mizzou_colors = {
    "tiger_paw_black": "#000000",
    "mizzou_gold":     "#FDB719",
    "limestone":       "#D4D4D4",
    "botanic_tint":    "#99CECF",
    "slate":           "#4A596E",
    "mulberry_shade":  "#370013",
    "botanic_shade":   "#004243",
    "sunrise_shade":   "#993429",
}

# ---------------------------------------------------------------------------
# Categorical colormap
# ---------------------------------------------------------------------------
# Colors are ordered for maximum color-blind safety (protanopia / deuteranopia /
# tritanopia).  The first four form the verified "SAFE" pairing set from the
# MU Color Compatibility Matrix; Sunrise Shade is added as the fifth option.
_categorical_colors = [
    mizzou_colors["mizzou_gold"],
    mizzou_colors["tiger_paw_black"],
    mizzou_colors["botanic_tint"],
    mizzou_colors["slate"],
    mizzou_colors["sunrise_shade"],
]
mu_categorical = ListedColormap(_categorical_colors, name="MizzouCategorical")

# ---------------------------------------------------------------------------
# Sequential colormap
# ---------------------------------------------------------------------------
# Progresses from Limestone (light neutral) → Mizzou Gold → deep gold,
# following the brand guideline that sequential scales should move from
# light to dark around the primary MU Gold color.
_sequential_stops = [
    mizzou_colors["limestone"],   # light end
    mizzou_colors["mizzou_gold"], # midpoint / brand anchor
    "#B8860B",                    # deep gold for high-end contrast
]
mu_sequential = LinearSegmentedColormap.from_list(
    "MizzouSequential", _sequential_stops
)

# ---------------------------------------------------------------------------
# Diverging colormap
# ---------------------------------------------------------------------------
# Botanic Shade (cool, dark teal) ← Limestone (neutral midpoint) → Sunrise Shade
# (warm, dark red).  Matches the MU diverging palette described in the guide.
_diverging_stops = [
    mizzou_colors["botanic_shade"],  # cool end
    mizzou_colors["limestone"],      # neutral midpoint
    mizzou_colors["sunrise_shade"],  # warm end
]
mu_diverging = LinearSegmentedColormap.from_list(
    "MizzouDiverging", _diverging_stops
)

# ---------------------------------------------------------------------------
# Registration helper
# ---------------------------------------------------------------------------
_COLORMAPS = [mu_categorical, mu_sequential, mu_diverging]


def register_mizzou_colormaps(override: bool = False) -> None:
    """Register all Mizzou colormaps with Matplotlib.

    After calling this function the colormaps are available by name in any
    Matplotlib call that accepts a ``cmap`` argument::

        plt.imshow(data, cmap="MizzouSequential")
        plt.imshow(data, cmap="MizzouDiverging")

    Parameters
    ----------
    override:
        If *True*, re-register colormaps even when they are already registered.
        Defaults to *False*.
    """
    for cmap in _COLORMAPS:
        if override or cmap.name not in mpl.colormaps:
            mpl.colormaps.register(cmap, force=override)

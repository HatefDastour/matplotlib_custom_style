# matplotlib_custom_style

A professional, customizable Matplotlib style sheet for consistent, publication-quality plots across platforms.

## Features

- **Enhanced grid visibility** for improved readability
- **Clear, bold axis titles and labels**
- **Readable font sizes** for all plot elements
- **Modern sans-serif font stack**: Prioritizes Arial, with robust cross-platform fallbacks (Helvetica, DejaVu Sans, Liberation Sans)
- **Optimized color palette** for print and digital media
- **Consistent marker and line widths** for visual clarity

## Font Compatibility

This style prioritizes Arial for a clean, modern look. If Arial is unavailable (e.g., on some Linux systems), it gracefully falls back to other widely available sans-serif fonts, ensuring consistent appearance on Windows, macOS, and Linux.

## Usage

### 1. Use Directly from GitHub

Apply the style directly in your Python scripts:

```
import matplotlib.pyplot as plt

plt.style.use("https://raw.githubusercontent.com/HatefDastour/matplotlib_custom_style/main/custom_style.mplstyle")
```

### 2. Use Locally

Download `custom_style.mplstyle` and reference its path:

```
import matplotlib.pyplot as plt

plt.style.use("path/to/custom_style.mplstyle")
```

### 3. Example

See [`examples/example_plot.py`](examples/example_plot.py) for a demonstration of this style in action.

## Style Details

- **Line width:** 1
- **Marker size:** 8
- **Axis label size:** 14
- **Tick label size:** 12
- **Title size:** 14, bold
- **Grid:** Gray, dashed, alpha 0.8
- **Font stack:** Arial, Helvetica, DejaVu Sans, Liberation Sans, sans-serif

## Contributing

Contributions to improve or extend this style are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
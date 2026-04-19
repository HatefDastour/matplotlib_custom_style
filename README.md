# Matplotlib Custom Style

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg?style=flat-square)](https://www.python.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.0%2B-orange.svg?style=flat-square)](https://matplotlib.org/)

A collection of professional, customizable Matplotlib style sheets for creating consistent, publication-quality plots across all platforms.

---

## ✨ Available Styles

### 1. `custom_style.mplstyle`

A clean, general-purpose style for everyday plotting with enhanced readability.

| Element | Value |
|---------|-------|
| **Line Width** | 1.0 |
| **Marker Size** | 8 |
| **Axis Label Size** | 14 pt |
| **Tick Label Size** | 12 pt |
| **Title Size** | 14 pt (bold) |
| **Grid Style** | Gray, dashed, alpha 0.8 |
| **Font Family** | Arial, Helvetica, DejaVu Sans, Liberation Sans |

### 2. `scientific.mplstyle`

A professional academic style optimized for scientific publications (e.g., Nature/Science journals). Features a color-blind safe (Wong) palette, clean open spines, and high-DPI PDF export.

| Element | Value |
|---------|-------|
| **Line Width** | 1.5 |
| **Marker Size** | 6 |
| **Axis Label Size** | 12 pt |
| **Tick Label Size** | 10 pt |
| **Title Size** | 14 pt (bold) |
| **Grid Style** | Gray, dashed, alpha 0.3 |
| **Spines** | Top & right removed |
| **Color Palette** | Wong color-blind safe (6 colors) |
| **Save DPI** | 220 (PDF vector format) |
| **Font Family** | Arial, Helvetica, DejaVu Sans, Liberation Sans |

---

## 🚀 Quick Start

### Method 1: Direct from GitHub (Recommended)

```python
import matplotlib.pyplot as plt

# ── General-purpose style ──
plt.style.use("https://raw.githubusercontent.com/HatefDastour/matplotlib_custom_style/main/custom_style.mplstyle")
# or via short URL
plt.style.use("https://tinyurl.com/mplstyle")

# ── Scientific / publication style ──
plt.style.use("https://raw.githubusercontent.com/HatefDastour/matplotlib_custom_style/main/scientific.mplstyle")
# or via short URL
plt.style.use("https://tinyurl.com/sci-mplstyle")

# Create your plot
plt.plot([1, 2, 3], [1, 4, 9])
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('My Plot')
plt.show()
```

### Method 2: Local Installation

```bash
# Download the style file(s)
wget https://raw.githubusercontent.com/HatefDastour/matplotlib_custom_style/main/custom_style.mplstyle
wget https://raw.githubusercontent.com/HatefDastour/matplotlib_custom_style/main/scientific.mplstyle
```

```python
import matplotlib.pyplot as plt

# Use local style file
plt.style.use("path/to/custom_style.mplstyle")
# or
plt.style.use("path/to/scientific.mplstyle")
```

### Method 3: Install in Matplotlib Config

```bash
# Find your matplotlib config directory
python -c "import matplotlib; print(matplotlib.get_configdir())"

# Copy the style file(s) to stylelib directory
cp custom_style.mplstyle <config_dir>/stylelib/
cp scientific.mplstyle  <config_dir>/stylelib/
```

```python
import matplotlib.pyplot as plt

# Use by name after installation
plt.style.use('custom_style')
# or
plt.style.use('scientific')
```

---

## 💻 Example

See the complete demonstration in [`examples/example_plot.py`](examples/example_plot.py).

```python
import matplotlib.pyplot as plt
import numpy as np

# Apply scientific style
plt.style.use("https://tinyurl.com/sci-mplstyle")

# Generate data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create plot
plt.figure(figsize=(9.5, 4.5))
plt.plot(x, y1, label='sin(x)')
plt.plot(x, y2, label='cos(x)')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Trigonometric Functions')
plt.legend()
plt.show()
```

---

## 🖥️ Font Compatibility

Both styles prioritize **Arial** for a clean, modern appearance. If Arial is unavailable (common on some Linux distributions), they automatically fall back to other widely available sans-serif fonts:

1. **Arial** (primary)
2. **Helvetica** (macOS)
3. **DejaVu Sans** (Linux)
4. **Liberation Sans** (Linux)
5. **sans-serif** (system default)

This ensures consistent appearance across Windows, macOS, and Linux platforms.

---

## 📁 Repository Structure

```plaintext
matplotlib_custom_style/
├── custom_style.mplstyle   # General-purpose style
├── scientific.mplstyle     # Academic / publication style
├── examples/               # Example scripts
│   └── example_plot.py     # Demonstration script
├── LICENSE                 # MIT License
└── README.md               # This file
```

---

## 🤝 Contributing

Contributions to improve or extend this style are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📧 Contact

**Dr. Hatef Dastour**  
University of Missouri, Columbia

- 🌐 **Website:** [hatefdastour.github.io](https://hatefdastour.github.io/)
- 🐙 **GitHub:** [@HatefDastour](https://github.com/HatefDastour)


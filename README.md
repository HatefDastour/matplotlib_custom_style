# Matplotlib Custom Style

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg?style=flat-square)](https://www.python.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.0%2B-orange.svg?style=flat-square)](https://matplotlib.org/)

A professional, customizable Matplotlib style sheet for creating consistent, publication-quality plots across all platforms.

---

## ✨ Features

- 📈 **Enhanced grid visibility** for improved readability
- 🔤 **Clear, bold axis titles and labels**
- 📝 **Readable font sizes** for all plot elements
- 🔤 **Modern sans-serif font stack**: Arial with cross-platform fallbacks
- 🎨 **Optimized color palette** for print and digital media
- 📊 **Consistent styling** for markers, lines, and visual elements

---

## 🚀 Quick Start

### Method 1: Direct from GitHub (Recommended)

```python
import matplotlib.pyplot as plt

# Apply the custom style
plt.style.use("https://raw.githubusercontent.com/HatefDastour/matplotlib_custom_style/main/custom_style.mplstyle")

# Create your plot
plt.plot([1, 2, 3], [1, 4, 9])
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('My Plot')
plt.show()
```

### Method 2: Local Installation

```bash
# Download the style file
wget https://raw.githubusercontent.com/HatefDastour/matplotlib_custom_style/main/custom_style.mplstyle
```

```python
import matplotlib.pyplot as plt

# Use local style file
plt.style.use("path/to/custom_style.mplstyle")
```

### Method 3: Install in Matplotlib Config

```bash
# Find your matplotlib config directory
python -c "import matplotlib; print(matplotlib.get_configdir())"

# Copy the style file to stylelib directory
cp custom_style.mplstyle <config_dir>/stylelib/
```

```python
import matplotlib.pyplot as plt

# Use by name after installation
plt.style.use('custom_style')
```

---

## 🎨 Style Specifications

| Element | Value |
|---------|-------|
| **Line Width** | 1.0 |
| **Marker Size** | 8 |
| **Axis Label Size** | 14 pt |
| **Tick Label Size** | 12 pt |
| **Title Size** | 14 pt (bold) |
| **Grid Style** | Gray, dashed, alpha 0.8 |
| **Font Family** | Arial, Helvetica, DejaVu Sans, Liberation Sans |

---

## 💻 Example

See the complete demonstration in [`examples/example_plot.py`](examples/example_plot.py).

```python
import matplotlib.pyplot as plt
import numpy as np

# Apply custom style
plt.style.use("https://raw.githubusercontent.com/HatefDastour/matplotlib_custom_style/main/custom_style.mplstyle")

# Generate data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create plot
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='sin(x)')
plt.plot(x, y2, label='cos(x)')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Trigonometric Functions')
plt.legend()
plt.grid(True)
plt.show()
```

---

## 🖥️ Font Compatibility

This style prioritizes **Arial** for a clean, modern appearance. If Arial is unavailable (common on some Linux distributions), it automatically falls back to other widely available sans-serif fonts:

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
├── custom_style.mplstyle   # Main style file
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

---

<div align="center">

Made with ❤️ for better data visualization

</div>
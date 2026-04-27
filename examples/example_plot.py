import os

import matplotlib.pyplot as plt
import numpy as np

plt.style.use("https://raw.githubusercontent.com/HatefDastour/matplotlib_custom_style/main/custom_style.mplstyle")

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y, marker='o', label='sin(x)')
plt.title("Example Plot with Custom Style")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.legend(title="Legend")

plt.savefig(
    os.path.join(os.path.dirname(__file__), "basic_example.pdf"),
    bbox_inches="tight",
)
plt.show()
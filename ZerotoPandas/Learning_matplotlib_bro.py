# Matplotlib

import matplotlib.pyplot as plt
import numpy as np


# Intro

# print(matplotlib.__version__)
# x = [2023, 2024, 2025, 2026]
# x = np.array([2023, 2024, 2025, 2026]) # arrays are faster
# # y = [15, 25, 30, 20]
# y = np.array([15, 25, 30, 20])

# plt.plot(x, y)

# plt.show()


# Plot customization
# Markers, there is a list of markers that can be used in the documentation

year = np.array([2022, 2023, 2024, 2025, 2026])
subjects = np.array([16, 24, 20, 13, 35])

plt.plot(year, subjects, marker=".",
                         markersize=20, # marker-size can be used as ms
                         markerfacecolor="#007AFF", # marker-face-color can be used as mfc
                         markeredgecolor="#007AFF", # marker-edge-color can be used as med
                         linestyle="dashed",
                         linewidth=3,
                         color="#000")

plt.show()

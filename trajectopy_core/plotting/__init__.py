import os

import matplotlib.pyplot as plt

plt.rcParams["figure.max_open_warning"] = 50

base_path = os.path.join(os.path.dirname(__file__))
MPL_STYLE_PATH = os.path.join(base_path, "default.mplstyle")
plt.style.use(MPL_STYLE_PATH)

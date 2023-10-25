import matplotlib.pyplot as plt

from trajectopy_core.util.path import mplstyle_file_path

plt.rcParams["figure.max_open_warning"] = 50
plt.style.use(mplstyle_file_path())

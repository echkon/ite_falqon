import pandas as pd
import matplotlib.pyplot as plt
import os
import glob
import re
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

here = os.path.dirname(__file__)

file_list = glob.glob(os.path.join(here, "data_*.csv"))

grids = set()
for f in file_list:
    base = os.path.basename(f)
    m = re.search(r'data_\((\d+)x(\d+)\)', base)
    if m:
        grids.add((int(m.group(1)), int(m.group(2))))

grids = sorted(grids)
cmap = plt.colormaps['tab10']
colors = cmap(np.linspace(0, 1, len(grids)))

color_map = {
    grid: colors[i] for i, grid in enumerate(grids)
}

fig, ax = plt.subplots(figsize=(12, 8))

for file_path in file_list:
    df = pd.read_csv(file_path, comment='#')
    base = os.path.basename(file_path)

    match = re.search(r'data_\((\d+)x(\d+)\)_(\d+)_(\d+)', base)
    if not match:
        continue

    nx, ny = int(match.group(1)), int(match.group(2))
    n_up, n_dn = int(match.group(3)), int(match.group(4))

    half_filled = (nx * ny) == (n_up + n_dn)
    linestyle = '-' if half_filled else '--'
    color = color_map[(nx, ny)]

    ax.plot(
        df['time'],
        df['beta'],
        color=color,
        linestyle=linestyle,
        linewidth=3,
        label=f"[{nx}x{ny}] ({n_up},{n_dn})"
    )

ax.set_xscale('log')
ax.set_xlabel('t', fontsize=16)
ax.set_ylabel('β(t)', fontsize=16)
ax.grid(True, which='major', linewidth=2)
ax.tick_params(labelsize=14)

ax_inset = inset_axes(
    ax,
    width="40%",
    height="40%",
    loc="upper right",
    borderpad=2
)

inset_order = [(2, 2), (1, 3)]

for grid in inset_order:
    nx, ny = grid

    for file_path in file_list:
        df = pd.read_csv(file_path, comment='#')
        base = os.path.basename(file_path)

        match = re.search(r'data_\((\d+)x(\d+)\)_(\d+)_(\d+)', base)
        if not match:
            continue

        fx, fy = int(match.group(1)), int(match.group(2))
        n_up, n_dn = int(match.group(3)), int(match.group(4))

        if (fx, fy) != (nx, ny):
            continue

        if (fx * fy) != (n_up + n_dn):
            continue

        ax_inset.plot(
            df['time'],
            df['beta'],
            color=color_map[(fx, fy)],
            linewidth=2
        )

ax_inset.set_xscale('log')
ax_inset.set_xlim(1e2, 1e3)
ax_inset.set_ylim(-0.02, 0.02)
ax_inset.tick_params(labelsize=14)
ax_inset.minorticks_off()

ax.legend(loc='lower left', fontsize=14)
plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import os
import glob
import re
import numpy as np

here = os.path.dirname(__file__)

file_list = glob.glob(os.path.join(here, "data_*.csv"))

# Lấy danh sách các grid khác nhau
grids = set()
for f in file_list:
    base = os.path.basename(f)
    m = re.search(r'data_\((\d+)x(\d+)\)', base)
    if m:
        grids.add((int(m.group(1)), int(m.group(2))))

grids = sorted(grids)

# Gán màu cho mỗi grid
cmap = plt.colormaps['tab10']
colors = cmap(np.linspace(0, 1, len(grids)))

color_map = {
    grid: colors[i] for i, grid in enumerate(grids)
}


plt.figure(figsize=(12, 8))

for file_path in file_list:
    df = pd.read_csv(file_path, comment='#')
    base = os.path.basename(file_path)

    match = re.search(r'data_\((\d+)x(\d+)\)_(\d+)_(\d+)', base)
    if not match:
        continue

    nx, ny = int(match.group(1)), int(match.group(2))
    n_up, n_dn = int(match.group(3)), int(match.group(4))

    # Half-filled condition (chuẩn Hubbard)
    half_filled = (nx * ny) == (n_up + n_dn)

    linestyle = '-' if half_filled else '--'
    color = color_map[(nx, ny)]

    label = f"[{nx}x{ny}] ({n_up},{n_dn})"

    plt.plot(
        df['time'],
        (df['energy_diff']),
        color=color,
        linestyle=linestyle,
        linewidth=3,
        label=label
    )

plt.xscale('log')
plt.yscale('log')
plt.xlabel('t', fontsize=16)
plt.ylabel('ΔE(t)', fontsize=16)
plt.legend(fontsize=14)
plt.grid(True, which='major', linewidth=2)
plt.tick_params(axis='both', labelsize=14)
plt.tight_layout()
plt.show()

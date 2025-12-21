from matplotlib import pyplot as plt
import pandas as pd
import os

here = os.path.dirname(__file__)
path = os.path.join(here, 'data_(2x2)_2_2(without ITE).csv')

first_few_levels = [-1.84428, -1.51360, -0.84428, -0.70156, 1.11357e-15]

df = pd.read_csv(path, comment='#')
energies = df['energy'].values
times = df['time'].values

fig, ax = plt.subplots()
ax.axhline(y=first_few_levels[0], color='b', label='n=0', linewidth=2)
ax.axhline(y=first_few_levels[1], color='c', label='n=1', linewidth=2)
ax.axhline(y=first_few_levels[2], color='g', label='n=2', linewidth=2)
ax.axhline(y=first_few_levels[3], color='y', label='n=3=4', linewidth=2)
ax.axhline(y=first_few_levels[4], color='orange', label='n=5', linewidth=2)
ax.plot(times, energies, linestyle='--', color='r', label='E(t)', linewidth=3)
ax.set_xscale('log')
ax.set_ylabel('E_n', fontsize=14)
ax.set_xlabel('t', fontsize=14)
ax.legend(fontsize=14)
ax.grid(True)
ax.tick_params(labelsize=14)
plt.show()
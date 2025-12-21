from matplotlib import pyplot as plt
import pandas as pd
import os

here = os.path.dirname(__file__)
path = os.path.join(here, 'data_(2x2)_2_2_eigenstate_histograms.csv')
df = pd.read_csv(path, comment='#')
t0_df = df[df['Time'] == 0]
t0_probabilities = t0_df['Probability'].values
t0_eigenvalues = t0_df['Eigenvalue'].values
init_energy = t0_eigenvalues @ t0_probabilities

fig, ax = plt.subplots()
ax.stem(t0_eigenvalues, t0_probabilities, linefmt='b-', markerfmt=' ', basefmt=' ')
ax.set_ylabel('P(E)', fontsize=14)
ax.set_xlabel('E', fontsize=14)
ax.set_ylim(0, 1)
ax.vlines(init_energy, 0, 1, colors='m', linestyles='dashed', label='E(t=0)', linewidth=2)
ax.legend(fontsize=14)
ax.tick_params(labelsize=14)
for spine in ax.spines.values():
    spine.set_linewidth(2)
plt.show()
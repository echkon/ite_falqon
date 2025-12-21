from matplotlib import pyplot as plt
import pandas as pd
import os

here = os.path.dirname(__file__)
path = os.path.join(here, 'data_(3x3)_4_5_eigenstate_histograms(ITE).csv')
df = pd.read_csv(path, comment='#')
tf_df = df[df['Time'] == 1]
tf_probabilities = tf_df['Probability'].values
tf_eigenvalues = tf_df['Eigenvalue'].values
init_energy = tf_eigenvalues @ tf_probabilities

fig, ax = plt.subplots()
ax.stem(tf_eigenvalues, tf_probabilities, linefmt='b-', markerfmt=' ', basefmt=' ')
ax.set_ylabel('P(E)', fontsize=14)
ax.set_xlabel('E', fontsize=14)
ax.set_xlim(None, 0)
ax.set_ylim(0, 0.5)
ax.vlines(init_energy, 0, 1, colors='g', linestyles='dashed', label='E(t=20)', linewidth=2)
ax.legend(fontsize=14)
ax.tick_params(labelsize=14)
for spine in ax.spines.values():
    spine.set_linewidth(2)
plt.show()
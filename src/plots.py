"""
:Author: Balazs Szigeti <szb37@pm.me>
:Copyright: 2021, DrugNerdsLab
:License: MIT
"""

from matplotlib import font_manager as fm, rcParams
import matplotlib.pyplot as plt
import seaborn as sns
import src.folders
import pandas as pd
import numpy as np
import os


sns.set_style("darkgrid")

df_all = pd.read_csv(os.path.join(src.folders.data_dir,'tolerance_all_md.csv'))
df_lsd = df_all.loc[(df_all.drug_cat==1)]
df_shroom = df_all.loc[(df_all.drug_cat==2)]

sns.regplot(x='n_MD', y='isGuessCorrectInt', label='All MDs', data=df_all, fit_reg=True, truncate=True, robust=True)
sns.regplot(x='n_MD', y='isGuessCorrectInt', label='LSD MDs',data=df_lsd, fit_reg=True,  truncate=True, robust=True)
sns.regplot(x='n_MD', y='isGuessCorrectInt', label='Psilocybin MDs',data=df_shroom, fit_reg=True,  truncate=True, robust=True)

plt.title('Guess accuracy vs. dose (LSD / LSD analogues)')
plt.xlabel('Number of prior microdoses')
plt.ylabel('Probablity of correct guess when MD taken')

plt.gca().set_aspect(2)
plt.xlim([0, 8])
plt.ylim([0.2, 0.7])
plt.legend()
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

F_Stat1 = 'summary_coare.csv'
F_Stat2 = 'summary_andreas.csv'
F_Stat3 = 'summary_ecume.csv'
F_Stat4 = 'summary_wasp.csv'


DataPath = '/home/lfaw/Bureau/Flux_turbulents/scores_flux_1km_10stat/'

#DataPath = '/home/lfaw/Bureau/AROME_ECMWF/summary_scores/'
OutPath = '/home/lfaw/Bureau/'
SummaryDF1 = pd.read_csv(DataPath + F_Stat1, sep=',')
SummaryDF2 = pd.read_csv(DataPath + F_Stat2, sep=',')
SummaryDF3 = pd.read_csv(DataPath + F_Stat3, sep=',')
SummaryDF4 = pd.read_csv(DataPath + F_Stat4, sep=',')

data_MeanBiais = [SummaryDF1['MeanBiais'], SummaryDF2['MeanBiais'], SummaryDF3['MeanBiais'], SummaryDF4['MeanBiais']]

# Créer une liste de labels pour chaque boîte à moustaches
labels = ['Coare','Andreas','Ecume','Wasp']

# Créer une liste de couleurs correspondant à chaque boîte à moustaches
colors = ['green', 'royalblue', 'orchid', 'orange']

# Charger les données pour le RMSE
data_RMSE = [SummaryDF1['rmse'], SummaryDF2['rmse'], SummaryDF3['rmse'], SummaryDF4['rmse']]

data_Corr = [SummaryDF1['Corr'], SummaryDF2['Corr'], SummaryDF3['Corr']]
# Créer une figure avec deux sous-graphiques partageant l'axe x
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
fig.set_size_inches(6, 4)
# Tracer les boîtes à moustaches pour le biais sur le premier sous-graphique
#bp3 = sns.boxplot(data=data_Corr, ax=ax3, notch=False, showmeans=True, meanprops={'markerfacecolor': 'black', 'markeredgecolor': 'black'}, palette=colors)
bp1 = sns.boxplot(data=data_MeanBiais, ax=ax1, notch=False, showmeans=True, meanprops={'markerfacecolor': 'black', 'markeredgecolor': 'black'}, palette=colors, width=0.5)
ax1.set_ylabel('Mean Biais')

# Ajuster les ordonnées pour le premier sous-graphique
#ax1.set_ylim(-6.5, 5)

#bp2 = sns.boxplot(data=data_RMSE, ax=ax2, notch=False, showmeans=True, meanprops={'markerfacecolor': 'black', 'markeredgecolor': 'black'}, palette=colors)
bp2 = sns.boxplot(data=data_RMSE, ax=ax2, notch=False, showmeans=True, meanprops={'markerfacecolor': 'black', 'markeredgecolor': 'black'}, palette=colors, width=0.5)
ax2.set_ylabel('RMSE')
for box, color in zip(bp2.artists, colors):
    box.set_facecolor('none')  
    box.set_edgecolor(color)  
    for element in box.elements:
        element.set_color(color) 
        
        

medians_MeanBiais = [np.median(data) for data in data_MeanBiais]
medians_RMSE = [np.median(data) for data in data_RMSE]

# Tracer les médianes sur les graphiques
#for i, median in enumerate(medians_MeanBiais):
   # ax1.text(i, median, f"{median:.2f}", ha='center', va='bottom', color='black', fontsize=10)

#for i, median in enumerate(medians_RMSE):
  #  ax2.text(i, median, f"{median:.2f}", ha='center', va='bottom', color='black', fontsize=10)

# Afficher les graphiques
plt.xticks(range(len(labels)), labels, fontsize = 12)
plt.tight_layout()
#ax2.set_ylim(1, 9)
#plt.xticks(range(len(data_MeanBiais)), labels)
ax1.tick_params(axis='both', which='major', labelsize=12)
ax2.tick_params(axis='both', which='major', labelsize=12)
#plt.xticks(range(len(data_MeanBiais)), labels)

#plt.savefig(OutPath +'boxplot_11stations.png')
ax1.set_ylabel('Bias ($m.s^{-1}$)', fontsize=12)
ax2.set_ylabel('RMSE ($m.s^{-1}$)', fontsize=12)
# Afficher le graphique
plt.show()

plt.savefig(OutPath + 'boxplot_11stations.png')

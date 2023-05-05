import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl

dataA = pd.read_csv("./survey_data_A.csv")
dataB = pd.read_csv("./survey_data_B.csv")
category = "Obstructive-Supportive"
CE_A = dataA[category]
CE_B = dataB[category]
text = category

mpl.rcParams['font.family'] = ['Times New Roman']
mpl.rcParams['font.size'] = 14

plt.figure()
plt.xlabel("Obstructive(1) vs. Supportive(7)")
plt.ylabel('# of people')

plt.hist([CE_A, CE_B] ,bins=7,range=[1,8],label=['Option A', 'Option B'],edgecolor="black",align="left",color=["blue", "orange"])
plt.legend(shadow=True)
axes = plt.gca()
axes.set_ylim([0,10])
plt.tight_layout()
plt.savefig("histograms/" + text + '.pdf')
plt.show()
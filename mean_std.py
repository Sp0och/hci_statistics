import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd

dataA = pd.read_csv("./survey_data_A.csv")
dataB = pd.read_csv("./survey_data_B.csv")
category = "mousetravel"
CE_A = dataA[category]
CE_B = dataB[category]

mean_A = np.mean(CE_A)
std_A = np.std(CE_A)

mean_B = np.mean(CE_B)
std_B = np.std(CE_B)

mpl.rcParams['font.size'] = 20
mpl.rcParams['font.family'] = ['Times New Roman']
text = 'Mouse travel'
xlab= ["Option A", "Option B"]
fig = plt.figure()
plt.title(text)
plt.ylabel("Distance [px]")
ax = plt.gca()
ax.set_xticks(range(len(xlab)))
ax.set_xticklabels(xlab)

plt.bar(np.arange(len(xlab)), [mean_A, mean_B], color=['blue', 'orange'], edgecolor='black')
plt.errorbar(np.arange(len(xlab)), [mean_A, mean_B], yerr=[std_A, std_B], fmt='.k', capsize=8.0)
plt.tight_layout()
plt.savefig("barplots/" + text + '.pdf')
plt.show()
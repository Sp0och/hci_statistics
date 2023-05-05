import matplotlib.pyplot as plt
import pandas as pd

dataA = pd.read_csv("./survey_data_A.csv")
dataB = pd.read_csv("./survey_data_B.csv")
category = "nr of clicks"
CE_A = dataA[category]
CE_B = dataB[category]
text = '# of mouse clicks'
plt.figure()
plt.xlabel(text)
plt.ylabel('# of people')

plt.hist([CE_A, CE_B] ,bins=15,range=[17,32],label=['Menu option A', 'Menu option B'],edgecolor="black",align="left",color=["blue", "orange"])
plt.legend(shadow=True)
axes = plt.gca()
axes.set_ylim([0, 10])
axes.set_xticks(range(17,32))
plt.savefig("histograms/" + text + '.pdf')
plt.show()
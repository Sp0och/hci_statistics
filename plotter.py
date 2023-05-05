import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# upper_rows=range(0,12)
# lower_rows=range(12,23)
dataA = pd.read_csv("./survey_data_A.csv")
dataB = pd.read_csv("./survey_data_B.csv")
# optionA = dataA['Please state your age']
# optionB = dataB['Please state your age']
would_A = dataA['time to perform']
would_B = dataB['time to perform']

# age = data['test3']
# A_dry = data['test1']
# B_dry = data['test2']

plt.figure()
plt.title('age vs completion time')
plt.xlabel('linspace')
plt.ylabel('performance time')

plt.scatter(range(0,10),would_A,label='time A')
plt.scatter(range(0,10),would_B,label='time B')
# plt.scatter(L2,Ts2,label='lighter envelope')
plt.legend(shadow=True)
# plt.savefig('measurements.pdf')
plt.show()
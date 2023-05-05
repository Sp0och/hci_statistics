import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats


dataA = pd.read_csv("./survey_data_A.csv")
dataB = pd.read_csv("./survey_data_B.csv")
category_array = ["Obstructive-Supportive","Complicated-Easy","Confusing-Clear","Boring-Exciting","Not Interesting-Interesting","Conventional-Inventive","Usual-Leading edge","I could complete all the given tasks satisfyingly with this version","I found this version's item placement intuitive.","I felt confident placing the correct items in the right place.","The menu structure of this version was intuitive.","The menu provided timely all the information I needed to complete the tasks.","The game visualizes climate change well.","The game helps me get a feeling of climate change and it's origin.","The information provided about the different objects was interesting and educational.","I would play a full version of this game","time to first place","time to perform","nr of clicks","mousetravel"]

print('What is your Alternative-Hypthesis? less, greater or two-sided (just a difference)')
alternative_input = input()

i = 0;

while i<len(category_array): # used for whole array, line 24 for individual test
    category = category_array[i]
    CE_A = dataA[category]
    CE_B = dataB[category]
    value = stats.wilcoxon(CE_A, CE_B,alternative = alternative_input)
    print("For ", category, ":", value)
    i+=1

# print(stats.wilcoxon(dataA["Obstructive-Supportive"],dataB["Obstructive-Supportive"]))   
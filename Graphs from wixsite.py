import pandas as pd
import matplotlib.pyplot as plt
import numpy as npimport seaborn as sns

# Pie graphs in intro

# Walc is a 1 -5 scale of weekend alcohol consumption, 1 being low
little_to_none = df.loc[df.Walc == 1].count()[0]
light = df.loc[df.Walc == 2].count()[0]
average = df.loc[df.Walc == 3].count()[0]
above_av = df.loc[df.Walc == 4].count()[0]
heavy = df.loc[df.Walc == 5].count()[0]


# Change plot style
plt.style.use('ggplot')


# Setup weights and lables for pie graph
weights = [little_to_none, light, average, above_av, heavy]
labels = ['Little to none', 'Light', 'Average', 'Above Average', 'Heavy']
explode = [0.01, 0.1, 0.1, 0.1, 0.15]

# Change plot style
plt.style.use('ggplot')

# Title
plt.title('Weekend Alcohol Consumption In\nGabriel Pereira and Mousinho da Silveira')


# Print pie with created weights and lables
plt.pie(weights, labels=labels, autopct = '%.2f%%', pctdistance=0.7, explode=explode)
plt.show()

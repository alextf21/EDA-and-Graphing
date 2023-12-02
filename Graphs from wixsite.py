import plotly.express as px
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


# Donut Chart

# Print pie with created weights and lables
plt.pie(weights, labels=labels, autopct = '%.2f%%', pctdistance=0.7, explode=explode)
plt.show()
# Create fig
fig = px.pie(df, names='sex', hole=0.5)
# Labels
fig.update_traces(textinfo='percent + value')
fig.update_layout(title_text='Male-Female Ratio', title_x=0.5)
# Layout
fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=0.00001,
    xanchor="center",
    x=.7
))
fig.show()


# Countplot for weekday and weekend alcohol consumption by gender


# create plot
sns.countplot(x='Dalc', hue='sex', data=df, palette='mako')
# set title
plt.title('Daily Alcohol Consumption by Gender')
# set axis labels
plt.ylabel('# Of Students')
plt.xlabel('(Dalc) Daily Alcohol Consumption Rate\nfrom 1 - very low to 5 - very high')

# create plot
sns.countplot(x='Walc',hue='sex',data=df, palette='mako');
# set title
plt.title('Weekend Alcohol Consumption by Gender')
# set axis labels, super easy
plt.ylabel('# Of Students')
plt.xlabel('(Weekend) Daily Alcohol Consumption Rate\nfrom 1 - very low to 5 - very high')


# Boxplot for alcohol consumption and grades


# Define the heavy drinkers, moderate drinkers and those who consume little to none
h_drinkers = df.loc[(df.Dalc>=4) & (df.Walc>=4)]['G1']
ltn_drinkers = df.loc[(df.Dalc<=2) & (df.Walc<=2)]['G1']
m_drinkers = df.loc[(df.Dalc==3) & (df.Walc==3)]['G1']
xlabels = ['Little to None', 'Mild', 'Heavy']

plt.title('Grades in first trimester for Heavy,\nLittle to None and Mild Alcohol Consumption')

plt.boxplot([ltn_drinkers, m_drinkers, h_drinkers], labels=xlabels)
plt.show()


# Heatmap


# Create heatmap with .corr function and change color
sns.heatmap(df.corr(), annot=True, cmap='plasma', lw=0)
# Font size
plt.xticks(fontsize=11)
plt.yticks(fontsize=13)
# Heatmap size
plt.rcParams['figure.figsize'] = (20,10)
# Display heatmap
plt.show()


# Countplot final Trimetser grade distribtion by gender


# Create heatmap with .corr function and change color
sns.heatmap(df.corr(), annot=True, cmap='plasma', lw=0)
# Font size
plt.xticks(fontsize=11)
plt.yticks(fontsize=13)
# Heatmap size
plt.rcParams['figure.figsize'] = (20,10)
# Display heatmap
plt.show()

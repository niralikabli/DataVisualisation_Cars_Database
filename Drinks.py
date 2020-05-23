import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

Drinks dataset visual analysis
WHO alcohol consumption data:

article: http://fivethirtyeight.com/datalab/dear-mona-followup-where-do-people-drink-the-most-beer-wine-and-spirits/

original data: https://github.com/fivethirtyeight/data/tree/master/alcohol-consumption

drink_cols = ['country', 'beer', 'spirit', 'wine', 'liters', 'continent']
drinks = pd.read_csv('drinks.csv',header=0, names=drink_cols)

drinks.head()

drinks.shape

# Histogram of Beer
drinks.beer.plot(kind='hist', bins=20, title='Histogram of Beer Servings')
plt.grid()
plt.xlabel('Beer Servings')
plt.ylabel('Frequency')

# compare with density plot (smooth version of a histogram)

drinks.beer.plot(kind='density', xlim=(0, 500))

# Scatter Plot

drinks.plot(kind='scatter', x= 'beer', y= 'wine')

pd.plotting.scatter_matrix(drinks[['beer','spirit', 'wine']], figsize=(10, 8))

# Calculate the mean alcohol amounts for each continent

drinks.groupby('continent').mean()

# Side-by-side bar plots

drinks.groupby('continent').mean().plot(kind = 'bar')

# Stacked bar plot
# (without the liters attribute)

drinks.groupby('continent').mean().drop('liters', axis=1).plot(kind='bar', stacked=True)

drinks.drop('liters', axis=1).plot(kind='box')

# Grouped Box Plots: show one box plot for each group

# Box plot of beer servings grouped by continent

drinks.boxplot(column='beer', by='continent')

# Box plot of all numeric columns grouped by continent

drinks.boxplot(by='continent', figsize=(10, 8))
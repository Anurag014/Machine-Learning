# Seaborn - Data visualization library

import seaborn as sns                # General importing name is as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Seaborn has some in-built datasets

# tips = sns.load_dataset('tips')          # Total bill vs  tip dataset
                                        # Loads the data as dataframe

# print(tips.head())

# Setting default theme
sns.set_theme()

                                                            # Relation plot

# Visualize the data
# sns.relplot(data = tips, x = 'total_bill',y = 'tip', col = 'time', hue = 'smoker', style = 'smoker', size = 'size')

# iris = sns.load_dataset('iris')

# print(iris.head())

                                                            # Scatter plot

# sns.scatterplot(x = 'sepal_length', y = 'petal_length', hue = 'species', data = iris)  # hue is used assign different representation for differnet values in these class
# plt.show()

                                                            # Count plot

# titanic = sns.load_dataset('titanic')
# print(titanic.head())
# sns.countplot(x = 'class', data = titanic)
# plt.show()
# sns.countplot(x = 'survived', data = titanic)
# plt.show()
# sns.barplot(x= 'sex', y= 'survived', hue = 'class', data = titanic)
# plt.show()

                                                            # Distribution plot

california_df = pd.read_csv("Python for ML\california_housing.csv")
print(california_df.head())

# sns.distplot(california_df['HouseAge'])
# plt.show()

                                                            # Heat map - Usefull for corelation

correlation = california_df.corr()
plt.figure(figsize=(10, 10))
sns.heatmap(correlation, cbar= True, square= True, fmt='.1f', annot= True, annot_kws={'size': 8}, cmap= 'Greens')
plt.show()
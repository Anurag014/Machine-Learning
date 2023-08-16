# Methods to handle missing values
# 1. Imputation
# 2. Dropping

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv('Data Collection and Preprocessing\Placement_Dataset.csv')
# print(dataset.head())

# print(dataset.isnull().sum())

# Understanding the distribution of salary data
fig, ax = plt.subplots(figsize = (8,8))
# sns.distplot(dataset.salary)
# plt.show()

# As there are otliers we can not fill missing values with mean 
# Filling missing values with mode

dataset['salary'].fillna(dataset['salary'].median(), inplace=True)
# Checking missing value
# print(dataset.isnull().sum())
# Visualizing distribution of salary column
sns.distplot(dataset.salary)
plt.show()

# Dropping missing value in ML model is not recommended for small dataset and for large dataset it may be used as per performance
salary_dataset = pd.read_csv('Data Collection and Preprocessing\Placement_Dataset.csv')
salary_dataset = salary_dataset.dropna(how = 'any')
print(salary_dataset.isnull().sum())
# Data Standardization - It is process of standardizinig the data in common format or common range

import numpy as np
import pandas as pd
import sklearn.datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Loading the datasets
dataset = sklearn.datasets.load_breast_cancer()
# print(dataset)

#Loading a dataset to panda dataframe
df = pd.DataFrame(dataset.data, columns=dataset.feature_names)
# print(df.head())
# print(df.shape)

X = df
Y = dataset.target

# print(X)
# print(Y)

# Splitting the data into training data and test data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size= 0.2, random_state = 3)
print(X.shape)
print(X_train.shape)
print(X_test.shape)

# Standardizing the data

# Checking whether data is in standard range or not
print(dataset.data.std())

scalar = StandardScaler()
# Making scalar to learn data
scalar.fit(X_train)
X_train_standardized = scalar.transform(X_train)
X_test_standardized = scalar.transform(X_test)
print(X_train_standardized)
print(X_test_standardized.std())
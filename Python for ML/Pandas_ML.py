# Pandas Library - Data processing and analysing
# Pandas Data frame are two dimensional tabular data structure with labelled axes (rows and columns)

import pandas as pd
from sklearn.datasets import fetch_california_housing
import numpy as np

california_housing_dataset = fetch_california_housing()

print(type(california_housing_dataset))
print(california_housing_dataset)        # This shows data as a map in python

                                                    # Converting data to dataframe

california_df = pd.DataFrame(california_housing_dataset.data, columns = california_housing_dataset.feature_names)
#print(california_df.head())      # Prints top 5 row of the dataframe by default
print(california_df.shape)     # Prints the shape of data

                                                    # Importing Dataset from csv file to Pandas DataFrame

diabetes_df = pd.read_csv('Python for ML\diabetes.csv')   # Similarly we can read other file
print(type(diabetes_df))
#print(diabetes_df.head())

                                                    # Exporting Dataframe to csv file

# california_df.to_csv('california_housing.csv')   # Similarly we can convert to other file 

                                                    # Creating Dataframe with Random values

'''random_df = pd.DataFrame(np.random.rand(20,10))
print(random_df)'''

                                                    # Inspecting Dataframe

print(california_df.shape)                    # Prints the shape of the data
print(california_df.head())                   # Prints the first 5 row of the dataframe until specific number specified
print(california_df.tail())                   # Prints the last 5 row of the dataframe until specific number specified
print(california_df.info())                   # Prints the information of the dataframe
print(california_df.isnull().sum())           # Prints the count of null values in the column
print(diabetes_df.value_counts('Outcome'))    # Print the count based on the label
print(diabetes_df.groupby('Outcome').mean())  # Groups the value based on the mean

                                                    # Statistical measures using Pandas

print(california_df.count())                  # Shows the count or no. of values in each column
print(california_df.mean())                   # Shows the mean value of each column
print(california_df.std())                    # Shows the standard deviation column wise
print(california_df.min())                    # Shows the minimum value of each column
print(california_df.max())                    # Shows the maximum value of each column
print(california_df.describe())               # Shows all the statistical measures about dataframe in one go

                                                    # Manipulating Dataframe

# Adding the column to a data frame
california_df['Median_price(100k$)'] = california_housing_dataset.target
print(california_df.head(2))

# Removing a row from a data frame         
print(california_df.drop(index= 0, axis= 0).head(2))      # Index defines the index no and axis defines the row or column for 0 and 1 respectively

# Removing a column from dataframe
print(california_df.drop(columns='Population', axis= 1).head(2))

# Locating a row using a index value
print(california_df.iloc[2])

# Locating a column using a index value
print(california_df.iloc[:, 0])

                                                    # Correlation in Pandas

print(california_df.corr())      # Shows the correlation between each variables(columns)
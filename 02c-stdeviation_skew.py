# Simple Statistical Analysis on Data Frame

# Standard deviations and skewness
import numpy as np
import pandas as pd

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


#Create a Dictionary from series of values
d = {'Name':pd.Series(['Tom','Jayesh','Ricky','Vinu','Shiv','Smita','Biren',
   'Latha','Anu','Ganesh','Navya','Akbar']),
   'Age':pd.Series([25,26,25,23,45,25,23,34,40,30,25,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}


#Create a DataFrame from dict d
df = pd.DataFrame(d)

# print the Dataframe
print("Data Frame is : ")
print(df)
print()

# Calculate the range of a specific numeric column, say Age
print("Range of Age values is : ")
print(df.Age.max() - df['Age'].min())
print()


# Calculate the range of numeric columns
print("Range of numeric values is : ")
df_nums = df.select_dtypes(include=np.number)  # extract only numeric columns
print(df_nums.max() - df_nums.min() )
print()

# Calculate the variance
print("Variance is : ")
print(df_nums.var())
print()

# Calculate the standard deviation
print ("Standard deviation is : ")
print(df_nums.std())
print()

# Calculate the skew
print ("Skew is : ")
print (df_nums.skew())  # calculate skew for Age and Rating
print()
# Observe: Distribution for Rating is nominal. Distribution for Age is skewed to right

# Calculate kurtosis
print("Kurtosis is : ")
print(df_nums.kurtosis())
print()
print("Done")

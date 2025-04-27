# Basic EDA on titanic.csv

import warnings
warnings.filterwarnings("ignore")

#Load the required libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


#Load the data
df = pd.read_csv('titanic.csv')
 
#check top records of the data
print(df.head())
print("Shape of the input data is : ", df.shape)
print()

# display basic information about the data
print("Displaying information about the data : ")
print("Also displays the number of non null values in each column ")
print(df.info())
print()

# display the statistical info of the data
print("Displaying basic statistics of the data : ")
print(df.describe())
print()
input("Type Enter to continue")


# find duplicate records in the data
print("Number of duplicate records = : ", df.duplicated().sum())

# find the number of unique columns in the data
#unique values
print("Print unique Values for the columns") 
print("unique values of Pclass ", df['Pclass'].unique())
print("unique values of Survided ", df['Survived'].unique()) 
print("Unique values of Sex " , df['Sex'].unique())
print()

input("Type Enter to continue")


# plot counts on categorical data

print("Generate a plot of Pclass values") 
sns.countplot(x='Pclass', data=df)
plt.show()
print()
print("Pclass split by gender")
sns.countplot(x='Sex', hue='Pclass', data=df)
plt.show()
print()
input("Press key to continue")

# find null values in the data

print("Null values in the data is :")
print(df.Age.isnull().sum())
print()


# replace null values with 0
df.replace(np.nan,'0',inplace = True)
# replace null values with mean
#df.replace(np.nan, df.mean(), inplace = True)

print("after replacing :") 
#Check the changes now
print(df.Age.isnull().sum())
print()

print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
#drop a few features in columns
print("Dropping a few columns")
notneeded = ['PassengerId', 'Name','Ticket']
cleaned = df.drop(columns=notneeded)   # drop columns in notneeded list
print(cleaned.head())
print()


##################################################################################
# Generate few plots

input("Press key to continue")

# plot histogram on the Age feature
# kde is kernel density estimator which smoothens values, if set True
sns.histplot(cleaned.Age, kde=True, bins=20)
plt.xlabel("Age")
plt.ylabel("Counts")
plt.grid(True)
plt.show()

print('Done')



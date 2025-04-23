# Program to Demonstrate Data Cleaning Operations

# import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline

# get the data
data_file = "test_data_for_data_cleaning.csv"
df = pd.read_csv(data_file)

# Explore the data
# print shape
print("Data Frame format is : ", df.shape)
print()

# Examine the attribute names (column names) of the dataset
print("Attribute names are:")
print(df.columns)
print()

#input("Hit Enter to Continue")


# examine the top and bottom few rows
# We can view the top five rows with with df.head()
print("Top few rows are")
print(df.head())
print()
# and bottom five rows of the dataset with df.tail() methods.
print("Botton few rows are")
print(df.tail(5))
print()
# Note that there are lot of discrepancies
'''
Observe:
For example, the age and sex columns are combined together with an underscore.
There should be two separate columns of age and sex.

The height and weight columns contain missing values.
Some values are coded as "xx", "?", "0" and negative values.
They are all invalid values as height and weight must be positive real numbers.

The three columns spend_A, spend_B and spend_C denote spending at three
supermarkets A,B and C.
These columns must contain positive real numbers.
The missing values in these columns denote nothing is spent in that market.
The negative value and the value coded as "xx" should be addressed properly.

'''

# Get information about the data set
print("Information of the dataframe is:")
df.info()
print()


# Check the data types
print("Data types of attributes in our data set is:")
print(df.dtypes)
print()

'''
Observe:
Data types are not correct.
Also, we can see that data types of height(cm) and weight(kg) columns are object
data type. The columns height(cm) and weight(kg) must contain positive real numbers.
Their data type must be float64.

Also, spend_A, spend_B and spend_C columns must contain numeric values.
We can see that the data type of spend_A and spend_B columns are float64.
But the data type of column spend_C is object.
So, we need to convert its data type to float64.

'''

# Handle incorrect data
# The height(cm) column has a value 'xx' we can force this invalid value
# to NaN using error option
df["height(cm)"] = pd.to_numeric(df["height(cm)"], errors='coerce')

# Similarly we handle the 'xx' in the weight(kg) and spend_C fields
df["weight(kg)"] = pd.to_numeric(df["weight(kg)"], errors='coerce')
df["spend_C"] = pd.to_numeric(df["spend_C"], errors='coerce')

# Re-examine the data types after the above operations
print("Data types after correction")
print(df.dtypes)
print()

'''
Observe:
Now, we can see that all the columns have appropriate data types.
The columns height(cm) and weight(kg) have float64 data type.
The columns spend_A, spend_B and spend_C have float64 data type.

'''
# Check if the values 'xx' have bee converted to NaN
#display head and tail of the datraset
print("Top 5 records")
print(df.head())
print()
print("Last 5 records")
print(df.tail())
print()

'''
Observe:
all 'xx' values are converted to NaN
'''

# Get summary Statistics of the data
print("Summary Statistics:")
print(df.describe())
print()

'''
Observe:
We can see that there are discrepancies in height(cm) and weight(kg) columns.
The minimum value of height(cm) is 0. It is not possible because height cannot be 0.
The minimum and maximum values of weight(kg) are -60 and 160.
Weight cannot be negative and weight cannot be as high as 160. Hence invalid values.
They are outliers and need to be properly addressed.
'''

####################################################################
# Visual Exploration of Data
# Data can be plotted to visually examine the data
# use matlpotlib


# Line plot. Displays a line graph. Can be used to show a single variable

df['age'].plot()
plt.title('Line graph of Age')
plt.xlabel("Sample No")
plt.ylabel('Age')
plt.show()

# Bar chart
df['age'].plot(kind='bar')
plt.title('Bar graph of Age')
plt.xlabel("Sample No")
plt.ylabel('Age Value')

# Histogram chart for height
df['height(cm)'].plot(kind='hist')
plt.title('Histogram for Height')
plt.xlabel("Height ")
plt.ylabel('Frequency')
plt.show()


'''
Observe:
Height on range 0-25 cms is present. This is an error in data with height = 0.0
Need to be rectified
'''

# Histogram for weight
df['weight(kg)'].plot(kind='hist')
plt.title('Histogram for Weight')
plt.xlabel("Weight ")
plt.ylabel('Frequency')
plt.show()


'''
Similar analysis of histogram of weight(kg) column shows that there is a
negative value of -60 and a very high value of 160 in the weight(kg) column.
Both need to be handled
'''

# Box Plots
# Box plot for height
df.boxplot(column='height(cm)')
plt.show()

'''
Observe:
There is an outlier in the box plot at 0.0. this value in the data needs to be handled.
'''

# Box plot for weight
# Shows outlier
df.boxplot(column='weight(kg)')
plt.show()

'''
Observe:
Negative value of weight and a very high value of weight are observed. 

'''

# Scatter plot displays relationship between two variables
df.plot(kind='scatter',x='height(cm)', y='weight(kg)', c='Red')
plt.show()

'''
Observe:
No major relationship is observed. 

'''

###########################################################################

# Split age_sex column. This column has both age and gender values joined by
# an _ (underscore). Need to split to seperate columns.
# split() is used to split and also create two seperate columns with names AGE & sex
df[['AGE','sex']] = df.age_sex.str.split("_", expand = True)

# display top records to check
print('After split')
print(df.head())
print()

# There are two columns age and AGE with same data. We can delete one of the two.
# Also the age_sex column also can be deleted
df.drop(['AGE'], axis=1, inplace=True)
df.drop(['age_sex'], axis=1, inplace=True)

# display top records to check
print('After dropping columns')
print(df.head())
print()

# Reorder column values 
df = df[['fname','lname','age','sex','section','height(cm)','weight(kg)','spend_A','spend_B','spend_C']]

# print dataframe
print('Data after re ordering')
print(df)
print()

##########################################################################

# Hanldle Negative Values
# weight column has -60. We can assume it was to be a value 60. (typo error)
# spend_B column also has a negative value. Assume it is +100
# Suppress settingwithcopywarning
import warnings
warnings.filterwarnings('ignore')

pd.set_option('mode.chained_assignment', None)
# replace value
df['weight(kg)'].replace(-60, 60, inplace=True)
df['spend_B'].replace(-100,100, inplace=True)

# check after replacement
print('Data after replacement')
print(df)

# Now, our data has no missing or negative values.
# There are no outliers in our data

print('Job Done')
print()


###########################################################################

# Handle outliers
# In the height(cm) column, there is a value of 0.0. Replace the 0.0 value
# with the mean value of the height(cm) column.
# we can replace with a constant, min, max. mean, mode values as per need

# calculate the mean of the column
mean_ht = df['height(cm)'].mean()
# replace the height outlier with the mean
df['height(cm)'].replace(0.0, mean_ht, inplace=True)

# display after replacing
print("Data after outlier removal")
print(df)
print()

# Similarly for weight(kg) column, there is a high value of 160.
# Let us replace this with min value (or a constant value, say 60)
min_wt = df['weight(kg)'].min()
# replace the weight outlier with the mean
df['weight(kg)'].replace(160, min_wt, inplace=True)

# display after replacing
print("Data after outlier removal")
print(df)
print()


##########################################################################

# Fill Missing Values
# we use df.isnull() and df.isnull.sum() to check and count number of missing values
# We use isna() and notna() functions to detect ‘NA’ values

# Find missing values in each column
print('Missing value details')
print(df.isnull().sum())
print()

# Fill missing values with a test static
# like mean, min, max, median or mode of the specific feature

# we will fill with mean values of the specific feature variable

# missing values of height
mean_height = df['height(cm)'].mean()
df['height(cm)'].fillna(mean_height, inplace=True)

# missing values of weight
mean_weight = df['weight(kg)'].mean()
df['weight(kg)'].fillna(mean_weight, inplace=True)

# missing values of spend_A
mean_spend_A = df['spend_A'].mean()
df['spend_A'].fillna(mean_spend_A, inplace=True)

# missing values of spend_B
mean_spend_B = df['spend_B'].mean()
df['spend_B'].fillna(mean_spend_B, inplace=True)

# missing values of spend_C
mean_spend_C = df['spend_C'].mean()
df['spend_C'].fillna(mean_spend_C, inplace=True)

# Recheck missing values
print("Missing value Status after replace")
# Again check for missing values
print(df.isnull().sum())
print()
'''
Observe:
Now, in our data there are no missing or negative values.
There are no outliers in our data
'''

# Scatter plot displays relationship between two variables after cleaning
df.plot(kind='scatter',x='height(cm)', y='weight(kg)', c='Red')
plt.show()

print('Job Done')

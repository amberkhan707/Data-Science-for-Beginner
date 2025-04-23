# Load iris dataset using pandas
# perform statistical analysis on the data

import pandas as pd

# read data from a csv file into a data frame
url = r"iris.csv"
fnames = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv(url, names=fnames)


# display structure of data frame
print('\nShape of data')
print(dataset.shape)

# display  top 20 records of data
print('\nTop 20 records')
print(dataset.head(20))
print()

input("Press Enter to proceed")


# get basic statistics using describe
print('\nBasic Statistics')
print(dataset.describe())
print()

input("Press Enter to proceed")

# class distribution
print("\nClass Distribution")
print(dataset.groupby('class').size())
print()

input("Press Enter to proceed")

# Visualization of the attributes
import matplotlib.pyplot as plt

# univariate plots
# create box plots
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()

# histogram plots	
dataset.hist()   # generate histograms
plt.show()


# multivariate plots give relationship between two variables	
# scatter plot matrix

#iris_df=pd.DataFrame(dataset)
#pd.plotting.scatter_matrix(iris_df,alpha=0.2, figsize=(10, 10))
pd.plotting.scatter_matrix(dataset)
plt.show()



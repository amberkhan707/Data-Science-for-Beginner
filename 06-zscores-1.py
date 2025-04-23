#Calculate the z-score from with scipy
import scipy.stats as stats
values = [4,5,6,6,6,7,8,12,13,13,14,18, 20, 19, 12, 10, 15, 13, 9, 14]
import numpy as np

v=np.array(values)  # convert list to np array
print("Data is ")
print(v)
print()

m=v.mean()  # mean
print ('mean : ', m)
st=v.std()  # std dev
print ('std dev : ' , st)
print()

print("Z-scores computed by normal formula")
v1= (v-m)/st    # v1 has Z scores for each element of v
print(v1)
print()

# using library function
z = stats.zscore(values)
print("Z score using library finction")
print(z)
print()

N = len(values)     # population size
                    #z = zscores

# Z score on a data frame
import pandas as pd
import matplotlib.pyplot as plt


data = pd.DataFrame(np.random.randint(0, 10, size=(5, 3)), columns=['A', 'B', 'C'])
print("Data frame of random values")
print(data)
print()

# use apply on the data frame to compute column wise z scores
zc=data.apply(stats.zscore)

# display the mean value for the columns
print("Mean values for columns are")
print(data.mean())
print()

# display z scores on all the columns
print("z scores on the data frame")
print(zc)
print()



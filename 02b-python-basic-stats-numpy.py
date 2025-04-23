# Basic statistics operations on numpy arrays
# percentile, mean, median

import numpy as np 
# Sample data
b=np.array([10,70,25,30,20,30,40,45,60,75,60])
print('Original Data : ' , b)
print("50 percentile is : ", np.percentile(b,50))
print()

# np supported statistical operations
# median
print ('\nApplying median() function:' )
print (np.median(b) )

# mean to calculate the arithmetic mean
print ('\nApplying mean() function:' )
print (np.mean(b) )

# weighted average
a1 = np.array([1,2,3,4,5]) 
print ('\nThe input array is:' ,a1)
print ()  

# average() function is used to evaluate weighted average
print ('Applying average() function:' )
print (np.average(a1)) 
print ()  

# this is same as mean when weight is not specified 
wts = np.array([4,3,2,2,1]) 
print("weight vector is ", wts)
print ('Applying average() function with weights:' )
print (np.average(a1,weights = wts))
print () 

# variance is average of squared deviations
# var() gives the variance of the elements
print('variance of [2,4,6,9,15] is :' , np.var([2,4,6,9,15]))
print()

# std deviation = sqrt(mean(abs(x - x.mean())**2))      
# std() gives standard deviation
print('std dev of [2,4,6,9,15] is :' , np.std([2,4,6,9,15]))
print()

print("Job Done")


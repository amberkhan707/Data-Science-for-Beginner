# Example box plots on single variable
import matplotlib.pyplot as plt
import statistics

# sample data lists 
value1 = [82,76,24,40,67,62,75,78,71,32,98,89,78,67,72,82,87,66,56,52]
value2 = [62,5,91,25,36,32,96,95,3,90,95,32,27,55,100,15,71,11,37,21]
value3 = [23,89,12,78,72,89,25,69,68,86,19,49,15,16,16,75,65,31,25,52]
value4 = [59,73,70,16,81,61,88,98,10,87,29,72,16,23,72,88,78,99,75,30]
v1= [1,2,3,4,5,6,7,8,119] 

# describe core statistical data from value1
print("Basic features")
meanval= statistics.mean(value1)
medianval = statistics.median(value1)
modeval= statistics.mode(value1)

# print Mean, Median and Mode of values 
print("Mean is : ", meanval)
print("Median is :", medianval)
print("Mode is :",modeval)
print()


# generate box plots
#plt.boxplot(value1)

plt.boxplot([value1,value2])
#plt.boxplot(v1)   # demonstrates outlier

plt.show()

# Determine Skew
if meanval > modeval :
    print ("Data is Right Skewed")
else:
    print("Data is Left Skewed")

print("Done")



import numpy as np
import matplotlib.pyplot as plt

rain = [20,24,27,0,32,12,36,8,21,31,22,29,2,0,14]
print("rainfall is" , rain)


# report basic stats of the list data
print("number of observations: ", len(rain))
print("Min rainfall: " , min(rain) )
print("Max rainfall: " , max(rain) )
print("Range rainfall: " , max(rain)- min(rain) )
print("number of days of NO rainfall: ", rain.count(0))
print("Total Rainfall: ", sum(rain))
print("Mean value of rainfall: ", sum(rain)/len(rain) )
print()

# complex stats operations
# Standard deviation of list 
# Using sum() + list comprehension 
mean = sum(rain) / len(rain)
numb_obs = len(rain)
variance = sum([((x - mean) ** 2) for x in rain]) / numb_obs 
std_dev = variance ** 0.5
print("Variance is : ", variance)
print("Standard deviation calculated is : ", std_dev)


# try with numpy
std_dev_1 = np.std(rain)
# printing list
print("Standard Deviation from numpy: ", std_dev_1)
print()

# print z score of a user given value
value=int(input("Enter a value to calculate z-score:"))
z= (value - mean) / std_dev

print('Z-score of ', value, 'is ', z)
print()

########################################################################

# some data plots
rain = [20,24,27,0,32,12,36,8,21,31,22,29,2,0,14]

# lineplot
plt.plot(rain)   # line plot
plt.title("Line plot of rain")
plt.show()

# boxplot
plt.boxplot(rain)  # box plot
plt.title("Box plot for rain")
plt.show()

# scatterplot
humidity = [80,83,78,99,74,70,69,45,39,90,96,89,78,50,45]
plt.scatter(rain,humidity)    # scatter plot
plt.title("Scatter plot of rain and humidity")
plt.show()



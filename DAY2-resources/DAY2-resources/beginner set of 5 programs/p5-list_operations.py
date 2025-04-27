# lists manipulations

daily_temp = [32,41,38,35,34,34,36,29,40,30]

print("Temperature values before append are :", daily_temp)

# append
daily_temp.append(45)
print("Temperature values after append are :", daily_temp)


# extend
daily_temp.extend([32,25,33,40])
print("Temperature values after extend are :", daily_temp)


# remove
daily_temp.remove(34)
print("Temperature values after remove are :", daily_temp)


print("number of elements is " , len(daily_temp))
print("max of elements is " , max(daily_temp))
print("min of elements is " , min(daily_temp))
print("average of  daily_temp is " , sum(daily_temp) / len(daily_temp))

print()
#################################################################


# program to count how many times temperature crossed the mean value using for

# Calculate mean daily temperature
daily_temp = [32,41,38,35,34,34,36,29,40,65]
mean_temp = sum(daily_temp) / len(daily_temp)
print('mean temperature of newdata : '  , mean_temp)
# count number of times temperature crossed mean value

k=0
for temperature in daily_temp:
    if temperature > mean_temp:
        k=k+1

print("Calculated with for: Temperature exceeded mean ", k, 'times')
print()



######################################################
# program to count how many times temperature crossed the mean value using while

# Calculate mean daily temperature
daily_temp = [32,41,38,35,34,34,36,29,40,65]
mean_temp = sum(daily_temp) / len(daily_temp)


# count number of times temperature crossed mean value
k=0
indx = 0
while indx < len(daily_temp):
    if daily_temp[indx] > mean_temp:
        k=k+1
    indx += 1
print("Calculated with while: Temperature exceeded mean ", k, 'times')
print()


######################################################
'''
# importing math library / module

#import math

print("value of pi is :", math.pi)
print("sin(0.5) is: ", math.sin(0.5))




'''
import matplotlib.pyplot as plt
daily_temp = [32,41,38,35,34,34,36,29,40,30]

plt.plot(daily_temp)
plt.show()



print("Job Done")


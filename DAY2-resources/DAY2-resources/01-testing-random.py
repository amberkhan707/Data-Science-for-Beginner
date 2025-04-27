# using random data

import numpy as np

ys = 200 + np.random.randn(100)        # normal distribution mean = 0, variance = 1
#ys = 200 + np.random.random(100)*5    # uniform distribution between 0 and 1
x= [x for x in range(len(ys))]

import matplotlib.pyplot as plt
plt.plot(x,ys)    # line plot
plt.show()


# plot the histogram of random samples
plt.hist(ys,10)     # 10 is number of buckets
plt.show()

# random numbers
r = np.random.randint(1,5,25)  # integers between 1 and 5
print(r)
print()

r = np.random.randint(-3,5,25)  # integers between -3 and 5
print(r)


# randomly pick an object from a list using choice
colors = ['Red', 'Green', 'Blue' , 'Yellow', 'Pink', 'White', 'Violet']
print( np.random.choice(colors))



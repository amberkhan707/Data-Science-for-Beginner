# Gaussian Distribution or Standard Distribution

# imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


# Generate 20 sample points from a standard normal distribution between -3 and 3
samples = np.linspace(-3, 3, 20)  # Range from -3 to 3 (standard normal limits)

# norm.pdf(samples, loc=0, scale=1) computes the Probability Density Function (PDF)
# with mean = 0 and std dev = 1.
pdf_values = norm.pdf(samples, loc=0, scale=1)  # Standard Normal (mean=0, std=1)


'''
# Consider some 20 samples of observation
samples=np.array([20,30,40,35,45,60,70,70,65,80,90,45,65,72,81,25,50,55,30,80])
s_mean= samples.mean()
s_dev = samples.std()
print('Mean of samples : ' , s_mean)
print('Strd Deviation : ' , s_dev)
print()
samples.sort()
pdf_values = norm.pdf(samples, loc=s_mean, scale=s_dev)

'''


# Plot the standard normal distribution
plt.plot(samples, pdf_values, marker='o', linestyle='-', color='blue', label="Standard Normal Distribution")
plt.xlabel("X-values")
plt.ylabel("Probability Density")
plt.title("Standard Normal Distribution (20 Samples)")
plt.legend()
plt.grid()
plt.show()


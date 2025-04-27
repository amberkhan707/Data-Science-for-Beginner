# Binomial probability to calculate the binomial probability of
# getting exactly 6 heads in 10 flips of a fair coin.

from math import comb

# Define parameters
n = 10  # Total coin flips
k = 6   # Desired number of heads
p = 0.5 # Probability of heads in a fair coin

# Calculate binomial probability
bprob = comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
print("Binomial Distribution")
print(f"The probability of getting exactly {k} heads in {n} flips is: {bprob:.4f}")
print()

# binomial distribution plot

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Define parameters for binomial distribution
n = 10   # Number of trials
p = 0.5  # Probability of success in each trial

# Generate possible values of k (number of successes)
k_values = np.arange(0, n+1)

# Compute binomial probabilities
binomial_probs = binom.pmf(k_values, n, p)

# Plot the binomial distribution
plt.bar(k_values, binomial_probs, color='skyblue', edgecolor='black')
plt.xlabel("Number of Successes (k)")
plt.ylabel("Probability")
plt.title(f"Binomial Distribution (n={n}, p={p})")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()



############################################################################

# Poisson Distribution

# Here's a simple program to calculate the probability of a call center
# receiving exactly 7 calls in an hour when the average is 5 calls per hour

# import modules
from scipy.stats import poisson

# Define the parameters
lambda_value = 5  # Average number of calls per hour usually
k = 7             # Exact number of calls we want to calculate probability for

# Calculate Poisson probability
# The .pmf() function is the Probability Mass Function (PMF) that calculates
# P(X = k) using the Poisson formula

pprob = poisson.pmf(k, lambda_value)

print("Poission Distribution")
print(f"The probability of receiving exactly {k} calls in an hour is: {pprob:.4f}")


print("Done")


# Poisson distribution plot

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Define the mean number of occurrences (λ)
lambda_value = 5  # Example: average 5 events per interval

# Generate possible values of k (number of occurrences)
k_values = np.arange(0, 20)

# Compute Poisson probabilities
poisson_probs = poisson.pmf(k_values, lambda_value)

# Plot the Poisson distribution
plt.bar(k_values, poisson_probs, color='skyblue', edgecolor='black')
plt.xlabel("Number of Events (k)")
plt.ylabel("Probability")
plt.title("Poisson Distribution (λ = 5)")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# normalization of data
# importing packages

import pandas as pd

# create data
df = pd.DataFrame([
		[180000, 110, 18.9, 1400],
		[360000, 905, 23.4, 1800],
		[230000, 230, 14.0, 1300],
		[60000, 450, 13.5, 1500]],
		columns=['Col A', 'Col B','Col C', 'Col D'])

# view data
print(df)
print()

# plot the data
import matplotlib.pyplot as plt
df.plot(kind = 'bar')   # bar plot from data frame
plt.show()

#####################################################################

# Scale / Normalise the data

# Use Maximum Absolute scaling
# copy the data
df_max_scaled = df.copy()

# apply normalization technique by dividing every feature by maximum
# absolute value
for column in df_max_scaled.columns:
    df_max_scaled[column] = df_max_scaled[column]  / df_max_scaled[column].abs().max()

# view normalized data
print("After Max Absolute Scaling")
print(df_max_scaled)
print()

# view ths plot after normalization
df_max_scaled.plot(kind= 'bar')
plt.title("Max Absolute Normalization")
plt.show()

##################################################
# min max feature scaling
# subtract the minimum value and divide by the range
# copy the data
df_min_max_scaled = df.copy()

# apply normalization techniques
for column in df_min_max_scaled.columns:
    df_min_max_scaled[column] = (df_min_max_scaled[column] - df_min_max_scaled[column].min()) / (df_min_max_scaled[column].max() - df_min_max_scaled[column].min())
    
# view normalized data
print("After Min - Max Scaling")
print(df_min_max_scaled)
print()

# view this plot after normalization
df_min_max_scaled.plot(kind= 'bar')
plt.title("Min - Max Normalization")
plt.show()


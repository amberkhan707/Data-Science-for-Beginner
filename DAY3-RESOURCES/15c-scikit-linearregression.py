# predicting the price of house based on Plot size
# using Linear Regression

# we use scikit-learn package
import warnings
warnings.filterwarnings("ignore")

# import libraries
import matplotlib.pyplot as plt
import numpy as np

# also import scikit-learn for ML
from sklearn import linear_model
import pandas as pd

# Load data from CSV into data frame columns
df = pd.read_csv("Housing1.csv")
print('First 20 rows of data of two columns of interest')
print(df[['plotsize','price']].head(20))

# extract plotsize and price columns into X and Y
X = df['plotsize']
Y = df['price']

# Convert to Data frame
X=pd.DataFrame(X)
Y=pd.DataFrame(Y)


# Split the data into training/testing sets
X_train = X[:-250]
X_test = X[-250:]

# Split the targets into training/testing sets
Y_train =  Y[:-250]
Y_test = Y[-250:]

# Plot the data points on a scatter plot
f = plt.figure()
f.set_figwidth(10)
f.set_figheight(8)

# scatter plot
plt.scatter(X_test, Y_test,  color='red')
plt.title('Housing Data')
plt.xlabel('Plot Size')
plt.ylabel('Price')

# ticks on x and y axes
plt.xticks((np.arange(0,int(X_test.max()),1000)))
plt.yticks((np.arange(0,int(Y_test.max()),10000)))

# Linear Regression 
# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model on the training data using fit method
#regr.fit(X_train, Y_train.reshape(-1,1))
regr.fit(X_train, Y_train)
print()

# model gives the coefficient and intercept as the model parameters
print("Coeff is : " , regr.coef_ )
print("Intercept is : " , regr.intercept_ )

# plot regression line using these model values X_test and Predicted values
plt.plot(X_test, regr.coef_ * X_test + regr.intercept_, linewidth=2)

# Plot refression line using predict method
#plt.plot(X_test, regr.predict(X_test), color='green',linewidth=2)

plt.show()
print()

#predict price for a given plot size
psize = int(input("Enter Plot Size : "))

#calculate the predicted price for the given plot size
pprice=regr.predict(np.array(psize).reshape(-1,1))
print("\nPrice predicted is : ", pprice)

print('Job Done')

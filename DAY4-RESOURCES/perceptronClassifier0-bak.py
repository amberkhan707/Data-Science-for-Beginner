from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score

from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import numpy as np


# load iris dataset
iris = datasets.load_iris()

# Create our X and y data
X = iris.data
y = iris.target


# view few observations
print("Shape is : ", X.shape)
print("\nfirst 5 observations")
print(X[:5])
print("\nfirst 5 observations of y values")
print( y[:5])


# Split data into training and test (70:30
X_train, X_test, y_train, y_test = train_test_split(
          X, y, test_size=0.3, random_state=0)
#print(X_train.shape,X_test.shape)

# preprocess X data with by standard scaling mean=0 
sc = StandardScaler()
# fit the training model
sc.fit(X_train)


# transform() method is used to apply scaler to X_training data
X_train_std = sc.transform(X_train)
# similarly for the test data
X_test_std = sc.transform(X_test)


# create perceptron object
# use n_iter=40
ppn = Perceptron( eta0=0.1, random_state=0)
# train the perceptron on training data
ppn.fit(X_train_std, y_train)

#predictions via the predict method
y_pred = ppn.predict(X_test_std)
print('classification output\n',y_test,'\n',y_pred)
print('Misclassified samples: %d' % (y_test != y_pred).sum())
print('Accuracy: %.2f' % accuracy_score(y_test, y_pred))

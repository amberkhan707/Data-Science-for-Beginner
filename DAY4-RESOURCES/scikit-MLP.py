# MLP feed forward  neural network

# Imports
import pandas as pd

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.neural_network import MLPClassifier

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

from sklearn.metrics import classification_report


# Load the data
fnames = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
file_name= r'iris.csv'
df = pd.read_csv(file_name, names=fnames)

# print top rows
print("Top 5 rows")
print(df.head(5))
print()


# list the class label counts
print("Class label counts")
print(df['class'].value_counts())


# seperate X and y
x = df.drop('class', axis=1)
y = df['class']

# test nd training split. 80:20 ratio
trainX, testX, trainY, testY = train_test_split(x, y, test_size = 0.2)


# scale trainX and testX data values using standard scaler
sc=StandardScaler()

scaler = sc.fit(trainX)
trainX_scaled = scaler.transform(trainX)
testX_scaled = scaler.transform(testX)


# Create a MLP classifier object
# input layer has 4 nodes
# hidden layer 1 = 150
# hidden layer 2 = 100
# hidden layer 3 = 50
# max epochs = 300
# activation function is relu
# weight adjustment = adam

mlp_clf = MLPClassifier(hidden_layer_sizes=(150,100,50),
                        max_iter = 300,activation = 'relu',
                        solver = 'adam')

# train the MLP on the data
mlp_clf.fit(trainX_scaled, trainY)

# Model Evaluation
# predict on testX to get y_pred
y_pred = mlp_clf.predict(testX_scaled)

# print Accuracy score between testY and y_pred
print('Accuracy: {:.2f}'.format(accuracy_score(testY, y_pred)))

'''
# Plot confusion matrix
fig = ConfusionMatrixDisplay(mlp_clf, testX_scaled, testY, display_labels=mlp_clf.classes_)
fig.figure_.suptitle("Confusion Matrix for Iris Dataset")
plt.show()
'''
# Create a confusion matrix
matrix = confusion_matrix(testY, y_pred)
print('Confusion matrix')
print(matrix)

# Plot the confusion matrix
plt.matshow(matrix)
plt.title('Confusion Matrix')
plt.colorbar()
plt.show()

# print classification report
print(classification_report(testY, y_pred))
print()

# display loss curve
plt.plot(mlp_clf.loss_curve_)
plt.title("Loss Curve", fontsize=14)
plt.xlabel('Iterations')
plt.ylabel('Cost')
plt.show()

# predict on unseen data
x_new= [[5.5,6,2.5,3]]
x_new_scaled= scaler.transform(x_new)
y_new_pred = mlp_clf.predict(x_new_scaled)

print("Prediction is: ", y_new_pred)
print()

######################################################################
# Hyper Parametrer tuning
from sklearn.model_selection import GridSearchCV

# define the parameters to be used
# this is a dictionary specifying the parameters to search through
param_grid = {
    'hidden_layer_sizes': [(150,100,50), (120,80,40), (100,50,30)],
    'max_iter': [50, 100, 150],
    'activation': ['tanh', 'relu'],
    'solver': ['sgd', 'adam'],
    'alpha': [0.0001, 0.05],
    'learning_rate': ['constant','adaptive'],
}


# start selection of best parameters
# GridSearchCV is a powerful tool in scikit-learn
# that allows for exhaustive search over specified parameter
# values for an estimator that may be the best / optimum

# n_jobs=-1 indicates to use all available CPU cores to speed up the search
# cv = 5 indicates cross validation of 5 folds
grid = GridSearchCV(mlp_clf, param_grid, n_jobs= -1, cv=5)
grid.fit(trainX_scaled, trainY)

print("Best parameters after hyper parameter tuning")
print(grid.best_params_)
print()

# use the model with the best parameters
grid_predictions = grid.predict(testX_scaled) 

print('Accuracy with hyper parameter tuning')     
print('Accuracy: {:.2f}'.format(accuracy_score(testY, grid_predictions)))

print('Job Done')

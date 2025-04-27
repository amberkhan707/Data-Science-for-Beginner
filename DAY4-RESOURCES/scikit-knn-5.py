# Knn on all features of the data

import numpy as np
import sklearn
from sklearn import neighbors, datasets
from sklearn import preprocessing

n_neighbors = 3

# import some data to prepare model
# use iris data
iris = datasets.load_iris()
print("Data Loaded")

# prepare data
X = iris.data
y = iris.target


# split data into training and testing sets (80:20)

from sklearn.model_selection import train_test_split
# random split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=45)
# stratified split
#X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=45, stratify=y)

# check shape of the input splits
print("\nShape of Training :" , X_train.shape)
print("\nShape of Testing :" , X_test.shape)

# check shape of the output splits
print("\nShape of Training :" , y_train.shape)
print("\nShape of Testing :" , y_test.shape)

# create a classifier instance
knn=neighbors.KNeighborsClassifier(n_neighbors)
# pass data to classifier
knntrained=knn.fit(X_train,y_train)
print("KNN cassifier is trained and ready\n")

from sklearn import metrics
# predict for values of the test data
y_pred=knntrained.predict(X_test)
print("Prediction over\n")

# get accuracy info
score=metrics.accuracy_score(y_test,y_pred)
print(" y in test    y in prediction")
mismatch=0
for i in range(y_test.size):
    print("Test : " , y_test[i], " Predicted : ", y_pred[i])
    if y_test[i] != y_pred[i]:
        mismatch +=1

errr=mismatch / y_test.size * 100
accu= 100-errr

print("Computed Accuracy : " , accu , "% Error : " , errr , "%")
print()
print("Prediction accuracy from scorer: " , score)
print()

# print confusiion matrix
from sklearn.metrics import confusion_matrix

# Create confusion matrix
confusion_mat = confusion_matrix(y_test, y_pred)
print("\nConfusion matrix is : ")
print(confusion_mat)

# classification Report
from sklearn.metrics import classification_report
targets=['sentosa', 'versicolor', 'virginica']
print('\n Classification Report: \n', classification_report(y_test, y_pred, target_names=targets))

# Use model on unseen data of 2 samples in x_new
x_new=[[6.5,2.2,5.8,2.1],[2.5,2.8,3.5,4.1]]
y_new=knntrained.predict(x_new)

classes={0:'sentosa', 1:'versicolor', 2:'virginica'}
print("\nPredictions on unseen data")
print("Data sample : " , x_new[0] , "is ", classes[y_new[0]])
print("Data sample : " , x_new[1] , "is ", classes[y_new[1]])


# make prediction
# get user data
print("\nI am ready to predict for your input")
sl = float(input('Enter sepal length (cm): '))
sw = float(input('Enter sepal width (cm): '))
pl = float(input('Enter petal length (cm): '))
pw = float(input('Enter petal width (cm): '))

# predict for the above data from user
dataClass = knntrained.predict([[sl,sw, pl,pw]])
print('Prediction: '),

if dataClass == 0:
    print('Iris Setosa')
elif dataClass == 1:
    print('Iris Versicolour')
else:
    print('Iris Virginica')

print("\nprediction probability aross 3 classes: ")
print(knntrained.predict_proba([[sl,sw, pl,pw]]))

print("Done")


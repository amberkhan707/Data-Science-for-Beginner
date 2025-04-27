# Support Vector Machine
from sklearn import datasets
from sklearn import metrics
from sklearn.svm import SVC

# load the iris datasets
dataset = datasets.load_iris()
print("Data Loaded")

for i in range(len(dataset.data)):
    print(dataset.data[i], 'class: ', dataset.target[i] )

input('Hit enter to continue')

# fit a SVM model to the data
# instantiate a SVC object from Sklearn
model = SVC()

# fit data to the SVC 
model.fit(dataset.data, dataset.target)
print("Model is ready ! \n")

# Display model Details
print("Model details : ", model)
print()

print("Classes are : ", model.classes_)
print()

print("Support Vectors : \n" , model.support_vectors_)
print()

# make predictions on the entire data
actual = dataset.target
predicted = model.predict(dataset.data)
print()

# print target and predicted classes
for i in range(len(dataset.data)):
    print(dataset.data[i],
          'actual class: ', dataset.target[i],
          'predicted: ',predicted[i]  )

input("Enter to continue")


# summarize the fit of the model
print("Classification Report")
print(metrics.classification_report(actual, predicted))
print()

print("Confusion Matrix")
print(metrics.confusion_matrix(actual, predicted))
print()

print("Done")

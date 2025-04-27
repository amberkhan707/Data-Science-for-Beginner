# clustering using KMeans
from sklearn import datasets
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# data from iris
# import some data to play with
iris = datasets.load_iris()
print("Data Loaded\n")

x=iris.data
print("Data points : \n " , x)
print()

# visualize data on the first two parameters
plt.figure(1)
plt.scatter(x[:,0],x[:,1], label='True Position')
plt.title("Data points")
plt.show()

k=3  # 3 categories of iris
# perform clustering
# create Kmeans clustering object from sklearn
kmeans=KMeans(n_clusters=k, random_state=0)

# fit data to clusters
clustered= kmeans.fit(x)
print("Clustering Done\n")
print()

#display the labels of the above points
print("Labels of points are : \n" , clustered.labels_ )
print()

# display the cluster centers
print("Cluster Centers are : \n" , clustered.cluster_centers_ )
print()

# display the SSE
print("Total SSE is : " , clustered.inertia_ )
print()

# display number of iterations needed to converge
print ("No of iterations to converge : " , clustered.n_iter_)
print()

# visualize the clusters on scatter plot
plt.figure(2)
plt.scatter(x[:,0],x[:,1], c=clustered.labels_, cmap='rainbow')
plt.title("Clustered Data")
plt.show()

# add the centroid points also
plt.figure(3)
plt.scatter(x[:,0], x[:,1], c=clustered.labels_, cmap='rainbow')
#plt.scatter(clustered.cluster_centers_[:,0] ,clustered.cluster_centers_[:,1], color='black')
plt.plot(clustered.cluster_centers_[:,0] ,clustered.cluster_centers_[:,1], 'gx')

plt.show()

            
print("Predict New Value on user data")
# predict for new values [0.5,3.0 ,4.4,3.9]
print("prediction for [[0.5,3.0 ,4.4,3.9] : " ,clustered.predict([[0.5,3.0 ,4.4,3.9]]))
print()
  

print("Done")

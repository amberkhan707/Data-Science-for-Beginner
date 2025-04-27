# clustering using KMeans

# import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#from sklearn import datasets
from sklearn.cluster import KMeans 

# input values
x = np.array([[5,3],
     [10,15],
     [15,12],
     [24,10],
     [30,45],
     [85,70],
     [71,80],
     [60,78],
     [55,52],
     [80,91],
     [35,40],
     [40,40]])

print("Data points : \n " , x)

# visualize data
plt.figure(1)
plt.scatter(x[:,0],x[:,1], label='True Position')
plt.title("Data points")
plt.show()

# get number of clusters from user
k=int(input("How many clusters ? : "))

# perform clustering
# create Kmeans clustering object
kmeans=KMeans(n_clusters=k, random_state=40)

# fit data to clusters
clustered= kmeans.fit(x)
print("Clustering Done\n")
print()

#display the labels of the above points
print("Cluster labels of points are : \n" , clustered.labels_ )
print()

# display the cluster centers
print("Cluster Centers are : \n" , clustered.cluster_centers_ )
print()

# print points and cluster data
print("Labelled Data is ")
for i in range (len(x)):
    print(x[i] , clustered.labels_[i])
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
plt.scatter(clustered.cluster_centers_[:,0] ,clustered.cluster_centers_[:,1], color='black', marker='s' )

plt.title("Clustered Data with Centroids")
plt.xlabel("Value 1")
plt.ylabel("Value 2")

plt.show()

   
print("=============")

# predict for unseen data [0,0] and [40,43]
print("prediction for [0,0] and [40,43] : \n" ,clustered.predict([[0,0], [40,43]]))

# display the cluster centers
print("Cluster Centers are : \n" , clustered.cluster_centers_ )
print("Clusters are unchanged ")
print()

# User given value
x_new = int(input("Enter x value of new point: "))
y_new = int(input("Enter y value of new point: "))
p_new=[x_new,y_new]
print("Prediction for point", p_new," is : ", clustered.predict([p_new]))

print("Done")

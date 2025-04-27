#Simple Linear Regression
# import libraries
import numpy as np

# age vs glucoselevels [x,y] observations in data1
data1=[[43,99],[21,65],[25,79],[42,75],[57,87],[59,81],[30,66],[37,74],[32,64],[48,75]]
#data1=[[43,69],[21,65]]
n=len(data1)  # number of points
#liner regression model
#y=a+bx
#a= (sum(y)*sum(x**2) - sum(x) *sum(x*y))/ (n*sum(x**2) - sum(x)**2)
#b= (n*sum(x*y) - sum(x)* sum(y))/ (n*sum(x*x) -sum(x)**2)

# create a np array from data
ndata1=np.array(data1)
print (ndata1)

# calculate all the components for the formulae above
# sum(x)
sumx=0
for i in range(n):
    sumx=sumx+ndata1[i][0]

#sum(y)
sumy=0
for i in range(n):
    sumy=sumy+ndata1[i][1]

#sum(x*y)
sumxy=0
for i in range(n):
    sumxy=sumxy+ndata1[i][0]*ndata1[i][1]    

#sum(x**2)
sumxx=0
for i in range(n):
    sumxx=sumxx+ndata1[i][0]*ndata1[i][0]

#sum(y**2)
sumyy=0
for i in range(n):
    sumyy=sumyy+ndata1[i][1]*ndata1[i][1]

# print basic calculations
print(sumx, sumy, sumxy, sumxx, sumyy)

# calculate regression coefficients a and b
denom= (n*sumxx - sumx*sumx)
a= (sumy * sumxx - sumx * sumxy)/denom
b= (n*sumxy - sumx*sumy)/denom

# print coeff and equation

print( "Regression coeffs are" , a,b)
print()

print("Linear model equation is : ")
print('y= '+str(a) +' + '+ str(b)+'x')
print()

# using the model for prediction
# input age and predict the glucose level
print("Prediction Phase")
age =int(input("Enter the age :"))
glucose= a + b*age
print("Glucose level predicted by LR is : " ,glucose)
print()

print("Job over")


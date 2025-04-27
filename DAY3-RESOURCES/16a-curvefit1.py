import numpy as np
x = np.array([0.0, 1.0, 2.0, 3.0,  4.0,  5.0])
y = np.array([0.0, 0.8, 0.9, 0.1, -0.8, -1.0])


# polyfit fits a polynomial of specified degree across data points
#p(x) = p[0] * (x**deg) + ... + p[deg]
# generate a polynomial of order 3
z = np.polyfit(x, y, 3)
print(z)
print()

#It is convenient to use poly1d objects for dealing with polynomials:
# poly1d realises a polynomial over the values
p = np.poly1d(z)
print("the poly coefficients are : " , p)
print()

# lets calculate some values of polynomial
print("p(0.65)  is :" ,p(0.65))
print("p(2.5)  is :" ,p(2.5))
print("p(8)  is :" ,p(8))
print()


#High-order polynomials may oscillate wildly:
p30 = np.poly1d(np.polyfit(x, y, 30))
#RankWarning: Polyfit may be poorly conditioned...
print("Fitting a higher order polynomial")
print("P30(4) is : ", p30(4))
print("P30(5) is : ", p30(5))
print("P30(4.5) is : ", p30(4.5))
print()


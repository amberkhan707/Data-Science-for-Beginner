# program to fit a curve of any higher order to data points
# import libraries
import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as poly
# use of  poly  library of numpy

x = np.array([ 3.08,  3.1 ,  3.12,  3.14,  3.16,  3.18,  3.2 ,  3.22,  3.24,
    3.26,  3.28,  3.3 ,  3.32,  3.34,  3.36,  3.38,  3.4 ,  3.42,
    3.44,  3.46,  3.48,  3.5 ,  3.52,  3.54,  3.56,  3.58,  3.6 ,
    3.62,  3.64,  3.66,  3.68])

y = np.array([ 0.000857,  0.001182,  0.001619,  0.002113,  0.002702,  0.003351,
    0.004062,  0.004754,  0.00546 ,  0.006183,  0.006816,  0.007362,
    0.007844,  0.008207,  0.008474,  0.008541,  0.008539,  0.008445,
    0.008251,  0.007974,  0.007608,  0.007193,  0.006752,  0.006269,
    0.005799,  0.005302,  0.004822,  0.004339,  0.00391 ,  0.003481,
    0.003095])

#np.polynomial.polynomial.polyfit returns coefficients [A, B, C] to A + Bx + Cx^2 +...
#np.polyfit returns: ... + Ax^2 + Bx + C.
#polynomial of order 1

coef1 =poly.polyfit(x, y, 1)
print('Coefficients for order 1:',coef1)
print()

#polynomial of order 2
coef2 =poly.polyfit(x, y, 2)
print('Coefficients for order 2:',coef2)
print()

#polynomial of order 3
coef3 =poly.polyfit(x, y, 3)
print('Coefficients for order 3:',coef3)
print()

#np.polyfit returns: ... + Ax^3 + Bx^2 + Cx + D.
coef4 =poly.polyfit(x, y, 4)
print('Coefficients for order 4:',coef4)
print()

# order 15
coef7 =poly.polyfit(x, y,7)
print('Coefficients for order 15:',coef7)
print()

#
# yfit is the computed output
#polyval() is used to evaluate the polynomial
yfit1=poly.polyval(x,coef1)
yfit2=poly.polyval(x,coef2)
yfit3=poly.polyval(x,coef3)
yfit4=poly.polyval(x,coef4)
yfit7=poly.polyval(x,coef7)


# plot is the computed output
plt.scatter(x,y)
plt.plot(x,y,'k-',label='original y')
plt.plot(x,yfit1,'r-',label='computed y order 1')
plt.plot(x,yfit2,'g-',label='computed y order 2')
plt.plot(x,yfit3,'b-',label='computed y order 3')
plt.plot(x,yfit4,'m-',label='computed y order 4')
plt.plot(x,yfit7,'c-',label='computed y order 7')


plt.legend(loc='upper left')
plt.title('Actual y and Computed y with poly of order1,2,3 and 4')
plt.show()

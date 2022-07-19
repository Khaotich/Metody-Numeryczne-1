#Karol Pichurski Lista 3 Zadanie 4

from numpy import array
from scipy import linalg


a = array([[0,0,0,0,1],
           [1,1,1,1,1],
           [81,27,9,3,1],
           [625,125,25,5,1],
           [1296,216,36,6,1]])

b = array([[-1],
           [1],
           [3],
           [2],
           [-2]])


print(linalg.solve(a, b))
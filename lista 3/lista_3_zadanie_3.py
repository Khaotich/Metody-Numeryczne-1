#Karol Pichurski Lista 3 Zadanie 3

from numpy import array
from scipy import linalg


a = array([[0,0,2,1,2],
           [0,1,0,2,-1],
           [1,2,0,-2,0],
           [0,0,0,-1,1],
           [0,1,-1,1,-1]])

b = array([[1],
           [1],
           [-4],
           [-2],
           [-1]])

print(linalg.solve(a, b))
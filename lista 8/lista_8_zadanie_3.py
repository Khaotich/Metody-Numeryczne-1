#Karol Pichurski Lista 8 Zadanie 3

from scipy.linalg import eigh_tridiagonal
import numpy as np

n_10 = 10
d_10 = 2 * np.ones(n_10)
nd_10 = -1 * np.ones(n_10 - 1)
own_values_n_10, own_vectors_n_10 = eigh_tridiagonal(d_10, nd_10)

n_100 = 100
d_100 = 2 * np.ones(n_100)
nd_100 = -1 * np.ones(n_100 - 1)
own_values_n_100, own_vectors_n_100 = eigh_tridiagonal(d_100, nd_100)

print('Macierz n = ', n_10)
print('Wartości własne: ', own_values_n_10[:3], sep='\n')
print('Wektory własne: ', own_vectors_n_10[:, :3], sep='\n')

print('Macierz n = ', n_100)
print('Wartości własne: ', own_values_n_100[:3], sep='\n')
print('Wektory własne: ', own_vectors_n_100[:, :3], sep='\n')
#Karol Pichurski Lista 3 Zadanie 6

import numpy as np
import scipy.linalg as sp

n_5 = sp.hilbert(5)
n_10 = sp.hilbert(10)
n_20 = sp.hilbert(20)

print('Norma macierzy Hilberta dla n=5:', np.linalg.norm(n_5))
print('Norma macierzy Hilberta dla n=10:', np.linalg.norm(n_10))
print('Norma macierzy Hilberta dla n=20:', np.linalg.norm(n_20))

print('Wskaźnik uwarunkowania macierzy Hilberta dla n=5:', np.linalg.cond(n_5))
print('Wskaźnik uwarunkowania macierzy Hilberta dla n=10:', np.linalg.cond(n_10))
print('Wskaźnik uwarunkowania macierzy Hilberta dla n=20:', np.linalg.cond(n_20))
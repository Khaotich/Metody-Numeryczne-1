#Karol Pichurski Lista 8 Zadanie 1

from scipy.linalg import eig
import numpy as np

matrix = np.array([[-1, -4, 1], 
                   [-1, -2, -5],
                   [5, 4, 3]])

own_values, own_vectors = eig(matrix)
for i in range(len(own_values)): 
    print(f'Wartość własna: {own_values[i]}')
    print(f'Wektor własny: {own_vectors[i]}\n')
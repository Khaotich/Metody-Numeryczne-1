#Karol Pichurski
#Lista 1 / Zadanie 3

import numpy as np

A = np.array([[4, -2, 1], [-2, 4, -2], [1, -2, 4]])
B = np.array([[4, 2, 0], [2, 5, 2], [0, 2, 4]])
w = np.array([1, -2, 3])

print(f'A * B \n{A@B} \n')
print(f'A * w \n{A@w} \n')
print(f'B * (Aw) \n{B@(A@w)} \n')
print(f'Wyznacznik macierzy A \n{np.linalg.det(A)} \n')
print(f'Wyznacznik macierzy B \n{np.linalg.det(B)} \n')
print(f'Macierz odwrotna A \n{np.linalg.inv(A)} \n')
print(f'Macierz odwrotna B \n{np.linalg.inv(B)} \n')
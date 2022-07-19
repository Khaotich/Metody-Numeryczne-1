#Karol Pichurski Lista 8 Zadanie 2

from scipy.linalg import hilbert, eig

matrix = hilbert(6)
own_values, own_vectors = eig(matrix)

for i in range(len(own_values)):
    print(f'Wartości własne: {own_values[i]}')
    print(f'Wektory własne: {own_vectors[i]}\n')
#Karol Pichurski
#Lista 1 / Zadanie 4

from scipy import linalg

print(f'Macierz Hilberta dla n=4 \n{linalg.hilbert(4)}\n')
print(f'Macierz Hilberta odwrotna dla n=4 \n{linalg.inv(linalg.hilbert(4))}\n')
print(f'Macierz Hilberta dla n=8 \n{linalg.hilbert(8)}\n')
print(f'Macierz Hilberta odwrotna dla n=8\n{linalg.inv(linalg.hilbert(8))}\n')

for i in range(5, 21):
    print(f'Wyznacznik macierzy Hilberta dla n={i} \n{linalg.det(linalg.hilbert(i))}\n')
#Karol Pichurski, Metody Numeryczne 1, Raport Zaliczeniowy Zadanie 7

import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as la

#dane
R = np.linspace(0, 5, 10000)
E= np.array([0, 120, 120])
I = []

#obliczenia
for Ri in R:
    matrix = np.array([[1, -1, -1],
                       [3.5, Ri, 0],
                       [3.5, 0, 6.5]])

    I.append(la.solve(matrix, E)[1])

P = [I[i]**2 * R[i] for i in range(len(I))]

#wyniki końcowe
P_max = max(P)
R_max = R[P.index(max(P))]

#wykres
plt.plot(R, P, R_max, P_max, 'ro')
plt.legend(['P(R)', '$P_{max}$'])
plt.grid()
plt.title('Wykres zależności mocy od oporu P(R)')
plt.xlabel('R [Ω]')
plt.ylabel('P [W]')
plt.show()

#wyświetlenie wyników końcowych
print(f'Maksymalna moc wydzielona przez opornik wynosi: {round(P_max, 2)} [W]')
print(f'Wartość oporu dla maksymalnej mocy wynosi: {round(R_max, 2)} [Ω]')
#Karol Pichurski Lista 5 Zadanie 6

import numpy as np
import matplotlib.pyplot as plt


h = np.array([0, 1.525, 3.05, 4.575, 6.1, 7.625, 9.150])
rho = np.array([1, 0.8617, 0.7385, 0.6292, 0.5328, 0.4481, 0.3741])
find_h = 10.5
h_p = np.linspace(0, 10, 100)

w = np.polyfit(h, rho, 1)
w_ = np.poly1d(w)

print(f'p(10,5) = {w_(find_h)}')

plt.plot(h, rho, 'o', h_p, w_(h_p), '-')
plt.legend(['dane', 'prosta regresji'])
plt.xlabel('h')
plt.ylabel('p')
plt.title('Wykres zależności p(h)')
plt.grid()
plt.show()

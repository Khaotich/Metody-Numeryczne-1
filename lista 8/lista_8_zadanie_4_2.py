#Karol Pichurski Lista 8 Zadanie 4.2

import matplotlib.pyplot as plt
import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import eigsh

a = 4.6
n = 1000 
h = 2 * a/n
lam = 0.2
d = np.fromfunction(lambda i: 1/h**2 + 0.5*(-a+(i+1)*h)**2 + lam*(-a+(i+1)*h)**4, (n-1,), dtype=float)
g = -0.5/h**2 * np.ones(n - 2)
positions = [0, 1, -1]

data = [d.tolist(), g.tolist(), g.tolist()]
Hm = diags(data, positions, (n-1,n-1)).tocsc()
eH, vH = eigsh(Hm, k=4, sigma=0.0, which='LM')
xx = np.arange(h - a, a - h + 1e-12, h)

for i in range(4):
    plt.subplot(2, 2, i+1)
    nv = 1/np.sqrt((h*(vH[:, i]**2)).sum())
    plt.plot(xx, nv*vH[:, i])
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid()
    plt.title(f'E = {str(round(eH[i], 2))}')
plt.show()

print(f'Wartości własne\n{eH}')
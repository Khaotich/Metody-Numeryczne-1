#Karol Pichurski Lista 5 Zadanie 4

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import Akima1DInterpolator
from scipy.interpolate import PchipInterpolator


re = np.array([0.2, 2, 20, 200, 2000, 20000])
cp = np.array([103, 13.9, 2.72, 0.8, 0.401, 0.433])
find_point = [5, 50, 5000]

pchi = PchipInterpolator(re, cp)
aks = Akima1DInterpolator(re, cp)
xnew = np.arange(0, 30000, 0.1)

plt.plot(re, cp, 'o')
plt.plot(xnew, pchi(xnew), 'g')
plt.plot(xnew, aks(xnew), 'r')

plt.legend(['punkty', 'Spline hermitowski', 'Spline Akima'])
plt.title('Wykres $c_{D}$(Re)')
plt.ylabel('$c_{D}$')
plt.xlabel('Re')
plt.grid()
plt.xscale('log')
plt.yscale('log')
plt.show()

print(f'Dla akime splina: Re({find_point}) = {aks(find_point)}')
print(f'Dla hermitowskiego splina: Re({find_point}) = {pchi(find_point)}')
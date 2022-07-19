#Karol Pichurski Lista 5 Zadanie 5

import numpy as np
import matplotlib.pyplot as plt
from numpy.core.numeric import full
from scipy import interpolate


x = np.array([1.0, 2.5, 3.5, 4.0, 1.1, 1.8, 2.2, 3.7])
y = np.array([6.008, 15.722, 27.13, 33.772, 5.257, 9.549, 11.098, 28.828])

#f. liniowa i kwadratowa - interpolacja
f1 = interpolate.interp1d(x, y, kind='linear')
f2 = interpolate.interp1d(x, y, kind='quadratic')
x_new = np.arange(1.0, 4.0, 0.01)

#obliczenie błędów dopasowania 
f1_ = np.polyfit(x, y, 1, full=True)
f2_ = np.polyfit(x, y, 2, full=True)

print(f'Suma kwadratów odchyleń od wartości danych dla dopasowania liniowego: {f1_[1][0]}')
print(f'Suma kwadratów odchyleń od wartości danych dla dopasowania kwadratowego: {f2_[1][0]}')

# linia prosta - aproksymacja
polly = np.polyfit(x, y, 1)
polly_y = np.poly1d(polly)(x)

plt.plot(x, y, 'o')
plt.plot(x, polly_y, 'r')
plt.plot(x_new, f1(x_new), 'y')
plt.plot(x_new, f2(x_new), 'g')
plt.title('Wykres dopasowywania lini prostej, f. liniowej i f. kwdratowej')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['punkty', 'linia prosta', 'f. liniowa', 'f. kwadratowa'])
plt.grid()
plt.show()
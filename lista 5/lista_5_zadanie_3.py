#Karol Pichurski Lista 5 Zadanie 3

from numpy import array, arange, log, linspace, exp
from scipy import interpolate
import matplotlib.pyplot as plt


Re = array([0.2, 2, 20, 200, 2000, 20000])
cD = array([103, 13.9, 2.72, 0.8, 0.401, 0.433])
find = [5.50, 5000]
x = linspace(log(0.2), log(20000), 40)

w = interpolate.interp1d(log(Re), log(cD), kind='cubic')

print(find, exp(w(log(find))))

plt.plot(log(Re), log(cD), 'o', x, w(x), '-')
plt.title('Wykres $c_{D}$(Re)')
plt.ylabel('$c_{D}$')
plt.xlabel('Re')
plt.grid()
plt.legend(['dane', 'Linear Spline'])
plt.show()

#Dla innych metod spline np.cubic wykres totalnie się psuje.
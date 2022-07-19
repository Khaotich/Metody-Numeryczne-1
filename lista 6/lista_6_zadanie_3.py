#Karol Pichurski Lista 6 Zadanie 3

from numpy import array, linspace
from scipy import interpolate
from matplotlib import pyplot as plt

x = array([-2.2, -0.3, 0.8, 1.9])
y = array([-15.18, 10.962, 1.92, -2.04])
x_ = linspace(-3, 3, 100)

f = interpolate.UnivariateSpline(x, y)
fprim_1 = f.derivative(1)
fprim_2 = f.derivative(2)

print(f'f\'(0) = {fprim_1(0)}')
print(f'f\'\'(0) = {fprim_2(0)}')

plt.plot(x, y, '.')
plt.plot(x_, f(x_))
plt.plot(x_, fprim_1(x_))
plt.plot(x_, fprim_2(x_))
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.legend(['dane','dopasowany wielomian', 'f\'', 'f\'\''])
plt.title('Wykres danych i wielomianu')
plt.show()
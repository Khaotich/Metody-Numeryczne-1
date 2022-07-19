#Karol Pichurski Lista 5 Zadanie 1

from numpy import array, polyfit, poly1d, linspace, append
from matplotlib import pyplot


h = array([0, 3, 6])
p = array([1.225, 0.905, 0.652])

z = polyfit(h, p, 2)
w = poly1d(z)

x = linspace(0, 100, 1000)
y = array([])
for i in x: y = append(y, w(i))

pyplot.plot(x, y)
pyplot.xlabel('h')
pyplot.ylabel('p')
pyplot.title('Wykres p(h)')
pyplot.grid()
pyplot.show()
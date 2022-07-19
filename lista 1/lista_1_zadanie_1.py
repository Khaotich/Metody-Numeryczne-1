#Karol Pichurski
#Lista 1 / Zadanie 1

import numpy as np
from matplotlib import pylab


def f(x):
    return np.cos(x) - 3*np.sin(np.tan(x) - 1)


#funkcja porównuje pary y i sprawdza czy różnią się znakiem po czym zwraca ilość miejsc zerowych
def find_0(y):
    result = 0
    for i in range(len(y)-1):
        if (y[i] > 0 and y[i+1] < 0 ) or (y[i] < 0 and y[i+1] > 0 ): result +=1
    return result


n = 1000
x = np.linspace(0, 1.49, n)
y = []

for i in x:
    y.append(f(i))

pylab.plot(x, y)
pylab.title("Wykres funkcji f")
pylab.xlabel("X")
pylab.ylabel("Y")
pylab.grid(True)
pylab.show()

print("Ilość miejsc zerowych:", find_0(y))

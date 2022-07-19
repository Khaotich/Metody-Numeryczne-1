#Karol Pichurski
#Lista 1 / Zadanie 2

import numpy as np
from matplotlib import pylab as plt


#funkcja zwracająca n-wyrazów jako listę
def ciag(n):
    result = [0.1]
    for i in range(1, n):
        result.append(3.5 * result[i - 1] * (1 - result[i - 1]))
    return result


n = 100
x = np.linspace(0, n, n)
y = np.array(ciag(n))

plt.scatter(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
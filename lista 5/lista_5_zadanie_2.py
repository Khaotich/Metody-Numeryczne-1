#Karol Pichurski Lista 5 Zadanie 2

from numpy import array, polyfit, poly1d, linspace
from scipy import optimize


x = linspace(1, 3, 9)
y = array([-0.5403, -0.0104, 0.9423, 1.7445, 1.3073, -0.7718, -2.4986, -0.7903, 2.7334])

w = polyfit(x, y, 6)
w_ = poly1d(w)
w_prim = w_.deriv()
root1 = optimize.newton(w_, 1, fprime=w_prim)
root2 = optimize.newton(w_, 2, fprime=w_prim)
root3 = optimize.newton(w_, 3, fprime=w_prim)

print(f'Wartość pochodnej funkcji w x=2.1 {w_prim(2.1)}')
print(f'Pierwiastki funkcji to: {root1}, {root2}, {root3}')
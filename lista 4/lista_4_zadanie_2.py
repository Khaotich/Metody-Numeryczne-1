#Karol Pichurski Lista 4 Zadanie 2

from scipy.optimize import newton

f = lambda x,a: x**5-a
f_prime = lambda x,a: 5*x**4

x = range(2, 11)

print(newton(f, x, fprime=f_prime, args=(x,)))

#pierwiastki piątego stopnia z liczb od 2 do 10
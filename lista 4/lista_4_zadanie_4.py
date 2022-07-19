#Karol Pichurski Lista 4 Zadanie 4

from scipy import optimize
from numpy import tan, exp, array 

def f(xy):
    x, y = xy
    return [x + exp(-x) + y**3, x**2 + 2*x*y - y**2 + tan(x)]


n = 3
answers = []
x_ = [array([-1.27, -1.26]), array([-0.72, -0.70]), array([1.20, 1.21])]

for i in x_:
    x1 = optimize.root(f, i)
    x = round(x1.x[0], n)
    y = round(x1.x[1], n)
    if x**2 + y**2 <= 4 and [round(x1.x[0], n), round(x1.x[1], n)] not in answers:
        answers.append([round(x1.x[0], n), round(x1.x[1], n)])

print(answers)
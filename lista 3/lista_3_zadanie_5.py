#Karol Pichurski Lista 3 Zadanie 5


def gauss(a, b):
    n = len(a)
    p = len(b[0])
    det = 1
    for i in range(n - 1):
        k = i
        for j in range(i + 1, n):
            if abs(a[j][i]) > abs(a[k][i]):
                k = j
        if k != i:
            a[i], a[k] = a[k], a[i]
            b[i], b[k] = b[k], b[i]
            det = -det
 
        for j in range(i + 1, n):
            t = a[j][i]/a[i][i]
            for k in range(i + 1, n):
                a[j][k] -= t*a[i][k]
            for k in range(p):
                b[j][k] -= t*b[i][k]
 
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            t = a[i][j]
            for k in range(p):
                b[i][k] -= t*b[j][k]
        t = 1/a[i][i]
        det *= a[i][i]
        for j in range(p):
            b[i][j] *= t
    return b


#Zadanie 1 z listy 3
a1 = [[-1,1,-4], [2,2,0], [3,3,2]]
b1 = [[0], [1], [0.5]]

print('Zadanie 1:' , gauss(a1, b1))

#Zadanie 2 z listy 2
#Deklaruje już macierz A powstałą z wymnorzenia macierzy L i U
a2 = [[2,-3,-1], [3,2,-5], [1,4,-1]]
b2 = [[1], [-1], [2]]

print('Zadanie 2:' , gauss(a2, b2))

#zadanie 3 z listy 3 
a3 = [[0,0,2,1,2], [0,1,0,2,-1], [1,2,0,-2,0], [0,0,0,-1,1], [0,1,-1,1,-1]]
b3 = [[1], [1], [-4], [-2], [-1]]

print('Zadanie 3:' , gauss(a3, b3))


#Zadanie 4 z listy 3
a4 = [[0,0,0,0,1],
    [1,1,1,1,1],
    [81,27,9,3,1],
    [625,125,25,5,1],
    [1296,216,36,6,1]]

b4 = [[-1],[1],[3],[2],[-2]]

print('Zadanie 4:' , gauss(a4, b4))
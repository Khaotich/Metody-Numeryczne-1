#Karol Pichurski
#Lista 2 / Zadanie 5

from math import e

I = 1
for n in range(2, 21):
    I = e - n * I
    print(n ,'   ', I)

"""
Uważam że błąd pojawai się od n = 17 ponieważ
dla mniejszych n-ów wartość maleje, a dla n = 17
mamy większą wartość niż dla n = 16
"""
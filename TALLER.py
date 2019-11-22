from math import *
import math
import numpy as np

def collatz(numero):

    lista = [numero]
    while lista [-1] > 1:

        if lista [-1] % 2 == 0:

            lista.append(lista[-1] //2)
        else:

            lista.append(3*lista[-1] + 1)

    return lista
#PUNTO 1 A
print("Punto 1 A")
print(collatz(13))

#PUNTO C
print("Punto 1 C")
for a in range(1,101):
    print(collatz(a))

#PUNTO 1 D
print("Punto 1 D")
longmax = 1
contador = 1
r = int(math.pow(2, 15))

for b in range(1,r):

    long = len(collatz(b))
    if long > longmax:
        longmax = long
        contador = b

print("La secuencia mas larga es la de a = ", contador, ", tiene una longitud de ", longmax)



#PUNTO 2

def Ta_n (n,l):
    rta = 0
    for i in range (0, n):

        rta += ((-1)**i)*(l**(2*i))/ math.factorial(2*i)
    print(rta)

def a_n (n,l):

    rta = ((-1)**n)*(l**(2*n))/ math.factorial(2*n)
    print(rta)


print("Punto 2 A")

a_n(2, 2.5)

print("Punto 2 B")

Ta_n(5, 2.5)

print("Punto 2 C")

Ta_n(6,40)

print("valor errado")
print("numpy coseno" )
print(np.cos(40))

g = 40 - 2*math.pi*6
print("valor corregido")
Ta_n(6,g)


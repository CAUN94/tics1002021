import numpy
import random

matriz = numpy.zeros([3,7])


for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
        matriz[i,j] = random.randint(1,10) 

print(matriz)
print(matriz[0,:3])
print(matriz[1,:-3])
print(matriz[1,3:])

print(matriz[:2,2])

print(matriz[1:3,2:5])
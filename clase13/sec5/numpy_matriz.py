import numpy
import random

matriz = numpy.zeros([4,3])
print(matriz)

# print(matriz[0,0])

# matriz[0,0] = 1

# print(matriz)
# print(matriz[0,0])

for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
        matriz[i,j] = random.randint(1,10)
print(matriz)

print(matriz.max())
print(matriz.min())
print(matriz.mean())
print(matriz.sum())
print(matriz.prod())

print(matriz*10)
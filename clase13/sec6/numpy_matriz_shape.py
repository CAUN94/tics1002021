import numpy
import random

matriz = numpy.zeros([10,10])
print('-----')
print(matriz)


matriz[8,8] = 1
print('-----')
print(matriz)

matriz[5,:] = 2
print('-----')
print(matriz)

matriz[:,9] = 3
print('-----')
print(matriz)

matriz[3:7,:] = 5
print('-----')
print(matriz)

matriz[:,2:6] = 6
print('-----')
print(matriz)

matriz[5:9,3:7] = 8
print('-----')
print(matriz)




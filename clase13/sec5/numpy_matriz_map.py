import numpy

matriz = numpy.zeros([10,10])
print(matriz)

print('---')

matriz[0,:] = 1
print(matriz)

print('---')

matriz[1,1:9] = 2
print(matriz)

print('---')

matriz[2,2:-2] = 3
print(matriz)

print('---')

matriz[:,7] = 4
print(matriz)

print('---')

matriz[6:9,3] = 5
print(matriz)


print('---')

matriz[3:6,3:7] = 6
print(matriz)
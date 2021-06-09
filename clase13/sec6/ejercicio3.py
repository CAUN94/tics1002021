import numpy
import random

notas_a = numpy.random.random([40,3])*6 + 1 
notas_a = numpy.round(notas_a,1)
notas_f = numpy.zeros([40])
# print(notas_a)
# print(notas_f)

for i in range(notas_a.shape[0]):
    # suma = 0
    # for j in range(notas_a.shape[1]):
    #     suma += notas_a[i,j]
    # notas_f[i] = suma/3
    # print(notas_a[i,:])
    notas_f[i] = notas_a[i,:].mean()

notas_f = numpy.round(notas_f,1)
for i in range(len(notas_f)):
    print(f'Nota estudiante {i+1}: {notas_f[i]}')
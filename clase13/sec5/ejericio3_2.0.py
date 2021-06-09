import numpy

notas_e = numpy.random.random([40,3])*6 +1
notas_e = numpy.round(notas_e,1)
print(notas_e)
notas_f = numpy.zeros(40)

for i in range(notas_e.shape[0]):
    notas_f[i] = round(notas_e[i,:].mean(),1)

for i in range(notas_f.size):
    print(f"Nota estudiante {i+1}: {notas_f[i]}")
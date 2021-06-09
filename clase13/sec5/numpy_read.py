import numpy

lista = numpy.random.randint(1,10,size=10)

for i in lista:
    print(i,end=" ")
print()

for i in range(lista.size):
    print(lista[i],end=" ")
print()

for i in range(len(lista)):
    print(lista[i],end=" ")
print()

for i in range(lista.shape[0]):
    print(lista[i],end=" ")
print()
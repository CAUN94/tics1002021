import numpy

# lista = numpy.random.random(10)
# print(lista)

lista = numpy.random.randint(1,10,size=10)

print(f"Lista: {lista}")
print(f'El maximo valor es: {lista.max()}')
print(f'El minimo valor es: {lista.min()}')
print(f'El promedio valor es: {lista.mean()}')

a = numpy.zeros(10)
print(a)
print(a[2])

# b = numpy.ones(10)
b = numpy.ones((10,))
print(b)
print(b[2])

# c = numpy.full(10,7)
c = numpy.full((10,),7)
print(c)
print(c[2])

d = numpy.random.random(10)
print(d)
print(d[2])


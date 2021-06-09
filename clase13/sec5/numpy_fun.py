import numpy

x = numpy.array([1,2,3,4,5])
print(x)

#Aritmetica
print(f"Lista multiplicada por 200: {x*200}")
print(f"Lista suma de 200: {x+200}")
print(f"Lista resta de 200: {x-200}")
print(f"Lista division entera por 200: {x//200}")
print(f"Lista elevado por 2: {x**2}")

#Calculos rapidos
print(f'El maximo valor es: {x.max()}')
print(f'El minimo valor es: {x.min()}')
print(f'El promedio valor es: {x.mean()}')

#Funciones algebraicas
print(f'Sumatoria de x: {x.sum()}')
print(f'Productoria de x: {x.prod()}')

y = numpy.random.random(10)*80+20
print(y)
print(numpy.round(y,2))

x = numpy.array([1,2,3,4,5])
y = numpy.array([5,4,3,2,1])

print(x+y)
print(x**y)
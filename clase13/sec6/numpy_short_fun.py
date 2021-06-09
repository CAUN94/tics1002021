import numpy

lista = numpy.random.randint(10, size=10)
print(f"Lista: {lista}")
print(f"Lista -7: {lista-7}")
print(f"Lista +7: {lista+7}")
print(f"Lista //7: {lista//7}")
print(f"Lista *7: {lista*7}")
print(f"Lista **7: {lista**7}")

print(f"Min lista: {lista.min()}")
print(f"Max lista: {lista.max()}")
print(f"Mean lista: {lista.mean()}")

print(f"Suma valores lista: {lista.sum()}")
print(f"Productoria valores lista: {lista.prod()}")

# lista1 = numpy.random.random(10)
# print(f"Lista1: {lista1}")
# print(f"Lista redondeada a 1: {lista1.round(1)}")
# print(f"Lista redondeada a 2: {lista1.round(2)}")
# print(f"Lista redondeada a 3: {lista1.round(3)}")

lista1 = numpy.array([1,2,3,4])
lista2 = numpy.array([2,2,2,2])

print(lista1+lista2)
print(lista1*lista2)
print(lista1-lista2)
print(lista1//lista2)



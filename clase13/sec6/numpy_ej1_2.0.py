import numpy
# import random
# lista = []
# for i in range(10):
#     lista.append(random.randint(1,10))

# print(lista)

# max = lista[0]
# for i in range(10):
#     if lista[i] > max:
#         max = lista[i] 


# print(f'El max es {max}')

# lista = numpy.random.random(10,)
lista = numpy.random.randint(10, size=10)
print(lista)
max = numpy.max(lista)
print(f'El max es {max}')
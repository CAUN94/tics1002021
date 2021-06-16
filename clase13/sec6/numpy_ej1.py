import numpy
import random
lista1 = []
lista2 = []
for i in range(10):
    lista1.append(random.randint(1,10))
    lista2.append(random.randint(1,10))
print(lista1)
print(lista2)

max1 = lista1[0]
max2 = lista2[0]
for i in range(10):
    if lista1[i] > max1:
        max1 = lista1[i] 
    if lista2[i] > max2:
        max2 = lista2[i] 

print(f'El max1 es {max1}')
print(f'El max2 es {max2}')
import numpy
import random
lista = []
n = 200
for i in range(n):
    sub_lista = []
    for j in range(10):
        sub_lista.append(random.randint(1,10))
    lista.append(sub_lista)




for i in range(n):
    lista_acutal = lista[i]
    print(lista_acutal)
    max = lista_acutal[0]
    for j in range(10):
        if lista_acutal[j] > max:
            max = lista_acutal[j] 
    print(f'El max de la lista {i+1}: {max}')
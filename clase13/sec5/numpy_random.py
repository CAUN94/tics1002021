import random

lista = []
n = 10

for i in range(n):
    lista.append(random.randint(1,10))

print(f"Lista: {lista}")
max = lista[0]

for valor in lista:
    if valor > max:
        max = valor
        
print(f'El maximo valor es: {max}')
import random

lista = ['Tommy','John','Arthur','Michael','Polly']

i = random.randint(0,4)

print(lista[i])
lista = []
for i in range(20):
    lista.append(random.randint(1,10))
    print(lista)

for i in range(20):
    lista.pop()
    print(lista)

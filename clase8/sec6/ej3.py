lista = [1,10,1,2]

menor = lista[0]
for nr in lista:
    if nr < menor:
        menor = nr
print(f"El menor nr es {menor}")
lista = [10,3,2,5,6,7,9,2] # 4 pares

contador_de_pares = 0
for nr_de_lista in lista:
    if nr_de_lista % 2 == 0:
        contador_de_pares += 1

print(f"La lista tiene {contador_de_pares} nr pares")

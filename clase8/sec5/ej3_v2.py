lista = [2,3,4,4,5,6,7,8]

pares = []
for i in lista:
    if i%2 == 0:
        pares.append(i)

print(f'Tenemos {len(pares)} números pares')
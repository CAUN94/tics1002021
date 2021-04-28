lista = range(2,2001,2)

cont = 0
for i in lista:
    if i%2 == 0:
        cont = cont + 1 # cont += 1

print(f'Tenemos {cont} números pares')
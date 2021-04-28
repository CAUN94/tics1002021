lista = []
cant = int(input('Cuantos nr quiere agregar: '))

 
for i in range(cant):
    print(f"Nr {i+1}: ")
    nr = input()
    lista.append(nr)

print(list(lista))

# for i in lista:
#     print(i)


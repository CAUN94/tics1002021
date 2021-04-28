lista = []

for i in range(100):
    print(f"Nr {i+1}: ")
    nr = int(input())
    lista.append(nr)

suma = 0
for i in range(len(lista)):
    suma += lista[i]
print(f"El promedio es {suma/len(lista)}")




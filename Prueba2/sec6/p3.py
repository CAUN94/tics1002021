import random

def mostrar_matriz(matriz):
    print("-----")
    for i in matriz:
        print(i)
    print("-----")

def menor_distancia(matrix):
    lista_km = []
    for sub_matrix in matrix:
        suma = 0
        for j in sub_matrix:
            # print(j,end=',')
            suma += j
        # print()
        lista_km.append(suma)
    # print(lista_km)

    min_km = lista_km[0]
    min_i = 0
    for i in range(len(lista_km)):
        if lista_km[i] < min_km:
            min_km = lista_km[i]
            min_i = i

    print(f'El proveedor con menos km es el P{min_i+1} y lo hace en {min_km}')

def mayor_costo_promedio(matrix):
    lista_prom = []
    for sub_matrix in matrix:
        suma = 0
        for j in sub_matrix:
            # print(j,end=',')
            suma += j
        # print()
        lista_prom.append(suma/len(sub_matrix))
    # print(lista_prom)

    max_prom = lista_prom[0]
    max_i = 0
    for i in range(len(lista_prom)):
        if lista_prom[i] > max_prom:
            max_prom = lista_prom[i]
            max_i = i

    print(f'El proveedor con mayor costo promedio es el P{max_i+1} y lo hace en {int(max_prom)}')

def eliminar_servicio(conectividad, supermercado, proveedor):
    mostrar_matriz(conectividad)
    conectividad[supermercado-1][proveedor-1] = 0
    mostrar_matriz(conectividad)
    return conectividad

mconect = []
mtray = []
mcosto = []

for i in range(5):
    sub_mconect = []
    sub_mtray = []
    sub_mcosto = []
    for j in range(6):
        sub_mconect.append(1)
        sub_mtray.append(random.randint(10,40))
        sub_mcosto.append(random.randint(120,200))
    mconect.append(sub_mconect)
    mtray.append(sub_mtray)
    mcosto.append(sub_mcosto)

print('Matriz Conectividad')
mostrar_matriz(mconect)
print('Matriz Trayecto')
mostrar_matriz(mtray)
print('Matriz Costos')
mostrar_matriz(mcosto)

menor_distancia(mtray)
mayor_costo_promedio(mcosto)
newconect = eliminar_servicio(mconect,3,2)
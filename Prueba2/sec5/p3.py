import random

def mostrar_matriz(matriz):
    for sub_matriz in matriz:
        print(sub_matriz)

def menor_distancia(trayectos):
    min = sum(trayectos[0])
    min_i = 0
    for i in range(len(trayectos)):
        if sum(trayectos[i]) > min:
            min = sum(trayectos[i])
            min_i = i

    return min,i

def   mayor_costo_promedio(costos):
    max = sum(costos[0])/len(costos[0])
    max_i = 0
    for i in range(len(costos)):
        if sum(costos[i])/len(costos[i]) < max:
            max = round(sum(costos[i])/len(costos[i]),2)
            max_i = i

    return max,i

def eliminar_servicio(conectividad, supermercado, proveedor): 
    conectividad[proveedor-1][supermercado-1] = 0
    return conectividad

matriz_con = []
matriz_tra = []
matriz_cos = []

for i in range(5):
    sub_matriz_con = []
    sub_matriz_tra = []
    sub_matriz_cos = []
    for i in range(6):
        sub_matriz_con.append(1)
        sub_matriz_tra.append(random.randint(20,40))
        sub_matriz_cos.append(random.randint(100,180))
    matriz_con.append(sub_matriz_con)
    matriz_tra.append(sub_matriz_tra)
    matriz_cos.append(sub_matriz_cos)

print('Matriz Conectividad')
mostrar_matriz(matriz_con)
print('Matriz Trayectos')
mostrar_matriz(matriz_tra)
print('Matriz Costos')
mostrar_matriz(matriz_cos)

menor_trayecto, proveedor = menor_distancia(matriz_tra)
print(f'La menor cantidad de km recorridos es de {menor_trayecto} y la realiza el proveedor {proveedor}.')

mayor_costo_prom, proveedor = mayor_costo_promedio(matriz_cos)

print(f'El mayor costo promedio generado es de {mayor_costo_prom} u.m y lo realiza el proveedor {proveedor}.')

nueva_conectividad = eliminar_servicio(matriz_con,3,4)
print('Nueva Matriz')
mostrar_matriz(nueva_conectividad)
# a. Check:	(1 punto) Escribe un programa que cree, llene y despliegue el contenido de una matriz de 10x10. Cada casilla de la matriz debe contener un número aleatorio entre 0 y 9, excepto las casillas de las orillas  que solo deben contener el valor 0.  La siguiente figura muestra un ejemplo de esta matriz. 

#aleatorio
#matriz 10x10
#orilla son 0

import random

matriz = []

for i in range(10):
    lista = []
    for j in range(10):
        if i == 0 or j == 0 or i == 9 or j == 9:
            lista.append(0)
        else:
            lista.append(random.randint(0,9))
    matriz.append(lista)

for linea in matriz:
    print(linea)


rocoso = []
for i in range(1,9):
    for j in range(1,9):
        flag_es_rocoso = True
        if matriz[i-1][j] <= matriz[i-1][j-1] or matriz[i-1][j] <= matriz[i-1][j+1]:
            flag_es_rocoso = False
        if matriz[i][j] <= matriz[i][j-1] or matriz[i][j] <= matriz[i][j+1]:
            flag_es_rocoso = False
        if matriz[i+1][j] <= matriz[i+1][j-1] or matriz[i+1][j] <= matriz[i+1][j+1]:
            flag_es_rocoso = False
        if flag_es_rocoso:
            lista = [f"{i-1},{j}",f"{i},{j}",f"{i+1},{j}"]
            rocoso.append(lista)

for i in range(len(rocoso)):
    print(f"Cordón {i+1}: {rocoso[i]}")

print(f'Esta matriz contiene {len(rocoso)} cordones montañosos.')
   

# Al programa anterior, agrégale el código necesario para contar y desplegar por pantalla el número de cordones montañosos y la posición de las casillas en las que se encuentra cada cordón. Un cordón es un trío de casillas en línea vertical, cada una de ellas con valor mayor a su vecinas izquierda y derecha.  Por ejemplo, las casillas [5][3] , [6][3] y [7][3] conforman un cordón montañoso.  A continuación se muestra el tipo de mensaje que debe aparecer por pantalla: 
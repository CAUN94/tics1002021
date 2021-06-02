# Check: Escribe un programa que cree, llene y despliegue el contenido de una matriz de 10x10. Cada casilla de la matriz debe contener un número aleatorio entre 0 y 9, excepto las casillas de las orillas  que solo deben contener el valor 0.  La siguiente figura muestra un ejemplo de esta matriz. 

import random

matriz = []

for i in range(10):
    lista = []
    for j in range(10):
        if i == 0 or i == 9 or j == 0 or j == 9:
            lista.append(0)
        else:
            lista.append(random.randint(0,9))
    matriz.append(lista)

for lista in matriz:
    print(lista)

# Al programa anterior, agrégale el código necesario para contar y desplegar por pantalla el número de cordones montañosos y la posición de las casillas en las que se encuentra cada cordón. Un cordón es un trío de casillas en línea vertical, cada una de ellas con valor mayor a su vecinas izquierda y derecha.  Por ejemplo, las casillas [5][3] , [6][3] y [7][3] conforman un cordón montañoso.  A continuación se muestra el tipo de mensaje que debe aparecer por pantalla: +

cordon = []

for i in range(1,9):
    for j in range(1,9):
        flag_cumple_con_ser_cordon = True
        # Estoy en la posición [j,i]
        if matriz[j-1][i-1] >= matriz[j-1][i] or matriz[j-1][i+1] >= matriz[j-1][i]:
            flag_cumple_con_ser_cordon = False

        if matriz[j][i-1] >= matriz[j][i] or matriz[j][i+1] >= matriz[j][i]:
            flag_cumple_con_ser_cordon = False

        if matriz[j+1][i-1] >= matriz[j+1][i] or matriz[j+1][i+1] >= matriz[j+1][i]:
            flag_cumple_con_ser_cordon = False
        
        if flag_cumple_con_ser_cordon == True:
            # print(f"i:{i},j:{j}")
            # print(matriz[j-1][i-1],end= ' ')
            # print(matriz[j-1][i],end= ' ')
            # print(matriz[j-1][i+1])
            # print(matriz[j][i-1],end= ' ')
            # print(matriz[j][i],end= ' ')
            # print(matriz[j][i+1])
            # print(matriz[j+1][i-1],end= ' ')
            # print(matriz[j+1][i],end= ' ')
            # print(matriz[j+1][i+1])
            cordon.append(f'[{i},{j}]')
            

matriz = [[1,2,3,4],[4,52,6,4],[7,8,9,4],[7,8,9,4]] # 4x4

max = matriz[0][0]


for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] > max:
            max = matriz[i][j]

print(f"El maximo valor es {max}")
        


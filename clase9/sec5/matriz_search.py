matriz = [[1,2,3,4],[4,5,6,4],[7,8,9,4],[7,8,9,4]] # 4x4

nr = int(input('Nr: '))

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == nr:
            print(f"El producto {nr} se encuentra en: {i},{j}")
        


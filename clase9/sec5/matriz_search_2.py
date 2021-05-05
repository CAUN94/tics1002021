matriz = [[1,2,3,4],[4,5,6,4],[6,6,6,6],[7,8,9,20]] # 4x4

nr = int(input('Nr: '))
encontrado = False

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == nr:
            print(f"El producto {nr} se encuentra en: {i},{j}")
            encontrado = True
            break
    if encontrado:
        break  


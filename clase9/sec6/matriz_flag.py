matriz = [[1,8,3,4],[4,8,6,7],[7,8,9,10]] # 3x4 

nr = int(input('Que quieres buscar? '))

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j],end=' ')
    print('')

print('')
print('Buscando...')
print('')

encontrado = False

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == nr:
            print(f"Esta en este lugar {i},{j}")
            encontrado = True
            break
    if encontrado:
        break




nr = int(input('Nr de filas: '))

valor = 1

for i in range(1,nr+1):
    for j in range(i):
        print(valor,end=' ')
        valor += 1
    print('')
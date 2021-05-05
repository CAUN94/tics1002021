nr = int(input('Nr: '))

cont = 1
for i in range(1,nr+1):
    for j in range(1,i+1):
        print(cont,end=' ')
        cont = cont + 1
    print('')
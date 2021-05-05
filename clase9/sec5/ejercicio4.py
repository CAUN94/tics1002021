nr = int(input('Nr: '))

suma = 0
for i in range(1,nr+1):
    factorial = 1
    for j in range(1,i+1):
        factorial = factorial * j
    print(f'Factorial de {i} es {factorial}')
    suma = suma + factorial

print(f"El resultado final es {suma}")
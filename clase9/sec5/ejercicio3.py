nr = int(input('Nr: '))

suma = 0
for i in range(1,nr+1):
    for j in range(1,i+1):
        print(f"{i}**{j}")
        suma += i**j
    print('')

print(f"El resultado final es {suma}")
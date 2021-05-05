nr = int(input('Dame un nr: '))
respuesta = 0

for i in range(1,nr+1):
    N = 1 # N!
    for j in range(1,i+1):
        print(f"{N}*{j}",end=" ")
        N *= j
    print(f' :N factorial de {i} es {N}')
    respuesta += N

print(f"La respuesta es {respuesta}")
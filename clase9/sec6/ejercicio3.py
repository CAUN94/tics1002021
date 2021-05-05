nr = int(input('Dame un nr: '))
respuesta = 0
# print('i**j')
for i in range(1,nr+1):
    for j in range(1,i+1):
        respuesta += i**j
        # print(f'{i}**{j}',end='')
    # print('')
print(f"La respuesta es {respuesta}")
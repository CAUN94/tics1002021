def add_worke_name(cant):
    list_name = []

    for i in range(cant):
        name = input('Nombre trabajador: ')
        list_name.append(name)

    return list_name

def list_week_km():
    week_km = []

    for i in range(5):
        km = int(input('Km del día: '))
        week_km.append(km)

    return week_km

def sum_list_week_km(lista):
    sum = 0
    for i in lista:
        sum += i

    return sum
    # return sum(lista)


# print(add_worke_name(10))
# print(list_week_km())
# print(sum_list_week_km([1,2,3,4,5]))

def max_index_km(lista):
    max_km = lista[0]
    max_i = 0

    for i in range(len(lista)):
        if lista[i] > max_km:
            max_km = lista[i]
            max_i = i
    
    return max_i


cantidad = int(input('Cantidad de trabajadores: '))

names = add_worke_name(cantidad)

max_km = []

for name in names:
    print(f'Nombre {name}')
    week_km = list_week_km()
    max_km.append(sum_list_week_km(week_km))

max_index = max_index_km(max_km)

print(f'El trabaador que más km recorrio fue {names[max_index]} con {max_km[max_index]} kms')


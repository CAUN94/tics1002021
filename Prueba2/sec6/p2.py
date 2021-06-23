def nom_lista_fun(cant):
    nom_lista = []

    for i in range(cant):
        nombre = input('Ingresa el nombre del trabajador: ')
        nom_lista.append(nombre)

    return nom_lista

def km_rec_fun():
    km_rec = []
    for i in range(1,6):
        km = int(input(f'Ingresa cantidad día {i}: '))
        km_rec.append(km)

    return km_rec


def sum_km_rec_fun(lista):
    # return sum(lista)
    sum = 0
    for i in lista:
        sum += i

    return sum

def max_index_km_fun(lista):
    max_km = lista[0]
    max_i = 0

    for i in range(len(lista)):
        if lista[i] > max_km:
            max_i = i
            max_km = lista[i]

    return max_i


cantidad = int(input('Cantidad de personas: '))
lista_nombres = nom_lista_fun(cantidad)
lista_km_trabajadores_semanal = []

for trabajador in lista_nombres:
    lista_km_trabajador = []
    print(trabajador)
    lista_km = km_rec_fun()
    lista_km_trabajadores_semanal.append(sum_km_rec_fun(lista_km))

max_i = max_index_km_fun(lista_km_trabajadores_semanal)

print(f"El trabajador que más km recorrio fue {lista_nombres[max_i]} y recorriio {lista_km_trabajadores_semanal[max_i]}")
    
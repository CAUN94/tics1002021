estudiante = []

nombre = 'Cristóbal '
estudiante.append(nombre)
apellido = 'Ugarte'
estudiante.append(apellido)
edad = '26'
estudiante.append(edad)
notas = [5,4,5,7]
estudiante.append(notas)

print(list(estudiante))
estudiante[2] = '27'
print(list(estudiante))



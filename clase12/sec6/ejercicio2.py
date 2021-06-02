# La consultora AprendiendoJuntos, requiere que se construya un programa en Python que califique un examen de 6 preguntas de selección múltiple a un curso de n estudiantes. Las preguntas que se deben mostrar a cada uno de los estudiantes están almacenadas en la siguiente lista:
# preguntas = ['P1: ¿Con cuál palabra reservada se define una función',
# 'P2: ¿Cómo se llama la función que retorna el largo de un texto o lista',
# 'P3: En este ramo, ¿en qué lenguaje se programa?',
# 'P4: ¿Con cuál palabra reservada se retorna un valor',
# 'P5: ¿Cuál es el nombre de la función que imprime un texto?',
# 'P6: ¿Cómo se define una lista vacía?']

# Las estructuras de las alternativas de cada pregunta se encuentran en la siguiente matriz de 3x6
# respuestas = [
# ["a.fun","b.funtion","c.def"],
# ["a.len","b.leng","c.lengh"],
# ["a.R","b.Python","c.C++"],
# ["a.return","b.break","c.ret"],
# ["a.Print()","b.print","c.print()"],
# ["a.lista=[]","b.lista","c.lista=0"]]

# Finalmente, las respuestas correctas se encuentran en la siguiente lista: 
# respuestas_correctas = ['c','a','b','a','c','a']

# Check: AprendamosJuntos, requiere que se cree una función que permita ingresar el nombre completo de cada uno de los alumnos inscritos en el examen.
# Check: Luego es necesario que cada alumno, identificado por su nombre de inscripción, se le muestren las 6 preguntas con cada una de las alternativas. 
# Check: Cada estudiante, debe ingresar las respuestas seleccionada a cada pregunta. El programa debe indicar de inmediato si la respuesta ingresada por el estudiante está buena o mala.
# Check: Al final del examen se debe mostrar la nota del estudiante, calculada como la suma de las respuestas correctas más un punto base
# Check: Finalmente es necesario, que mediante el uso de funciones permita calcular el promedio de notas del curso que rindió los exámenes (promedio de notas obtenidos por cada alumno, que se almacenó en una lista)

def ingresar_estudiantes(cantidad):
    estudiantes = []
    for i in range(cantidad):
        estudiante = input(f'Nombre del estudiante numero {i+1}: ')
        estudiantes.append(estudiante)

    return estudiantes

def promedio_notas_estudiantes(notas):
    sum = 0
    cant = len(notas)

    for nota in notas:
        sum += nota
    
    return sum/cant

preguntas = ['P1: ¿Con cuál palabra reservada se define una función',
'P2: ¿Cómo se llama la función que retorna el largo de un texto o lista',
'P3: En este ramo, ¿en qué lenguaje se programa?',
'P4: ¿Con cuál palabra reservada se retorna un valor',
'P5: ¿Cuál es el nombre de la función que imprime un texto?',
'P6: ¿Cómo se define una lista vacía?']

respuestas = [
["a.fun","b.funtion","c.def"],
["a.len","b.leng","c.lengh"],
["a.R","b.Python","c.C++"],
["a.return","b.break","c.ret"],
["a.Print()","b.print","c.print()"],
["a.lista=[]","b.lista","c.lista=0"]]

respuestas_correctas = ['c','a','b','a','c','a']

cantidad = int(input('Cantdad de estudiantes: '))
estudiantes = ingresar_estudiantes(cantidad)

lista_notas = []

for i in range(cantidad):
    print(f'Estudiante: {estudiantes[i]}')
    print('Preguntas: ')
    nota = 1
    
    for j in range(len(preguntas)):
        print(preguntas[j])
        for k in range(len(respuestas[j])):
            print(respuestas[j][k])

        respuestas_estudiante = input('Ingresar respuesta: ')

        if respuestas_estudiante == respuestas_correctas[j]:
            print('Respuesta Correcta')
            nota += 1
        else:
            print(f'Error la respuesta correcta es {respuestas_correctas[j]}')
    
    print(f'La nota de {estudiantes[i]} es {nota}')
    lista_notas.append(nota)
    print('\n\n')

print(promedio_notas_estudiantes(lista_notas))

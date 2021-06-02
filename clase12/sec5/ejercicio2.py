# Ejercicio 2
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
# check: Al final del examen se debe mostrar la nota del estudiante, calculada como la suma de las respuestas correctas más un punto base
# Finalmente es necesario, que mediante el uso de funciones permita calcular el promedio de notas del curso que rindió los exámenes (promedio de notas obtenidos por cada alumno, que se almacenó en una lista)


def ingresar_estudiantes(nr):
    estudiantes = []
    for i in range(nr):
        estudiante = input('Nombre estudiante: ')
        estudiantes.append(estudiante)
    return estudiantes

def promedio_notas_curso(notas):
    sum_notas = 0
    for nota in notas:
        sum_notas += nota
    return sum_notas/len(notas)

preguntas = ['P1: ¿Con cuál palabra reservada se define una función', #0
'P2: ¿Cómo se llama la función que retorna el largo de un texto o lista', #1
'P3: En este ramo, ¿en qué lenguaje se programa?', #2
'P4: ¿Con cuál palabra reservada se retorna un valor', #3
'P5: ¿Cuál es el nombre de la función que imprime un texto?', #4
'P6: ¿Cómo se define una lista vacía?'] #5

respuestas = [
["a.fun","b.funtion","c.def"], #0 hay una lista con las respuesta
["a.len","b.leng","c.lengh"], #1 hay una lista con las respuesta
["a.R","b.Python","c.C++"], #2 hay una lista con las respuesta
["a.return","b.break","c.ret"], #3 hay una lista con las respuesta
["a.Print()","b.print","c.print()"], #4 hay una lista con las respuesta
["a.lista=[]","b.lista","c.lista=0"]] #5 hay una lista con las respuesta

respuestas_correctas = ['c','a','b','a','c','a']  # 0,1,2,3,4,5

nr = int(input('Cantidad de estudiantes: '))
estudiantes = ingresar_estudiantes(nr)
notas = []

for estudiante in estudiantes:
    print(f'Estudiante {estudiante}')
    nota = 1
    for i in range(len(preguntas)):
        print(preguntas[i])
        for j in range(len(respuestas[i])):
            print(respuestas[i][j])
        respuesta = input('Respuesta: ')

        if respuesta == respuestas_correctas[i]:
            print('Correcto')
            nota += 1
        else:
            print('Incorreco')
    notas.append(nota)
    print(f"La nota de {estudiante} es {nota}")

print(promedio_notas_curso(notas))
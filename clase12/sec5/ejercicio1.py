# El juego del quemado consiste en adivinar una palabra aleatoria. Para esto el jugador debe adivinar las letras que componen la palabra hasta finalmente completar la palabra.
# En esta versión del “quemado” el jugador no tiene límite de intentos, pero si ingresa 5 letras incorrectas el jugador pierde. Si adivina todas las letras de la palabra gana el juego.
# Cuando el jugador acumula 5 errores se finaliza el juego y se despliega un menú que le pregunta si quiere adivinar la palabra en 3 intentos.
# Mecánica del juego
# 1.	Check: Obtener palabra aleatoria que debe adivinar el jugador de una lista de animales.
# 2.	Check: Mostrar por pantalla tantas líneas como letras tiene la palabra a adivinar.
# 1.	Check: El jugador ingresa una letra.
# 2.	Check: Comprobar si la letra existe en la palabra.
# 3.	Check: Si la letra está en la palabra reemplazarla en la/s línea/s correspondientes.
# 4.	Check: Si completa la palabra, se termina el juego y el usuario gana.
# 5.	Si acumula 5 errores y no ha adivinado la palabra, se finaliza el juego y se le da la posibilidad de adivinar la palabra en 3 intentos.

# Aleatoria
# Ciclo que mantiene el juego funcionando
# If con una condición intentos
# Otro ifo para adivinar palabras
# Menu
# Tener lista de animales

import random

lista_animales = ['gato','perro','caballo','tigre','leon','pantera']
largo_lista = len(lista_animales)
valor_aleatorio = random.randint(0,largo_lista-1)
palabra_secreta = lista_animales[valor_aleatorio]

#palabra_secreta = lista_animales[random.randint(0,len(lista_animales)-1)]

intentos = 0
lista_de_letras_acertadas = []
for i in palabra_secreta:
    print('-',end="")
print('')
while True:

    letra_usuario = input('Ingresar una letra en minuscula: ')

    flag_existe_letra = False
    for i in palabra_secreta:
        if i == letra_usuario:
            flag_existe_letra = True
            lista_de_letras_acertadas.append(i)
    
    if flag_existe_letra:
        print('Letra Correcta')
    else:
        print('Letra no encontrada')
        intentos += 1

    acertadas = 0
    for i in palabra_secreta:
        if i in lista_de_letras_acertadas:
            print(i,end="")
            acertadas += 1
        else:
            print('-',end="")
    print('')

    if acertadas == len(palabra_secreta):
        print('Ganaste')
        break


    if intentos >= 5:
        print('Tienes 3 intentos para adivinar la palabra')
        flag_dio_respuesta_correcta = False
        for i in range(3):
            respuesta = input('La palabra es: ')
            if respuesta == palabra_secreta:
                flag_dio_respuesta_correcta = True
                break

        if flag_dio_respuesta_correcta:
            print('Ganaste')
        else:
            print('Perdiste')
        print('Juego Terminado')
        break

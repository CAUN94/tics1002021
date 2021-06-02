# Ejercicio 1
# El juego del quemado consiste en adivinar una palabra aleatoria. Para esto el jugador debe adivinar las letras que componen la palabra hasta finalmente completar la palabra.
# En esta versión del “quemado” el jugador no tiene límite de intentos, pero si ingresa 5 letras incorrectas el jugador pierde. Si adivina todas las letras de la palabra gana el juego.
# Cuando el jugador acumula 5 errores se finaliza el juego y se despliega un menú que le pregunta si quiere adivinar la palabra en 3 intentos.
# Mecánica del juego
# 1.	Obtener palabra aleatoria que debe adivinar el jugador de una lista de animales.
# 2.	Mostrar por pantalla tantas líneas como letras tiene la palabra a adivinar.
# 1.	El jugador ingresa una letra.
# 2.	Comprobar si la letra existe en la palabra.
# 3.	Si la letra está en la palabra reemplazarla en la/s línea/s correspondientes.
# 4.	Si completa la palabra, se termina el juego y el usuario gana.
# 5.	Si acumula 5 errores y no ha adivinado la palabra, se finaliza el juego y se le da la posibilidad de adivinar la palabra en 3 intentos.

#debo usar random
#recorrer una palabra
#ciclo con un break que se corta cuando es igual a 5
#en la que tengo 3 intentos para adivinar 
#la lista de animales la creo yo
#contar letras y mostrar referencia en pantalla

import random

lista_palabras = ['gato','perro','caballo']

largo = len(lista_palabras)

aleatorio = random.randint(0, largo-1) 
palabra_secreta = lista_palabras[aleatorio]

contador_errores = 0
lista = [] #Letras que han sido correctas

print('Palabra: ', end='')
# for i in range(len(palabra_secreta)):
for i in palabra_secreta:
    print('-',end='')

print('')

while True: 
    letra_usuario = input('Dame una letra en minuscula: ')

    flag = False
    for letra in palabra_secreta:
        if letra == letra_usuario:
            lista.append(letra)
            flag = True
    

    if flag == False:
        print('No esta')
        contador_errores += 1

    print('Palabra: ', end='')


    letras_correctas = 0

    for letra_s in palabra_secreta:
        if letra_s in lista:
            letras_correctas += 1
            print(letra_s, end='')
        else:
            print('-', end='')
    
    if letras_correctas == len(palabra_secreta):
        print('')
        print('Ganaste')
        break

    print('')


    if contador_errores == 5:
        print('Cometiste 5 errores')
        print('Que quieres hacer?')
        print('a) Intentar adivinar')
        print('b) Salir del juego')
        r = input('Alternativa: ')
        if r == 'a':
            flag_adivino = False
            for i in range(3):
                respuesta = input('Adivina la palabra: ')
                if respuesta == palabra_secreta:
                    print('Ganaste')
                    flag_adivino = True
                    break
            if flag_adivino == False:
                print('No Adivinaste')

        print('Juego Terminado')   
        print('')
        print('')
        print('')
        print('Que quieres hacer?')
        print('a) Volver a jugar')
        print('b) Salir del juego')
        r = input('Alternativa: ')
        if r == 'b':
            break
        else:
            aleatorio = random.randint(0, largo-1) 
            palabra_secreta = lista_palabras[aleatorio]

            contador_errores = 0
            lista = []

            print('Nueva Palabra: ', end='')
            # for i in range(len(palabra_secreta)):
            for i in palabra_secreta:
                print('-',end='')

            print('')



    



s = input('Ingrese su sexo H/M o escriba Salir para finalizar:')
kg = float(input('Ingrese su peso en Kg:'))
cm = float(input('Ingrese su altura en cm:'))
años = float(input('Ingrese su peso en años:'))
print('según la siguiente tabla usted hacer:')
print('a) Poco o nada de ejercicio')
print('b) Ejercicio ligero')
print('c) Ejercicio moderado')
print('d) Soy deportista')
print('e) Soy atleta')

alternativa = input('Alternativa a, b, c, d, e?:')

if alternativa == 'a':
    factor = 1.2
elif alternativa == 'b':
    factor = 1.375
elif alternativa == 'c':
    factor = 1.55
elif alternativa == 'd':
    factor = 1.72
elif alternativa == 'e':
    factor = 1.9

if s == 'H':
    TMB = 66 + (13.7 * kg) + (5 * cm) - (6.75 * años)
elif s == 'M':
    TMB = 65.5 + (9.6 * kg) + (1.8 * cm) - (4.7 * años)

TMB *= factor

print(f'Su TMB es {TMB}')

while True:
    print('a) Desea conocer como esta su alimentación? b) Salir del programa')

    r = input('¿Qué opción desea? a/b:')

    if r == 'a':
        hc = float(input('¿cuántos gramos de hidrato de carbono consume al día?:'))
        p = float(input('¿cuántos gramos de proteínas consume al día?:'))
        g = float(input('¿cuántos gramos de grasa consume al día?:'))

        calorias = hc*4 + p*4 + g*9

        calor_f = (TMB-calorias)*30

        if calor_f < 0:
            calor_f *= -1
            kilos = calor_f/7000
            print(f'Usted subira {kilos}kg cada 30 días')
        else :
            kilos = calor_f/7000
            print(f'Usted bajara {kilos}kg cada 30 días')
        break
    if r == 'b':
        print('Programa finalizado')
        break

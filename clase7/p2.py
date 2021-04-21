while True:
    c1 = input('¿Se comprobó dirección? (SI/NO)')

    if c1 == 'NO':
        print('Rechaza solicitud de préstamo')
        break

    c2 = input('¿Se comprobó identidad? (SI/NO)')

    if c2 == 'NO':
        print('Rechaza solicitud de préstamo')
        break

    c3 = input('¿Monto préstamo es menor que sueldo mes? (SI/NO)')

    if c1 == 'SI' and c2 == 'SI' and c3 == 'SI':
        print('Aprueba préstamo inmediatamente')
        break

    c4 = input('¿Monto préstamo es >= que sueldo mes? (SI/NO)')
    c5 = input('Propósito del préstamo Comprar casa (1) Pago impuestos (2) Otro (3)')
    c6 = input('¿Es propietario de casa? (SI/NO)')

    if c1 == 'SI' and c2 == 'SI' and c5 == '1':
        print('Aprueba préstamo inmediatamente')
        break
    elif c1 == 'SI' and c2 == 'SI' and c4 == 'SI' and c5 == '2':
        print('Aprueba préstamo inmediatamente')
        break
    elif c1 == 'SI' and c2 == 'SI' and c4 == 'SI' and c5 == '3':
        print('Aprueba préstamo inmediatamente')
        break

    break
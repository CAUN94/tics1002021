V = 0
A = 0
I = 0
G = 0



dividendo = 0

while True:
    r = int(input('Ingrese notas en formato 4331 o 0 para terminar:'))

    if r == 0:
        break

    cont = 0
    while(r > 0):
        digito = r - (r//10)*10
        r = r//10
        if cont == 0:
            G += digito
        elif cont == 1:
            I += digito
        elif cont == 2:
            A += digito
        elif cont == 3:
            V += digito  
        cont += 1   
    dividendo += 1   

    
print(f'Nota promedio del producto V: {V/dividendo}')
print(f'Nota promedio del producto A: {A/dividendo}')
print(f'Nota promedio del producto I: {I/dividendo}')
print(f'Nota promedio del producto G: {G/dividendo}')
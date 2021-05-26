def first_function():
    print('Hola')

def second_function(nombre):
    print(f'Hola {nombre}')

def third_function(nombre,apellido):
    print(f'Hola {nombre} {apellido}')


def four_function(x):
    for i in range(x):
        for j in range(x):
            if i == 0 or j == 0 or i == x-1 or j == x-1:
                print('x',end=" ")
            else:
                print('o',end=" ")
        print('')

def five_function(x):
    fact = 1
    for i in range(1,x+1):
        fact *= i

    return fact

def six_function():
    first_function()
    second_function('Andres')

def seven_function(x):
    if x == 1:
        return x
    x = seven_function(x-1)

def eight_function(nombre = 'Jon',apellido = 'Doe'):
    print(f'Hola {nombre} {apellido}')

first_function()
second_function('Cris')
first_function()
second_function('Andres')

third_function('Andres','Vergara')

four_function(20)

fact = five_function(10)
print(fact)

six_function()

x = seven_function(10)
print(x)

eight_function()
eight_function('Cris')
eight_function('Cris','Ugarte')
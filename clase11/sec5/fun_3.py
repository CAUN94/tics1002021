def message(nombre):
    print(f"Hola {nombre}")

def message_complete_name(nombre,apellido):
    print(f"Hola {nombre} {apellido}")

def message_cant(num):
    for i in range(num):
        print('Hola')




message('Cristóbal')
message('Javier')
message('Jon')
message('Jane')

message_complete_name('Cristóbal','Ugarte')

message_cant(10)
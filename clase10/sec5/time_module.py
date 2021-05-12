import time
import math

# print('Cargando...')

# time.sleep(2)

# print('Bienvenido')

a = time.time()


print(f'Today is {time.ctime()}')
nombre = input('Como te llamas? ')

b = time.time()

seg = math.floor(b-a)

print(f"{nombre} tardaste {seg} segundos en responder")


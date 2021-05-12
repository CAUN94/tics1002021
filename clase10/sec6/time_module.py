import time
import math
print('10 seg para summar 20+20')
# time.sleep(5)
print('La respuesta era 40')

print()
print('-------')
print()


print('Cuanto es la raiz cuadrada de 81')
first = time.time()
respuesta = int(input('Respuesta: '))

last = time.time()
seg = math.floor(last-first)


print(f"Te demoraste {seg} segundos")
print(time.ctime())
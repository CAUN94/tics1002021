import random

rand = random.randint(1,10)
print(rand)
cont = 0

while True:
    if cont == 3:
        print('Perdiste')
        break

    r = int(input('Nr: '))

    if r == rand:
        print('Ganaste')
        break
    else :
        cont += 1
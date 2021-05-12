import random

nr = random.randint(1,10)
print(nr)
cont = 0
while True:
    if cont == 3:
        print('Perdiste')
        break

    guess = int(input('Adivina el nr random: '))

    if guess == nr:
        print('Advinaste')
        break
    else:
        print('Ah ah ah, no dijiste la palabra magica')
    cont += 1
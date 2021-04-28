
nr = int(input('Dame un nr: '))
print('For')

for i in range(1,nr+1):
    if nr % i == 0:
        print(f"El nr {nr} es divisible por {i}")

print("--------")
print('While')

i = 1
while nr >= i :
    if nr % i == 0:
        print(f"El nr {nr} es divisible por {i}")
    i += 1


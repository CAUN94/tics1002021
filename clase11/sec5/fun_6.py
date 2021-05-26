def prime_number(num):
    for i in range(2,num):
        if num%i == 0:
            return 'no es primo'
    return 'es primo'

for i in range(1,1001):
    print(f"El numero {i} {prime_number(i)}")




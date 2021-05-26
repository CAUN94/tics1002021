def prime_n(x):
    for i in range(2,x):
        if x % i == 0:
            return 'No es primo'
    return 'Es Primo'

for i in range(2,80):
    print(f"{i}: {prime_n(i)}")
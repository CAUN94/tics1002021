def suma(num1,num2):
    # a = 2
    # b = 4
    # c = 5
    # sum = a + b + c
    return (num1 + num2)

def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact *= i
    return fact

sum = suma(1,2)

num = 10

print(f'El factorial de {num} es {factorial(num)}')
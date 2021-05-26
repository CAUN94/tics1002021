def message_function():
    print('Mi primera función')
    print('Mi primera función')
    print('Mi primera función')
    print('Mi primera función')
    print('Mi primera función')

def cuenta_del_1_al_10():
    for i in range(1,11):
        print(i)

def factorial_de_X(x):
    x = int(x)
    fact = 1
    for i in range(1,x + 1):
        fact *= i
    return float(fact)

def suma_4_numeros(a,b,c,d):
    print(a+b+c+d)


suma_4_numeros(1,2,3,4)

message_function()

print('Chao')

cuenta_del_1_al_10()
print('---')
fact_10 = factorial_de_X(10)
fact_2 = factorial_de_X(2)
fact_20 = factorial_de_X(20)
fact_5 = factorial_de_X(5)

print(f"El factorial es: {fact_5}")
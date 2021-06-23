def num_gemelo(a,b):
    # flag = False
    # if a > b and a-b == 2:
    #     flag = True
    # if a < b and b - a == 2:
    #     flag = True

    if primo(a) and primo(b) and abs(a-b) == 2:
        print('Los 2 numeros son primos gemelos')
        return
    
    print('No son gemelos')
    return

def primo(a):
    if a < 2:
        print(f'{a} no es primo')
        return False    

    for i in range(2,a):
        if a % i == 0:
            print(f'{a} no es primo')
            return False
    return True


numa = int(input("Ingrese el primer valor: ")) 
numb = int(input("Ingrese el segundo valor: ")) 

num_gemelo(numa,numb)
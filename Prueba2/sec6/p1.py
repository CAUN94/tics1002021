def num_gemelo(a,b):
    if primo(a) and primo(b) and abs(a-b) == 2:
        print('Los números son primos gemelos')
    else:
        print('Los NO números sonprimos gemelos')


def primo(a):
    if a < 2:
        print('No es Primo')
        return False
    for i in range(2,a):
        if a%i == 0:
            print('No es Primo')
            return False
    return True
    


numa = int(input('Ingresa el primer valor: '))
numb = int(input('Ingresa el primer valor: '))
num_gemelo(numa,numb)

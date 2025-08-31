while(True):

    n = int(input('Digite um número inteiro maior do que 1: ' \
    ''))
    x = 0
    if n>1:

        for c in range (1, n+1):
            if n % c == 0:
                x += 1
        
        if x == 2:
            print(f'O Número {n}, é primo!')
        else:
            print(f'O número {n} não é primo!')
        break
    else:
        print('Valor inválido')

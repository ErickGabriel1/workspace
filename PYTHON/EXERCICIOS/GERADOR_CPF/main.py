from random import randint

#Função que gera um dígito
def digit(m, peso, list):
    i = 0
    n1 = 0

    while i < m:
        n1+=list[i]*peso
        i += 1
        peso -=1
    n1 = 0 if n1 % 11 < 2 else 11 - (n1%11)
    return (n1)

def gerar_cpf():

    #Gerar os primeiros 9 dígitos
    cpf = []
    c = 1
    while c <= 9:
        cpf.append(randint(0, 9))
        c += 1
    
    # Gera Dígito 1
    h1 = digit(9, 10, cpf)
    cpf.append(h1)

    # Gera Dígito 2
    h2 = digit(10, 11, cpf)
    cpf.append(h2)

    #Retorna o valor do cpf gerado
    return f'CPF: {cpf[0]}{cpf[1]}{cpf[2]}.{cpf[3]}{cpf[4]}{cpf[5]}.{cpf[6]}{cpf[7]}{cpf[8]}-{cpf[9]}{cpf[10]}'

def verificar_cpf():
    
    while True:

        entry = input("Digite o CPF: ").strip()

        cpf = [int(d) for d in entry if d.isdigit()]

        if len(cpf) == 11:
            break
        else:
            print('Erro! Escreva um formato válido!')


    # Gera Dígito 1
    h1 = digit(9, 10, cpf)
    cpf.append(h1)

    # Gera Dígito 2
    h2 = digit(10, 11, cpf)
    cpf.append(h2)

    if cpf[9] == h1 and cpf[10] == h2:
        return f'O CPF: {cpf[0]}{cpf[1]}{cpf[2]}.{cpf[3]}{cpf[4]}{cpf[5]}.{cpf[6]}{cpf[7]}{cpf[8]}-{cpf[9]}{cpf[10]} é válido!'
    else:
        return f'O CPF: {cpf[0]}{cpf[1]}{cpf[2]}.{cpf[3]}{cpf[4]}{cpf[5]}.{cpf[6]}{cpf[7]}{cpf[8]}-{cpf[9]}{cpf[10]} é inválido'

#Pergunta ao usuário o que ele qual operação ele quer realizar    
while True:

    print('------------------------------------------------------')
    print('(1) Gerar um CPF')
    print('(2) Verificar um CPF')

    choice = int(input('Qual ação deseja realizar?').strip())

    if choice == 1:

        print(gerar_cpf())

    elif choice == 2:

        print(verificar_cpf())

    else:
        print('Erro! Tente novamente!')  
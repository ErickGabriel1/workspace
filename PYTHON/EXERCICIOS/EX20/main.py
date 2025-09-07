import os
import time
alfhabet = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]

def encrypt(message, shift_number):
    cipher_message = ''
    for word in message:
        if word not in alfhabet:
            cipher_message += word
        else:
            if alfhabet.index(word)+shift_number > 25:
                temp = (alfhabet.index(word)+shift_number) - 26
                cipher_message += alfhabet[temp]
            else:
                cipher_message += alfhabet[alfhabet.index(word)+shift_number]
    print(f'O seu código emcrypitado é: {cipher_message}')

def decrypt(message, shift_number):
    decipher_message = ''
    for word in message:
        if word not in alfhabet:
            decipher_message += word
        else:
            if alfhabet.index(word)-shift_number < 0:
                temp = (alfhabet.index(word)-shift_number) + 26
                decipher_message += alfhabet[temp]
            else:
                decipher_message += alfhabet[alfhabet.index(word)-shift_number]
    print(f'O seu código encrypitado é: {decipher_message}')
        
while(True):
    os.system('cls')
    while(True):
        os.system('cls')
        print('0 - Encrypitar\n1 - Decrypitar\n2 - Sair')
        op = int(input('Digite qual operação quer realizar: '))
        if op in (0, 1, 2):
            break

    if op == 2:
        break

    choice = str(input("Digite a mensagem:")).lower()
    snum = int(input('Digite o número chave:'))

    if op == 0:
        encrypt(choice, snum)
    elif op == 1:
        decrypt(choice, snum)
    
    ok = input('')
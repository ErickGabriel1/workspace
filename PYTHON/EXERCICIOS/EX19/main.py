from app import words
import random
import os
import time

choice = random.choice(words)
list_words = [d for d in choice if d.isalpha()]
print(list_words)
secret_list = []
life = 6
used = ""

for c in range(0, len(list_words)):
    secret_list.append("_")

while life != 0:
    
    os.system('cls')
    print(f'Sua vida é igual a: {life}')
    print(f'Letras utilizadas: {used}')
    print(f'Palavra: {secret_list}\n')
    char = str(input("Digite uma palava: ")[0].lower())

    hit = 0
    for c in range(0, len(list_words)):
        if char == list_words[c]:
            secret_list[c] = char
            hit += 1
    used += char
    if hit > 0:
        print(f'\nVocê acertou {hit} letra(s)')
        time.sleep(0.4)
        if list_words == secret_list:
            break
    else:
        print('\nVocê errou!')
        life -= 1
        time.sleep(0.4)

if life == 0:
    print("Você perdeu:")
else:
    print("Você ganhou!")



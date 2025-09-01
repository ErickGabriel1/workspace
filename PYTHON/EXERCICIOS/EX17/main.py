import random

game = ['Pedra', 'Papel', 'Tesoura']

console_choice = random.randint(0,2)

player_choice = int(input('Escolha:\n(0)Pedra\n(1)Papel\n(2)Tesousa\nQual a sua escolha:'))

print(f'\nVocê escolheu: {game[player_choice]}\n')
print(f'A máquina escolheu: {game[console_choice]}\n')

if console_choice == player_choice:
    print('Empate!')
elif (console_choice == 0 and player_choice == 2) or (console_choice == 1 and player_choice == 0) or (console_choice == 2 and player_choice == 1):
    print('Você perdeu!')
else:
    print('Você ganhou!')

print('\n')
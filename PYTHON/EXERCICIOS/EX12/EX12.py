from random import randint
from time import sleep

print('------------------------------------------------------')
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('------------------------------------------------------')

n1 = int(input('Em que número em pensei?'))
n2 = randint(0, 5)

print("PENSANDO...")
sleep(3)

if n1 == n2:
    print("Você acertou")
else:
    print('Você errou')
#Password Generator
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

n_letters = int(input('Digite quantas letras sua senha vai ter: '))
n_numbers = int(input('Digite quantos números sua senha vai ter: '))
n_symbols = int(input('Digite quants letras sua senha vai ter: '))

password = []

for n in range(0, n_letters):
    password.append(random.choice(letters))

for n in range(0, n_numbers):
    password.append(random.choice(numbers))

for n in range(0, n_symbols):
    password.append(random.choice(symbols))

print(password)
random.shuffle(password)
print(password)

password_key = ''

for c in password:
    password_key += c

print(f'Sua senha é: {password_key}')
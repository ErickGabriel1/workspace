s = float(input('Digite o seu salário:'))

if s <= 1250.00:
    a = (s*15)/100
else:
    a = (s*10)/100

print(f'O seu salário de {s:.2f} R$, passou a ser de {s+a:.2f} R$')
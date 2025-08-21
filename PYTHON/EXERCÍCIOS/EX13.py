n1 = float(input('Digite o valor a:'))
n2 = float(input('Digite o valor b:'))
n3 = float(input('Digite o valor c:'))

if n1 < n2+n3 and n2 < n3+n1 and n3 < n2+n1:
    print("É um triâmgulo")
else:
    print('Não é um triângulo')
casa = float(input("Digite o valor da casa: "))
salario =  float(input("Digite quanto você recebed de salário: "))

anos = int(input("Digite em quantos anos você quer pagar a casa: "))

prestacao = casa/(anos*12)

print(f"O valor da prestação é: R$ {prestacao:.2f}")

if (0.3*salario) <= prestacao:
    print("Empréstimo negado!")

else:
    print('Empréstimo aprovado!')
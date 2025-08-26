n1 = int(input("Digite um número inteiro:"))
c = 1
print("--------------------------------")

while c <= 10:
    print("{} x {:2} = {}".format(n1, c, n1*c))
    c = c+1
else:
    print("--------------------------------")

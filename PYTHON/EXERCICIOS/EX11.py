name = str(input("Digite seu nome:")).strip().title()

name = name.split()

print(f'Seu primeiro nome é {name[0]}')
print(f'Seu último nome é {name[len(name)-1]} ')

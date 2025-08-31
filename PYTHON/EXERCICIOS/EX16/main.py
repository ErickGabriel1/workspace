sum = 0
woman = 0
age_male = 0
name_male = ''

for c in range(1, 5):

    name = str(input('Name: '))
    age = int(input('Age: '))
    sum += age
    gender = str(input('Gender(M/F):')).strip().upper()

    if gender != 'M' and gender != 'F':
        print('Invalid!')
        break

    elif gender == 'M':
        if age > age_male:
            age_male = age
            name_male = name
    
    else:
        if age < 20:
            woman += 1

media = sum/4

print(f'A idade média das pessoas é igual a: {media}.')
print(f'The oldest man is {age_male} years old and is named {name_male}.')
print(f'The total number of women under 20 years old is: {woman}')



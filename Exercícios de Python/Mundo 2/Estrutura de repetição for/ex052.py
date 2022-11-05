num = int(input('Digite um número: '))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        cont += 1
        print('\033[33m', end=' ')
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mO numero {num} foi dividido {cont} vezes.')
if cont == 2:
    print('Então ele É PRIMO!')
else:
    print('Então ele NÃO É PRIMO!')

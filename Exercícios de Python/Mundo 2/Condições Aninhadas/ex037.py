print('\033[1:34m>=<\033[m' * 20)
print('Este programa converte um valor decimal para um binário ou \noctal ou hexadecimal')
print('\033[1:34m>=<\033[m' * 20)

num = int(input('Digite um número inteiro qualquer: '))

print('''Escolha uma das bases de conversão:
\033[1:31m[ 1 ] para BINÁRIO\033[m
\033[1:32m[ 2 ] para OCTAL\033[m
\033[1:33m[ 3 ] para HEXADECIMAL\033[m''')
opc = int(input('Sua opcão: '))

if opc == 1:
    binary = format(num, 'b')
    print(f'\033[1:31m{num} em binário equivale a {binary} na base 2\033[m')
elif opc == 2:
    octal = format(num, 'o')
    print(f'\033[1:32m{num} em octal equivale a {octal} na base 8\033[m')
elif opc == 3:
    hexa = format(num, 'x')
    print(f'\033[1:33m{num} em hexadecimal equivale a {hexa} na base 16\033[m')
else:
    print('Opcão inválida!')

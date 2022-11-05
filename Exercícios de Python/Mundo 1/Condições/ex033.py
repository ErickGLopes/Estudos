from time import sleep

print('\033[1:35m-=-\033[m' * 19)
print('\033[1:95mEste programa analisa três números e verifica qual é o \nmaior e qual é o menor entre eles\033[m')
print('\033[1:35m-=-\033[m' * 19)
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
print('VERIFICANDO...')
sleep(1.1)
if n1 > n2 and n1 > n3:
    print('\033[1:95m{} é o maior número\033[m'.format(n1))
if n2 > n1 and n2 > n3:
    print('\033[1:95m{} é o maior número\033[m'.format(n2))
if n3 > n1 and n3 > n2:
    print('\033[1:95m{} é o maior número\033[m'.format(n3))

if n1 < n2 and n1 < n3:
    print('\033[1:35m{} é o menor número\033[m'.format(n1))
if n2 < n1 and n2 < n3:
    print('\033[1:35m{} é o menor número\033[m'.format(n2))
if n3 < n1 and n3 < n2:
    print('\033[1:35m{} é o menor número\033[m'.format(n3))

if n1 == n2 and n1 < n3:
    print('\033[1:35m{} é o menor número\033[m'.format(n1))
if n3 == n1 and n3 < n2:
    print('\033[1:35m{} é o menor número\033[m'.format(n3))

if n1 == n2 and n1 > n3:
    print('\033[1:95m{} é o maior número\033[m'.format(n1))
if n3 == n1 and n3 > n2:
    print('\033[1:95m{} é o maior número\033[m'.format(n3))

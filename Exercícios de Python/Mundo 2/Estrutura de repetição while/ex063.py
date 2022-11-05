print('\033[1:33m-=-\033[m' * 10, end='')
print('\033[1:32mSEQUÊNCIA DE FIBONACCI\033[m', end='')
print('\033[1:33m-=-\033[m' * 10)
t1 = 0
t2 = 1
t3 = 0
n = int(input('Quantos termos exibir?: '))
print('~' * 30)
print(f'{t1} -> {t2} -> ', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f'{t3} -> ', end='')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')

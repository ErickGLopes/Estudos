from time import sleep
print('=-=' * 10, 'CALCULADORA DE FATORIAL', '=-=' * 10)
num = int(input('Digite o número a ser calculado: '))
print(f'Calculando {num}! = ', end='')
c = num
f = 1
sleep(0.6)
while c > 0:
    print(f'{c}', end='')
    print(f' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')

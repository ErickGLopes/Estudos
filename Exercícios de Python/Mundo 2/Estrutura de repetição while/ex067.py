print('-' * 30)
print('      TABUADA OTIMIZADA')
print('-' * 30)
num = 0
while True:
    num = int(input('Cunsultar tabuada do: '))
    print('\033[1:0m-\033[m' * 30)
    for c in range(1, 11):
        print(f'{num} x {c} = {num * c}')
    print('-' * 30)
    if num < 0:
        break
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
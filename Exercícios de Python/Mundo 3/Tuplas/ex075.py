n = (int(input('Digite o 1° valor: ')),
           int(input('Digite o 2° valor: ')),
           int(input('Digite o 3° valor: ')),
           int(input('Digite o 4° valor: ')))
print(f'a) O 9 apareceu {n.count(9)} vez(es)')
if 3 in n:
    print(f'b) O 3 apareceu na {n.index(3) + 1}ª posição pela primeira vez')
else:
    print('b) O número 3 não foi digitado')
if n[0] % 2 == 0 or n[1] % 2 == 0 or n[2] % 2 == 0 or n[3] % 2 == 0:
    print('c) Os números pares digitados foram: ', end='')
    for c in n:
        if c % 2 == 0:
            print(f'{c}', end=' ')
else:
    print('c) Não há números pares digitados')

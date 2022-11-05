from random import randint
ns = (randint(1, 9), randint(1, 9), randint(1, 9),
      randint(1, 9), randint(1, 9))
print(f'Os números sorteados foram: ', end='')
for n in ns:
    print(f'{n}', end=' ')
print(f'\nO maior valor sorteado foi {max(ns)}')
print(f'O menor valor sorteado foi {min(ns)}')

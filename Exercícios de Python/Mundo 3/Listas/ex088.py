from time import sleep
from random import randint
lista = list()
jogos = list()
print('-' * 30)
texto = 'SORTEAR JOGOS'
print(f'{texto:^30}')
print('-' * 30)
n = int(input('Quantas jogos sortear?: '))
tot = 0
while tot < n:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=-=-=-', f'Sorteando {n} jogo(s)...', '-=-=-=-')
for i, j in enumerate(jogos):
    print(f'Jogo {i + 1}: {j}')
    sleep(1)

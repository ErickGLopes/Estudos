from random import randint
from operator import itemgetter
from time import sleep
dado1, dado2, dado3, dado4 = randint(1, 6), randint(1, 6),\
                             randint(1, 6), randint(1, 6)
players = {
    'Jogador 1': dado1,
    'Jogador 2': dado2,
    'Jogador 3': dado3,
    'Jogador 4': dado4
}
print('Jogador 1 jogando', end='')
sleep(1)
for a in range(0, 3):
    print('.', end='')
    sleep(1)
print(f'\ntirou {players["Jogador 1"]}')
print('-' * 20)
print('Jogador 2 jogando', end='')
sleep(1)
for b in range(0, 3):
    print('.', end='')
    sleep(1)
print(f'\ntirou {players["Jogador 2"]}')
print('-' * 20)
print('Jogador 3 jogando', end='')
sleep(1)
for a in range(0, 3):
    print('.', end='')
    sleep(1)
print(f'\ntirou {players["Jogador 3"]}')
print('-' * 20)
print('Jogador 4 jogando', end='')
sleep(1)
for d in range(0, 3):
    print('.', end='')
    sleep(1)
print(f'\ntirou {players["Jogador 4"]}')
print(f'{"=" * 9}{"RANKING"}{"=" * 9}')
ranking = sorted(players.items(), key=itemgetter(1), reverse=True)
# se colocarmos parte 0 a ordenação será pelas chaves, se 1, por valores.
for c in range(0, 4):
    print(f'{c + 1}°{"." * 6}|{ranking[c][0]}|{"." * 6}')

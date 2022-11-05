from random import randint
from time import sleep
numeros = list()


def sorteia(lista):
    for c in range(0, 5):
        lista.append(randint(1, 10))
    print('Sorteando 5 valores: ', end='', flush=True)
    for valor in numeros:
        sleep(0.5)
        print(f'{valor}, ', end='')
    print('PRONTO!')


sorteia(numeros)


def somaPar(listint):
    soma = 0
    for n in listint:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {listint}, temos {soma}')


somaPar(numeros)

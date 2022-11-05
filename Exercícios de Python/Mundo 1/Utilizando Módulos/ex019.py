from random import choice
from time import sleep
n1 = str(input('Digite o nome do primeiro aluno:'))
n2 = str(input('Digite o nome do segundo aluno:'))
n3 = str(input('Digite o nome do terceiro aluno:'))
n4 = str(input('Digite o nome do quarto aluno:'))

print('Sorteando...')
sleep(1.25)

lista = [n1, n2, n3, n4]
escolhido = choice(lista)

print('O aluno escolhido entre {}, {}, {} e {} foi o(a) {}'.format(n1, n2, n3, n4, escolhido))
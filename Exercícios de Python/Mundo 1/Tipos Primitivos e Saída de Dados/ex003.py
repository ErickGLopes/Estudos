cores = {'verde': '\033[32m', 'amarelo': '\033[33m', 'limpa': '\033[m'}
print('{}-=-{}'.format(cores['verde'], cores['limpa']) * 20)
print('{}Este programa solicita dois número ao usuário e calcula a \nsoma entre eles{}'.format(cores['amarelo'],
                                                                                               cores['limpa']))
print('{}-=-{}'.format(cores['verde'], cores['amarelo']) * 20)
n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro:'))
s = n1+n2
print('{}A soma entre {} e {} é {}{}'.format(cores['limpa'], n1, n2, s, cores['limpa']))

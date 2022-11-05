cores = {'verde': '\033[1:32m', 'amarelo': '\033[1:33m', 'azul': '\033[1:34m', 'limpa': '\033[m'}
print('\033[32m***\033[m' * 20)
print('\033[33m===\033[m' * 8, '\033[1:33mTABUADA\033[m', '\033[33m===\033[m' * 9)
print('\033[32m***\033[m' * 20)

num = int(input('Consultar a tabuada do: '))
print(f'A tabuada do {num} é:')
res = 0
cont = 1
for c in range(1, 11):
    res += 1
    print('{}{}{} x {}{}{} = {}'.format(cores['verde'], num, cores['limpa'],
                                        cores['amarelo'], cont, cores['limpa'], res * num))
    cont += 1

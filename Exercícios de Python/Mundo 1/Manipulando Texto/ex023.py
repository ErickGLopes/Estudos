from time import sleep

n = int(input('Digite um número entre 0 e 9999:'))

print('Analisando o número {}...'.format(n))
sleep(1.35)

if n < 1 or n > 9999:
    print('Número inválido!')
    exit()

print('O número {} tem:'.format(n))
strnum = str(n)
strnum = ' '.join(strnum)
strnum = strnum.split()

if len(str(n)) == 1:
    print('Unidade(s): {}\nDezena(s): {}\nCentena(s): {}\nMilhar(es): {}'.format(strnum[0], 0, 0, 0))

if len(str(n)) == 2:
    print('Unidade(s): {}\nDezena(s): {}\nCentena(s): {}\nMilhar(es): {}'.format(strnum[1], strnum[0], 0, 0))

if len(str(n)) == 3:
    print('Unidade(s): {}\nDezena(s): {}\nCentena(s): {}\nMilhar(es): {}'.format(strnum[2], strnum[1], strnum[0], 0))

if len(str(n)) == 4:
    print('Unidade(s): {}\nDezena(s): {}\nCentena(s): {}\nMilhar(es): {}'.format(strnum[3], strnum[2],
                                                                                 strnum[1], strnum[0]))

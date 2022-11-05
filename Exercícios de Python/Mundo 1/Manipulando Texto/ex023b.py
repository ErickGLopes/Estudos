num = int(input('Digite um número entre 0 e 9999:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analisando o número {}'.format(num))
print('Unidade(s): {}'.format(u))
print('Dezena(s): {}'.format(d))
print('Centena(s): {}'.format(c))
print('Milhar(s): {}'.format(m))

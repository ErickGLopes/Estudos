print('-=-' * 10)
print('Analizador de triângulos')
print('-=-' * 10)
r1 = float(input('Digite o seguimento 1: '))
r2 = float(input('Digite o seguimento 2: '))
r3 = float(input('Digite o seguimento 3: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r3 + r2 > r1:
    print('Esses seguimentos formam um triângulo', end='')
    if r1 == r2 == r3:
        print(' EQUILÁTERO!')
    elif r1 == r2 and r1 != r3 or r1 == r3 and r1 != r2 or r2 == r3 and r3 != r1:
        print(' ISÓSCELES!')
    else:
        print(' ESCALENO!')
else:
    print('Esses seguimentos  NÃO formam uma triângulo')

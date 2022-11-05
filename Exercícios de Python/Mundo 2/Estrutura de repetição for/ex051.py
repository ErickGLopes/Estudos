print('=' * 21)
print('10 TERMOS DE UMA P.A')
print('=' * 21)

a1 = int(input('Digite o 1° termo da PA: '))
r = int(input('Digite a razão da PA: '))
a10 = a1 + (10 - 1) * r
# Fórmula PA => an = a1 + (n - 1) . r

for c in range(a1, a10 + r, r):
    print(f'{c} >', end=' ')
print('ACABOU')



print('=' * 20)
print('     BANCO LOPES')
print('=' * 20)
num = int(input('Que valor você quer sacar?: '))
total = num
ced = 50
contced = 0
while True:
    if total >= ced:
        total -= ced
        contced += 1
    else:
        if contced > 0:
            print(f'Total de {contced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        contced = 0
        if total == 0:
            break
print('=' * 20)

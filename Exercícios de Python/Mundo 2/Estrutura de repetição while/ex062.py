a1 = int(input('Primeiro termo: '))
r = int(input('Razão da P.A: '))
termo = a1
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos mostrar a mais?: '))
print(f'Programa finalizado com {total} termos mostrados.')

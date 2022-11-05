from time import sleep


def line():
    print('=-' * 20)


def carregamento():
    for c in range(0, 3):
        sleep(0.5)
        print('.', end='')


def larger(*num):
    line()
    print('Analizando os valores passados', end='', flush=True)
    carregamento()
    print()
    if len(num) != 0:
        cont = maior = 0
        for valor in num:
            print(f'{valor} ', end='')
            if cont == 0:
                maior = valor
            else:
                if valor > maior:
                    maior = valor
            cont += 1
        print(f'- Foram informados {len(num)} valores ao todo.')
        print(f'O maior valor foi {maior}.')
    else:
        print('Nenhum valor foi informado!')


larger(14, 0, 4)
larger(1, 6, 9, 11, 33, 0)
larger()
from time import sleep


def linha():
    print('-=' * 20)


def contador(i, f, p):
    if  p < 0:
        p *= -1        
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    sleep(2.5)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end="", flush=True)
            cont += p
            sleep(0.5)
        print('FIM!')
        linha()
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end="", flush=True)
            cont -= p
            sleep(0.5)
        print('FIM!')
        linha()


contador(1, 10, 1)
contador(10, 0, 2)
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)

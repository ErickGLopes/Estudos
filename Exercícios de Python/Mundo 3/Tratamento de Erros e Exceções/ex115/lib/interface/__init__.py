from time import sleep


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def leiaInt(txt):
    while True:
        try:
            numInt = int(input(txt))
        except ValueError:
            print(f'\033[31mERRO: por favor, digite um número INTEIRO válido!\033[m')
            sleep(2)
        except KeyboardInterrupt:
            print(f'\033[31mUsuário preferiu não digitar esse número.\033[m')
            sleep(2)
            return 0
        else:
            return numInt


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    opc = leiaInt('Sua opção: ')
    return opc


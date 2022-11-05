def leiaDinheiro(txt):
    valido = False
    while not valido:
        entrada = str(input(txt)).replace(',','.').strip()
        if entrada.isalpha():
            print(f'\033[31mERRO. "{entrada}" não é um preço válido!\033[m')
        if entrada.isspace():
            print(f'\033[31mERRO. "{entrada}" não é um preço válido!\033[m')
        else:
            valido = True
            return float(entrada)


def leiaInt(txt):
    valido = False
    while not valido:
        num = str(input(txt)).strip()
        if num.isnumeric() and num != '':
            valido = True
            return int(num)
        else:
            print('\033[31mErro! Digite um número inteiro válido.\033[m')

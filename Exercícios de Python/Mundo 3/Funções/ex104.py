from unicodedata import numeric


def leiaInt(txt):
    while True:
        num = str(input(txt)).strip()
        if num.isnumeric() and num != '':
            break
        else:
            print('\033[31mErro! Digite um número inteiro válido.\033[m')
            
    return num


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
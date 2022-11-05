def leiaInt(txt):
    while True:
        try:
            numInt = int(input(txt))
        except ValueError:
            print(f'\033[31mERRO: por favor, digite um número INTEIRO válido!\033[m')
        except KeyboardInterrupt:
            print(f'\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return numInt
            

def leiaFloat(msg):
    while True:
        try:
            numFloat = float(input(msg))
        except ValueError:
            print(f'\033[31mERRO: por favor, digite um número REAL válido!\033[m')
        except KeyboardInterrupt:
            print(f'\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return numFloat

nInt = leiaInt('Digite um número Inteiro: ')
nFloat = leiaFloat('Digite um número Real: ')
print(f'\nNúmeros digitados:\n\tInteiro: {nInt}\n\tReal: {nFloat}\n')

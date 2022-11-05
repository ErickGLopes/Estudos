from time import sleep
num1 = int(input('Digite o 1° valor: '))
num2 = int(input('Digite o 2° valor: '))
opc = 0
maior = 0
menor = 0
while opc != 5:
    if opc != 5:
        sleep(0.5)
        print('=-=-=-=-=-=-==-=-==-=-=')
        print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior valor
[ 4 ] Novos números
[ 5 ] Sair do programa
=-=-=-=-=-=-=-=-=-=-=-=''')
        opc = int(input('Selecione uma das opções acima: '))
        print('=-=-=-=-=-=-=-=-=-=-=-=')
        if opc == 1:
            soma = num1 + num2
            print(f'A soma entre {num1} e {num2} é igual a {soma}')
        elif opc == 2:
            mult = num1 * num2
            print(f'O produto entre {num1:} e {num2} é igual a {mult}')
        elif opc == 3:
            if num1 > num2:
                maior = num1
                print(f'O maior valor é o {num1}')
            else:
                maior = num2
                print(f'O maior valor é o {num2}')
        elif opc == 4:
            num1 = int(input('Digite o 1° valor: '))
            num2 = int(input('Digite o 2° valor: '))
        elif opc == 5:
            print('Finalizando...')
            print('Fim do programa. Volte sempre!')
        else:
            print('\033[31mOpção inválida. Tente novamente\033[m')
            print('=-=-=-=-=-=-=-=-=-=-=-=')

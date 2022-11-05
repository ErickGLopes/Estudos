listageral = list()
opc = 'S'
while opc == 'S':
    n = int(input('Digite um valor: '))
    listageral.append(n)
    opc = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if opc == 'N':
        break
    elif opc not in 'SN':
        print('\033[31mErro: Opção inválida!\033[m\nQuer continuar? [S/N]:')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
listapares = list()
listaimpares = list()
cont = 0
while cont < len(listageral):
    if listageral[cont] % 2 == 0:
        listapares.append(listageral[cont])
    elif listageral[cont] % 2 != 0:
        listaimpares.append(listageral[cont])
    cont += 1
print(f'A lista completa é {listageral}')
print(f'A lista de pares é {listapares}' if len(listapares) != 0 else 'Não há valores pares.')
print(f'A lista de ímpares é {listaimpares}' if len(listaimpares) != 0 else 'Não há valores ímpares.')

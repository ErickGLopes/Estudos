opc = 'S'
lista = list()
while opc == 'S':
    n = int(input('Digite um valor inteiro: '))
    if n in lista:
        print('\033[33mValor duplicado! Não vou adicioná-lo...\033[m')
    else:
        lista.append(n)
        print('\033[32mValor adicionado com sucesso...\033[m')
    opc = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if opc == 'N':
        print('====================================================')
        break
    elif opc not in 'SN':
        n = str(input('\033[31mErro: Opção inválida.\033[m\nQuer continuar? [S/N]: '))
lista.sort()
print(f'Você adicionou os números {lista}')

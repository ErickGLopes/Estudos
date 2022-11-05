valores = list()
opc = 'S'
while opc == 'S':
    n = int(input('Digite um valor: '))
    valores.append(n)
    valores.sort(reverse=True)
    opc = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if opc == 'N':
        break
    elif opc not in 'SN':
        opc = str(input('\033[31mErro: Opção inválida!\033[m\nQuer continuar? [S/N]: '))
print(f'Você digitou {len(valores)} elementos.')
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print(f'O valor 5 foi encontrado na posição {valores.index(5)} da lista!')
else:
    print('O valor 5 NÃO faz parte da lista.')

maior = menor = 0
predados = []
dados = []

opc = 'S'
while opc == 'S':
    predados.append(str(input('NOME: ')))
    predados.append(float(input('PESO: ')))
    dados.append(predados[:])
    predados.clear()

    opc = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if opc == 'N':
        break
    elif opc not in 'SN':
        opc = str(input('\033[31mOpcão inválida!\033[m\nQuer continuar? [S/N]: ')).strip().upper()

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

cont = pesmai = pesmen = 0
while cont < len(dados):
    if cont == 0:
        maior = menor = dados[cont][1]
        maiorpeso = menorpeso = dados[cont][0]
    else:
        if dados[cont][1] > maior:
            maior = dados[cont][1]
            pesmai = dados[cont][0]
        elif dados[cont][1] < menor:
            menor = dados[cont][1]
            pesmen = dados[cont][0]

    cont += 1
print(f'Ao todo você cadastrou {len(dados)} pessoas')
print(f'O maior peso foi de {maior:.2f} --> Peso de {pesmai}')
print(f'O menor peso foi de {menor:.2f} --> Peso de {pesmen}')

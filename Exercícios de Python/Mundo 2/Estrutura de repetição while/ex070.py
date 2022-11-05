totgasto = totprod1000 = cont = menor = 0
prodMbarato = ''
while True:
    cont += 1
    print('-' * 22)
    print('   MERCADÃO JUNDIAÍ')
    print('-' * 22)
    prod = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    totgasto += preco
    if preco > 1000:
        totprod1000 += 1
    if cont == 1:
        prodMbarato = prod
        menor = preco
    else:
        if preco < menor:
            prodMbarato = prod
            menor = preco
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?: ')).strip().upper()[0]
    if resp == 'N':
        break
print('-' * 20, end=' ')
print('FIM DO PROGRAMA', end=' ')
print('-' * 20)
print(f'O total da compra foi R${totgasto:.2f}')
print(f'Temos {totprod1000} custando mais de R$1000.00')
print(f'O produto mais barato mais barato foi o(a) {prodMbarato} que custa R${menor:.2f}')

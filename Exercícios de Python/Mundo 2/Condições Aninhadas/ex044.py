print('=' * 20, 'LOJA DA FAMÍLIA LOPES', '=' * 20)

valor = float(input('Digite o preço original do produto: R$'))
print('''Selecione uma das formas de pagamento abaixo:
[ 1 ] À vista (dinheiro/cheque): 10% de desconto
[ 2 ] À vista (cartão): 5% de desconto
[ 3 ] Em até 2x no cartão: preço original
[ 4 ] 3x ou mais no cartão: 20% de juros''')
opc = int(input('Sua opção: '))

if opc == 1:
    vt = valor - (valor * 10 / 100)
elif opc == 2:
    vt = valor - (valor * 5 / 100)
elif opc == 3:
    vt = valor
    parcela = valor / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS')
elif opc == 4:
    vt = valor + (valor * 20 / 100)
    qtde_vezes = int(input('Em quantas vezes você pretende pagar? '))
    parcela = vt / qtde_vezes
    print(f'Sua compra será parcelada em {qtde_vezes}x de R${parcela:.2f} COM JUROS')
else:
    vt = valor
    print('\033[1:31mOpção inválida! Tente novamente\033[m')
print(f'Seu subtotal é de R${valor:.2f} e você pagará R${vt:.2f} no final')

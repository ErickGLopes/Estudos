# valores de 13/12/2021
val = float(input('Quantos reais você tem na carteira?: R$'))
print('Com R${:.2f} você poderá comprar U${:.2f} ou ₤{:.2f}'.format(val, val / 5.67, val / 6.40))

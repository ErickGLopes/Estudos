preco = float(input('Preço do produto: R$'))
desc = preco * 0.05
df = preco - desc
print('O preço com desconto de 5% é R${:.2f}\n(R${:.2f} de desconto)'.format(df, desc))

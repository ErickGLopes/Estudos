produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
            'Estojo', 25.00, 'Tranferidor', 4.20, 'Compasso',
            9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS".center(30)}')
print('-' * 40)
for c in range(0, len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c]:.<30}', end='')
    elif c % 2 == 1:
        print(f'R${produtos[c]:>7}')
print('-' * 40)

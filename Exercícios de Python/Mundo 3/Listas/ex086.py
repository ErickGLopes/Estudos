matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
cont = cont_col3 = sam = 0
for lin in range(0, 3):
    for col in range(0, 3):
        matriz[lin][col] = int(input(f'Digite um valor para [{lin}, {col}]: '))
        if matriz[lin][2]:
            cont_col3 += matriz[lin][col]
        if matriz[lin][col] % 2 == 0:
            cont += 1
        sam += matriz[lin][col]
print('=' * 35)
for lin in range(0, 3):
    for col in range(0, 3):
        print(f'[{matriz[lin][col]:^5}]', end='')
    print()
print(f'A matriz possui {cont} números pares;')
print(f'A soma de todos os números da matriz é {sam}; e')
print(f'A soma dos números da terceira coluna é {cont_col3}.')

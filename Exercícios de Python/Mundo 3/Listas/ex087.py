matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sam_pares = sam_col3 = maior = 0
for lin in range(0, 3):
    for col in range(0, 3):
        matriz[lin][col] = int(input(f'Digite um valor para [{lin}, {col}]: '))
        if matriz[lin][col] % 2 == 0:
            sam_pares += matriz[lin][col]
        if matriz[lin][2]:
            sam_col3 += matriz[lin][col]
        maior = max(matriz[1])
print('=' * 35)
for lin in range(0, 3):
    for col in range(0, 3):
        print(f'[{matriz[lin][col]:^5}]', end='')
    print()
print(f'Soma dos números pares: {sam_pares}')
print(f'Soma da 3° coluna: {sam_col3}')
print(f'Maior valor da 2° linha: {maior}')

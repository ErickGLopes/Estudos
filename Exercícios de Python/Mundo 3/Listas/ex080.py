lista = list()
for c in range(1, 6):
    n = int(input('Digite um valor inteiro: '))
    if c == 1 or n > lista[-1]:
        lista.append(n)
        print('Valor adicionado no final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Valor inserido na posição {pos} da lista.')
                break
            pos += 1
print('=================================================')
print(f'Você adicionou os números {lista}')

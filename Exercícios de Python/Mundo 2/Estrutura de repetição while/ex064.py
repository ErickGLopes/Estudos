soma = cont = 0
num = int(input('Digite um número (999 para parar): '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número (999 para parar): '))
parada = 0
print('Programa finalizado.')
print(f'Foram digitados \033[33m{cont}\033[m números e a soma entre eles equivale a \033[33m{soma}\033[m')

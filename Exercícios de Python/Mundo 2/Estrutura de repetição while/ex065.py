num = cont = soma = maior = menor = 0
opc = 'S'
while opc == 'S':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    opc = str(input('Deseja continuar?[S/N]: ')).strip().upper()[0]
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
m = soma / cont
print(f'Você digitou {cont} números, a média foi de {m:.2f}')
print(f'O maior número é o {maior} e o menor o {menor}')

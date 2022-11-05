valores = [[], []]
for c in range(1, 8):
    num = int(input(f'Digite o {c}° valor: '))
    if num % 2 == 0:
        valores[0].append(num)
        valores[0].sort()
    elif num % 2 != 0:
        valores[1].append(num)
        valores[1].sort()
print(f'Os valores pares digitados foram {valores[0]}')
print(f'Os valores ímpares digitados foram {valores[1]}')

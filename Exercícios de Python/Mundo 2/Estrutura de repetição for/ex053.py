frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'Sua frase é {junto} que ao contrário é {inverso}.')
if junto == inverso:
    print('Eis um PALÍNDROMO!')
else:
    print('NÃO temos um palíndromo!')

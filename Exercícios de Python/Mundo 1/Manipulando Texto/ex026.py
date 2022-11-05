frase = str(input('Digite uma frase:')).strip()

print('Quantos "a" exite na frase?: {}'.format(frase.upper().count('A')))
print('Posição em que a letra "a" aparece pela primeira vez: {}'.format(frase.upper().find('A') + 1))
print('Posição em que a letra "a" aparece pela última vez: {}'.format(frase.upper().rfind('A') + 1))

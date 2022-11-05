palavras = ('vida', 'presente', 'forca', 'sabedoria',
            'complexo', 'escravo', 'servir', 'adoracao',
            'paz', 'eternidade', 'batalha')
for p in palavras:
    print(f'\nNa palavra {p} temos -> ', end='')
    for letra in p:
        if letra.upper() in 'AEIOU':
            print(f'{letra}', end=' ')

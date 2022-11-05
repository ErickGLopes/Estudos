maisricos = ('Estados Unidos', 'Rússia', 'China', 'Alemanha',
             'Reino Unido', 'França', 'Japão', 'Israel',
             'Coreia do Sul', 'Arábia Saudita', 'Emirados Árabes Unidos',
             'Canadá', 'Suiça', 'Índia', 'Austrália', 'Turquia', 'Itália',
             'Catar', 'Espanha', 'Suécia')
print('Os cinco países mais ricos:')
print(f'1° {maisricos[0]}\n2° {maisricos[1]}\n3° {maisricos[2]}\n4° {maisricos[3]}\n5° {maisricos[4]}')
print('=' * 30)
print('Os quatro últimos mais ricos:')
print(f'17° {maisricos[-4]}\n18° {maisricos[-3]}\n19° {maisricos[-2]}\n20° {maisricos[-1]}')
print('=' * 30)
print('Em ordem alfabética:')
ordalf = sorted(maisricos)
for c in range(0, 20):
    print(f'- {ordalf[c]}')
print('=' * 30)
pos = maisricos.index('Israel') + 1
print(f'Israel está na {pos}ª posição')

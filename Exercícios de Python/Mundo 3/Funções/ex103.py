def ficha(nome='<desconhecido>',gols=0):
    print(f'O(a) jogador(a) {nome} fez {gols} gol(s) no campeonato.')

n = str(input('Nome: ')).strip()
g = str(input('Qtde de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n == '':
    ficha(gols=g)
else:
    ficha(n, g)
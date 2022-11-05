dados = {'nome': str(input('Nome do Jogador: '))}
qtde_partidas = int(input(f'Quantas partidas {dados["nome"]} jogou?: '))
listadegols = []
for c in range(0, qtde_partidas):
    listadegols.append(int(input(f'{" " * 5}Quantos gols na {c + 1}° partida?: ')))
dados['gols'] = listadegols.copy()
dados['total'] = sum(listadegols)
print('=-' * 30)
print(dados)
print('=-' * 30)
print(f'Campo nome = {dados["nome"]}')
print(f'Campo gols = {dados["gols"]}')
print(f'Campo total = {dados["total"]}')
print('=-' * 30)
print(f'O jogador {dados["nome"]} jogou {qtde_partidas} partidas.')
cont = 0
while cont < qtde_partidas:
    print(f'{" " * 5}=> Na partida {cont + 1}, fez {listadegols[cont]} gols')
    cont += 1
print(f'Foi um total de {dados["total"]} gols.')

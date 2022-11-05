jogadores = []
dados = []
listadegols = []
while True:
    dados.clear()
    dados = {'nome': str(input('Nome do Jogador: '))}
    qtde_partidas = int(input(f'Quantas partidas {dados["nome"]} jogou?: '))
    listadegols.clear()
    for c in range(0, qtde_partidas):
        listadegols.append(int(input(f'{" " * 5}Quantos gols na {c + 1}° partida?: ')))
    dados['gols'] = listadegols[:]
    dados['total'] = sum(listadegols)
    jogadores.append(dados.copy())
    resp = str(input('Quer continuar?[S/N]: ')).strip().upper()
    while resp not in 'SN':
        print('\033[31mOpção inválida! Tente novamente.\033[m')
        resp = str(input('Quer continuar?[S/N]: ')).strip().upper()
    print('=' * 40)
    if resp == 'N':
        break
print('cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('--------------------------------------------')
for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('--------------------------------------------')
while True:
    busca = int(input('Mostrar os dados de qual jogador?(999 para parar): '))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f'ERRO! Não existe jogador com o código {busca}.')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[busca]["nome"]}:')
        for i, g in enumerate(jogadores[busca]['gols']):
            print(f'   No jogo {i + 1} fez {g} gols')
    print('--------------------------------------------')
print('<< VOLTE SEMPRE! >>')

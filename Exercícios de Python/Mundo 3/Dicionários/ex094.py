pessoas = list()
while True:
    dados = {'nome': str(input('Nome: ')),
             'sexo': str(input('Sexo [M/F]: ')).strip().upper(),
             'idade': int(input('Idade: '))}
    while dados['sexo'] not in 'MF' or dados['sexo'] == '':
        del(dados['sexo'])
        print('\033[31mOpção inválida! Tente novamente.\033[m')
        dados['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
    pessoas.append(dados.copy())
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    while resp not in 'SN':
        print('\033[31mOpção inválida! Tente novamente.\033[m')
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    print('=-' * 20)
    if resp == 'N':
        break
print(pessoas)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
soma = 0
totF = []
for c in range(0, len(pessoas)):
    soma += pessoas[c]['idade']
    if pessoas[c]['sexo'] == 'F':
        totF.append(pessoas[c]['nome'])
media = soma / len(pessoas)
print(f'A média de idade do grupo é {media:.2f} anos.')
print(f'Mulheres do grupo: {totF}')
print('=' * 6, 'IDADE ACIMA DA MÉDIA', '=' * 6)
print(f'{"NOME":<10}{"IDADE":^20}{"SEXO":<10}')
for c in range(0, len(pessoas)):
    if pessoas[c]['idade'] > media:
        print(f'{pessoas[c]["nome"]:.<10}{pessoas[c]["idade"]:.^20}{pessoas[c]["sexo"]:<10}')
print('<<ENCERRADO>>')

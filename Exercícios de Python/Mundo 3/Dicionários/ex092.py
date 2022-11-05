from datetime import datetime
dados = {'nome': str(input('Digite seu nome: ')).strip(),
         'nasc': int(input('Digite o ano do seu nascimento: ')),
         'ctps': int(input('Carteira de Trabalho [0 se não tiver]: '))}
cor = {'amarelo': '\033[33m', 'limpa': '\033[m'}
if dados['ctps'] != 0:
    dados['ano_contr'] = int(input('Ano de contratação: '))
    dados['sal'] = float(input('Salário: R$'))
    dados['aposentadoria'] = (dados['ano_contr'] + 35) - dados['nasc']
print('=' * 15, 'SEUS DADOS', '=' * 15)
ano_atual = datetime.today().year
dados['idade'] = ano_atual - dados['nasc']
print(f'NOME: {cor["amarelo"]}{dados["nome"]}{cor["limpa"]}  | '
      f'ANO DE NASCIMENTO: {cor["amarelo"]}{dados["nasc"]}{cor["limpa"]}')
print(f'IDADE: {cor["amarelo"]}{dados["idade"]}{cor["limpa"]}')
if dados['ctps'] != 0:
    print(f'CARTEIRA DE TRABALHO: {cor["amarelo"]}{dados["ctps"]}{cor["limpa"]}')
    print(f'SALÁRIO: {cor["amarelo"]}R${dados["sal"]}{cor["limpa"]}')
    print(f'ANO DE CONTRATAÇÃO: {cor["amarelo"]}{dados["ano_contr"]}{cor["limpa"]}')
    print(f'\033[33mVocê se aposentará com {dados["aposentadoria"]} anos.\033[m')
if dados["ctps"] == 0:
    print(f'{cor["amarelo"]}Você não tem Carteira de Trabalho.{cor["limpa"]}')

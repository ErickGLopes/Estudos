print('-=-' * 20)
print('Esse programa analisa se você pode pedir um determinado empréstimo')
print('-=-' * 20)
valor_casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Quantos você recebe por mês? R$'))
qtde_anos = int(input('Em quantos anos você pretende pagá-la? '))
prest_mensal = valor_casa / (qtde_anos * 12)
print(f'Para pagar uma casa de R${valor_casa:,.2f} em {qtde_anos} anos, você pagará prestações de R${prest_mensal:.2f}')
if prest_mensal > salario * (30 / 100):
    print('Empréstimo NEGADO!')
else:
    print('Esse emprestimo É VIÁVEL!')

from datetime import date

ano = int(input('Digite seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano
print(f'Você tem {idade} ano(s) em {ano_atual}')

if idade <= 9:
    print('Sua categoria é a MIRIM')
elif idade <= 14:
    print('Sua categoria é a INFANTIL')
elif idade <= 19:
    print('Sua categoria é a JÚNIOR')
elif idade <= 20:
    print('Sua categoria é a SÊNIOR')
else:
    print('Sua categoria é a MASTER')

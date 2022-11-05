from datetime import date
num = 1
ano_atual = date.today().year
maiores = 0
menores = 0
for c in range(1, 8):
    ano = int(input(f'Digite o ano de nascimento da {num}° pessoa: '))
    num += 1
    if ano_atual - ano >= 18:
        maiores += 1
    else:
        menores += 1
print(f'\nTemos {maiores} pessoas maiores de idade; e')
print(f'Outras {menores} pessoas menores de idade.')

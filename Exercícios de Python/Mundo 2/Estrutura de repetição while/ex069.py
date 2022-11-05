mais18 = mens = f20 = 0
while True:
    print('--' * 12)
    print('  CADASTRE UMA PESSOA')
    print('--' * 12)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo[M/F]: ')).strip().upper()[0]
    if idade >= 18:
        mais18 += 1
    if sexo == 'M':
        mens += 1
    if sexo == 'F' and idade < 20:
        f20 += 1
    opc = ' '
    while opc not in 'SN':
        opc = str(input('Cadastrar mais pessoas?[S/N]: ')).strip().upper()[0]
    if opc == 'N':
        break
print('-=-' * 15)
print(f'- Há {mais18} pessoas maiores de dezoito anos')
print(f'- Foram cadastrados {mens} homens')
print(f'- Há {f20} mulheres menores de vinte anos')

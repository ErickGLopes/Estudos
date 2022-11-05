nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
m = (nota1 + nota2) / 2

if m < 5.0:
    print('REPROVADO!')
elif 5.0 <= m <= 6.9:
    print('RECUPERAÇÃO!')
else:
    print('APROVADO!')

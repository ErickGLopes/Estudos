print('\033[1:33m-=-\033[m' * 20)
print('\033[1:32mEsse programa calcula o valor do aumento em um determinado \nsalário.\033[m')
print('\033[1:33m-=-\033[m' * 20)
salario = float(input('Digite o seu salário: '))
percentual = 0
if salario > 1250.0:
    percentual = 10.0 / 100.0
if salario <= 1250.0:
    percentual = 15.0 / 100.0
comaumento = salario + (salario * percentual)
valoraumento = comaumento - salario
print('Tendo um sálario de R${:.2f} você receberá um aumento de \033[1:32mR${:.2f}\033[m'.format(salario, valoraumento))
print('Seu salário com aumento é de \033[1:32mR${:.2f}\033[m'.format(comaumento))

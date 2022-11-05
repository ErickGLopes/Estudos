salario = float(input('Salário do funcionário: R$'))
aumento = salario * 0.15
af = salario + aumento
print('Salário após aumento: R${:.2f}\n(R${:.2f} de aumento)'.format(af, aumento))
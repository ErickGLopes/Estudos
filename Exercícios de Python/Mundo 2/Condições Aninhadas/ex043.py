peso = float(input('Digite o seu peso em Kg: '))
alt = float(input('Digite a sua altura em Metros: '))
imc = peso / pow(alt, 2)
print(f'Seu IMC é de {imc:.2f}Kg/m². \nSITUAÇÃO: ', end='')
if imc < 18.5:
    print('abaixo do peso')
elif 18.5 <= imc <= 25:
    print('seso ideal')
elif 25 <= imc <= 30:
    print('sobrepeso')
elif 30 <= imc <= 40:
    print('obesidade')
else:
    print('obesidade mórbida')

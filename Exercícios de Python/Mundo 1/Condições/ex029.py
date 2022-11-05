v = float(input('Digite a velocidade do carro: '))
if v > 80.0:
    print('\033[1:31:40mMULTADO!. Você ultrapassou o limite de velocidade que é de 80Km/h\033[m')
    multa = (v - 80) * 7
    print('\033[1:33:40mTerá que pagar uma multa de R${:.2f}\033[m'.format(multa))
print('\033[1:32:40mBom dia! Dirija com segurança!\033[m')

d = float(input('Digite a distância da sua viagem: '))
print('Você está prestes a iniciar uma viagem de {}Km'.format(d))
if d <= 200.0:
    print('O preço da sua passagem é de R${:.2f}'.format(d * 0.5))
if d > 200.0:
    print('O preço da sua passagem é de R${:.2f}'.format(d * 0.45))
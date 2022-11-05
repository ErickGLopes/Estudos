from random import choice
from time import sleep

print('=' * 11, 'Jokenpô', '=' * 11)
jokenpo = ['Pedra', 'Papel', 'Tesoura']
cpu = choice(jokenpo)
print('''Faça a sua escolha entre:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
opc = int(input('Sua escolha: '))

player = 0
if opc == 1:
    player = 'Pedra'
elif opc == 2:
    player = 'Papel'
elif opc == 3:
    player = 'Tesoura'
else:
    print('\033[1:31mOpção inválida!. Tente novamente\033[m')
    exit()

print('JO')
sleep(0.8)
print('KEN')
sleep(0.8)
print('PÔ')
sleep(0.8)

if player == 'Pedra' and cpu == 'Papel':
    print('\033[1:31mO COMPUTADOR VENCEU!\033[m')
elif player == 'Pedra' and cpu == 'Tesoura':
    print('\033[1:32mVOCÊ GANHOU!\033[m')
elif player == 'Papel' and cpu == 'Tesoura':
    print('\033[1:31mO COMPUTADOR VENCEU!\033[m')

elif cpu == 'Pedra' and player == 'Papel':
    print('\033[1:32mVOCÊ GANHOU!\033[m')
elif cpu == 'Pedra' and player == 'Tesoura':
    print('\033[1:31mO COMPUTADOR VENCEU!\033[m')
elif cpu == 'Papel' and player == 'Tesoura':
    print('\033[1:32mVOCÊ GANHOU!\033[m')

else:
    print('\033[1:34mEMPATE!\033[m')

print(f'Você escolheu {player} e o computador {cpu}.')

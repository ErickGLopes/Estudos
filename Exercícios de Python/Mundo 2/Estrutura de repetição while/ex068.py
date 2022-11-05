from random import randint
print('=-=' * 8)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-=' * 8)
num_player = num_pc = 0
opc_player = opc_pc = ''
cont = 0
while True:
    num_player = int(input('Digite um valor: '))
    opc_player = str(input('Par ou ímpar [P/I]: ')).strip().upper()
    if opc_player == 'P':
        opc_pc = 'I'
    if opc_player == 'I':
        opc_pc = 'P'
    num_pc = randint(1, 10)
    soma = num_player + num_pc
    print('-' * 24)
    print(f'Você jogou {num_player} e o computador {num_pc}. TOTAL DE {soma} ', end='')
    print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
    print('-' * 24)
    if opc_player == 'P':
        if soma % 2 == 0:
            print(f'Você GANHOU!')
            print('=-=' * 8)
            cont += 1
        else:
            print('Você PERDEU!')
            print('=-=' * 8)
            break
    if opc_player == 'I':
        if soma % 2 != 0:
            print('Você GANHOU!')
            print('=-=' * 8)
            cont += 1
        else:
            print('Você PERDEU!')
            print('=-=' * 8)
            break
print(f'GAME OVER! Você venceu {cont} vez(es)')

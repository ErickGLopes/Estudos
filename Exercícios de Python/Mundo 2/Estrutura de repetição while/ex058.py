from random import randint
random_num = randint(1, 9)
print('Sou o seu pc...\nAcabei de pensar em um número entre 0 e 10')
print('Você consegue acertar?')
acertou = False
cont_tentativas = 0
while not acertou:
    user_num = int(input('Digite o seu palpite: '))
    cont_tentativas += 1
    if user_num == random_num:
        acertou = True
    else:
        if user_num < random_num:
            print('Mais... Tente outra vez.')
        elif user_num > random_num:
            print('Menos... Tente outra vez.')
print(f'Você acertou! Depois de {cont_tentativas} tentativa(s)')

'''from random import randint
random_num = randint(1, 9)
print('Sou o seu pc...\nAcabei de pensar em um número entre 0 e 10')
print('Você consegue acertar?')
cont_tentativas = 0
acertou = False
while not acertou:
    user_num = int(input('Digite o seu palpite: '))
    cont_tentativas += 1
    if random_num == user_num:
        acertou = True
    else:
        if user_num < random_num:
            print('Mais... Tente uma outra vez.')
        elif user_num > random_num:
            print('Menos... Tente uma outra vez.')
print(f'Você acertou! Depois de {cont_tentativas} tentativa(s)')'''

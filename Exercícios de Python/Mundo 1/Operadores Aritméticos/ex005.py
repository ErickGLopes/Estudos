# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e o seu antecessor
print('\033[35m-=-\033[m' * 20)
print('\033[34mEsse programa lê um número e mostra o seu sucessor e o seu antecessor respectivamente\033[m')
print('\033[35m-=-\033[m' * 20)
num = int(input('Digite um número inteiro: '))
print('O sucessor deste número é {} e o seu antecessor é {}'.format(num+1, num-1))

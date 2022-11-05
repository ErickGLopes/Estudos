import random
import emoji

print('Olá! Pensei em um número entre 0 e 5. Tente adivinhar!')
n = random.randrange(0, 5)
num = int(input('Digite seu palpite: '))
if num == n:
    print(emoji.emojize('Parabéns! Você acertou! :polegar_para_cima:', language='pt'))
else:
    print(emoji.emojize('Que pena! Você errou :polegar_para_baixo:', language='pt'))

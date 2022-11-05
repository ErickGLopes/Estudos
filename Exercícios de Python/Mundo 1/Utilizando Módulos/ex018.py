# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, coseno e tangente.
from math import sin, cos, tan, radians
ang = float(input('Digite o valor do ângulo:'))
seno = sin(radians(ang))
coseno = cos(radians(ang))
tg = tan(radians(ang))
print('Os valores são:\n Seno de {}° = {:.3f}\n Coseno de {}° = {:.3f}\n Tangente de {}° = {:.3f}'.format(ang, seno, ang, coseno, ang, tg))
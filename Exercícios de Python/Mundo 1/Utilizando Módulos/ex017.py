from math import sqrt, pow
co = float(input('Digite o cateto oposto do triângulo retângualo:'))
ca = float(input('Agora digite o cateto adjacente do mesmo:'))
hip = sqrt(pow(co, 2) + pow(ca, 2))
print('A hipotenusa desse triângulo retângulo é {:.3f}'.format(hip))

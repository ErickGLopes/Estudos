a1 = int(input('Primeiro termo: '))
r = int(input('Razão da P.A: '))
n = 1
while n != 11:
    an = a1 + (n - 1) * r
    print(f'{an}', end='')
    print(' -> ' if n != 10 else '', end='')
    n += 1

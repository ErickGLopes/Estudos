from time import sleep
from datetime import date

print('\033[1:33m-=-\033[m' * 19)
print('\033[1:93mEste programa verifica se determinado ano é bissexto\033[m')
print('\033[1:33m-=-\033[m' * 19)
ano = int(input('\033[1:33mDigite o ano\033[m (coloque 0 para verificar o ano atual): '))
print('\033[1:37mVERIFICANDO...\033[m')
sleep(1.3)
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\033[1:32mO ano {} É BISSEXTO!\033[m'.format(ano))
else:
    print('\033[1:31mO ano {} NÃO é BISSEXTO!\033[m'.format(ano))

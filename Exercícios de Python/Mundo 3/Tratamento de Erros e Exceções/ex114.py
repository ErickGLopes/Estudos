import urllib.request as rq
import urllib

try:
    resp = rq.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print(f'\033[31mO site Pudim não está acessível no momento.\033[m')
else:
    print(f'\033[33mConsegui acessar o site Pudim com sucesso\033[m')


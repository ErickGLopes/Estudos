def escreva(txt):
    tam = len(txt) + 4
    print('~' * tam)
    print(f'{txt.center(tam)}')
    print('~' * tam)


escreva('Olá, mundo!')
escreva('Módulo 3 de Python')
escreva('Funções')
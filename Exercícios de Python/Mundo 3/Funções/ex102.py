def fatorial(n,show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f    


print(fatorial(5))


def limpa(opc=' '):
    from pyautogui import hotkey
    while True:
        opc = str(input('Deseja limpar o terminal?[S/n]: ')).strip().upper()
        if opc == 'S':
            hotkey('ctrl', 'l')
            break
        elif opc == 'N':
            break


limpa()

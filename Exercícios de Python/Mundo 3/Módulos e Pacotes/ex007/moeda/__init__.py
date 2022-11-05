def aumentar(i, n, opc=False):
    aum = i + i * n / 100
    if opc == True:
        aum = moeda(aum)
    return aum


def diminuir(i, n, opc=False):
    dim = i - i * n / 100
    if opc == True:
        dim = moeda(dim)
    return dim


def dobro(i, opc=False):
    d = i * 2
    if opc == True:
        d = moeda(d)
    return d


def metade(i, opc=False):
    m = i / 2
    if opc == True:
        m = moeda(m)
    return m


def moeda(v):
    v = f'R${v:.2f}'.replace('.',',')
    return v


def resumo(i, per1=10, per2=5):
    print('-' * 33)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 33)
    print(f'Preço analizado: \t{moeda(i)}')
    print(f'Dobro do preço: \t{dobro(i, True)}')
    print(f'Metade do preço: \t{metade(i, True)}')
    print(f'{per1}% de aumento: \t{aumentar(i, per1, True)}')
    print(f'{per2}% de redução: \t{diminuir(i, per2, True)}')
    print('-' * 33)
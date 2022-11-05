def voto(anoNasc):
    from datetime import date
    #anoNasc = int(input('Em que ano você nasceu?: '))
    anoAtual = date.today().year
    idade = anoAtual - anoNasc
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 <= idade < 18 or idade > 70:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


nasc = int(input('Digite seu ano de nascimento: '))
print(voto(nasc))


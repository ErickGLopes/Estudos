def notas(*x, sit=False):
    """
    -> Função para analisar as notas e situações de vários alunos. 
    :param x: uma ou mais notas dos alunos.
    :param sit: (opcional) adiciona a situação do aluno.
    :return: dicionário com várias informações sobre a turma.
    """
    lis = list()
    for y in x:
        lis.append(y)
    d = {'total': len(lis), 'maior': max(lis), 'menor': min(lis), 'média': sum(lis) / len(lis)}
    if sit:
        if d['média'] < 6:
            d['situação'] = 'RUIM'
        elif 6 <= d['média'] < 7:
            d['situação'] = 'RAZOÁVEL'
        elif d['média'] >= 7:
            d['situação'] = 'BOA'
    return d


resp = notas(8, 6, 8, 8, sit=True)
print(resp)

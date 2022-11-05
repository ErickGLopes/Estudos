aluno = dict()
aluno['nome'] = str(input('Digite o seu nome: '))
aluno['media'] = float(input('Digite a sua média: '))
if aluno['media'] >= 7:
    aluno['status'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['status'] = 'Recuperação'
else:
    aluno['status'] = 'Reprovado'
print('=-' * 17)
print(f'{"NOME":<13}{"MÉDIA":<10}{"SITUAÇÃO":>8}')
print('-' * 35)
print(f'{aluno["nome"]:<13}{aluno["media"]:<10.1f}{aluno["status"]:>8}')

from datetime import date
ano = int(input('Digite o seu ano de nascimento: '))
idade = date.today().year - ano

print(f'Quem nasceu em {ano} tem {idade} em {date.today().year}.')
if idade > 18:
    diferenca = idade - 18
    print(f'Já se passou {diferenca} ano(s) do seu alistamento.')
    print(f'Era para você ter se alistado em {date.today().year - diferenca}')
elif idade < 18:
    diferenca = 18 - idade
    print(f'Ainda falta(m) {diferenca} ano(s) para o seu alistamento')
    print(f'Seu alistamento será em {date.today().year + diferenca}')
else:
    print('Já é hora de se alistar no exército!')

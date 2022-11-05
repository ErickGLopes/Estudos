m_menos20 = 0
soma_idade = 0
media = 0
homemmaior_idade = 0
nome_maior = ''
for p in range(1, 5):
    print(f'----{p}ª PESSOA----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    soma_idade += idade
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    if p == 1 and sexo == 'M':
        homemmaior_idade = idade
        nome_maior = nome
    if sexo == 'M' and idade > homemmaior_idade:
        homemmaior_idade = idade
        nome_maior = nome
    if p == 1 and sexo == 'M' and idade < 20:
        m_menos20 += 1
media = soma_idade / 4
print(f'A média de idade do grupo é de {media:.2f} anos;')
print(f'O homem mais velho chama-se {nome_maior} e tem {homemmaior_idade} anos')
print(f'Há {m_menos20} mulheres com menos de 20 anos')

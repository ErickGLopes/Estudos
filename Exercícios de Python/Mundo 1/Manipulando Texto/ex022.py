from time import sleep

nome = str(input('Digite seu nome completo:')).strip()
print('Analisando seu nome...')
sleep(1.35)

print('- Seu nome em letras maiúsculas é: {}'.format(nome.upper()))
print('- Seu nome em letras minúsculas é: {}'.format(nome.lower()))
'''print('- Seu nome tem {} letras ao todo'.format(len(nome.replace(' ', ''))))'''
print('- Seu nome tem {} letras ao todo'.format(len(nome) - nome.count(' ')))

firstname = nome.split()
print('- Seu primeiro nome é {} e tem {} letras'.format(firstname[0], len(firstname[0])))

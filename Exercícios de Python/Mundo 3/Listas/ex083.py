exp = str(input('Digite a expressão: '))
cont = []
for simb in exp:
    if simb == '(':
        cont.append('(')
    elif simb == ')':
        if len(cont) > 0:
            cont.pop()
        else:
            cont.append(')')
            break
if len(cont) == 0:
    print('A sua expressão está válida!')
elif len(cont) > 0:
    print('A sua expressão está errada!')

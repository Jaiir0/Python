expressao = str(input('digite uma expressão: '))
parenteses= []

for simbolo in expressao:
    if simbolo == '(':
        parenteses.append(simbolo)
    elif simbolo == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(simbolo)
            break
    print(parenteses)
if len(parenteses) == 0:
    print('expressão correta')
else:
    print('expressao incorreta')


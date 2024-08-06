lista = [[],[]]
for c in range(1,8):
    numeros = int(input(f'Digite o {c}º valor: '))
    if numeros % 2 == 0:
        lista[0].append(numeros)
    else:
        lista[1].append(numeros)
print (f'pares: {sorted(lista[0])}')  
print (f'impares: {sorted(lista[1])}')  





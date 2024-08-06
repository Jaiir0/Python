lista = []
pares = []
impares = []

while True:
    num = int(input('digite um número: '))
    lista.append(num)
    continuar = input('quer continuar? [S/N]')
    if continuar in 'nN':
        break

for numero in lista:
    if numero == 0:
        ('não adicina 0')
    else:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)

print(f'a lista completa foi {lista}')
print(f'a lista de pares são: {pares}')
print(f'a lista de impares são: {impares}')

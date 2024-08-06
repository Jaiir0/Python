lista = []

while True:
    num = int(input('digite um número: '))
    lista.append(num)
    continuar = input('quer continuar? [S/N]')
    if continuar in 'nN':
        break
lista.sort(reverse=True)
print(f'os valores em ordem decrescente são: {lista}')
print(f'a lista possuia {len(lista)} algarismos')

if 5 in lista:
    print('o valor 5 faz parte da lista.')
else:
    print('o valor 5 não estava na lista')
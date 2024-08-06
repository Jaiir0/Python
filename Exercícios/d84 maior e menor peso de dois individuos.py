lista = []
pessoas = []
maior = menor = 0


while True:

    lista.append(input('nome: '))
    lista.append(float(input('peso: ')))

    if len(pessoas) == 0:
        maior = menor = lista[1]
    else:
       
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]  
    pessoas.append(lista[:])
    lista.clear()
    continuar = input('quer continuar? [S/N]')
    if continuar in 'nN':
        break 


print(f'numero de pessoas foi: {len(pessoas)}')
print(f'O maior peso foi {maior}Kg de ',end = ' ')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]',end = ' ')
print()
print(f'O menor peso foi {menor}Kg  de',end = ' ')
for p in pessoas:
    if p[1] == menor:
        print(f' [{p[0]}]',end = ' ')


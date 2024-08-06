
valores = []
minimo = 0
maximo = 0
for c in range(0,5):
    valores.append(int(input(f'digite uma valor para posição {c}: ')))
    if valores == 0:
        minimo = 0
        maximo = 0
    else:
        maximo = max(valores)
        minimo = min(valores)
print('=-='*30)
print(f'Os valores escolhidos foram: {valores} \nvalor mininmo: {minimo}  valor maximo: {maximo}')
print('=-='*30)
if minimo == 0 and maximo == 0:
    print('O maior valor e menor foi 0 em todas posições')

else:
    print(f'O maior valor digitado foi {maximo} nas posições: ',end = '')
    for n,v in enumerate(valores):
        if v == maximo:
            print(f'{n},' ,end = '')
    print()
    print(f'O menor valor digitador foi {minimo} nas posicões: ',end = '')    
    for n,v in enumerate(valores):
        if v == minimo:
            print(f'{n},',end = '')
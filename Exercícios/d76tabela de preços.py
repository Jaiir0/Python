tabela = ('Banana', 2.00, 'Maça',1.50, 'Melão',10.50, 'Uva',4.20) 

print('-'*35)
print(f'{'TABELA DE PREÇOS':^30}')
print ('-'*35)

for pos in range (0,(len(tabela))):
    if pos % 2 == 0:
        print (f'{tabela[pos]:.<30}',end = '')
    else:
        print (f'R$ {tabela[pos]:>3.2f}')
print ('-'*35)
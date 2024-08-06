num = (int(input('digite um número')),
       int(input('digite um número')),
       int(input('digite um número')),
       int(input('digite um número')))

print(f'Os número que você digitou foram: {num}')



if 9 in num:
    print (f'O número 9 apareceu {num.count(9)} vezes')
else:
    print('O número 9 não estava presente nos números escolhidos. ')
if 3 in num:
    print(f'A posição do número 3 foi: {num.index(3)+1}')
else:
    print('O número 3 não estava entre os números escolhidos')

print ('Os número pares digitados foram: ',end = ' ')

for numero in num:
    if numero % 2 == 0:
        print (numero,end = ' ')
     

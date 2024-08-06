valores = []

while  True: 
    num = int(input('digite um valor: '))

    if num not in valores:
        valores.append(num)
        print('O valor foi adicionado a lista com sucesso! ')

   
    else:
        print('Não foi possivel adicionar o valor na lista. ')

    continuar =input('Quer continuar? [S/N] ')
    if continuar in 'Nn':
        break


valores.sort()
print(f'Os valores em ordem crescentes foram: {valores}')

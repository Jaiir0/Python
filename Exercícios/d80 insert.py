lista = []


for c in range (0,5):
    num = int(input('digite um número: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print('adicionado ao final da lista...')
    else:
        posicao = 0
        while posicao <= len(lista):
            if num <= lista[posicao]:
                lista.insert(posicao,num)
                print(f'adiciona na posição {posicao} da lista...')
                break
            posicao += 1


print('=-'*30)
print(f'os valores digitados foram: {lista}')

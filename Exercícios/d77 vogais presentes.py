
tupla = ('aprender','python','linguagem','arroz','camarao','feijao')
vogais = ('a','e','i','o','u')

for palavra in tupla:

    print (f'\n Na palavra {palavra} temos ',end = '')
    for letra in palavra:
        if (letra) in 'aeiou':
            print (f'{letra},',end = '' )
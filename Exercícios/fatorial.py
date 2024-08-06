num = int(input('digite um número inteiro para fazer o fatorial: '))
x = 0
prod = 1
while x < num:
    x = x + 1
    prod = prod * x
    
    print (x ,end='-' )
print (f' Multiplicados resultou em: {prod} ')
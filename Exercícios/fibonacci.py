termos = int(input('Quantos termos você quer que seja exibido? '))
pri = 0
seg = 1
c = 3

print (pri,seg, end= ' ')
while c <= termos:
    soma = pri + seg
    print (soma, end= ' ')
    pri = seg
    seg = soma 
    c += 1

    
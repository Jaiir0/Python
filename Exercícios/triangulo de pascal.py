linha = [1]
print(*linha)
for i in range(1, 20):
    
    nova_linha = []
    nova_linha.append(1)  
    
    for j in range(1, i):
        nova_linha.append(linha[j-1] + linha[j])

    nova_linha.append(1)
    print(*nova_linha)
    linha = nova_linha
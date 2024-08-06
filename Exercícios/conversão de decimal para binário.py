valor = int(input('Digite um número para converter em binário: '))
binario = []

for c in range(7,-1,-1):

    if 2**c <= valor:
        valor -= 2**c
        binario.append(1)
    else:
        binario.append(0)

print(*binario)
lista = [[0,0,0],[0,0,0],[0,0,0],]

for l in range (0,3):
    for c in range(0,3):
        lista[l][c] = (int(input(f'digite um valo para [{l},{c}] ')))

for l in range (0,3):
    for c in range(0,3):
        print(f'[{lista[l][c]:^5}]',end = ' ')
    print()
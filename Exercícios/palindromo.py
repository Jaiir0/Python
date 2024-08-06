#Maior idade com 21 anos

maior = 0
menor = 0

for c in range (0,7):
    idade = int(input('Diga o ano que você nasceu: '))
    if idade <=2003:
        maior += 1
    else:
        menor += 1

print (f' {maior} pessoas são maiores de idade (+21) \n {menor} pessoas são menores de idade ')
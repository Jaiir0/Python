tabela = ('Athletico-PR','Bahia','Flamengo','Botafogo','São Paulo','Cruzeiro','Atlético-MG','Bragantino',
'Palmeiras','Internacional','Fortaleza','Grêmio','Vasco','Criciúma','Juventude','Corinthians','Fluminense',
'Vitória','Atlético-GO','Cuiabá')
print ('Tabela do Brasileirão')
print (tabela)

print ('=-='*28)

print ('Os 5 primeiros colocados foram: \n ')
for times in tabela[:5]:
   print (times)

print ('=-='*28)

print('Os 5 ultimos colocados foram: \n')
for times in tabela [-4:]:
   print (times)

print ('=-='*28)

print (sorted(tabela))

print ('=-='*28)

vasco_colocacao = tabela.index('Vasco')+1
print (f'O Vasco está na {vasco_colocacao}º colocação')

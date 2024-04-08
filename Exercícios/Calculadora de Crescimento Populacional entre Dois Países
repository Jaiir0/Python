paisA = int(input('Informe a população da país A: '))
taxaA =  float(input('Informe a taxa anual de crescimento populacional do pais A: '))
paisB = int(input('Informe a população da país B: '))
taxaB = float(input('Informe a taxa anual de crescimento populacional do pais B: '))
ano = 0

while paisA <= paisB:
    paisA = int (paisA * (taxaA/100)) + paisA
    paisB = int  (paisB * (taxaB/100)) + paisB
    ano = ano + 1

    print (f'No ano {ano}')
    print (f'População do país A: {paisA}')
    print (f'População do país B: {paisB} \n ')
    print (f'=-='*29)

print (f'Foram necessários {ano} anos para o país A ultrapassar a população do país B')

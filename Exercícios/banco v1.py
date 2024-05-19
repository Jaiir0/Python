menu = '''
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''

saldo = 0
limite = 0
extrato = []
numero_de_saques = 0


while True:
    escolha = int(input(menu))

    if escolha ==  1:
        deposito = float(input('Informe o valor que deseja depositar: '))

        if deposito > 0:
            saldo += deposito
            extrato.append(f'Deposito: R$ {deposito:.2f}')
        else:
            print ('Por favor, insira um valor de depósito valido ')

    
    elif  escolha == 2:
        saque = float(input('Informe quanto deseja sacar: '))
        
        if numero_de_saques >= 3:
            print('você atingigiu o limite de saques por dia.')
           
        else:

            if saque <= 500 and saque <= saldo :
                extrato.append(f'Saque: R$ {saque:.2f}')
                numero_de_saques += 1
                saldo -= saque
               

            else:
                print ('O valor do saque e maior que seu limite.')

    elif  escolha == 3:
        print('---------------------------------- \n EXTRATO: \n')
        print ('\n'.join (extrato))
        print ('----------------------------------')
       
    elif  escolha == 4:
        break
    
    else:
        print ('Operação inválida, por favor selecione novamente a operacão desejada.')



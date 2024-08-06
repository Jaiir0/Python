menu = '''
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''

saldo = 0
extrato = []
numero_de_saques = 0

def depositar(valor, saldo, extrato):
    
    if valor > 0:
        saldo += valor
        extrato.append(f'Depósito: R$ {valor:.2f}')
        print("Depósito realizado com sucesso!")
    else:
        print("Valor inválido para depósito.")
    return saldo, extrato

def sacar(valor, saldo, extrato, numero_de_saques):
    
    if numero_de_saques >= 3:
        print("Você atingiu o limite de saques por dia.")
    else:
        if valor <= 500 and valor <= saldo:
            extrato.append(f'Saque: R$ {valor:.2f}')
            numero_de_saques += 1
            saldo -= valor
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente ou valor de saque inválido.")
    return saldo, extrato, numero_de_saques

def exibir_extrato(extrato):
    """Exibe o extrato da conta."""
    print("---------------------------------- \n EXTRATO: \n")
    if not extrato:
        print("Não há movimentações na conta.")
    else:
        print('\n'.join(extrato))
    print("----------------------------------")

while True:
    escolha = int(input(menu))

    if escolha == 1:
        valor_deposito = float(input('Informe o valor que deseja depositar: '))
        saldo, extrato = depositar(valor_deposito, saldo, extrato)

    elif escolha == 2:
        valor_saque = float(input('Informe quanto deseja sacar: '))
        saldo, extrato, numero_de_saques = sacar(valor_saque, saldo, extrato, numero_de_saques)

    elif escolha == 3:
        exibir_extrato(extrato)

    elif escolha == 4:
        break

    else:
        print ('Operação inválida, por favor selecione novamente a operação desejada.')
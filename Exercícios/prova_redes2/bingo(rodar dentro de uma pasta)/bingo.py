#Jairo Bezerra = 20241014050017

import random  
import time

filename = 'cartelas.txt'

menu =  '''
                [1] Gerar Cartelas
                [2] Salvar Cartelas
                [3] Ler Cartelas
                [4] Imprimir Cartelas
                [5] Sorteio Do Bingo
                [6] Sair
                '''

def armazena_cartela():
    try:
        cartela = [
            sorted(random.sample(range(1, 16), 5)),
            sorted(random.sample(range(16, 31), 5)),
            sorted(random.sample(range(31, 46), 5)),
            sorted(random.sample(range(46, 61), 5)),
            sorted(random.sample(range(61, 76), 5))
        ]
        return cartela
    except Exception as e:
        print(f'Erro ao gerar a cartela : {e}')

def gerar_cartelas():
    try:
        nume = int(input('Digite o número de cartelas que você quer gerar: '))
        while nume > 10000:
            print('O número máximo de cartelas que podem ser geradas é 10.000. Tente novamente.')
            nume = int(input('Digite o número de cartelas que você quer gerar (máximo 10.000): '))
        while nume <0:
            print(f'Erro Digite um valor positivo valido.')
            nume = int(input('Digite o número de cartelas que você quer gerar: '))

        cartelas = {}

        for k in range(1, nume + 1):
            cartelas[k] = armazena_cartela()

        return cartelas
    except (ValueError,NameError):
        print('Erro. Por favor Digite um número')
    except Exception as e:
        print(f'Erro inesperado ao gerar cartelas: {e}')

def salvar_cartelas(cartelas):
    if len(cartelas) > 0:
        try:
            with open(filename, 'w') as arquivo:
                arquivo.write('{\n')
                for chave, cartela in cartelas.items():
                    arquivo.write(f'{chave}: {cartela},\n')
                arquivo.write('}\n')
            print(f'Cartelas salvas no arquivo {filename}.')
        except IOError as e:
            print(f'Erro ao salvar as cartelas: {e}')
    else:
        print('Não há cartelas armazenadas ainda.')


def ler_cartelas():
    try:
        arquivo = open(filename, 'r')
        conteudo = arquivo.read()
        arquivo.close()
        if not conteudo:
            print('Não há cartelas salvas para serem lidas')
        else:
            print('\nConteúdo do arquivo de cartelas:')
            print(conteudo)
    except FileNotFoundError:
        print(f'O arquivo {filename} não foi encontrado.')
    except IOError as e:
        print(f'Erro ao ler arquivo: {e}')

def imprimir_cartela():
    try:
        arquivo = open(filename,'r')
        conteudo = arquivo.read()
        arquivo.close()
        if len(conteudo) == 0:
            print('O arquivo que armazena as cartelas está vazio.')

        else:

            numero_Da_cartela = int(input('Qual cartela você deseja visualizar? '))
            if numero_Da_cartela not in cartelas:
                print(f'Cartela {numero_Da_cartela} não encontrada.')
                return
            cartela = cartelas[numero_Da_cartela]

            print('+----+----+----+----+----+')
            print(f'| Cartela: {numero_Da_cartela:05d}         |')
            print('+----+----+----+----+----+')
            print('| B  | I  | N  | G  | O  |')
            print('+----+----+----+----+----+')
            for linha in cartela:
                print(f'| {linha[0]:2} | {linha[1]:2} | {linha[2]:2} | {linha[3]:2} | {linha[4]:2} |')
                print('+----+----+----+----+----+')
    except (ValueError,NameError):
        print('Entrada inválida, insira um número.')
    except FileNotFoundError:
        print(f'O arquivo {filename} não foi encontrado.')
    except IOError as e:
        print(f'Erro ao ler o arquivo: {e}')

def sorteio():

    if len(cartelas) == 0:
            print("Nenhuma cartela foi gerada ou carregada. Por favor, gere ou carregue cartelas antes de realizar o sorteio.")
            return
    try:
        numeros_sorteados = set(random.sample(range(1, 76), 24))
        print(f'Números sorteados: {numeros_sorteados}')
        while True:
            for chave, carte in cartelas.items():
                if all(num in numeros_sorteados for linha in carte for num in linha):
                    print("Cartela vencedora:")

                    print('+----+----+----+----+----+')
                    print(f'| Cartela: {chave:05d}         |')
                    print('+----+----+----+----+----+')
                    print('| B  | I  | N  | G  | O  |')
                    print('+----+----+----+----+----+')
                    for linha in carte:
                        print(f'| {linha[0]:2} | {linha[1]:2} | {linha[2]:2} | {linha[3]:2} | {linha[4]:2} |')
                        print('+----+----+----+----+----+')
                    print()
                    print(f"Números sorteados no total: {sorted(numeros_sorteados)}")
                    return chave, numeros_sorteados


            novo_numero = random.randint(1, 75)
            if novo_numero not in numeros_sorteados:
                time.sleep(2)
                print(f'Número sorteado: {novo_numero}')
                numeros_sorteados.add(novo_numero)
    except Exception as e:
        print(f'Erro no sorteio {e}')

cartelas = {}
try:
    while True:
        print(menu)
        try:
            opcao = int(input('Escolha uma Opção: '))
        except(NameError,ValueError):
            print('Opção inválida. Tente novamente')
            continue


        if opcao == 1:
            cartelas = gerar_cartelas()
        elif opcao == 2:
            salvar_cartelas(cartelas)
        elif opcao == 3:
            ler_cartelas()
        elif opcao == 4:
            imprimir_cartela()
        elif opcao == 5:
            sorteio()
        elif opcao == 6:
            break

        else:
            print('Opção inválida. Tente novamente.')
except KeyboardInterrupt:
    print("\nOperação interrompida pelo usuário.")
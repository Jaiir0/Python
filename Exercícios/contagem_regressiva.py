import time
contagem= int(input('Digite o tempo a ser cronometrado: ')) +1
for c in range (0,contagem):
    contagem -= 1
    time.sleep(1)
    print (contagem)
